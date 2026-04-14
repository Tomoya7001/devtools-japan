#!/usr/bin/env python3
"""
DevTools Japan — 全ツールSEO強化スクリプト（第2弾）
Search Consoleデータに基づき、表示回数が多い16ページのtitle/descriptionを最適化
"""
import os, re

BASE = os.getcwd()

if not os.path.exists(os.path.join(BASE, "index.html")):
    print("エラー: ~/Desktop/devtools-japan-complete で実行してください")
    exit(1)

FIXES = {
    "tool-22-withholding-tax": {
        "title": (
            "<title>源泉徴収税計算ツール | DevTools Japan</title>",
            "<title>源泉徴収税計算ツール | フリーランス・副業の報酬から引かれる税額を自動計算【無料】</title>"
        ),
        "desc": (
            'content="フリーランス・個人事業主向け源泉徴収税額の自動計算ツール"',
            'content="フリーランス・副業の報酬にかかる源泉徴収税額を自動計算。報酬額を入力するだけで10.21%の税額・手取り額がわかる無料ツール。100万円超の20.42%計算にも対応。請求書作成の必須ツール。"'
        ),
    },
    "tool-29-byte-converter": {
        "title": (
            "<title>バイト変換ツール | DevTools Japan</title>",
            "<title>バイト変換・換算ツール | KB・MB・GB・TBの単位変換を一瞬で計算【無料】</title>"
        ),
        "desc": (
            'content="バイト数の単位変換ツール。B/KB/MB/GB/TBを相互変換"',
            'content="バイト数をKB・MB・GB・TBに一瞬で変換する無料ツール。ファイルサイズの確認、ストレージ容量の計算、通信データ量の換算に。SI単位（1000）とバイナリ単位（1024）の両方に対応。"'
        ),
    },
    "tool-28-aspect-ratio": {
        "title": (
            "<title>アスペクト比計算ツール | DevTools Japan</title>",
            "<title>アスペクト比計算ツール | 画像・動画の縦横比を自動計算【16:9・4:3・1:1対応】</title>"
        ),
        "desc": (
            'content="画像・動画のアスペクト比を自動計算。リサイズ時の縦横比維持に"',
            'content="画像・動画のアスペクト比（縦横比）を自動計算する無料ツール。幅と高さからアスペクト比を算出、指定比率でのリサイズ計算にも対応。YouTube(16:9)・Instagram(1:1, 4:5)・TikTok(9:16)の推奨サイズ確認に。"'
        ),
    },
    "tool-09-diff": {
        "title": (
            "<title>テキスト比較（Diff）ツール | DevTools Japan</title>",
            "<title>テキスト比較（Diff）ツール | 2つの文章の違い・差分を一瞬で検出【無料】</title>"
        ),
        "desc": (
            'content="2つのテキストの違いをハイライト表示するDiffツール。コード比較・文章校正に"',
            'content="2つのテキストを比較して違い（差分）をハイライト表示する無料Diffツール。追加・削除・変更箇所を色分け表示。コードレビュー、文章の変更確認、設定ファイルの差分チェックに。行番号付きの見やすい対比表示。"'
        ),
    },
    "tool-31-ip-checker": {
        "title": (
            "<title>IPアドレス確認ツール | DevTools Japan</title>",
            "<title>IPアドレス確認ツール | 自分のグローバルIPを即表示【無料・登録不要】</title>"
        ),
        "desc": (
            'content="現在のグローバルIPアドレスを即座に確認"',
            'content="自分のグローバルIPアドレスを即座に確認できる無料ツール。リモートアクセス設定、ファイアウォールのIP許可、VPN接続確認に。登録不要でアクセスするだけですぐ表示。"'
        ),
    },
    "tool-02-password-gen": {
        "title": (
            "<title>パスワード生成ツール | 安全なランダムパスワードを自動作成</title>",
            "<title>パスワード生成ツール | 安全なランダムパスワードを自動作成【無料・登録不要】</title>"
        ),
        "desc": (
            'content="セキュアなランダムパスワードを瞬時に生成。長さ・文字種を指定可能。パスワード管理の必須ツール。"',
            'content="安全なランダムパスワードを瞬時に生成する無料ツール。長さ（8〜128文字）、大文字・小文字・数字・記号の組み合わせを指定可能。複数個の一括生成にも対応。登録不要でブラウザだけで使えます。"'
        ),
    },
    "tool-41-text-reverse": {
        "title": (
            "<title>テキスト反転ツール | DevTools Japan</title>",
            "<title>テキスト反転ツール | 文字列を逆順に変換・回文チェック【無料】</title>"
        ),
        "desc": (
            'content="テキストを逆順に変換。文字列の反転、回文チェック、プログラミングのデバッグに使える無料オンラインツール。"',
            'content="テキストを逆順に変換する無料ツール。文字列の反転、回文チェック、プログラミングのアルゴリズムテスト、暗号・パズルに。行単位の反転にも対応。ブラウザだけで即使える。"'
        ),
    },
    "tool-03-json-formatter": {
        "title": (
            "<title>JSON整形ツール | フォーマッター＆バリデーター</title>",
            "<title>JSON整形・フォーマッターツール | JSONを見やすく整形・構文チェック【無料】</title>"
        ),
        "desc": (
            'content="JSONを見やすくインデント整形。構文エラーの検出も。APIレスポンスの確認、設定ファイルの編集に。"',
            'content="JSONを見やすくインデント整形する無料ツール。構文エラーの検出・バリデーション付き。APIレスポンスの確認、設定ファイルの編集、デバッグに。2スペース/4スペース/タブのインデント指定、圧縮（ミニファイ）にも対応。"'
        ),
    },
    "tool-08-regex-tester": {
        "title": (
            "<title>正規表現テスター | リアルタイムでマッチ確認</title>",
            "<title>正規表現テスター | 正規表現をリアルタイムでテスト・マッチ確認【無料】</title>"
        ),
        "desc": (
            'content="正規表現パターンをリアルタイムでテスト。マッチ結果のハイライト、グループキャプチャの確認に。"',
            'content="正規表現（regex）をリアルタイムでテストする無料ツール。マッチ結果のハイライト表示、キャプチャグループの確認、フラグ（g/i/m）対応。メールアドレスや電話番号のバリデーション、ログ解析のパターン作成に。"'
        ),
    },
    "tool-45-chmod-calc": {
        "title": (
            "<title>chmod計算ツール | DevTools Japan</title>",
            "<title>chmod計算ツール | Linuxファイル権限（パーミッション）を数値⇔記号で変換【無料】</title>"
        ),
        "desc": (
            'content="Linuxのファイル権限（パーミッション）を数値⇔記号で変換。chmod 755やrwxr-xr-xの意味を視覚的に確認できる無料ツール。"',
            'content="Linuxのchmod（ファイルパーミッション）を数値⇔記号で変換する無料ツール。755→rwxr-xr-x、644→rw-r--r--をワンクリックで確認。チェックボックスで権限を視覚的に設定。サーバー管理・Web開発の必須ツール。"'
        ),
    },
    "tool-10-image-compress": {
        "title": (
            "<title>画像圧縮ツール | DevTools Japan</title>",
            "<title>画像圧縮ツール | JPEG・PNG・WebPを品質を保ったまま軽量化【無料・アップロード不要】</title>"
        ),
        "desc": (
            'content="JPEG、PNG、WebP画像のファイルサイズを圧縮。画質を維持しながら容量削減"',
            'content="JPEG・PNG・WebP画像をブラウザだけで圧縮する無料ツール。品質を保ったまま50〜80%サイズ削減。サーバーへのアップロード不要でプライバシー安全。Webサイトの表示速度改善、メール添付のサイズ削減に。"'
        ),
    },
    "tool-12-wareki": {
        "title": (
            "<title>和暦西暦変換ツール | 令和・平成・昭和を自動変換</title>",
            "<title>和暦西暦変換ツール | 令和・平成・昭和・大正・明治を自動変換【無料】</title>"
        ),
        "desc": (
            'content="和暦（令和・平成・昭和・大正・明治）と西暦を相互変換。年齢計算、業務書類の日付変換に。"',
            'content="和暦（令和・平成・昭和・大正・明治）と西暦を相互変換する無料ツール。2026年→令和8年、平成10年→1998年を一瞬で変換。履歴書の年号確認、業務書類の日付変換、年齢計算に。元号の境界日も正確に対応。"'
        ),
    },
    "tool-17-hash": {
        "title": (
            "<title>ハッシュ生成ツール | MD5・SHA256を瞬時に計算</title>",
            "<title>ハッシュ生成ツール | MD5・SHA-1・SHA-256・SHA-512を一括計算【無料】</title>"
        ),
        "desc": (
            'content="テキストのハッシュ値（MD5・SHA-1・SHA-256・SHA-512）を瞬時に生成。ファイル検証、パスワードハッシュの確認に。"',
            'content="テキストのハッシュ値を一括生成する無料ツール。MD5・SHA-1・SHA-256・SHA-512の4種類を同時計算。ファイルの整合性チェック、パスワードハッシュ確認、データ署名の検証に。ブラウザ内で即計算。"'
        ),
    },
    "tool-04-qr-generator": {
        "title": (
            "<title>QRコード生成ツール | URLやテキストから無料で作成</title>",
            "<title>QRコード生成ツール | URL・テキスト・Wi-FiからQRコードを即作成【無料】</title>"
        ),
        "desc": (
            'content="URLやテキストからQRコードを瞬時に生成。サイズ・色のカスタマイズ可能。名刺、ポスター、Webサイトに。"',
            'content="URLやテキストからQRコードを瞬時に生成する無料ツール。サイズ・色・エラー訂正レベルをカスタマイズ可能。PNG画像でダウンロード。名刺、ポスター、チラシ、Wi-Fi接続情報の共有に。"'
        ),
    },
    "tool-06-base64": {
        "title": (
            "<title>Base64エンコード・デコード | DevTools Japan</title>",
            "<title>Base64エンコード・デコードツール | テキスト・画像をBase64に変換【無料】</title>"
        ),
        "desc": (
            'content="テキストや画像をBase64に変換。デコードにも対応。データURI生成やAPIデバッグに。"',
            'content="テキストや画像をBase64にエンコード・デコードする無料ツール。データURIスキームでの画像埋め込み、メール添付のMIMEエンコード、JWTトークンのデバッグに。ブラウザ内で処理、サーバー送信なし。"'
        ),
    },
    "tool-16-timestamp": {
        "title": (
            "<title>Unixタイムスタンプ変換ツール | DevTools Japan</title>",
            "<title>Unixタイムスタンプ変換ツール | 日時⇔タイムスタンプを即変換【JST対応・無料】</title>"
        ),
        "desc": (
            'content="Unixタイムスタンプと日時を相互変換。現在時刻の取得も。"',
            'content="Unixタイムスタンプと日時を相互変換する無料ツール。10桁（秒）と13桁（ミリ秒）の両方に対応。UTC/JST（日本標準時）表示。サーバーログの解析、APIレスポンスの日時確認、データベースのデバッグに。"'
        ),
    },
}

print("=" * 60)
print("  DevTools Japan — 全ツールSEO強化（第2弾）")
print("=" * 60)

total = 0
for tool_dir, fixes in FIXES.items():
    filepath = os.path.join(BASE, tool_dir, "index.html")
    if not os.path.exists(filepath):
        print(f"  ❌ {tool_dir} が見つかりません")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    replaced = 0
    
    if "title" in fixes:
        old, new = fixes["title"]
        if old in content:
            content = content.replace(old, new)
            replaced += 1
    
    if "desc" in fixes:
        old, new = fixes["desc"]
        if old in content:
            content = content.replace(old, new)
            replaced += 1
    
    if replaced > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        total += 1
        print(f"  ✅ {tool_dir}: {replaced}箇所を最適化")
    else:
        print(f"  ⏭️  {tool_dir}: 置換対象なし（既に最適化済みか構造が異なる）")

print(f"\n  合計: {total}ツールを最適化")
print()
print("デプロイ:")
print("  git add .")
print('  git commit -m "SEO boost round 2: optimize title/desc for 16 tool pages"')
print("  git push")
print()
print("デプロイ後、AdSenseの再審査もリクエスト:")
print("  AdSense → サイト → devtools-japan.com → 再審査をリクエスト")
