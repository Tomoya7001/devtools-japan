#!/usr/bin/env python3
"""
DevTools Japan — 新ツール11本のポータル登録 + SEO強化
1. ポータル index.html に新ツール11本を追加
2. 新カテゴリ「ビジネス」「フリーランス」を追加
3. ツール数表示を50→60+に更新
4. タイトル・descriptionを更新
5. 既存ツールから新ツールへのクロスリンク追加
"""
import os, re

BASE = "/Users/tom/Desktop/devtools-japan-complete"

# ============================================================
# 1. ポータルに新ツール11本 + 新カテゴリを追加
# ============================================================
print("📋 1. ポータルに新ツール11本を追加中...")

portal_path = os.path.join(BASE, "index.html")
with open(portal_path, "r", encoding="utf-8") as f:
    content = f.read()

# 新ツールのJS配列要素
new_tools_js = """,
    { id: 'business-day', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3h-1V1h-2v2H8V1H6v2H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm0 16H5V8h14v11zM9 10H7v2h2v-2zm4 0h-2v2h2v-2zm4 0h-2v2h2v-2z"/></svg>', name: '営業日計算', desc: '土日祝を除いたN営業日後の日付・期間の営業日数を計算', cat: 'business', tags: ['営業日','納期','届出期限','祝日'], accent: '#3b82f6', url: 'tool-51-business-day-calc/' },
    { id: 'invoice-calc', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6zm-1 2l5 5h-5V4zM8 13h2v2H8v-2zm0 4h2v2H8v-2zm4-4h4v2h-4v-2zm0 4h4v2h-4v-2z"/></svg>', name: '請求書金額計算', desc: '税込・税抜・消費税・源泉徴収・振込額を一括計算', cat: 'business', tags: ['請求書','税込','源泉徴収','振込額'], accent: '#8b5cf6', url: 'tool-52-invoice-calc/' },
    { id: 'age-calc', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>', name: '年齢・勤続年数計算', desc: '生年月日から年齢、入社日から勤続年数・有給日数を計算', cat: 'business', tags: ['年齢','勤続年数','有給休暇','人事'], accent: '#059669', url: 'tool-53-age-calc/' },
    { id: 'working-hours', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/></svg>', name: '残業代・割増賃金計算', desc: '時間外25%・深夜25%・休日35%の残業代を自動計算', cat: 'business', tags: ['残業代','割増賃金','労働時間','社労士'], accent: '#dc2626', url: 'tool-54-working-hours/' },
    { id: 'late-fee', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11 17h2v-6h-2v6zm1-15C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM11 9h2V7h-2v2z"/></svg>', name: '遅延損害金計算', desc: '法定利率3%・賃金14.6%・約定利率で遅延損害金を計算', cat: 'business', tags: ['遅延損害金','法定利率','弁護士','司法書士'], accent: '#b45309', url: 'tool-55-late-fee-calc/' },
    { id: 'inheritance', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1H6.5c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.88-4.4z"/></svg>', name: '相続税シミュレーター', desc: '遺産総額と相続人数から基礎控除・概算税額を計算', cat: 'business', tags: ['相続税','基礎控除','税理士','FP'], accent: '#7c3aed', url: 'tool-56-inheritance-tax/' },
    { id: 'stamp-duty', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-7 14H6v-2h6v2zm4-4H6v-2h10v2zm0-4H6V7h10v2z"/></svg>', name: '印紙税額検索', desc: '契約書・領収書に必要な収入印紙の金額を即検索', cat: 'business', tags: ['印紙税','収入印紙','契約書','行政書士'], accent: '#0891b2', url: 'tool-57-stamp-duty/' },
    { id: 'freelance-income', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M5 9.2h3V19H5V9.2zM10.6 5h2.8v14h-2.8V5zm5.6 8H19v6h-2.8v-6z"/></svg>', name: 'フリーランス年収シミュレーター', desc: '月単価と稼働率から年収・税金・手取りを一括計算', cat: 'freelance', tags: ['フリーランス','年収','手取り','月単価'], accent: '#f59e0b', url: 'tool-58-freelance-income/' },
    { id: 'depreciation', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4V8h16v10zm-8-3a3 3 0 100-6 3 3 0 000 6z"/></svg>', name: '減価償却計算', desc: 'PC・車・設備の減価償却費を定額法・定率法で計算', cat: 'freelance', tags: ['減価償却','耐用年数','PC','経費'], accent: '#0d9488', url: 'tool-59-depreciation/' },
    { id: 'nhi-calc', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-1 16H6c-.55 0-1-.45-1-1V6c0-.55.45-1 1-1h12c.55 0 1 .45 1 1v12c0 .55-.45 1-1 1zm-4.44-6.19l-2.35 3.02-1.56-1.88L8 16h8l-2.44-3.19z"/></svg>', name: '国民健康保険料計算', desc: 'フリーランスの国保料を所得から概算シミュレーション', cat: 'freelance', tags: ['国保','健康保険','社会保険','フリーランス'], accent: '#e11d48', url: 'tool-60-nhi-calc/' },
    { id: 'business-tax', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.14 12.94a7.07 7.07 0 00.06-.94c0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 00.12-.61l-1.92-3.32a.49.49 0 00-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54a.48.48 0 00-.48-.41h-3.84a.48.48 0 00-.48.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96a.49.49 0 00-.59.22L2.74 8.87a.48.48 0 00.12.61l2.03 1.58c-.05.3-.07.62-.07.94s.02.64.07.94l-2.03 1.58a.49.49 0 00-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6A3.6 3.6 0 1115.6 12 3.61 3.61 0 0112 15.6z"/></svg>', name: '個人事業税計算', desc: '事業所得290万超の個人事業税を業種別税率で計算', cat: 'freelance', tags: ['個人事業税','事業税','290万','業種別'], accent: '#6366f1', url: 'tool-61-business-tax/' }"""

