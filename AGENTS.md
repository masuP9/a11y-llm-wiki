# a11y-llm-wiki — エージェント向け指示

このリポジトリは、Web アクセシビリティの標準化動向と GitHub 上のアクセシビリティ関連エコシステムを追跡する LLM-Wiki である。
Karpathy の [LLM-Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) と、
Jxck の [tc39-llm-wiki](https://blog.jxck.io/entries/2026-06-29/tc39-llm-wiki.html) の方式に倣う。

- 人間はソースを選び、問いを立てる。LLM は要約・相互リンク・整合性維持を担う。
- wiki は毎週の Ingest と、オンデマンドの Ingest / Query の File back で育てる。全データを最初から解析しない。

## ディレクトリ

| パス | 役割 | 書き換え |
|---|---|---|
| `sources.yml` | 収集ソース定義 | 人間 / `/lint` で提案 |
| `scripts/collect.py` | 前回以降の差分を収集 | 人間 |
| `raw/<YYYY-MM-DD>/collected.{md,json}` | 収集結果 (不変のソース) | **編集禁止** |
| `state/` | 前回実行日時・既出リポジトリ | スクリプトのみ |
| `wiki/index.md` | 全ページの目次 | LLM |
| `wiki/log.md` | 追記専用の作業ログ | LLM (追記のみ) |
| `wiki/weekly/<YYYY>-W<ww>.md` | 週次ダイジェスト | LLM |
| `wiki/specs/<slug>.md` | 仕様ごとのページ | LLM |
| `wiki/topics/<slug>.md` | 仕様横断のトピック (Jxck の Families に相当) | LLM |
| `wiki/people/<github-login>.md` | 編集者・主要参加者 | LLM |
| `wiki/repos/<owner>__<name>.md` | エコシステムの注目リポジトリ | LLM |
| `wiki/repos/discovered.md` | 新規発見リポジトリの台帳 | LLM (追記) |

## ページの書式

すべて日本語。仕様名・API名・ロール名・SC 番号などの固有名は原語のまま書く。

各 wiki ページの先頭には YAML frontmatter を置く。

```yaml
---
title: WCAG 3.0
type: spec | topic | person | repo | weekly
status: (spec のみ) ED | WD | CR | PR | REC | Note | CG | 不明
updated: 2026-09-30
sources: [raw/2026-09-30]
---
```

本文のルール:

1. 事実には必ず一次ソースへのリンクを付ける (Issue/PR/議事録/仕様の URL)。リンクの無い記述は書かない。
2. 推測は `（推測）` と明記する。議論中の事項を決定事項として書かない。
3. 人物は初出で `[[people/<login>]]` にリンクする。所属は議事録や W3C の参加者ページで確認できた場合のみ書く。
4. spec ページには「現状」「最近の動き (新しい順・日付付き)」「未解決の論点」「関連」の節を持つ。時系列が重要なら mermaid の timeline を使う。
5. ページ間リンクは `[[specs/wcag-3]]` の形式で書く (Obsidian 互換)。
6. 同じ事実を複数ページに重複して書かない。詳細は 1 ページに置き、他からはリンクする。

## コマンド

`.claude/commands/` に定義がある。口頭で同じことを頼まれても同じ手順で行う。

- `/weekly` — 最新の `raw/` を読み、wiki を更新し、週次ダイジェストを書く (GitHub Actions から毎週実行)
- `/ingest <対象>` — 仕様やトピックを深掘りして wiki ページを作る・育てる (オンデマンド)
- `/lint` — 矛盾・リンク切れ・古い記述・取得失敗ソースを点検する
- `/query <質問>` — wiki から答える。価値のある答えは wiki に File back する

## 判断基準: 何を重要とみなすか

高: 仕様の新バージョン公開 (WD/CR/REC)、SC やロールの追加・削除・意味変更、ブラウザの実装・出荷、
    AGWG/ARIA WG の決議 (RESOLUTION)、水平レビューでの a11y-needs-resolution、主要ツールのメジャーリリース
中: 活発な議論 (コメント多数) の新規 Issue、APG パターンの追加・改訂、Interop の focus area 変更
低: 編集上の修正、typo、CI、依存更新 — 週次ダイジェストでは件数だけ示すか省く

## 禁止事項

- `raw/` と `state/` を編集しない。
- 収集結果に無い「今週の出来事」を創作しない。WebFetch で確認した内容は出典 URL を付ける。
- 外部に向けた操作 (Issue へのコメント、PR 作成など) を wiki 更新の範囲外で行わない。
