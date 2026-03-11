# DevTools Japan デプロイ完全ガイド

## 所要時間：約30分

---

## ステップ1：事前準備（5分）

### 必要なアカウント
- **GitHub**：https://github.com （コード管理・Vercelと連携）
- **Vercel**：https://vercel.com （ホスティング・無料）

### 必要なツール
```bash
# Gitがインストールされているか確認
git --version

# なければインストール（Mac）
brew install git

# なければインストール（Windows）
# https://git-scm.com/download/win からダウンロード
```

---

## ステップ2：GitHubリポジトリ作成（5分）

### 2-1. ダウンロードしたファイルを整理
Claudeからダウンロードした全ファイルを1つのフォルダにまとめます。

```
devtools-japan/
├── index.html                    ← ポータルページ
├── sitemap.xml                   ← SEO用サイトマップ
├── robots.txt                    ← クローラー設定
├── privacy/index.html            ← プライバシーポリシー
├── about/index.html              ← サイトについて
├── contact/index.html            ← お問い合わせ
├── tool-01-moji-counter/index.html
├── tool-02-password-gen/index.html
├── ...
└── tool-50-htaccess-gen/index.html
```

### 2-2. Gitで初期化してGitHubにプッシュ

```bash
cd devtools-japan

# Git初期化
git init
git add .
git commit -m "Initial commit: 50 tools + portal"

# GitHubでリポジトリを作成した後
git remote add origin https://github.com/あなたのユーザー名/devtools-japan.git
git branch -M main
git push -u origin main
```

---

## ステップ3：Vercelでデプロイ（5分）

### 3-1. Vercelにログイン
1. https://vercel.com にアクセス
2. 「Sign Up」→「Continue with GitHub」でGitHubアカウントと連携

### 3-2. プロジェクトをインポート
1. ダッシュボードで「Add New...」→「Project」
2. GitHubリポジトリ一覧から「devtools-japan」を選択
3. 設定はデフォルトのままでOK
   - Framework Preset: Other
   - Root Directory: ./
4. 「Deploy」をクリック

### 3-3. デプロイ完了
- 1〜2分でデプロイが完了
- `https://devtools-japan.vercel.app` のようなURLが発行される
- このURLで即座にサイトにアクセス可能

---

## ステップ4：独自ドメイン設定（10分）

### 4-1. ドメインを取得
推奨レジストラ：
- **ムームードメイン**（https://muumuu-domain.com）— 日本語対応
- **Cloudflare Registrar**（https://www.cloudflare.com/products/registrar/）— 最安値

候補ドメイン例：
- `devtools-japan.com`
- `devtools.jp`
- `dt-japan.com`

費用：年間 約1,000〜2,000円

### 4-2. Vercelでドメインを設定
1. Vercelダッシュボード → プロジェクト → Settings → Domains
2. 購入したドメインを入力して「Add」
3. 表示されるDNSレコード（AレコードまたはCNAME）をレジストラ側で設定

### 4-3. DNSレコード設定（レジストラ側）
```
タイプ: A
名前: @
値: 76.76.21.21

タイプ: CNAME
名前: www
値: cname.vercel-dns.com
```

※ DNS反映まで最大48時間（通常は30分〜数時間）

### 4-4. SSL証明書
Vercelが自動でHTTPS化してくれるため、設定不要。

---

## ステップ5：Google Search Console登録（5分）

### 5-1. Search Consoleにアクセス
1. https://search.google.com/search-console にアクセス
2. 「プロパティを追加」→「URLプレフィックス」を選択
3. ドメインのURLを入力（例：https://devtools-japan.com）

### 5-2. 所有権確認
- HTMLファイルをダウンロードしてサイトのルートに配置する方法が簡単
- または、Vercelのドメイン設定でDNS TXTレコードを追加

### 5-3. サイトマップ送信
1. Search Console → サイトマップ
2. `sitemap.xml` と入力して「送信」
3. ステータスが「成功」になればOK

---

## ステップ6：Google AdSense申請（デプロイ後1〜2週間後）

### 申請条件（目安）
- ✅ 独自ドメイン（必須）
- ✅ プライバシーポリシーページ（作成済み）
- ✅ お問い合わせページ（作成済み）
- ✅ サイト概要ページ（作成済み）
- ✅ コンテンツが十分にある（50ページ以上 — 達成済み）
- ⬜ サイトが一定期間運用されている（1〜2週間以上）

### 申請手順
1. https://www.google.com/adsense にアクセス
2. 「お申し込み」→ サイトURLとメールアドレスを入力
3. AdSenseのコードを `<head>` タグ内に追加
4. 審査結果を待つ（通常1〜14日）

### AdSenseコード設置方法
審査コードが発行されたら、全HTMLファイルの `<head>` 内に追加：

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-あなたのID" crossorigin="anonymous"></script>
```

一括追加コマンド：
```bash
# 全HTMLファイルに一括挿入
find . -name "index.html" -exec sed -i 's|</head>|<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-あなたのID" crossorigin="anonymous"></script>\n</head>|' {} \;
```

### 審査通過後
各ツールの「広告スペース」プレースホルダーを実際のAdSenseコードに差し替え：

```html
<!-- 差し替え前 -->
<div class="ad-slot">広告スペース（Google AdSense 728×90）</div>

<!-- 差し替え後 -->
<div class="ad-slot">
  <ins class="adsbygoogle"
    style="display:block"
    data-ad-client="ca-pub-あなたのID"
    data-ad-slot="あなたのスロットID"
    data-ad-format="auto"
    data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
```

---

## ステップ7：Google Analytics設定（任意・推奨）

### 7-1. GA4プロパティ作成
1. https://analytics.google.com にアクセス
2. プロパティを作成
3. 測定IDを取得（G-XXXXXXXXXX 形式）

### 7-2. トラッキングコード設置
全HTMLの `<head>` に追加：
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-あなたのID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-あなたのID');
</script>
```

---

## 運用後のメンテナンス

### コンテンツ更新
```bash
# ファイルを編集した後
git add .
git commit -m "ツール追加/修正の説明"
git push

# Vercelが自動でデプロイしてくれる（約30秒〜1分）
```

### 月次チェックリスト
- [ ] Search Consoleでインデックス状況確認
- [ ] AdSense収益確認
- [ ] Analytics でPV・流入キーワード確認
- [ ] 新規ツールの追加検討
- [ ] 既存ツールの改善（ユーザーフィードバック対応）

---

## コスト一覧

| 項目 | 費用 |
|------|------|
| Vercel ホスティング | 無料 |
| ドメイン | 年間 約1,000〜2,000円 |
| Google AdSense | 無料 |
| Google Analytics | 無料 |
| Search Console | 無料 |
| **年間合計** | **約1,000〜2,000円** |

---

## トラブルシューティング

### Vercelデプロイが失敗する
→ ファイル名に日本語や特殊文字が含まれていないか確認

### ドメインがつながらない
→ DNS設定後、最大48時間待つ。`dig ドメイン名` で確認可能

### AdSense審査に落ちた
→ 最低2週間の運用実績を作ってから再申請。コンテンツ量は十分なので、運用期間が足りていない可能性が高い

### ツールが動かない
→ ブラウザのコンソール（F12 → Console）でエラーメッセージを確認
