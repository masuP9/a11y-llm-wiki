#!/usr/bin/env python3
"""前回実行以降の差分を sources.yml に従って収集し、raw/<today>/ に書き出す。

出力:
  raw/<today>/collected.json  機械可読の全データ
  raw/<today>/collected.md    LLM が読むための要約 (wiki 更新の入力)
  state/last_run.json         次回の since
  state/seen_repos.json       発見済みリポジトリ (重複報告を防ぐ)

環境変数:
  GITHUB_TOKEN  GitHub API 用 (Actions では自動で入る)
  SINCE         YYYY-MM-DD を指定すると state を無視してその日から収集
  DRY_RUN=1     state を更新しない
"""
from __future__ import annotations

import datetime as dt
import email.utils
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = "a11y-llm-wiki-collector (+https://github.com/masuP9/a11y-llm-wiki)"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
FAILURES: list[str] = []


# ------------------------------------------------------------------ http
def http_get(url: str, *, accept: str | None = None, method: str = "GET",
             retries: int = 2) -> tuple[int, bytes, dict]:
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    if TOKEN and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {TOKEN}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    req = urllib.request.Request(url, headers=headers, method=method)
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as res:
                return res.status, res.read(), dict(res.headers)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and attempt < retries and "api.github.com" in url:
                reset = e.headers.get("X-RateLimit-Reset")
                wait = max(5, min(90, int(reset) - int(time.time()))) if reset else 30
                time.sleep(wait)
                continue
            return e.code, e.read() if e.fp else b"", dict(e.headers or {})
        except Exception as e:  # noqa: BLE001
            if attempt < retries:
                time.sleep(3)
                continue
            return 0, str(e).encode(), {}
    return 0, b"", {}


def gh(path: str, params: dict | None = None) -> object | None:
    url = "https://api.github.com" + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    status, body, _ = http_get(url, accept="application/vnd.github+json")
    if status != 200:
        FAILURES.append(f"GitHub API {status}: {path} {params or ''}")
        return None
    return json.loads(body)


def gh_paged(path: str, params: dict, max_pages: int) -> list:
    out: list = []
    for page in range(1, max_pages + 1):
        data = gh(path, {**params, "per_page": 100, "page": page})
        if not isinstance(data, list):
            break
        out.extend(data)
        if len(data) < 100:
            break
    return out


# ------------------------------------------------------------------ helpers
def iso(d: dt.datetime) -> str:
    return d.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_time(s: str | None) -> dt.datetime | None:
    if not s:
        return None
    s = s.strip()
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        pass
    try:
        return email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        return None


def excerpt(text: str | None, n: int = 400) -> str:
    if not text:
        return ""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:n] + ("…" if len(text) > n else "")


def hit(text: str, keywords: list[str]) -> bool:
    t = text.lower()
    return any(k.lower() in t for k in keywords)


# ------------------------------------------------------------------ collectors
def collect_repo(src: dict, since: dt.datetime, max_pages: int) -> list[dict]:
    repo = src["repo"]
    labels = src.get("labels") or []
    keywords = src.get("keywords") or []
    base = {"state": "all", "since": iso(since), "sort": "updated", "direction": "desc"}
    raw: dict[int, dict] = {}
    if labels:
        for label in labels:
            for it in gh_paged(f"/repos/{repo}/issues", {**base, "labels": label}, max_pages):
                raw[it["number"]] = it
    if keywords:
        for it in gh_paged(f"/repos/{repo}/issues", base, max_pages):
            if hit(it.get("title", ""), keywords):
                raw[it["number"]] = it
    if not labels and not keywords:
        for it in gh_paged(f"/repos/{repo}/issues", base, max_pages):
            raw[it["number"]] = it

    items = []
    for it in raw.values():
        is_pr = "pull_request" in it
        created = parse_time(it.get("created_at"))
        closed = parse_time(it.get("closed_at"))
        merged = parse_time((it.get("pull_request") or {}).get("merged_at"))
        if merged and merged >= since:
            event = "merged"
        elif closed and closed >= since:
            event = "closed"
        elif created and created >= since:
            event = "opened"
        else:
            event = "updated"
        items.append({
            "repo": repo,
            "number": it["number"],
            "kind": "PR" if is_pr else "Issue",
            "event": event,
            "title": it.get("title", ""),
            "url": it.get("html_url"),
            "user": (it.get("user") or {}).get("login"),
            "labels": [l["name"] for l in it.get("labels", [])],
            "comments": it.get("comments", 0),
            "created_at": it.get("created_at"),
            "updated_at": it.get("updated_at"),
            "body": excerpt(it.get("body")) if event in ("opened", "merged") else "",
        })
    order = {"merged": 0, "opened": 1, "closed": 2, "updated": 3}
    items.sort(key=lambda x: (order[x["event"]], -x["comments"]))
    return items


