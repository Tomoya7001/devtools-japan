#!/usr/bin/env python3
"""
DevTools Japan — フリーランス向けツール4本を追加
tool-58〜tool-61
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
        .row input,.row select{{width:200px;padding:10px 14px;background:#f7f8fb;border:1px solid var(--border);border-radius:8px;color:var(--text);font-family:'Noto Sans JP',sans-serif;font-size:0.9rem;outline:none;text-align:right}}
        .row input:focus,.row select:focus{{border-color:var(--accent)}}
        .row .unit{{font-size:0.8rem;color:var(--text3);margin-left:8px;min-width:20px}}
        .result-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px}}
        @media(max-width:600px){{.result-grid{{grid-template-columns:1fr}}.row{{flex-wrap:wrap;gap:8px}}.row input,.row select{{width:100%}}}}
        .result-item{{background:#f7f8fb;border:1px solid var(--border);border-radius:var(--radius);padding:16px;text-align:center}}
        .result-item .label{{font-size:0.7rem;color:var(--text3);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px}}
        .result-item .value{{font-family:'JetBrains Mono',monospace;font-size:1.4rem;font-weight:700;color:var(--accent)}}
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
# Tool 58: フリーランス年収シミュレーター
# ============================================================
tool58 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>フリーランス年収シミュレーター | 月単価から年収・手取りを自動計算【無料】</title>
    <meta name="description" content="フリーランスエンジニアの年収・手取りを月単価と稼働率から自動計算。所得税・住民税・国民健康保険・国民年金を差し引いた実際の手取り額がわかる無料シミュレーター。独立前の収入シミュレーションに。">
    {FONT}
    <style>
{make_style("#f59e0b","rgba(245,158,11,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-58-freelance-income/">
    <meta property="og:title" content="フリーランス年収シミュレーター | 月単価から手取りを計算【無料】">
    <meta property="og:description" content="月単価×稼働率から年収・税金・社会保険料・手取りを自動計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-58-freelance-income/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="フリーランス年収シミュレーター【無料】">
    <meta name="twitter:description" content="月単価から年収・手取りを自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"フリーランス年収シミュレーター","description":"月単価から年収・手取りを自動計算","url":"https://www.devtools-japan.com/tool-58-freelance-income/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>フリーランス年収シミュレーター</h1><p>月単価・稼働率から年収・手取りを自動計算</p></header>
    <div class="note">独立を検討中のエンジニア・デザイナー向け。会社員時代と比較して「実際いくら手元に残るか」を把握できます。</div>

    <div class="card"><h3>収入</h3>
        <div class="row"><label>月単価</label><input type="number" id="monthlyRate" value="700000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>年間稼働月数</label><input type="number" id="workMonths" value="11" min="1" max="12" oninput="calc()"><span class="unit">ヶ月</span></div>
    </div>
    <div class="card"><h3>経費</h3>
        <div class="row"><label>年間経費合計</label><input type="number" id="expenses" value="600000" oninput="calc()"><span class="unit">円</span></div>
    </div>
    <div class="card"><h3>控除</h3>
        <div class="row"><label>青色申告特別控除</label><select id="blueDeduction" onchange="calc()"><option value="650000" selected>65万円（e-Tax+複式簿記）</option><option value="100000">10万円（簡易簿記）</option><option value="0">なし（白色申告）</option></select><span class="unit"></span></div>
        <div class="row"><label>小規模企業共済（月額）</label><input type="number" id="idc" value="30000" oninput="calc()"><span class="unit">円/月</span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">年間売上</div><div class="value" id="rRevenue">-</div></div>
        <div class="result-item"><div class="label">事業所得</div><div class="value" id="rIncome">-</div></div>
        <div class="result-item"><div class="label">所得税</div><div class="value tax" id="rIncomeTax">-</div></div>
        <div class="result-item"><div class="label">住民税</div><div class="value tax" id="rResTax">-</div></div>
        <div class="result-item"><div class="label">国民健康保険（概算）</div><div class="value tax" id="rNhi">-</div></div>
        <div class="result-item"><div class="label">国民年金</div><div class="value tax" id="rPension">-</div></div>
        <div class="result-item"><div class="label">個人事業税</div><div class="value tax" id="rBizTax">-</div></div>
        <div class="result-item"><div class="label">小規模企業共済</div><div class="value" id="rIdc">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">年間手取り額（税金・社保差引後）</div><div class="value take" id="rTakeHome" style="font-size:2rem">-</div><div class="sub" id="rMonthly"></div></div>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>フリーランス年収シミュレーターの使い方</h2>
        <p>フリーランスエンジニア・デザイナーが月単価と稼働率から年収と手取り額をシミュレーションする無料ツールです。会社員時代は会社が天引きしていた所得税・住民税・社会保険料をすべて自分で把握する必要があるフリーランスのために、主要な税金と社会保険料を一括で概算計算します。</p>
        <h3>フリーランスが支払う税金・社会保険</h3>
        <p>フリーランスは所得税、住民税、国民健康保険料、国民年金、個人事業税（所得290万超）を自分で支払います。会社員は社会保険料の半分を会社が負担しますが、フリーランスは全額自己負担です。そのため「月単価70万円で年収840万円」でも、手取りは600万円台になることが多いです。</p>
        <h3>会社員との手取り比較</h3>
        <p>一般的に、フリーランスが会社員と同じ手取りを得るには、会社員時代の年収の1.3〜1.5倍の売上が必要と言われています。このツールで具体的な数字を出して、独立前に現実的な収入プランを立てましょう。</p>
        <h3>節税のポイント</h3>
        <p>青色申告65万円控除、小規模企業共済（最大月7万円、全額所得控除）、iDeCo、ふるさと納税を組み合わせることで、大幅な節税が可能です。このツールで控除額を変えてシミュレーションしてみてください。</p>
    </div>

    {footer(rl("/tool-21-tax-simulator/","確定申告シミュレーター") + rl("/tool-22-withholding-tax/","源泉徴収税計算") + rl("/tool-52-invoice-calc/","請求書金額計算"))}
</div>
<script>
function calc() {{
    const rate = parseInt(document.getElementById('monthlyRate').value) || 0;
    const months = parseInt(document.getElementById('workMonths').value) || 11;
    const expenses = parseInt(document.getElementById('expenses').value) || 0;
    const blue = parseInt(document.getElementById('blueDeduction').value) || 0;
    const idcMonthly = parseInt(document.getElementById('idc').value) || 0;
    const idcAnnual = idcMonthly * 12;
    const pensionAnnual = 16980 * 12; // 2026年度国民年金

    const revenue = rate * months;
    const income = Math.max(0, revenue - expenses);
    const bizTax = income > 2900000 ? Math.floor((income - 2900000) * 0.05) : 0;

    // 社会保険料控除（国保概算 + 国民年金）
    const nhiRate = 0.10; // 国保概算（所得の約10%、自治体により異なる）
    const nhiBase = Math.max(0, income - 430000); // 基礎控除43万
    const nhiAnnual = Math.min(Math.floor(nhiBase * nhiRate), 1060000); // 上限106万
    const socialInsurance = nhiAnnual + pensionAnnual;

    // 課税所得
    const taxableIncome = Math.max(0, income - blue - 480000 - socialInsurance - idcAnnual);

    // 所得税（累進課税）
    let incomeTax = 0;
    if (taxableIncome <= 1950000) incomeTax = taxableIncome * 0.05;
    else if (taxableIncome <= 3300000) incomeTax = taxableIncome * 0.10 - 97500;
    else if (taxableIncome <= 6950000) incomeTax = taxableIncome * 0.20 - 427500;
    else if (taxableIncome <= 9000000) incomeTax = taxableIncome * 0.23 - 636000;
    else if (taxableIncome <= 18000000) incomeTax = taxableIncome * 0.33 - 1536000;
    else incomeTax = taxableIncome * 0.40 - 2796000;
    incomeTax = Math.floor(incomeTax * 1.021); // 復興特別所得税

    // 住民税
    const resTax = Math.floor(taxableIncome * 0.10) + 5000;

    const totalDeductions = incomeTax + resTax + nhiAnnual + pensionAnnual + bizTax + idcAnnual;
    const takeHome = revenue - expenses - incomeTax - resTax - nhiAnnual - pensionAnnual - bizTax - idcAnnual;

    const f = n => n.toLocaleString();
    document.getElementById('rRevenue').textContent = '\\u00a5' + f(revenue);
    document.getElementById('rIncome').textContent = '\\u00a5' + f(income);
    document.getElementById('rIncomeTax').textContent = '\\u00a5' + f(Math.max(0,incomeTax));
    document.getElementById('rResTax').textContent = '\\u00a5' + f(Math.max(0,resTax));
    document.getElementById('rNhi').textContent = '\\u00a5' + f(nhiAnnual);
    document.getElementById('rPension').textContent = '\\u00a5' + f(pensionAnnual);
    document.getElementById('rBizTax').textContent = bizTax > 0 ? '\\u00a5' + f(bizTax) : '\\u00a50（290万以下）';
    document.getElementById('rIdc').textContent = idcAnnual > 0 ? '\\u00a5' + f(idcAnnual) : '-';
    document.getElementById('rTakeHome').textContent = '\\u00a5' + f(Math.max(0,takeHome));
    document.getElementById('rMonthly').textContent = '月平均 \\u00a5' + f(Math.round(Math.max(0,takeHome)/12));
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 59: 減価償却計算
# ============================================================
tool59 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>減価償却計算ツール | PC・車・設備の減価償却費を自動計算【無料】</title>
    <meta name="description" content="PC・車・事務機器などの減価償却費を定額法・定率法で自動計算する無料ツール。取得価額・耐用年数を入力するだけで年間の経費額がわかる。フリーランス・個人事業主の確定申告に。">
    {FONT}
    <style>
{make_style("#0d9488","rgba(13,148,136,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-59-depreciation/">
    <meta property="og:title" content="減価償却計算 | PC・車の減価償却費を自動計算【無料】">
    <meta property="og:description" content="取得価額と耐用年数から減価償却費を定額法・定率法で計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-59-depreciation/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="減価償却計算ツール【無料】">
    <meta name="twitter:description" content="PC・車の減価償却費を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"減価償却計算ツール","description":"減価償却費を定額法・定率法で計算","url":"https://www.devtools-japan.com/tool-59-depreciation/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>減価償却計算</h1><p>PC・車・設備の減価償却費を自動計算</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>取得価額</label><input type="number" id="cost" value="250000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>耐用年数</label><select id="life" onchange="calc()">
            <option value="2">2年</option><option value="3">3年</option><option value="4" selected>4年（PC）</option><option value="5">5年</option><option value="6">6年（自動車）</option><option value="8">8年</option><option value="10">10年</option><option value="15">15年</option><option value="20">20年</option>
        </select><span class="unit"></span></div>
        <div class="row"><label>償却方法</label><select id="method" onchange="calc()"><option value="straight" selected>定額法</option><option value="declining">定率法</option></select><span class="unit"></span></div>
        <div class="row"><label>事業使用割合</label><input type="number" id="bizRatio" value="100" min="1" max="100" oninput="calc()"><span class="unit">%</span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">年間の減価償却費</div><div class="value take" id="rAnnual">-</div></div>
        <div class="result-item"><div class="label">月額の減価償却費</div><div class="value" id="rMonthly">-</div></div>
    </div>

    <div class="card" id="schedule"></div>

    <div class="note">10万円未満の資産は全額経費（消耗品費）。青色申告者は30万円未満の資産を一括で経費にできる特例（少額減価償却資産の特例）があります。</div>

    <div class="card"><h3>よく使う耐用年数</h3>
        <table class="ref">
            <tr><th>資産</th><th>耐用年数</th></tr>
            <tr><td>パソコン（PC）</td><td>4年</td></tr>
            <tr><td>サーバー</td><td>5年</td></tr>
            <tr><td>ソフトウェア（自社開発）</td><td>3年</td></tr>
            <tr><td>ソフトウェア（購入）</td><td>5年</td></tr>
            <tr><td>普通自動車</td><td>6年</td></tr>
            <tr><td>軽自動車</td><td>4年</td></tr>
            <tr><td>事務机・椅子（金属製）</td><td>15年</td></tr>
            <tr><td>事務机・椅子（その他）</td><td>8年</td></tr>
            <tr><td>エアコン</td><td>6年</td></tr>
            <tr><td>コピー機・プリンター</td><td>5年</td></tr>
        </table>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>減価償却計算ツールの使い方</h2>
        <p>10万円以上の資産（PC、車、オフィス家具等）を購入した場合、一括で経費にせず耐用年数に分けて経費化する「減価償却」が必要です。このツールは取得価額と耐用年数を入力するだけで、年間の減価償却費を自動計算します。</p>
        <h3>定額法と定率法</h3>
        <p>定額法は毎年同じ金額を経費にする方法（個人事業主のデフォルト）。定率法は初年度に多く経費化し、年々減少する方法（法人のデフォルト）。個人事業主が定率法を使うには税務署への届出が必要です。</p>
        <h3>フリーランスのPC購入</h3>
        <p>25万円のMacBookを購入した場合、通常は4年で減価償却（年62,500円の経費）。ただし青色申告者なら「少額減価償却資産の特例」で30万円未満の資産を一括経費にできます。年間300万円まで。</p>
        <h3>事業使用割合（按分）</h3>
        <p>プライベートでも使うPCや車の場合、事業使用割合で按分します。PCの事業使用割合が80%なら、減価償却費の80%のみが経費になります。</p>
    </div>

    {footer(rl("/tool-21-tax-simulator/","確定申告シミュレーター") + rl("/tool-58-freelance-income/","フリーランス年収シミュレーター") + rl("/tool-52-invoice-calc/","請求書金額計算"))}
</div>
<script>
function calc() {{
    const cost = parseInt(document.getElementById('cost').value) || 0;
    const life = parseInt(document.getElementById('life').value) || 4;
    const method = document.getElementById('method').value;
    const ratio = (parseInt(document.getElementById('bizRatio').value) || 100) / 100;

    let html = '<h3>償却スケジュール</h3><table class="ref"><tr><th>年</th><th>償却額</th><th>期末帳簿価額</th></tr>';
    let remaining = cost;

    if (method === 'straight') {{
        const annual = Math.floor(cost / life);
        const annualBiz = Math.floor(annual * ratio);
        document.getElementById('rAnnual').textContent = '\\u00a5' + annualBiz.toLocaleString();
        document.getElementById('rMonthly').textContent = '\\u00a5' + Math.round(annualBiz/12).toLocaleString();
        for (let y = 1; y <= life; y++) {{
            const dep = y === life ? remaining - 1 : annual;
            remaining -= dep;
            html += `<tr><td>${{y}}年目</td><td>${{Math.floor(dep*ratio).toLocaleString()}}円</td><td>${{Math.max(1,remaining).toLocaleString()}}円</td></tr>`;
        }}
    }} else {{
        const rate = Math.round((1 / life) * 2.5 * 1000) / 1000;
        const guarantee = Math.floor(cost * 0.04448);
        let firstYear = Math.floor(cost * rate * ratio);
        document.getElementById('rAnnual').textContent = '\\u00a5' + firstYear.toLocaleString() + '（初年度）';
        document.getElementById('rMonthly').textContent = '\\u00a5' + Math.round(firstYear/12).toLocaleString() + '（初年度）';
        for (let y = 1; y <= life; y++) {{
            let dep = Math.floor(remaining * rate);
            if (dep < guarantee || y === life) dep = remaining - 1;
            remaining -= dep;
            html += `<tr><td>${{y}}年目</td><td>${{Math.floor(dep*ratio).toLocaleString()}}円</td><td>${{Math.max(1,remaining).toLocaleString()}}円</td></tr>`;
            if (remaining <= 1) break;
        }}
    }}
    html += '</table>';
    document.getElementById('schedule').innerHTML = html;
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 60: 国民健康保険料計算
# ============================================================
tool60 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>国民健康保険料計算ツール | フリーランスの国保料を概算シミュレーション【無料】</title>
    <meta name="description" content="フリーランス・個人事業主の国民健康保険料を概算計算する無料ツール。年間所得を入力するだけで保険料の目安がわかる。独立前の社会保険料シミュレーションに。">
    {FONT}
    <style>
{make_style("#e11d48","rgba(225,29,72,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-60-nhi-calc/">
    <meta property="og:title" content="国民健康保険料計算 | フリーランスの国保料を概算【無料】">
    <meta property="og:description" content="年間所得から国民健康保険料を概算シミュレーション">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-60-nhi-calc/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="国民健康保険料計算【無料】">
    <meta name="twitter:description" content="フリーランスの国保料を概算計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"国民健康保険料計算ツール","description":"フリーランスの国民健康保険料を概算計算","url":"https://www.devtools-japan.com/tool-60-nhi-calc/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>国民健康保険料計算</h1><p>フリーランスの国保料を概算シミュレーション</p></header>
    <div class="note">保険料率は自治体によって異なります。このツールは全国平均的な料率で概算しています。正確な金額はお住まいの市区町村にお問い合わせください。</div>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>年間所得（売上−経費）</label><input type="number" id="income" value="5000000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>年齢</label><select id="age" onchange="calc()"><option value="under40" selected>40歳未満</option><option value="40to64">40〜64歳（介護保険あり）</option><option value="65over">65歳以上</option></select><span class="unit"></span></div>
        <div class="row"><label>世帯の加入者数</label><input type="number" id="members" value="1" min="1" max="10" oninput="calc()"><span class="unit">人</span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">医療分</div><div class="value tax" id="rMedical">-</div></div>
        <div class="result-item"><div class="label">後期高齢者支援分</div><div class="value tax" id="rElderly">-</div></div>
        <div class="result-item"><div class="label">介護分（40〜64歳のみ）</div><div class="value tax" id="rCare">-</div></div>
        <div class="result-item"><div class="label">均等割（人数分）</div><div class="value tax" id="rFlat">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">国民健康保険料（年額）</div><div class="value tax" id="rTotal" style="font-size:2rem">-</div><div class="sub" id="rMonthly"></div></div>
    </div>

    <div class="card"><h3>国民健康保険料の賦課限度額（2024年度）</h3>
        <table class="ref">
            <tr><th>区分</th><th>上限額</th></tr>
            <tr><td>医療分</td><td>65万円</td></tr>
            <tr><td>後期高齢者支援分</td><td>24万円</td></tr>
            <tr><td>介護分</td><td>17万円</td></tr>
            <tr><td>合計上限</td><td>106万円</td></tr>
        </table>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>国民健康保険料計算ツールの使い方</h2>
        <p>フリーランス・個人事業主が加入する国民健康保険（国保）の保険料を概算計算する無料ツールです。会社員の社会保険（協会けんぽ等）と異なり、国保は全額自己負担で、所得に応じて保険料が大きく変動します。</p>
        <h3>国保の計算の仕組み</h3>
        <p>国民健康保険料は「所得割（所得に応じた額）」と「均等割（加入者1人あたりの定額）」の合計で計算されます。さらに「医療分」「後期高齢者支援分」「介護分（40〜64歳のみ）」の3つに分かれており、それぞれに上限額が設定されています。</p>
        <h3>会社員との比較</h3>
        <p>会社員は社会保険料の半分を会社が負担しますが、フリーランスは全額自己負担です。年間所得500万円のフリーランスの国保料は年間約50〜60万円（月4〜5万円）になることが多く、会社員時代より負担が大きくなるケースがほとんどです。</p>
        <h3>保険料を抑えるには</h3>
        <p>経費を漏れなく計上して所得を下げる、青色申告65万円控除を使う、法人化して社会保険に切り替える（所得が高い場合）などの方法があります。</p>
    </div>

    {footer(rl("/tool-58-freelance-income/","フリーランス年収シミュレーター") + rl("/tool-21-tax-simulator/","確定申告シミュレーター") + rl("/tool-22-withholding-tax/","源泉徴収税計算"))}
</div>
<script>
function calc() {{
    const income = parseInt(document.getElementById('income').value) || 0;
    const age = document.getElementById('age').value;
    const members = parseInt(document.getElementById('members').value) || 1;

    const base = Math.max(0, income - 430000); // 基礎控除43万

    // 概算料率（全国平均的な値）
    const medicalRate = 0.079, medicalFlat = 28000, medicalCap = 650000;
    const elderlyRate = 0.026, elderlyFlat = 9500, elderlyCap = 240000;
    const careRate = 0.023, careFlat = 12000, careCap = 170000;

    let medical = Math.min(Math.floor(base * medicalRate) + medicalFlat * members, medicalCap);
    let elderly = Math.min(Math.floor(base * elderlyRate) + elderlyFlat * members, elderlyCap);
    let care = 0;
    if (age === '40to64') {{
        care = Math.min(Math.floor(base * careRate) + careFlat * members, careCap);
    }}
    const flat = (medicalFlat + elderlyFlat + (age === '40to64' ? careFlat : 0)) * members;
    const total = medical + elderly + care;

    const f = n => n.toLocaleString();
    document.getElementById('rMedical').textContent = '\\u00a5' + f(medical);
    document.getElementById('rElderly').textContent = '\\u00a5' + f(elderly);
    document.getElementById('rCare').textContent = care > 0 ? '\\u00a5' + f(care) : '-（対象外）';
    document.getElementById('rFlat').textContent = '\\u00a5' + f(flat);
    document.getElementById('rTotal').textContent = '\\u00a5' + f(total);
    document.getElementById('rMonthly').textContent = '月額 \\u00a5' + f(Math.round(total / 12));
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 61: 個人事業税計算
# ============================================================
tool61 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>個人事業税計算ツール | フリーランスの事業税を自動計算【無料】</title>
    <meta name="description" content="フリーランス・個人事業主の個人事業税を自動計算する無料ツール。事業所得が290万円を超えると課税される個人事業税の概算額がわかる。業種ごとの税率（3%〜5%）に対応。">
    {FONT}
    <style>
{make_style("#6366f1","rgba(99,102,241,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-61-business-tax/">
    <meta property="og:title" content="個人事業税計算 | フリーランスの事業税を自動計算【無料】">
    <meta property="og:description" content="事業所得が290万超で課税される個人事業税を概算計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-61-business-tax/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="個人事業税計算ツール【無料】">
    <meta name="twitter:description" content="フリーランスの個人事業税を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"個人事業税計算ツール","description":"個人事業税を自動計算","url":"https://www.devtools-japan.com/tool-61-business-tax/","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>個人事業税計算</h1><p>フリーランスの事業税を自動計算</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>事業所得（売上−経費）</label><input type="number" id="income" value="5000000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>青色申告特別控除</label><select id="blue" onchange="calc()"><option value="650000" selected>65万円</option><option value="100000">10万円</option><option value="0">なし</option></select><span class="unit"></span></div>
        <div class="row"><label>業種</label><select id="biz" onchange="calc()">
            <option value="5" selected>第一種（5%）: コンサルタント、デザイン、ライター等</option>
            <option value="4">第二種（4%）: 畜産業、水産業等</option>
            <option value="3">第三種（3%）: 医師、弁護士、税理士等</option>
            <option value="0">非課税業種: プログラマー（※下記参照）</option>
        </select><span class="unit"></span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">事業所得</div><div class="value" id="rIncome">-</div></div>
        <div class="result-item"><div class="label">事業主控除</div><div class="value take" id="rDeduction">\\u00a52,900,000</div></div>
        <div class="result-item"><div class="label">課税所得</div><div class="value" id="rTaxable">-</div></div>
        <div class="result-item"><div class="label">税率</div><div class="value" id="rRate">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">個人事業税（年額）</div><div class="value tax" id="rTax" style="font-size:2rem">-</div><div class="sub" id="rNote"></div></div>
    </div>

    <div class="note">個人事業税は事業主控除290万円を超えた部分に課税されます。確定申告をすれば自動的に計算され、8月と11月に納付書が届きます。</div>

    <div class="card"><h3>ITフリーランスの事業税について</h3>
        <p style="font-size:0.85rem;color:var(--text2);line-height:2;margin:0">プログラマー・SE・エンジニアの業務内容が「請負」の場合は第一種事業（5%）に該当しますが、「システムエンジニア」として届出している場合は非課税（法定業種に該当しない）と判断される場合があります。ただし実態によって判断が分かれるため、税務署や税理士にご確認ください。コンサルティングやデザイン業務が含まれる場合は課税対象になることが多いです。</p>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>個人事業税計算ツールの使い方</h2>
        <p>フリーランス・個人事業主が納める個人事業税を概算計算する無料ツールです。事業所得が290万円（事業主控除額）を超えると課税され、業種に応じて3%〜5%の税率が適用されます。</p>
        <h3>個人事業税とは</h3>
        <p>個人事業税は都道府県に納める地方税です。所得税・住民税とは別に課税されます。確定申告を行えば自動的に計算され、8月と11月の年2回に分けて納付します。経費として計上可能（翌年の確定申告で控除）です。</p>
        <h3>事業主控除</h3>
        <p>全ての個人事業主に一律290万円の事業主控除が適用されます。そのため、事業所得が290万円以下であれば個人事業税はかかりません。なお、青色申告特別控除は個人事業税の計算では適用されない点に注意してください。</p>
        <h3>確定申告での扱い</h3>
        <p>納付した個人事業税は、翌年の確定申告で経費（租税公課）として計上できます。つまり、事業税を払った分だけ翌年の所得税・住民税が少なくなります。</p>
    </div>

    {footer(rl("/tool-58-freelance-income/","フリーランス年収シミュレーター") + rl("/tool-21-tax-simulator/","確定申告シミュレーター") + rl("/tool-60-nhi-calc/","国民健康保険料計算"))}
</div>
<script>
function calc() {{
    const income = parseInt(document.getElementById('income').value) || 0;
    const blue = parseInt(document.getElementById('blue').value) || 0;
    const rate = parseInt(document.getElementById('biz').value) || 0;

    // 個人事業税では青色申告控除は適用されないが、所得計算には反映済みの前提
    const deduction = 2900000;
    const taxable = Math.max(0, income - deduction);
    const tax = Math.floor(taxable * rate / 100);

    const f = n => n.toLocaleString();
    document.getElementById('rIncome').textContent = '\\u00a5' + f(income);
    document.getElementById('rTaxable').textContent = taxable > 0 ? '\\u00a5' + f(taxable) : '\\u00a50（290万以下）';
    document.getElementById('rRate').textContent = rate > 0 ? rate + '%' : '非課税';
    document.getElementById('rTax').textContent = rate > 0 && tax > 0 ? '\\u00a5' + f(tax) : '\\u00a50';
    document.getElementById('rNote').textContent = rate === 0 ? '非課税業種のため事業税はかかりません' : taxable <= 0 ? '事業主控除以下のため非課税' : '8月と11月に半額ずつ納付';
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# 書き出し
# ============================================================
tools = {
    "tool-58-freelance-income": tool58,
    "tool-59-depreciation": tool59,
    "tool-60-nhi-calc": tool60,
    "tool-61-business-tax": tool61,
}

print("=" * 60)
print("  DevTools Japan — フリーランス向けツール4本を生成")
print("=" * 60)

for dirname, content in tools.items():
    dirpath = os.path.join(BASE, dirname)
    os.makedirs(dirpath, exist_ok=True)
    filepath = os.path.join(dirpath, "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {dirname}")

# sitemap更新
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
    print("  ✅ sitemap.xml に4ツールを追加")

print("\n" + "=" * 60)
print("  完了！フリーランス向け4ツール生成 + sitemap更新")
print("=" * 60)
print()
print("デプロイ:")
print("  git add .")
print('  git commit -m "Add 4 freelance tools: 年収シミュレーター, 減価償却, 国保計算, 個人事業税"')
print("  git push")
