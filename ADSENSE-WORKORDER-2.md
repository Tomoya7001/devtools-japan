# AdSense対策 第2弾 — Claude Code 作業指示書

作成日: 2026-06-10 / 対象リポジトリ: `devtools-japan-complete`（本リポジトリ）
前提: 第1弾 `ADSENSE-WORKORDER.md` 完了済み（優先8ツール＋最薄11＋blog9本）。本書はその続き。

## 目的
サイトにまだ残る **可視テキスト1,000字未満の48ツールを全て1,000字以上へ増強**する。第1弾と同品質・同手順。noindexは原則使わず**全て増強**（第1弾の方針を踏襲）。どうしても800字相当の独自コンテンツが作れないツールのみ、自動でnoindexせず `# TODO要確認:` を残して人間判断を仰ぐ。

---

## 1. 絶対遵守のガードレール（第1弾と同一・再掲）
1. **既存のインタラクティブUI・`<script>`計算ロジックには一切触らない。差分は追加のみ**（メタ/JSON-LD追記を除き、既存行の削除・改変禁止）。
2. 追加は必ず**ツール操作部の下**（`.seo-content`領域）。ファーストビュー＝即使える状態を維持。
3. **新規CSSは追加のみ**。`.lookup-table` `.faq-item` 等は第1弾で増強済みツール（例 `tool-25-speech-time/index.html`）からコピー。既存ルール書き換え禁止。
4. デザイン統一: 絵文字禁止／ベタ塗りSVGアイコン（`fill="currentColor"`）／Noto Sans JP+JetBrains Mono／白基調／全処理ブラウザ完結。
5. モバイル幅(<600px)で崩さない。横長表は `overflow-x:auto` ラッパに入れる。
6. **数値・換算表・税額は必ずコードで計算して検証**してから記載（憶測値禁止）。**計算系ツールの表は、そのツール自身のJS計算式と同一ロジックで算出**し整合させる（第1弾 tool-64方式）。
7. 税・法律系の数値は**公式（国税庁等）の区分に厳密準拠**。確証が持てない値は `# TODO要確認:` ＋出典URLを残す。
8. FAQ（5問）は**見える本文と FAQPage JSON-LD を完全一致**させる。
9. 各ページ目標: **可視テキスト1,000〜1,500字以上**。一般論の水増し禁止、そのツール固有の具体例・数字を入れる。

---

## 2. 追加する「型」（第1弾と同一）
操作部の下に `<div class="seo-content">` で:
1. **使い方・具体例**（独自の切り口・具体的な場面/数字）
2. **早見表・対応表・変換例**（該当すれば。数値はコード検証）
3. **「○○とは」概念・背景解説**（開発系で特に有効）
4. **よくある質問 5問**（見える本文 `.faq-item` ＋ FAQPage JSON-LD）

---

## 3. 対象48ツール（この順で実施：A=お金/税金系を先、B=開発/ユーティリティ系）

### グループA：お金・税金・実務計算系（18本／検索需要が高い・最優先）
表は必ず**ツールJSと同一式でコード算出**。税・制度は公式準拠＋出典明記。

| ツール | 現状 | 追加コンテンツの要点 |
|---|---|---|
| tool-27-loan-calc ローン返済 | 549 | 借入額×金利×期間の返済額早見表、元利均等の仕組み、総返済額の見方。FAQ「3000万・35年・1%の月返済は？」等 |
| tool-52-invoice-calc 請求書金額 | 584 | 小計→消費税→源泉→振込手数料の計算順序、税込/税抜の例、源泉対象の判定。FAQ |
| tool-12-wareki 和暦西暦 | 636 | 令和/平成/昭和の西暦対応表、改元年の数え方、年齢との関係。FAQ「令和7年は西暦何年？」 |
| tool-55-late-fee-calc 遅延損害金 | 744 | 法定利率・年率別の遅延損害金計算式と例、起算日の考え方。FAQ。要確認:現行法定利率は出典付きで |
| tool-67-wage-converter 時給/月給/年収 | 754 | 時給⇔月給⇔年収の換算表（労働時間前提を明記）、各換算式。FAQ「時給1500円は年収いくら？」 |
| tool-65-consumption-tax 消費税 | 782 | 8%/10%軽減税率の対象、税込⇔税抜の計算式と例、端数処理。FAQ |
| tool-69-currency-calc 為替 | 820 | 主要通貨の換算の考え方、レートの読み方、手数料/スプレッド注意。FAQ（※リアルタイムレートは扱わない旨明記） |
| tool-68-invoice-tax インボイス消費税 | 823 | 適格請求書の記載要件、税率別の消費税計算、端数処理ルール。FAQ。国税庁出典 |
| tool-59-depreciation 減価償却 | 831 | 定額法/定率法の違い、耐用年数別の例、少額資産特例。FAQ。要確認:耐用年数表は出典付き |
| tool-54-working-hours 残業代 | 836 | 割増率（時間外25%/深夜25%/休日35%）と計算式・具体例。FAQ。労基法準拠で出典 |
| tool-60-nhi-calc 国保 | 839 | 国保料の構成（医療/支援/介護）、所得別の概算例、自治体差の注意。FAQ |
| tool-58-freelance-income フリーランス年収 | 891 | 売上→経費→所得→手取りの流れ、税・社保の概算。FAQ。概算前提を明記 |
| tool-56-inheritance-tax 相続税 | 927 | 基礎控除（3000万+600万×法定相続人）、税率速算表、具体例。FAQ。国税庁出典 |
| tool-66-furusato-tax ふるさと納税 | 952 | 上限額の決まり方、年収・家族構成別の目安表、ワンストップ特例。FAQ。概算前提 |
| tool-61-business-tax 個人事業税 | 967 | 業種別税率（3〜5%）、事業主控除290万、計算例。FAQ。要確認:業種区分は出典付き |
| tool-51-business-day-calc 営業日 | 684 | 営業日の数え方、祝日の扱い、納期計算の例。FAQ「5営業日後はいつ？」 |
| tool-01-moji-counter 文字数カウンター | 788 | 各SNS/媒体の文字数制限表（X/Insta/原稿用紙/レポート等）、全角半角の数え方。FAQ |
| tool-26-proofreader 文章校正 | 649 | チェック観点（誤字/二重表現/表記ゆれ）、使いどころ、限界。FAQ |