def collect_releases(repo: str, since: dt.datetime) -> list[dict]:
    data = gh(f"/repos/{repo}/releases", {"per_page": 10})
    out = []
    for r in data or []:
        pub = parse_time(r.get("published_at"))
        if pub and pub >= since and not r.get("draft"):
            out.append({
                "repo": repo, "tag": r.get("tag_name"), "name": r.get("name"),
                "url": r.get("html_url"), "published_at": r.get("published_at"),
                "prerelease": r.get("prerelease"), "body": excerpt(r.get("body"), 800),
            })
    return out


def collect_minutes(groups: list[dict], since: dt.datetime, until: dt.datetime) -> list[dict]:
    out = []
    day = since.date()
    while day <= until.date():
        for g in groups:
            url = f"https://www.w3.org/{day:%Y/%m/%d}-{g['name']}-minutes.html"
            status, _, _ = http_get(url, method="HEAD", retries=0)
            if status == 405:
                status, _, _ = http_get(url, retries=0)
            if status == 200:
                out.append({"group": g["label"], "date": day.isoformat(), "url": url})
            elif status not in (404, 410):
                FAILURES.append(f"minutes {status}: {url}")
        day += dt.timedelta(days=1)
    return out


def _text(el: ET.Element | None) -> str:
    return (el.text or "").strip() if el is not None else ""


def collect_feed(src: dict, since: dt.datetime) -> list[dict]:
    status, body, _ = http_get(src["url"])
    if status != 200:
        FAILURES.append(f"feed {status}: {src['name']} {src['url']}")
        return []
    try:
        root = ET.fromstring(body)
    except ET.ParseError as e:
        FAILURES.append(f"feed parse error: {src['name']} ({e})")
        return []
    atom = "{http://www.w3.org/2005/Atom}"
    entries = []
    for item in root.iter("item"):  # RSS
        entries.append({
            "title": _text(item.find("title")),
            "url": _text(item.find("link")),
            "date": _text(item.find("pubDate")) or _text(item.find("{http://purl.org/dc/elements/1.1/}date")),
            "summary": _text(item.find("description")),
        })
    for item in root.iter(f"{atom}entry"):  # Atom
        link = item.find(f"{atom}link[@rel='alternate']")
        if link is None:
            link = item.find(f"{atom}link")
        entries.append({
            "title": _text(item.find(f"{atom}title")),
            "url": link.get("href") if link is not None else "",
            "date": _text(item.find(f"{atom}published")) or _text(item.find(f"{atom}updated")),
            "summary": _text(item.find(f"{atom}summary")) or _text(item.find(f"{atom}content")),
        })
    kws = src.get("keywords") or []
    out = []
    for e in entries:
        d = parse_time(e["date"])
        if not d or d < since:
            continue
        if kws and not hit(e["title"] + " " + e["summary"], kws):
            continue
        out.append({"feed": src["name"], "group": src.get("group", ""), "title": e["title"],
                    "url": e["url"], "date": iso(d),
                    "summary": excerpt(re.sub(r"<[^>]+>", " ", e["summary"]), 300)})
    return out


