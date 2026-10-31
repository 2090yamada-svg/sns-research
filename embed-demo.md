---
layout: default
title: 埋め込みの見本
permalink: /embed-demo/
---
<article class="post"><div class="prose" markdown="1">

# 埋め込みの見本

記事の中で使える部品の見本です。書き方は `_drafts/TEMPLATE.md` にあります。

## 画像（figure）
{% include figure.html src="/assets/img/keiba_backtest.png" alt="100レースのバックテスト結果のグラフ" caption="例: 100レースのバックテスト結果" credit="作成: 本サイト" %}

## YouTube（youtube）
`youtube-nocookie.com` を使い、再生するまでCookieを置かない形で読み込みます。
{% include youtube.html id="148c_3BtvRo" title="【過去5年】天皇賞（秋）2021〜2025｜JRA公式（JRA公式チャンネル）" %}

## Xの投稿（tweet）
<p class="demo-note">見本として載せてよい投稿を確認できていないため、ここは置き場所の説明だけです。記事では <code>{&#37; include tweet.html url="https://x.com/ユーザー名/status/投稿ID" &#37;}</code> と書くと、投稿がカードの形で表示されます。</p>

## 地図（map）
{% include map.html query="静岡駅" %}

## リンクカード（linkcard）
外部サイトの情報は取りに行かず、書いた内容だけで表示します。
{% include linkcard.html url="https://www.jra.go.jp/" title="JRA日本中央競馬会" description="JRAの公式サイト。レース情報やデータが見られます。" image="/assets/img/keiba_stats.png" %}
{% include linkcard.html url="https://github.com/2090yamada-svg/sns-research" title="このサイトのリポジトリ" description="記事のMarkdownや部品はここにあります。" %}

</div></article>