### グループB：開発・ユーティリティ系（30本／増強）
開発系も日本語検索需要あり（「base64 デコード」「cron 書き方」「正規表現 チェック」等）。各ツールに「**○○とは／仕組み**」「**よくある使い方・変換例の表**」「**FAQ5問**」を追加して1,000字超へ。

対象（薄い順）:
tool-38-gradient-gen / tool-18-dummy-text / tool-24-ogp-preview / tool-44-tab-space / tool-36-uuid-gen / tool-19-zenkaku-hankaku / tool-17-hash / tool-39-shadow-gen / tool-20-favicon / tool-03-json-formatter / tool-13-csv-json / tool-16-timestamp / tool-04-qr-generator / tool-31-ip-checker / tool-02-password-gen / tool-15-case-converter / tool-10-image-compress / tool-07-url-encode / tool-14-html-escape / tool-06-base64 / tool-49-sql-formatter / tool-42-number-format / tool-09-diff / tool-05-color-converter / tool-30-cron-generator / tool-35-random-number / tool-08-regex-tester / tool-37-number-base / tool-63-mac-address / tool-11-markdown-preview

**特に表が有効なもの（コード検証して載せる）:**
- tool-37-number-base: 2/8/10/16進の対応表（0〜16, 代表値）
- tool-16-timestamp: Unix時間⇔日時の例、桁（秒/ミリ秒）の違い
- tool-06-base64 / tool-07-url-encode / tool-14-html-escape: 代表文字の変換例表
- tool-30-cron-generator: cron書式の早見表（分時日月曜＋よく使う式の例）
- tool-05-color-converter: HEX/RGB/HSL対応例
- tool-19-zenkaku-hankaku: 全角半角の対応例（英数記号カナ）
- tool-63-mac-address: 区切り形式（コロン/ハイフン/ドット）の対応例

---

## 4. 1ツールごとの手順（第1弾と同一）
1. 対象 `index.html` と手本（第1弾で増強済みの近いツール）を読む。
2. 表の数値を**python等で計算**して確定（計算系はツールJSの式と一致させる）。
3. `<style>` に `.lookup-table` `.faq-item` が無ければ追加（既存ルールは触らない）。
4. 操作部の下に `.seo-content` で「使い方/表/解説/FAQ5」を追加。
5. FAQPage JSON-LD に同一Q&Aを追記。
6. title/meta descriptionを軽く調整（クエリ語を自然に。既存主要KWは残す）。
7. 下記検証を全項目パス → `git add <そのファイル>` → コミット。

## 5. 検証（コミット前に必須）
```python
import re,json
f="tool-XX-xxxx/index.html"
h=open(f,encoding='utf-8').read()
assert len(re.findall(r'<div\b',h))==len(re.findall(r'</div>',h)), "div不一致"
for b in re.findall(r'application/ld\+json">(.*?)</script>',h,re.S): json.loads(b)  # JSON妥当性
b=re.sub(r'<script.*?</script>','',h,flags=re.S); b=re.sub(r'<style.*?</style>','',b,flags=re.S)
chars=len(re.sub(r'\s','',re.sub(r'<[^>]+>',' ',b)))
assert chars>=1000, f"まだ薄い:{chars}"
# 既存JSが残っているか（ツール固有トークンで確認）。表に数値があれば式で再計算し一致確認。
print("OK", chars)
```
- ブラウザで (a)従来通り動作 (b)モバイルで崩れない を目視。

## 6. デプロイ
```bash
git add <対象ファイル>
git commit -m "Thicken <tool> content for AdSense (UX unchanged)"
git push   # SSH・Vercel自動
```
- 数ツールごとにpush。全48本完了後、`sitemap.xml` の lastmod を更新。

## 7. 完了の定義
- **70ツール全てが可視1,000字以上**（1000字未満 0本）。
- 全ページで検証スクリプトパス、UI/UX非劣化を目視確認。
- div崩れ・JSON破損ゼロ。
- sitemap.xml 更新。
- 完了後、人間がGSCでsitemap再送信／AdSense再申請（前回不承認から2〜3週間以上空ける）。
