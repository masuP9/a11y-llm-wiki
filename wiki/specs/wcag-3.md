---
title: WCAG 3.0
type: spec
status: WD
updated: 2026-09-30
sources: [raw/2026-09-30]
---
# WCAG 3.0

W3C Accessibility Guidelines 3.0。AGWG が策定中の次世代ガイドライン。リポジトリは [w3c/wcag3](https://github.com/w3c/wcag3)。

## 現状

- 2026-09-10 付の Working Draft が出ている ([w3c/wcag3#876](https://github.com/w3c/wcag3/issues/876) の本文が「10 September 2026 Working Draft」の Guideline 2.1.7 を参照)。
- この WD には報告用の tier (reporting tiers) が入った。tier はタグで決まり、要件と 1 対 1 には対応しない (WD の 4.1 節)。適合 (conformance) 自体は単一の tier で、すべての core requirement を満たすことが条件 ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。
- 要件に付けるタグの定義案: physical harm / risk (金銭・医療・法律・プライバシー・セキュリティ) / barrier / friction / supplemental ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。
- 進捗: 要件 198、成熟度ステップ 765 のうち約 28%。最初の snapshot の見込みは 2028-08-31。WCAG 2 にあるものを WCAG 3 の下限とする ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。

## 最近の動き

- 2026-09-29 AGWG で要件のタグ付け (categorization) 作業を 4 グループに分けて実施。結果は survey ([tagging_sept_26](https://www.w3.org/wbs/35422/tagging_sept_26/)) で集め、chair が数週間かけてまとめる。決議はなし ([IRC](https://www.w3.org/2026/09/29-ag-irc))。進行は [[people/rachaelbradley]]。
- 2026-09 タグ付け作業の中で「Hover content persistent」を別要件にした理由が分からないという指摘 ([w3c/wcag3#879](https://github.com/w3c/wcag3/issues/879))。
- 2026-09 decorative images の定義を見直す提案 ([w3c/wcag3#878](https://github.com/w3c/wcag3/issues/878))、「Error messages collocated」の and/or が曖昧という指摘 ([w3c/wcag3#877](https://github.com/w3c/wcag3/issues/877))。
- 2026-09 Sign language (2.1.7) を上位の tier に置き、harm/risk タグを付けるよう求める公開コメント。AI による手話出力もネイティブのろう者が確認すべきとする ([w3c/wcag3#876](https://github.com/w3c/wcag3/issues/876))。
- 2026-09 FPWD 期の conformance に関する古いコメント Issue (#102, #230, #244〜#260, #280, #281, #416, #450, #506, #510 など) がまとめて close された ([例: w3c/wcag3#259](https://github.com/w3c/wcag3/issues/259))。close の理由は未確認。

## 未解決の論点

- サンプリング手法を WCAG 3 に入れるか ([w3c/wcag3#509](https://github.com/w3c/wcag3/issues/509))。
- 問題の深刻度 (severity) の評価 ([w3c/wcag3#103](https://github.com/w3c/wcag3/issues/103))。
- Page Variations の適合要件 ([w3c/wcag3#682](https://github.com/w3c/wcag3/issues/682))。
- 機能的ニーズ (functional needs) を規範にするか ([w3c/wcag3#419](https://github.com/w3c/wcag3/issues/419))。

## 関連

- [[specs/wcag-2]]
- [[specs/wcag2ict]]
