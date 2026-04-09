#!/usr/bin/env python3
"""
DevTools Japan — Favicon設置 + ブログ記事3本追加
"""
import os, re

BASE = "/Users/tom/Desktop/devtools-japan-complete"

# ============================================================
# 1. 全HTMLファイルにfaviconリンクを追加
# ============================================================
print("📋 1. favicon を全ページに設置中...")

FAVICON_TAG = '    <link rel="icon" href="/favicon.svg" type="image/svg+xml">'
count = 0

for root, dirs, files in os.walk(BASE):
    if '.git' in root:
        continue
    for fname in files:
        if not fname.endswith('.html') or fname.startswith('google'):
            continue
        filepath = os.path.join(root, fname)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'favicon.svg' in content:
            continue
        
        # <meta charset の直後に挿入
        if '<meta charset="UTF-8">' in content:
            content = content.replace(
                '<meta charset="UTF-8">',
                '<meta charset="UTF-8">\n' + FAVICON_TAG
            )
        elif '</head>' in content:
            content = content.replace('</head>', FAVICON_TAG + '\n</head>')
        else:
            continue
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"  ✅ {count}ファイルにfaviconを設置")

# ============================================================
# 2. ブログ記事3本を追加
# ============================================================
print("\n📋 2. ブログ記事3本を作成中...")

COMMON_HEAD = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-E27Q8YTG7L');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072" crossorigin="anonymous"></script>
<meta charset="UTF-8">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta name="viewport" content="width=device-width, initial-scale=1.0">"""

COMMON_STYLE = """<style>
:root{--bg:#f7f8fb;--bg-card:#fff;--border:#e0e2ed;--text:#1e1e35;--text2:#5a5f78;--text3:#9498b0;--accent:#10b981;--radius:12px}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);line-height:2}
.container{max-width:800px;margin:0 auto;padding:40px 20px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
h1{font-size:1.4rem;font-weight:700;color:var(--text);margin-bottom:8px;line-height:1.5}
h2{font-size:1.2rem;font-weight:600;margin-top:36px;margin-bottom:12px;color:var(--text);border-left:4px solid var(--accent);padding-left:12px}
h3{font-size:1rem;font-weight:600;margin-top:24px;margin-bottom:8px;color:var(--text)}
p{margin-bottom:16px;color:var(--text2);font-size:0.9rem}
.meta{font-size:0.75rem;color:var(--text3);margin-bottom:32px}
.back{display:inline-flex;align-items:center;gap:6px;margin-bottom:24px;font-size:0.8rem;color:var(--text3);text-decoration:none}
.card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin:20px 0}
ul{margin:0 0 16px 20px;color:var(--text2);font-size:0.9rem}li{margin-bottom:6px}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:0.85rem}
th{background:var(--bg-card);border:1px solid var(--border);padding:10px 12px;text-align:left;font-weight:600}
td{border:1px solid var(--border);padding:10px 12px;color:var(--text2)}
.cta{background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);border-radius:var(--radius);padding:20px;margin:24px 0;text-align:center}
.cta p{color:var(--text);margin-bottom:8px}
footer{text-align:center;margin-top:60px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}
</style>"""

COMMON_FOOTER = """<footer>
<p style="margin-bottom:8px">&copy; 2026 DevTools Japan</p>
<p style="font-size:0.65rem"><a href="/" style="color:inherit">トップ</a> | <a href="/blog/" style="color:inherit">ブログ</a> | <a href="/about/" style="color:inherit">サイトについて</a> | <a href="/privacy/" style="color:inherit">プライバシーポリシー</a></p>
</footer>"""

# --- 記事1: フリーランスの経費一覧 ---
art1_dir = os.path.join(BASE, "blog", "freelance-expenses")
os.makedirs(art1_dir, exist_ok=True)

art1 = f"""<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
<title>フリーランスエンジニアの経費一覧 — 何が落とせる？【2026年版】 | DevTools Japan</title>
<meta name="description" content="フリーランスエンジニアが経費にできるもの・できないものを一覧で解説。通信費、家賃按分、PC購入費、サブスク、書籍、カフェ代など具体例付きで紹介。">
<link rel="canonical" href="https://www.devtools-japan.com/blog/freelance-expenses/">
<meta property="og:title" content="フリーランスエンジニアの経費一覧【2026年版】">
<meta property="og:description" content="何が経費になる？通信費、家賃、PC、サブスク、書籍を具体例で解説">
<meta property="og:url" content="https://www.devtools-japan.com/blog/freelance-expenses/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"フリーランスエンジニアの経費一覧","datePublished":"2026-04-09","author":{{"@type":"Organization","name":"DevTools Japan"}},"publisher":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
{COMMON_STYLE}
</head>
<body>
<div class="container">
<a href="/blog/" class="back"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg> ブログ一覧に戻る</a>
<h1>フリーランスエンジニアの経費一覧 — 何が落とせる？【2026年版】</h1>
<div class="meta">2026年4月9日 公開 | DevTools Japan</div>

