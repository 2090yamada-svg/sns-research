# SNS調査ブログ

公開ページ: https://2090yamada-svg.github.io/sns-research/

## 記事一覧
- [Xの年齢層調査](https://2090yamada-svg.github.io/sns-research/2026/11/01/x-age/)（2026-11-01）
- [Xに似たSNSの比較](https://2090yamada-svg.github.io/sns-research/2026/11/01/x-like-sns/)（2026-11-01）
- [国ごとのSNS利用状況](https://2090yamada-svg.github.io/sns-research/2026/11/01/sns-by-country/)（2026-11-01）
- [AI競馬予想バックテスト500レース](https://2090yamada-svg.github.io/sns-research/2026/11/01/keiba-backtest-500/)（2026-11-01）
- [スマホの中の「孤独」— アメリカ・韓国・日本はどう呼んでいるか](https://2090yamada-svg.github.io/sns-research/2026/11/01/loneliness/)（2026-11-01）
- [「ただいま」の前にする仕事 — 介護をアメリカ・韓国・日本はどう数えているか](https://2090yamada-svg.github.io/sns-research/2026/11/01/caregiving/)（2026-11-01）
- [「2.5%」という約束 — 障害のある人の働き方をアメリカ・韓国・日本はどう測っているか](https://2090yamada-svg.github.io/sns-research/2026/11/01/disability-work/)（2026-11-01）
- [戦争はタイムラインから届く — アメリカ・韓国・日本、ニュースの入口はどう違うか](https://2090yamada-svg.github.io/sns-research/2026/11/01/war-news-sns/)（2026-11-01）

## 記事の追加方法
1. `_posts/` に `YYYY-MM-DD-英数字のタイトル.md` というファイルを作ります。
2. 先頭に次のような情報を書きます。
   ```
   ---
   layout: post
   title: "記事タイトル"
   date: 2026-11-02
   ---
   ```
3. 本文をMarkdownで書き、mainブランチにpushすると数分で公開されます。
4. このREADMEの記事一覧にも1行追加します。

## 画像と埋め込み
- 記事のひな形: `_drafts/TEMPLATE.md`（front matter と各部品の書き方の例）。見本ページ: https://2090yamada-svg.github.io/sns-research/embed-demo/
- カード画像: `assets/img/posts/<スラッグ>.jpg`（300KB以下）を置き、front matter に `image:` を書きます。
- 使える部品（`_includes/`、すべて遅延読み込み・スマホ対応）:
  - `{% include figure.html src="..." alt="..." caption="..." credit="..." %}` 画像＋キャプション＋クレジット
  - `{% include youtube.html id="動画ID" title="..." %}` YouTube（youtube-nocookie.com）
  - `{% include tweet.html url="https://x.com/.../status/..." %}` Xの投稿
  - `{% include map.html query="場所" %}` Googleマップ
  - `{% include linkcard.html url="..." title="..." description="..." image="..." %}` リンクカード（外部取得なし）
- よそのサイトの写真は直接載せず、Canva画像・フリー素材・公式の埋め込みを使います。
