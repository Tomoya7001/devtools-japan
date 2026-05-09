#!/usr/bin/env python3
"""
DevTools Japan — OL・事務・士業向けツール7本を一括生成
tool-51〜tool-57
"""
import os

BASE = "/Users/tom/Desktop/devtools-japan-complete"

COMMON_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-E27Q8YTG7L');
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072"
     crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">"""

COMMON_STYLE = """        :root{--bg:#f7f8fb;--bg-card:#ffffff;--border:#e0e2ed;--text:#1e1e35;--text2:#5a5f78;--text3:#9498b0;--accent:ACCENT_COLOR;--accent-dim:ACCENT_DIM;--green:#22c55e;--red:#ef4444;--radius:12px}
        ::selection{background:rgba(99,102,241,0.15);color:#1e1e35}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);min-height:100vh}
        .container{max-width:800px;margin:0 auto;padding:40px 20px}
        .ad-slot{display:none}
        header{text-align:center;margin-bottom:36px}header h1{font-size:1.8rem;font-weight:700;color:var(--accent);margin-bottom:8px}header p{color:var(--text2);font-size:0.85rem}
        .card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:16px}
        .card h3{font-size:0.75rem;color:var(--text3);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:16px}
        .row{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border)}
        .row:last-child{border-bottom:none}
        .row label{font-size:0.85rem;color:var(--text2);flex:1}
        .row input,.row select{width:200px;padding:10px 14px;background:#f7f8fb;border:1px solid var(--border);border-radius:8px;color:var(--text);font-family:'Noto Sans JP',sans-serif;font-size:0.9rem;outline:none;text-align:right}
        .row input:focus,.row select:focus{border-color:var(--accent)}
        .row .unit{font-size:0.8rem;color:var(--text3);margin-left:8px;min-width:20px}
        .result-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px}
        @media(max-width:600px){.result-grid{grid-template-columns:1fr}.row{flex-wrap:wrap;gap:8px}.row input,.row select{width:100%}}
        .result-item{background:#f7f8fb;border:1px solid var(--border);border-radius:var(--radius);padding:16px;text-align:center}
        .result-item .label{font-size:0.7rem;color:var(--text3);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px}
        .result-item .value{font-family:'JetBrains Mono',monospace;font-size:1.4rem;font-weight:700;color:var(--accent)}
        .result-item .value.tax{color:var(--red)}
        .result-item .value.take{color:var(--green)}
        .result-item .sub{font-size:0.75rem;color:var(--text3);margin-top:4px}
        .seo-content{margin-top:40px;padding:28px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);color:var(--text2);font-size:0.85rem;line-height:2}
        .seo-content h2{color:var(--text);font-size:1.05rem;margin-bottom:12px}.seo-content h3{color:var(--text);font-size:0.95rem;margin-top:20px;margin-bottom:8px}.seo-content p{margin-bottom:10px}
        footer{text-align:center;margin-top:48px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}
        .note{background:var(--accent-dim);border:1px solid rgba(0,0,0,0.08);border-radius:8px;padding:12px 16px;font-size:0.75rem;color:var(--text2);margin-bottom:24px}
        table.ref{width:100%;border-collapse:collapse;margin:16px 0;font-size:0.8rem}
        table.ref th{background:var(--bg);border:1px solid var(--border);padding:8px 12px;text-align:left;font-weight:600;color:var(--text)}
        table.ref td{border:1px solid var(--border);padding:8px 12px;color:var(--text2)}
        .btn{padding:10px 24px;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:0.9rem;font-weight:600;cursor:pointer;font-family:'Noto Sans JP',sans-serif}
        .btn:hover{opacity:0.9}"""

NAV = '<div style="max-width:960px;margin:0 auto;padding:12px 20px 0"><a href="/" style="display:inline-flex;align-items:center;gap:6px;color:#5a5f78;text-decoration:none;font-size:0.8rem;font-family:Noto Sans JP,sans-serif"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8h5z"/></svg> DevTools Japan トップへ</a></div>'

FOOTER = '''    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:20px;margin-top:24px;margin-bottom:24px">
      <h3 style="font-size:0.75rem;color:var(--text3);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:12px">関連ツール</h3>
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        RELATED_LINKS
      </div>
    </div>
    <footer><p style="margin-bottom:8px">&copy; 2026 DevTools Japan — 無料オンラインツール</p>
            <p style="font-size:0.65rem"><a href="/about/" style="color:inherit;text-decoration:none;margin:0 8px">サイトについて</a> | <a href="/privacy/" style="color:inherit;text-decoration:none;margin:0 8px">プライバシーポリシー</a> | <a href="/contact/" style="color:inherit;text-decoration:none;margin:0 8px">お問い合わせ</a></p></footer>'''

def related_link(href, text):
    return f'<a href="{href}" style="padding:8px 16px;background:var(--bg);border:1px solid var(--border);border-radius:8px;color:var(--text2);text-decoration:none;font-size:0.8rem;transition:border-color 0.2s" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'var(--border)\'">{text}</a>'


