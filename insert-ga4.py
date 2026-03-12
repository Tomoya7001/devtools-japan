#!/usr/bin/env python3
"""
GA4タグ一括挿入スクリプト
~/Desktop/devtools-japan-complete/ で実行してください

使い方:
  cd ~/Desktop/devtools-japan-complete
  python3 insert-ga4.py
"""

import os
import glob

GA4_TAG = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E27Q8YTG7L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-E27Q8YTG7L');
</script>'''

def insert_ga4():
    # プロジェクトルートの全index.htmlを検索
    html_files = glob.glob('**/index.html', recursive=True)
    
    if not html_files:
        print("❌ HTMLファイルが見つかりません。")
        print("   ~/Desktop/devtools-japan-complete/ で実行してください。")
        return
    
    updated = 0
    skipped = 0
    errors = 0
    
    for filepath in sorted(html_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 既にGA4タグが入っている場合はスキップ
            if 'G-E27Q8YTG7L' in content:
                print(f"⏭  スキップ（既に設置済み）: {filepath}")
                skipped += 1
                continue
            
            # <head> タグの直後に挿入
            if '<head>' in content:
                new_content = content.replace('<head>', f'<head>\n{GA4_TAG}', 1)
            elif '<HEAD>' in content:
                new_content = content.replace('<HEAD>', f'<HEAD>\n{GA4_TAG}', 1)
            else:
                print(f"⚠️  <head>タグが見つかりません: {filepath}")
                errors += 1
                continue
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ 挿入完了: {filepath}")
            updated += 1
            
        except Exception as e:
            print(f"❌ エラー: {filepath} - {e}")
            errors += 1
    
    print(f"\n{'='*50}")
    print(f"完了！")
    print(f"  挿入: {updated} ファイル")
    print(f"  スキップ: {skipped} ファイル")
    print(f"  エラー: {errors} ファイル")
    print(f"  合計: {updated + skipped + errors} ファイル")
    print(f"\n次のステップ:")
    print(f"  git add .")
    print(f'  git commit -m "GA4タグ追加（G-E27Q8YTG7L）"')
    print(f"  git push")

if __name__ == '__main__':
    insert_ga4()
