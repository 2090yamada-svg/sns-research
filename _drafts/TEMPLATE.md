---
layout: post
title: "記事タイトル"
date: 2026-11-02 12:00:00 +0900
description: "トップページのカードに出る短い説明（60〜80字くらい）"
tags: [SNS, 調査]
image: /assets/img/posts/スラッグ.jpg
---

<!--
使い方:
1. このファイルを _posts/YYYY-MM-DD-スラッグ.md にコピーします（スラッグは英数字とハイフン）。
2. 上の front matter を書き換えます。image は assets/img/posts/ に置いた画像（300KB以下のjpg推奨）。
3. 下の部品は必要なものだけ残して消してください。
-->

## 見出し
本文はMarkdownで書きます。

### 画像（キャプション・クレジット付き）
{% include figure.html src="/assets/img/posts/スラッグ.jpg" alt="画像の説明" caption="図1: キャプション" credit="画像: Canvaで作成" %}

### YouTube動画（idは watch?v= の後ろの11文字）
{% include youtube.html id="動画ID" title="動画のタイトル" %}

### Xの投稿
{% include tweet.html url="https://x.com/ユーザー名/status/投稿ID" %}

### Googleマップ
{% include map.html query="静岡駅" %}

### リンクカード（外部の情報は取りに行かず、書いた内容だけ表示）
{% include linkcard.html url="https://example.com/" title="ページのタイトル" description="ひとこと説明" image="/assets/img/posts/スラッグ.jpg" %}

<!-- 注意: よそのサイトの写真は直接載せず、Canva画像やフリー素材、公式の埋め込みを使います。 -->
