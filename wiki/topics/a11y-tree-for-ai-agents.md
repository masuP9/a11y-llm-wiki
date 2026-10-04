---
title: AI エージェントとアクセシビリティツリー
type: topic
updated: 2026-10-04
sources: [raw/2026-09-30, raw/2026-10-04]
---
# AI エージェントとアクセシビリティツリー

AI エージェント (computer use、ブラウザ操作) が画面を読む手段として、アクセシビリティツリーや OS の UI Automation を使う動き。GitHub の新規リポジトリから追う。

## 現状

同じ週に、アクセシビリティツリーをエージェント向けに使うリポジトリが複数見つかった。いずれも小規模 (★10 未満が中心)。

- ブラウザの DOM / アクセシビリティツリーから操作できない要素を落とし、エージェント向けに圧縮する: [Alpha-Park/genpark-browser-dom-accessibility-tree-pruner-skill](https://github.com/Alpha-Park/genpark-browser-dom-accessibility-tree-pruner-skill)、[Alpha-Park/genpark-html-dom-semantic-tree-pruner-skill](https://github.com/Alpha-Park/genpark-html-dom-semantic-tree-pruner-skill) (alphaparkinc にも同名のリポジトリがある)
- Windows の UI Automation ツリーを使う MCP サーバー: [Zichen-6688/Windows-MCP-Highspeed-Rust](https://github.com/Zichen-6688/Windows-MCP-Highspeed-Rust)
- Android の画面を読み取りに使う: [Nisaka520/JevGuide](https://github.com/Nisaka520/JevGuide)
- AI 向けに WCAG に沿ったルールを渡す: [fecarrico/A11Y.md](https://github.com/fecarrico/A11Y.md) (★415、既存リポジトリ)

## 最近の動き

- 2026-10-01 WebMCP (Web Machine Learning CG) が APA に水平レビューを依頼。自己レビューは [webmachinelearning/webmcp#272](https://github.com/webmachinelearning/webmcp/issues/272)。TPAC (2026-10-27) の F2F への参加も呼びかけている ([w3c/a11y-request#189](https://github.com/w3c/a11y-request/issues/189))。
- 2026-10-04 Android / デスクトップの accessibility API でエージェントに端末を操作させるリポジトリが新規・既存とも目立つ: [oroplex/pony](https://github.com/oroplex/pony) (★8、MCP)、[boxshell-org/BoxAgent](https://github.com/boxshell-org/BoxAgent) (★3)、既存の [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) (★1761、OS のアクセシビリティツリー)、[Core-Mate/OpenGUI](https://github.com/Core-Mate/OpenGUI) (★1813)。
- 2026-09-30 上記の新規リポジトリを発見 ([[repos/discovered]])。

## 関連

- [[repos/discovered]]
