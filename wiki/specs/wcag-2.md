---
title: WCAG 2.x
type: spec
status: REC
updated: 2026-09-30
sources: [raw/2026-09-30]
---
# WCAG 2.x

Web Content Accessibility Guidelines 2.0 / 2.1 / 2.2。リポジトリは [w3c/wcag](https://github.com/w3c/wcag)。

## 現状

- backlog task force が WCAG 2 の変更案を出しており、2026-09-29 時点でコメント期間は残り 1 週間。変更案の 1 つは「best practice」という語をやめるもの ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。

## 最近の動き

- 2026-09-29 AGWG で [[people/patrickhlauke]] が、フォーカス可能な要素に role が必須かという議論 ([w3c/wcag#3029](https://github.com/w3c/wcag/issues/3029)、コメント 60 件) への意見を募った ([IRC](https://www.w3.org/2026/09/29-ag-irc))。
- 2026-09 overlay ツールが conforming alternate version (CAV) になりうるかの Issue ([w3c/wcag#2750](https://github.com/w3c/wcag/issues/2750)、コメント 79 件) が close。論点は新しい Issue [w3c/wcag#5373](https://github.com/w3c/wcag/issues/5373) に要約して移された。
- 2026-09 2.5.8 Target Size (Minimum) の Inline 例外が、文の外にある control と接する場合にも効くかという質問 ([w3c/wcag#5384](https://github.com/w3c/wcag/issues/5384))。

## 未解決の論点

- CAV への導線: overlay の操作部品に「CAV に行ける」ことを示すラベルが無い場合、2.4.6 / 3.3.2 違反になるか。Detlev Fischer は違反とし、Patrick Lauke は規範上の要件は無いとする ([w3c/wcag#5373](https://github.com/w3c/wcag/issues/5373))。
- 3.3.8 / 3.3.9 の「authentication process」の定義 ([w3c/wcag#3264](https://github.com/w3c/wcag/issues/3264))。
- 3.3.1 と 4.1.2 の重なり ([w3c/wcag#696](https://github.com/w3c/wcag/issues/696))。

## 関連

- [[specs/wcag-3]]
- [[specs/wcag2ict]]
