#!/usr/bin/env python3
"""
DevTools Japan — 税金・お金系ツール4本を追加
tool-66 ふるさと納税上限シミュレーター
tool-67 時給・月給・年収 換算
tool-68 インボイス消費税計算（適格請求書）
tool-69 為替計算（手入力レート）
"""
import os

BASE = "/Users/tom/Desktop/devtools-japan-complete"

COMMON_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-E27Q8YTG7L');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">"""

def make_style(accent, dim):
    return f"""        :root{{--bg:#f7f8fb;--bg-card:#ffffff;--border:#e0e2ed;--text:#1e1e35;--text2:#5a5f78;--text3:#9498b0;--accent:{accent};--accent-dim:{dim};--green:#22c55e;--red:#ef4444;--radius:12px}}
        ::selection{{background:rgba(99,102,241,0.15);color:#1e1e35}}*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);min-height:100vh}}
        .container{{max-width:800px;margin:0 auto;padding:40px 20px}}
        .ad-slot{{display:none}}
        header{{text-align:center;margin-bottom:36px}}header h1{{font-size:1.8rem;font-weight:700;color:var(--accent);margin-bottom:8px}}header p{{color:var(--text2);font-size:0.85rem}}
        .card{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:16px}}
        .card h3{{font-size:0.75rem;color:var(--text3);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:16px}}
        .row{{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border)}}.row:last-child{{border-bottom:none}}
        .row label{{font-size:0.85rem;color:var(--text2);flex:1}}
        .row input,.row select{{width:240px;padding:10px 14px;background:#f7f8fb;border:1px solid var(--border);border-radius:8px;color:var(--text);font-family:'Noto Sans JP',sans-serif;font-size:0.9rem;outline:none;text-align:right}}
        .row input:focus,.row select:focus{{border-color:var(--accent)}}
        .row .unit{{font-size:0.8rem;color:var(--text3);margin-left:8px;min-width:20px}}
        .result-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px}}
        @media(max-width:600px){{.result-grid{{grid-template-columns:1fr}}.row{{flex-wrap:wrap;gap:8px}}.row input,.row select{{width:100%}}}}
        .result-item{{background:#f7f8fb;border:1px solid var(--border);border-radius:var(--radius);padding:16px;text-align:center}}
        .result-item .label{{font-size:0.7rem;color:var(--text3);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px}}
        .result-item .value{{font-family:'JetBrains Mono',monospace;font-size:1.3rem;font-weight:700;color:var(--accent);word-break:break-all}}
        .result-item .value.tax{{color:var(--red)}}.result-item .value.take{{color:var(--green)}}
        .result-item .sub{{font-size:0.75rem;color:var(--text3);margin-top:4px}}
        .seo-content{{margin-top:40px;padding:28px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);color:var(--text2);font-size:0.85rem;line-height:2}}
        .seo-content h2{{color:var(--text);font-size:1.05rem;margin-bottom:12px}}.seo-content h3{{color:var(--text);font-size:0.95rem;margin-top:20px;margin-bottom:8px}}.seo-content p{{margin-bottom:10px}}
        footer{{text-align:center;margin-top:48px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}}
        .note{{background:var(--accent-dim);border:1px solid rgba(0,0,0,0.06);border-radius:8px;padding:12px 16px;font-size:0.75rem;color:var(--text2);margin-bottom:24px}}
        table.ref{{width:100%;border-collapse:collapse;margin:16px 0;font-size:0.8rem}}
        table.ref th{{background:var(--bg);border:1px solid var(--border);padding:8px 12px;text-align:left;font-weight:600;color:var(--text)}}
        table.ref td{{border:1px solid var(--border);padding:8px 12px;color:var(--text2)}}"""

NAV = '<div style="max-width:960px;margin:0 auto;padding:12px 20px 0"><a href="/" style="display:inline-flex;align-items:center;gap:6px;color:#5a5f78;text-decoration:none;font-size:0.8rem;font-family:Noto Sans JP,sans-serif"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8h5z"/></svg> DevTools Japan トップへ</a></div>'

def rl(href, text):
    return f'<a href="{href}" style="padding:8px 16px;background:var(--bg);border:1px solid var(--border);border-radius:8px;color:var(--text2);text-decoration:none;font-size:0.8rem;transition:border-color 0.2s" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'var(--border)\'">{text}</a>'