<p>フリーランスとして独立すると、確定申告で経費を計上できるようになります。経費が増えれば課税所得が減り、結果的に税金が安くなります。でも「何が経費になるのか」がわからないと、本来落とせるはずの経費を見逃してしまうことも。この記事では、フリーランスエンジニアが経費にできるものを具体例付きで一覧にまとめました。</p>

<h2>エンジニアの経費になるもの一覧</h2>

<table>
<tr><th>勘定科目</th><th>具体例</th><th>ポイント</th></tr>
<tr><td>通信費</td><td>インターネット回線、スマホ料金</td><td>事業使用割合で按分（50〜80%が一般的）</td></tr>
<tr><td>地代家賃</td><td>自宅の家賃（作業スペース分）</td><td>面積比で按分（例: 25%が作業部屋なら家賃の25%）</td></tr>
<tr><td>消耗品費</td><td>10万円未満のPC周辺機器、マウス、キーボード、モニター、ケーブル</td><td>10万円未満は一括経費</td></tr>
<tr><td>減価償却費</td><td>10万円以上のPC、ディスプレイ</td><td>4年で減価償却（青色申告なら30万円未満は一括可）</td></tr>
<tr><td>外注費</td><td>デザイン発注、他のフリーランスへの外注</td><td>源泉徴収が必要な場合あり</td></tr>
<tr><td>旅費交通費</td><td>客先訪問の電車代、タクシー代</td><td>ICカード履歴やレシートを保管</td></tr>
<tr><td>会議費</td><td>打ち合わせのカフェ代、ランチミーティング</td><td>1人5,000円以下が目安</td></tr>
<tr><td>新聞図書費</td><td>技術書籍、Udemy等のオンライン講座</td><td>事業に関連するものに限る</td></tr>
<tr><td>ソフトウェア費</td><td>Adobe CC、AWS、GitHub、ドメイン、サーバー</td><td>月額サブスクも年額で計上可</td></tr>
<tr><td>水道光熱費</td><td>電気代（自宅作業分）</td><td>面積比や時間比で按分</td></tr>
<tr><td>支払手数料</td><td>クラウドソーシングの手数料、振込手数料</td><td>全額経費OK</td></tr>
<tr><td>広告宣伝費</td><td>名刺作成、ポートフォリオサイトのドメイン</td><td>事業に関連するもの</td></tr>
<tr><td>諸会費</td><td>コワーキングスペースの月額利用料</td><td>全額経費OK</td></tr>
<tr><td>保険料</td><td>フリーランス向け賠償責任保険</td><td>事業用のみ（生命保険は控除で対応）</td></tr>
</table>

<h2>按分（あんぶん）とは？</h2>
<p>自宅で仕事をしている場合、家賃や電気代は「事業用」と「プライベート用」が混在します。これを事業使用割合に応じて分けることを「按分」と言います。</p>

