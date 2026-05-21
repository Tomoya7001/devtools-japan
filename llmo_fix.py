#!/usr/bin/env python3
"""
DevTools Japan — AdSense再審査 + LLMO対策スクリプト
1. robots.txt 修正（www統一 + AI クローラー許可）
2. llms.txt 作成（LLMO対策）
3. sitemap.xml の lastmod を更新
4. 新ツール11本にFAQスキーマを追加
"""
import os, re
from datetime import date

BASE = "/Users/tom/Desktop/devtools-japan-complete"
TODAY = date.today().isoformat()

print("=" * 60)
print("  DevTools Japan — AdSense再審査 + LLMO対策")
print("=" * 60)

# ============================================================
# 1. robots.txt 修正
# ============================================================
print("\n📋 1. robots.txt を修正中...")

robots = f"""User-agent: *
Allow: /
Sitemap: https://www.devtools-japan.com/sitemap.xml

User-agent: Googlebot
Allow: /

User-agent: bingbot
Allow: /

# AI Crawlers - LLMO対策
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: cohere-ai
Allow: /
"""

with open(os.path.join(BASE, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)
print("  ✅ robots.txt: www統一 + AIクローラー6種を許可")


# ============================================================
# 2. llms.txt 作成（LLMO対策）
# ============================================================
print("\n📋 2. llms.txt を作成中...")

llms_txt = """# DevTools Japan

> 日本の開発者・デザイナー・フリーランス・士業向けの無料オンラインツール集。61種類以上のツールをブラウザだけで利用可能。会員登録不要・サーバー送信なし。

## サイト情報
- URL: https://www.devtools-japan.com
- API: https://api.devtools-japan.com
- 運営: DevTools Japan
- 言語: 日本語
- 料金: 全ツール無料

## ツールカテゴリ

### 開発者向けツール
- JSON整形ツール: https://www.devtools-japan.com/tool-03-json-formatter/
- 正規表現テスター: https://www.devtools-japan.com/tool-08-regex-tester/
- テキスト比較（Diff）: https://www.devtools-japan.com/tool-09-diff/
- Base64変換: https://www.devtools-japan.com/tool-06-base64/
- URLエンコード・デコード: https://www.devtools-japan.com/tool-07-url-encode/
- HTML特殊文字変換: https://www.devtools-japan.com/tool-14-html-escape/
- ハッシュ生成（MD5/SHA-256）: https://www.devtools-japan.com/tool-17-hash/
- UUID生成: https://www.devtools-japan.com/tool-36-uuid-gen/
- Unixタイムスタンプ変換: https://www.devtools-japan.com/tool-16-timestamp/
- Cron式ジェネレーター: https://www.devtools-japan.com/tool-30-cron-generator/
- chmod計算: https://www.devtools-japan.com/tool-45-chmod-calc/
- JWTデコーダー: https://www.devtools-japan.com/tool-48-jwt-decoder/
- SQLフォーマッター: https://www.devtools-japan.com/tool-49-sql-formatter/
- .htaccess生成: https://www.devtools-japan.com/tool-50-htaccess-gen/
- CSV⇔JSON変換: https://www.devtools-japan.com/tool-13-csv-json/
- パスワード生成: https://www.devtools-japan.com/tool-02-password-gen/
- IPアドレス確認: https://www.devtools-japan.com/tool-31-ip-checker/

### デザイナー向けツール
- カラーコード変換: https://www.devtools-japan.com/tool-05-color-converter/
- カラーパレット生成: https://www.devtools-japan.com/tool-46-color-palette/
- CSSグラデーション生成: https://www.devtools-japan.com/tool-38-gradient-gen/
- CSSボックスシャドウ生成: https://www.devtools-japan.com/tool-39-shadow-gen/
- SNS画像サイズ一覧: https://www.devtools-japan.com/tool-23-sns-image-sizes/
- OGPプレビュー: https://www.devtools-japan.com/tool-24-ogp-preview/
- アスペクト比計算: https://www.devtools-japan.com/tool-28-aspect-ratio/
- 画像圧縮: https://www.devtools-japan.com/tool-10-image-compress/
- Favicon生成: https://www.devtools-japan.com/tool-20-favicon/
- プレースホルダー画像: https://www.devtools-japan.com/tool-40-placeholder-img/

### 日本語・日本特化ツール
- 文字数カウンター: https://www.devtools-japan.com/tool-01-moji-counter/
- 和暦西暦変換: https://www.devtools-japan.com/tool-12-wareki/
- 全角半角変換: https://www.devtools-japan.com/tool-19-zenkaku-hankaku/
- 文章校正チェッカー: https://www.devtools-japan.com/tool-26-proofreader/
- 読み上げ時間計算: https://www.devtools-japan.com/tool-25-speech-time/

### フリーランス・副業向けツール
- 確定申告シミュレーター: https://www.devtools-japan.com/tool-21-tax-simulator/
- 源泉徴収税計算: https://www.devtools-japan.com/tool-22-withholding-tax/
- フリーランス年収シミュレーター: https://www.devtools-japan.com/tool-58-freelance-income/
- 請求書金額計算: https://www.devtools-japan.com/tool-52-invoice-calc/
- 国民健康保険料計算: https://www.devtools-japan.com/tool-60-nhi-calc/
- 個人事業税計算: https://www.devtools-japan.com/tool-61-business-tax/
- 減価償却計算: https://www.devtools-japan.com/tool-59-depreciation/

### ビジネス・士業向けツール
- 営業日計算: https://www.devtools-japan.com/tool-51-business-day-calc/
- 年齢・勤続年数計算: https://www.devtools-japan.com/tool-53-age-calc/
- 残業代・割増賃金計算: https://www.devtools-japan.com/tool-54-working-hours/
- 遅延損害金計算: https://www.devtools-japan.com/tool-55-late-fee-calc/
- 相続税シミュレーター: https://www.devtools-japan.com/tool-56-inheritance-tax/
- 印紙税額検索: https://www.devtools-japan.com/tool-57-stamp-duty/
- ローン返済シミュレーター: https://www.devtools-japan.com/tool-27-loan-calc/

## API
DevTools Japan APIとして30本以上の無料REST APIも提供。認証不要で即利用可能。
- ポータル: https://api.devtools-japan.com
- ドキュメント: https://api.devtools-japan.com/docs
- 和暦変換、祝日判定、郵便番号検索、全角半角変換、ハッシュ生成、UUID生成等

## ブログ
- フリーランスの確定申告ガイド: https://www.devtools-japan.com/blog/freelance-tax-guide/
- SNS画像サイズガイド: https://www.devtools-japan.com/blog/sns-image-size-guide/
- フリーランスの経費一覧: https://www.devtools-japan.com/blog/freelance-expenses/
- 副業の20万円ルール: https://www.devtools-japan.com/blog/side-job-tax-rule/
- 源泉徴収の計算方法: https://www.devtools-japan.com/blog/withholding-tax-guide/
"""

with open(os.path.join(BASE, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(llms_txt)
print("  ✅ llms.txt を作成（AIがサイト構造を理解するためのファイル）")


# ============================================================
# 3. sitemap.xml の lastmod を更新
# ============================================================
print("\n📋 3. sitemap.xml の lastmod を更新中...")

sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

# www統一
sitemap = sitemap.replace(
    "https://devtools-japan.com/sitemap.xml",
    "https://www.devtools-japan.com/sitemap.xml"
)

# lastmod を今日に更新
sitemap = re.sub(
    r'<lastmod>2026-03-11</lastmod>',
    f'<lastmod>{TODAY}</lastmod>',
    sitemap
)

# lastmod がないエントリに追加
def add_lastmod(match):
    loc = match.group(0)
    if '<lastmod>' not in loc:
        loc = loc.replace('<changefreq>', f'<lastmod>{TODAY}</lastmod>\n    <changefreq>')
    return loc

sitemap = re.sub(r'<url>.*?</url>', add_lastmod, sitemap, flags=re.DOTALL)

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)
print(f"  ✅ sitemap.xml: lastmod を {TODAY} に更新")


# ============================================================
# 4. FAQスキーマを主要ツールに追加（LLMO対策）
# ============================================================
print("\n📋 4. FAQスキーマを主要ツールに追加中...")

FAQ_DATA = {
    "tool-21-tax-simulator": {
        "questions": [
            {"q": "副業の確定申告はいくらから必要？", "a": "副業の所得（売上−経費）が年間20万円を超える場合、確定申告が必要です。ただし住民税の申告は20万円以下でも必要です。"},
            {"q": "青色申告と白色申告の違いは？", "a": "青色申告は最大65万円の特別控除が受けられ、赤字の繰越や家族への給与の経費化が可能です。白色申告は簡単ですが特別控除がありません。"},
            {"q": "フリーランスの所得税率は？", "a": "所得税は累進課税で、課税所得195万円以下は5%、330万円以下は10%、695万円以下は20%、900万円以下は23%と段階的に上がります。"}
        ]
    },
    "tool-22-withholding-tax": {
        "questions": [
            {"q": "源泉徴収税の計算方法は？", "a": "報酬が100万円以下の場合は報酬額×10.21%、100万円超の場合は超過分×20.42%＋102,100円です。"},
            {"q": "源泉徴収はどんな報酬にかかる？", "a": "原稿料、デザイン料、コンサルティング料、講演料、弁護士・税理士等の士業報酬が対象です。システム開発は原則対象外ですが、クライアントの判断で徴収される場合があります。"}
        ]
    },
    "tool-58-freelance-income": {
        "questions": [
            {"q": "フリーランスの手取りは月単価の何割？", "a": "一般的にフリーランスの手取りは売上の60〜70%程度です。所得税、住民税、国民健康保険、国民年金、個人事業税を差し引くと、会社員と同じ手取りを得るには1.3〜1.5倍の売上が必要です。"},
            {"q": "フリーランスが払う税金・社会保険は？", "a": "所得税、住民税、国民健康保険料、国民年金、個人事業税（所得290万超）の5つです。会社員と違い全額自己負担です。"}
        ]
    },
    "tool-51-business-day-calc": {
        "questions": [
            {"q": "営業日とは？", "a": "営業日とは土曜日、日曜日、祝日（振替休日・国民の休日含む）を除いた平日のことです。ビジネスでは支払期限や届出期限が営業日ベースで設定されることが多くあります。"},
            {"q": "3営業日後の計算方法は？", "a": "基準日の翌日から数えて、土日祝を除いた3日目が該当日です。例えば金曜が基準日なら、翌月曜・火曜・水曜の3営業日後は水曜日になります。"}
        ]
    },
    "tool-54-working-hours": {
        "questions": [
            {"q": "残業代の計算方法は？", "a": "月給制の場合、時間単価（月給÷月の所定労働時間）に割増率を掛けます。時間外労働は25%増（×1.25）、深夜労働は25%増、休日労働は35%増（×1.35）です。"},
            {"q": "月60時間超の残業代は？", "a": "2023年4月から全企業で月60時間を超える時間外労働は50%以上の割増賃金が必要です。"}
        ]
    },
    "tool-56-inheritance-tax": {
        "questions": [
            {"q": "相続税の基礎控除額はいくら？", "a": "3,000万円＋600万円×法定相続人の数です。例えば配偶者と子供2人（計3人）なら基礎控除は4,800万円で、遺産総額がこれ以下なら相続税はかかりません。"},
            {"q": "相続税の税率は？", "a": "累進課税で、1,000万円以下は10%、3,000万円以下は15%、5,000万円以下は20%、1億円以下は30%と段階的に上がります。最高税率は6億円超の55%です。"}
        ]
    },
}

faq_count = 0
for tool_dir, data in FAQ_DATA.items():
    filepath = os.path.join(BASE, tool_dir, "index.html")
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "FAQPage" in content:
        continue

    # FAQスキーマ生成
    faq_items = []
    for q in data["questions"]:
        faq_items.append(f'{{"@type":"Question","name":"{q["q"]}","acceptedAnswer":{{"@type":"Answer","text":"{q["a"]}"}}}}')

    faq_schema = f'''    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join(faq_items)}]}}
    </script>'''

    content = content.replace("</head>", faq_schema + "\n</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    faq_count += 1

print(f"  ✅ {faq_count}ツールにFAQスキーマを追加")


# ============================================================
# 完了
# ============================================================
print("\n" + "=" * 60)
print("  完了！")
print("=" * 60)
print()
print("デプロイ:")
print("  git add .")
print('  git commit -m "LLMO: robots.txt AI crawlers, llms.txt, FAQ schema, sitemap lastmod update"')
print("  git push")
print()
print("push後:")
print("  1. Search Console で sitemap.xml を再送信")
print("  2. AdSense で再審査リクエスト")
print("  3. Search Console「ページのインデックス登録」のスクリーンショットを撮って確認")