def collect_discovery(cfg: dict, since: dt.datetime, seen: set[str]) -> tuple[list, list]:
    s = since.date().isoformat()
    min_stars = cfg.get("min_stars", 0)
    new: dict[str, dict] = {}
    for q in cfg.get("queries", []):
        data = gh("/search/repositories", {"q": q.format(since=s), "sort": "stars",
                                           "order": "desc", "per_page": cfg.get("per_query", 30)})
        time.sleep(2.5)  # search API: 30 req/min
        for r in (data or {}).get("items", []):
            name = r["full_name"]
            if name in seen or r.get("fork") or r["stargazers_count"] < min_stars:
                continue
            new[name] = _repo_summary(r)
    rising: dict[str, dict] = {}
    for q in cfg.get("rising", []):
        data = gh("/search/repositories", {"q": q.format(since=s), "sort": "updated",
                                           "order": "desc", "per_page": 20})
        time.sleep(2.5)
        for r in (data or {}).get("items", []):
            rising[r["full_name"]] = _repo_summary(r)
    return (sorted(new.values(), key=lambda x: -x["stars"]),
            sorted(rising.values(), key=lambda x: -x["stars"]))


def _repo_summary(r: dict) -> dict:
    return {"repo": r["full_name"], "url": r["html_url"], "stars": r["stargazers_count"],
            "description": excerpt(r.get("description"), 200), "topics": r.get("topics", []),
            "language": r.get("language"), "created_at": r.get("created_at"),
            "pushed_at": r.get("pushed_at")}


def collect_awesome(src: dict, since: dt.datetime) -> list[dict]:
    repo, path = src["repo"], src.get("path", "README.md")
    commits = gh(f"/repos/{repo}/commits", {"since": iso(since), "path": path, "per_page": 30})
    out = []
    for c in commits or []:
        detail = gh(f"/repos/{repo}/commits/{c['sha']}")
        for f in (detail or {}).get("files", []):
            for line in (f.get("patch") or "").splitlines():
                if line.startswith("+") and not line.startswith("+++") and "](http" in line:
                    out.append({"repo": repo, "line": line[1:].strip()[:300],
                                "commit": c.get("html_url")})
    return out


# ------------------------------------------------------------------ render
def render_md(d: dict) -> str:
    L = [f"# Collected: {d['since'][:10]} 〜 {d['until'][:10]}", ""]
    L += ["> scripts/collect.py の自動出力。/weekly コマンドの入力。", ""]

    L += ["## 1. 標準リポジトリの動き", ""]
    by_group: dict[str, list] = {}
    for it in d["spec_items"]:
        by_group.setdefault(it["group"], []).append(it)
    for group, items in by_group.items():
        L += [f"### {group}", ""]
        for it in items:
            meta = f"{it['event']} · {it['kind']} · @{it['user']} · 💬{it['comments']}"
            if it["labels"]:
                meta += " · " + ", ".join(it["labels"][:5])
            L.append(f"- [{it['repo']}#{it['number']}]({it['url']}) {it['title']}  \n  {meta}")
            if it["body"]:
                L.append(f"  > {it['body']}")
        L.append("")
    if not d["spec_items"]:
        L += ["(なし)", ""]

    L += ["## 2. 議事録", ""]
    L += [f"- {m['date']} {m['group']}: {m['url']}" for m in d["minutes"]] or ["(なし)"]
    L.append("")

    L += ["## 3. フィード", ""]
    L += [f"- [{f['feed']}] [{f['title']}]({f['url']}) ({f['date'][:10]})  \n  {f['summary']}"
          for f in d["feeds"]] or ["(なし)"]
    L.append("")

    L += ["## 4. リリース", ""]
    L += [f"- [{r['repo']} {r['tag']}]({r['url']}){' (pre)' if r['prerelease'] else ''} ({r['published_at'][:10]})  \n  {r['body'][:300]}"
          for r in d["releases"]] or ["(なし)"]
    L.append("")

    L += ["## 5. 新規リポジトリ", ""]
    L += [f"- [{r['repo']}]({r['url']}) ★{r['stars']} {r['language'] or ''} — {r['description']}  \n  topics: {', '.join(r['topics'][:8])}"
          for r in d["discovered"]] or ["(なし)"]
    L += ["", "### 活発な既存リポジトリ (stars≥200, 期間内に push)", ""]
    L += [f"- [{r['repo']}]({r['url']}) ★{r['stars']} — {r['description']}" for r in d["rising"]] or ["(なし)"]
    L.append("")

    L += ["## 6. Awesome 系リストへの追加", ""]
    L += [f"- ({a['repo']}) {a['line']}" for a in d["awesome"]] or ["(なし)"]
    L.append("")

    L += ["## 取得失敗", ""]
    L += [f"- {x}" for x in d["failures"]] or ["(なし)"]
    L.append("")
    return "\n".join(L)


