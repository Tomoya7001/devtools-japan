#!/usr/bin/env python3
"""
canonical URL + sitemap.xml を www.devtools-japan.com に統一するスクリプト
~/Desktop/devtools-japan-complete/ で実行してください

python3 fix-canonical-urls.py
"""

import os
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # https://devtools-japan.com → https://www.devtools-japan.com
    # ただし https://www.devtools-japan.com は変換しない（二重wwwを防ぐ）
    # また https://api.devtools-japan.com は変換しない
    
    # まず www.devtools-japan.com を一時プレースホルダーに
    content = content.replace('https://www.devtools-japan.com', '___WWW_PLACEHOLDER___')
    content = content.replace('https://api.devtools-japan.com', '___API_PLACEHOLDER___')
    
    # wwwなしをwwwありに変換
    content = content.replace('https://devtools-japan.com', 'https://www.devtools-japan.com')
    
    # プレースホルダーを戻す
    content = content.replace('___WWW_PLACEHOLDER___', 'https://www.devtools-japan.com')
    content = content.replace('___API_PLACEHOLDER___', 'https://api.devtools-japan.com')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    # HTMLファイル
    html_files = sorted(glob.glob('**/index.html', recursive=True))
    
    # sitemap.xml
    all_files = html_files + ['sitemap.xml']
    
    if not html_files:
        print("HTMLファイルが見つかりません。")
        print("~/Desktop/devtools-japan-complete/ で実行してください。")
        return
    
    print(f"canonical URL修正を開始します...")
    print(f"対象: {len(all_files)} ファイル\n")
    
    updated = 0
    unchanged = 0
    
    for filepath in all_files:
        if not os.path.exists(filepath):
            print(f"  スキップ（ファイルなし）: {filepath}")
            continue
        changed = fix_file(filepath)
        if changed:
            print(f"  修正完了: {filepath}")
            updated += 1
        else:
            print(f"  変更なし: {filepath}")
            unchanged += 1
    
    print(f"\n{'='*50}")
    print(f"完了！")
    print(f"  修正: {updated} ファイル")
    print(f"  変更なし: {unchanged} ファイル")
    print(f"\n次のステップ:")
    print(f"  git add .")
    print(f'  git commit -m "canonical URLをwww.devtools-japan.comに統一"')
    print(f"  git push")
    print(f"\nデプロイ後、Search Consoleでサイトマップを再送信してください。")

if __name__ == '__main__':
    main()
