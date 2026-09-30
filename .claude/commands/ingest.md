---
description: 仕様・トピック・リポジトリを深掘りして wiki ページを作る/育てる
argument-hint: "<対象: 例 'WCAG 3.0' 'aria-actions' 'focus appearance' 'dequelabs/axe-core'>"
---

# /ingest $ARGUMENTS

オンデマンドの深掘り。Jxck の tc39-llm-wiki における Proposal 単位の Ingest に相当する。

## 手順

1. `wiki/index.md` と既存の関連ページを読み、既に分かっていることを確認する。
2. 対象の一次ソースを集める (WebFetch / GitHub):
   - 仕様: Editor's Draft と最新の TR、GitHub リポジトリの主要 Issue/PR、変更履歴 (Changes / Change log 節)
   - 議論の経緯: `raw/*/collected.json` の過去分から対象に関係する項目、該当 WG の議事録 (`https://www.w3.org/YYYY/MM/DD-<group>-minutes.html`) の RESOLUTION
   - トピック: 関係する複数の仕様・Issue を横断
   - リポジトリ: README、リリース履歴、メンテナ、利用状況
3. ページを作成・更新する。
   - spec: 「現状」「経緯 (mermaid timeline)」「最近の動き」「未解決の論点」「主要な参加者」「関連」
   - topic: 「概要」「関係する仕様と該当箇所」「論点」「実装状況」「関連」
   - repo: 「概要」「位置付け」「最近のリリース」「関連」
4. 登場した人物の `wiki/people/*.md` を作成・更新する。
5. `wiki/index.md` を更新し、`wiki/log.md` に `- <日付> ingest: <対象> → <ページ>` を追記する。

## 注意

- 全事実にリンクを付ける。推測は明記する。
- 一度に全部を解析しようとしない。対象の範囲を超えたら関連ページのスタブ (1〜2 行 + TODO) を作って止める。
