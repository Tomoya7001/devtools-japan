#!/usr/bin/env python3
import os, re
BASE = os.path.expanduser("~/Desktop/devtools-japan-complete")
print("="*50)
print("  SE/税金ツール(62-65) ポータル登録 + SEO")
print("="*50)

portal_path = os.path.join(BASE, "index.html")
with open(portal_path, "r", encoding="utf-8") as f:
    content = f.read()

new_tools_js = """,
    { id: 'subnet-calc', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 3h8v8H3V3zm10 0h8v8h-8V3zM3 13h8v8H3v-8zm15 0h-2v3h-3v2h3v3h2v-3h3v-2h-3v-3z"/></svg>', name: 'サブネット計算（CIDR）', desc: 'IPアドレス範囲・ネットマスク・ホスト数を自動計算', cat: 'utility', tags: ['サブネット','CIDR','ネットマスク','SE'], accent: '#2563eb', url: 'tool-62-subnet-calc/' },
    { id: 'mac-address', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM8 16H6v-2h2v2zm0-4H6v-2h2v2zm4 4h-2v-2h2v2zm0-4h-2v-2h2v2zm4 4h-2v-2h2v2zm0-4h-2v-2h2v2z"/></svg>', name: 'MACアドレス整形', desc: '区切り文字・大文字小文字を一括変換。キッティングに', cat: 'utility', tags: ['MACアドレス','キッティング','区切り文字','SE'], accent: '#0891b2', url: 'tool-63-mac-address/' },
    { id: 'take-home-pay', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1H6.5c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.88-4.4z"/></svg>', name: '手取り計算', desc: '年収・月給の額面から手取り額を自動計算', cat: 'freelance', tags: ['手取り','年収','給与','社会保険'], accent: '#16a34a', url: 'tool-64-take-home-pay/' },
    { id: 'consumption-tax', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 15h2c0 1.08 1.37 2 3 2s3-.92 3-2c0-1.1-1.04-1.64-3.24-2.16C9.64 12.32 7 11.49 7 8.5 7 6.57 8.6 4.95 11 4.34V2h2v2.34c2.4.61 4 2.23 4 4.16h-2c0-1.08-1.37-2-3-2s-3 .92-3 2c0 1.1 1.04 1.64 3.24 2.16C14.36 11.68 17 12.51 17 15.5c0 1.93-1.6 3.55-4 4.16V22h-2v-2.34c-2.4-.6-4-2.23-4-4.16z"/></svg>', name: '消費税計算', desc: '税込・税抜・内税・外税を一瞬で計算（10%/8%）', cat: 'utility', tags: ['消費税','税込','税抜','軽減税率'], accent: '#ea580c', url: 'tool-65-consumption-tax/' }"""

if "tool-62-subnet-calc" not in content:
    content = content.replace("url: 'tool-61-business-tax/' }\n];", "url: 'tool-61-business-tax/' }" + new_tools_js + "\n];")
    print("[1] OK 新4ツールをTOOLS配列に追加")
else:
    print("[1] -- 既に追加済み")

content = content.replace("全60+ツール無料・登録不要", "全65ツール無料・登録不要")
content = content.replace("無料オンラインツール60選", "無料オンラインツール65選")
content = content.replace("ツール60選", "ツール65選")
with open(portal_path, "w", encoding="utf-8") as f:
    f.write(content)
print("    ツール数表示を65に更新")

print("\n[2] クロスリンク追加中...")
CROSS = {
    "tool-31-ip-checker": [("/tool-62-subnet-calc/","サブネット計算"),("/tool-63-mac-address/","MACアドレス整形")],
    "tool-21-tax-simulator": [("/tool-64-take-home-pay/","手取り計算"),("/tool-65-consumption-tax/","消費税計算")],
}
tpl = '<a href="{}" style="padding:8px 16px;background:var(--bg);border:1px solid var(--border);border-radius:8px;color:var(--text2);text-decoration:none;font-size:0.8rem">{}</a>'
for td, links in CROSS.items():
    fp = os.path.join(BASE, td, "index.html")
    if not os.path.exists(fp):
        print(f"    -- {td} なし"); continue
    with open(fp,"r",encoding="utf-8") as f: tc = f.read()
    added = 0
    for href, text in links:
        if href not in tc:
            tc = tc.replace('</div>\n    </div>\n    <footer>', tpl.format(href,text)+'\n</div>\n    </div>\n    <footer>', 1)
            added += 1
    if added:
        with open(fp,"w",encoding="utf-8") as f: f.write(tc)
        print(f"    OK {td}: {added}リンク")

print("\n[3] SEO診断...")
ok = True
for num in range(62,66):
    m = [d for d in os.listdir(BASE) if d.startswith(f"tool-{num}-")]
    if not m: print(f"    NG tool-{num} なし"); ok=False; continue
    with open(os.path.join(BASE,m[0],"index.html"),"r",encoding="utf-8") as f: tc=f.read()
    head = re.search(r'<head[^>]*>(.*?)</head>', tc, re.DOTALL)
    head = head.group(1) if head else ""
    iss = [l for k,l in [('G-E27Q8YTG7L','GA4'),('ca-pub-7300747004702072','AdSense'),('favicon.svg','favicon'),('<title>','title'),('name="description"','desc'),('rel="canonical"','canonical'),('og:title','og'),('twitter:card','twitter'),('application/ld+json','JSON-LD')] if k not in head]
    if 'seo-content' not in tc: iss.append('SEOテキスト')
    if '関連ツール' not in tc: iss.append('関連ツール')
    print(f"    {'OK' if not iss else 'NG'} {m[0]}: {'全項目クリア' if not iss else ', '.join(iss)}")
    if iss: ok=False
print("\n>> 完璧" if ok else "\n>> 要確認")
print("\nデプロイ: git add . && git commit -m 'Register 4 SE/tax tools in portal' && git push")
