#!/usr/bin/env python3
"""
DevTools Japan — AdSense再審査対策スクリプト（全部入り）
1. ads.txt 設置
2. aboutページ充実化
3. 全50ツールのSEOテキスト充実化（300文字以上に統一）
4. ブログ記事ページ2本を新規作成

使い方:
  cd ~/Desktop/devtools-japan-complete
  python3 adsense_resubmit.py
"""

import os
import re

BASE = os.getcwd()

if not os.path.exists(os.path.join(BASE, "index.html")):
    print("エラー: ~/Desktop/devtools-japan-complete で実行してください")
    exit(1)

print("=" * 60)
print("  DevTools Japan — AdSense再審査対策")
print("=" * 60)

# ============================================================
# 1. ads.txt 設置
# ============================================================
print("\n📋 1. ads.txt を設置中...")

ads_txt_content = "google.com, pub-7300747004702072, DIRECT, f08c47fec0942fa0\n"
ads_txt_path = os.path.join(BASE, "ads.txt")

with open(ads_txt_path, "w", encoding="utf-8") as f:
    f.write(ads_txt_content)
print("  ✅ ads.txt を作成しました")


# ============================================================
# 2. aboutページ充実化
# ============================================================
print("\n📋 2. aboutページを充実化中...")

about_html = """<!DOCTYPE html>
<html lang="ja">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-E27Q8YTG7L');
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072"
     crossorigin="anonymous"></script>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevTools Japanについて | 開発者・デザイナー向け無料オンラインツール集</title>
    <meta name="description" content="DevTools Japanは日本の開発者・デザイナー・フリーランス向けに50種類以上の無料オンラインツールを提供するサービスです。サイトの運営方針・特徴・よくある質問をご紹介します。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
    <link rel="canonical" href="https://www.devtools-japan.com/about/">
    <meta property="og:title" content="DevTools Japanについて | 無料オンラインツール集">
    <meta property="og:description" content="日本の開発者・デザイナー・フリーランス向けに50種類以上の無料オンラインツールを提供">
    <meta property="og:url" content="https://www.devtools-japan.com/about/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="DevTools Japanについて | 無料オンラインツール集">
    <meta name="twitter:description" content="日本の開発者・デザイナー・フリーランス向けに50種類以上の無料オンラインツールを提供">
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"WebSite","name":"DevTools Japan","description":"開発者・デザイナー・フリーランス向けの無料オンラインツール集","url":"https://www.devtools-japan.com"}
    </script>
    <style>
        :root{--bg:#f7f8fb;--bg-card:#ffffff;--border:#e0e2ed;--text:#1e1e35;--text2:#5a5f78;--text3:#9498b0;--accent:#10b981;--radius:12px}
        ::selection{background:rgba(16,185,129,0.15);color:#1e1e35}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;line-height:2}
        .container{max-width:800px;margin:0 auto;padding:40px 20px}
        a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
        h1{font-size:1.6rem;font-weight:700;margin-bottom:8px;color:var(--accent)}
        h2{font-size:1.15rem;font-weight:600;margin-top:36px;margin-bottom:12px;color:var(--text);border-bottom:2px solid var(--accent);padding-bottom:6px;display:inline-block}
        h3{font-size:1rem;font-weight:600;margin-top:24px;margin-bottom:8px;color:var(--text)}
        p{margin-bottom:16px;color:var(--text2);font-size:0.9rem}
        .sub{color:var(--text3);font-size:0.8rem;margin-bottom:32px}
        .back{display:inline-flex;align-items:center;gap:6px;margin-bottom:24px;font-size:0.8rem;color:var(--text3);text-decoration:none}
        .card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin:20px 0}
        .stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:20px 0}
        @media(max-width:600px){.stats{grid-template-columns:1fr}}
        .stat{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:16px;text-align:center}
        .stat .num{font-size:1.8rem;font-weight:700;color:var(--accent)}
        .stat .label{font-size:0.75rem;color:var(--text3);margin-top:4px}
        ul{margin:0 0 16px 20px;color:var(--text2);font-size:0.9rem}
        li{margin-bottom:6px}
        footer{text-align:center;margin-top:60px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}
    </style>
</head>
<body>
<div class="container">
    <a href="/" class="back"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8h5z"/></svg> DevTools Japan トップへ</a>
    <h1>DevTools Japan について</h1>
    <p class="sub">日本の開発者・デザイナー・フリーランスのための無料オンラインツール集</p>

    <div class="stats">
        <div class="stat"><div class="num">50+</div><div class="label">無料ツール</div></div>
        <div class="stat"><div class="num">30+</div><div class="label">無料API</div></div>
        <div class="stat"><div class="num">0円</div><div class="label">利用料金</div></div>
    </div>

    <h2>DevTools Japan とは</h2>
    <p>DevTools Japanは、日本の開発者・Webデザイナー・フリーランスの方々が日常的に使う便利ツールを、ブラウザだけで無料で使えるようにまとめたオンラインツール集です。会員登録やソフトのインストールは一切不要で、サイトにアクセスするだけですぐに使い始められます。</p>
    <p>すべてのツールはブラウザ内で動作し、入力したデータがサーバーに送信されることはありません。プライバシーを重視した設計になっています。</p>

    <h2>提供しているツール</h2>
    <p>現在50種類以上のツールを以下のカテゴリで提供しています。</p>

    <h3>開発者向けツール</h3>
    <p>JSON整形、正規表現テスト、Base64変換、URLエンコード、テキスト比較（Diff）、ハッシュ生成、UUID生成、タイムスタンプ変換、Cron式ジェネレーター、chmod計算、.htaccess生成、SQLフォーマッター、JWTデコーダーなど、プログラミングの日常作業を効率化するツールを揃えています。</p>

    <h3>デザイナー向けツール</h3>
    <p>カラーコード変換、カラーパレット生成、CSSグラデーション生成、CSSボックスシャドウ生成、SNS画像サイズ一覧、OGPプレビュー、アスペクト比計算、画像圧縮、Favicon生成、プレースホルダー画像生成など、Webデザインの作業を支援するツールを提供しています。</p>

    <h3>日本特化ツール</h3>
    <p>和暦西暦変換、確定申告シミュレーター、源泉徴収税計算、全角半角変換、文章校正チェッカー、読み上げ時間計算など、日本の開発者・フリーランスに特化したツールも充実しています。</p>

    <h3>ライティングツール</h3>
    <p>文字数カウンター、テキスト統計、英文ワードカウンター、ダミーテキスト生成、テキスト反転など、文章作成をサポートするツールを提供しています。</p>

    <h2>DevTools Japan API</h2>
    <p>Webツールに加えて、<a href="https://api.devtools-japan.com">DevTools Japan API</a>として30本以上の無料APIも提供しています。和暦変換、祝日判定、郵便番号検索、全角半角変換、ハッシュ生成など、認証不要で即座に利用できるREST APIです。あなたのアプリやサービスに数行のコードで組み込めます。</p>

    <h2>運営方針</h2>
    <div class="card">
        <h3>完全無料</h3>
        <p>すべてのWebツールは完全無料で利用できます。会員登録も不要です。広告収入によってサービスの運営を維持しています。</p>

        <h3>プライバシー重視</h3>
        <p>ツールはすべてブラウザ内（JavaScript）で動作します。入力したテキスト、数値、画像などのデータがDevTools Japanのサーバーに送信されることはありません。安心してご利用ください。</p>

        <h3>継続的な改善</h3>
        <p>ユーザーのフィードバックに基づいて、既存ツールの改善と新規ツールの追加を継続的に行っています。「こんなツールがほしい」というご要望がありましたら、<a href="/contact/">お問い合わせページ</a>からお気軽にご連絡ください。</p>
    </div>

    <h2>よくある質問</h2>
    <div class="card">
        <h3>本当に無料ですか？</h3>
        <p>はい、すべてのWebツールは完全無料です。隠れた課金や有料プランはありません。</p>

        <h3>会員登録は必要ですか？</h3>
        <p>Webツールの利用に会員登録は不要です。API（有料機能）を利用する場合のみ、メールアドレスでのAPIキー取得が必要です。</p>

        <h3>入力したデータは保存されますか？</h3>
        <p>いいえ。すべてのツールはブラウザ内で処理されるため、入力データがサーバーに送信・保存されることはありません。</p>

        <h3>スマートフォンでも使えますか？</h3>
        <p>はい。すべてのツールはレスポンシブ対応しており、スマートフォンやタブレットでも快適に利用できます。</p>

        <h3>商用利用は可能ですか？</h3>
        <p>ツールの処理結果（変換結果、生成データ等）は自由にご利用いただけます。ツール自体の再配布やコピーはご遠慮ください。</p>
    </div>

    <h2>お問い合わせ</h2>
    <p>バグ報告、機能リクエスト、ご意見・ご感想は<a href="/contact/">お問い合わせページ</a>からお寄せください。</p>

    <footer>
        <p style="margin-bottom:8px">&copy; 2026 DevTools Japan — 無料オンラインツール</p>
        <p style="font-size:0.65rem"><a href="/about/" style="color:inherit;text-decoration:none;margin:0 8px">サイトについて</a> | <a href="/privacy/" style="color:inherit;text-decoration:none;margin:0 8px">プライバシーポリシー</a> | <a href="/contact/" style="color:inherit;text-decoration:none;margin:0 8px">お問い合わせ</a></p>
    </footer>
</div>
</body>
</html>"""

