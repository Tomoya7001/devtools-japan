#!/usr/bin/env python3
"""
DevTools Japan — GA4トラッキングコード一括挿入スクリプト

使い方:
  cd ~/Desktop/devtools-japan-complete
  python3 add_ga4.py G-XXXXXXXXXX

※ G-XXXXXXXXXX を自分のGA4測定IDに置き換えてください
"""

import os
import sys
import re

def get_ga4_snippet(measurement_id: str) -> str:
    return f'''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{measurement_id}');
</script>'''


def inject_ga4(directory: str, measurement_id: str):
    snippet = get_ga4_snippet(measurement_id)
    modified = []
    skipped = []
    errors = []

    for root, dirs, files in os.walk(directory):
        for fname in files:
            if not fname.endswith('.html'):
                continue
            filepath = os.path.join(root, fname)
            rel_path = os.path.relpath(filepath, directory)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                errors.append((rel_path, str(e)))
                continue

            # 既にGA4タグが挿入済みかチェック
            if measurement_id in content or 'googletagmanager.com/gtag/js' in content:
                skipped.append(rel_path)
                continue

            # <head> タグの直後に挿入
            pattern = r'(<head[^>]*>)'
            match = re.search(pattern, content, re.IGNORECASE)
            if not match:
                errors.append((rel_path, '<head> タグが見つかりません'))
                continue

            insert_pos = match.end()
            new_content = content[:insert_pos] + '\n' + snippet + '\n' + content[insert_pos:]

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            modified.append(rel_path)

    return modified, skipped, errors


def main():
    if len(sys.argv) != 2 or not sys.argv[1].startswith('G-'):
        print("使い方: python3 add_ga4.py G-XXXXXXXXXX")
        print("※ GA4の測定IDを引数に指定してください")
        sys.exit(1)

    measurement_id = sys.argv[1]
    directory = os.getcwd()

    # index.html が存在するか確認（正しいディレクトリかチェック）
    if not os.path.exists(os.path.join(directory, 'index.html')):
        print(f"エラー: {directory} に index.html が見つかりません")
        print("devtools-japan-complete ディレクトリで実行してください")
        sys.exit(1)

    print(f"GA4測定ID: {measurement_id}")
    print(f"対象ディレクトリ: {directory}")
    print(f"{'='*50}")

    modified, skipped, errors = inject_ga4(directory, measurement_id)

    print(f"\n✅ 挿入完了: {len(modified)} ファイル")
    for f in sorted(modified):
        print(f"   + {f}")

    if skipped:
        print(f"\n⏭️  スキップ（既に挿入済み）: {len(skipped)} ファイル")
        for f in sorted(skipped):
            print(f"   - {f}")

    if errors:
        print(f"\n❌ エラー: {len(errors)} ファイル")
        for f, e in sorted(errors):
            print(f"   ! {f}: {e}")

    print(f"\n{'='*50}")
    print(f"合計: 挿入={len(modified)}, スキップ={len(skipped)}, エラー={len(errors)}")

    if modified:
        print(f"\n次のステップ:")
        print(f"  git add .")
        print(f'  git commit -m "Add GA4 tracking ({measurement_id})"')
        print(f"  git push")


if __name__ == '__main__':
    main()
