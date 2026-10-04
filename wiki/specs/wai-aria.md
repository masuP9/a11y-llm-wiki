---
title: WAI-ARIA と AAM
type: spec
status: ED
updated: 2026-10-04
sources: [raw/2026-09-30, raw/2026-10-04]
---
# WAI-ARIA と AAM

WAI-ARIA 1.3 と、HTML-AAM などのマッピング仕様。ARIA WG が担当。リポジトリは [w3c/aria](https://github.com/w3c/aria)、[w3c/html-aam](https://github.com/w3c/html-aam)。

## 現状

- ARIA Notify (`ariaNotify()`) の導入文と i18n の例を足す編集上の PR が 2026-09-28 に merge された ([w3c/aria#2869](https://github.com/w3c/aria/pull/2869))。これで [w3c/aria#2828](https://github.com/w3c/aria/issues/2828) (`AriaNotificationOptions` に言語・方向を持たせる) と [#2837](https://github.com/w3c/aria/issues/2837) が close。`lang` / `dir` のメンバーが追加されたかは未確認。セキュリティの記述は [#2914](https://github.com/w3c/aria/pull/2914) に分かれた。
- ARIA WG の新しい charter 案が出ており、APA が水平レビューした ([APA 2026-09-23](https://www.w3.org/2026/09/23-apa-minutes.html)、[w3c/strategy#571](https://github.com/w3c/strategy/issues/571))。

## 最近の動き

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
