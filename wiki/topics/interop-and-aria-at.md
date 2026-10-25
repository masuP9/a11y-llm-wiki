---
title: Interop と ARIA-AT (支援技術の相互運用テスト)
type: topic
updated: 2026-10-25
sources: [raw/2026-09-30, raw/2026-10-04, raw/2026-10-11, raw/2026-10-18, raw/2026-10-25]
---
# Interop と ARIA-AT

ブラウザと支援技術 (AT) の組み合わせでアクセシビリティが実際に動くかを確かめる取り組み。Interop の Accessibility investigation、ARIA-AT CG、AT Driver、Accessibility Compat Data (ACD) を扱う。

## 現状

- **ARIA-AT**: Tri-State Checkbox のテスト計画は 6 回の実行のうち 2 回が残り (JAWS)。HTML Button のテスト計画は JAWS・NVDA・VoiceOver で完了。VoiceOver の自動実行は macOS 15 では動くが、macOS 26 では音声がハーネスに取り込まれない ([ARIA-AT 2026-09-23](https://www.w3.org/2026/09/23-aria-at-minutes.html)、[w3c/aria-at-app#1671](https://github.com/w3c/aria-at-app/issues/1671))。
- JAWS 2026 が Vispero アカウントを求めるようになり、テスト環境での追跡・ライセンスが懸念になっている ([ARIA-AT 2026-09-23](https://www.w3.org/2026/09/23-aria-at-minutes.html))。
- **AT Driver** (AT を自動操作する仕様): Sovereign Tech Agency の資金を得た。BTT charter から ARIA charter への移管を予定 ([w3c/aria#2915](https://github.com/w3c/aria/issues/2915)、[w3c/strategy#558](https://github.com/w3c/strategy/issues/558))。
- **ACD**: WPT と ARIA-AT の結果から、Baseline / BCD にアクセシビリティのサポート情報を載せる計画。「supported」をどう判定し、どう見せるかを ARIA WG に問うている ([w3c/aria#2916](https://github.com/w3c/aria/issues/2916))。

## 最近の動き

- 2026-10-21 ARIA-AT CG: 決議なし。TPAC breakout ([w3c-cg/aria-at#1402](https://github.com/w3c-cg/aria-at/issues/1402)) を、ARIA-AT を WPT・BCD・web-features に結びつける内容に組み替える案。ARIA-AT のデータに web-features key を持たせる案を挙げ、Matt King は WCAG の method のテスト自動化と、WCAG 3 の accessibility support set の定義への活用を目標に挙げた。Tri-State Checkbox は VoiceOver の結果が食い違い再確認、HTML Button は JAWS / NVDA の実行が割り当て済みで VoiceOver に 3 件の conflict、disabled button は NVDA の結果を final にできる状態。disabled button は reading cursor を JavaScript で置けない問題 ([w3c-cg/aria-at#1415](https://github.com/w3c-cg/aria-at/issues/1415)) があり、自動 setup が不可能な場合のテスト方法を設計する Issue が立った ([#1421](https://github.com/w3c-cg/aria-at/issues/1421))。AT Driver で出力を取る案も出た ([議事録](https://www.w3.org/2026/10/21-aria-at-minutes.html))。reusable test modules ([#1396](https://github.com/w3c-cg/aria-at/issues/1396)) も更新。
- 2026-10 cookiecrook が、アクセシビリティ関連の WPT にラベルが付いていなかった問題を Claude で洗い出して修正した経緯を述べ、AI の skill / tool をリポジトリに置くかを問う Issue を起票 ([web-platform-tests/interop-accessibility#256](https://github.com/web-platform-tests/interop-accessibility/issues/256))。Interop 2026 accessibility investigation ([interop-accessibility#202](https://github.com/web-platform-tests/interop-accessibility/issues/202)) は 13 コメントで更新。10-07 の会合 Issue ([#246](https://github.com/web-platform-tests/interop-accessibility/issues/246)) は close。
- 2026-10 [[people/spectranaut]] が Core-AAM の `aamtest` を API 別に書く Issue を起票: ATSPI ([web-platform-tests/interop-accessibility#254](https://github.com/web-platform-tests/interop-accessibility/issues/254))、UIA ([#251](https://github.com/web-platform-tests/interop-accessibility/issues/251)。hatheo が role テストに着手済み)、AX API ([#252](https://github.com/web-platform-tests/interop-accessibility/issues/252))、IA2 ([#253](https://github.com/web-platform-tests/interop-accessibility/issues/253))。HTML-AAM の概念を Core-AAM のテストにどう対応させるか ([#255](https://github.com/web-platform-tests/interop-accessibility/issues/255))。zcorpan は CSS 生成コンテンツの alt のテストを提案 ([#250](https://github.com/web-platform-tests/interop-accessibility/issues/250))。
- 2026-10 aria-at に HTML `a` (href 付き) のテスト計画を追加する PR ([w3c/aria-at#1419](https://github.com/w3c-cg/aria-at/pull/1419))。NVDA の disabled button の報告 ([#1415](https://github.com/w3c-cg/aria-at/issues/1415)) が更新。
- 2026-10-07 ARIA-AT CG: 決議なし。disabled HTML button のテスト計画が Draft に進んだ。B キーの quick-key が disabled button に移る挙動は、失敗する optional assertion として記録することで合意 (JAWS は移らない)。VoiceOver の shift+j の不具合は macOS 26.6.2 で直る可能性がある。次回は 10-21 ([議事録](https://www.w3.org/2026/10/07-aria-at-minutes.html))。
- 2026-10 aria-at に web-features カタログの採用を提案 ([w3c/aria-at#1414](https://github.com/w3c-cg/aria-at/issues/1414)、lolaodelola)。APG / HTML-AAM テストの再利用モジュール ([#1396](https://github.com/w3c-cg/aria-at/issues/1396))。NVDA が disabled button を section と読むという報告 ([#1415](https://github.com/w3c-cg/aria-at/issues/1415))。
- 2026-10 次回 Interop Accessibility 会合は 2026-11-03 ([web-platform-tests/interop-accessibility#249](https://github.com/web-platform-tests/interop-accessibility/issues/249))。Interop 2026 の accessibility investigation ([#202](https://github.com/web-platform-tests/interop-accessibility/issues/202))、computed property のテスト ([#248](https://github.com/web-platform-tests/interop-accessibility/issues/248))、aria-description の公開先 ([#237](https://github.com/web-platform-tests/interop-accessibility/issues/237)) が更新。wpt/html-aam の再構成は [web-platform-tests/wpt#62897](https://github.com/web-platform-tests/wpt/issues/62897) と並行 ([w3c/html-aam#615](https://github.com/w3c/html-aam/issues/615) の本文より)。
- 2026-10-04 aria-at-app v1.26.1 が出た。テスター追加とセキュリティ修正が中心 ([リリース](https://github.com/w3c/aria-at-app/releases/tag/v1.26.1))。
- 2026-10 新しい accessibility WebDriver コマンドで computed property (aria-label、aria-checked など) をテストする tentative テストの追加が提案された ([web-platform-tests/interop-accessibility#248](https://github.com/web-platform-tests/interop-accessibility/issues/248))。
- 2026-10 `ariaNotify()` ([web-platform-tests/interop#1387](https://github.com/web-platform-tests/interop/issues/1387)) と Reference Target ([#1333](https://github.com/web-platform-tests/interop/issues/1333)) の focus area 提案が更新された。
- 2026-09 Interop の Accessibility testing investigation area を来年も続けるかの評価 Issue が立った ([web-platform-tests/interop#1489](https://github.com/web-platform-tests/interop/issues/1489))。
- 2026-09 Reference Target (Cross-Root ARIA) の focus area 提案が更新 ([web-platform-tests/interop#1333](https://github.com/web-platform-tests/interop/issues/1333))。
- 2026-09-23 ARIA-AT CG で TPAC ブレイクアウトの準備 (テスト計画の構成・実行・結果の扱い) を議論 ([w3c-cg/aria-at#1402](https://github.com/w3c-cg/aria-at/issues/1402))。
- 次回 Interop Accessibility 会合は 2026-10-07 ([web-platform-tests/interop-accessibility#246](https://github.com/web-platform-tests/interop-accessibility/issues/246))。

## 関連

- [[specs/wai-aria]]
