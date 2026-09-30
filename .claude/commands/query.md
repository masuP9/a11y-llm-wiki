---
description: wiki を使って質問に答え、価値のある答えは wiki に File back する
argument-hint: "<質問>"
---

# /query $ARGUMENTS

1. `wiki/index.md` から関連ページを特定して読む。足りなければ `raw/` と一次ソース (WebFetch) を当たる。
2. 出典リンク付きで答える。wiki に無い情報で答えた部分はそう明示する。
3. 答えが今後も参照する価値を持つなら (仕様間の関係の整理、経緯の説明、比較など)、
   該当ページに追記するか `wiki/topics/` に新規ページを作り、index.md と log.md を更新する。