about_path = os.path.join(BASE, "about", "index.html")
with open(about_path, "w", encoding="utf-8") as f:
    f.write(about_html)
print("  ✅ about/index.html を充実化しました")


# ============================================================
# 3. 全50ツールのSEOテキスト充実化
# ============================================================
print("\n📋 3. 全50ツールのSEOテキストを充実化中...")

# 各ツールのSEOテキスト（300文字以上の充実したコンテンツ）
SEO_TEXTS = {
    "tool-02-password-gen": """
        <h2>パスワード生成ツールの使い方</h2>
        <p>セキュアなランダムパスワードを瞬時に生成する無料ツールです。パスワードの長さ（8〜128文字）や、使用する文字種（大文字・小文字・数字・記号）を自由に指定できます。</p>
        <h3>なぜ強いパスワードが必要か</h3>
        <p>短いパスワードや推測されやすいパスワードは、ブルートフォース攻撃（総当たり攻撃）で短時間で突破されてしまいます。8文字の英小文字のみのパスワードは数分で解読される一方、16文字で大文字・小文字・数字・記号を含むパスワードは数百年以上かかると言われています。このツールで生成するパスワードは暗号学的に安全な乱数を使用しています。</p>
        <h3>パスワード管理のコツ</h3>
        <p>サービスごとに異なるパスワードを使うことが推奨されています。すべてを覚えるのは現実的ではないため、パスワードマネージャー（1Password、Bitwarden等）と組み合わせて使うのが効果的です。このツールで生成したパスワードはブラウザ内で処理され、サーバーに送信されることはありません。</p>""",

    "tool-03-json-formatter": """
        <h2>JSON整形ツールの使い方</h2>
        <p>圧縮されたJSON文字列を見やすくインデント整形する無料ツールです。APIのレスポンス確認、設定ファイルの編集、デバッグ作業など、開発者が日常的にJSONを扱う場面で活躍します。</p>
        <h3>JSON整形が必要な場面</h3>
        <p>APIから返ってくるJSONレスポンスは、多くの場合、改行やインデントなしの1行で圧縮されています。そのままでは構造を把握するのが困難です。このツールにペーストするだけで、階層構造が一目でわかるように整形されます。構文エラーがある場合はエラー箇所も表示します。</p>
        <h3>対応する操作</h3>
        <p>インデント整形（2スペース/4スペース/タブ）、JSON圧縮（ミニファイ）、構文バリデーション、キーのソートに対応しています。大きなJSONファイル（数MBまで）もブラウザ内で高速に処理できます。入力データがサーバーに送信されることはありません。</p>""",

    "tool-04-qr-generator": """
        <h2>QRコード生成ツールの使い方</h2>
        <p>テキストやURLからQRコードを即座に生成できる無料ツールです。名刺のURL、Wi-Fiの接続情報、イベントの参加URLなど、さまざまな情報をQRコードに変換できます。</p>
        <h3>QRコードの活用場面</h3>
        <p>ビジネスでは名刺にWebサイトのURLをQRコードとして印刷したり、店舗の決済用QRコードとして活用されています。イベントでは参加登録ページへの誘導、教育現場では教材へのリンク共有に使われます。Wi-Fiの接続情報をQRコードにすれば、ゲストに簡単にネットワーク接続を提供できます。</p>
        <h3>生成されるQRコードについて</h3>
        <p>生成されたQRコードはPNG画像としてダウンロードできます。サイズやエラー訂正レベルをカスタマイズ可能。すべてブラウザ内で処理され、入力したデータがサーバーに送信されることはありません。商用利用も自由です。</p>""",

    "tool-05-color-converter": """
        <h2>カラーコード変換ツールの使い方</h2>
        <p>HEX・RGB・HSLのカラーコードを相互変換する無料ツールです。CSSのカラー指定、デザインツール間での色の受け渡し、配色の調整など、Web開発・デザインで頻繁に使う変換を瞬時に行えます。</p>
        <h3>対応するカラー形式</h3>
        <p>HEX（#FF5733）、RGB（rgb(255, 87, 51)）、HSL（hsl(11, 100%, 60%)）の3形式に対応しています。いずれかの値を入力すると、他の2形式にリアルタイムで変換されます。CSSにそのままコピペできる形式で出力します。</p>
        <h3>カラーピッカー機能</h3>
        <p>カラーピッカーで視覚的に色を選択することもできます。選択した色のHEX/RGB/HSL値が即座に表示されるので、デザインの微調整に便利です。すべてブラウザ上で動作し、データがサーバーに送信されることはありません。</p>""",

    "tool-06-base64": """
        <h2>Base64変換ツールの使い方</h2>
        <p>テキストや画像をBase64形式にエンコード・デコードする無料ツールです。メール添付のエンコード、データURIスキームでの画像埋め込み、APIでのバイナリデータ送受信など、さまざまな開発場面で活用できます。</p>
        <h3>Base64が使われる場面</h3>
        <p>Base64は、バイナリデータをテキスト形式（ASCII文字のみ）で表現するためのエンコード方式です。HTMLやCSSに小さな画像を直接埋め込む「データURI」、メールの添付ファイル（MIME）、JWTトークンのペイロード部分など、テキストベースのプロトコルでバイナリデータを扱う必要がある場面で広く使われています。</p>
        <h3>注意点</h3>
        <p>Base64エンコードするとデータサイズが約33%増加します。大きなファイルのエンコードには適していません。すべてブラウザ内で処理され、データがサーバーに送信されることはありません。</p>""",

    "tool-07-url-encode": """
        <h2>URLエンコード・デコードツールの使い方</h2>
        <p>URLに含められない文字（日本語、スペース、特殊記号等）をパーセントエンコーディングに変換する無料ツールです。検索パラメータの生成、API呼び出しのURL構築、リダイレクトURLの作成などに使います。</p>
        <h3>URLエンコードとは</h3>
        <p>URLにはASCII文字の一部しか使用できないため、日本語やスペース、一部の記号はパーセントエンコーディング（%XX形式）に変換する必要があります。例えば「東京」は「%E6%9D%B1%E4%BA%AC」になります。このツールでは、エンコードとデコードの両方向に対応しています。</p>
        <h3>開発での活用</h3>
        <p>APIのクエリパラメータに日本語を含める場合や、リダイレクトURLをパラメータとして渡す場合に必須の処理です。すべてブラウザ内で処理されます。</p>""",

    "tool-08-regex-tester": """
        <h2>正規表現テスターの使い方</h2>
        <p>正規表現（regex）パターンをリアルタイムでテストできる無料ツールです。パターンを入力するとテスト文字列に対するマッチ結果が即座にハイライト表示されます。メールアドレスや電話番号のバリデーション、ログファイルからのデータ抽出、テキストの検索・置換パターンの作成などに活用できます。</p>
        <h3>正規表現の基本</h3>
        <p>正規表現は文字列のパターンマッチングに使われる表記法です。例えば「\\d{3}-\\d{4}」は郵便番号（810-0001形式）にマッチし、「[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}」はメールアドレスにマッチします。このツールでパターンを試しながら、正しく動作することを確認できます。</p>
        <h3>フラグ対応</h3>
        <p>グローバルマッチ（g）、大文字小文字無視（i）、複数行モード（m）のフラグに対応しています。キャプチャグループの内容も表示されるので、複雑なパターンのデバッグに便利です。</p>""",

    "tool-09-diff": """
        <h2>テキスト比較（Diff）ツールの使い方</h2>
        <p>2つのテキストを比較し、差分（追加・削除・変更）を行単位でハイライト表示する無料ツールです。コードレビュー、ドキュメントの変更確認、設定ファイルの差分チェックなど、テキストの変更箇所を素早く把握したい場面で活躍します。</p>
        <h3>差分の表示方式</h3>
        <p>追加された行は緑色、削除された行は赤色でハイライトされ、変更箇所が一目でわかります。行番号付きの対比表示で、どの行がどう変わったかを正確に確認できます。</p>
        <h3>活用場面</h3>
        <p>プルリクエストのレビュー前の事前確認、設定ファイルの本番環境とステージング環境の差分チェック、翻訳テキストの更新確認、契約書の改訂箇所の特定などに使われています。すべてブラウザ内で処理されます。</p>""",

    "tool-10-image-compress": """
        <h2>画像圧縮ツールの使い方</h2>
        <p>JPEG・PNG・WebP画像のファイルサイズを削減する無料ツールです。Webサイトの表示速度改善、メール添付サイズの削減、ストレージ容量の節約に活用できます。画質を維持しながらファイルサイズを大幅に削減します。</p>
        <h3>なぜ画像圧縮が重要か</h3>
        <p>Webサイトのページ読み込み時間の大部分は画像のダウンロードに費やされます。Googleのページスピード評価にも画像サイズが影響するため、SEO対策としても画像圧縮は重要です。このツールでは、視覚的な品質をほとんど損なわずにファイルサイズを50〜80%削減できます。</p>
        <h3>プライバシー</h3>
        <p>画像の圧縮処理はすべてブラウザ内で完結します。アップロードした画像がサーバーに送信されることはありません。</p>""",

    "tool-11-markdown-preview": """
        <h2>Markdownプレビューツールの使い方</h2>
        <p>Markdown記法で書いたテキストをリアルタイムでHTML表示に変換する無料ツールです。GitHubのREADME作成、ブログ記事の下書き、技術ドキュメントの執筆など、Markdownを使う場面で即座にプレビューを確認できます。</p>
        <h3>対応するMarkdown記法</h3>
        <p>見出し（#）、太字・斜体、リスト（箇条書き・番号付き）、リンク、画像、コードブロック（シンタックスハイライト対応）、引用、テーブル、水平線、タスクリストに対応しています。GitHub Flavored Markdown（GFM）に準拠しています。</p>
        <h3>活用場面</h3>
        <p>GitHubのREADME.mdの作成、Qiita/Zennの技術記事の下書き、社内ドキュメントの執筆、プレゼン資料の原稿作成などに使われています。左側にMarkdownを入力すると、右側にリアルタイムでプレビューが表示されます。</p>""",

    "tool-12-wareki": """
        <h2>和暦西暦変換ツールの使い方</h2>
        <p>西暦と和暦（令和・平成・昭和・大正・明治）を相互変換する無料ツールです。業務システムの日付表示、公的書類の日付変換、履歴書の年号変換など、日本特有の日付処理で活躍します。</p>
        <h3>対応する元号</h3>
        <p>令和（2019年5月1日〜）、平成（1989年1月8日〜2019年4月30日）、昭和（1926年12月25日〜1989年1月7日）、大正（1912年7月30日〜1926年12月24日）、明治（1868年1月25日〜1912年7月29日）に対応しています。元号の境界日も正確に処理します。</p>
        <h3>よく使われる変換例</h3>
        <p>「令和8年 → 2026年」「平成元年 → 1989年」「昭和64年 → 1989年」など。昭和64年と平成元年が同じ1989年であるような、元号をまたぐ変換も正しく処理します。すべてブラウザ上で動作します。</p>""",

    "tool-13-csv-json": """
        <h2>CSV⇔JSON変換ツールの使い方</h2>
        <p>CSVファイルとJSON形式を相互変換する無料ツールです。ExcelからエクスポートしたCSVをJSON形式に変換してAPIに投入したり、APIのJSONレスポンスをCSVに変換してExcelで分析したりする場面で活用できます。</p>
        <h3>CSV→JSON変換</h3>
        <p>CSVの1行目をヘッダー（キー名）として使用し、2行目以降をオブジェクトの配列に変換します。タブ区切り（TSV）にも対応しています。</p>
        <h3>JSON→CSV変換</h3>
        <p>JSON配列をCSV形式に変換します。ネストされたオブジェクトはフラットに展開されます。変換結果はコピーまたはダウンロードできます。すべてブラウザ内で処理されます。</p>""",

    "tool-14-html-escape": """
        <h2>HTML特殊文字変換ツールの使い方</h2>
        <p>HTMLの特殊文字（<, >, &, " 等）をHTMLエンティティ（&lt; &gt; &amp; 等）に変換する無料ツールです。XSS（クロスサイトスクリプティング）対策、HTMLテンプレートへのデータ埋め込み、技術ブログでのコード表示などに使います。</p>
        <h3>エスケープが必要な理由</h3>
        <p>ユーザーが入力したテキストをそのままHTMLに埋め込むと、悪意のあるスクリプトが実行されるXSS脆弱性が発生します。特に &lt;script&gt; タグを含む入力は必ずエスケープする必要があります。このツールで変換結果を確認しながら、安全なHTML出力を構築できます。</p>
        <h3>逆変換（アンエスケープ）にも対応</h3>
        <p>HTMLエンティティを元の文字に戻すアンエスケープ機能も搭載しています。すべてブラウザ内で処理されます。</p>""",

    "tool-15-case-converter": """
        <h2>文字列ケース変換ツールの使い方</h2>
        <p>テキストの大文字・小文字を変換する無料ツールです。プログラミングでの命名規則変換（camelCase、snake_case、kebab-case、PascalCase等）や、文章の大文字小文字統一に使います。</p>
        <h3>対応する変換パターン</h3>
        <p>UPPER CASE（全大文字）、lower case（全小文字）、Title Case（各単語の先頭大文字）、camelCase（キャメルケース）、snake_case（スネークケース）、kebab-case（ケバブケース）、PascalCase（パスカルケース）、CONSTANT_CASE（定数ケース）に対応しています。</p>
        <h3>開発での活用</h3>
        <p>変数名・関数名・クラス名の命名規則をチーム内で統一する際に便利です。データベースのカラム名（snake_case）をフロントエンドの変数名（camelCase）に変換するなど、異なる命名規則間の変換にも使えます。</p>""",

    "tool-16-timestamp": """
        <h2>タイムスタンプ変換ツールの使い方</h2>
        <p>Unixタイムスタンプと人間が読める日時形式を相互変換する無料ツールです。サーバーログの解析、APIレスポンスの日時確認、データベースのタイムスタンプ検証など、開発者がタイムスタンプを扱う場面で即座に変換できます。</p>
        <h3>Unixタイムスタンプとは</h3>
        <p>Unixタイムスタンプは、1970年1月1日00:00:00 UTC（Unixエポック）からの経過秒数で日時を表現する形式です。タイムゾーンに依存しないため、国際的なシステム間での日時データのやり取りに広く使われています。10桁（秒）と13桁（ミリ秒）の両方に対応しています。</p>
        <h3>JST（日本標準時）表示</h3>
        <p>変換結果にはUTCとJST（UTC+9）の両方を表示します。日本のサービス開発で使いやすいよう、JSTでの表示を標準で提供しています。</p>""",

    "tool-17-hash": """
        <h2>ハッシュ生成ツールの使い方</h2>
        <p>テキストのハッシュ値（MD5・SHA-1・SHA-256・SHA-512）を生成する無料ツールです。ファイルの整合性チェック、パスワードのハッシュ化確認、データの一意性検証などに使います。</p>
        <h3>ハッシュアルゴリズムの選び方</h3>
        <p>MD5は高速ですが衝突耐性が低く、セキュリティ用途には推奨されません。SHA-256は現在最も広く使われており、ブロックチェーンやSSL証明書にも使用されています。SHA-512はより長いハッシュ値を生成し、高いセキュリティが求められる場面に適しています。</p>
        <h3>活用場面</h3>
        <p>ダウンロードしたファイルが改ざんされていないかをチェックサムで検証する、APIのリクエスト署名を生成する、パスワードをハッシュ化して保存する（※本番環境ではbcrypt等の専用ライブラリを推奨）などの場面で使われています。</p>""",

    "tool-18-dummy-text": """
        <h2>ダミーテキスト生成ツールの使い方</h2>
        <p>Webデザインやモックアップで使う仮テキスト（ダミーテキスト）を生成する無料ツールです。日本語のダミーテキスト（「吾輩は猫である」等）と英語のダミーテキスト（Lorem Ipsum）の両方に対応しています。</p>
        <h3>なぜダミーテキストが必要か</h3>
        <p>Webサイトやアプリのデザイン段階では、実際のコンテンツがまだ用意できていないことが多くあります。ダミーテキストを使うことで、レイアウトの確認、フォントサイズの調整、テキスト量による見た目の変化を事前に検証できます。</p>
        <h3>文字数指定・段落数指定</h3>
        <p>生成するテキストの文字数や段落数を指定できます。デザインの要件に合わせた長さのダミーテキストを即座に生成できます。</p>""",

    "tool-19-zenkaku-hankaku": """
        <h2>全角半角変換ツールの使い方</h2>
        <p>全角文字と半角文字を相互変換する無料ツールです。フォーム入力の正規化（全角数字を半角に統一）、データベースの文字列クレンジング、CSVファイルの整形などに活用できます。</p>
        <h3>変換対象のカスタマイズ</h3>
        <p>英字（Ａ→A）、数字（１→1）、カタカナ（ア→ｱ）、記号（！→!）のそれぞれについて、変換するかどうかを個別に指定できます。「数字だけ半角にしたい」「カタカナは全角のまま」といった細かい要件にも対応します。</p>
        <h3>日本のWebフォームでよくある問題</h3>
        <p>日本語入力では全角数字が入力されることが多く、電話番号や郵便番号のフィールドで問題になります。このツールでバッチ変換すれば、データの統一が簡単にできます。</p>""",

    "tool-20-favicon": """
        <h2>Favicon生成ツールの使い方</h2>
        <p>Webサイト用のFavicon（ブラウザタブに表示される小さなアイコン）を生成する無料ツールです。テキスト・絵文字からFaviconを作成、または画像をアップロードしてFavicon用にリサイズできます。</p>
        <h3>Faviconのサイズ</h3>
        <p>一般的なFaviconサイズは16×16px、32×32px、48×48pxですが、Apple Touch Iconには180×180px、Android Chromeには192×192pxが必要です。このツールでは複数サイズを一括生成できます。</p>
        <h3>ICO形式とPNG形式</h3>
        <p>従来のICO形式に加え、現在はPNG形式のFaviconも広くサポートされています。PNG形式の方がファイルサイズが小さく、透過にも対応しています。</p>""",

    "tool-22-withholding-tax": """
        <h2>源泉徴収税計算ツールの使い方</h2>
        <p>フリーランス・個人事業主が受け取る報酬にかかる源泉徴収税額を自動計算する無料ツールです。請求書の作成時に「源泉徴収後の振込額はいくらになるか」を即座に確認できます。</p>
        <h3>源泉徴収の計算方法</h3>
        <p>報酬額が100万円以下の場合は報酬額×10.21%、100万円を超える場合は超過分×20.42%＋102,100円が源泉徴収税額です。復興特別所得税（0.21%分）も含まれています。</p>
        <h3>フリーランスの請求書作成に</h3>
        <p>クライアントに請求書を送る際、源泉徴収ありの場合は「報酬額−源泉徴収税額＝振込額」を記載する必要があります。このツールで正確な金額を計算してから請求書を作成しましょう。消費税の扱い（税込み・税抜き）による源泉徴収額の違いも確認できます。</p>""",

    "tool-26-proofreader": """
        <h2>文章校正チェッカーの使い方</h2>
        <p>日本語テキストの誤字脱字、文法ミス、表記ゆれ、冗長表現を検出する無料ツールです。ブログ記事、ビジネスメール、プレゼン資料、レポートなどの文章品質を向上させます。</p>
        <h3>検出できる問題</h3>
        <p>ら抜き言葉（「食べれる」→「食べられる」）、い抜き言葉（「してる」→「している」）、二重否定、冗長表現（「〜することができる」→「〜できる」）、表記ゆれ（「サーバー」と「サーバ」の混在）、敬語の誤用などを検出します。</p>
        <h3>注意事項</h3>
        <p>このツールは一般的な日本語文法規則に基づくチェックです。文脈によっては意図的な表現もあるため、検出された問題はあくまで参考としてご利用ください。</p>""",

    "tool-27-loan-calc": """
        <h2>ローン返済シミュレーターの使い方</h2>
        <p>住宅ローン、自動車ローン、教育ローンなどの返済額を自動計算する無料ツールです。借入額・金利・返済期間を入力するだけで、毎月の返済額、総返済額、利息総額が即座にわかります。</p>
        <h3>元利均等返済と元金均等返済</h3>
        <p>元利均等返済は毎月の返済額が一定で計画を立てやすい反面、利息の総額は多くなります。元金均等返済は毎月の返済額が徐々に減少し、利息の総額は少なくなりますが、初期の返済額が大きくなります。このツールでは両方の返済方式をシミュレーションできます。</p>
        <h3>繰り上げ返済のシミュレーション</h3>
        <p>繰り上げ返済を行った場合の利息軽減効果も確認できます。返済開始後何年目に繰り上げ返済するかによって、節約できる利息額が変わります。</p>""",

    "tool-28-aspect-ratio": """
        <h2>アスペクト比計算ツールの使い方</h2>
        <p>画像や動画のアスペクト比（縦横比）を計算する無料ツールです。幅と高さを入力するとアスペクト比を算出し、指定したアスペクト比に合わせたサイズの計算もできます。</p>
        <h3>よく使われるアスペクト比</h3>
        <p>16:9（ワイドスクリーン、YouTube動画）、4:3（旧テレビ、iPadの画面）、1:1（Instagram正方形投稿）、9:16（スマートフォン縦画面、TikTok/リール）、21:9（ウルトラワイドモニター）が代表的です。</p>
        <h3>レスポンシブデザインでの活用</h3>
        <p>CSSのaspect-ratioプロパティやpadding-topハックでアスペクト比を維持したレスポンシブ画像を実装する際に、正確な比率を計算するのに役立ちます。</p>""",

    "tool-29-byte-converter": """
        <h2>バイト変換ツールの使い方</h2>
        <p>バイト数をKB・MB・GB・TBなどの単位に変換する無料ツールです。ファイルサイズの確認、ストレージ容量の計算、通信データ量の換算など、コンピュータの容量に関する計算に使います。</p>
        <h3>SI単位とバイナリ単位</h3>
        <p>1KB = 1,000バイト（SI単位、10進法）と 1KiB = 1,024バイト（バイナリ単位、2進法）の2つの表記があります。このツールでは両方の換算結果を表示します。ハードディスクメーカーはSI単位、OSはバイナリ単位を使うため、表示容量に差が出ることがあります。</p>
        <h3>よく使われる容量の目安</h3>
        <p>1MBは高画質写真1枚分、1GBは動画約1時間分（SD画質）、1TBは写真約25万枚分が目安です。</p>""",

    "tool-30-cron-generator": """
        <h2>Cron式ジェネレーターの使い方</h2>
        <p>LinuxのCronジョブで使うスケジュール式（Cron式）をGUIで簡単に生成する無料ツールです。バックアップの定期実行、レポートの自動送信、データベースのメンテナンスなど、定期タスクの設定に活用できます。</p>
        <h3>Cron式の構造</h3>
        <p>Cron式は「分 時 日 月 曜日」の5つのフィールドで構成されます。例えば「0 9 * * 1-5」は「平日の午前9時に実行」を意味します。このツールではフィールドごとにドロップダウンやチェックボックスで指定できるので、Cron式の文法を覚えていなくても正確なスケジュールを設定できます。</p>
        <h3>よく使われるCron式の例</h3>
        <p>「0 0 * * *」は毎日深夜0時、「0 */6 * * *」は6時間ごと、「0 9 * * 1」は毎週月曜9時です。生成されたCron式はクリップボードにコピーして、crontabにそのまま貼り付けられます。</p>""",

    "tool-31-ip-checker": """
        <h2>IPアドレス確認ツールの使い方</h2>
        <p>あなたの現在のグローバルIPアドレスを確認できる無料ツールです。リモートアクセスの設定、ファイアウォールのIP制限、VPN接続の確認などに使います。</p>
        <h3>グローバルIPとプライベートIP</h3>
        <p>グローバルIPアドレスはインターネット上であなたを識別するアドレスです。プライベートIPアドレス（192.168.x.x等）はローカルネットワーク内でのみ有効で、外部からはアクセスできません。このツールではグローバルIPアドレスを表示します。</p>
        <h3>IPアドレスが変わるケース</h3>
        <p>一般的な家庭用インターネット回線では、動的IPアドレスが割り当てられるため、ルーターの再起動などでIPアドレスが変わることがあります。固定IPが必要な場合はプロバイダーに確認してください。</p>""",

    "tool-32-unit-converter": """
        <h2>単位変換ツールの使い方</h2>
        <p>長さ・重さ・温度などの単位を相互変換する無料ツールです。cm⇔inch、kg⇔lb、摂氏⇔華氏など、日常生活やビジネスでよく使う単位の変換を瞬時に行えます。</p>
        <h3>対応するカテゴリ</h3>
        <p>長さ（mm/cm/m/km/inch/ft/yard/mile）、重さ（mg/g/kg/ton/oz/lb）、温度（摂氏/華氏/ケルビン）に対応しています。値を入力するとリアルタイムで変換結果が表示されます。</p>
        <h3>海外とのやり取りに</h3>
        <p>アメリカとの取引ではインチ・ポンド・華氏が使われるため、メートル法との変換が頻繁に必要になります。レシピの単位変換（カップ⇔ml等）にも便利です。</p>""",

    "tool-33-emoji-search": """
        <h2>絵文字検索ツールの使い方</h2>
        <p>キーワードで絵文字を検索し、ワンクリックでコピーできる無料ツールです。Slack、Discord、Twitter、LINE、メールなど、絵文字を使いたい場面で素早く目当ての絵文字を見つけられます。</p>
        <h3>日本語キーワード対応</h3>
        <p>「笑顔」「犬」「天気」「食べ物」など、日本語のキーワードで絵文字を検索できます。カテゴリ別（顔・動物・食べ物・旅行・物・記号等）のフィルタリングにも対応しています。</p>
        <h3>絵文字のバージョン</h3>
        <p>最新のUnicode絵文字に対応しています。ただし、表示される絵文字のデザインはOS・ブラウザによって異なります。絵文字をクリックするとクリップボードにコピーされるので、そのまま貼り付けて使えます。</p>""",

    "tool-36-uuid-gen": """
        <h2>UUID生成ツールの使い方</h2>
        <p>UUID（Universally Unique Identifier）v4を生成する無料ツールです。データベースの主キー、セッションID、一時ファイル名など、グローバルに一意な識別子が必要な場面で使います。</p>
        <h3>UUIDとは</h3>
        <p>UUIDは128ビットの識別子で、「550e8400-e29b-41d4-a716-446655440000」のような形式です。v4 UUIDは暗号学的に安全な乱数に基づいて生成されるため、重複する確率は天文学的に低く（2^122の組み合わせ）、事実上一意とみなせます。</p>
        <h3>一括生成対応</h3>
        <p>1個から100個まで一括生成に対応しています。生成されたUUIDはハイフンあり・なしの両形式でコピーできます。テストデータの作成や、マイグレーションスクリプトでの大量ID生成に便利です。</p>""",

    "tool-38-gradient-gen": """
        <h2>CSSグラデーション生成ツールの使い方</h2>
        <p>CSSのlinear-gradientやradial-gradientを視覚的に作成する無料ツールです。色の選択、角度の調整、カラーストップの追加をGUIで行い、完成したCSSコードをそのままコピーして使えます。</p>
        <h3>リニアグラデーション</h3>
        <p>2色以上の色を直線的に変化させるグラデーションです。角度を指定して斜めや水平方向のグラデーションを作成できます。ボタンの背景、ヘッダーのデザイン、テキストのグラデーションなどに使われます。</p>
        <h3>ラジアルグラデーション</h3>
        <p>中心から外側に向かって色が変化するグラデーションです。円形や楕円形のグラデーションを作成できます。背景デザインやアイコンの光沢表現に効果的です。</p>""",

    "tool-39-shadow-gen": """
        <h2>CSSボックスシャドウ生成ツールの使い方</h2>
        <p>CSSのbox-shadowプロパティを視覚的に調整して生成する無料ツールです。X/Y方向のオフセット、ぼかし、広がり、色をスライダーで直感的に操作し、リアルタイムでプレビューしながらCSSコードを生成できます。</p>
        <h3>シャドウの種類</h3>
        <p>外側シャドウ（ドロップシャドウ）と内側シャドウ（インセットシャドウ）の両方に対応しています。複数のシャドウを重ねることで、より立体的な表現が可能です。</p>
        <h3>デザイントレンド</h3>
        <p>フラットデザインでは影をほとんど使いませんが、ニューモーフィズム（Neumorphism）デザインでは内側と外側の影を組み合わせて柔らかな立体感を表現します。このツールで各種デザインスタイルの影を試すことができます。</p>""",

    "tool-40-placeholder-img": """
        <h2>プレースホルダー画像生成ツールの使い方</h2>
        <p>指定したサイズ・色・テキストのプレースホルダー画像を生成する無料ツールです。Webデザインのモックアップ、開発中のダミー画像、ワイヤーフレームの画像枠に使います。</p>
        <h3>カスタマイズ可能な項目</h3>
        <p>画像サイズ（幅×高さ）、背景色、テキスト色、表示するテキスト（デフォルトはサイズ表示）をカスタマイズできます。生成された画像はPNG形式でダウンロードできます。</p>
        <h3>開発での活用</h3>
        <p>フロントエンド開発中に、サーバーから配信される画像の代わりにプレースホルダー画像を使うことで、レイアウトの確認やレスポンシブデザインのテストができます。</p>""",

    "tool-44-tab-space": """
        <h2>タブ⇔スペース変換ツールの使い方</h2>
        <p>テキスト内のタブ文字とスペースを相互変換する無料ツールです。チームのコーディング規約に合わせてインデントを統一する場面で活躍します。</p>
        <h3>タブ vs スペース</h3>
        <p>インデントにタブを使うかスペースを使うかは、プログラミングの世界で長年議論されているテーマです。PythonはPEP8でスペース4つを推奨、GoはタブがデフォルトなどI言語によって慣習が異なります。このツールでは2スペース、4スペース、8スペースとタブの相互変換に対応しています。</p>
        <h3>一括変換</h3>
        <p>コード全体のインデントを一括で変換できるため、他の開発者から受け取ったコードのインデントを自分のエディタ設定に合わせる際に便利です。</p>""",

    "tool-46-color-palette": """
        <h2>カラーパレット生成ツールの使い方</h2>
        <p>メインカラーから調和の取れた配色パターンを自動生成する無料ツールです。Webサイト、アプリ、プレゼン資料のデザインで、色の組み合わせに迷ったときに最適な配色を提案します。</p>
        <h3>配色パターンの種類</h3>
        <p>補色（反対色）、類似色（隣接色）、トライアド（三角形）、テトラード（四角形）、スプリットコンプリメンタリーなどの配色理論に基づいたパレットを生成します。色彩理論を知らなくても、調和の取れた配色が得られます。</p>
        <h3>デザイナーの実務で</h3>
        <p>ブランドカラーからWebサイト全体の配色を決める、プレゼン資料のアクセントカラーを選ぶ、アプリのUIテーマを設計するなど、プロのデザイナーも日常的に使うカラーパレット生成機能です。</p>""",

    "tool-47-html-color-names": """
        <h2>HTMLカラーネーム一覧の使い方</h2>
        <p>HTML/CSSで使用できる140色以上の名前付きカラー（Named Colors）を一覧表示する無料ツールです。色名・HEXコード・RGB値をまとめて確認でき、クリックでカラーコードをコピーできます。</p>
        <h3>名前付きカラーとは</h3>
        <p>CSSでは「red」「blue」「skyblue」「coral」などの英語の色名でカラーを指定できます。HEXコードを覚えなくても直感的に色を指定できるため、プロトタイプの作成やデバッグ時に便利です。</p>
        <h3>検索・フィルター機能</h3>
        <p>色名やHEXコードで検索できるほか、赤系・青系・緑系などの色相でフィルタリングもできます。デザインの色選びの参考にも使えます。</p>""",

    "tool-49-sql-formatter": """
        <h2>SQLフォーマッターの使い方</h2>
        <p>SQL文を見やすくインデント整形する無料ツールです。SELECT・JOIN・WHERE・GROUP BY・ORDER BY等のキーワードを適切に改行・インデントし、複雑なクエリの可読性を大幅に向上させます。</p>
        <h3>なぜSQLの整形が必要か</h3>
        <p>複数テーブルのJOINやサブクエリを含むSQLは、1行で書くと構造を把握するのが困難です。このツールで整形することで、テーブル間の関係、フィルタ条件、集計方法が一目でわかるようになります。コードレビュー時のミス発見にも役立ちます。</p>
        <h3>対応するSQL方言</h3>
        <p>標準SQL（ANSI SQL）に対応しています。MySQL、PostgreSQL、SQLite、SQL Serverなど、主要なRDBMSのSQLを整形できます。</p>""",
}

