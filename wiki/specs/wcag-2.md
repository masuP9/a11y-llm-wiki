---
title: WCAG 2.x
type: spec
status: REC
updated: 2026-10-18
sources: [raw/2026-09-30, raw/2026-10-04, raw/2026-10-11, raw/2026-10-18]
---
# WCAG 2.x

Web Content Accessibility Guidelines 2.0 / 2.1 / 2.2。リポジトリは [w3c/wcag](https://github.com/w3c/wcag)。

## 現状

- backlog task force が WCAG 2 の変更案を出しており、2026-09-29 時点でコメント期間は残り 1 週間。変更案の 1 つは「best practice」という語をやめるもの ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。

## 最近の動き

- 2026-10-13 AGWG: adam が WCAG 2 の変更案の新しいバッチを 10-19 までのレビューとして告知 ([議事録](https://www.w3.org/2026/10/13-ag-minutes.html))。
- 2026-10 [[people/patrickhlauke]] が Understanding と定義の編集 PR を連続して出した: 4.1.2 の「in brief」で「correct」を「appropriate」に ([w3c/wcag#5407](https://github.com/w3c/wcag/pull/5407))、`role` の定義の例を更新 ([#5404](https://github.com/w3c/wcag/pull/5404)、[#1476](https://github.com/w3c/wcag/issues/1476) を close する案)、「programmatically determined」の例に accessibility API を明記 ([#5403](https://github.com/w3c/wcag/pull/5403))、2.5.8 に 24×24 の根拠の note ([#5402](https://github.com/w3c/wcag/pull/5402))、3.3.2 の 2 つの例の修正 ([#5408](https://github.com/w3c/wcag/pull/5408))。4.1.2 の対象を利用者が設定できる state / property に限る提案は PR [#5399](https://github.com/w3c/wcag/pull/5399) として更新 ([#5395](https://github.com/w3c/wcag/issues/5395))。
- 2026-10 yatil が Understanding の「Key Terms」見出しを「Relevant Glossary Entries」などに変える提案を起票。規範的な用語定義が補足的・任意に見えるという理由 ([w3c/wcag#5409](https://github.com/w3c/wcag/issues/5409)、6 コメント)。
- 2026-10 1.4.11 Non-text contrast の Understanding にボタンの境界についての説明を足す PR ([w3c/wcag#5411](https://github.com/w3c/wcag/pull/5411)、[#865](https://github.com/w3c/wcag/issues/865) 対応)。CAV と 2.4.6 / 3.3.2 ([#5373](https://github.com/w3c/wcag/issues/5373)、20 コメント) が更新。
- 2026-10 4.1.2 Name, Role, Value の Understanding に、対象は「利用者が設定できる」state / property に限ると明記する提案。`disabled` や `required` は対象外という整理 ([w3c/wcag#5395](https://github.com/w3c/wcag/issues/5395)、[[people/patrickhlauke]]、Substantive ラベル)。
- 2026-10 3.3.8 / 3.3.9 の「authentication process」の定義を問う Issue が更新 (41 コメント、[w3c/wcag#3264](https://github.com/w3c/wcag/issues/3264))。内容は未確認。
- 2026-10 CAV への導線と 2.4.6 / 3.3.2 の関係 ([w3c/wcag#5373](https://github.com/w3c/wcag/issues/5373)、15 コメント) と、3.3.2 でラベル不要な control の例 ([#4977](https://github.com/w3c/wcag/issues/4977)) が更新。1.4.10 Reflow の「functionality」([#5320](https://github.com/w3c/wcag/issues/5320)) は close。結論は未確認。
- 2026-10 2.5.8 Target Size で、文中のリンクが隣接する control と接する場合 ([w3c/wcag#5384](https://github.com/w3c/wcag/issues/5384))、プログラミング言語を人間の言語とみなすか (1.4.3 / 1.4.6、[#5369](https://github.com/w3c/wcag/issues/5369))、Conformance の 5.4 節「Third Party Content」の名称誤り (ErratumRaised、[#5263](https://github.com/w3c/wcag/issues/5263)) も更新。
- 2026-10 「フォーカス可能な要素に role が必須か」([w3c/wcag#3029](https://github.com/w3c/wcag/issues/3029)、61 コメント) が close。Issue 上は「working group response は長いスレッドの終わり近く」とあるが、結論は確認できず未確認。
- 2026-10 SC 2.1.4 の例が薄く判別しにくいという Issue ([w3c/wcag#953](https://github.com/w3c/wcag/issues/953)) が close。focus indicator のスタイルガイドなど新規ガイダンス案 ([#5387](https://github.com/w3c/wcag/issues/5387)、[#5388](https://github.com/w3c/wcag/issues/5388)、[#5389](https://github.com/w3c/wcag/issues/5389)) も close された (理由は未確認)。
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
