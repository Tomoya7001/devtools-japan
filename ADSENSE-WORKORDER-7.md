# E-E-A-T TODO埋め込み（運営者情報確定）— Claude Code 作業指示書（第7弾）

作成日: 2026-06-19 / 対象: `devtools-japan-complete`
Tom本人が確定した値を、第6弾で残したTODOプレースホルダに反映する。**捏造でなく本人確定値**。

## 確定値
- 運営者ハンドル：**Tomoya7001**
- サイト開設：**2026年3月**
- sameAs（公式プロフィール）：**https://github.com/Tomoya7001**（掲載可）
- contact：現状維持（Formspreeフォーム稼働中・変更不要）

## 作業（macOS。Linuxなら `sed -i ''`→`sed -i`）
```bash
cd ~/Desktop/devtools-japan-complete

# 対象：Organizationを持つ14ページ
FILES=$(grep -rl '"@type":"Organization"' index.html about/index.html contact/index.html privacy/index.html blog/*/index.html)

# 1) Organization JSON-LD に sameAs を追加（contactPoint直後に挿入）
echo "$FILES" | tr ' ' '\n' | xargs sed -i '' 's#"contactType":"customer support","url":"https://www.devtools-japan.com/contact/"}}#"contactType":"customer support","url":"https://www.devtools-japan.com/contact/"},"sameAs":["https://github.com/Tomoya7001"]}#g'

# 2) sameAsのTODOコメント行を削除（用済み）
echo "$FILES" | tr ' ' '\n' | xargs sed -i '' '/TODO要記入(Tom): OrganizationのsameAs/d'

# 3) about：運営者ハンドルと開設年月
sed -i '' 's#DevTools Japan（<!-- TODO要記入(Tom): 運営者の実名またはハンドル -->）#DevTools Japan（運営者: Tomoya7001）#' about/index.html
sed -i '' 's#<strong>サイト開設</strong>：<!-- TODO要記入(Tom): 開設年月 -->#<strong>サイト開設</strong>：2026年3月#' about/index.html
```
※ tool側に残る `// TODO要確認:`（税の不確実値）は**別物。絶対に削除しない**。本作業が消すのは `TODO要記入(Tom)` のみ。

## 検証（必須・全パス）
```bash
cd ~/Desktop/devtools-japan-complete
echo "sameAs設置(14期待):"; grep -rl '"sameAs":\["https://github.com/Tomoya7001"\]' index.html about/index.html contact/index.html privacy/index.html blog/*/index.html | wc -l
echo "TODO要記入の残り(0期待):"; grep -rn 'TODO要記入' index.html about contact privacy blog 2>/dev/null | wc -l
echo "TODO要確認は温存されているか(>0期待・税ツール):"; grep -rl 'TODO要確認' tool-*/index.html | wc -l
echo "about 反映確認:"; grep -nE 'Tomoya7001|2026年3月' about/index.html
# JSON-LD妥当性＆div開閉（触れた14ファイル）
python3 - <<'PY'
import re,json,glob
files=['index.html','about/index.html','contact/index.html','privacy/index.html']+glob.glob('blog/*/index.html')
ng=[]
for f in files:
    h=open(f,encoding='utf-8').read()
    if len(re.findall(r'<div\b',h))!=len(re.findall(r'</div>',h)): ng.append(('div',f))
    for b in re.findall(r'application/ld\+json">(.*?)</script>',h,re.S):
        try: json.loads(b)
        except Exception as e: ng.append(('json',f,str(e)))
print("問題:", ng or "なし(全妥当)")
PY
```

## デプロイ（llms.txtの未コミット分も一緒に）
```bash
git add index.html about/index.html contact/index.html privacy/index.html blog/*/index.html llms.txt
git commit -m "Fill E-E-A-T operator info (sameAs GitHub, handle, founding); update llms.txt for tools 71-91"
git push
```

## 完了の定義
- sameAs が14ページに入る／`TODO要記入` 残り0／税ツールの `TODO要確認` は温存／about に「Tomoya7001」「2026年3月」反映／JSON-LD全妥当・div一致。