seo_count = 0
for tool_dir in sorted(os.listdir(BASE)):
    if not tool_dir.startswith("tool-") or not os.path.isdir(os.path.join(BASE, tool_dir)):
        continue
    
    filepath = os.path.join(BASE, tool_dir, "index.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # SEOテキストの現在の長さをチェック
    seo_match = re.search(r'<div class="seo-content">(.*?)</div>\s*(?:<div class="ad-slot"|$)', content, re.DOTALL)
    if seo_match:
        current_text = re.sub(r'<[^>]+>', '', seo_match.group(1)).strip()
        if len(current_text) >= 300:
            continue  # 既に十分な長さ
    
    # 新しいSEOテキストがあれば置換
    if tool_dir in SEO_TEXTS:
        old_pattern = re.search(r'(<div class="seo-content">.*?</div>)', content, re.DOTALL)
        if old_pattern:
            new_seo = f'<div class="seo-content">{SEO_TEXTS[tool_dir]}\n        </div>'
            content = content.replace(old_pattern.group(1), new_seo)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            seo_count += 1

print(f"  ✅ {seo_count}ツールのSEOテキストを充実化しました")


# ============================================================
# 4. ブログ記事ページ2本を新規作成
# ============================================================
print("\n📋 4. ブログ記事ページを作成中...")

blog_dir = os.path.join(BASE, "blog")
os.makedirs(blog_dir, exist_ok=True)

# ブログインデックスページ
blog_index = """<!DOCTYPE html>
<html lang="ja">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-E27Q8YTG7L');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072" crossorigin="anonymous"></script>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ブログ | DevTools Japan</title>
<meta name="description" content="DevTools Japanの技術ブログ。Web開発、デザイン、フリーランスに役立つ情報を発信しています。">
<link rel="canonical" href="https://www.devtools-japan.com/blog/">
<meta property="og:title" content="ブログ | DevTools Japan">
<meta property="og:description" content="Web開発、デザイン、フリーランスに役立つ技術情報">
<meta property="og:url" content="https://www.devtools-japan.com/blog/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f7f8fb;--bg-card:#fff;--border:#e0e2ed;--text:#1e1e35;--text2:#5a5f78;--text3:#9498b0;--accent:#10b981;--radius:12px}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);line-height:2}
.container{max-width:800px;margin:0 auto;padding:40px 20px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
h1{font-size:1.6rem;font-weight:700;color:var(--accent);margin-bottom:8px}
.sub{color:var(--text3);font-size:0.85rem;margin-bottom:32px}
.back{display:inline-flex;align-items:center;gap:6px;margin-bottom:24px;font-size:0.8rem;color:var(--text3);text-decoration:none}
.post-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-bottom:16px;transition:border-color 0.2s}
.post-card:hover{border-color:var(--accent)}
.post-card h2{font-size:1.1rem;margin-bottom:4px}.post-card h2 a{color:var(--text)}
.post-meta{font-size:0.75rem;color:var(--text3);margin-bottom:8px}
.post-excerpt{font-size:0.85rem;color:var(--text2)}
footer{text-align:center;margin-top:60px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}
</style>
</head>
<body>
<div class="container">
<a href="/" class="back"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8h5z"/></svg> DevTools Japan トップへ</a>
<h1>ブログ</h1>
<p class="sub">Web開発・デザイン・フリーランスに役立つ情報</p>

<div class="post-card">
<h2><a href="/blog/freelance-tax-guide/">フリーランスエンジニアが知っておくべき確定申告の基礎知識【2026年版】</a></h2>
<div class="post-meta">2026年4月9日</div>
<p class="post-excerpt">フリーランスになったら避けて通れない確定申告。青色申告と白色申告の違い、経費にできるもの、節税のコツを初心者向けに解説します。</p>
</div>

<div class="post-card">
<h2><a href="/blog/sns-image-size-guide/">【2026年最新】SNS画像サイズ完全ガイド — X(Twitter)・Instagram・YouTube・LINE</a></h2>
<div class="post-meta">2026年4月9日</div>
<p class="post-excerpt">各SNSの推奨画像サイズは頻繁に変更されます。2026年最新の推奨サイズ、アスペクト比、作成のコツをまとめました。</p>
</div>

<footer>
<p style="margin-bottom:8px">&copy; 2026 DevTools Japan</p>
<p style="font-size:0.65rem"><a href="/" style="color:inherit">トップ</a> | <a href="/about/" style="color:inherit">サイトについて</a> | <a href="/privacy/" style="color:inherit">プライバシーポリシー</a> | <a href="/contact/" style="color:inherit">お問い合わせ</a></p>
</footer>
</div>
</body>
</html>"""

with open(os.path.join(blog_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(blog_index)

# ブログ記事1: フリーランスの確定申告ガイド
article1_dir = os.path.join(blog_dir, "freelance-tax-guide")
os.makedirs(article1_dir, exist_ok=True)

article1 = """<!DOCTYPE html>
<html lang="ja">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-E27Q8YTG7L');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072" crossorigin="anonymous"></script>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>フリーランスエンジニアが知っておくべき確定申告の基礎知識【2026年版】 | DevTools Japan</title>
<meta name="description" content="フリーランスエンジニア・副業プログラマー向けの確定申告ガイド。青色申告と白色申告の違い、経費にできるもの、節税のコツを初心者にもわかりやすく解説。">
<link rel="canonical" href="https://www.devtools-japan.com/blog/freelance-tax-guide/">
<meta property="og:title" content="フリーランスエンジニアの確定申告ガイド【2026年版】">
<meta property="og:description" content="青色申告と白色申告の違い、経費にできるもの、節税のコツを初心者向けに解説">
<meta property="og:url" content="https://www.devtools-japan.com/blog/freelance-tax-guide/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Article","headline":"フリーランスエンジニアが知っておくべき確定申告の基礎知識","datePublished":"2026-04-09","author":{"@type":"Organization","name":"DevTools Japan"},"publisher":{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f7f8fb;--bg-card:#fff;--border:#e0e2ed;--text:#1e1e35;--text2:#5a5f78;--text3:#9498b0;--accent:#10b981;--radius:12px}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);line-height:2}
.container{max-width:800px;margin:0 auto;padding:40px 20px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
h1{font-size:1.5rem;font-weight:700;color:var(--text);margin-bottom:8px;line-height:1.5}
h2{font-size:1.2rem;font-weight:600;margin-top:36px;margin-bottom:12px;color:var(--text);border-left:4px solid var(--accent);padding-left:12px}
h3{font-size:1rem;font-weight:600;margin-top:24px;margin-bottom:8px;color:var(--text)}
p{margin-bottom:16px;color:var(--text2);font-size:0.9rem}
.meta{font-size:0.75rem;color:var(--text3);margin-bottom:32px}
.back{display:inline-flex;align-items:center;gap:6px;margin-bottom:24px;font-size:0.8rem;color:var(--text3);text-decoration:none}
.card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin:20px 0}
.ad-slot{display:none}
ul{margin:0 0 16px 20px;color:var(--text2);font-size:0.9rem}li{margin-bottom:6px}
.cta{background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);border-radius:var(--radius);padding:20px;margin:24px 0;text-align:center}
.cta p{color:var(--text);margin-bottom:8px}
footer{text-align:center;margin-top:60px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}
</style>
</head>
<body>
<div class="container">
<a href="/blog/" class="back"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg> ブログ一覧に戻る</a>
<h1>フリーランスエンジニアが知っておくべき確定申告の基礎知識【2026年版】</h1>
<div class="meta">2026年4月9日 公開 | DevTools Japan</div>

<div class="ad-slot"></div>

<p>フリーランスエンジニアや副業でプログラミングをしている方にとって、確定申告は避けて通れないイベントです。「何から始めればいいかわからない」「経費って何が認められるの？」という疑問を持つ方のために、基礎知識をまとめました。</p>

<h2>確定申告が必要な人</h2>
<p>以下のいずれかに該当する場合、確定申告が必要です。</p>
<ul>
<li>フリーランス・個人事業主として事業収入がある方</li>
<li>会社員で副業の所得が年間20万円を超える方</li>
<li>2か所以上から給与を受けている方</li>
<li>年間の給与収入が2,000万円を超える方</li>
</ul>
<p>会社員の副業の場合、「所得」は「売上−経費」で計算します。売上が30万円でも経費が15万円あれば所得は15万円となり、20万円以下なので確定申告は不要です（ただし住民税の申告は必要）。</p>

<h2>青色申告と白色申告の違い</h2>
<p>確定申告には「青色申告」と「白色申告」の2種類があります。</p>

<div class="card">
<h3>青色申告のメリット</h3>
<ul>
<li>最大65万円の特別控除（e-Tax + 複式簿記の場合）</li>
<li>赤字を3年間繰り越せる</li>
<li>家族への給与を経費にできる（青色事業専従者給与）</li>
<li>30万円未満の資産を一括で経費にできる（少額減価償却資産の特例）</li>
</ul>
<p>デメリットは複式簿記での記帳が必要なこと。ただし、freeeやマネーフォワードなどの会計ソフトを使えば、簿記の知識がなくても対応できます。</p>
</div>

<div class="card">
<h3>白色申告</h3>
<p>記帳が簡単（単式簿記）ですが、特別控除がありません。収入が少ない場合や、初めて確定申告する場合に選ばれることがありますが、65万円控除のメリットを考えると、最初から青色申告を選ぶことをおすすめします。</p>
</div>

<h2>エンジニアが経費にできるもの</h2>
<p>フリーランスエンジニアが経費にできる主な項目は以下の通りです。</p>
<ul>
<li><strong>通信費</strong>: インターネット回線料金、スマートフォン通信料（事業使用分）</li>
<li><strong>家賃（按分）</strong>: 自宅で作業する場合、作業スペースの面積比で按分</li>
<li><strong>消耗品費</strong>: パソコン（10万円未満）、モニター、キーボード、マウス、書籍</li>
<li><strong>減価償却費</strong>: パソコン（10万円以上）は3〜4年で減価償却</li>
<li><strong>外注費</strong>: 他のフリーランスへの外注、デザイン発注</li>
<li><strong>旅費交通費</strong>: 客先訪問の電車代、打ち合わせのタクシー代</li>
<li><strong>会議費</strong>: 打ち合わせのカフェ代、ランチミーティング</li>
<li><strong>ソフトウェア費</strong>: Adobe CC、AWS、GitHub、ドメイン料、サーバー費用</li>
<li><strong>研修費</strong>: 技術書籍、オンライン講座（Udemy等）、勉強会参加費</li>
</ul>
<p>ポイントは「事業に関連する支出であること」と「領収書・レシートを保管すること」です。プライベートと兼用のものは、事業使用割合で按分します。</p>

<h2>節税のコツ</h2>

<h3>1. 青色申告65万円控除を使う</h3>
<p>e-Taxで電子申告し、複式簿記で記帳すれば65万円の特別控除を受けられます。これだけで所得税と住民税を合わせて約10万円以上の節税になります。</p>

<h3>2. 小規模企業共済に加入する</h3>
<p>フリーランスの退職金制度で、掛金が全額所得控除になります。月額1,000円〜70,000円で、年間最大84万円の控除が可能です。</p>

<h3>3. ふるさと納税を活用する</h3>
<p>実質2,000円の負担で返礼品を受け取れるふるさと納税は、フリーランスでも利用できます。確定申告で寄附金控除を申請します。</p>

<h3>4. 経費を漏れなく計上する</h3>
<p>上述のように、エンジニアは多くの支出を経費にできます。「これは経費になるかな？」と迷ったものは、税理士に相談するか、会計ソフトの判定機能を活用しましょう。</p>

<div class="cta">
<p><strong>税金の概算を計算してみましょう</strong></p>
<p><a href="/tool-21-tax-simulator/">確定申告シミュレーター</a>で売上・経費・控除を入力すると、所得税・住民税・手取り額がすぐにわかります。</p>
<p><a href="/tool-22-withholding-tax/">源泉徴収税計算ツール</a>もあわせてご利用ください。</p>
</div>

<h2>確定申告の期限</h2>
<p>所得税の確定申告期限は毎年3月15日（土日の場合は翌営業日）です。期限を過ぎると延滞税や加算税がかかる場合があります。早めの準備を心がけましょう。</p>

<h2>まとめ</h2>
<ul>
<li>フリーランス・副業所得20万円超は確定申告が必要</li>
<li>青色申告を選んで65万円控除を活用</li>
<li>通信費・家賃按分・書籍・ソフトウェアは経費にできる</li>
<li>小規模企業共済とふるさと納税も活用</li>
<li>会計ソフトを使えば簿記の知識がなくても対応可能</li>
</ul>
<p>※この記事は一般的な情報提供を目的としています。個別の税務相談については税理士にご確認ください。</p>

<div class="ad-slot"></div>

<footer>
<p style="margin-bottom:8px">&copy; 2026 DevTools Japan</p>
<p style="font-size:0.65rem"><a href="/" style="color:inherit">トップ</a> | <a href="/blog/" style="color:inherit">ブログ</a> | <a href="/about/" style="color:inherit">サイトについて</a> | <a href="/privacy/" style="color:inherit">プライバシーポリシー</a></p>
</footer>
</div>
</body>
</html>"""

with open(os.path.join(article1_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(article1)

# ブログ記事2: SNS画像サイズガイド
article2_dir = os.path.join(blog_dir, "sns-image-size-guide")
os.makedirs(article2_dir, exist_ok=True)

article2 = """<!DOCTYPE html>
<html lang="ja">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-E27Q8YTG7L');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072" crossorigin="anonymous"></script>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>【2026年最新】SNS画像サイズ完全ガイド — X(Twitter)・Instagram・YouTube・LINE | DevTools Japan</title>
<meta name="description" content="2026年最新のSNS推奨画像サイズを完全網羅。X(Twitter)投稿画像、Instagramフィード、YouTubeサムネイル、LINEリッチメニューの最適サイズとアスペクト比を詳しく解説。">
<link rel="canonical" href="https://www.devtools-japan.com/blog/sns-image-size-guide/">
<meta property="og:title" content="【2026年最新】SNS画像サイズ完全ガイド">
<meta property="og:description" content="X(Twitter)・Instagram・YouTube・LINEの推奨画像サイズを完全網羅">
<meta property="og:url" content="https://www.devtools-japan.com/blog/sns-image-size-guide/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Article","headline":"【2026年最新】SNS画像サイズ完全ガイド","datePublished":"2026-04-09","author":{"@type":"Organization","name":"DevTools Japan"},"publisher":{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f7f8fb;--bg-card:#fff;--border:#e0e2ed;--text:#1e1e35;--text2:#5a5f78;--text3:#9498b0;--accent:#3b82f6;--radius:12px}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);line-height:2}
.container{max-width:800px;margin:0 auto;padding:40px 20px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
h1{font-size:1.4rem;font-weight:700;color:var(--text);margin-bottom:8px;line-height:1.5}
h2{font-size:1.2rem;font-weight:600;margin-top:36px;margin-bottom:12px;color:var(--text);border-left:4px solid var(--accent);padding-left:12px}
h3{font-size:1rem;font-weight:600;margin-top:20px;margin-bottom:8px;color:var(--text)}
p{margin-bottom:16px;color:var(--text2);font-size:0.9rem}
.meta{font-size:0.75rem;color:var(--text3);margin-bottom:32px}
.back{display:inline-flex;align-items:center;gap:6px;margin-bottom:24px;font-size:0.8rem;color:var(--text3);text-decoration:none}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:0.85rem}
th{background:var(--bg-card);border:1px solid var(--border);padding:10px 12px;text-align:left;color:var(--text);font-weight:600}
td{border:1px solid var(--border);padding:10px 12px;color:var(--text2)}
.ad-slot{display:none}
.cta{background:rgba(59,130,246,0.08);border:1px solid rgba(59,130,246,0.2);border-radius:var(--radius);padding:20px;margin:24px 0;text-align:center}
.cta p{color:var(--text);margin-bottom:8px}
footer{text-align:center;margin-top:60px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}
</style>
</head>
<body>
<div class="container">
<a href="/blog/" class="back"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg> ブログ一覧に戻る</a>
<h1>【2026年最新】SNS画像サイズ完全ガイド — X(Twitter)・Instagram・YouTube・LINE</h1>
<div class="meta">2026年4月9日 公開 | DevTools Japan</div>

<div class="ad-slot"></div>

<p>SNSに画像を投稿する際、プラットフォームごとに推奨される画像サイズが異なります。サイズが合っていないと画像が自動トリミングされたり、画質が劣化したりすることがあります。この記事では、2026年現在の各SNSの推奨画像サイズをまとめました。</p>

<h2>X（旧Twitter）の画像サイズ</h2>
<table>
<tr><th>用途</th><th>推奨サイズ</th><th>アスペクト比</th></tr>
<tr><td>投稿画像（1枚）</td><td>1200 x 675 px</td><td>16:9</td></tr>
<tr><td>投稿画像（2枚）</td><td>700 x 800 px</td><td>7:8</td></tr>
<tr><td>ヘッダー画像</td><td>1500 x 500 px</td><td>3:1</td></tr>
<tr><td>プロフィール画像</td><td>400 x 400 px</td><td>1:1</td></tr>
</table>
<p>Xの投稿画像は16:9が基本です。1枚投稿の場合は横長で表示されますが、2枚投稿になると表示比率が変わるため注意が必要です。ヘッダー画像はデバイスによって表示範囲が変わるため、重要な情報は中央に配置しましょう。</p>
<p>画像の最大ファイルサイズは5MBまで。JPEG、PNG、GIF、WebPに対応しています。</p>

<h2>Instagramの画像サイズ</h2>
<table>
<tr><th>用途</th><th>推奨サイズ</th><th>アスペクト比</th></tr>
<tr><td>フィード投稿（正方形）</td><td>1080 x 1080 px</td><td>1:1</td></tr>
<tr><td>フィード投稿（縦長）</td><td>1080 x 1350 px</td><td>4:5</td></tr>
<tr><td>ストーリーズ / リール</td><td>1080 x 1920 px</td><td>9:16</td></tr>
<tr><td>プロフィール画像</td><td>320 x 320 px</td><td>1:1</td></tr>
</table>
<p>Instagramのフィードでは縦長画像（4:5）の方が正方形（1:1）よりも画面に大きく表示されるため、エンゲージメント率が高くなる傾向があります。ストーリーズとリールは9:16の縦型フルスクリーンが基本です。</p>

<h2>YouTubeの画像サイズ</h2>
<table>
<tr><th>用途</th><th>推奨サイズ</th><th>アスペクト比</th></tr>
<tr><td>サムネイル</td><td>1280 x 720 px</td><td>16:9</td></tr>
<tr><td>チャンネルアート</td><td>2560 x 1440 px</td><td>16:9</td></tr>
<tr><td>プロフィール画像</td><td>800 x 800 px</td><td>1:1</td></tr>
</table>
<p>YouTubeのサムネイルは動画のクリック率に最も大きく影響する要素です。1280x720px以上で、ファイルサイズ2MB以下、JPEG/PNG/GIF/BMPに対応しています。文字は大きく、コントラストを高くすることで、スマートフォンの小さな画面でも視認性が上がります。</p>
<p>チャンネルアートは2560x1440pxが推奨ですが、デバイスによって表示される範囲が異なります。TVでは全体が表示されますが、スマートフォンでは中央の1546x423pxしか表示されません。</p>

<h2>LINEの画像サイズ</h2>
<table>
<tr><th>用途</th><th>推奨サイズ</th><th>アスペクト比</th></tr>
<tr><td>リッチメッセージ</td><td>1040 x 1040 px</td><td>1:1</td></tr>
<tr><td>リッチメニュー（大）</td><td>2500 x 1686 px</td><td>約3:2</td></tr>
<tr><td>プロフィール画像</td><td>480 x 480 px</td><td>1:1</td></tr>
</table>
<p>LINE公式アカウントのリッチメニューは、ユーザーのトーク画面下部に常時表示されるため、ビジネス利用では特に重要です。タップ領域を分割して複数のリンクを設定できます。</p>

<h2>Facebookの画像サイズ</h2>
<table>
<tr><th>用途</th><th>推奨サイズ</th><th>アスペクト比</th></tr>
<tr><td>投稿画像</td><td>1200 x 630 px</td><td>約1.9:1</td></tr>
<tr><td>カバー画像</td><td>851 x 315 px</td><td>約2.7:1</td></tr>
<tr><td>プロフィール画像</td><td>170 x 170 px</td><td>1:1</td></tr>
</table>

<h2>OGP画像のサイズ</h2>
<table>
<tr><th>用途</th><th>推奨サイズ</th><th>アスペクト比</th></tr>
<tr><td>OGP画像（共通）</td><td>1200 x 630 px</td><td>約1.9:1</td></tr>
<tr><td>Twitterカード</td><td>1200 x 628 px</td><td>約1.9:1</td></tr>
</table>
<p>OGP（Open Graph Protocol）画像は、WebページがSNSでシェアされた時に表示されるプレビュー画像です。1200x630pxで作成すれば、Facebook・Twitter・LINEのいずれにも対応できます。</p>

<div class="cta">
<p><strong>各SNSの推奨サイズを一覧で確認</strong></p>
<p><a href="/tool-23-sns-image-sizes/">SNS画像サイズ一覧ツール</a>で、すべてのSNSのサイズをビジュアルプレビュー付きで確認できます。</p>
<p><a href="/tool-24-ogp-preview/">OGPプレビューチェッカー</a>でSNSシェア時の表示も確認しましょう。</p>
</div>

<h2>画像作成のコツ</h2>
<h3>ファイルサイズを最適化する</h3>
<p>推奨サイズの画像はファイルサイズが大きくなりがちです。<a href="/tool-10-image-compress/">画像圧縮ツール</a>で品質を維持しながらファイルサイズを削減しましょう。</p>

<h3>セーフエリアを意識する</h3>
<p>チャンネルアートやヘッダー画像はデバイスによって表示範囲が変わります。重要なテキストやロゴは中央のセーフエリア内に配置しましょう。</p>

<h3>テンプレートを活用する</h3>
<p>CanvaやFigmaなどのデザインツールには、各SNSのサイズに合わせたテンプレートが用意されています。ゼロから作るよりも効率的です。</p>

<h2>まとめ</h2>
<p>SNSの推奨画像サイズは頻繁に変更されることがあります。最新の情報は各プラットフォームの公式ヘルプページで確認してください。DevTools Japanの<a href="/tool-23-sns-image-sizes/">SNS画像サイズ一覧</a>ツールも随時更新しています。</p>

<div class="ad-slot"></div>

<footer>
<p style="margin-bottom:8px">&copy; 2026 DevTools Japan</p>
<p style="font-size:0.65rem"><a href="/" style="color:inherit">トップ</a> | <a href="/blog/" style="color:inherit">ブログ</a> | <a href="/about/" style="color:inherit">サイトについて</a> | <a href="/privacy/" style="color:inherit">プライバシーポリシー</a></p>
</footer>
</div>
</body>
</html>"""

with open(os.path.join(article2_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(article2)

print("  ✅ blog/index.html（ブログトップ）を作成")
print("  ✅ blog/freelance-tax-guide/index.html（確定申告ガイド）を作成")
print("  ✅ blog/sns-image-size-guide/index.html（SNS画像サイズガイド）を作成")


# ============================================================
# 5. sitemap.xmlにブログページを追加
# ============================================================
print("\n📋 5. sitemap.xml を更新中...")

sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_urls = """  <url>
    <loc>https://www.devtools-japan.com/blog/</loc>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.devtools-japan.com/blog/freelance-tax-guide/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.devtools-japan.com/blog/sns-image-size-guide/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""

if "blog/freelance-tax-guide" not in sitemap:
    sitemap = sitemap.replace("</urlset>", new_urls + "\n</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("  ✅ sitemap.xml にブログ3ページを追加")
else:
    print("  ⏭️  既にブログページは登録済み")


# ============================================================
# 完了
# ============================================================
print("\n" + "=" * 60)
print("  全ての修正が完了しました！")
print("=" * 60)
print()
print("次のステップ:")
print("  1. デプロイ:")
print("     git add .")
print('     git commit -m "AdSense resubmit: ads.txt, about page, SEO text enrichment, blog articles"')
print("     git push")
print()
print("  2. Search Console でsitemap.xmlを再送信:")
print("     https://search.google.com/search-console")
print("     → サイトマップ → sitemap.xml を再送信")
print()
print("  3. AdSense で再審査リクエスト:")
print("     https://www.google.com/adsense → サイト → devtools-japan.com → 再審査")
