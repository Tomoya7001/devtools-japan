import os, re
BASE = os.path.expanduser("~/Desktop/devtools-japan-complete")

# [1] sitemap登録
sp = os.path.join(BASE, "sitemap.xml")
with open(sp, "r", encoding="utf-8") as f: sm = f.read()
url = "https://www.devtools-japan.com/tool-70-zip-password/"
if url not in sm:
    sm = sm.replace("</urlset>", '  <url>\n    <loc>'+url+'</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n</urlset>')
    with open(sp, "w", encoding="utf-8") as f: f.write(sm)
    print("[1] OK sitemap登録")
else:
    print("[1] -- sitemap既存")

# [2] ポータル登録
pp = os.path.join(BASE, "index.html")
with open(pp, "r", encoding="utf-8") as f: c = f.read()
newjs = """,
    { id: 'zip-password', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>', name: 'パスワード付きZIP作成', desc: 'ファイルを選んで暗号化ZIPを作成。AES-256/ZipCrypto対応', cat: 'utility', tags: ['zip','パスワード','暗号化','圧縮'], accent: '#475569', url: 'tool-70-zip-password/' }"""
if "tool-70-zip-password" not in c:
    c = c.replace("url: 'tool-69-currency-calc/' }\n];", "url: 'tool-69-currency-calc/' }" + newjs + "\n];")
    print("[2] OK ポータルTOOLS配列に追加")
else:
    print("[2] -- ポータル既存")
c = c.replace("全69ツール無料・登録不要", "全70ツール無料・登録不要")
c = c.replace("無料オンラインツール69選", "無料オンラインツール70選")
c = c.replace("ツール69選", "ツール70選")
with open(pp, "w", encoding="utf-8") as f: f.write(c)
print("    ツール数表示を70に更新")

# [3] SEO診断
fp = os.path.join(BASE, "tool-70-zip-password", "index.html")
with open(fp, "r", encoding="utf-8") as f: tc = f.read()
head = re.search(r'<head[^>]*>(.*?)</head>', tc, re.DOTALL).group(1)
iss = [l for k,l in [('G-E27Q8YTG7L','GA4'),('ca-pub-7300747004702072','AdSense'),('favicon.svg','favicon'),('<title>','title'),('name="description"','desc'),('rel="canonical"','canonical'),('og:title','og'),('twitter:card','twitter')] if k not in head]
if 'seo-content' not in tc: iss.append('SEOテキスト')
if '関連ツール' not in tc: iss.append('関連ツール')
print("[3] SEO診断: " + ("全項目クリア" if not iss else ", ".join(iss)))
print("\nデプロイ: git add . && git commit -m 'Add password-protected ZIP tool (tool-70)' && git push")
