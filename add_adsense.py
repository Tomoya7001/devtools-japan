#!/usr/bin/env python3
"""全HTMLファイルにAdSenseコードスニペットを挿入する"""
import os, re

BASE = os.getcwd()
ADSENSE_CODE = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7300747004702072"
     crossorigin="anonymous"></script>'''

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
        
        # 既にAdSenseコードがある場合はスキップ
        if 'ca-pub-7300747004702072' in content:
            continue
        
        # GA4タグの直後に挿入（</script>の後の改行の後）
        # GA4の閉じタグを探す
        ga4_pattern = "gtag('config', 'G-E27Q8YTG7L');\n</script>"
        if ga4_pattern in content:
            content = content.replace(
                ga4_pattern,
                ga4_pattern + "\n" + ADSENSE_CODE
            )
        elif '</head>' in content:
            # GA4がない場合は</head>の前に挿入
            content = content.replace('</head>', ADSENSE_CODE + '\n</head>')
        else:
            continue
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        rel = os.path.relpath(filepath, BASE)
        count += 1

print(f"✅ {count}ファイルにAdSenseコードを挿入しました")

# 確認
total = 0
has_adsense = 0
for root, dirs, files in os.walk(BASE):
    if '.git' in root:
        continue
    for fname in files:
        if not fname.endswith('.html') or fname.startswith('google'):
            continue
        filepath = os.path.join(root, fname)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        total += 1
        if 'ca-pub-7300747004702072' in content:
            has_adsense += 1

print(f"📊 全{total}ページ中 {has_adsense}ページにAdSenseコード設置済み")
if total != has_adsense:
    print(f"⚠️ {total - has_adsense}ページにAdSenseコードがありません")
