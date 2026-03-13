#!/usr/bin/env python3
"""
DevTools Japan ライトテーマ一括変換スクリプト（v2）
~/Desktop/devtools-japan-complete/ で実行してください

使い方:
  cd ~/Desktop/devtools-japan-complete
  python3 convert-to-light-theme.py
"""

import os
import re
import glob

LIGHT_COLORS = {
    'bg_main':       '#f7f8fb',
    'bg_white':      '#ffffff',
    'bg_hover':      '#f0f1f7',
    'border':        '#e0e2ed',
    'border_hover':  '#c8cbdb',
    'text_primary':  '#1e1e35',
    'text_secondary':'#5a5f78',
    'text_muted':    '#9498b0',
}


def hex_brightness(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join(c*2 for c in hex_color)
    if len(hex_color) != 6:
        return -1
    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r * 299 + g * 587 + b * 114) / 1000
    except:
        return -1


def classify_and_replace_root_var(var_name, var_value):
    name = var_name.lower().strip()
    value = var_value.strip()
    if not re.match(r'^#[0-9a-fA-F]{3,6}$', value):
        return None
    brightness = hex_brightness(value)

    bg_patterns = ['bg-primary', 'bg-secondary', 'bg-card', 'bg-elevated', 'bg-input', 'bg-card-hover', 'bg-hover']

    if name == '--bg':
        if brightness < 30:
            return LIGHT_COLORS['bg_main']

    for pat in bg_patterns:
        if pat in name:
            if 'hover' in name:
                return LIGHT_COLORS['bg_hover']
            elif 'card' in name or 'elevated' in name or 'secondary' in name or 'input' in name:
                return LIGHT_COLORS['bg_white']
            else:
                return LIGHT_COLORS['bg_main']

    if 'border' in name:
        if 'hover' in name:
            return LIGHT_COLORS['border_hover']
        else:
            return LIGHT_COLORS['border']

    text_primary_names = ['--text-primary', '--text']
    text_secondary_names = ['--text-secondary', '--text2']
    text_muted_names = ['--text-muted', '--text3']

    if name in text_primary_names and brightness > 150:
        return LIGHT_COLORS['text_primary']
    if name in text_secondary_names and brightness > 80:
        return LIGHT_COLORS['text_secondary']
    if name in text_muted_names and brightness > 50:
        return LIGHT_COLORS['text_muted']

    return None


def transform_root_block(content):
    def replace_var(match):
        full = match.group(0)
        var_name = match.group(1)
        var_value = match.group(2)
        new_value = classify_and_replace_root_var(var_name, var_value)
        if new_value:
            return f'{var_name}:{new_value}'
        return full

    return re.sub(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})', replace_var, content)


def fix_direct_dark_colors(content):
    def replace_bg_color(match):
        prop = match.group(1)
        color = match.group(2)
        b = hex_brightness(color)
        if b < 25:
            return f'{prop}{LIGHT_COLORS["bg_main"]}'
        elif b < 35:
            return f'{prop}{LIGHT_COLORS["bg_white"]}'
        return match.group(0)

    result = re.sub(r'(background\s*:\s*)(#[0-9a-fA-F]{6})', replace_bg_color, content)
    result = re.sub(r'(background-color\s*:\s*)(#[0-9a-fA-F]{6})', replace_bg_color, result)
    return result


def fix_shadows_and_effects(content):
    result = content
    result = re.sub(
        r'rgba\(0\s*,\s*0\s*,\s*0\s*,\s*0\.([3-5])\)',
        lambda m: f'rgba(0,0,0,0.0{m.group(1)})',
        result
    )
    result = result.replace("opacity='0.03'", "opacity='0.012'")
    result = re.sub(r'opacity:\s*0\.0[5-9];', 'opacity: 0.04;', result)
    return result


def fix_dim_colors(content):
    result = re.sub(
        r'rgba\((\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*0\.0([12])\)',
        lambda m: f'rgba({m.group(1)},{m.group(2)},{m.group(3)},0.0{int(m.group(4))+2})',
        content
    )
    return result


def fix_gradient_text_visibility(content):
    result = content
    result = re.sub(r'rgba\(99,102,241,0\.015\)', 'rgba(99,102,241,0.03)', result)
    result = re.sub(r'rgba\(99,102,241,0\.04\)\s*0%', 'rgba(99,102,241,0.05) 0%', result)
    result = re.sub(r'rgba\(34,211,238,0\.03\)\s*0%', 'rgba(34,211,238,0.04) 0%', result)
    return result


def add_selection_style(content):
    if '::selection' not in content:
        selection = '::selection{background:rgba(99,102,241,0.15);color:#1e1e35}'
        content = content.replace('*{margin:0;', f'{selection}*{{margin:0;')
        content = content.replace('* { margin: 0;', f'{selection}\n        * {{ margin: 0;')
    return content


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = transform_root_block(content)
    content = fix_direct_dark_colors(content)
    content = fix_shadows_and_effects(content)
    content = fix_dim_colors(content)
    content = fix_gradient_text_visibility(content)
    content = add_selection_style(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    html_files = sorted(glob.glob('**/index.html', recursive=True))

    if not html_files:
        print("HTMLファイルが見つかりません。")
        print("~/Desktop/devtools-japan-complete/ で実行してください。")
        return

    print(f"ライトテーマ変換を開始します...")
    print(f"対象: {len(html_files)} ファイル\n")

    updated = 0
    unchanged = 0

    for filepath in html_files:
        changed = process_file(filepath)
        if changed:
            print(f"  変換完了: {filepath}")
            updated += 1
        else:
            print(f"  変更なし: {filepath}")
            unchanged += 1

    print(f"\n{'='*50}")
    print(f"完了！")
    print(f"  変換: {updated} ファイル")
    print(f"  変更なし: {unchanged} ファイル")
    print(f"\n次のステップ:")
    print(f"  1. ブラウザで確認: open index.html")
    print(f'  2. git add . && git commit -m "ライトテーマに変更" && git push')
    print(f"\nロールバック: git checkout -- .")


if __name__ == '__main__':
    main()