# TOOLS配列の最後のツール（htaccess）の直後に追加
if "tool-51-business-day-calc" not in content:
    content = content.replace(
        "url: 'tool-50-htaccess-gen/' },\n];",
        "url: 'tool-50-htaccess-gen/' }" + new_tools_js + "\n];"
    )
    print("  ✅ 新ツール11本をTOOLS配列に追加")
else:
    print("  ⏭️  既に追加済み")

# 新カテゴリを追加
new_cats = """    { id: 'business', emoji: '<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20 6h-4V4c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H4c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-6 0h-4V4h4v2z"/></svg>', label: 'ビジネス・士業' },
    { id: 'freelance', emoji: '<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>', label: 'フリーランス' },"""

if "'business'" not in content:
    content = content.replace(
        "{ id: 'utility',",
        new_cats + "\n    { id: 'utility',"
    )
    print("  ✅ 新カテゴリ「ビジネス・士業」「フリーランス」を追加")

# ツール数を更新
content = content.replace("全50ツール無料・登録不要", "全60+ツール無料・登録不要")
content = content.replace("<div class=\"num\">50+</div>", "<div class=\"num\">60+</div>")
content = content.replace("無料オンライン開発者ツール50選", "無料オンラインツール60選 | 開発者・フリーランス・士業向け")
content = content.replace(
    'content="開発者・デザイナー・フリーランス向けの無料オンラインツール集。JSON整形、文字数カウント、パスワード生成、画像圧縮、確定申告計算など50種類以上。すべてブラウザ完結・サーバー送信なし。">',
    'content="開発者・デザイナー・フリーランス・士業向けの無料オンラインツール集。JSON整形、確定申告シミュレーター、源泉徴収計算、営業日計算、残業代計算、相続税計算など60種類以上。すべてブラウザ完結・登録不要。">'
)
content = content.replace(
    'content="DevTools Japan | 無料オンライン開発者ツール50選">',
    'content="DevTools Japan | 開発者・フリーランス・士業向け無料オンラインツール60選">'
)

# SEOテキストにビジネス・フリーランスツールの説明を追加
old_seo = """            <h3>フリーランス向け</h3>
            <p>確定申告の経費計算、源泉徴収税の計算、ローン返済シミュレーションなど、フリーランスや副業に役立つ計算ツールも用意しています。税金や報酬の計算を瞬時に行えます。</p>"""

new_seo = """            <h3>フリーランス向け</h3>
            <p>確定申告シミュレーター、源泉徴収税計算、フリーランス年収シミュレーター、国民健康保険料計算、個人事業税計算、減価償却計算、請求書金額計算など、フリーランスや副業に必要な税金・お金の計算ツールを充実させています。独立前の収入シミュレーションから確定申告の準備まで、このサイトだけで完結します。</p>

            <h3>ビジネス・士業向け</h3>
            <p>営業日計算（土日祝除外）、残業代・割増賃金計算、年齢・勤続年数計算（有給日数付き）、遅延損害金計算（法定利率対応）、相続税シミュレーター、印紙税額検索など、経理・総務・人事・弁護士・司法書士・税理士・社労士・行政書士・FPの実務で使えるツールを揃えています。</p>"""

content = content.replace(old_seo, new_seo)

