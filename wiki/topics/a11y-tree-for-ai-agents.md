---
title: AI エージェントとアクセシビリティツリー
type: topic
updated: 2026-09-30
sources: [raw/2026-09-30]
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

- 2026-09-30 上記の新規リポジトリを発見 ([[repos/discovered]])。

## 関連

- [[repos/discovered]]