<div class="card">
<h3>按分の計算例</h3>
<p><strong>家賃10万円、自宅の25%が作業部屋の場合:</strong></p>
<p>10万円 x 25% = 2.5万円/月 = 年間30万円が経費</p>
<p><strong>インターネット回線 月5,000円、事業利用70%の場合:</strong></p>
<p>5,000円 x 70% = 3,500円/月 = 年間42,000円が経費</p>
</div>

<p>按分割合に厳密なルールはありませんが、税務調査で説明できる合理的な根拠が必要です。「作業部屋の面積比」「業務時間の割合」など、客観的に説明できる基準を使いましょう。</p>

<h2>経費にできないもの</h2>
<ul>
<li><strong>所得税・住民税</strong>: 税金自体は経費にならない（事業税・消費税は可）</li>
<li><strong>生活費</strong>: 食費、衣服代（作業着を除く）、趣味の支出</li>
<li><strong>罰金・反則金</strong>: 駐車違反の罰金等</li>
<li><strong>プライベートの旅行費</strong>: 事業との関連性がないもの</li>
<li><strong>家族への給与</strong>: 青色事業専従者でない限り不可</li>
</ul>

<h2>経費を漏らさないコツ</h2>
<h3>1. レシートは即スマホで撮影</h3>
<p>紙のレシートは紛失しやすいので、もらったその場でスマホで撮影する習慣をつけましょう。freeeやマネーフォワードのアプリなら、写真から自動で仕訳できます。</p>

<h3>2. 事業用クレジットカードを分ける</h3>
<p>事業用とプライベート用のクレジットカードを分けておくと、年末の経費集計が格段に楽になります。明細がそのまま経費帳簿になります。</p>

<h3>3. サブスクリプションを見直す</h3>
<p>Adobe CC、GitHub、AWS、ドメイン、サーバーなど、エンジニアは月額サービスの支出が多いです。これらはすべて経費にできるので、漏れなく計上しましょう。</p>

<div class="cta">
<p><strong>経費を入力して税金をシミュレーション</strong></p>
<p><a href="/tool-21-tax-simulator/">確定申告シミュレーター</a>で売上・経費・控除を入力すると、所得税・住民税・手取り額がすぐにわかります。</p>
</div>

<h2>まとめ</h2>
<ul>
<li>通信費・家賃・電気代は按分で経費にできる</li>
<li>PC・モニター・書籍・サブスクは事業関連なら全額経費</li>
<li>レシートの即時撮影と事業用カード分離が経費管理のコツ</li>
<li>青色申告なら30万円未満の資産を一括経費にできる特例あり</li>
</ul>
<p>※この記事は一般的な情報提供です。個別の判断は税理士にご相談ください。</p>

{COMMON_FOOTER}
</div>
</body>
</html>"""

with open(os.path.join(art1_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(art1)
print("  ✅ blog/freelance-expenses/ を作成")

# --- 記事2: 副業の20万円ルール ---
art2_dir = os.path.join(BASE, "blog", "side-job-tax-rule")
os.makedirs(art2_dir, exist_ok=True)

art2 = f"""<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
<title>副業の確定申告は必要？20万円ルールを正しく理解する【2026年版】 | DevTools Japan</title>
<meta name="description" content="副業の所得が20万円を超えたら確定申告が必要？住民税はどうなる？会社にバレない方法は？副業の税金に関する疑問を初心者向けにわかりやすく解説。">
<link rel="canonical" href="https://www.devtools-japan.com/blog/side-job-tax-rule/">
<meta property="og:title" content="副業の確定申告は必要？20万円ルール【2026年版】">
<meta property="og:description" content="副業の所得20万円で確定申告が必要？住民税は？会社バレ対策も解説">
<meta property="og:url" content="https://www.devtools-japan.com/blog/side-job-tax-rule/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"副業の確定申告は必要？20万円ルールを正しく理解する","datePublished":"2026-04-09","author":{{"@type":"Organization","name":"DevTools Japan"}},"publisher":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
{COMMON_STYLE}
</head>
<body>
<div class="container">
<a href="/blog/" class="back"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg> ブログ一覧に戻る</a>
<h1>副業の確定申告は必要？20万円ルールを正しく理解する【2026年版】</h1>
<div class="meta">2026年4月9日 公開 | DevTools Japan</div>

