#!/usr/bin/env python3
"""
DevTools Japan — 税金・お金系新4ツール(66-69)のポータル登録 + SEO
"""
import os, re

BASE = "/Users/tom/Desktop/devtools-japan-complete"

print("=" * 50)
print("  税金・お金系ツール(66-69) ポータル登録 + SEO")
print("=" * 50)

# [1] ポータルのTOOLS配列に追加
print("\n[1] ポータルに新4ツールを追加中...")
portal_path = os.path.join(BASE, "index.html")
with open(portal_path, "r", encoding="utf-8") as f:
    content = f.read()

new_tools_js = """,
    { id: 'furusato-tax', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 6h-2.18c.11-.31.18-.65.18-1a2.996 2.996 0 00-5.5-1.65l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z"/></svg>', name: 'ふるさと納税 上限額シミュレーター', desc: '年収と家族構成から控除上限額を概算計算', cat: 'freelance', tags: ['ふるさと納税','上限額','控除','節税'], accent: '#e11d48', url: 'tool-66-furusato-tax/' },
    { id: 'wage-converter', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7.5 21H2V9h5.5v12zm7.25-18h-5.5v18h5.5V3zM22 11h-5.5v10H22V11z"/></svg>', name: '時給・月給・年収 換算', desc: '時給⇔月給⇔年収を相互に自動換算', cat: 'freelance', tags: ['時給','月給','年収','換算'], accent: '#7c3aed', url: 'tool-67-wage-converter/' },
    { id: 'invoice-tax', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>', name: 'インボイス消費税計算', desc: '適格請求書の税率ごとの消費税額・端数処理を計算', cat: 'utility', tags: ['インボイス','適格請求書','消費税','端数処理'], accent: '#0d9488', url: 'tool-68-invoice-tax/' },
    { id: 'currency-calc', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>', name: '為替計算', desc: 'レートを入力して外貨⇔円を相互換算（手数料対応）', cat: 'utility', tags: ['為替','ドル円','外貨','換算'], accent: '#2563eb', url: 'tool-69-currency-calc/' }"""

if "tool-66-furusato-tax" not in content:
    content = content.replace(
        "url: 'tool-65-consumption-tax/' }\n];",
        "url: 'tool-65-consumption-tax/' }" + new_tools_js + "\n];"
    )
    print("  OK 新4ツールをTOOLS配列に追加")
else:
    print("  -- 既に追加済み")

content = content.replace("全65ツール無料・登録不要", "全69ツール無料・登録不要")
content = content.replace("無料オンラインツール65選", "無料オンラインツール69選")
content = content.replace("ツール65選", "ツール69選")
with open(portal_path, "w", encoding="utf-8") as f:
    f.write(content)
print("  OK ツール数表示を69に更新")

# [2] クロスリンク
print("\n[2] クロスリンク追加中...")
CROSS = {
    "tool-64-take-home-pay": [("/tool-66-furusato-tax/","ふるさと納税上限額"),("/tool-67-wage-converter/","時給・月給・年収換算")],
    "tool-65-consumption-tax": [("/tool-68-invoice-tax/","インボイス消費税計算"),("/tool-69-currency-calc/","為替計算")],
}
tpl = '<a href="{}" style="padding:8px 16px;background:var(--bg);border:1px solid var(--border);border-radius:8px;color:var(--text2);text-decoration:none;font-size:0.8rem">{}</a>'
for td, links in CROSS.items():
    fp = os.path.join(BASE, td, "index.html")
    if not os.path.exists(fp):
        print(f"  -- {td} なし"); continue
    with open(fp,"r",encoding="utf-8") as f: tc = f.read()
    added = 0
    for href, text in links:
        if href not in tc:
            tc = tc.replace('</div>\n    </div>\n    <footer>', tpl.format(href,text)+'\n</div>\n    </div>\n    <footer>', 1)
            added += 1
    if added:
        with open(fp,"w",encoding="utf-8") as f: f.write(tc)
        print(f"  OK {td}: {added}リンク")

# [3] SEO診断
print("\n[3] SEO診断...")
ok = True
for num in range(66,70):
    m = [d for d in os.listdir(BASE) if d.startswith(f"tool-{num}-")]
    if not m: print(f"  NG tool-{num} なし"); ok=False; continue
    with open(os.path.join(BASE,m[0],"index.html"),"r",encoding="utf-8") as f: tc=f.read()
    head = re.search(r'<head[^>]*>(.*?)</head>', tc, re.DOTALL)
    head = head.group(1) if head else ""
    iss = [l for k,l in [('G-E27Q8YTG7L','GA4'),('ca-pub-7300747004702072','AdSense'),('favicon.svg','favicon'),('<title>','title'),('name="description"','desc'),('rel="canonical"','canonical'),('og:title','og'),('twitter:card','twitter'),('application/ld+json','JSON-LD')] if k not in head]
    if 'seo-content' not in tc: iss.append('SEOテキスト')
    if '関連ツール' not in tc: iss.append('関連ツール')
    print(f"  {'OK' if not iss else 'NG'} {m[0]}: {'全項目クリア' if not iss else ', '.join(iss)}")
    if iss: ok=False
print("\n>> 完璧" if ok else "\n>> 要確認")
print("\nデプロイ: git add . && git commit -m 'Add 4 money tools (furusato/wage/invoice/currency) + portal' && git push")
