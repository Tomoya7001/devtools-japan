#!/usr/bin/env python3
"""
DevTools Japan — SEO一括修正スクリプト
診断で見つかった全問題を一括修正する
"""

import os
import re

BASE = os.getcwd()

# ===== 1. meta description が短いページの改善テキスト =====
DESC_FIXES = {
    "tool-33-emoji-search": "絵文字をキーワードで検索・コピー。Slack、Twitter、LINE等で使える絵文字を名前・カテゴリから素早く見つけられる無料ツール。",
    "tool-34-text-counter-detail": "テキストの詳細統計を分析。ひらがな・カタカナ・漢字・英字・数字の文字種別カウント、出現頻度、語彙密度を可視化する無料ツール。",
    "tool-35-random-number": "指定した範囲でランダムな数値を生成。抽選・くじ引き・テストデータ作成に便利。複数個の同時生成にも対応する無料ツール。",
    "tool-41-text-reverse": "テキストを逆順に変換。文字列の反転、回文チェック、プログラミングのデバッグに使える無料オンラインツール。",
    "tool-42-number-format": "数値を3桁カンマ区切り・通貨形式・パーセント表示などに変換。日本円・ドル表記にも対応する無料フォーマッター。",
    "tool-43-word-counter-en": "英文のワード数・センテンス数・パラグラフ数をリアルタイムカウント。英語レポート・論文・TOEIC対策の文字数管理に。",
    "tool-44-tab-space": "タブとスペースの相互変換ツール。インデント幅（2/4/8スペース）を指定して一括変換。コーディング規約の統一に便利。",
    "tool-45-chmod-calc": "Linuxのファイル権限（パーミッション）を数値⇔記号で変換。chmod 755やrwxr-xr-xの意味を視覚的に確認できる無料ツール。",
    "tool-46-color-palette": "メインカラーから調和の取れた配色パターンを自動生成。補色・類似色・トライアドなど、デザインに使えるカラーパレット作成ツール。",
    "tool-47-html-color-names": "HTML/CSSで使える140色以上のカラーネーム一覧。色名・HEXコード・RGB値を一覧表示。コピペで即使える無料リファレンス。",
    "tool-48-jwt-decoder": "JWTトークンのヘッダーとペイロードをデコードして中身を確認。有効期限チェック付き。認証デバッグに必須の無料ツール。",
    "tool-49-sql-formatter": "SQL文を見やすくインデント整形。SELECT・JOIN・WHERE句を自動フォーマット。複雑なクエリの可読性向上に。",
    "tool-50-htaccess-gen": ".htaccessの設定をGUIで簡単生成。HTTPSリダイレクト・www統一・キャッシュ・Gzip圧縮・直リンク防止をチェックボックスで選ぶだけ。",
}

# ===== 2. OGP/Twitter/canonical/JSON-LD 欠損ページの修正データ =====
OGP_FIXES = {
    "tool-01-moji-counter": {
        "og:url": "https://www.devtools-japan.com/tool-01-moji-counter/",
        "twitter:card": "summary",
        "twitter:title": "文字数カウンター | DevTools Japan",
        "twitter:description": "テキストの文字数・単語数・行数をリアルタイムでカウント",
    },
    "tool-24-ogp-preview": {
        "og:title": "OGPプレビューチェッカー | DevTools Japan",
        "og:description": "URLを入力してOGP（Open Graph Protocol）の表示をプレビュー確認",
        "og:url": "https://www.devtools-japan.com/tool-24-ogp-preview/",
        "og:type": "website",
        "twitter:card": "summary",
        "twitter:title": "OGPプレビューチェッカー | DevTools Japan",
        "twitter:description": "URLを入力してOGP表示をプレビュー確認",
    },
    "about": {
        "canonical": "https://www.devtools-japan.com/about/",
        "og:title": "サイトについて | DevTools Japan",
        "og:description": "DevTools Japanは開発者・デザイナー・フリーランス向けの無料オンラインツール集です",
        "og:url": "https://www.devtools-japan.com/about/",
        "og:type": "website",
        "twitter:card": "summary",
        "twitter:title": "サイトについて | DevTools Japan",
        "twitter:description": "開発者・デザイナー・フリーランス向けの無料オンラインツール集",
        "json_ld": '{"@context":"https://schema.org","@type":"WebSite","name":"DevTools Japan","description":"開発者・デザイナー・フリーランス向けの無料オンラインツール集","url":"https://www.devtools-japan.com"}',
    },
    "privacy": {
        "canonical": "https://www.devtools-japan.com/privacy/",
        "og:title": "プライバシーポリシー | DevTools Japan",
        "og:description": "DevTools Japanのプライバシーポリシー。個人情報の取り扱い、Cookie、広告について",
        "og:url": "https://www.devtools-japan.com/privacy/",
        "og:type": "website",
        "twitter:card": "summary",
        "twitter:title": "プライバシーポリシー | DevTools Japan",
        "twitter:description": "DevTools Japanのプライバシーポリシー",
        "json_ld": '{"@context":"https://schema.org","@type":"WebPage","name":"プライバシーポリシー","description":"DevTools Japanのプライバシーポリシー","url":"https://www.devtools-japan.com/privacy/","provider":{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}',
    },
    "contact": {
        "og:title": "お問い合わせ | DevTools Japan",
        "og:description": "DevTools Japanへのお問い合わせ。バグ報告、機能リクエスト、ご意見などお気軽にどうぞ",
        "og:url": "https://www.devtools-japan.com/contact/",
        "og:type": "website",
        "twitter:card": "summary",
        "twitter:title": "お問い合わせ | DevTools Japan",
        "twitter:description": "DevTools Japanへのお問い合わせ",
        "json_ld": '{"@context":"https://schema.org","@type":"ContactPage","name":"お問い合わせ","description":"DevTools Japanへのお問い合わせ","url":"https://www.devtools-japan.com/contact/","provider":{"@type":"Organization","name":"DevTools Japan","url":"https://www.devtools-japan.com"}}',
    },
}


