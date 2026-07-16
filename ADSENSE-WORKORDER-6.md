# E-E-A-T 強化（信頼性シグナル）— Claude Code 作業指示書（第6弾）

作成日: 2026-06-19 / 対象: `devtools-japan-complete`
目的: AdSense再申請前の仕上げとして、運営者情報・著者性・信頼性（E-E-A-T）を強化する。コンテンツ量は充足済み（全91ツール＋blog9本）なので、本書は「誰が・どんな方針で・どれだけ信頼できるか」を明示する作業。

## 最重要ルール：捏造禁止（E-E-A-Tは“本物”でないと逆効果）
- **事実でない情報を作らない**。特に禁止：虚偽の個人名・経歴・資格・「税理士監修」等の監修表記・架空の実績や受賞・でっち上げの連絡先。
- **Tom本人しか確定できない情報はプレースホルダ**で残す：`<!-- TODO要記入(Tom): 運営者名/ハンドル -->` のように。該当：運営者の実名orハンドル、連絡手段（フォームor公開用メール）、サイト開設年月、SNS/外部プロフィールURL。
- 著者表記は**「DevTools Japan 編集部」**（組織著者）を既定とする（実在する運営主体＝正直）。個人名を出したい場合のみTomがTODOを埋める。
- 日付は**git履歴等の実日付**を使う（`git log --format=%ai -- <file>` で各記事の作成/最終更新を取得）。憶測の日付禁止。

## 設計・共通
- 既存の白基調デザイン・UX・全処理ブラウザ完結を維持。追加・補強のみ（既存の有用な記述は消さない）。
- 構造化データは妥当なJSON（追加後に必ずparse確認）。

---

## 作業1：Organization 構造化データ（全ページ）
全ページ（最低でも index.html・about・各blog）に Organization のJSON-LDを追加（既存ld+jsonと別ブロックで可）：
```json
{"@context":"https://schema.org","@type":"Organization","name":"DevTools Japan",
 "url":"https://www.devtools-japan.com","logo":"https://www.devtools-japan.com/favicon.svg",
 "description":"日本の開発者・ビジネスパーソン・フリーランス向けの無料オンラインツール集。全処理ブラウザ完結・登録不要。",
 "contactPoint":{"@type":"ContactPoint","contactType":"customer support","url":"https://www.devtools-japan.com/contact/"}
 /* ,"sameAs":[ <!-- TODO要記入(Tom): X/GitHub等のURL --> ] */ }
```
- `sameAs`（SNS等）はTomのプロフィールURLが分かるまでコメントで保留。

## 作業2：blog記事9本の著者性・日付
各 `blog/*/index.html` で:
1. **可視の著者・日付**を本文冒頭（h1直下）に追加：例 `<p class="byline">DevTools Japan 編集部 ・ 公開 2026-06-02 ・ 更新 2026-06-10</p>`（`.byline{color:var(--text3);font-size:0.8rem}` を追加）。日付は **git履歴の実日付**。
2. **BlogPosting JSON-LD を補強**（既存に追記）：`author`（{"@type":"Organization","name":"DevTools Japan 編集部"}）、`datePublished`・`dateModified`（ISO 8601）、`publisher`（Organization＋logo）、`mainEntityOfPage`。
3. 記事末に**出典・参考**（公的情報を引いている記事は国税庁等のURL）と、税/お金記事は「本記事は一般的情報であり税務助言ではない。正確な判断は専門家へ」の免責を1文。

## 作業3：/about/ 強化
既存（1,710字）に以下を追記:
- **運営者**：`DevTools Japan`（運営者名/ハンドルは `<!-- TODO要記入(Tom) -->`）、開設年月 `<!-- TODO要記入(Tom) -->`。
- **専門性・運営方針**：ツールは全てブラウザ内で完結し入力データを送信しないこと、税・法令系は国税庁・財務省・総務省等の**公的情報に基づく概算**であること、数値は計算で検証していること、誤りの指摘を受け付け修正する方針。
- **連絡先**：/contact/ への導線。
- ※ 虚偽の経歴・資格は書かない。

## 作業4：/contact/ 強化（現240字→拡充）
- 問い合わせ方法を明記。**個人のGmailを直書きしない**（スパム/プライバシー）。`<!-- TODO要記入(Tom): 問い合わせフォームURL もしくは 公開用メール -->` を置き、方法が決まるまでは「お問い合わせは準備中／〇〇から」を暫定表示。
- 何に対応するか（ツールの不具合報告・数値の誤り指摘・要望）を案内し、対応姿勢を示す。

## 作業5：/privacy/ 確認・微補強
- 既にAdSense/Cookie/GA開示あり。**Google AdSenseによる広告配信・Cookie利用・パーソナライズ広告のオプトアウト導線（https://www.google.com/settings/ads ）・GA4の利用**が揃っているか確認し、欠けていれば補う。第三者配信事業者の記載も確認。

## 作業6：税/お金ツールの免責の一貫性
- 該当ツール（税・社保・年収の壁・手取り等）に「概算であり、正確な額は公式情報・税理士/自治体で確認」のnoteが入っているか確認、無ければ統一文を追加（監修表記の捏造はしない）。

---

## 品質ゲート
- G1 編集後に各ファイルを読み直し、追記が実在することをgrep確認。
- G3' 触れた全ページで ld+json が妥当なJSON・div開閉一致。Organization/BlogPostingのJSONが`json.loads`で通ること。
- G4 ダークテーマ残骸ゼロ（`.byline`等の追加CSSが白系文字を白地に置かないこと、`--text3`等の既定トークン使用）。
- 日付は全てISO 8601、未来日でないこと、datePublished ≤ dateModified。
- TODOプレースホルダが残る箇所を一覧で報告（Tomが後で埋める）。

## デプロイ
```bash
git add about/index.html privacy/index.html contact/index.html blog/*/index.html index.html
git commit -m "Strengthen E-E-A-T: Organization schema, article author/dates, about/contact enrichment"
git push
```

## 完了の定義
- Organizationデータが主要ページに入る／blog9本に可視の著者・日付＋BlogPosting補強／about・contact拡充／privacy確認／免責一貫。
- **捏造ゼロ**（Tom限定情報はTODOで保留し、その一覧を報告）。
- 既存UI/UX・ツール機能は無改変。
