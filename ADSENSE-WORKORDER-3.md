# ダークテーマ残骸の色修正 — Claude Code 作業指示書（第3弾）

作成日: 2026-06-10 / 対象リポジトリ: `devtools-japan-complete`

## 背景
サイトは白基調テーマだが、旧ネイビー背景時代の色指定が一部に残り、白地で見えない/暗い箱になっている。**個別の確定バグ（tool-11 Markdownプレビュー、tool-24 OGPプレビュー）は対応済み**。本書は**全ツール共通の共有コンポーネント2点**を、全ツール一括で白基調に統一する。

## 方針
「白基調で読みやすく・他と統一感がある」状態にする。**機能・レイアウト・JSには一切触れず、指定の文字列を置換するだけ**。

---

## 修正1：ヘッダー「DevTools Japan トップへ」リンクのホバー白化（全50ツール）
ホバーで文字色が `#e4e4f0`（ほぼ白）になり白地で消える。ホバーで「暗くなる」よう修正。

- **対象文字列（全ツール完全一致・50箇所）**
  ```
  onmouseover="this.style.color='#e4e4f0'" onmouseout="this.style.color='#8888a8'"
  ```
- **置換後**
  ```
  onmouseover="this.style.color='#1e1e35'" onmouseout="this.style.color='#8888a8'"
  ```
- つまり `'#e4e4f0'`（onmouseover側のみ）→ `'#1e1e35'`。onmouseout側の `#8888a8` は変更しない。

## 修正2：「関連ツール」「API」ブロックのチップが黒背景（全50ツール・157箇所）
`--bg-elevated` が未定義のため、フォールバックの `#0c0c14`（ほぼ黒）が背景に出ている。白系に変更。

- **対象文字列**
  ```
  var(--bg-elevated,#0c0c14)
  ```
- **置換後**
  ```
  var(--bg-elevated,#f7f8fb)
  ```
- ※ 同ブロックの `var(--border,#1e1e30)` `var(--text,#e4e4f0)` `var(--bg-card,#111118)` `var(--accent,#6366f1)` は、`:root` で `--border/--text/--bg-card/--accent` が定義済みのため明るい値に解決される＝**変更不要**。`var(--text-secondary,#8888a8)` `var(--text-muted,#4a4a68)` も白地で可読＝**変更不要**。触るのは `#0c0c14` のみ。

---

## 実施方法（推奨：スクリプトで一括）
```bash
cd ~/Desktop/devtools-japan-complete
# 修正1
grep -rl "this.style.color='#e4e4f0'" tool-*/index.html | xargs sed -i '' "s/this\.style\.color='#e4e4f0'/this.style.color='#1e1e35'/g"
# 修正2
grep -rl "var(--bg-elevated,#0c0c14)" tool-*/index.html | xargs sed -i '' "s/var(--bg-elevated,#0c0c14)/var(--bg-elevated,#f7f8fb)/g"
```
※ macOSの `sed -i ''` 構文。Linux環境なら `sed -i`。手作業置換でも可。

---

## ガードレール（厳守）
- 置換するのは上記2パターンの**該当文字列のみ**。HTML構造・JS・レイアウト・他の色は触らない。
- 確定対応済みの tool-11 / tool-24 は**再変更しない**。

## 検証（必須）
```bash
cd ~/Desktop/devtools-japan-complete
echo "残存(0が正常):"
grep -rc "this.style.color='#e4e4f0'" tool-*/index.html | grep -v ':0' | wc -l
grep -rc "var(--bg-elevated,#0c0c14)" tool-*/index.html | grep -v ':0' | wc -l
# div開閉バランス全ツール
python3 - <<'PY'
import re,glob
ng=[f for f in glob.glob("tool-*/index.html") if len(re.findall(r'<div\b',open(f,encoding='utf-8').read()))!=len(re.findall(r'</div>',open(f,encoding='utf-8').read()))]
print("div崩れ:", ng or "なし")
PY
```
- 代表ツール（tool-11, tool-29, tool-57 等）をブラウザで開き、(a)ヘッダーのトップへリンクがホバーで消えない (b)関連ツールチップが白系で読める (c)ツール機能は従来通り、を目視確認。

## デプロイ
```bash
git add tool-*/index.html
git commit -m "Fix dark-theme color remnants (back-link hover, related-tools chip bg) site-wide"
git push   # SSH・Vercel自動
```

## 完了の定義
- 上記2パターンの残存0、div崩れ0。
- ヘッダーリンクのホバーで文字が消えない／関連ツールチップが白基調で可読。
- 全ツールでツール機能（UI/JS）は無改変。