<p>副業を始めた方が最初にぶつかる疑問が「確定申告って必要なの？」ということ。よく聞く「20万円ルール」は正しく理解しないと、思わぬ税金トラブルになることがあります。この記事では、副業の税金の基本ルールをわかりやすく解説します。</p>

<h2>20万円ルールとは？</h2>
<p>会社員（給与所得者）が副業をしている場合、<strong>副業の所得が年間20万円以下であれば、所得税の確定申告は不要</strong>です。これが「20万円ルール」です。</p>

<div class="card">
<h3>重要なポイント</h3>
<ul>
<li>「売上」ではなく「所得」（売上 − 経費）で判断する</li>
<li>所得税の確定申告が不要なだけで、住民税の申告は別途必要</li>
<li>給与所得者にのみ適用（フリーランス本業の方は対象外）</li>
<li>副業が複数ある場合は合算して判断</li>
</ul>
</div>

<h2>所得の計算方法</h2>
<p>「所得」は「売上（収入）」から「経費」を引いた金額です。</p>

<div class="card">
<h3>計算例</h3>
<p><strong>例1:</strong> Webサイト制作の副業で年間売上50万円、経費（PC・通信費・サーバー代等）が35万円の場合</p>
<p>所得 = 50万円 − 35万円 = <strong>15万円 → 確定申告不要</strong>（20万円以下）</p>
<p><strong>例2:</strong> プログラミング教室の副業で年間売上40万円、経費が10万円の場合</p>
<p>所得 = 40万円 − 10万円 = <strong>30万円 → 確定申告が必要</strong>（20万円超）</p>
</div>

<h2>住民税の申告は別途必要</h2>
<p>20万円ルールで確定申告が不要になっても、<strong>住民税の申告は必要</strong>です。これを知らない人が非常に多いので要注意です。</p>
<p>住民税は市区町村に申告します。お住まいの市区町村の窓口で「住民税の申告」を行うか、eLTAX（地方税ポータル）で電子申告できます。</p>

<h2>副業が会社にバレない方法</h2>
<p>副業が会社に知られる最も多い原因は「住民税の通知」です。副業で収入が増えると住民税が上がり、会社の経理部門が気づく可能性があります。</p>

<div class="card">
<h3>対策: 住民税の普通徴収を選択する</h3>
<p>確定申告の際に、住民税の納付方法で<strong>「自分で納付（普通徴収）」</strong>を選択します。これにより、副業分の住民税は自分で直接納付することになり、会社の給与天引き額に影響しません。</p>
<p>ただし、市区町村によっては普通徴収に対応していない場合もあるため、事前に確認しておきましょう。</p>
</div>

<h2>副業の税金はいくらかかる？</h2>
<p>副業の所得にかかる税金は、本業の給与と合算した総所得に対して累進課税で計算されます。</p>

<table>
<tr><th>課税所得</th><th>税率</th><th>控除額</th></tr>
<tr><td>〜195万円</td><td>5%</td><td>0円</td></tr>
<tr><td>195〜330万円</td><td>10%</td><td>97,500円</td></tr>
<tr><td>330〜695万円</td><td>20%</td><td>427,500円</td></tr>
<tr><td>695〜900万円</td><td>23%</td><td>636,000円</td></tr>
<tr><td>900〜1800万円</td><td>33%</td><td>1,536,000円</td></tr>
</table>