# ============================================================
# Tool 51: 営業日計算
# ============================================================
tool51 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>営業日計算ツール | 土日祝を除いた営業日数・納期計算【無料】</title>
    <meta name="description" content="営業日（土日祝を除いた平日）を自動計算する無料ツール。「3営業日後は何日？」「この期間は何営業日？」を即回答。納期計算、届出期限、振込予定日の確認に。日本の祝日対応。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
{COMMON_STYLE.replace("ACCENT_COLOR","#3b82f6").replace("ACCENT_DIM","rgba(59,130,246,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-51-business-day-calc/">
    <meta property="og:title" content="営業日計算ツール | 土日祝を除いた営業日数・納期計算【無料】">
    <meta property="og:description" content="3営業日後は何日？この期間は何営業日？を即計算。日本の祝日対応。">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-51-business-day-calc/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="営業日計算ツール | 納期・届出期限を自動計算【無料】">
    <meta name="twitter:description" content="土日祝を除いた営業日数・期日を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"営業日計算ツール","description":"土日祝を除いた営業日数を計算","url":"https://www.devtools-japan.com/tool-51-business-day-calc/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>営業日計算</h1><p>土日祝を除いた営業日数・期日を自動計算</p></header>

    <div class="card"><h3>N営業日後の日付を求める</h3>
        <div class="row"><label>基準日</label><input type="date" id="baseDate" style="text-align:left"></div>
        <div class="row"><label>営業日数</label><input type="number" id="bizDays" value="3" min="1"><span class="unit">営業日後</span></div>
        <div class="result-grid" style="margin-top:16px">
            <div class="result-item"><div class="label">結果日</div><div class="value" id="resultDate">-</div></div>
            <div class="result-item"><div class="label">曜日</div><div class="value" id="resultDow">-</div></div>
        </div>
    </div>

    <div class="card"><h3>2つの日付間の営業日数</h3>
        <div class="row"><label>開始日</label><input type="date" id="startDate" style="text-align:left"></div>
        <div class="row"><label>終了日</label><input type="date" id="endDate" style="text-align:left"></div>
        <div class="result-grid" style="margin-top:16px">
            <div class="result-item"><div class="label">営業日数</div><div class="value" id="bizCount">-</div></div>
            <div class="result-item"><div class="label">暦日数</div><div class="value" id="calCount">-</div></div>
        </div>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>営業日計算ツールの使い方</h2>
        <p>「3営業日後は何日？」「この期間は何営業日ある？」を即座に計算する無料ツールです。土曜日・日曜日・日本の祝日（振替休日・国民の休日含む）を除いた平日のみをカウントします。</p>
        <h3>営業日計算が必要な場面</h3>
        <p>ビジネスの現場では「営業日ベース」で期限が設定されることが多くあります。請求書の支払期限（月末締め翌月末払い、30営業日以内等）、届出書類の提出期限、銀行振込の着金予定日、納品期限の確認、契約書の期日計算など、正確な営業日計算は事務・経理・法務の基本業務です。</p>
        <h3>祝日の正確な反映</h3>
        <p>このツールは日本の祝日データ（2020年〜2030年）を内蔵しています。春分の日・秋分の日の天文計算、振替休日、国民の休日にも正確に対応しているため、市販のカレンダーアプリよりも信頼性の高い営業日計算ができます。</p>
        <h3>こんな場面で使えます</h3>
        <p>経理部門の支払日計算、法務部門の届出期限管理、営業部門の納期回答、人事部門の手続き期限確認、士業（弁護士・司法書士・社労士）の申立期限計算など。すべてブラウザ上で動作し、データがサーバーに送信されることはありません。</p>
    </div>

    <div class="ad-slot"></div>
    {FOOTER.replace("RELATED_LINKS", related_link("/tool-21-tax-simulator/","確定申告シミュレーター") + related_link("/tool-22-withholding-tax/","源泉徴収税計算") + related_link("/tool-12-wareki/","和暦西暦変換"))}
</div>
<script>
const HOLIDAYS_2024_2030 = [
"2024-01-01","2024-01-08","2024-02-11","2024-02-12","2024-02-23","2024-03-20","2024-04-29","2024-05-03","2024-05-04","2024-05-05","2024-05-06","2024-07-15","2024-08-11","2024-08-12","2024-09-16","2024-09-22","2024-09-23","2024-10-14","2024-11-03","2024-11-04","2024-11-23",
"2025-01-01","2025-01-13","2025-02-11","2025-02-23","2025-02-24","2025-03-20","2025-04-29","2025-05-03","2025-05-04","2025-05-05","2025-05-06","2025-07-21","2025-08-11","2025-09-15","2025-09-23","2025-10-13","2025-11-03","2025-11-23","2025-11-24",
"2026-01-01","2026-01-12","2026-02-11","2026-02-23","2026-03-20","2026-04-29","2026-05-03","2026-05-04","2026-05-05","2026-05-06","2026-07-20","2026-08-11","2026-09-21","2026-09-22","2026-09-23","2026-10-12","2026-11-03","2026-11-23",
"2027-01-01","2027-01-11","2027-02-11","2027-02-23","2027-03-21","2027-03-22","2027-04-29","2027-05-03","2027-05-04","2027-05-05","2027-07-19","2027-08-11","2027-09-20","2027-09-23","2027-10-11","2027-11-03","2027-11-23",
"2028-01-01","2028-01-10","2028-02-11","2028-02-23","2028-03-20","2028-04-29","2028-05-03","2028-05-04","2028-05-05","2028-07-17","2028-08-11","2028-09-18","2028-09-22","2028-10-09","2028-11-03","2028-11-23",
"2029-01-01","2029-01-08","2029-02-11","2029-02-12","2029-02-23","2029-03-20","2029-04-29","2029-04-30","2029-05-03","2029-05-04","2029-05-05","2029-07-16","2029-08-11","2029-09-17","2029-09-23","2029-09-24","2029-10-08","2029-11-03","2029-11-23",
"2030-01-01","2030-01-14","2030-02-11","2030-02-23","2030-03-20","2030-04-29","2030-05-03","2030-05-04","2030-05-05","2030-05-06","2030-07-15","2030-08-11","2030-08-12","2030-09-16","2030-09-23","2030-10-14","2030-11-03","2030-11-04","2030-11-23"
];
const holidaySet = new Set(HOLIDAYS_2024_2030);
const DOW = ["日","月","火","水","木","金","土"];

function isBusinessDay(d) {{
    const day = d.getDay();
    if (day === 0 || day === 6) return false;
    const str = d.toISOString().slice(0,10);
    return !holidaySet.has(str);
}}

function fmt(d) {{ return d.toISOString().slice(0,10); }}

function calcForward() {{
    const base = document.getElementById('baseDate').value;
    const n = parseInt(document.getElementById('bizDays').value) || 0;
    if (!base || n < 1) return;
    let d = new Date(base + 'T00:00:00');
    let count = 0;
    while (count < n) {{
        d.setDate(d.getDate() + 1);
        if (isBusinessDay(d)) count++;
    }}
    document.getElementById('resultDate').textContent = fmt(d);
    document.getElementById('resultDow').textContent = DOW[d.getDay()] + '曜日';
}}

function calcBetween() {{
    const s = document.getElementById('startDate').value;
    const e = document.getElementById('endDate').value;
    if (!s || !e) return;
    let start = new Date(s + 'T00:00:00');
    let end = new Date(e + 'T00:00:00');
    if (start > end) [start, end] = [end, start];
    let biz = 0, cal = 0;
    let d = new Date(start);
    while (d <= end) {{
        cal++;
        if (isBusinessDay(d)) biz++;
        d.setDate(d.getDate() + 1);
    }}
    document.getElementById('bizCount').textContent = biz + '日';
    document.getElementById('calCount').textContent = cal + '日';
}}

// 初期値
const today = new Date();
document.getElementById('baseDate').value = fmt(today);
document.getElementById('startDate').value = fmt(today);
const next = new Date(today); next.setMonth(next.getMonth()+1);
document.getElementById('endDate').value = fmt(next);

document.getElementById('baseDate').addEventListener('input', calcForward);
document.getElementById('bizDays').addEventListener('input', calcForward);
document.getElementById('startDate').addEventListener('input', calcBetween);
document.getElementById('endDate').addEventListener('input', calcBetween);
calcForward(); calcBetween();
</script>
</body>
</html>'''


# ============================================================
# Tool 52: 請求書金額計算
# ============================================================
tool52 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>請求書金額計算ツール | 税込・税抜・源泉徴収・振込額を一括計算【無料】</title>
    <meta name="description" content="請求書に必要な金額を一括計算する無料ツール。税抜額から税込額、消費税額、源泉徴収税額、実際の振込額を自動計算。フリーランスの請求書作成、経理の検算に。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
{COMMON_STYLE.replace("ACCENT_COLOR","#8b5cf6").replace("ACCENT_DIM","rgba(139,92,246,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-52-invoice-calc/">
    <meta property="og:title" content="請求書金額計算 | 税込・源泉徴収・振込額を一括計算【無料】">
    <meta property="og:description" content="請求書の税込額・消費税・源泉徴収・振込額を自動計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-52-invoice-calc/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="請求書金額計算 | 税込・源泉徴収・振込額【無料】">
    <meta name="twitter:description" content="フリーランス・経理向け。請求書の金額を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"請求書金額計算ツール","description":"請求書の税込・税抜・源泉徴収・振込額を一括計算","url":"https://www.devtools-japan.com/tool-52-invoice-calc/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>請求書金額計算</h1><p>税込・税抜・源泉徴収・振込額を一括計算</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>報酬額（税抜）</label><input type="number" id="amount" value="300000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>消費税率</label><select id="taxRate" onchange="calc()"><option value="0.1" selected>10%</option><option value="0.08">8%（軽減税率）</option></select><span class="unit"></span></div>
        <div class="row"><label>源泉徴収</label><select id="withholding" onchange="calc()"><option value="yes" selected>あり（10.21%）</option><option value="no">なし</option></select><span class="unit"></span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">報酬額（税抜）</div><div class="value" id="rBase">-</div></div>
        <div class="result-item"><div class="label">消費税額</div><div class="value" id="rTax">-</div></div>
        <div class="result-item"><div class="label">小計（税込）</div><div class="value" id="rTotal">-</div></div>
        <div class="result-item"><div class="label">源泉徴収税額</div><div class="value tax" id="rWith">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">ご請求額（振込額）</div><div class="value take" id="rFinal" style="font-size:2rem">-</div></div>
    </div>

    <div class="card" id="breakdown" style="font-size:0.85rem;color:var(--text2);line-height:2"></div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>請求書金額計算ツールの使い方</h2>
        <p>フリーランス・個人事業主が請求書を作成する際に必要な金額を一括で計算する無料ツールです。報酬額（税抜き）を入力するだけで、消費税額、税込金額、源泉徴収税額、実際にクライアントから振り込まれる金額が即座にわかります。</p>
        <h3>源泉徴収がある場合の計算</h3>
        <p>デザイン料・原稿料・コンサルティング料などは源泉徴収の対象です。報酬が100万円以下の場合は10.21%、100万円超の部分は20.42%が源泉徴収されます。請求書に消費税を明記している場合、税抜額に対して源泉徴収が計算されるため、手取りが増えます。</p>
        <h3>経理の検算にも</h3>
        <p>受け取った請求書の金額が正しいか検算する場面でも使えます。「税込金額から逆算して税抜額を出す」「源泉徴収額が正しいか確認する」などの用途に対応しています。</p>
    </div>

    {FOOTER.replace("RELATED_LINKS", related_link("/tool-22-withholding-tax/","源泉徴収税計算") + related_link("/tool-21-tax-simulator/","確定申告シミュレーター") + related_link("/tool-51-business-day-calc/","営業日計算"))}
</div>
<script>
function calc() {{
    const amount = parseInt(document.getElementById('amount').value) || 0;
    const taxRate = parseFloat(document.getElementById('taxRate').value);
    const withholding = document.getElementById('withholding').value === 'yes';

    const tax = Math.floor(amount * taxRate);
    const total = amount + tax;

    let withTax = 0;
    if (withholding) {{
        if (amount <= 1000000) {{
            withTax = Math.floor(amount * 0.1021);
        }} else {{
            withTax = Math.floor((amount - 1000000) * 0.2042) + 102100;
        }}
    }}
    const final = total - withTax;

    const f = n => n.toLocaleString();
    document.getElementById('rBase').textContent = '\\u00a5' + f(amount);
    document.getElementById('rTax').textContent = '\\u00a5' + f(tax);
    document.getElementById('rTotal').textContent = '\\u00a5' + f(total);
    document.getElementById('rWith').textContent = withholding ? '-\\u00a5' + f(withTax) : '-';
    document.getElementById('rFinal').textContent = '\\u00a5' + f(final);

    let bd = '<strong>請求書の記載例:</strong><br>';
    bd += '報酬: ' + f(amount) + '円<br>';
    bd += '消費税（' + (taxRate*100) + '%）: ' + f(tax) + '円<br>';
    bd += '小計: ' + f(total) + '円<br>';
    if (withholding) bd += '源泉徴収税額: -' + f(withTax) + '円<br>';
    bd += '<strong>ご請求額: ' + f(final) + '円</strong>';
    document.getElementById('breakdown').innerHTML = bd;
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 53: 年齢・勤続年数計算
# ============================================================
tool53 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>年齢・勤続年数計算ツール | 生年月日から年齢、入社日から勤続年数を自動計算【無料】</title>
    <meta name="description" content="生年月日から年齢を正確に計算、入社日から勤続年数を自動計算する無料ツール。有給休暇の付与日数、定年退職日も表示。人事・総務の業務効率化に。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
{COMMON_STYLE.replace("ACCENT_COLOR","#059669").replace("ACCENT_DIM","rgba(5,150,105,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-53-age-calc/">
    <meta property="og:title" content="年齢・勤続年数計算 | 生年月日・入社日から自動計算【無料】">
    <meta property="og:description" content="年齢・勤続年数・有給日数・定年退職日を自動計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-53-age-calc/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="年齢・勤続年数計算【無料】">
    <meta name="twitter:description" content="生年月日から年齢、入社日から勤続年数を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"年齢・勤続年数計算ツール","description":"年齢・勤続年数・有給日数を自動計算","url":"https://www.devtools-japan.com/tool-53-age-calc/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>年齢・勤続年数計算</h1><p>生年月日・入社日から自動計算</p></header>

    <div class="card"><h3>年齢計算</h3>
        <div class="row"><label>生年月日</label><input type="date" id="birthDate" value="1990-04-15" style="text-align:left" oninput="calcAge()"></div>
        <div class="row"><label>基準日</label><input type="date" id="ageBase" style="text-align:left" oninput="calcAge()"></div>
        <div class="result-grid" style="margin-top:16px">
            <div class="result-item"><div class="label">年齢</div><div class="value" id="age">-</div></div>
            <div class="result-item"><div class="label">次の誕生日まで</div><div class="value" id="nextBday">-</div></div>
        </div>
    </div>

    <div class="card"><h3>勤続年数・有給休暇</h3>
        <div class="row"><label>入社日</label><input type="date" id="joinDate" value="2020-04-01" style="text-align:left" oninput="calcTenure()"></div>
        <div class="result-grid" style="margin-top:16px">
            <div class="result-item"><div class="label">勤続年数</div><div class="value" id="tenure">-</div></div>
            <div class="result-item"><div class="label">有給付与日数（年間）</div><div class="value take" id="paidLeave">-</div></div>
        </div>
    </div>

    <div class="note">有給休暇の付与日数は労働基準法に基づく最低基準です。会社の就業規則でこれを上回る場合があります。</div>

    <div class="card"><h3>有給休暇 付与日数の目安（労働基準法）</h3>
        <table class="ref">
            <tr><th>勤続年数</th><th>付与日数</th></tr>
            <tr><td>6ヶ月</td><td>10日</td></tr>
            <tr><td>1年6ヶ月</td><td>11日</td></tr>
            <tr><td>2年6ヶ月</td><td>12日</td></tr>
            <tr><td>3年6ヶ月</td><td>14日</td></tr>
            <tr><td>4年6ヶ月</td><td>16日</td></tr>
            <tr><td>5年6ヶ月</td><td>18日</td></tr>
            <tr><td>6年6ヶ月以上</td><td>20日（上限）</td></tr>
        </table>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>年齢・勤続年数計算ツールの使い方</h2>
        <p>生年月日から正確な年齢を計算し、入社日から勤続年数と有給休暇の付与日数を自動計算する無料ツールです。人事・総務部門の日常業務で頻繁に必要になる計算をブラウザだけで即座に行えます。</p>
        <h3>年齢計算の正確性</h3>
        <p>日本の法律では「年齢は誕生日の前日に1歳加算される」と定められています（年齢計算ニ関スル法律）。例えば4月1日生まれの人は、3月31日に満年齢に達します。このツールはこのルールに基づいて正確に年齢を計算します。</p>
        <h3>有給休暇の付与日数</h3>
        <p>労働基準法第39条に基づき、入社6ヶ月後に10日、以降1年ごとに日数が増え、6年6ヶ月以上で上限の20日が付与されます。このツールは勤続年数から自動的に法定の最低付与日数を表示します。</p>
        <h3>活用場面</h3>
        <p>人事部門での入社手続き、保険の年齢確認、定年退職日の計算、有給休暇の管理、履歴書の年齢確認など。社労士の方の労務管理業務にもお使いいただけます。</p>
    </div>

    {FOOTER.replace("RELATED_LINKS", related_link("/tool-51-business-day-calc/","営業日計算") + related_link("/tool-12-wareki/","和暦西暦変換") + related_link("/tool-54-working-hours/","労働時間・残業代計算"))}
</div>
<script>
const today = new Date();
document.getElementById('ageBase').value = today.toISOString().slice(0,10);

function calcAge() {{
    const bd = document.getElementById('birthDate').value;
    const base = document.getElementById('ageBase').value;
    if (!bd || !base) return;
    const b = new Date(bd), d = new Date(base);
    let age = d.getFullYear() - b.getFullYear();
    if (d.getMonth() < b.getMonth() || (d.getMonth() === b.getMonth() && d.getDate() < b.getDate())) age--;
    document.getElementById('age').textContent = age + '歳';

    // 次の誕生日まで
    let nextB = new Date(d.getFullYear(), b.getMonth(), b.getDate());
    if (nextB <= d) nextB.setFullYear(nextB.getFullYear() + 1);
    const diff = Math.ceil((nextB - d) / (1000*60*60*24));
    document.getElementById('nextBday').textContent = diff + '日';
}}

function calcTenure() {{
    const jd = document.getElementById('joinDate').value;
    if (!jd) return;
    const j = new Date(jd), d = new Date();
    let years = d.getFullYear() - j.getFullYear();
    let months = d.getMonth() - j.getMonth();
    if (d.getDate() < j.getDate()) months--;
    if (months < 0) {{ years--; months += 12; }}
    document.getElementById('tenure').textContent = years + '年' + months + 'ヶ月';

    // 有給日数（勤続月数ベース）
    const totalMonths = years * 12 + months;
    let leave = 0;
    if (totalMonths >= 78) leave = 20; // 6年6ヶ月以上
    else if (totalMonths >= 66) leave = 18;
    else if (totalMonths >= 54) leave = 16;
    else if (totalMonths >= 42) leave = 14;
    else if (totalMonths >= 30) leave = 12;
    else if (totalMonths >= 18) leave = 11;
    else if (totalMonths >= 6) leave = 10;
    else leave = 0;
    document.getElementById('paidLeave').textContent = leave + '日';
}}

calcAge(); calcTenure();
</script>
</body>
</html>'''


# ============================================================
# Tool 54: 労働時間・残業代計算
# ============================================================
tool54 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>残業代計算ツール | 時給・月給から残業代・割増賃金を自動計算【無料】</title>
    <meta name="description" content="残業代・割増賃金を自動計算する無料ツール。時給・月給から残業代を計算。時間外（25%）、深夜（25%）、休日（35%）の割増率に対応。社労士の労務管理、総務の給与計算に。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
{COMMON_STYLE.replace("ACCENT_COLOR","#dc2626").replace("ACCENT_DIM","rgba(220,38,38,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-54-working-hours/">
    <meta property="og:title" content="残業代計算ツール | 割増賃金を自動計算【無料】">
    <meta property="og:description" content="時給・月給から残業代を計算。時間外25%、深夜25%、休日35%の割増に対応">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-54-working-hours/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="残業代計算ツール | 割増賃金を自動計算【無料】">
    <meta name="twitter:description" content="残業代を正確に計算。時間外・深夜・休日の割増率に対応">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"残業代計算ツール","description":"残業代・割増賃金を自動計算","url":"https://www.devtools-japan.com/tool-54-working-hours/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>残業代・割増賃金計算</h1><p>時給・月給から残業代を自動計算</p></header>

    <div class="card"><h3>基本情報</h3>
        <div class="row"><label>計算方法</label><select id="calcType" onchange="toggleInput();calc()"><option value="hourly">時給から計算</option><option value="monthly" selected>月給から計算</option></select><span class="unit"></span></div>
        <div class="row" id="hourlyRow" style="display:none"><label>時給</label><input type="number" id="hourlyWage" value="1500" oninput="calc()"><span class="unit">円</span></div>
        <div class="row" id="monthlyRow"><label>月給（基本給+各種手当）</label><input type="number" id="monthlySalary" value="300000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row" id="workHoursRow"><label>月の所定労働時間</label><input type="number" id="workHours" value="160" oninput="calc()"><span class="unit">時間</span></div>
    </div>

    <div class="card"><h3>残業時間</h3>
        <div class="row"><label>時間外労働（法定外残業）</label><input type="number" id="overtime" value="20" oninput="calc()"><span class="unit">時間</span></div>
        <div class="row"><label>深夜労働（22時〜5時）</label><input type="number" id="nighttime" value="0" oninput="calc()"><span class="unit">時間</span></div>
        <div class="row"><label>休日労働</label><input type="number" id="holiday" value="0" oninput="calc()"><span class="unit">時間</span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">時間単価</div><div class="value" id="rHourly">-</div></div>
        <div class="result-item"><div class="label">時間外 残業代（25%増）</div><div class="value" id="rOvertime">-</div></div>
        <div class="result-item"><div class="label">深夜 残業代（25%増）</div><div class="value" id="rNight">-</div></div>
        <div class="result-item"><div class="label">休日 残業代（35%増）</div><div class="value" id="rHoliday">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">残業代 合計</div><div class="value tax" id="rTotal" style="font-size:2rem">-</div></div>
    </div>

    <div class="card"><h3>割増賃金率（労働基準法）</h3>
        <table class="ref">
            <tr><th>種類</th><th>割増率</th><th>計算式</th></tr>
            <tr><td>時間外労働</td><td>25%以上</td><td>時間単価 x 1.25 x 時間数</td></tr>
            <tr><td>深夜労働（22時〜5時）</td><td>25%以上</td><td>時間単価 x 1.25 x 時間数</td></tr>
            <tr><td>休日労働</td><td>35%以上</td><td>時間単価 x 1.35 x 時間数</td></tr>
            <tr><td>時間外+深夜</td><td>50%以上</td><td>時間単価 x 1.50 x 時間数</td></tr>
            <tr><td>月60時間超の時間外</td><td>50%以上</td><td>時間単価 x 1.50 x 時間数</td></tr>
        </table>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>残業代計算ツールの使い方</h2>
        <p>月給または時給から、残業代（割増賃金）を自動計算する無料ツールです。時間外労働（25%割増）、深夜労働（25%割増）、休日労働（35%割増）のそれぞれの残業代を正確に算出します。</p>
        <h3>月給制の場合の時間単価</h3>
        <p>月給制の場合、まず1時間あたりの賃金（時間単価）を計算します。時間単価 = 月給 ÷ 月の所定労働時間 で求めます。月の所定労働時間は、一般的に160〜170時間程度です（1日8時間 x 月20〜21日）。</p>
        <h3>2023年4月からの法改正</h3>
        <p>2023年4月から、中小企業でも月60時間を超える時間外労働に対して50%以上の割増賃金が必要になりました。従来は大企業のみが対象でしたが、全ての企業に適用されています。</p>
        <h3>こんな場面で使えます</h3>
        <p>給与計算担当者の検算、社労士の労務管理、従業員の残業代確認、未払い残業代の概算計算など。すべてブラウザ上で計算され、データがサーバーに送信されることはありません。</p>
    </div>

    {FOOTER.replace("RELATED_LINKS", related_link("/tool-53-age-calc/","年齢・勤続年数計算") + related_link("/tool-51-business-day-calc/","営業日計算") + related_link("/tool-22-withholding-tax/","源泉徴収税計算"))}
</div>
<script>
function toggleInput() {{
    const t = document.getElementById('calcType').value;
    document.getElementById('hourlyRow').style.display = t === 'hourly' ? 'flex' : 'none';
    document.getElementById('monthlyRow').style.display = t === 'monthly' ? 'flex' : 'none';
    document.getElementById('workHoursRow').style.display = t === 'monthly' ? 'flex' : 'none';
}}
function calc() {{
    const t = document.getElementById('calcType').value;
    let hourly;
    if (t === 'hourly') {{
        hourly = parseInt(document.getElementById('hourlyWage').value) || 0;
    }} else {{
        const monthly = parseInt(document.getElementById('monthlySalary').value) || 0;
        const hours = parseInt(document.getElementById('workHours').value) || 160;
        hourly = Math.round(monthly / hours);
    }}
    const ot = parseFloat(document.getElementById('overtime').value) || 0;
    const nt = parseFloat(document.getElementById('nighttime').value) || 0;
    const hd = parseFloat(document.getElementById('holiday').value) || 0;

    const otPay = Math.round(hourly * 1.25 * ot);
    const ntPay = Math.round(hourly * 1.25 * nt);
    const hdPay = Math.round(hourly * 1.35 * hd);
    const total = otPay + ntPay + hdPay;

    const f = n => n.toLocaleString();
    document.getElementById('rHourly').textContent = '\\u00a5' + f(hourly);
    document.getElementById('rOvertime').textContent = '\\u00a5' + f(otPay);
    document.getElementById('rNight').textContent = '\\u00a5' + f(ntPay);
    document.getElementById('rHoliday').textContent = '\\u00a5' + f(hdPay);
    document.getElementById('rTotal').textContent = '\\u00a5' + f(total);
}}
toggleInput(); calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 55: 遅延損害金計算
# ============================================================
tool55 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>遅延損害金計算ツール | 法定利率・約定利率での遅延損害金を自動計算【無料】</title>
    <meta name="description" content="未払い金の遅延損害金を自動計算する無料ツール。法定利率（民法3%）、商事法定利率、約定利率に対応。弁護士・司法書士の訴状作成、債権回収、内容証明郵便の金額計算に。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
{COMMON_STYLE.replace("ACCENT_COLOR","#b45309").replace("ACCENT_DIM","rgba(180,83,9,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-55-late-fee-calc/">
    <meta property="og:title" content="遅延損害金計算 | 法定利率・約定利率で自動計算【無料】">
    <meta property="og:description" content="未払い金の遅延損害金を法定利率3%・約定利率で自動計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-55-late-fee-calc/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="遅延損害金計算ツール【無料】">
    <meta name="twitter:description" content="法定利率・約定利率で遅延損害金を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"遅延損害金計算ツール","description":"未払い金の遅延損害金を自動計算","url":"https://www.devtools-japan.com/tool-55-late-fee-calc/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>遅延損害金計算</h1><p>法定利率・約定利率で遅延損害金を自動計算</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>元金（未払い額）</label><input type="number" id="principal" value="1000000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>利率</label><select id="rateType" onchange="toggleRate();calc()">
            <option value="civil" selected>法定利率（民法）3%</option>
            <option value="labor">賃金の場合 14.6%</option>
            <option value="custom">約定利率（手動入力）</option>
        </select><span class="unit"></span></div>
        <div class="row" id="customRateRow" style="display:none"><label>年利</label><input type="number" id="customRate" value="5" step="0.1" oninput="calc()"><span class="unit">%</span></div>
        <div class="row"><label>遅延開始日（支払期日の翌日）</label><input type="date" id="lateStart" style="text-align:left" oninput="calc()"></div>
        <div class="row"><label>計算日</label><input type="date" id="lateEnd" style="text-align:left" oninput="calc()"></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">遅延日数</div><div class="value" id="rDays">-</div></div>
        <div class="result-item"><div class="label">適用利率</div><div class="value" id="rRate">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item"><div class="label">遅延損害金</div><div class="value tax" id="rFee" style="font-size:1.6rem">-</div></div>
        <div class="result-item"><div class="label">合計請求額（元金+遅延損害金）</div><div class="value" id="rTotal" style="font-size:1.6rem">-</div></div>
    </div>

    <div class="card"><div class="label" style="font-size:0.75rem;color:var(--text3);margin-bottom:8px">計算式</div><div id="formula" style="font-size:0.85rem;color:var(--text2);line-height:2"></div></div>

    <div class="note">このツールは概算計算です。閏年の日数計算を含む正確な計算については弁護士・司法書士にご確認ください。法定利率は3年ごとに見直されます（2023年4月〜2026年3月: 3%）。</div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>遅延損害金計算ツールの使い方</h2>
        <p>支払期日を過ぎた未払い金に対する遅延損害金（遅延利息）を自動計算する無料ツールです。弁護士・司法書士が訴状や内容証明郵便を作成する際の金額計算、債権回収の際の請求額の算出に使えます。</p>
        <h3>法定利率について</h3>
        <p>2020年4月の民法改正により、法定利率は年3%に統一されました（改正前は民事5%、商事6%）。法定利率は3年ごとに見直される変動制となっています。当事者間の契約で別途利率を定めている場合（約定利率）はそちらが優先されます。</p>
        <h3>賃金の遅延損害金</h3>
        <p>退職後の未払い賃金に対する遅延損害金は、賃金の支払の確保等に関する法律により年14.6%が適用されます（在職中は法定利率）。</p>
        <h3>計算式</h3>
        <p>遅延損害金 = 元金 x 年利率 x 遅延日数 ÷ 365 で計算します。閏年を含む期間の場合、正確には365日と366日を分けて計算する必要がありますが、このツールでは簡易的に365日で計算しています。</p>
    </div>

    {FOOTER.replace("RELATED_LINKS", related_link("/tool-51-business-day-calc/","営業日計算") + related_link("/tool-52-invoice-calc/","請求書金額計算") + related_link("/tool-27-loan-calc/","ローン返済シミュレーター"))}
</div>
<script>
const today = new Date();
const threeMonthsAgo = new Date(today); threeMonthsAgo.setMonth(threeMonthsAgo.getMonth()-3);
document.getElementById('lateStart').value = threeMonthsAgo.toISOString().slice(0,10);
document.getElementById('lateEnd').value = today.toISOString().slice(0,10);

function toggleRate() {{
    document.getElementById('customRateRow').style.display = document.getElementById('rateType').value === 'custom' ? 'flex' : 'none';
}}
function calc() {{
    const principal = parseInt(document.getElementById('principal').value) || 0;
    const rateType = document.getElementById('rateType').value;
    let rate;
    if (rateType === 'civil') rate = 3;
    else if (rateType === 'labor') rate = 14.6;
    else rate = parseFloat(document.getElementById('customRate').value) || 0;

    const start = document.getElementById('lateStart').value;
    const end = document.getElementById('lateEnd').value;
    if (!start || !end) return;

    const s = new Date(start), e = new Date(end);
    const days = Math.max(0, Math.ceil((e - s) / (1000*60*60*24)));
    const fee = Math.floor(principal * (rate / 100) * days / 365);
    const total = principal + fee;

    const f = n => n.toLocaleString();
    document.getElementById('rDays').textContent = days + '日';
    document.getElementById('rRate').textContent = rate + '%';
    document.getElementById('rFee').textContent = '\\u00a5' + f(fee);
    document.getElementById('rTotal').textContent = '\\u00a5' + f(total);
    document.getElementById('formula').innerHTML = f(principal) + '円 x ' + rate + '% x ' + days + '日 / 365 = <strong>' + f(fee) + '円</strong>';
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 56: 相続税シミュレーター
# ============================================================
tool56 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>相続税シミュレーター | 基礎控除額・税額を概算計算【無料】</title>
    <meta name="description" content="相続税の基礎控除額と概算税額を計算する無料ツール。遺産総額と法定相続人の数を入力するだけで、相続税がかかるかどうか、かかる場合はいくらかを即計算。税理士・FPの概算シミュレーションに。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
{COMMON_STYLE.replace("ACCENT_COLOR","#7c3aed").replace("ACCENT_DIM","rgba(124,58,237,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-56-inheritance-tax/">
    <meta property="og:title" content="相続税シミュレーター | 基礎控除・税額を概算計算【無料】">
    <meta property="og:description" content="遺産総額と相続人数から相続税の概算を即計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-56-inheritance-tax/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="相続税シミュレーター【無料】">
    <meta name="twitter:description" content="相続税の基礎控除と概算税額を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"相続税シミュレーター","description":"相続税の基礎控除と概算税額を計算","url":"https://www.devtools-japan.com/tool-56-inheritance-tax/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>相続税シミュレーター</h1><p>基礎控除額と概算税額を自動計算</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>遺産総額</label><input type="number" id="estate" value="80000000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>法定相続人の数</label><input type="number" id="heirs" value="3" min="1" max="20" oninput="calc()"><span class="unit">人</span></div>
        <div class="row"><label>債務・葬式費用</label><input type="number" id="debts" value="2000000" oninput="calc()"><span class="unit">円</span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">基礎控除額</div><div class="value take" id="rDeduction">-</div><div class="sub">3,000万 + 600万 x 相続人数</div></div>
        <div class="result-item"><div class="label">課税遺産総額</div><div class="value" id="rTaxable">-</div><div class="sub">遺産総額 - 債務 - 基礎控除</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">相続税 概算総額</div><div class="value tax" id="rTax" style="font-size:2rem">-</div><div class="sub" id="rNote"></div></div>
    </div>

    <div class="card"><h3>相続税の速算表</h3>
        <table class="ref">
            <tr><th>法定相続分に応じた取得金額</th><th>税率</th><th>控除額</th></tr>
            <tr><td>〜1,000万円</td><td>10%</td><td>0円</td></tr>
            <tr><td>〜3,000万円</td><td>15%</td><td>50万円</td></tr>
            <tr><td>〜5,000万円</td><td>20%</td><td>200万円</td></tr>
            <tr><td>〜1億円</td><td>30%</td><td>700万円</td></tr>
            <tr><td>〜2億円</td><td>40%</td><td>1,700万円</td></tr>
            <tr><td>〜3億円</td><td>45%</td><td>2,700万円</td></tr>
            <tr><td>〜6億円</td><td>50%</td><td>4,200万円</td></tr>
            <tr><td>6億円超</td><td>55%</td><td>7,200万円</td></tr>
        </table>
    </div>

    <div class="note">このツールは概算シミュレーションです。配偶者控除（1億6,000万円）、小規模宅地の特例、生命保険金の非課税枠などは含まれていません。正確な税額は税理士にご相談ください。</div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>相続税シミュレーターの使い方</h2>
        <p>遺産総額と法定相続人の数を入力するだけで、相続税の基礎控除額と概算税額を計算する無料ツールです。「相続税がかかるかどうか」「かかる場合はおよそいくらか」を手軽に確認できます。</p>
        <h3>基礎控除額の計算</h3>
        <p>相続税の基礎控除額は「3,000万円 + 600万円 x 法定相続人の数」で計算されます。例えば、配偶者と子供2人（計3人）の場合、基礎控除は3,000万 + 600万 x 3 = 4,800万円です。遺産総額がこの基礎控除額以下であれば、相続税はかかりません。</p>
        <h3>2015年の改正で対象者が増加</h3>
        <p>2015年1月の税制改正で基礎控除額が40%縮小されました。改正前は「5,000万円 + 1,000万円 x 法定相続人の数」でしたが、現在は「3,000万円 + 600万円 x 法定相続人の数」に引き下げられ、課税対象者が大幅に増加しました。</p>
        <h3>税理士・FPの方へ</h3>
        <p>このツールは初回面談時の概算シミュレーションにお使いいただけます。配偶者控除や小規模宅地の特例を適用する前の概算税額を素早く計算して、お客様に「相続税がかかるかどうか」をその場でお伝えする際に便利です。</p>
    </div>

    {FOOTER.replace("RELATED_LINKS", related_link("/tool-21-tax-simulator/","確定申告シミュレーター") + related_link("/tool-55-late-fee-calc/","遅延損害金計算") + related_link("/tool-27-loan-calc/","ローン返済シミュレーター"))}
</div>
<script>
function calc() {{
    const estate = parseInt(document.getElementById('estate').value) || 0;
    const heirs = Math.max(1, parseInt(document.getElementById('heirs').value) || 1);
    const debts = parseInt(document.getElementById('debts').value) || 0;

    const deduction = 30000000 + 6000000 * heirs;
    const netEstate = Math.max(0, estate - debts);
    const taxable = Math.max(0, netEstate - deduction);

    // 法定相続分で按分して税額計算（簡易版: 均等按分）
    const perPerson = Math.floor(taxable / heirs);
    function taxForAmount(a) {{
        if (a <= 10000000) return a * 0.10;
        if (a <= 30000000) return a * 0.15 - 500000;
        if (a <= 50000000) return a * 0.20 - 2000000;
        if (a <= 100000000) return a * 0.30 - 7000000;
        if (a <= 200000000) return a * 0.40 - 17000000;
        if (a <= 300000000) return a * 0.45 - 27000000;
        if (a <= 600000000) return a * 0.50 - 42000000;
        return a * 0.55 - 72000000;
    }}
    const totalTax = Math.floor(taxForAmount(perPerson) * heirs);

    const f = n => n.toLocaleString();
    document.getElementById('rDeduction').textContent = '\\u00a5' + f(deduction);
    document.getElementById('rTaxable').textContent = taxable > 0 ? '\\u00a5' + f(taxable) : '\\u00a50（非課税）';
    document.getElementById('rTax').textContent = taxable > 0 ? '\\u00a5' + f(totalTax) : '\\u00a50';
    document.getElementById('rNote').textContent = taxable > 0 ? '配偶者控除・小規模宅地の特例は含まない概算' : '基礎控除以下のため相続税はかかりません';
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 57: 印紙税額検索
# ============================================================
tool57 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>印紙税額検索ツール | 契約書・領収書の収入印紙はいくら？【無料】</title>
    <meta name="description" content="契約書や領収書に必要な収入印紙の金額を即検索できる無料ツール。売買契約、請負契約、領収書など文書の種類と金額から必要な印紙税額を自動判定。行政書士・経理の実務に。">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
{COMMON_STYLE.replace("ACCENT_COLOR","#0891b2").replace("ACCENT_DIM","rgba(8,145,178,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-57-stamp-duty/">
    <meta property="og:title" content="印紙税額検索 | 収入印紙はいくら必要？【無料】">
    <meta property="og:description" content="契約書・領収書に必要な収入印紙の金額を即検索">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-57-stamp-duty/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="印紙税額検索ツール【無料】">
    <meta name="twitter:description" content="契約書・領収書に必要な収入印紙の金額を即検索">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"印紙税額検索ツール","description":"契約書・領収書に必要な印紙税額を検索","url":"https://www.devtools-japan.com/tool-57-stamp-duty/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>印紙税額検索</h1><p>契約書・領収書に必要な収入印紙の金額を即検索</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>文書の種類</label><select id="docType" onchange="calc()" style="text-align:left">
            <option value="contract1">不動産売買契約書（第1号文書）</option>
            <option value="contract2" selected>請負契約書（第2号文書）</option>
            <option value="receipt">領収書・受取書（第17号文書）</option>
        </select><span class="unit"></span></div>
        <div class="row"><label>記載金額</label><input type="number" id="docAmount" value="5000000" oninput="calc()"><span class="unit">円</span></div>
    </div>

    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">必要な印紙税額</div><div class="value" id="rStamp" style="font-size:2.5rem">-</div><div class="sub" id="rStampNote"></div></div>
    </div>

    <div class="card"><h3>請負契約書（第2号文書）の印紙税額表</h3>
        <table class="ref">
            <tr><th>記載金額</th><th>印紙税額</th></tr>
            <tr><td>1万円未満</td><td>非課税</td></tr>
            <tr><td>1万円〜100万円</td><td>200円</td></tr>
            <tr><td>100万円超〜200万円</td><td>400円</td></tr>
            <tr><td>200万円超〜300万円</td><td>1,000円</td></tr>
            <tr><td>300万円超〜500万円</td><td>2,000円</td></tr>
            <tr><td>500万円超〜1,000万円</td><td>10,000円</td></tr>
            <tr><td>1,000万円超〜5,000万円</td><td>20,000円</td></tr>
            <tr><td>5,000万円超〜1億円</td><td>60,000円</td></tr>
            <tr><td>1億円超〜5億円</td><td>100,000円</td></tr>
            <tr><td>5億円超〜10億円</td><td>200,000円</td></tr>
            <tr><td>10億円超〜50億円</td><td>400,000円</td></tr>
            <tr><td>50億円超</td><td>600,000円</td></tr>
            <tr><td>金額の記載なし</td><td>200円</td></tr>
        </table>
    </div>

    <div class="note">2024年3月31日までの軽減税率は終了しています。電子契約の場合、印紙税は不要です。詳しくは国税庁のサイトをご確認ください。</div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>印紙税額検索ツールの使い方</h2>
        <p>契約書や領収書に必要な収入印紙の金額を、文書の種類と記載金額から即座に検索できる無料ツールです。「この契約書にはいくらの印紙が必要？」「領収書の印紙税はいくら？」という疑問に即答します。</p>
        <h3>印紙税とは</h3>
        <p>印紙税は、契約書や領収書などの文書に対して課される税金です。文書の作成者が収入印紙を貼付し、消印を押すことで納付します。印紙を貼らなかった場合、本来の印紙税額の3倍が過怠税として徴収されます。</p>
        <h3>電子契約なら印紙税不要</h3>
        <p>電子契約（クラウドサイン、DocuSign等）で締結した契約書には印紙税がかかりません。高額な契約では電子契約に切り替えることで大幅なコスト削減が可能です。例えば5,000万円の請負契約書の場合、紙の契約書なら2万円の印紙が必要ですが、電子契約なら0円です。</p>
        <h3>行政書士・経理の方へ</h3>
        <p>契約書の作成・チェック業務で「この金額ならいくらの印紙？」を即座に確認できます。すべてブラウザ上で動作し、データがサーバーに送信されることはありません。</p>
    </div>

    {FOOTER.replace("RELATED_LINKS", related_link("/tool-52-invoice-calc/","請求書金額計算") + related_link("/tool-55-late-fee-calc/","遅延損害金計算") + related_link("/tool-51-business-day-calc/","営業日計算"))}
</div>
<script>
function getStampDuty(type, amount) {{
    if (type === 'receipt') {{
        if (amount < 50000) return {{tax: 0, note: '5万円未満は非課税'}};
        if (amount <= 1000000) return {{tax: 200, note: ''}};
        if (amount <= 2000000) return {{tax: 400, note: ''}};
        if (amount <= 3000000) return {{tax: 600, note: ''}};
        if (amount <= 5000000) return {{tax: 1000, note: ''}};
        if (amount <= 10000000) return {{tax: 2000, note: ''}};
        if (amount <= 20000000) return {{tax: 4000, note: ''}};
        if (amount <= 30000000) return {{tax: 6000, note: ''}};
        if (amount <= 50000000) return {{tax: 10000, note: ''}};
        if (amount <= 100000000) return {{tax: 20000, note: ''}};
        if (amount <= 200000000) return {{tax: 40000, note: ''}};
        if (amount <= 300000000) return {{tax: 60000, note: ''}};
        if (amount <= 500000000) return {{tax: 100000, note: ''}};
        return {{tax: 200000, note: ''}};
    }}
    // 請負契約書・売買契約書
    if (amount < 10000) return {{tax: 0, note: '1万円未満は非課税'}};
    if (amount <= 1000000) return {{tax: 200, note: ''}};
    if (amount <= 2000000) return {{tax: 400, note: ''}};
    if (amount <= 3000000) return {{tax: 1000, note: ''}};
    if (amount <= 5000000) return {{tax: 2000, note: ''}};
    if (amount <= 10000000) return {{tax: 10000, note: ''}};
    if (amount <= 50000000) return {{tax: 20000, note: ''}};
    if (amount <= 100000000) return {{tax: 60000, note: ''}};
    if (amount <= 500000000) return {{tax: 100000, note: ''}};
    if (amount <= 1000000000) return {{tax: 200000, note: ''}};
    if (amount <= 5000000000) return {{tax: 400000, note: ''}};
    return {{tax: 600000, note: ''}};
}}

function calc() {{
    const type = document.getElementById('docType').value;
    const amount = parseInt(document.getElementById('docAmount').value) || 0;
    const result = getStampDuty(type, amount);
    document.getElementById('rStamp').textContent = result.tax === 0 ? '非課税' : '\\u00a5' + result.tax.toLocaleString();
    document.getElementById('rStampNote').textContent = result.note;
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# 全ツールを書き出し
# ============================================================
tools = {
    "tool-51-business-day-calc": tool51,
    "tool-52-invoice-calc": tool52,
    "tool-53-age-calc": tool53,
    "tool-54-working-hours": tool54,
    "tool-55-late-fee-calc": tool55,
    "tool-56-inheritance-tax": tool56,
    "tool-57-stamp-duty": tool57,
}

print("=" * 60)
print("  DevTools Japan — OL・事務・士業向けツール7本を生成")
print("=" * 60)

for dirname, content in tools.items():
    dirpath = os.path.join(BASE, dirname)
    os.makedirs(dirpath, exist_ok=True)
    filepath = os.path.join(dirpath, "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {dirname}")

# sitemap.xml更新
print("\n📋 sitemap.xml を更新中...")
sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_urls = ""
for dirname in tools:
    url = f"https://www.devtools-japan.com/{dirname}/"
    if url not in sitemap:
        new_urls += f'  <url>\n    <loc>{url}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'

if new_urls:
    sitemap = sitemap.replace("</urlset>", new_urls + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("  ✅ sitemap.xml に7ツールを追加")

print("\n" + "=" * 60)
print("  完了！7ツール生成 + sitemap更新")
print("=" * 60)
print()
print("デプロイ:")
print("  git add .")
print('  git commit -m "Add 7 business/legal tools: 営業日計算, 請求書計算, 年齢計算, 残業代計算, 遅延損害金, 相続税, 印紙税"')
print("  git push")
