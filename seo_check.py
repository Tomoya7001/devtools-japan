#!/usr/bin/env python3
"""
DevTools Japan — 全50ツール SEO診断スクリプト
各ページのSEO要素を検査し、問題をレポートする
"""

import os
import re
import json

BASE = os.getcwd()
results = []

TOOLS = [d for d in sorted(os.listdir(BASE)) if d.startswith("tool-") and os.path.isdir(os.path.join(BASE, d))]
# 固定ページも含む
PAGES = TOOLS + ["about", "privacy", "contact"]

for page_dir in PAGES:
    filepath = os.path.join(BASE, page_dir, "index.html")
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.DOTALL)
    head = head_match.group(1) if head_match else ""

    issues = []
    
    # 1. title
    title_match = re.search(r'<title>(.*?)</title>', head)
    title = title_match.group(1) if title_match else ""
    if not title:
        issues.append("❌ title なし")
    elif len(title) < 15:
        issues.append(f"⚠️ title 短すぎ ({len(title)}文字): {title}")
    
    # 2. meta description
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', head)
    desc = desc_match.group(1) if desc_match else ""
    if not desc:
        issues.append("❌ meta description なし")
    elif len(desc) < 30:
        issues.append(f"⚠️ meta description 短すぎ ({len(desc)}文字)")
    
    # 3. canonical
    if 'rel="canonical"' not in head:
        issues.append("❌ canonical なし")
    
    # 4. og:title
    if 'og:title' not in head:
        issues.append("❌ og:title なし")
    
    # 5. og:description
    if 'og:description' not in head:
        issues.append("❌ og:description なし")
    
    # 6. og:url
    if 'og:url' not in head:
        issues.append("⚠️ og:url なし")
    
    # 7. og:type
    if 'og:type' not in head:
        issues.append("⚠️ og:type なし")
    
    # 8. twitter:card
    if 'twitter:card' not in head:
        issues.append("⚠️ twitter:card なし")
    
    # 9. JSON-LD
    if 'application/ld+json' not in head:
        issues.append("❌ JSON-LD なし")
    
    # 10. GA4
    if 'G-E27Q8YTG7L' not in head:
        issues.append("❌ GA4 なし")
    
    # 11. SEOテキスト
    seo_match = re.search(r'class="seo-content"', content)
    if not seo_match and page_dir.startswith("tool-"):
        issues.append("⚠️ SEOテキストセクション なし")
    
    # 12. 関連ツールリンク
    if page_dir.startswith("tool-") and '関連ツール' not in content:
        issues.append("⚠️ 関連ツールリンク なし")
    
    # 13. 広告プレースホルダー（display:none確認）
    visible_ads = re.findall(r'<div class="ad-slot">(?!.*display:none)', content)
    if visible_ads:
        issues.append(f"⚠️ 非表示でない広告枠 {len(visible_ads)}箇所")

    status = "✅" if not issues else "⚠️" if all("⚠️" in i for i in issues) else "❌"
    results.append({
        "page": page_dir,
        "status": status,
        "title_len": len(title),
        "desc_len": len(desc),
        "issues": issues,
    })

# レポート出力
print("=" * 70)
print("  DevTools Japan — SEO診断レポート")
print("=" * 70)

perfect = sum(1 for r in results if r["status"] == "✅")
warning = sum(1 for r in results if r["status"] == "⚠️")
error = sum(1 for r in results if r["status"] == "❌")

print(f"\n  合計: {len(results)}ページ | ✅ {perfect} 問題なし | ⚠️ {warning} 警告あり | ❌ {error} 要修正\n")

for r in results:
    if r["issues"]:
        print(f"\n{r['status']} {r['page']} (title:{r['title_len']}文字, desc:{r['desc_len']}文字)")
        for issue in r["issues"]:
            print(f"    {issue}")

# 問題なしのページ
ok_pages = [r["page"] for r in results if not r["issues"]]
if ok_pages:
    print(f"\n✅ 問題なし ({len(ok_pages)}ページ): {', '.join(ok_pages[:10])}{'...' if len(ok_pages) > 10 else ''}")

# 統計
missing_og_url = sum(1 for r in results if any("og:url" in i for i in r["issues"]))
missing_twitter = sum(1 for r in results if any("twitter:card" in i for i in r["issues"]))
missing_og_type = sum(1 for r in results if any("og:type" in i for i in r["issues"]))
short_desc = sum(1 for r in results if any("description 短すぎ" in i for i in r["issues"]))

print(f"\n--- 統計 ---")
print(f"  og:url 欠損: {missing_og_url}ページ")
print(f"  og:type 欠損: {missing_og_type}ページ")
print(f"  twitter:card 欠損: {missing_twitter}ページ")
print(f"  meta description 短い: {short_desc}ページ")
