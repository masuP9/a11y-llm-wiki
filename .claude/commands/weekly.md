---
description: 最新の収集結果から wiki を更新し、週次ダイジェストを書く
argument-hint: "[raw/<YYYY-MM-DD> (省略時は state/last_run.json の dir)]"
---

# /weekly

入力: `$ARGUMENTS` が指定されていればその `raw/` ディレクトリ。無ければ `state/last_run.json` の `dir`。

## 手順

1. `AGENTS.md`、`wiki/index.md`、直近の `wiki/weekly/*.md` 1 本を読み、既存の wiki の構成と前回までの流れを把握する。
2. 入力ディレクトリの `collected.md` を読む。詳細が必要なら `collected.json` を参照する。
3. **トリアージ**: 各項目を AGENTS.md の「判断基準」で 高 / 中 / 低 に分ける。
   - 高・中の項目は、必要に応じて WebFetch で Issue/PR/議事録本文を読み、事実を確認する。
     議事録は `RESOLUTION:` 行と、議題 (Topic) の見出しを優先して読む。
   - 1 回の実行で WebFetch は 25 回程度までに抑える。確認できなかった項目は「未確認」と書く。
4. **wiki 更新**:
   - 高・中の項目に対応する `wiki/specs/*.md` / `wiki/topics/*.md` の「最近の動き」に日付付きで追記し、「現状」「未解決の論点」を必要なら改める。ページが無ければ作る。
   - 新しく登場した主要な参加者は `wiki/people/<login>.md` を作る (役割と、どの仕様で見かけたか)。
   - 新規リポジトリは `wiki/repos/discovered.md` に 1 行ずつ追記する (日付・★・一言説明・分類)。
     特に注目すべきもの (★が多い、標準団体・ブラウザベンダー・著名な開発者によるもの、AI とアクセシビリティの交差) は `wiki/repos/<owner>__<name>.md` を作る。
   - `wiki/index.md` を更新する。
5. **週次ダイジェスト** `wiki/weekly/<ISO年>-W<ISO週2桁>.md` を書く。構成:

   ```markdown
   ---
   title: Web Accessibility Weekly 2026-W40
   type: weekly
   period: 2026-09-23 〜 2026-09-30
   sources: [raw/2026-09-30]
   ---
   # Web Accessibility Weekly 2026-W40

   ## 今週のハイライト
   (3〜5 項目。それぞれ 2〜3 文で「何が起きたか」「なぜ重要か」とリンク)

   ## 標準
   ### WCAG / AGWG
   ### ARIA / AAM / APG
   ### HTML / CSS (水平レビュー含む)
   ### ブラウザ / AT / Interop
   (各節: 箇条書き 1 項目 1 行 + リンク。該当なしの節は省略)

   ## 議事録
   (会合ごとに主要な決議を 1〜3 行)

   ## リリース

   ## GitHub: 新規・注目リポジトリ
   (新規発見から最大 10 件。★・言語・一言説明。ノイズ (個人の課題提出、空リポジトリ、テンプレート) は除外)

   ## 低優先度の動き
   (件数と代表例のみ)

   ## wiki の更新
   (今回作成・更新したページへのリンク)
   ```

6. `wiki/log.md` の末尾に `- <YYYY-MM-DD> weekly: <入力dir> → <ダイジェストのパス> (更新 N ページ)` を追記する。
7. `collected.md` の「取得失敗」に項目があれば、ダイジェスト末尾に「収集の不具合」として列挙する (sources.yml の修正は提案に留める)。

## 注意

- 書き言葉は直接的・平叙的に。比喩や煽りは使わない。
- 収集結果に無い出来事を足さない。
- `raw/` と `state/` は編集しない。
