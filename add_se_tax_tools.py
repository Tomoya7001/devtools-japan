#!/usr/bin/env python3
"""
DevTools Japan — SE/キッティング向け2本 + 税金向け2本を追加
tool-62〜tool-65
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
        .mono-out{{font-family:'JetBrains Mono',monospace;background:#f7f8fb;border:1px solid var(--border);border-radius:8px;padding:12px 14px;font-size:0.95rem;color:var(--accent);word-break:break-all;cursor:pointer}}
        .seo-content{{margin-top:40px;padding:28px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);color:var(--text2);font-size:0.85rem;line-height:2}}
        .seo-content h2{{color:var(--text);font-size:1.05rem;margin-bottom:12px}}.seo-content h3{{color:var(--text);font-size:0.95rem;margin-top:20px;margin-bottom:8px}}.seo-content p{{margin-bottom:10px}}
        footer{{text-align:center;margin-top:48px;padding-top:20px;border-top:1px solid var(--border);color:var(--text3);font-size:0.75rem}}
        .note{{background:var(--accent-dim);border:1px solid rgba(0,0,0,0.06);border-radius:8px;padding:12px 16px;font-size:0.75rem;color:var(--text2);margin-bottom:24px}}
        table.ref{{width:100%;border-collapse:collapse;margin:16px 0;font-size:0.8rem}}
        table.ref th{{background:var(--bg);border:1px solid var(--border);padding:8px 12px;text-align:left;font-weight:600;color:var(--text)}}
        table.ref td{{border:1px solid var(--border);padding:8px 12px;color:var(--text2)}}
        .btn{{padding:8px 18px;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:0.85rem;font-weight:600;cursor:pointer;font-family:'Noto Sans JP',sans-serif}}"""

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
# Tool 62: サブネット計算（CIDR）
# ============================================================
tool62 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>サブネット計算ツール（CIDR計算） | IPアドレス範囲・ネットマスク・ホスト数を自動計算【無料】</title>
    <meta name="description" content="CIDR表記からネットワークアドレス・ブロードキャストアドレス・使用可能IP範囲・ホスト数・サブネットマスクを自動計算する無料ツール。ネットワーク設計、サーバー構築、インフラ設定に。SE・インフラエンジニア必携。">
    {FONT}
    <style>
{make_style("#2563eb","rgba(37,99,235,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-62-subnet-calc/">
    <meta property="og:title" content="サブネット計算ツール（CIDR） | IP範囲・ホスト数を自動計算【無料】">
    <meta property="og:description" content="CIDRからネットワークアドレス・IP範囲・ホスト数・サブネットマスクを計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-62-subnet-calc/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="サブネット計算ツール（CIDR）【無料】">
    <meta name="twitter:description" content="CIDRからIP範囲・ホスト数・サブネットマスクを自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"サブネット計算ツール（CIDR計算）","description":"CIDRからネットワークアドレス・IP範囲・ホスト数を計算","url":"https://www.devtools-japan.com/tool-62-subnet-calc/","applicationCategory":"DeveloperApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>サブネット計算（CIDR）</h1><p>IPアドレス範囲・ネットマスク・ホスト数を自動計算</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>IPアドレス</label><input type="text" id="ip" value="192.168.1.0" oninput="calc()"></div>
        <div class="row"><label>プレフィックス（CIDR）</label><select id="cidr" onchange="calc()">
        </select><span class="unit"></span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">ネットワークアドレス</div><div class="value" id="rNetwork">-</div></div>
        <div class="result-item"><div class="label">ブロードキャストアドレス</div><div class="value" id="rBroadcast">-</div></div>
        <div class="result-item"><div class="label">サブネットマスク</div><div class="value" id="rMask">-</div></div>
        <div class="result-item"><div class="label">ワイルドカードマスク</div><div class="value" id="rWildcard">-</div></div>
        <div class="result-item"><div class="label">使用可能IP範囲</div><div class="value" id="rRange" style="font-size:1rem">-</div></div>
        <div class="result-item"><div class="label">使用可能ホスト数</div><div class="value take" id="rHosts">-</div></div>
    </div>

    <div class="note">使用可能ホスト数は、ネットワークアドレスとブロードキャストアドレスを除いた数です（/31, /32 は特殊扱い）。</div>

    <div class="card"><h3>よく使うCIDRとホスト数</h3>
        <table class="ref">
            <tr><th>CIDR</th><th>サブネットマスク</th><th>使用可能ホスト数</th></tr>
            <tr><td>/24</td><td>255.255.255.0</td><td>254</td></tr>
            <tr><td>/25</td><td>255.255.255.128</td><td>126</td></tr>
            <tr><td>/26</td><td>255.255.255.192</td><td>62</td></tr>
            <tr><td>/27</td><td>255.255.255.224</td><td>30</td></tr>
            <tr><td>/28</td><td>255.255.255.240</td><td>14</td></tr>
            <tr><td>/29</td><td>255.255.255.248</td><td>6</td></tr>
            <tr><td>/30</td><td>255.255.255.252</td><td>2</td></tr>
        </table>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>サブネット計算ツール（CIDR計算）の使い方</h2>
        <p>IPアドレスとCIDRプレフィックス（/24など）を入力するだけで、ネットワークアドレス、ブロードキャストアドレス、サブネットマスク、使用可能なIPアドレスの範囲、ホスト数を自動計算する無料ツールです。ネットワーク設計、サーバー構築、ファイアウォール設定で必須の計算を瞬時に行えます。</p>
        <h3>CIDR表記とは</h3>
        <p>CIDR（Classless Inter-Domain Routing）は、IPアドレスとサブネットマスクを「192.168.1.0/24」のように表記する方法です。/24はサブネットマスクの先頭24ビットが1であることを意味し、255.255.255.0と同じです。プレフィックスが大きいほどネットワークが小さく（ホスト数が少なく）なります。</p>
        <h3>SE・インフラエンジニアの実務で</h3>
        <p>VPCのサブネット設計、ロードバランサーの設定、ファイアウォールのIP許可範囲の指定、ルーティングテーブルの設定など、ネットワークを扱うあらゆる場面で使います。「/26だと何台のサーバーを収容できる？」「このIPはどのネットワークに属する？」を即座に確認できます。</p>
        <h3>プライバシー</h3>
        <p>すべての計算はブラウザ内で完結します。入力したIPアドレスがサーバーに送信されることはありません。</p>
    </div>

    {footer(rl("/tool-31-ip-checker/","IPアドレス確認") + rl("/tool-63-mac-address/","MACアドレス整形") + rl("/tool-37-number-base/","進数変換"))}
</div>
<script>
const cidrSel = document.getElementById('cidr');
for (let i = 8; i <= 32; i++) {{
    const opt = document.createElement('option');
    opt.value = i; opt.textContent = '/' + i;
    if (i === 24) opt.selected = true;
    cidrSel.appendChild(opt);
}}

function ipToInt(ip) {{
    const parts = ip.split('.').map(Number);
    if (parts.length !== 4 || parts.some(p => isNaN(p) || p < 0 || p > 255)) return null;
    return ((parts[0] << 24) >>> 0) + (parts[1] << 16) + (parts[2] << 8) + parts[3];
}}
function intToIp(int) {{
    return [(int >>> 24) & 255, (int >>> 16) & 255, (int >>> 8) & 255, int & 255].join('.');
}}

function calc() {{
    const ip = document.getElementById('ip').value.trim();
    const cidr = parseInt(document.getElementById('cidr').value);
    const ipInt = ipToInt(ip);
    if (ipInt === null) {{
        document.getElementById('rNetwork').textContent = '不正なIP';
        return;
    }}
    const mask = cidr === 0 ? 0 : (0xFFFFFFFF << (32 - cidr)) >>> 0;
    const network = (ipInt & mask) >>> 0;
    const broadcast = (network | (~mask >>> 0)) >>> 0;
    const wildcard = (~mask) >>> 0;

    let hosts, firstIp, lastIp;
    if (cidr === 32) {{
        hosts = 1; firstIp = lastIp = intToIp(network);
    }} else if (cidr === 31) {{
        hosts = 2; firstIp = intToIp(network); lastIp = intToIp(broadcast);
    }} else {{
        hosts = broadcast - network - 1;
        firstIp = intToIp(network + 1);
        lastIp = intToIp(broadcast - 1);
    }}

    document.getElementById('rNetwork').textContent = intToIp(network);
    document.getElementById('rBroadcast').textContent = intToIp(broadcast);
    document.getElementById('rMask').textContent = intToIp(mask);
    document.getElementById('rWildcard').textContent = intToIp(wildcard);
    document.getElementById('rRange').textContent = firstIp + ' 〜 ' + lastIp;
    document.getElementById('rHosts').textContent = hosts.toLocaleString() + '台';
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 63: MACアドレス整形
# ============================================================
tool63 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>MACアドレス整形・変換ツール | 区切り文字変換・大文字小文字・形式統一【無料】</title>
    <meta name="description" content="MACアドレスの区切り文字（コロン・ハイフン・ドット・なし）変換、大文字小文字の統一を一括で行う無料ツール。キッティング作業、資産管理台帳の整形、ネットワーク機器の設定に。複数行の一括変換対応。">
    {FONT}
    <style>
{make_style("#0891b2","rgba(8,145,178,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-63-mac-address/">
    <meta property="og:title" content="MACアドレス整形・変換ツール | 区切り文字・大文字小文字を統一【無料】">
    <meta property="og:description" content="MACアドレスの区切り文字変換・大文字小文字統一を一括処理">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-63-mac-address/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="MACアドレス整形・変換ツール【無料】">
    <meta name="twitter:description" content="MACアドレスの区切り文字・大文字小文字を一括変換">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"MACアドレス整形・変換ツール","description":"MACアドレスの区切り文字・大文字小文字を変換","url":"https://www.devtools-japan.com/tool-63-mac-address/","applicationCategory":"DeveloperApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>MACアドレス整形・変換</h1><p>区切り文字・大文字小文字を一括変換</p></header>

    <div class="card"><h3>設定</h3>
        <div class="row"><label>区切り文字</label><select id="sep" onchange="calc()">
            <option value=":" selected>コロン区切り（AA:BB:CC:DD:EE:FF）</option>
            <option value="-">ハイフン区切り（AA-BB-CC-DD-EE-FF）</option>
            <option value=".">ドット区切り（AABB.CCDD.EEFF）</option>
            <option value="">区切りなし（AABBCCDDEEFF）</option>
        </select><span class="unit"></span></div>
        <div class="row"><label>大文字小文字</label><select id="case" onchange="calc()">
            <option value="upper" selected>大文字（AA:BB:CC）</option>
            <option value="lower">小文字（aa:bb:cc）</option>
        </select><span class="unit"></span></div>
    </div>

    <div class="card"><h3>入力（複数行可・1行1MACアドレス）</h3>
        <textarea id="input" oninput="calc()" style="width:100%;min-height:120px;padding:12px;background:#f7f8fb;border:1px solid var(--border);border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:var(--text);outline:none;resize:vertical">00:1A:2B:3C:4D:5E
AABBCCDDEEFF
a0-b1-c2-d3-e4-f5</textarea>
    </div>

    <div class="card"><h3>変換結果</h3>
        <textarea id="output" readonly style="width:100%;min-height:120px;padding:12px;background:var(--accent-dim);border:1px solid var(--border);border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:var(--accent);outline:none;resize:vertical"></textarea>
        <button class="btn" onclick="copyOut()" style="margin-top:12px">結果をコピー</button>
        <span id="copied" style="font-size:0.8rem;color:var(--green);margin-left:12px"></span>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>MACアドレス整形・変換ツールの使い方</h2>
        <p>MACアドレスの区切り文字（コロン・ハイフン・ドット・区切りなし）と大文字小文字を一括変換する無料ツールです。キッティング作業、IT資産管理台帳の整形、ネットワーク機器の設定など、MACアドレスの形式を統一したい場面で活躍します。複数行をまとめて一括変換できます。</p>
        <h3>MACアドレスの表記ゆれ問題</h3>
        <p>MACアドレスは機器やOSによって表記が異なります。Windowsはハイフン区切り（AA-BB-CC-DD-EE-FF）、Linux/Macはコロン区切り（aa:bb:cc:dd:ee:ff）、Cisco機器はドット区切り（aabb.ccdd.eeff）が一般的です。資産管理台帳に登録する際、これらの表記を統一する必要があります。</p>
        <h3>キッティング作業での活用</h3>
        <p>大量のPCやネットワーク機器をセットアップするキッティング作業では、各機器のMACアドレスを収集して管理台帳に記録します。収集したMACアドレスの区切り文字がバラバラだと管理しにくいため、このツールで一括統一できます。DHCP予約やMACアドレスフィルタリングの設定時にも便利です。</p>
        <h3>プライバシー</h3>
        <p>すべての変換はブラウザ内で完結します。入力したMACアドレスがサーバーに送信されることはありません。</p>
    </div>

    {footer(rl("/tool-62-subnet-calc/","サブネット計算") + rl("/tool-31-ip-checker/","IPアドレス確認") + rl("/tool-15-case-converter/","文字列ケース変換"))}
</div>
<script>
function calc() {{
    const sep = document.getElementById('sep').value;
    const caseType = document.getElementById('case').value;
    const lines = document.getElementById('input').value.split('\\n');
    const out = lines.map(line => {{
        const hex = line.replace(/[^0-9a-fA-F]/g, '');
        if (hex.length !== 12) return line.trim() ? '（不正: ' + line.trim() + '）' : '';
        let h = caseType === 'upper' ? hex.toUpperCase() : hex.toLowerCase();
        if (sep === '.') {{
            return h.match(/.{{4}}/g).join('.');
        }} else if (sep === '') {{
            return h;
        }} else {{
            return h.match(/.{{2}}/g).join(sep);
        }}
    }}).join('\\n');
    document.getElementById('output').value = out;
}}
function copyOut() {{
    const out = document.getElementById('output');
    out.select();
    navigator.clipboard.writeText(out.value);
    document.getElementById('copied').textContent = 'コピーしました';
    setTimeout(() => document.getElementById('copied').textContent = '', 2000);
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 64: 手取り計算（給与額面→手取り）
# ============================================================
tool64 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>手取り計算ツール | 年収・月給の額面から手取り額を自動計算【無料】</title>
    <meta name="description" content="会社員の年収・月給の額面から、社会保険料・所得税・住民税を差し引いた手取り額を自動計算する無料ツール。額面と手取りの違いを把握。転職・年収交渉・家計管理に。">
    {FONT}
    <style>
{make_style("#16a34a","rgba(22,163,74,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-64-take-home-pay/">
    <meta property="og:title" content="手取り計算ツール | 年収・月給の額面から手取りを計算【無料】">
    <meta property="og:description" content="額面から社会保険料・所得税・住民税を引いた手取り額を自動計算">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-64-take-home-pay/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="手取り計算ツール【無料】">
    <meta name="twitter:description" content="年収・月給の額面から手取り額を自動計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"手取り計算ツール","description":"年収・月給の額面から手取り額を計算","url":"https://www.devtools-japan.com/tool-64-take-home-pay/","applicationCategory":"FinanceApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>手取り計算</h1><p>年収・月給の額面から手取り額を自動計算</p></header>
    <div class="note">会社員（給与所得者）向けの概算計算です。協会けんぽ・東京都の料率をベースにしています。実際の手取りは扶養人数・地域・会社の制度により異なります。</div>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>額面年収（総支給）</label><input type="number" id="income" value="5000000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>年齢</label><select id="age" onchange="calc()"><option value="under40" selected>40歳未満</option><option value="40over">40歳以上（介護保険あり）</option></select><span class="unit"></span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">健康保険料</div><div class="value tax" id="rHealth">-</div></div>
        <div class="result-item"><div class="label">厚生年金保険料</div><div class="value tax" id="rPension">-</div></div>
        <div class="result-item"><div class="label">雇用保険料</div><div class="value tax" id="rEmployment">-</div></div>
        <div class="result-item"><div class="label">所得税</div><div class="value tax" id="rIncomeTax">-</div></div>
        <div class="result-item"><div class="label">住民税</div><div class="value tax" id="rResTax">-</div></div>
        <div class="result-item"><div class="label">社会保険料合計</div><div class="value tax" id="rSocial">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item"><div class="label">年間手取り</div><div class="value take" id="rTakeHome" style="font-size:1.8rem">-</div></div>
        <div class="result-item"><div class="label">月間手取り（目安）</div><div class="value take" id="rMonthly" style="font-size:1.8rem">-</div></div>
    </div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>手取り計算ツールの使い方</h2>
        <p>会社員の額面年収（総支給額）から、健康保険料・厚生年金・雇用保険・所得税・住民税を差し引いた「手取り額」を自動計算する無料ツールです。求人票や年収交渉で提示される「額面」と、実際に銀行口座に振り込まれる「手取り」の違いを把握できます。</p>
        <h3>額面と手取りの違い</h3>
        <p>額面年収は税金や社会保険料が引かれる前の総支給額です。実際の手取りは額面の約75〜85%になります。年収が高くなるほど税率が上がるため、手取りの割合は下がっていきます。一般的に、年収500万円なら手取りは約390万円程度です。</p>
        <h3>引かれるもの</h3>
        <p>給与から引かれるのは、健康保険料（約5%）、厚生年金保険料（約9.15%）、雇用保険料（0.6%）、所得税（累進）、住民税（約10%）です。社会保険料は会社が半分を負担しているため、給与明細に記載される金額は本来の半額です。</p>
        <h3>転職・年収交渉に</h3>
        <p>転職時に提示される年収はほとんどが額面です。「額面600万円」が実際にどれくらいの手取りになるかを事前に把握しておくと、生活設計が立てやすくなります。</p>
    </div>

    {footer(rl("/tool-21-tax-simulator/","確定申告シミュレーター") + rl("/tool-65-consumption-tax/","消費税計算") + rl("/tool-58-freelance-income/","フリーランス年収シミュレーター"))}
</div>
<script>
function calc() {{
    const income = parseInt(document.getElementById('income').value) || 0;
    const age = document.getElementById('age').value;

    // 社会保険料（協会けんぽ・東京都2024年度ベースの概算）
    const healthRate = age === '40over' ? 0.0582 : 0.0499; // 介護保険含む/含まない（折半後）
    const health = Math.floor(income * healthRate);
    const pension = Math.floor(income * 0.0915); // 厚生年金（折半後）
    const employment = Math.floor(income * 0.006); // 雇用保険
    const social = health + pension + employment;

    // 給与所得控除
    let salaryDeduction;
    if (income <= 1625000) salaryDeduction = 550000;
    else if (income <= 1800000) salaryDeduction = income * 0.4 - 100000;
    else if (income <= 3600000) salaryDeduction = income * 0.3 + 80000;
    else if (income <= 6600000) salaryDeduction = income * 0.2 + 440000;
    else if (income <= 8500000) salaryDeduction = income * 0.1 + 1100000;
    else salaryDeduction = 1950000;

    // 課税所得（基礎控除48万 + 社会保険料控除）
    const taxableIncome = Math.max(0, income - salaryDeduction - 480000 - social);

    // 所得税
    let incomeTax = 0;
    if (taxableIncome <= 1950000) incomeTax = taxableIncome * 0.05;
    else if (taxableIncome <= 3300000) incomeTax = taxableIncome * 0.10 - 97500;
    else if (taxableIncome <= 6950000) incomeTax = taxableIncome * 0.20 - 427500;
    else if (taxableIncome <= 9000000) incomeTax = taxableIncome * 0.23 - 636000;
    else if (taxableIncome <= 18000000) incomeTax = taxableIncome * 0.33 - 1536000;
    else incomeTax = taxableIncome * 0.40 - 2796000;
    incomeTax = Math.floor(incomeTax * 1.021);

    // 住民税（課税所得の10% + 均等割）。住民税の基礎控除は43万なので再計算
    const resTaxable = Math.max(0, income - salaryDeduction - 430000 - social);
    const resTax = Math.floor(resTaxable * 0.10) + 5000;

    const takeHome = income - social - incomeTax - resTax;

    const f = n => '\\u00a5' + Math.max(0, n).toLocaleString();
    document.getElementById('rHealth').textContent = f(health);
    document.getElementById('rPension').textContent = f(pension);
    document.getElementById('rEmployment').textContent = f(employment);
    document.getElementById('rIncomeTax').textContent = f(incomeTax);
    document.getElementById('rResTax').textContent = f(resTax);
    document.getElementById('rSocial').textContent = f(social);
    document.getElementById('rTakeHome').textContent = f(takeHome);
    document.getElementById('rMonthly').textContent = f(Math.floor(takeHome / 12));
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# Tool 65: 消費税計算
# ============================================================
tool65 = f'''<!DOCTYPE html>
<html lang="ja">
<head>
{COMMON_HEAD}
    <title>消費税計算ツール | 税込・税抜・内税・外税を一瞬で計算【無料・10%/8%対応】</title>
    <meta name="description" content="金額から消費税を計算する無料ツール。税抜→税込、税込→税抜の両方向、内税・外税、10%・8%軽減税率に対応。請求書作成、経理、買い物の計算に。">
    {FONT}
    <style>
{make_style("#ea580c","rgba(234,88,12,0.08)")}
    </style>
    <link rel="canonical" href="https://www.devtools-japan.com/tool-65-consumption-tax/">
    <meta property="og:title" content="消費税計算ツール | 税込・税抜を一瞬で計算【無料・10%/8%対応】">
    <meta property="og:description" content="税抜→税込、税込→税抜の両方向。10%・8%軽減税率に対応">
    <meta property="og:url" content="https://www.devtools-japan.com/tool-65-consumption-tax/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="消費税計算ツール【無料・10%/8%対応】">
    <meta name="twitter:description" content="税込・税抜・内税・外税を一瞬で計算">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"消費税計算ツール","description":"税込・税抜・消費税額を計算","url":"https://www.devtools-japan.com/tool-65-consumption-tax/","applicationCategory":"FinanceApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"JPY"}},"provider":{{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}}}
    </script>
</head>
<body>
{NAV}
<div class="container">
    <div class="ad-slot"></div>
    <header><h1>消費税計算</h1><p>税込・税抜・内税・外税を一瞬で計算</p></header>

    <div class="card"><h3>入力</h3>
        <div class="row"><label>金額</label><input type="number" id="amount" value="10000" oninput="calc()"><span class="unit">円</span></div>
        <div class="row"><label>入力した金額は</label><select id="type" onchange="calc()">
            <option value="exclude" selected>税抜価格（この金額に税を足す）</option>
            <option value="include">税込価格（この金額から税を抜く）</option>
        </select><span class="unit"></span></div>
        <div class="row"><label>税率</label><select id="rate" onchange="calc()">
            <option value="0.10" selected>10%（標準税率）</option>
            <option value="0.08">8%（軽減税率・食品等）</option>
        </select><span class="unit"></span></div>
    </div>

    <div class="result-grid">
        <div class="result-item"><div class="label">税抜価格</div><div class="value" id="rExclude" style="font-size:1.6rem">-</div></div>
        <div class="result-item"><div class="label">消費税額</div><div class="value tax" id="rTax" style="font-size:1.6rem">-</div></div>
    </div>
    <div class="result-grid">
        <div class="result-item" style="grid-column:1/-1"><div class="label">税込価格</div><div class="value take" id="rInclude" style="font-size:2.2rem">-</div></div>
    </div>

    <div class="note">消費税の端数処理は事業者によって異なります（切り捨て・切り上げ・四捨五入）。このツールは切り捨てで計算しています。</div>

    <div class="ad-slot"></div>

    <div class="seo-content">
        <h2>消費税計算ツールの使い方</h2>
        <p>金額から消費税を計算する無料ツールです。税抜価格から税込価格を求める（外税）、税込価格から税抜価格と消費税額を求める（内税）の両方向に対応しています。10%の標準税率と8%の軽減税率を切り替えられます。</p>
        <h3>外税と内税</h3>
        <p>外税は「税抜価格 + 消費税」で表示する方式で、税抜10,000円なら税込11,000円になります。内税は税込価格から逆算する方式で、税込11,000円の商品の税抜価格は10,000円、消費税額は1,000円です。請求書や見積書の作成、レシートの検算に使えます。</p>
        <h3>軽減税率（8%）</h3>
        <p>2019年10月の消費税増税時に導入された軽減税率は、飲食料品（酒類・外食を除く）と定期購読の新聞に適用されます。テイクアウトは8%、店内飲食は10%といった違いがあるため、飲食業の経理では両方の計算が必要です。</p>
        <h3>こんな場面で使えます</h3>
        <p>請求書・見積書の作成、経理の検算、確定申告の集計、買い物の合計金額の確認、税抜価格表示の商品の支払総額の計算など。すべてブラウザ上で計算され、データがサーバーに送信されることはありません。</p>
    </div>

    {footer(rl("/tool-52-invoice-calc/","請求書金額計算") + rl("/tool-64-take-home-pay/","手取り計算") + rl("/tool-21-tax-simulator/","確定申告シミュレーター"))}
</div>
<script>
function calc() {{
    const amount = parseInt(document.getElementById('amount').value) || 0;
    const type = document.getElementById('type').value;
    const rate = parseFloat(document.getElementById('rate').value);

    let exclude, tax, include;
    if (type === 'exclude') {{
        exclude = amount;
        tax = Math.floor(amount * rate);
        include = exclude + tax;
    }} else {{
        include = amount;
        exclude = Math.floor(amount / (1 + rate));
        tax = include - exclude;
    }}

    const f = n => '\\u00a5' + n.toLocaleString();
    document.getElementById('rExclude').textContent = f(exclude);
    document.getElementById('rTax').textContent = f(tax);
    document.getElementById('rInclude').textContent = f(include);
}}
calc();
</script>
</body>
</html>'''


# ============================================================
# 書き出し
# ============================================================
tools = {
    "tool-62-subnet-calc": tool62,
    "tool-63-mac-address": tool63,
    "tool-64-take-home-pay": tool64,
    "tool-65-consumption-tax": tool65,
}

print("=" * 60)
print("  DevTools Japan — SE/税金向けツール4本を生成")
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

print("\n完了！SE/税金向け4ツール生成 + sitemap更新")
print("\nデプロイ:")
print("  git add .")
print('  git commit -m "Add 4 SE/tax tools: subnet calc, MAC address, take-home pay, consumption tax"')
print("  git push")