<p>例えば、本業の課税所得が350万円（税率20%）の方が副業で50万円の所得があった場合、副業分にかかる所得税は概算で約10万円（50万円 x 20%）+住民税5万円（50万円 x 10%）= 約15万円です。</p>

<div class="cta">
<p><strong>副業の税金を具体的に計算してみましょう</strong></p>
<p><a href="/tool-21-tax-simulator/">確定申告シミュレーター</a>で売上・経費を入力すると、所得税・住民税・手取り額がすぐにわかります。</p>
</div>

<h2>確定申告の時期と方法</h2>
<ul>
<li><strong>申告期間:</strong> 毎年2月16日〜3月15日（土日の場合は翌営業日）</li>
<li><strong>申告方法:</strong> e-Tax（電子申告）、税務署への郵送、税務署窓口での提出</li>
<li><strong>必要なもの:</strong> 源泉徴収票（本業分）、副業の収支内訳書、マイナンバーカード</li>
</ul>
<p>e-Taxならスマホやパソコンから24時間申告でき、還付金の受取も早くなります。</p>

<h2>まとめ</h2>
<ul>
<li>副業所得20万円以下なら所得税の確定申告は不要（住民税は別途必要）</li>
<li>「所得」=「売上−経費」で判断。経費を漏れなく計上することが重要</li>
<li>会社バレ防止は住民税の「普通徴収」を選択</li>
<li>20万円を超えたら確定申告が必要。青色申告で65万円控除を活用</li>
</ul>
<p>※この記事は一般的な情報提供です。個別の税務判断は税理士にご相談ください。</p>

{COMMON_FOOTER}
</div>
</body>
</html>"""

with open(os.path.join(art2_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(art2)
print("  ✅ blog/side-job-tax-rule/ を作成")

# --- 記事3: 源泉徴収の計算方法 ---
art3_dir = os.path.join(BASE, "blog", "withholding-tax-guide")
os.makedirs(art3_dir, exist_ok=True)

art3 = f"""<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
<title>源泉徴収とは？フリーランスが知っておくべき計算方法と請求書の書き方 | DevTools Japan</title>
<meta name="description" content="フリーランスが受け取る報酬の源泉徴収について解説。10.21%の計算方法、100万円超の場合の税率、請求書への記載方法、確定申告での還付申請まで。">
<link rel="canonical" href="https://www.devtools-japan.com/blog/withholding-tax-guide/">
<meta property="og:title" content="源泉徴収とは？フリーランスの計算方法と請求書の書き方">
<meta property="og:description" content="フリーランスの源泉徴収を解説。計算方法、請求書の書き方、確定申告での還付まで">
<meta property="og:url" content="https://www.devtools-japan.com/blog/withholding-tax-guide/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"源泉徴収とは？フリーランスが知っておくべき計算方法","datePublished":"2026-04-09","author":{{"@type":"Organization","name":"DevTools Japan"}},"publisher":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
{COMMON_STYLE}
</head>
<body>
<div class="container">
<a href="/blog/" class="back"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg> ブログ一覧に戻る</a>
<h1>源泉徴収とは？フリーランスが知っておくべき計算方法と請求書の書き方</h1>
<div class="meta">2026年4月9日 公開 | DevTools Japan</div>

<p>フリーランスとして仕事を受けると、請求書の金額から「源泉徴収税」が差し引かれて振り込まれることがあります。「請求した金額より少ない…」と焦った経験がある方もいるのではないでしょうか。この記事では、源泉徴収の仕組みと計算方法、請求書の書き方を解説します。</p>

<h2>源泉徴収とは</h2>
<p>源泉徴収とは、報酬を支払う側（クライアント）が、支払い時に所得税を差し引いて国に納付する制度です。フリーランスが確定申告で自分で納税する代わりに、クライアントが「先払い」してくれる仕組みです。</p>
<p>源泉徴収された税額は、確定申告で精算されます。経費や控除を考慮した結果、払いすぎていれば還付（返金）されます。</p>

