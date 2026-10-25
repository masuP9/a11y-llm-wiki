---
title: WAI-ARIA と AAM
type: spec
status: ED
updated: 2026-10-25
sources: [raw/2026-09-30, raw/2026-10-04, raw/2026-10-11, raw/2026-10-18, raw/2026-10-25]
---
# WAI-ARIA と AAM

WAI-ARIA 1.3 と、HTML-AAM などのマッピング仕様。ARIA WG が担当。リポジトリは [w3c/aria](https://github.com/w3c/aria)、[w3c/html-aam](https://github.com/w3c/html-aam)。

## 現状

- ARIA Notify (`ariaNotify()`) の導入文と i18n の例を足す編集上の PR が 2026-09-28 に merge された ([w3c/aria#2869](https://github.com/w3c/aria/pull/2869))。これで [w3c/aria#2828](https://github.com/w3c/aria/issues/2828) (`AriaNotificationOptions` に言語・方向を持たせる) と [#2837](https://github.com/w3c/aria/issues/2837) が close。`lang` / `dir` のメンバーが追加されたかは未確認。セキュリティの記述は [#2914](https://github.com/w3c/aria/pull/2914) に分かれた。
- ARIA WG の新しい charter 案が出ており、APA が水平レビューした ([APA 2026-09-23](https://www.w3.org/2026/09/23-apa-minutes.html)、[w3c/strategy#571](https://github.com/w3c/strategy/issues/571))。

## 最近の動き

- 2026-10 (10-18〜10-25) smhigley が interactive list 用の `listview` role を追加する PR を出した ([w3c/aria#2951](https://github.com/w3c/aria/pull/2951)、[#2036](https://github.com/w3c/aria/issues/2036) 対応)。[[people/scottaohara]] は `th` の `scope=rowgroup` の mapping の PR ([#2950](https://github.com/w3c/aria/pull/2950)) と、main / banner / contentinfo の note を揃える editorial PR ([#2948](https://github.com/w3c/aria/pull/2948)) を出した。aria-hidden とフォーカスされた要素の期待を定める PR [#2181](https://github.com/w3c/aria/pull/2181) は 37 コメントで更新。
- 2026-10 daniel-montalvo: ARIA 1.2 の notes の cleanup と respec validator の有効化が merge ([w3c/aria#2949](https://github.com/w3c/aria/pull/2949)、[#2928](https://github.com/w3c/aria/pull/2928))。ARIA Process を「evergreen」方式に向けて更新する PR ([#2947](https://github.com/w3c/aria/pull/2947))。
- 2026-10 ARIA in HTML: scottaohara が `figcaption` の implicit role の更新 ([w3c/html-aria#611](https://github.com/w3c/html-aria/pull/611)、`caption` は許可するが非推奨)、`mark` の implicit role ([#613](https://github.com/w3c/html-aria/pull/613)、[#609](https://github.com/w3c/html-aria/issues/609) 対応)、video `poster` の allowances ([#615](https://github.com/w3c/html-aria/pull/615)、[#608](https://github.com/w3c/html-aria/issues/608) 対応) の PR を出した。冗長な暗黙 role の明示宣言に関する記述を簡素化する提案 ([#612](https://github.com/w3c/html-aria/issues/612))、`dd` / `dt` の許可 role ([#614](https://github.com/w3c/html-aria/issues/614))。hidden な `<label>` がフォームコントロールの名前になりうるかの Issue ([w3c/html-aam#370](https://github.com/w3c/html-aam/issues/370)、16 コメント) は close。結論は未確認。
- 2026-10 APG: Disclosure Navigation Menu の keyboard support の記述を実装に合わせる PR ([w3c/aria-practices#3475](https://github.com/w3c/aria-practices/pull/3475)、[#1632](https://github.com/w3c/aria-practices/issues/1632)・[#1390](https://github.com/w3c/aria-practices/issues/1390) 対応)。color contrast settings の practice ページの PR ([#2991](https://github.com/w3c/aria-practices/pull/2991)) は 69 コメントで更新。accname の例が不適切という Issue ([w3c/accname#255](https://github.com/w3c/accname/issues/255)) が 11 コメントで更新 (Agenda ラベル)。
- 2026-10 ACT-Rules: role-required-states-and-properties ルールを ARIA 1.3 に合わせる PR ([act-rules/act-rules.github.io#2466](https://github.com/act-rules/act-rules.github.io/pull/2466)、2 週間の Call for Review が必要と記載)。
- 2026-10-15 ARIA WG: RESOLUTION 行なし。PR / Issue の triage が中心 ([議事録](https://www.w3.org/2026/10/15-aria-minutes.html))。
  - child roles の PR [w3c/aria#2929](https://github.com/w3c/aria/pull/2929) は ACT のレビュー待ちで、翌週の議題。Section 7 を DOM node 以外 (CSS が生成する構造) に広げる件 ([#2938](https://github.com/w3c/aria/issues/2938)) は TPAC 後に議論。
  - video の `poster` 要素の提案 ([w3c/html-aria#608](https://github.com/w3c/html-aria/issues/608)、[w3c/html-aam#618](https://github.com/w3c/html-aam/issues/618)) は HTML-AAM 側で扱い、HTML 側は初期段階。`form` 属性を relationship に map する案 ([html-aam#617](https://github.com/w3c/html-aam/issues/617))、`<select multiple size="1">` ([#616](https://github.com/w3c/html-aam/issues/616)) は今後の議題ラベル。
  - aria-keyshortcuts の macOS mapping ([w3c/core-aam#272](https://github.com/w3c/core-aam/issues/272)) は単純な提案として jcraig がレビュー。VoiceOver が「Meta Shift M」と読む件が背景。
  - `aria-checked` on option の AX API 公開 ([core-aam#270](https://github.com/w3c/core-aam/issues/270)) は、macOS API を変える前に使用例の文書化が必要という整理。`role="time"` ([#2926](https://github.com/w3c/aria/issues/2926)) は TPAC で扱い、Core-AAM の mapping を見直す。
  - image map の ATK mapping ([html-aam#614](https://github.com/w3c/html-aam/issues/614))、attr-target の IA2 / ATK mapping ([#613](https://github.com/w3c/html-aam/issues/613)) は good first issue で、AI の成果物は人間のレビューが必須とされた。
  - TPAC 前の最終会合。breakout のスケジュールは公開済み。
- 2026-10 PDF-AAM の作業に関連して、DuffJohnson が PDF の artifact の位置的セマンティクス ([w3c/aria#2944](https://github.com/w3c/aria/issues/2944)) と title content ([#2943](https://github.com/w3c/aria/issues/2943)) を ARIA に求める Issue を起票。neet は Text Equivalent Computation 2.1.2 の例が不適切 ([#2946](https://github.com/w3c/aria/issues/2946))、`<output>` の AXRoleDescription mapping ([html-aam#620](https://github.com/w3c/html-aam/issues/620))、`<mark>` の implicit role が html-aria と HTML-AAM で食い違う ([html-aria#609](https://github.com/w3c/html-aria/issues/609)) を起票。いずれも起票直後で議論はこれから。
- 2026-10 daniel-montalvo が ARIA リポジトリのツール整備の PR を複数 merge ([#2935](https://github.com/w3c/aria/pull/2935)、[#2934](https://github.com/w3c/aria/pull/2934)、[#2932](https://github.com/w3c/aria/pull/2932))。respec から WPT を参照する試み ([#2941](https://github.com/w3c/aria/pull/2941)、[#2940](https://github.com/w3c/aria/issues/2940))。jnurthen は「list」の曖昧さを直す editorial PR を出した ([#2942](https://github.com/w3c/aria/pull/2942)、[#2939](https://github.com/w3c/aria/issues/2939))。
- 2026-10 ACT-Rules CG: ARIA の child roles の変更に合わせ、required owned elements ルールを ARIA 1.3 の用語に更新する Issue ([act-rules/act-rules.github.io#2461](https://github.com/act-rules/act-rules.github.io/issues/2461))。AI の利用方針を作る Issue ([#2463](https://github.com/act-rules/act-rules.github.io/issues/2463)。AI が書いた Issue / PR は開示する、AI が書いたルールは人間が検証する、などが CG 会合のメモにある) と、ACT ルール公開用の agent skill の PR ([#2462](https://github.com/act-rules/act-rules.github.io/pull/2462))。
- 2026-10-14 ARIA APG TF: RESOLUTION 行なし。準備できた PR は 11-05 に公開予定だが、contrast setting とランドマークの更新は未解決の問題があり含まない。fork の PR にはプレビューが出ない問題があり、Remy が戻る 1 月までは mirror PR で対応 ([議事録](https://www.w3.org/2026/10/14-aria-apg-minutes.html))。Accordion の例に reduced motion を考慮したアニメーションを足す PR ([w3c/aria-practices#3473](https://github.com/w3c/aria-practices/pull/3473))。
- 2026-10-08 ARIA WG 決議 1 件: 「`role=none` からグローバルな state と property を取り除く」。[w3c/aria#1288](https://github.com/w3c/aria/issues/1288) (author が conflict resolution を起こすのを禁じる) が対象で、action は pkra ([議事録](https://www.w3.org/2026/10/08-aria-minutes.html))。
- 2026-10-08 radiogroup の posinset / setsize ([w3c/html-aam#598](https://github.com/w3c/html-aam/issues/598)): [[people/spectranaut]] が「ARIA はネイティブの radio の名前によるまとまりを上書きできない」と明確にする案と Chrome の修正案を出した。隣り合う radio を暗黙にグループ化することには反対があり、jcraig は ARIA のグループ化の仕組みを検討するよう提案。決議なし ([議事録](https://www.w3.org/2026/10/08-aria-minutes.html))。
- 2026-10-08 「label」の用語 ([w3c/aria#2904](https://github.com/w3c/aria/issues/2904)): 「name」の意味での「label」の使用を減らす方向に支持があり、変更は最小限に。WCAG の定義の採用は支持されなかった。giacomo が方針を作る。決議なし ([議事録](https://www.w3.org/2026/10/08-aria-minutes.html))。
- 2026-10-08 menu / group / menuitem の親子関係 PR ([w3c/aria#2483](https://github.com/w3c/aria/pull/2483)) は、間に入る role を足して定義を改めた版が再レビュー待ち。presentational role の conflict resolution の PR ([#2237](https://github.com/w3c/aria/pull/2237)) は、presentational の継承を廃止する案 ([#2509](https://github.com/w3c/aria/issues/2509)) の結果次第で影響を受ける (pkra の指摘)。child roles の PR [#2929](https://github.com/w3c/aria/pull/2929) は cyns、giacomo、jcraig がレビュー。TPAC の breakout の暫定スケジュールは翌週早くに出る見込み ([議事録](https://www.w3.org/2026/10/08-aria-minutes.html))。
- 2026-10 「Allowed Accessibility Child Roles」の記述の明確化を求める Issue ([w3c/aria#2930](https://github.com/w3c/aria/issues/2930)、gsnedders、[#1033](https://github.com/w3c/aria/issues/1033) の続き)。ARIA の暗黙のセマンティクスを公開する案 ([#2663](https://github.com/w3c/aria/issues/2663)、37 コメント)、"accessibility descendant" ([#2832](https://github.com/w3c/aria/issues/2832)) が更新。Security 水平レビュー ([#2861](https://github.com/w3c/aria/issues/2861)) は Agenda 付きで更新。
- 2026-10 HTML-AAM: image map を ATK_ROLE_IMAGE_MAP に対応させる提案 ([w3c/html-aam#614](https://github.com/w3c/html-aam/issues/614)、joanmarie。本文によれば Chromium は対応済み、Gecko は未対応、Orca は期待している)。`target` 属性の IA2 / ATK の mapping ([#613](https://github.com/w3c/html-aam/issues/613))。wpt/html-aam の再構成 ([#615](https://github.com/w3c/html-aam/issues/615))。HTML-ARIA に switch 属性付き checkbox の追加 ([w3c/html-aria#607](https://github.com/w3c/html-aria/issues/607))。
- 2026-10-01 ARIA WG 決議 1 件: translatable attributes の editorial な変更 ([w3c/aria#2862](https://github.com/w3c/aria/pull/2862)) を merge する。[w3c/aria#2827](https://github.com/w3c/aria/issues/2827) も close ([議事録](https://www.w3.org/2026/10/01-aria-minutes.html))。
- 2026-10-01 `aria-actions` の追加 PR ([w3c/aria#1805](https://github.com/w3c/aria/pull/1805)) は、関連 Issue [#2845](https://github.com/w3c/aria/issues/2845) の完了と実装が揃うまで editor's draft に入れない。TPAC でテスト作成のワークショップを開く案 ([議事録](https://www.w3.org/2026/10/01-aria-minutes.html))。
- 2026-10-01 CSS の `::picker-icon` / `::checkmark` をアクセシビリティツリーから除くかは合意なし。luke が CSSWG に戻す ([議事録](https://www.w3.org/2026/10/01-aria-minutes.html)、[w3c/csswg-drafts#14316](https://github.com/w3c/csswg-drafts/issues/14316))。
- 2026-10-01 radio の setsize / posinset の計算を明確にする PR ([w3c/aria#2919](https://github.com/w3c/aria/pull/2919)) にレビュアーが付いた。Security considerations の PR [#2914](https://github.com/w3c/aria/pull/2914) は優先度が高い ([議事録](https://www.w3.org/2026/10/01-aria-minutes.html))。
- 2026-10 Android の Core-AAM マッピングを作っている dtsengchromium から 2 件の質問: `role="time"` が time / date / duration を区別せず TTS API (`TtsSpan`) に渡せない ([w3c/aria#2926](https://github.com/w3c/aria/issues/2926))、Core-AAM の「option inside combobox」と「option not inside combobox」の区別が不明確 ([w3c/core-aam#271](https://github.com/w3c/core-aam/issues/271))。
- 2026-10 "API's focus event" が曖昧という用語の Issue ([w3c/aria#2925](https://github.com/w3c/aria/issues/2925))。ARIA IDL と HTML IDL の reflection の整合を TPAC で議論する提案 ([w3c/aria#2922](https://github.com/w3c/aria/issues/2922))。
- 2026-10 `option` 要素の `role=option` を「not recommended」とする記述の削除を提案 ([w3c/html-aria#605](https://github.com/w3c/html-aria/issues/605))。[w3c/aria#2896](https://github.com/w3c/aria/issues/2896) と関連。
- 2026-10 APG のランドマーク例のサイドバーで、表示ラベル「Asst. Tech.」とアクセシブル名が違い SC 2.5.3 Label in Name に反するという指摘 ([w3c/aria-practices#3472](https://github.com/w3c/aria-practices/issues/3472))。

- 2026-09-24 ARIA WG 決議: 「ARIA の radiogroup と、`name` でまとまった input radio を混ぜてはいけない。author への MUST を足してよいが、名前付き radiogroup をブラウザが修復する方法 (名前付き group に格下げ) を検討する」 ([議事録](https://www.w3.org/2026/09/24-aria-minutes.html)、[w3c/html-aam#598](https://github.com/w3c/html-aam/issues/598))。ACT ルールへの影響は giacomo-petri が確認する。
- 2026-09-24 radiogroup の子の制約 ([w3c/aria#2910](https://github.com/w3c/aria/issues/2910)) は決定なし。ブラウザごとに祖先の探し方が違い、表の行を選ぶ radio も支えたい。将来の grouping 属性 (「radioname」のようなもの) の案が出た。Issue は close ([議事録](https://www.w3.org/2026/09/24-aria-minutes.html))。
- 2026-09-24 `role="option"` を combobox の子に許すか ([w3c/aria#2896](https://github.com/w3c/aria/issues/2896)) は決定なし。要件は描画後の DOM (option が listbox に slot される) を指すという見方 ([議事録](https://www.w3.org/2026/09/24-aria-minutes.html))。
- 2026-09 TPAC の F2F 候補として、AT Driver の紹介 ([#2915](https://github.com/w3c/aria/issues/2915))、ACD の「supported」の意味 ([#2916](https://github.com/w3c/aria/issues/2916))、要素削除時の `blur` ([#2920](https://github.com/w3c/aria/issues/2920))、疑似要素への ARIA ([#2921](https://github.com/w3c/aria/issues/2921)) が追加された。詳細は [[topics/interop-and-aria-at]] と [[topics/css-and-accessibility]]。
- 2026-09 html-aria を ARIA のモノレポに移す提案 ([w3c/aria#2918](https://github.com/w3c/aria/issues/2918))。[[people/spectranaut]] が起票。
- 2026-09 `input` の date 系が公開する spinbutton の子を仕様に書くか ([w3c/html-aam#612](https://github.com/w3c/html-aam/issues/612))。

## 未解決の論点

- `blur` の同期発火をやめる Blink の変更 (代替の `focusreset`、[whatwg/html#12842](https://github.com/whatwg/html/issues/12842)) がフォーカス追跡に与える影響 ([w3c/aria#2920](https://github.com/w3c/aria/issues/2920))。
- 明示的なグループ無しで control を関連づける仕組み ([w3c/aria#1721](https://github.com/w3c/aria/issues/1721))。
- filterable select (テキスト欄で listbox を絞り込む) ([w3c/aria#2841](https://github.com/w3c/aria/issues/2841))。

## 関連

- [[topics/interop-and-aria-at]]
- [[topics/css-and-accessibility]]
