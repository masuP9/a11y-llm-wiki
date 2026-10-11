---
title: CSS とアクセシビリティ
type: topic
updated: 2026-10-11
sources: [raw/2026-09-30, raw/2026-10-04, raw/2026-10-11]
---
# CSS とアクセシビリティ

CSSWG の提案のうち、アクセシビリティに関わるもの (`a11y-tracker` ラベルや APA の水平レビュー対象)。

## 現状

- **prefers-bold-text**: iOS / Android の「文字を太くする」設定を反映するメディア特性の提案。open で、CSSWG の決議は未確認 ([w3c/csswg-drafts#14477](https://github.com/w3c/csswg-drafts/issues/14477))。APA では、author 側の負担とレイアウト崩れ、fingerprinting、UA が自分で太字にすべきか (Janina) author にメディアクエリを渡すべきか (PaulG) が議論された ([APA 2026-09-23](https://www.w3.org/2026/09/23-apa-minutes.html)、[w3c/a11y-tracking#351](https://github.com/w3c/a11y-tracking/issues/351))。
- **疑似要素への ARIA**: 疑似要素にだけ効く `aria-*` プロパティ (と `role` 用の `aria-role`) を CSS に足す提案 ([w3c/csswg-drafts#14534](https://github.com/w3c/csswg-drafts/issues/14534))。提案者は TPAC で ARIA WG に説明する予定 ([w3c/aria#2921](https://github.com/w3c/aria/issues/2921))。
- **css-forms-1**: `::picker-icon` と `::checkmark` の代替テキストを空にする案 ([#14316](https://github.com/w3c/csswg-drafts/issues/14316))、prefers-contrast と forced-colors を既定で扱う案 ([#14318](https://github.com/w3c/csswg-drafts/issues/14318))。
- **css-overflow-5 の scroll marker**: APA の PaulG は、ARIA が必要な本格的な作り方と並んで CSS だけの簡易な道ができることを懸念している。アクセシビリティ上の注意の節を後で見直す ([APA 2026-09-23](https://www.w3.org/2026/09/23-apa-minutes.html)、[w3c/a11y-tracking#353](https://github.com/w3c/a11y-tracking/issues/353)、[#354](https://github.com/w3c/a11y-tracking/issues/354))。

## 最近の動き

- 2026-10 CSS Color 4 (CR) の水平レビュー依頼 ([w3c/a11y-request#190](https://github.com/w3c/a11y-request/issues/190)、期限 2026-12-09、次の遷移は 12 月の CR Snapshot の予定)。
- 2026-10 css-overflow の line-clamp とスクリーンリーダー ([w3c/csswg-drafts#12859](https://github.com/w3c/csswg-drafts/issues/12859)) が close (「Closed Accepted by CSSWG Resolution」ラベル)。css-content の counter の alt text ([#10387](https://github.com/w3c/csswg-drafts/issues/10387)) も同ラベルで close。内容は未確認。
- 2026-10 css-forms-1 の `::picker-icon` / `::checkmark` の空 alt ([#14316](https://github.com/w3c/csswg-drafts/issues/14316))、prefers-contrast / forced-colors の既定の扱い ([#14318](https://github.com/w3c/csswg-drafts/issues/14318)、「Closed Accepted by CSSWG Resolution」ラベル) が更新。css-content の画像読み込み失敗時の alt ([#218](https://github.com/w3c/csswg-drafts/issues/218)、[#2832](https://github.com/w3c/csswg-drafts/issues/2832)) は TPAC の Agenda+。
- 2026-10 WHATWG: 逐次フォーカスナビゲーションのプリミティブの公開提案 ([whatwg/html#13051](https://github.com/whatwg/html/issues/13051)、vmpstr、実装者の関心待ち)。video の poster に alt とレスポンシブ画像を足す提案 ([whatwg/html#10378](https://github.com/whatwg/html/issues/10378)、92 コメント)。
- 2026-10-01 ARIA WG で `::picker-icon` / `::checkmark` をアクセシビリティツリーから除くかを議論。合意なし ([議事録](https://www.w3.org/2026/10/01-aria-minutes.html)、[w3c/csswg-drafts#14316](https://github.com/w3c/csswg-drafts/issues/14316))。
- 2026-10 `prefers-bold-text` ([#14477](https://github.com/w3c/csswg-drafts/issues/14477)) は `Agenda+ TPAC` ラベル付き。css-image-animation の role / state の AAPI への伝え方 ([#13784](https://github.com/w3c/csswg-drafts/issues/13784)) も同ラベル。carousel / scroll container への `focus()` ([#12240](https://github.com/w3c/csswg-drafts/issues/12240)) が更新された。

## 関連

- [[specs/wai-aria]]