<h2>源泉徴収の対象となる報酬</h2>
<p>すべてのフリーランス報酬に源泉徴収がかかるわけではありません。源泉徴収の対象となる主な報酬は以下の通りです。</p>
<ul>
<li>原稿料・講演料</li>
<li>デザイン料</li>
<li>コンサルティング料</li>
<li>弁護士・税理士・社労士等の士業報酬</li>
<li>プロスポーツ選手の報酬</li>
</ul>
<p><strong>システム開発・プログラミングの報酬は、原則として源泉徴収の対象外</strong>です。ただし、デザインを含む場合や、クライアントの判断で源泉徴収されるケースもあります。</p>

<h2>源泉徴収税額の計算方法</h2>

<div class="card">
<h3>報酬が100万円以下の場合</h3>
<p>源泉徴収税額 = 報酬額 x <strong>10.21%</strong></p>
<p>例: 報酬30万円の場合 → 300,000 x 10.21% = <strong>30,630円</strong></p>
<p>振込額: 300,000 - 30,630 = <strong>269,370円</strong></p>
</div>

<div class="card">
<h3>報酬が100万円を超える場合</h3>
<p>源泉徴収税額 = (報酬額 - 100万円) x <strong>20.42%</strong> + <strong>102,100円</strong></p>
<p>例: 報酬150万円の場合 → (1,500,000 - 1,000,000) x 20.42% + 102,100 = <strong>204,200円</strong></p>
<p>振込額: 1,500,000 - 204,200 = <strong>1,295,800円</strong></p>
</div>

<p>10.21%の内訳は、所得税10% + 復興特別所得税0.21%です。</p>

<h2>消費税と源泉徴収の関係</h2>
<p>請求書に消費税を明記している場合、<strong>税抜き金額に対して源泉徴収</strong>が計算されます。消費税を明記していない場合は、税込み金額に対して計算されるため、源泉徴収額が多くなります。</p>

<div class="card">
<h3>消費税を明記した場合の計算例</h3>
<p>報酬: 30万円（税抜き）+ 消費税30,000円 = 合計330,000円</p>
<p>源泉徴収: 300,000 x 10.21% = 30,630円（税抜き額に対して計算）</p>
<p>振込額: 330,000 - 30,630 = <strong>299,370円</strong></p>
</div>

<p>消費税を明記するだけで、手取りが増えます。請求書には必ず消費税額を記載しましょう。</p>

<h2>請求書への記載方法</h2>
<p>源泉徴収ありの請求書には、以下の項目を記載します。</p>
<ul>
<li>報酬額（税抜き）</li>
<li>消費税額</li>
<li>源泉徴収税額（マイナス表記）</li>
<li>差引請求額（振込額）</li>
</ul>

<div class="card">
<h3>請求書の記載例</h3>
<p>Webデザイン制作費: 300,000円</p>
<p>消費税（10%）: 30,000円</p>
<p>小計: 330,000円</p>
<p>源泉徴収税額: -30,630円</p>
<p><strong>ご請求額: 299,370円</strong></p>
</div>

<h2>確定申告で還付を受ける</h2>
<p>源泉徴収された税金は、あくまで「仮の税額」です。確定申告で年間の所得と経費を正しく計算した結果、源泉徴収額が本来の税額より多ければ、差額が還付（返金）されます。</p>
<p>特に経費が多いフリーランスは、源泉徴収で払いすぎているケースが多いため、確定申告での還付は重要です。確定申告書の「源泉徴収税額」欄に年間の源泉徴収合計額を記入します。</p>

<div class="cta">
<p><strong>源泉徴収税額を計算する</strong></p>
<p><a href="/tool-22-withholding-tax/">源泉徴収税計算ツール</a>で報酬額を入力するだけで、源泉徴収額と振込額がすぐにわかります。</p>
<p><a href="/tool-21-tax-simulator/">確定申告シミュレーター</a>で年間の税額と手取りも確認しましょう。</p>
</div>

