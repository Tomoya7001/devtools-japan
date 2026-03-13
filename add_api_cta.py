#!/usr/bin/env python3
"""
DevTools Japan — API CTA導線 追加スクリプト

使い方:
  cd ~/Desktop/devtools-japan-complete
  python3 add_api_cta.py
"""

import os
import re

TIER1_TOOLS = ["tool-26-proofreader"]

TIER2_TOOLS = [
    "tool-01-moji-counter",
    "tool-34-text-counter-detail",
    "tool-19-zenkaku-hankaku",
    "tool-12-wareki",
    "tool-25-speech-time",
    "tool-43-word-counter-en",
]

CTA_TIER1 = '''
    <div style="background:linear-gradient(135deg,rgba(99,102,241,0.08),rgba(88,166,255,0.08));border:1px solid rgba(99,102,241,0.3);border-radius:12px;padding:24px;margin-bottom:24px;text-align:center">
      <div style="display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:8px">
        <svg viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2" width="20" height="20"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>
        <span style="font-size:0.9rem;font-weight:600;color:#6366f1">API版が登場</span>
      </div>
      <p style="color:#e4e4f0;font-size:0.85rem;margin-bottom:12px;line-height:1.6">この校正機能をあなたのアプリに組み込みませんか？<br>REST APIで簡単に統合できます。月100リクエスト無料。</p>
      <a href="https://api.devtools-japan.com" target="_blank" rel="noopener" style="display:inline-block;padding:10px 24px;background:#6366f1;color:#fff;border-radius:8px;text-decoration:none;font-size:0.8rem;font-weight:600;transition:background 0.2s" onmouseover="this.style.background='#818cf8'" onmouseout="this.style.background='#6366f1'">日本語校正APIを見る →</a>
    </div>
'''

CTA_TIER2 = '''
    <div style="background:var(--bg-card,#111118);border:1px solid rgba(99,102,241,0.2);border-radius:12px;padding:16px 20px;margin-bottom:24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
      <div>
        <span style="font-size:0.75rem;color:#6366f1;font-weight:600">API</span>
        <span style="font-size:0.8rem;color:#8888a8;margin-left:8px">この機能をアプリに組み込みませんか？</span>
      </div>
      <a href="https://api.devtools-japan.com" target="_blank" rel="noopener" style="padding:6px 16px;background:transparent;border:1px solid rgba(99,102,241,0.4);color:#6366f1;border-radius:6px;text-decoration:none;font-size:0.75rem;font-weight:500;transition:all 0.2s;white-space:nowrap" onmouseover="this.style.background='rgba(99,102,241,0.1)'" onmouseout="this.style.background='transparent'">APIを見る →</a>
    </div>
'''

CTA_MARKER = "api.devtools-japan.com"


def add_cta(directory):
    modified = []
    skipped = []

    all_targets = [(t, "tier1") for t in TIER1_TOOLS] + [(t, "tier2") for t in TIER2_TOOLS]

    for tool_dir, tier in all_targets:
        filepath = os.path.join(directory, tool_dir, "index.html")
        if not os.path.exists(filepath):
            print(f"  ⚠️  {tool_dir}/index.html が見つかりません")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if CTA_MARKER in content:
            skipped.append(tool_dir)
            continue

        cta_html = CTA_TIER1 if tier == "tier1" else CTA_TIER2

        related_pattern = r'(<div style="background:var\(--bg-card[^>]*>\s*<h3[^>]*>関連ツール)'
        match = re.search(related_pattern, content)

        if match:
            insert_pos = match.start()
            new_content = content[:insert_pos] + cta_html + "\n" + content[insert_pos:]
        else:
            footer_match = re.search(r'(<footer>)', content)
            if footer_match:
                insert_pos = footer_match.start()
                new_content = content[:insert_pos] + cta_html + "\n" + content[insert_pos:]
            else:
                print(f"  ⚠️  {tool_dir}: 挿入位置が見つかりません")
                continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        modified.append((tool_dir, tier))

    return modified, skipped


def main():
    directory = os.getcwd()

    if not os.path.exists(os.path.join(directory, "index.html")):
        print("エラー: devtools-japan-complete ディレクトリで実行してください")
        return

    print("=" * 50)
    print("  DevTools Japan — API CTA導線追加")
    print("=" * 50)
    print()

    modified, skipped = add_cta(directory)

    if modified:
        print(f"✅ CTA追加: {len(modified)}ツール")
        for tool, tier in modified:
            label = "🔥 強CTA" if tier == "tier1" else "💡 軽CTA"
            print(f"   {label}  {tool}")

    if skipped:
        print(f"\n⏭️  スキップ（既に追加済み）: {len(skipped)}ツール")
        for tool in skipped:
            print(f"   - {tool}")

    print()
    if modified:
        print("次のステップ:")
        print("  git add .")
        print('  git commit -m "Add API CTA banners to related tools"')
        print("  git push")


if __name__ == "__main__":
    main()
