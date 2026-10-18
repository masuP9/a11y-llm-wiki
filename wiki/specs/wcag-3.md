---
title: WCAG 3.0
type: spec
status: WD
updated: 2026-10-18
sources: [raw/2026-09-30, raw/2026-10-04, raw/2026-10-11, raw/2026-10-18]
---
# WCAG 3.0

W3C Accessibility Guidelines 3.0。AGWG が策定中の次世代ガイドライン。リポジトリは [w3c/wcag3](https://github.com/w3c/wcag3)。

## 現状

- 2026-09-10 付の Working Draft が出ている ([w3c/wcag3#876](https://github.com/w3c/wcag3/issues/876) の本文が「10 September 2026 Working Draft」の Guideline 2.1.7 を参照)。
- この WD には報告用の tier (reporting tiers) が入った。tier はタグで決まり、要件と 1 対 1 には対応しない (WD の 4.1 節)。適合 (conformance) 自体は単一の tier で、すべての core requirement を満たすことが条件 ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。
- 要件に付けるタグの定義案: physical harm / risk (金銭・医療・法律・プライバシー・セキュリティ) / barrier / friction / supplemental ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。
- 進捗: 要件 198、成熟度ステップ 765 のうち約 28%。最初の snapshot の見込みは 2028-08-31。WCAG 2 にあるものを WCAG 3 の下限とする ([AGWG 2026-09-29 IRC](https://www.w3.org/2026/09/29-ag-irc))。

## 最近の動き

- 2026-10-13 AGWG: WCAG 3 の 2027・2028 年のスケジュールをレビュー。[[people/rachaelbradley]] の説明では、2027 年末までに公開レビュー用の snapshot、2028 年 1 月を目標に CR snapshot。「CR snapshot」の意味と、CR snapshot を 2 回計画するのが現実的かが議論され、明確なマイルストーンと進捗の追跡手段を求める声が出た。続く要件の分類 (categorization) では、physical harm の「immediate」は片頭痛・吐き気・めまいなど遅れて出る影響を含まないので変更すべきという意見、risk に「reputational」を加えるのは曖昧という意見が出た。タグ定義を規範にするかは記録上決まっていない。決議なし ([議事録](https://www.w3.org/2026/10/13-ag-minutes.html)。本文の一部のみ確認)。
- 2026-10-12 COGA TF: 10-22 に WCAG 3 の exploratory provisions を確認する単発の会合を開く方針 ([議事録](https://www.w3.org/2026/10/12-coga-minutes.html))。同週、COGA の lbeaze が「Focus retained」([w3c/wcag3#915](https://github.com/w3c/wcag3/issues/915))、「Pointer focus indicated」の例外 ([#917](https://github.com/w3c/wcag3/issues/917))、「Expected Behavior」に core requirement が無いこと ([#916](https://github.com/w3c/wcag3/issues/916))、Consistent control location ([#918](https://github.com/w3c/wcag3/issues/918))、Contextual help ([#919](https://github.com/w3c/wcag3/issues/919))、Data visualizations ([#920](https://github.com/w3c/wcag3/issues/920))、Support available ([#921](https://github.com/w3c/wcag3/issues/921))、Feedback mechanism ([#922](https://github.com/w3c/wcag3/issues/922)) への COGA コメントを一括して起票した。
- 2026-10 GreggVan が WD への指摘を連続起票: focus を「keyboard focus」に統一 ([w3c/wcag3#908](https://github.com/w3c/wcag3/issues/908))、Flashing の例外の削除 ([#913](https://github.com/w3c/wcag3/issues/913))、自動更新テキスト ([#912](https://github.com/w3c/wcag3/issues/912))、5 秒超の自動再生音声の provision が無い ([#911](https://github.com/w3c/wcag3/issues/911))、Keyboard operable の不足 ([#910](https://github.com/w3c/wcag3/issues/910))、Navigating content の位置 ([#909](https://github.com/w3c/wcag3/issues/909))。いずれも起票直後で議論はこれから。
- 2026-10 mcking65 が、例外を持つ provision の「except when」固定の書式を緩める提案を起票 ([w3c/wcag3#906](https://github.com/w3c/wcag3/issues/906))。maryjom は WCAG 3 の Functional Performance Statements が EN 301 549 / Revised 508 の機能性能基準と対応しにくいと指摘 ([#914](https://github.com/w3c/wcag3/issues/914))。
- 2026-10 iadawn が sign language の exploratory provision 3 件 (動画の解像度・フレームレート・話者の特定) を追加する PR を出した ([w3c/wcag3#907](https://github.com/w3c/wcag3/pull/907))。glossary を definition list から見出しに変える PR ([#923](https://github.com/w3c/wcag3/pull/923)、adampage)。accessibility supported の PR [#902](https://github.com/w3c/wcag3/pull/902) と programmatically detectable の PR [#891](https://github.com/w3c/wcag3/pull/891) が更新。
- 2026-10 media 系の古い Issue が close: [#325](https://github.com/w3c/wcag3/issues/325) (sign language / subtitles)、[#535](https://github.com/w3c/wcag3/issues/535) (meaningful sound)、[#611](https://github.com/w3c/wcag3/issues/611)、[#490](https://github.com/w3c/wcag3/issues/490) (diacritics)。理由は未確認。
- 2026-10-06 AGWG で「mechanism」の定義が主題。WCAG 2 の「a mechanism is available」が曖昧なため、語をやめて「users can」と書く案が出た。平易さを支持する声がある一方、法務の観点などから、主語が UA・インターフェースから利用者に移るという懸念が複数出た。UA 実装か author 実装かを示すタグの案もあった。決議なし。音と音声の用語 (dialogue、speech、non-speech sounds など) は [GitHub discussion #899](https://github.com/w3c/wcag3/discussions/899) で 1〜2 週間議論する ([議事録](https://www.w3.org/2026/10/06-ag-minutes.html)。取得できた本文に RESOLUTION 行は無かったが、休憩後の subgroup 作業の部分は含まれておらず、決議の有無は完全には確認できていない)。
- 2026-10 mcking65 が「accessibility supported」の問題分析と提案を起票した ([w3c/wcag3#901](https://github.com/w3c/wcag3/issues/901))。用語が author の実装方法と UA の機能の両方を指して一貫せず、author が実行できる要件になっていないという分析。PR [#902](https://github.com/w3c/wcag3/pull/902) は、この語を「user agent supported method」と「user agent test set」に置き換え、新設の Testing 節に移し、test set の宣言と method の支持の証明を規範的要件とし、中核の適合要件を改める。AGWG の合意を前提とした探索的な方向で、決定ではない。
- 2026-10 「language adjustable」系の provision (Caption / Audio description) を「applies when」形式に揃えるか ([w3c/wcag3#900](https://github.com/w3c/wcag3/issues/900)、ashleemboyer)。mcking65 は「Change of focus notified」の「programmatically」の意図が不明という Issue も起票 ([#897](https://github.com/w3c/wcag3/issues/897))。#885 の用語整理の続き。
- 2026-10 Pseudo-motion を独立した provision にするか ([w3c/wcag3#739](https://github.com/w3c/wcag3/issues/739)、4 コメント)。AFixt (karlgroves) が 2026-09-10 版 WD へのコメントを提出 ([#874](https://github.com/w3c/wcag3/issues/874))。
- 2026-09-30〜10-04 mcking65 が「programmatically」系の用語を整理する Issue を連続して起票した。[#885](https://github.com/w3c/wcag3/issues/885) は「programmatically determinable」の定義が使われ方に合わないとして、定義を「Exposed to user agents in an application programming interface」に置き換える案を出している。同義語から「programmatically」を外す PR [#886](https://github.com/w3c/wcag3/pull/886) も参照されている (PR の状態は未確認)。個別の provision への Issue が続く: [#884](https://github.com/w3c/wcag3/issues/884) (Decorative images hidden)、[#883](https://github.com/w3c/wcag3/issues/883)・[#882](https://github.com/w3c/wcag3/issues/882) (Risk comparable)、[#889](https://github.com/w3c/wcag3/issues/889) (Changes to elements notified)、[#890](https://github.com/w3c/wcag3/issues/890) (視覚ラベルと programmatic name の要件を分ける)、[#892](https://github.com/w3c/wcag3/issues/892) (All steps listed)、[#894](https://github.com/w3c/wcag3/issues/894) (Return to start prominent)。いずれもコメント 1 件以下で、議論はこれから。
- 2026-10 decorative images の定義の Issue [#878](https://github.com/w3c/wcag3/issues/878) が 34 コメントに伸びた。内容は未確認。
- 2026-10 「single pointer」と「simple pointer」が紛らわしいという Issue [#643](https://github.com/w3c/wcag3/issues/643) が close (理由は未確認)。
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