with open(portal_path, "w", encoding="utf-8") as f:
    f.write(content)
print("  ✅ ポータル全体を更新（タイトル・description・SEOテキスト）")


# ============================================================
# 2. 既存ツールから新ツールへのクロスリンク追加
# ============================================================
print("\n📋 2. 既存ツールから新ツールへのクロスリンクを追加中...")

CROSS_LINKS = {
    "tool-21-tax-simulator": [
        ("/tool-58-freelance-income/", "フリーランス年収シミュレーター"),
        ("/tool-60-nhi-calc/", "国民健康保険料計算"),
        ("/tool-61-business-tax/", "個人事業税計算"),
    ],
    "tool-22-withholding-tax": [
        ("/tool-52-invoice-calc/", "請求書金額計算"),
        ("/tool-58-freelance-income/", "フリーランス年収シミュレーター"),
    ],
    "tool-27-loan-calc": [
        ("/tool-56-inheritance-tax/", "相続税シミュレーター"),
        ("/tool-55-late-fee-calc/", "遅延損害金計算"),
    ],
}

link_template = '<a href="{}" style="padding:8px 16px;background:var(--bg-elevated,#0c0c14);border:1px solid var(--border,#1e1e30);border-radius:8px;color:var(--text-secondary,#8888a8);text-decoration:none;font-size:0.8rem;transition:all 0.2s" onmouseover="this.style.borderColor=\'var(--accent,#6366f1)\';this.style.color=\'var(--text,#e4e4f0)\'" onmouseout="this.style.borderColor=\'var(--border,#1e1e30)\';this.style.color=\'var(--text-secondary,#8888a8)\'">{}</a>'

for tool_dir, links in CROSS_LINKS.items():
    filepath = os.path.join(BASE, tool_dir, "index.html")
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        tc = f.read()

    added = 0
    for href, text in links:
        if href not in tc:
            # 関連ツールセクションの</div>の直前に追加
            new_link = link_template.format(href, text)
            # 最後の関連ツールリンクの後に追加
            tc = tc.replace("</div>\n    </div>\n    <footer>",
                          new_link + "\n</div>\n    </div>\n    <footer>", 1)
            added += 1

    if added > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(tc)
        print(f"  ✅ {tool_dir}: {added}リンク追加")


# ============================================================
# 3. SEO診断を実行
# ============================================================
print("\n📋 3. 新ツール11本のSEO診断...")

import re as re_module
new_tools = [f"tool-{i}" for i in range(51, 62)]
all_ok = True

for d in sorted(os.listdir(BASE)):
    if not d.startswith("tool-5") and not d.startswith("tool-6"):
        continue
    num = int(d.split("-")[1])
    if num < 51 or num > 61:
        continue

    filepath = os.path.join(BASE, d, "index.html")
    if not os.path.exists(filepath):
        print(f"  ❌ {d}: ファイルなし")
        all_ok = False
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        tc = f.read()

    head = re_module.search(r'<head[^>]*>(.*?)</head>', tc, re_module.DOTALL)
    head = head.group(1) if head else ""

    issues = []
    if 'G-E27Q8YTG7L' not in head: issues.append("GA4なし")
    if 'ca-pub-7300747004702072' not in head: issues.append("AdSenseなし")
    if 'favicon.svg' not in head: issues.append("faviconなし")
    if '<title>' not in head: issues.append("titleなし")
    if 'name="description"' not in head: issues.append("descriptionなし")
    if 'rel="canonical"' not in head: issues.append("canonicalなし")
    if 'og:title' not in head: issues.append("og:titleなし")
    if 'og:url' not in head: issues.append("og:urlなし")
    if 'twitter:card' not in head: issues.append("twitter:cardなし")
    if 'application/ld+json' not in head: issues.append("JSON-LDなし")
    if 'seo-content' not in tc: issues.append("SEOテキストなし")
    if '関連ツール' not in tc: issues.append("関連ツールなし")

    if issues:
        print(f"  ⚠️  {d}: {', '.join(issues)}")
        all_ok = False
    else:
        print(f"  ✅ {d}: 全項目OK")

if all_ok:
    print("\n  全11ツール、SEO完璧！")


print("\n" + "=" * 60)
print("  完了！")
print("=" * 60)
print()
print("デプロイ:")
print("  git add .")
print('  git commit -m "SEO: add 11 tools to portal, new categories, cross-links, updated meta"')
print("  git push")
print()
print("push後:")
print("  1. Search Console で sitemap.xml を再送信")
print("  2. AdSense で再審査リクエスト")
