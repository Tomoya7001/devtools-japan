# 【引き継ぎ】第5弾P2の続き — Claude Code 作業指示書（再開用）

作成日: 2026-06-16 / 対象: `devtools-japan-complete`（本リポジトリ）
前のセッションが不具合で中断したため、**正確な現状から再開**するための指示書。

## まず読むもの
- `ADSENSE-WORKORDER-5.md`（P2の全体仕様）
- `ADSENSE-WORKORDER-4.md`（§1〜§5：設計・コンテンツ基準・品質ゲートG1〜G6。**全継承**）
- 雛形にする既存ツール：税系=`tool-73-retirement-tax`、お金系=`tool-64-take-home-pay`、文字数系=`tool-25-speech-time`。

## 正確な現状（実ファイル確認済み・2026-06-16）
- **push済み（完成）**：tool-86-tax-refund / tool-87-pdf-split / tool-88-image-resize / tool-89-warikan / tool-90-ogp-image / tool-91-countdown の6本（各index.htmlあり・コミット済み）。
- **未作成**：`tool-85-year-end-tax`（年末調整 還付金シミュレーター）はディレクトリごと未作成。※還付額の計算式＝「追加控除額 × 限界税率 × 1.021」は前セッションでPython検証済み。
- **未更新**：`index.html` はツール数「84」のまま＝新ツール6本のカード未登録。`sitemap.xml` は98URLのまま＝新6本未追加。
- **注意**：`.git/index.lock` が残っている可能性。git操作前に `rm -f .git/index.lock` を実行。

## 最初にやること（思い込み防止）
1. `rm -f .git/index.lock` → `git status` / `git log --oneline -8` で実状態を確認。
2. `ls -d tool-8*/ tool-9*/` でディレクトリ実在を確認。報告と食い違えば**実態を優先**。

## 残作業（この順で）
1. **tool-85-year-end-tax を新規作成**（品質基準で）。
   - 内容：年末調整の還付金シミュレーター。生命保険料控除・扶養・配偶者控除等の「追加控除」を入れると還付見込みを概算。
   - 計算：還付 ≈ 追加控除額 × 限界税率 × 1.021（復興特別所得税込み）。**前セッション検証済みの式に整合**させ、別途Python/nodeで独立再計算してassert。
   - 正確性：国税庁準拠、令和8年（2026）値・適用時期を明記、不確実値は `// TODO要確認:` ＋出典。「概算・正確な額は勤務先/税理士で確認」のnote。
   - コンテンツ：可視1,000字以上＋早見表＋FAQ5（**見える本文とFAQPage JSON-LDを5問一致**）。
2. **index.html を更新**：未登録の新ツール **85〜91（計7本）** のカードを一覧に追加、**ツール数表記を全箇所「91」に統一**（「84」「90」等の残存ゼロをgrepで確認）、関連ツール内部リンク。
3. **sitemap.xml に 85〜91 の7URLを追加**＋lastmod更新（XML妥当性確認）。
4. **品質ゲートG1〜G6を新ツール全数（85〜91）で実施**：
   - G1 編集後にファイルを読み直し実在確認（ハーネス不整合対策）。
   - G2 計算（tool-85還付）を独立再計算assert。
   - G3 div開閉一致／ld+json妥当・FAQPage1個／可視1000字以上／FAQ本文=JSON-LD件数。
   - G4 ダークテーマ残骸ゼロ（`color:#fff`等の白文字が暗背景なしで無い／`var(--bg-elevated,#0c0c14)`無し／back-linkホバー非白）。
   - G5 ファイル系（87 PDF分割/88 画像リサイズ/90 OGP生成）は実ファイルで動作確認（可能なら）。
   - G6 ツール数=91をnode eval/grepで確認、index.html div一致、sitemap妥当、非cdnjs外部スクリプトなし。
5. **数本ごとに** `git add` →commit→ `git push`（SSH・Vercel自動）。

## 完了の定義
- tool-85完成（1,000字＋FAQ5＋公式準拠＋TODO残置）、85〜91がindex/sitemapに登録、ツール数「91」統一、G1〜G6全パス。
- 既存ツール・UI/JSは無改変（追加のみ）。
- 完了後、何をどう検証して通したかのサマリーを報告。