# ------------------------------------------------------------------ main
def main() -> int:
    cfg = yaml.safe_load((ROOT / "sources.yml").read_text())
    defaults = cfg.get("defaults", {})
    state_dir = ROOT / "state"
    state_dir.mkdir(exist_ok=True)
    last_run_f = state_dir / "last_run.json"
    seen_f = state_dir / "seen_repos.json"

    now = dt.datetime.now(dt.timezone.utc)
    if os.environ.get("SINCE"):
        since = dt.datetime.fromisoformat(os.environ["SINCE"]).replace(tzinfo=dt.timezone.utc)
    elif last_run_f.exists():
        since = parse_time(json.loads(last_run_f.read_text())["until"])
    else:
        since = now - dt.timedelta(days=defaults.get("window_days", 7))
    seen = set(json.loads(seen_f.read_text())) if seen_f.exists() else set()
    max_pages = defaults.get("max_pages", 3)

    print(f"collect: {iso(since)} .. {iso(now)}", file=sys.stderr)
    spec_items = []
    for src in cfg.get("spec_repos", []):
        for it in collect_repo(src, since, max_pages):
            it["group"] = src.get("group", "")
            spec_items.append(it)
        print(f"  repo {src['repo']}", file=sys.stderr)

    releases = []
    for repo in [s["repo"] for s in cfg.get("spec_repos", [])] + cfg.get("release_watch", []):
        releases += collect_releases(repo, since)

    minutes = collect_minutes(cfg.get("minutes", []), since, now)
    feeds = [e for src in cfg.get("feeds", []) for e in collect_feed(src, since)]
    discovered, rising = collect_discovery(cfg.get("discovery", {}), since, seen)
    awesome = [a for src in cfg.get("awesome", []) for a in collect_awesome(src, since)]

    data = {"since": iso(since), "until": iso(now), "spec_items": spec_items,
            "minutes": minutes, "feeds": feeds, "releases": releases,
            "discovered": discovered, "rising": rising, "awesome": awesome,
            "failures": FAILURES}

    out_dir = ROOT / "raw" / now.date().isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "collected.json").write_text(json.dumps(data, ensure_ascii=False, indent=2))
    (out_dir / "collected.md").write_text(render_md(data))
    print(f"wrote {out_dir.relative_to(ROOT)}  items={len(spec_items)} minutes={len(minutes)} "
          f"feeds={len(feeds)} releases={len(releases)} new_repos={len(discovered)} "
          f"failures={len(FAILURES)}", file=sys.stderr)

    if not os.environ.get("DRY_RUN"):
        last_run_f.write_text(json.dumps({"since": iso(since), "until": iso(now),
                                          "dir": str(out_dir.relative_to(ROOT))}, indent=2) + "\n")
        seen |= {r["repo"] for r in discovered}
        seen_f.write_text(json.dumps(sorted(seen), indent=0) + "\n")
    # GitHub Actions の後続ステップ用
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            fh.write(f"dir={out_dir.relative_to(ROOT)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
