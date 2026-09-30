---
title: CSS とアクセシビリティ
type: topic
updated: 2026-09-30
sources: [raw/2026-09-30]
---
# CSS とアクセシビリティ

CSSWG の提案のうち、アクセシビリティに関わるもの (`a11y-tracker` ラベルや APA の水平レビュー対象)。

## 現状

- **prefers-bold-text**: iOS / Android の「文字を太くする」設定を反映するメディア特性の提案。open で、CSSWG の決議は未確認 ([w3c/csswg-drafts#14477](https://github.com/w3c/csswg-drafts/issues/14477))。APA では、author 側の負担とレイアウト崩れ、fingerprinting、UA が自分で太字にすべきか (Janina) author にメディアクエリを渡すべきか (PaulG) が議論された ([APA 2026-09-23](https://www.w3.org/2026/09/23-apa-minutes.html)、[w3c/a11y-tracking#351](https://github.com/w3c/a11y-tracking/issues/351))。
- **疑似要素への ARIA**: 疑似要素にだけ効く `aria-*` プロパティ (と `role` 用の `aria-role`) を CSS に足す提案 ([w3c/csswg-drafts#14534](https://github.com/w3c/csswg-drafts/issues/14534))。提案者は TPAC で ARIA WG に説明する予定 ([w3c/aria#2921](https://github.com/w3c/aria/issues/2921))。
- **css-forms-1**: `::picker-icon` と `::checkmark` の代替テキストを空にする案 ([#14316](https://github.com/w3c/csswg-drafts/issues/14316))、prefers-contrast と forced-colors を既定で扱う案 ([#14318](https://github.com/w3c/csswg-drafts/issues/14318))。
- **css-overflow-5 の scroll marker**: APA の PaulG は、ARIA が必要な本格的な作り方と並んで CSS だけの簡易な道ができることを懸念している。アクセシビリティ上の注意の節を後で見直す ([APA 2026-09-23](https://www.w3.org/2026/09/23-apa-minutes.html)、[w3c/a11y-tracking#353](https://github.com/w3c/a11y-tracking/issues/353)、[#354](https://github.com/w3c/a11y-tracking/issues/354))。

## 関連

- [[specs/wai-aria]]
