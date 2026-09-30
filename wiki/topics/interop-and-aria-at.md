---
title: Interop と ARIA-AT (支援技術の相互運用テスト)
type: topic
updated: 2026-09-30
sources: [raw/2026-09-30]
---
# Interop と ARIA-AT

ブラウザと支援技術 (AT) の組み合わせでアクセシビリティが実際に動くかを確かめる取り組み。Interop の Accessibility investigation、ARIA-AT CG、AT Driver、Accessibility Compat Data (ACD) を扱う。

## 現状

- **ARIA-AT**: Tri-State Checkbox のテスト計画は 6 回の実行のうち 2 回が残り (JAWS)。HTML Button のテスト計画は JAWS・NVDA・VoiceOver で完了。VoiceOver の自動実行は macOS 15 では動くが、macOS 26 では音声がハーネスに取り込まれない ([ARIA-AT 2026-09-23](https://www.w3.org/2026/09/23-aria-at-minutes.html)、[w3c/aria-at-app#1671](https://github.com/w3c/aria-at-app/issues/1671))。
- JAWS 2026 が Vispero アカウントを求めるようになり、テスト環境での追跡・ライセンスが懸念になっている ([ARIA-AT 2026-09-23](https://www.w3.org/2026/09/23-aria-at-minutes.html))。
- **AT Driver** (AT を自動操作する仕様): Sovereign Tech Agency の資金を得た。BTT charter から ARIA charter への移管を予定 ([w3c/aria#2915](https://github.com/w3c/aria/issues/2915)、[w3c/strategy#558](https://github.com/w3c/strategy/issues/558))。
- **ACD**: WPT と ARIA-AT の結果から、Baseline / BCD にアクセシビリティのサポート情報を載せる計画。「supported」をどう判定し、どう見せるかを ARIA WG に問うている ([w3c/aria#2916](https://github.com/w3c/aria/issues/2916))。

## 最近の動き

- 2026-09 Interop の Accessibility testing investigation area を来年も続けるかの評価 Issue が立った ([web-platform-tests/interop#1489](https://github.com/web-platform-tests/interop/issues/1489))。
- 2026-09 Reference Target (Cross-Root ARIA) の focus area 提案が更新 ([web-platform-tests/interop#1333](https://github.com/web-platform-tests/interop/issues/1333))。
- 2026-09-23 ARIA-AT CG で TPAC ブレイクアウトの準備 (テスト計画の構成・実行・結果の扱い) を議論 ([w3c-cg/aria-at#1402](https://github.com/w3c-cg/aria-at/issues/1402))。
- 次回 Interop Accessibility 会合は 2026-10-07 ([web-platform-tests/interop-accessibility#246](https://github.com/web-platform-tests/interop-accessibility/issues/246))。

## 関連

- [[specs/wai-aria]]