def fix_meta_description(filepath: str, new_desc: str) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    old_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content)
    if not old_match:
        return False

    old_tag = old_match.group(0)
    new_tag = f'<meta name="description" content="{new_desc}"'
    content = content.replace(old_tag, new_tag)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def add_missing_tags(filepath: str, fixes: dict) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    tags_added = 0
    insert_before = "</head>"

    new_tags = []

    # canonical
    if "canonical" in fixes and 'rel="canonical"' not in content:
        new_tags.append(f'    <link rel="canonical" href="{fixes["canonical"]}">')
        tags_added += 1

    # OGP tags
    for key in ["og:title", "og:description", "og:url", "og:type"]:
        if key in fixes and f'property="{key}"' not in content:
            new_tags.append(f'    <meta property="{key}" content="{fixes[key]}">')
            tags_added += 1

    # Twitter tags
    for key in ["twitter:card", "twitter:title", "twitter:description"]:
        if key in fixes and f'name="{key}"' not in content:
            new_tags.append(f'    <meta name="{key}" content="{fixes[key]}">')
            tags_added += 1

    # JSON-LD
    if "json_ld" in fixes and "application/ld+json" not in content:
        new_tags.append(f'    <script type="application/ld+json">\n    {fixes["json_ld"]}\n    </script>')
        tags_added += 1

    if new_tags:
        tag_block = "\n".join(new_tags) + "\n"
        content = content.replace(insert_before, tag_block + insert_before)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return tags_added


def main():
    if not os.path.exists(os.path.join(BASE, "index.html")):
        print("エラー: devtools-japan-complete ディレクトリで実行してください")
        return

    print("=" * 60)
    print("  DevTools Japan — SEO一括修正")
    print("=" * 60)

    total_desc = 0
    total_tags = 0

    # 1. meta description 修正
    print("\n📝 1. meta description を改善中...")
    for tool_dir, new_desc in DESC_FIXES.items():
        filepath = os.path.join(BASE, tool_dir, "index.html")
        if os.path.exists(filepath):
            if fix_meta_description(filepath, new_desc):
                total_desc += 1
                print(f"  ✅ {tool_dir}")
            else:
                print(f"  ⚠️ {tool_dir}: meta descriptionタグが見つかりません")

    # 2. OGP/Twitter/canonical/JSON-LD 修正
    print("\n🏷️  2. OGP・Twitter・canonical・JSON-LD を追加中...")
    for page_dir, fixes in OGP_FIXES.items():
        filepath = os.path.join(BASE, page_dir, "index.html")
        if os.path.exists(filepath):
            count = add_missing_tags(filepath, fixes)
            if count > 0:
                total_tags += count
                print(f"  ✅ {page_dir}: {count}タグ追加")
            else:
                print(f"  ⏭️  {page_dir}: 追加不要（既に設定済み）")

    print("\n" + "=" * 60)
    print(f"  修正完了！")
    print(f"  meta description改善: {total_desc}ページ")
    print(f"  タグ追加: {total_tags}個")
    print("=" * 60)
    print("\n次のステップ:")
    print("  python3 seo_check.py  # 再診断して問題が0になったか確認")
    print()
    print("問題なければ:")
    print("  git add .")
    print('  git commit -m "SEO fix: improve meta descriptions, add missing OGP/Twitter/canonical/JSON-LD"')
    print("  git push")


if __name__ == "__main__":
    main()