<h2>まとめ</h2>
<ul>
<li>源泉徴収はクライアントが所得税を先払いする制度</li>
<li>報酬100万円以下は10.21%、100万円超の部分は20.42%</li>
<li>請求書に消費税を明記すれば、税抜き額で計算されて手取りが増える</li>
<li>確定申告で払いすぎた分は還付される</li>
<li>システム開発は原則対象外だが、クライアントの判断で徴収される場合もある</li>
</ul>
<p>※この記事は一般的な情報提供です。個別の税務判断は税理士にご相談ください。</p>

{COMMON_FOOTER}
</div>
</body>
</html>"""

with open(os.path.join(art3_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(art3)
print("  ✅ blog/withholding-tax-guide/ を作成")

# ============================================================
# 3. ブログインデックスに新記事を追加
# ============================================================
print("\n📋 3. ブログインデックスを更新中...")

blog_index_path = os.path.join(BASE, "blog", "index.html")
with open(blog_index_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

new_posts = """<div class="post-card">
<h2><a href="/blog/freelance-expenses/">フリーランスエンジニアの経費一覧 — 何が落とせる？【2026年版】</a></h2>
<div class="post-meta">2026年4月9日</div>
<p class="post-excerpt">通信費、家賃按分、PC購入費、サブスク、書籍、カフェ代…フリーランスエンジニアが経費にできるもの・できないものを具体例付きで一覧にしました。</p>
</div>

<div class="post-card">
<h2><a href="/blog/side-job-tax-rule/">副業の確定申告は必要？20万円ルールを正しく理解する【2026年版】</a></h2>
<div class="post-meta">2026年4月9日</div>
<p class="post-excerpt">副業の所得が20万円を超えたら確定申告が必要。住民税の申告は別途必要。会社にバレない方法も解説。</p>
</div>

<div class="post-card">
<h2><a href="/blog/withholding-tax-guide/">源泉徴収とは？フリーランスが知っておくべき計算方法と請求書の書き方</a></h2>
<div class="post-meta">2026年4月9日</div>
<p class="post-excerpt">フリーランスの報酬から引かれる源泉徴収の仕組み、10.21%の計算方法、請求書の書き方、確定申告での還付まで。</p>
</div>

"""

# フッターの前に追加
if "freelance-expenses" not in blog_content:
    blog_content = blog_content.replace("<footer>", new_posts + "\n<footer>")
    # faviconも追加
    if "favicon.svg" not in blog_content:
        blog_content = blog_content.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">')
    with open(blog_index_path, "w", encoding="utf-8") as f:
        f.write(blog_content)
    print("  ✅ ブログインデックスに3記事を追加")

# ============================================================
# 4. sitemap.xmlに新記事を追加
# ============================================================
print("\n📋 4. sitemap.xml を更新中...")

sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_urls = """  <url>
    <loc>https://www.devtools-japan.com/blog/freelance-expenses/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.devtools-japan.com/blog/side-job-tax-rule/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.devtools-japan.com/blog/withholding-tax-guide/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""

if "freelance-expenses" not in sitemap:
    sitemap = sitemap.replace("</urlset>", new_urls + "\n</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("  ✅ sitemap.xml に3記事を追加")

print("\n" + "=" * 60)
print("  完了！")
print("=" * 60)
print()
print("追加されたもの:")
print("  - favicon.svg（緑色のコードブラケットアイコン）")
print("  - 全HTMLファイルにfaviconリンク")
print("  - blog/freelance-expenses/（フリーランスの経費一覧）")
print("  - blog/side-job-tax-rule/（副業の20万円ルール）")
print("  - blog/withholding-tax-guide/（源泉徴収の計算方法）")
print()
print("デプロイ:")
print("  git add .")
print('  git commit -m "Add favicon, 3 blog articles targeting freelance/副業 keywords"')
print("  git push")
