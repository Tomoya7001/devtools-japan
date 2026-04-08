#!/usr/bin/env python3
"""
SEO強化スクリプト — Search Consoleデータに基づく上位3ページの最適化
対象: tool-25, tool-23, tool-21
"""
import os, re

BASE = "/Users/tom/Desktop/devtools-japan-complete"

FIXES = [
    # ===== tool-25: 読み上げ時間 (217表示) =====
    {
        "file": "tool-25-speech-time/index.html",
        "replacements": [
            # title強化
            (
                "<title>読み上げ時間計算ツール | プレゼン・スピーチの所要時間</title>",
                "<title>読み上げ時間計算 | プレゼン・スピーチ・YouTube台本の所要時間を自動計算【無料】</title>"
            ),
            # description強化
            (
                '<meta name="description" content="テキストの読み上げ時間を自動計算。プレゼン、スピーチ、YouTube台本の所要時間が一目でわかる。">',
                '<meta name="description" content="テキストの読み上げ時間を自動計算する無料ツール。プレゼン原稿・スピーチ・YouTube台本・朝礼挨拶の所要時間が一目でわかる。速度4段階（ゆっくり〜アナウンサー）対応、原稿用紙換算付き。">'
            ),
            # OGP強化
            (
                '<meta property="og:title" content="読み上げ時間計算ツール | DevTools Japan">',
                '<meta property="og:title" content="読み上げ時間計算 | プレゼン・スピーチの所要時間を自動計算【無料】">'
            ),
            (
                '<meta property="og:description" content="テキストの読み上げ・プレゼン所要時間を自動計算">',
                '<meta property="og:description" content="プレゼン原稿・スピーチ・YouTube台本の読み上げ時間を自動計算。速度4段階対応。">'
            ),
            (
                '<meta name="twitter:title" content="読み上げ時間計算ツール | DevTools Japan">',
                '<meta name="twitter:title" content="読み上げ時間計算 | プレゼン・スピーチの所要時間【無料】">'
            ),
            (
                '<meta name="twitter:description" content="テキストの読み上げ・プレゼン所要時間を自動計算">',
                '<meta name="twitter:description" content="プレゼン原稿・スピーチ・YouTube台本の所要時間を自動計算">'
            ),
            # SEOテキスト大幅強化
            (
                """    <div class="seo-content">
        <h2>読み上げ時間計算ツールについて</h2>
        <p>プレゼンテーション、スピーチ、YouTube動画の台本など、テキストを読み上げた際のおおよその所要時間を計算するツールです。日本語の平均的な読み上げ速度は300〜400字/分と言われています。</p>
        <p>速度は「ゆっくり」「普通」「早口」「アナウンサー」の4段階から選択可能。各速度での目安時間も一覧で確認できます。</p>
    </div>""",
                """    <div class="seo-content">
        <h2>読み上げ時間計算ツールの使い方</h2>
        <p>プレゼンテーション、スピーチ、YouTube動画の台本、朝礼の挨拶、結婚式のスピーチなど、テキストを声に出して読み上げた際のおおよその所要時間を自動計算する無料ツールです。原稿を入力するだけで、瞬時に読み上げ時間・文字数・原稿用紙換算が表示されます。</p>

        <h3>読み上げ速度の目安</h3>
        <p>日本語の読み上げ速度は、場面や話し方によって大きく異なります。ゆっくり（250字/分）は結婚式スピーチや式典の挨拶に適しています。普通（350字/分）は一般的なプレゼンテーションや会議での説明に使われる速度です。早口（450字/分）はテンポの良いYouTube動画やセミナーで見られます。アナウンサー（500字/分）はニュース番組の読み上げ速度です。</p>

        <h3>プレゼンの時間配分に活用</h3>
        <p>「15分のプレゼンなら何文字の原稿が必要？」という疑問に即答できます。普通の速度（350字/分）で15分なら約5,250文字が目安です。原稿用紙に換算すると約13枚分になります。時間オーバーや時間余りを事前に防ぐことができます。</p>

        <h3>YouTube台本の時間計算にも対応</h3>
        <p>YouTube動画やポッドキャストの台本を書く際に、完成した台本が何分の動画になるかを事前に確認できます。話す速度を調整しながら、目標の動画時間に合わせた台本の長さを計画できます。</p>

        <h3>こんな場面で使えます</h3>
        <p>会社のプレゼンテーション、学校の発表、結婚式の友人代表スピーチ、朝礼の挨拶、YouTube動画の台本、ポッドキャストの原稿、面接の自己PR、卒業式の答辞など。すべてブラウザ上で完結し、入力したテキストがサーバーに送信されることはありません。</p>
    </div>"""
            ),
        ]
    },
    # ===== tool-23: SNS画像サイズ (72表示) =====
    {
        "file": "tool-23-sns-image-sizes/index.html",
        "replacements": [
            # title強化（「twitter 投稿 画像サイズ」でクリックを取る）
            (
                "<title>SNS画像サイズ一覧 | Twitter・Instagram・YouTube推奨サイズ</title>",
                "<title>SNS画像サイズ一覧【2026年最新】X(Twitter)・Instagram・YouTube・LINE推奨サイズ早見表</title>"
            ),
            # description強化
            (
                '<meta name="description" content="X(Twitter)、Instagram、YouTube、LINE、Facebookの推奨画像サイズ一覧。各SNSに最適なサイズが一目でわかる早見表。">',
                '<meta name="description" content="【2026年最新】X(Twitter)投稿画像・Instagramフィード・YouTubeサムネイル・LINEリッチメニュー・Facebookカバーの推奨画像サイズ一覧。各SNSの最適サイズ・アスペクト比が一目でわかる無料早見表。">'
            ),
            # OGP強化
            (
                '<meta property="og:title" content="SNS画像サイズ一覧 | DevTools Japan">',
                '<meta property="og:title" content="SNS画像サイズ一覧【2026年最新】Twitter・Instagram・YouTube推奨サイズ">'
            ),
            (
                '<meta property="og:description" content="各SNSの推奨画像サイズ早見表">',
                '<meta property="og:description" content="X(Twitter)・Instagram・YouTube・LINE・Facebookの推奨画像サイズ・アスペクト比を一覧表示">'
            ),
            (
                '<meta name="twitter:title" content="SNS画像サイズ一覧 | DevTools Japan">',
                '<meta name="twitter:title" content="SNS画像サイズ一覧【2026年最新】推奨サイズ早見表">'
            ),
            (
                '<meta name="twitter:description" content="各SNSの推奨画像サイズ早見表">',
                '<meta name="twitter:description" content="Twitter・Instagram・YouTube・LINE・Facebookの推奨画像サイズ一覧">'
            ),
            # SEOテキスト大幅強化
            (
                """    <div class="seo-content">
        <h2>SNS画像サイズについて</h2>
        <p>SNSに画像を投稿する際、推奨サイズに合わせることで、画質の劣化やトリミングを防ぎ、最適な表示が可能になります。各プラットフォームによって推奨サイズが異なるため、用途に合ったサイズを確認しましょう。</p>
        <p>サイズカードをクリックすると、サイズ情報をクリップボードにコピーできます。</p>
    </div>""",
                """    <div class="seo-content">
        <h2>SNS画像サイズ一覧について</h2>
        <p>SNSに画像を投稿する際、推奨サイズに合わせることで画質の劣化やトリミングを防ぎ、最適な表示が可能になります。各プラットフォームによって推奨サイズが異なるため、投稿前に確認しておくことが重要です。</p>

        <h3>X（旧Twitter）の画像サイズ</h3>
        <p>X（Twitter）の投稿画像は1200×675px（16:9）が推奨です。2枚投稿の場合は700×800px（7:8）になります。ヘッダー画像は1500×500px（3:1）、プロフィール画像は400×400px（1:1）です。画像が推奨サイズと異なると自動トリミングされるため、重要な情報が切れてしまうことがあります。</p>

        <h3>Instagramの画像サイズ</h3>
        <p>Instagramのフィード投稿は正方形1080×1080px（1:1）が基本ですが、縦長1080×1350px（4:5）の方がフィードで大きく表示されるため、エンゲージメントが高くなる傾向があります。ストーリーズとリールは1080×1920px（9:16）の縦型フルスクリーンです。</p>

        <h3>YouTubeの画像サイズ</h3>
        <p>YouTubeサムネイルは1280×720px（16:9）が推奨です。サムネイルは動画のクリック率に直結するため、推奨サイズで高画質な画像を作成することが重要です。チャンネルアートは2560×1440pxですが、デバイスによって表示範囲が変わるため、重要な情報は中央の1546×423pxに収めましょう。</p>

        <h3>LINE・Facebook・OGPのサイズ</h3>
        <p>LINEリッチメニュー（大）は2500×1686px、リッチメッセージは1040×1040pxです。Facebookの投稿画像は1200×630px、カバー画像は851×315pxが推奨です。OGP（Open Graph Protocol）画像は1200×630pxで、SNSでURLがシェアされた時に表示されるプレビュー画像に使われます。</p>

        <h3>画像作成のコツ</h3>
        <p>推奨サイズで作成した画像はファイルサイズが大きくなりがちです。投稿前に画像を圧縮することで、アップロード時間の短縮と表示速度の向上が期待できます。サイズカードをクリックすると、サイズ情報をクリップボードにコピーできます。</p>
    </div>"""
            ),
        ]
    },
    # ===== tool-21: 確定申告シミュレーター (46表示) =====
    {
        "file": "tool-21-tax-simulator/index.html",
        "replacements": [
            # title強化（「副業 確定申告」「副業 税金 シミュレーション」を狙う）
            (
                "<title>確定申告シミュレーター | フリーランス・副業の税金計算</title>",
                "<title>確定申告シミュレーター | 副業・フリーランスの税金・手取り計算【無料】</title>"
            ),
            # description強化
            (
                '<meta name="description" content="フリーランス・副業の所得税・住民税・手取りを自動計算。経費入力で節税額がわかる。確定申告の事前シミュレーションに。">',
                '<meta name="description" content="副業・フリーランスの確定申告を簡単シミュレーション。年間売上・経費・控除を入力するだけで所得税・住民税・手取り額を自動計算。副業の税金がいくらになるか、青色申告の節税効果も一目でわかる無料ツール。">'
            ),
            # OGP強化
            (
                '<meta property="og:title" content="確定申告シミュレーター | DevTools Japan">',
                '<meta property="og:title" content="確定申告シミュレーター | 副業・フリーランスの税金計算【無料】">'
            ),
            (
                '<meta property="og:description" content="フリーランス・副業の所得税・住民税・手取りを自動計算">',
                '<meta property="og:description" content="副業・フリーランスの所得税・住民税・手取りを自動計算。経費入力で節税額がわかる。">'
            ),
            (
                '<meta name="twitter:title" content="確定申告シミュレーター | DevTools Japan">',
                '<meta name="twitter:title" content="確定申告シミュレーター | 副業・フリーランスの税金計算【無料】">'
            ),
            (
                '<meta name="twitter:description" content="フリーランス・副業の所得税・住民税・手取りを自動計算">',
                '<meta name="twitter:description" content="副業の税金がいくらになるか、手取り額を自動計算">'
            ),
            # SEOテキスト大幅強化
            (
                """    <div class="seo-content">
        <h2>確定申告シミュレーターについて</h2>
        <p>フリーランスや副業の方向けに、年間の売上・経費・控除から所得税・住民税・手取りを概算計算するツールです。経費を増やした場合の節税効果もリアルタイムで確認できます。</p>
        <p>青色申告特別控除（65万円/10万円）、基礎控除（48万円）、社会保険料控除に対応。所得税は累進課税率（5%〜45%）に基づいて計算しています。</p>
    </div>""",
                """    <div class="seo-content">
        <h2>副業・フリーランスの確定申告シミュレーター</h2>
        <p>副業やフリーランスで収入を得ている方向けに、年間の売上・経費・控除から所得税・住民税・手取り額を概算計算する無料ツールです。「副業を始めたけど税金がいくらになるかわからない」「確定申告でどれくらい払うことになるの？」という疑問に、数値を入力するだけで即座に回答します。</p>

        <h3>副業の税金シミュレーション</h3>
        <p>会社員が副業で得た収入にかかる税金を事前に把握できます。副業の年間売上から経費を引いた所得が20万円を超える場合、確定申告が必要です。このツールで副業収入を入力すれば、所得税・住民税の概算額と、手元に残る手取り額がすぐにわかります。</p>

        <h3>フリーランスの税金計算</h3>
        <p>フリーランス（個人事業主）の方は、売上から経費を引いた事業所得に対して所得税が課税されます。経費として認められる項目（通信費、家賃按分、交通費、消耗品費、外注費等）を入力することで、経費計上による節税効果をリアルタイムで確認できます。</p>

        <h3>青色申告の節税効果</h3>
        <p>青色申告特別控除（最大65万円）を適用すると、課税所得が大幅に減少し、所得税と住民税が軽減されます。このツールでは青色申告控除額を変更して、白色申告と青色申告の税額の差をシミュレーションできます。65万円控除を受けるには、複式簿記での記帳とe-Taxでの電子申告が必要です。</p>

        <h3>計算に使用している税率</h3>
        <p>所得税は累進課税率（5%〜45%の7段階）に基づいて計算しています。住民税は一律10%（所得割）＋均等割5,000円の概算です。復興特別所得税（所得税額の2.1%）も含めています。基礎控除は48万円（合計所得2,400万円以下の場合）を適用しています。</p>

        <h3>注意事項</h3>
        <p>このツールは概算シミュレーションです。実際の税額は、扶養控除・医療費控除・ふるさと納税等の追加控除や、事業税（290万円超の場合）によって変動します。正確な税額については税理士にご相談ください。すべてブラウザ上で計算され、入力データがサーバーに送信されることはありません。</p>
    </div>"""
            ),
        ]
    },
]

# 実行
for fix in FIXES:
    filepath = os.path.join(BASE, fix["file"])
    if not os.path.exists(filepath):
        print(f"❌ {fix['file']} が見つかりません")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    replaced = 0
    for old, new in fix["replacements"]:
        if old in content:
            content = content.replace(old, new)
            replaced += 1
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ {fix['file']}: {replaced}箇所を置換")

print("\n完了。デプロイ後、Search Console で3つのURLの「インデックス登録をリクエスト」を送信してください。")
print("  https://www.devtools-japan.com/tool-25-speech-time/")
print("  https://www.devtools-japan.com/tool-23-sns-image-sizes/")
print("  https://www.devtools-japan.com/tool-21-tax-simulator/")