def footer(links):
    return f'''    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:20px;margin-top:24px;margin-bottom:24px">
      <h3 style="font-size:0.75rem;color:var(--text3);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:12px">関連ツール</h3>
      <div style="display:flex;gap:8px;flex-wrap:wrap">{links}</div>
    </div>
    <footer><p style="margin-bottom:8px">&copy; 2026 DevTools Japan — 無料オンラインツール</p>
    <p style="font-size:0.65rem"><a href="/about/" style="color:inherit;text-decoration:none;margin:0 8px">サイトについて</a> | <a href="/privacy/" style="color:inherit;text-decoration:none;margin:0 8px">プライバシーポリシー</a> | <a href="/contact/" style="color:inherit;text-decoration:none;margin:0 8px">お問い合わせ</a></p></footer>'''

FONT = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

# ============================================================
# Tool 66: ふるさと納税 上限額シミュレーター
# ============================================================
tool66 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>ふるさと納税 上限額シミュレーター | 年収から控除上限を概算【無料】</title>
    <meta name="description" content="年収と家族構成からふるさと納税の控除上限額（自己負担2,000円で済む寄付額の目安）を概算計算する無料ツール。会社員・給与所得者向け。年末の駆け込み寄付の前に上限額を確認。">
    {FONT}
    <style>
{make_style("#e11d48","rgba(225,29,72,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-66-furusato-tax/">
    <meta property="og:title" content="ふるさと納税 上限額シミュレーター | 年収から控除上限を概算【無料】">
    <meta property="og:description" content="年収と家族構成からふるさと納税の控除上限額を概算計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-66-furusato-tax/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="ふるさと納税 上限額シミュレーター【無料】">
    <meta name="twitter:description" content="年収から控除上限額を概算計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"ふるさと納税 上限額シミュレーター","description":"年収からふるさと納税の控除上限額を概算","url":"https://www.devtools-japan.com/tool-66-furusato-tax/","applicationCategory":"FinanceApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"ふるさと納税の上限額はどう決まる？","acceptedAnswer":{{"@type":"Answer","text":"ふるさと納税の控除上限額は、年収（課税所得）と家族構成によって決まります。年収が高いほど上限額が大きくなります。上限額を超えて寄付した分は自己負担になります。"}}}},{{"@type":"Question","name":"自己負担2000円とは？","acceptedAnswer":{{"@type":"Answer","text":"ふるさと納税は寄付額のうち2,000円を超える部分が所得税・住民税から控除されます。上限額の範囲内であれば、実質的な自己負担は2,000円のみで返礼品を受け取れます。"}}}}]}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>ふるさと納税 上限額シミュレーター</h1><p>年収から控除上限額を概算</p></header>
    <div class="note">概算シミュレーションです。実際の上限額は社会保険料・各種控除（医療費控除・住宅ローン控除等）により変動します。正確な金額は寄付前にお住まいの自治体や税理士にご確認ください。</div>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>給与収入（額面年収）</label><input type="number" id="income" value="5000000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>家族構成</label><select id="family" onchange="calc()">
            <option value="single" selected>独身または共働き</option>
            <option value="spouse">夫婦（配偶者に収入なし）</option>
            <option value="spouse_child1">夫婦+子1人（高校生）</option>
            <option value="spouse_child2">夫婦+子2人（高校生+大学生）</option>
        </select><span class="unit"></span></div>
    </div>

    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">控除上限額の目安</div><div class="value take" id="rLimit" style="font-size:2.4rem">-</div><div class="sub">この金額までの寄付なら自己負担2,000円で済みます</div></div>
    </div>

    <div class="card"><h3>年収別の上限額の目安（独身・共働きの場合）</h3>
        <table class="ref">
            <tr><th>年収</th><th>上限額の目安</th></tr>
            <tr><td>300万円</td><td>約28,000円</td></tr>
            <tr><td>400万円</td><td>約42,000円</td></tr>
            <tr><td>500万円</td><td>約61,000円</td></tr>
            <tr><td>600万円</td><td>約77,000円</td></tr>
            <tr><td>700万円</td><td>約108,000円</td></tr>
            <tr><td>800万円</td><td>約129,000円</td></tr>
            <tr><td>1,000万円</td><td>約180,000円</td></tr>
        </table>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>ふるさと納税 上限額シミュレーターの使い方</h2>
        <p>年収と家族構成を入力するだけで、ふるさと納税の控除上限額（自己負担2,000円で済む寄付額の上限）を概算計算する無料ツールです。年末の駆け込み寄付の前に、自分がいくらまで寄付できるかを把握できます。</p>
        <h3>ふるさと納税の仕組み</h3>
        <p>ふるさと納税は、好きな自治体に寄付すると、寄付額のうち2,000円を超える部分が所得税と住民税から控除される制度です。さらに自治体から返礼品がもらえるため、実質2,000円の負担で各地の特産品を受け取れる、人気の節税制度です。</p>
        <h3>上限額を超えるとどうなる？</h3>
        <p>控除上限額を超えて寄付すると、超過分は控除されず全額自己負担になります。そのため、自分の上限額を事前に把握しておくことが重要です。上限額は年収が高いほど大きくなり、家族構成（配偶者控除・扶養控除の有無）によっても変わります。</p>
        <h3>注意点</h3>
        <p>このツールは給与所得者向けの概算です。医療費控除、住宅ローン控除、iDeCoなどの控除を受けている場合は上限額が下がります。正確な上限額は、各ふるさと納税サイトの詳細シミュレーターや、お住まいの自治体にご確認ください。</p>
    </div>

    {footer(rl("/tool-64-take-home-pay/","手取り計算") + rl("/tool-21-tax-simulator/","確定申告シミュレーター") + rl("/tool-22-withholding-tax/","源泉徴収税計算"))}
</div>
<script>
function calc() {{
    const income = parseInt(document.getElementById('income').value) || 0;
    const family = document.getElementById('family').value;

    // 家族構成による調整係数（簡易）
    let adjust = 1.0;
    if (family === 'spouse') adjust = 0.85;
    else if (family === 'spouse_child1') adjust = 0.78;
    else if (family === 'spouse_child2') adjust = 0.70;

    // 給与所得控除
    let salaryDeduction;
    if (income <= 1625000) salaryDeduction = 550000;
    else if (income <= 1800000) salaryDeduction = income * 0.4 - 100000;
    else if (income <= 3600000) salaryDeduction = income * 0.3 + 80000;
    else if (income <= 6600000) salaryDeduction = income * 0.2 + 440000;
    else if (income <= 8500000) salaryDeduction = income * 0.1 + 1100000;
    else salaryDeduction = 1950000;

    // 社会保険料概算（額面の約15%）
    const social = income * 0.15;
    // 課税所得（基礎控除48万）
    let taxable = Math.max(0, income - salaryDeduction - 480000 - social);
    taxable = taxable * adjust;

    // 住民税所得割額（課税所得の10%）
    const residentTax = taxable * 0.10;

    // 所得税率（限界税率）
    let rate;
    if (taxable <= 1950000) rate = 0.05;
    else if (taxable <= 3300000) rate = 0.10;
    else if (taxable <= 6950000) rate = 0.20;
    else if (taxable <= 9000000) rate = 0.23;
    else if (taxable <= 18000000) rate = 0.33;
    else rate = 0.40;

    // ふるさと納税上限額 = 住民税所得割 × 20% ÷ (90% - 所得税率×1.021) + 2000
    const limit = Math.floor((residentTax * 0.2) / (0.9 - rate * 1.021) + 2000);
    const rounded = Math.floor(limit / 1000) * 1000;

    document.getElementById('rLimit').textContent = income > 0 && rounded > 2000 ? '\\u00a5' + rounded.toLocaleString() : '\\u00a50';
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 67: 時給・月給・年収 換算
# ============================================================
tool67 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>時給・月給・年収 換算ツール | 給与の相互変換を自動計算【無料】</title>
    <meta name="description" content="時給・月給・年収を相互に換算する無料ツール。「時給1,500円は年収いくら？」「年収500万は時給換算でいくら？」を即計算。労働時間を指定して正確に変換。転職・副業・パート勤務の比較に。">
    {FONT}
    <style>
{make_style("#7c3aed","rgba(124,58,237,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-67-wage-converter/">
    <meta property="og:title" content="時給・月給・年収 換算ツール | 給与の相互変換【無料】">
    <meta property="og:description" content="時給・月給・年収を相互に換算。労働時間を指定して正確に計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-67-wage-converter/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="時給・月給・年収 換算ツール【無料】">
    <meta name="twitter:description" content="時給・月給・年収を相互に換算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"時給・月給・年収 換算ツール","description":"時給・月給・年収を相互に換算","url":"https://www.devtools-japan.com/tool-67-wage-converter/","applicationCategory":"FinanceApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>時給・月給・年収 換算</h1><p>給与の相互変換を自動計算</p></header>

    <div class="card"><h3>労働条件</h3>
        <div class="row"><label>1日の労働時間</label><input type="number" id="hoursPerDay" value="8" step="0.5" oninput="recalc()"><span class="unit">時間</span></div>
        <div class="row"><label>月の労働日数</label><input type="number" id="daysPerMonth" value="20" oninput="recalc()"><span class="unit">日</span></div>
    </div>

    <div class="card"><h3>金額を入力（いずれか1つ）</h3>
        <div class="row"><label>時給</label><input type="number" id="hourly" value="1500" oninput="fromHourly()"><span class="unit">円</span></div>
        <div class="row"><label>月給</label><input type="number" id="monthly" oninput="fromMonthly()"><span class="unit">円</span></div>
        <div class="row"><label>年収</label><input type="number" id="yearly" oninput="fromYearly()"><span class="unit">円</span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">時給換算</div><div class="value" id="rHourly">-</div></div>
        <div class="result-item"><div class="label">日給換算</div><div class="value" id="rDaily">-</div></div>
        <div class="result-item"><div class="label">月給換算</div><div class="value" id="rMonthly">-</div></div>
        <div class="result-item"><div class="label">年収換算</div><div class="value take" id="rYearly">-</div></div>
    </div>

    <div class="note">額面ベースの単純換算です。実際の手取りは税金・社会保険料が引かれます。手取りを知りたい場合は手取り計算ツールをご利用ください。</div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>時給・月給・年収 換算ツールの使い方</h2>
        <p>時給・月給・年収のいずれか1つを入力すると、残りの2つを自動的に換算する無料ツールです。「時給1,500円で働くと年収いくら？」「年収500万円は時給換算でいくら？」といった疑問を即座に解決できます。1日の労働時間と月の労働日数を指定して、正確に計算します。</p>
        <h3>換算の計算方法</h3>
        <p>時給から月給は「時給 × 1日の労働時間 × 月の労働日数」、月給から年収は「月給 × 12」で計算します。労働条件（1日8時間・月20日など）を変えると結果も変わるため、自分の勤務状況に合わせて入力してください。</p>
        <h3>転職・副業・パート比較に</h3>
        <p>正社員（年収提示）とパート・アルバイト（時給提示）の収入を比較したいとき、フリーランスの単価を時給換算したいとき、副業の時給が割に合うか確認したいときなどに便利です。異なる給与体系を同じ土俵で比較できます。</p>
        <h3>額面と手取りの違い</h3>
        <p>このツールは額面（税引き前）の単純換算です。実際に受け取る手取り額は、ここから所得税・住民税・社会保険料が引かれます。手取り額を知りたい場合は、手取り計算ツールをあわせてご利用ください。</p>
    </div>

    {footer(rl("/tool-64-take-home-pay/","手取り計算") + rl("/tool-54-working-hours/","残業代計算") + rl("/tool-58-freelance-income/","フリーランス年収シミュレーター"))}
</div>
<script>
function hoursPerMonth() {{
    const h = parseFloat(document.getElementById('hoursPerDay').value) || 8;
    const d = parseInt(document.getElementById('daysPerMonth').value) || 20;
    return h * d;
}}
function update(hourly) {{
    const hpm = hoursPerMonth();
    const hpd = parseFloat(document.getElementById('hoursPerDay').value) || 8;
    const monthly = hourly * hpm;
    const yearly = monthly * 12;
    const daily = hourly * hpd;
    const f = n => '\\u00a5' + Math.round(n).toLocaleString();
    document.getElementById('rHourly').textContent = f(hourly);
    document.getElementById('rDaily').textContent = f(daily);
    document.getElementById('rMonthly').textContent = f(monthly);
    document.getElementById('rYearly').textContent = f(yearly);
}}
function fromHourly() {{
    const h = parseFloat(document.getElementById('hourly').value) || 0;
    document.getElementById('monthly').value = '';
    document.getElementById('yearly').value = '';
    update(h);
}}
function fromMonthly() {{
    const m = parseFloat(document.getElementById('monthly').value) || 0;
    const hpm = hoursPerMonth();
    document.getElementById('hourly').value = '';
    document.getElementById('yearly').value = '';
    update(hpm > 0 ? m / hpm : 0);
}}
function fromYearly() {{
    const y = parseFloat(document.getElementById('yearly').value) || 0;
    const hpm = hoursPerMonth();
    document.getElementById('hourly').value = '';
    document.getElementById('monthly').value = '';
    update(hpm > 0 ? (y / 12) / hpm : 0);
}}
function recalc() {{
    // 労働条件変更時は時給基準で再計算
    const h = parseFloat(document.getElementById('hourly').value);
    if (h) {{ fromHourly(); return; }}
    const m = parseFloat(document.getElementById('monthly').value);
    if (m) {{ fromMonthly(); return; }}
    const y = parseFloat(document.getElementById('yearly').value);
    if (y) {{ fromYearly(); return; }}
}}
fromHourly();
</script>
</body>
</html>'''


# ============================================================
# Tool 68: インボイス消費税計算（適格請求書）
# ============================================================
tool68 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>インボイス消費税計算ツール | 適格請求書の消費税額・端数処理を計算【無料】</title>
    <meta name="description" content="インボイス制度（適格請求書）に対応した消費税計算ツール。税率ごと（10%・8%）に区分して消費税額を計算し、1請求書あたり税率ごとに1回の端数処理を行う。インボイスの記載要件に沿った正確な税額計算に。">
    {FONT}
    <style>
{make_style("#0d9488","rgba(13,148,136,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-68-invoice-tax/">
    <meta property="og:title" content="インボイス消費税計算ツール | 適格請求書の税額・端数処理【無料】">
    <meta property="og:description" content="税率ごとに区分して消費税額を計算。インボイス制度の端数処理ルールに対応">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-68-invoice-tax/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="インボイス消費税計算ツール【無料】">
    <meta name="twitter:description" content="適格請求書の消費税額・端数処理を計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"インボイス消費税計算ツール","description":"適格請求書の消費税額を税率ごとに計算","url":"https://www.devtools-japan.com/tool-68-invoice-tax/","applicationCategory":"FinanceApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>インボイス消費税計算</h1><p>適格請求書の税額・端数処理を計算</p></header>
    <div class="note">インボイス制度では「1つの適格請求書につき、税率ごとに1回」の端数処理が原則です。このツールは税率区分ごとに合計してから端数処理（切り捨て）します。</div>

    <div class="card"><h3>10%対象の品目（税抜合計）</h3>
        <div class="row"><label>10%対象の税抜合計</label><input type="number" id="base10" value="50000" oninput="calc()"><span class="unit">円</span></div>
    </div>
    <div class="card"><h3>8%対象の品目（税抜合計・軽減税率）</h3>
        <div class="row"><label>8%対象の税抜合計</label><input type="number" id="base8" value="20000" oninput="calc()"><span class="unit">円</span></div>
    </div>
    <div class="card"><h3>端数処理</h3>
        <div class="row"><label>処理方法</label><select id="rounding" onchange="calc()">
            <option value="floor" selected>切り捨て</option>
            <option value="round">四捨五入</option>
            <option value="ceil">切り上げ</option>
        </select><span class="unit"></span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">10%対象 税抜</div><div class="value" id="r10base">-</div></div>
        <div class="result-item"><div class="label">10%消費税額</div><div class="value tax" id="r10tax">-</div></div>
        <div class="result-item"><div class="label">8%対象 税抜</div><div class="value" id="r8base">-</div></div>
        <div class="result-item"><div class="label">8%消費税額</div><div class="value tax" id="r8tax">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item"><div class="label">消費税合計</div><div class="value tax" id="rTaxTotal" style="font-size:1.6rem">-</div></div>
        <div class="result-item"><div class="label">税込合計</div><div class="value take" id="rTotal" style="font-size:1.6rem">-</div></div>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>インボイス消費税計算ツールの使い方</h2>
        <p>インボイス制度（適格請求書等保存方式）に対応した消費税計算ツールです。10%と8%の税率ごとに税抜金額を区分入力すると、税率ごとの消費税額と合計を計算します。インボイスの記載要件に沿った正確な税額計算ができます。</p>
        <h3>インボイス制度の端数処理ルール</h3>
        <p>2023年10月開始のインボイス制度では、消費税の端数処理は「1つの適格請求書につき、税率ごとに1回まで」と定められています。これまでのように商品1つずつ端数処理することはできません。税率ごとに税抜金額を合計してから、まとめて1回だけ端数処理を行います。</p>
        <h3>税率ごとの区分が必須</h3>
        <p>適格請求書には、10%対象と8%対象（軽減税率）を分けて記載し、それぞれの税抜金額（または税込金額）と消費税額を明記する必要があります。このツールは税率ごとに分けて計算するため、インボイスの記載内容の確認に使えます。</p>
        <h3>端数処理の方法</h3>
        <p>端数処理の方法（切り捨て・四捨五入・切り上げ）は事業者が任意に選択できますが、継続して同じ方法を使う必要があります。このツールでは3つの方法を切り替えて確認できます。</p>
    </div>

    {footer(rl("/tool-65-consumption-tax/","消費税計算") + rl("/tool-52-invoice-calc/","請求書金額計算") + rl("/tool-22-withholding-tax/","源泉徴収税計算"))}
</div>
<script>
function calc() {{
    const base10 = parseInt(document.getElementById('base10').value) || 0;
    const base8 = parseInt(document.getElementById('base8').value) || 0;
    const method = document.getElementById('rounding').value;

    function roundTax(v) {{
        if (method === 'floor') return Math.floor(v);
        if (method === 'ceil') return Math.ceil(v);
        return Math.round(v);
    }}

    const tax10 = roundTax(base10 * 0.10);
    const tax8 = roundTax(base8 * 0.08);
    const taxTotal = tax10 + tax8;
    const total = base10 + base8 + taxTotal;

    const f = n => '\\u00a5' + n.toLocaleString();
    document.getElementById('r10base').textContent = f(base10);
    document.getElementById('r10tax').textContent = f(tax10);
    document.getElementById('r8base').textContent = f(base8);
    document.getElementById('r8tax').textContent = f(tax8);
    document.getElementById('rTaxTotal').textContent = f(taxTotal);
    document.getElementById('rTotal').textContent = f(total);
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 69: 為替計算（手入力レート）
# ============================================================
tool69 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>為替計算ツール | レートを入力して外貨⇔円を換算【無料】</title>
    <meta name="description" content="為替レートを入力して外貨と日本円を相互換算する無料ツール。ドル・ユーロ・ポンドなど任意の通貨に対応。海外通販、旅行予算、外貨建て請求書の計算に。手数料（スプレッド）込みの計算も可能。">
    {FONT}
    <style>
{make_style("#2563eb","rgba(37,99,235,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-69-currency-calc/">
    <meta property="og:title" content="為替計算ツール | レートを入力して外貨⇔円を換算【無料】">
    <meta property="og:description" content="為替レートを入力して外貨と円を相互換算。手数料込みの計算も可能">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-69-currency-calc/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="為替計算ツール【無料】">
    <meta name="twitter:description" content="レートを入力して外貨⇔円を換算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"為替計算ツール","description":"為替レートを入力して外貨と円を換算","url":"https://www.devtools-japan.com/tool-69-currency-calc/","applicationCategory":"FinanceApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>為替計算</h1><p>レートを入力して外貨⇔円を換算</p></header>
    <div class="note">為替レートは手入力です。最新レートはGoogle検索や金融機関のサイトでご確認ください（「ドル円 レート」等で検索）。リアルタイムレートの自動取得には対応していません。</div>

    <div class="card"><h3>レート設定</h3>
        <div class="row"><label>通貨単位</label><input type="text" id="currency" value="USD" oninput="calc()"></div>
        <div class="row"><label>1<span id="curLabel">USD</span> = </label><input type="number" id="rate" value="155" step="0.01" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>為替手数料（スプレッド片道）</label><input type="number" id="fee" value="0" step="0.1" oninput="calc()"><span class="unit">円</span></div>
    </div>

    <div class="card"><h3>外貨 → 円</h3>
        <div class="row"><label>外貨金額</label><input type="number" id="foreign" value="100" oninput="fromForeign()"><span class="unit" id="fUnit">USD</span></div>
        <div class="result-grid" style="margin-top:12px">
            <div class="result-item"><div class="label">円換算（レートのみ）</div><div class="value" id="rToYen">-</div></div>
            <div class="result-item"><div class="label">手数料込み（購入時）</div><div class="value take" id="rToYenFee">-</div></div>
        </div>
    </div>

    <div class="card"><h3>円 → 外貨</h3>
        <div class="row"><label>円金額</label><input type="number" id="yen" value="10000" oninput="fromYen()"><span class="unit">円</span></div>
        <div class="result-grid" style="margin-top:12px">
            <div class="result-item"><div class="label">外貨換算（レートのみ）</div><div class="value" id="rToForeign">-</div></div>
            <div class="result-item"><div class="label">手数料込み（両替時）</div><div class="value take" id="rToForeignFee">-</div></div>
        </div>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>為替計算ツールの使い方</h2>
        <p>為替レートを手動で入力して、外貨と日本円を相互に換算する無料ツールです。米ドル・ユーロ・ポンド・ウォンなど、任意の通貨に対応しています。海外通販の支払額確認、旅行予算の計算、外貨建て請求書の円換算などに使えます。</p>
        <h3>為替手数料（スプレッド）の計算</h3>
        <p>実際に両替や外貨決済をする際は、為替レートに手数料（スプレッド）が上乗せされます。例えば「1ドル155円」でも、銀行で外貨を買うと1ドル156円になることがあります。このツールでは手数料を入力することで、実際の負担額に近い金額を計算できます。</p>
        <h3>こんな場面で使えます</h3>
        <p>海外ECサイト（Amazon.com、eBay等）での購入金額の円換算、海外旅行の予算管理、外貨預金の損益計算、海外取引先への請求書の円換算、クレジットカードの海外利用額の確認など。レートを自分で入力するため、任意のタイミング・任意のレートで計算できます。</p>
        <h3>最新レートの確認方法</h3>
        <p>このツールはリアルタイムレートの自動取得には対応していません。最新の為替レートは、Google検索で「ドル円」と入力するか、金融機関や為替情報サイトでご確認のうえ、レート欄に入力してください。</p>
    </div>

    {footer(rl("/tool-65-consumption-tax/","消費税計算") + rl("/tool-67-wage-converter/","時給・月給・年収換算") + rl("/tool-32-unit-converter/","単位変換"))}
</div>
<script>
function getRate() {{ return parseFloat(document.getElementById('rate').value) || 0; }}
function getFee() {{ return parseFloat(document.getElementById('fee').value) || 0; }}
function calc() {{
    const cur = document.getElementById('currency').value || 'USD';
    document.getElementById('curLabel').textContent = cur;
    document.getElementById('fUnit').textContent = cur;
    fromForeign();
}}
function fromForeign() {{
    const f = parseFloat(document.getElementById('foreign').value) || 0;
    const rate = getRate(), fee = getFee();
    const yen = f * rate;
    const yenFee = f * (rate + fee);
    const fmt = n => '\\u00a5' + Math.round(n).toLocaleString();
    document.getElementById('rToYen').textContent = fmt(yen);
    document.getElementById('rToYenFee').textContent = fmt(yenFee);
}}
function fromYen() {{
    const y = parseFloat(document.getElementById('yen').value) || 0;
    const cur = document.getElementById('currency').value || 'USD';
    const rate = getRate(), fee = getFee();
    const foreign = rate > 0 ? y / rate : 0;
    const foreignFee = (rate + fee) > 0 ? y / (rate + fee) : 0;
    const fmt = n => n.toFixed(2) + ' ' + cur;
    document.getElementById('rToForeign').textContent = fmt(foreign);
    document.getElementById('rToForeignFee').textContent = fmt(foreignFee);
}}
calc();
fromYen();
</script>
</body>
</html>'''


# ============================================================
# 書き出し
# ============================================================
tools = {
    "tool-66-furusato-tax": tool66,
    "tool-67-wage-converter": tool67,
    "tool-68-invoice-tax": tool68,
    "tool-69-currency-calc": tool69,
}

print("=" * 60)
print("  DevTools Japan — 税金・お金系ツール4本を生成")
print("=" * 60)

for dirname, content in tools.items():
    dirpath = os.path.join(BASE, dirname)
    os.makedirs(dirpath, exist_ok=True)
    filepath = os.path.join(dirpath, "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK {dirname}")

# sitemap更新
print("\nsitemap.xml を更新中...")
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
    print("  OK sitemap.xml に4ツールを追加")

print("\n完了！税金・お金系4ツール生成 + sitemap更新")
print("\n次: python3 money_portal_update.py でポータル登録")
