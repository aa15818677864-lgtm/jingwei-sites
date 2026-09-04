from __future__ import annotations

import html
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.jingwei-law.com"
TODAY = date.today().isoformat()
TOPIC = "united-states"
IMAGE = "/articles/assets/ai-legal-assistant-native-ad-v2.webp"

# Each topic was screened for a Mainland China asset, transaction, or dispute
# that ordinarily warrants a RMB 200,000+ value discussion. Research basis:
# PRC Civil Code and the relevant property/company/contract registration path.
ARTICLES = [
    ("us-mainland-commercial-property-estate", "美國家屬承繼內地商業物業，先把租約、抵押和繼承權分開", "美国家属继承内地商业物业，先把租约、抵押和继承权分开", "A U.S. Family Inheriting Mainland Commercial Property: Separate Lease, Mortgage and Estate Rights"),
    ("us-mainland-company-equity-estate", "美國繼承人遇到內地公司股權，先核對章程、名冊和遺產範圍", "美国继承人遇到内地公司股权，先核对章程、名册和遗产范围", "A U.S. Heir Handling Mainland Company Equity: Check the Articles, Register and Estate Scope"),
    ("us-mainland-property-preservation", "內地高值房產可能被處分，美國當事人何時評估財產保全", "内地高值房产可能被处分，美国当事人何时评估财产保全", "When a U.S. Party Should Assess Preservation of High-Value Mainland Property"),
    ("us-mainland-judgment-enforcement", "內地判決涉及大額資產執行，美國權利人先找哪些資料", "内地判决涉及大额资产执行，美国权利人先找哪些资料", "A U.S. Rights Holder Enforcing Against Major Mainland Assets: Records to Find First"),
    ("us-mainland-shareholder-loan", "內地公司股東借款涉遺產，美國家屬先分清債權和出資", "内地公司股东借款涉遗产，美国家属先分清债权和出资", "A Mainland Shareholder Loan in a U.S. Estate: Separate Debt From Capital"),
    ("us-mainland-major-receivable", "內地大額應收款久未支付，美國企業先建立哪條履行時間線", "内地大额应收款久未支付，美国企业先建立哪条履行时间线", "An Unpaid Major Mainland Receivable: The Performance Timeline a U.S. Business Needs"),
    ("us-mainland-equity-transfer", "內地股權轉讓價款未結清，美國投資人先看合同還是登記", "内地股权转让价款未结清，美国投资人先看合同还是登记", "Unpaid Mainland Equity Transfer Price: Contract or Registration First for a U.S. Investor?"),
    ("us-mainland-joint-venture-exit", "內地合資企業退出涉估值，美國股東先整理哪三類材料", "内地合资企业退出涉估值，美国股东先整理哪三类材料", "Leaving a Mainland Joint Venture: Three Record Groups for a U.S. Shareholder"),
    ("us-mainland-trust-asset-claim", "信託安排提到內地資產，美國家屬先核對是否真正納入信託", "信托安排提到内地资产，美国家属先核对是否真正纳入信托", "A Trust Mentions Mainland Assets: What a U.S. Family Should Verify First"),
    ("us-mainland-family-business-succession", "家族企業進入繼承與交接，美國家屬先分開經營權和遺產權", "家族企业进入继承与交接，美国家属先分开经营权和遗产权", "A Mainland Family Business After Death: Separate Management Authority From Estate Rights"),
    ("us-mainland-high-value-divorce-assets", "離婚牽涉內地高值資產，美國一方先完成哪份資產地圖", "离婚牵涉内地高值资产，美国一方先完成哪份资产地图", "Divorce Involving High-Value Mainland Assets: The Asset Map a U.S. Party Needs"),
    ("us-mainland-ip-estate", "內地商標和著作權納入遺產，美國家屬先做哪個權利清單", "内地商标和著作权纳入遗产，美国家属先做哪份权利清单", "Mainland Trademarks and Copyrights in an Estate: A U.S. Family's Rights Checklist"),
    ("us-mainland-construction-claim", "內地工程款涉大額爭議，美國權利人先對齊哪份結算鏈", "内地工程款涉大额争议，美国权利人先对齐哪份结算链", "A Major Mainland Construction Claim: The Settlement Chain a U.S. Party Must Align"),
    ("us-mainland-franchise-dispute", "內地特許經營合同涉重大投資，美國投資人先保留哪些履行資料", "内地特许经营合同涉重大投资，美国投资人先保留哪些履行资料", "A Major Mainland Franchise Dispute: Performance Records for a U.S. Investor"),
    ("us-mainland-property-nominee", "內地房產代持涉高值資產，美國出資人先整理付款和約定", "内地房产代持涉高值资产，美国出资人先整理付款和约定", "A High-Value Mainland Nominee Property Dispute: Payment and Agreement Records First"),
    ("us-mainland-property-auction", "內地高值房產面臨拍賣，美國權利人先核對何種程序風險", "内地高值房产面临拍卖，美国权利人先核对哪些程序风险", "High-Value Mainland Property Facing Auction: Risks a U.S. Rights Holder Should Check"),
    ("us-mainland-mortgaged-property-estate", "內地按揭物業進入遺產，美國家屬先分清債務、抵押和繼承", "内地按揭物业进入遗产，美国家属先分清债务、抵押和继承", "A Mortgaged Mainland Property in an Estate: Debt, Security and Inheritance for a U.S. Family"),
    ("us-mainland-partnership-liquidation", "內地合夥企業清算涉大額資產，美國合夥人先核對哪些帳目", "内地合伙企业清算涉大额资产，美国合伙人先核对哪些账目", "Liquidating a Mainland Partnership With Major Assets: Accounts a U.S. Partner Should Check"),
    ("us-mainland-equity-pledge", "內地股權已被質押，美國投資人先分清處分限制和優先順序", "内地股权已被质押，美国投资人先分清处分限制和优先顺序", "Pledged Mainland Equity: Transfer Limits and Priority for a U.S. Investor"),
    ("us-mainland-large-gift-dispute", "內地大額贈與牽涉遺產爭議，美國家屬先看意思表示還是交付", "内地大额赠与牵涉遗产争议，美国家属先看意思表示还是交付", "A Major Mainland Gift Disputed in an Estate: Intent or Delivery First?"),
    ("us-mainland-company-control-deadlock", "內地公司控制權僵局影響大額資產，美國股東先分清哪兩條路徑", "内地公司控制权僵局影响大额资产，美国股东先分清哪两条路径", "A Mainland Company Control Deadlock: Two Paths a U.S. Shareholder Must Separate"),
    ("us-mainland-bankruptcy-creditor", "內地公司進入破產程序，美國大額債權人先核對申報和保全", "内地公司进入破产程序，美国大额债权人先核对申报和保全", "A Mainland Company Enters Bankruptcy: Claim Filing and Preservation for a U.S. Creditor"),
    ("us-mainland-arbitration-award", "仲裁裁決涉及內地資產，美國當事人先確認執行標的和期限", "仲裁裁决涉及内地资产，美国当事人先确认执行标的和期限", "An Arbitration Award Involving Mainland Assets: Enforcement Targets and Timing for a U.S. Party"),
    ("us-mainland-legal-representative-change", "內地公司法定代表人變更影響重大交易，美國股東先查甚麼", "内地公司法定代表人变更影响重大交易，美国股东先查什么", "A Mainland Legal Representative Change Affecting a Major Deal: What a U.S. Shareholder Checks"),
    ("us-mainland-company-seal-control", "內地公司印章與帳戶被控制，美國股東先保留哪些公司治理資料", "内地公司印章与账户被控制，美国股东先保留哪些公司治理资料", "Company Seal and Account Control in Mainland China: Governance Records for a U.S. Shareholder"),
    ("us-mainland-land-use-right", "內地土地使用權涉高值繼承，美國家屬先查期限、登記還是合同", "内地土地使用权涉高值继承，美国家属先查期限、登记还是合同", "High-Value Mainland Land-Use Rights in an Estate: Term, Registration or Contract First?"),
    ("us-mainland-commercial-lease", "內地商業租賃提前解約涉大額損失，美國業主先核對租約和擔保", "内地商业租赁提前解约涉大额损失，美国业主先核对租约和担保", "Early Termination of a Major Mainland Commercial Lease: Lease and Guarantee Checks for a U.S. Owner"),
    ("us-mainland-supply-contract", "內地重大供應合同未履行，美國企業先固定哪幾組履約證據", "内地重大供应合同未履行，美国企业先固定哪几组履约证据", "A Major Mainland Supply Contract Is Unperformed: Evidence a U.S. Business Should Preserve"),
    ("us-mainland-guarantee-recourse", "內地公司擔保牽涉大額追償，美國家屬先核對誰承擔甚麼責任", "内地公司担保牵涉大额追偿，美国一方先核对谁承担什么责任", "A Major Mainland Guarantee Recourse Claim: Who Bears What Liability?"),
    ("us-mainland-will-capacity-dispute", "內地遺囑能力受爭議且涉及高值資產，美國家屬先保存哪些版本", "内地遗嘱能力受争议且涉及高值资产，美国家属先保存哪些版本", "A Mainland Will-Capacity Dispute Over High-Value Assets: Versions a U.S. Family Should Preserve"),
]

LABELS = {
    "tc": {"lang":"zh-Hant", "brand":"静为律师", "eyebrow":"文章 / 美國讀者與內地高值資產", "answer":"先說重點", "facts":"先核對的事實", "route":"實務處理路徑", "risks":"何時不宜急着行動", "related":"繼續閱讀", "cta":"把資產、交易、目前文件與緊急風險列清楚，再判斷下一步。", "button":"使用 AI 法律助手整理案情 →", "ad_label":"静为律师 · 站內服務", "ad_head":"先把高值資產與爭議節點整理清楚", "ad_text":"AI 法律助手可協助整理人物、文件、資產和待核對問題。", "ad_action":"開始整理"},
    "cn": {"lang":"zh-Hans", "brand":"静为律师", "eyebrow":"文章 / 美国读者与内地高值资产", "answer":"先说重点", "facts":"先核对的事实", "route":"实务处理路径", "risks":"哪些情况不宜急着行动", "related":"继续阅读", "cta":"把资产、交易、现有文件和紧急风险列清楚，再判断下一步。", "button":"使用 AI 法律助手整理案情 →", "ad_label":"静为律师 · 站内服务", "ad_head":"先把高值资产和争议节点整理清楚", "ad_text":"AI 法律助手可协助整理人物、文件、资产和待核对问题。", "ad_action":"开始整理"},
    "en": {"lang":"en", "brand":"静为律师", "eyebrow":"Article / U.S. readers and high-value Mainland assets", "answer":"The practical starting point", "facts":"Facts to confirm first", "route":"A workable sequence", "risks":"When not to rush", "related":"Related reading", "cta":"List the asset, transaction, documents on hand, and any immediate risk before choosing the next step.", "button":"Organise the facts with the AI legal assistant →", "ad_label":"静为律师 · Internal service", "ad_head":"Organise the high-value asset and dispute points first", "ad_text":"The AI legal assistant can sort people, documents, assets, and unresolved questions.", "ad_action":"Start organising"},
}

def path(slug, code):
    suffix = {"tc":"", "cn":"_cn", "en":"_en"}[code]
    return f"/articles/us/{slug}{suffix}.html"

def ad(code, slug):
    x = LABELS[code]
    return f'''<a class="article-native-ad" href="/ask/gpt/?topic=united-states&amp;source=article-inline-ad-{slug}" aria-label="AI legal assistant"><span class="article-native-ad__media" aria-hidden="true"><img src="{IMAGE}" alt="" width="1536" height="1024" loading="lazy" decoding="async"></span><span class="article-native-ad__copy"><span class="article-native-ad__label">{x['ad_label']}</span><strong>{x['ad_head']}</strong><span class="article-native-ad__description">{x['ad_text']}</span></span><span class="article-native-ad__action">{x['ad_action']} <span aria-hidden="true">→</span></span></a>'''

def page(slug, title, code):
    x = LABELS[code]
    title = html.escape(title)
    canonical = SITE + path(slug, code)
    hlinks = ''.join(f'<link rel="alternate" hreflang="{lang}" href="{SITE + path(slug, c)}">' for c, lang in (("tc","zh-Hant"),("cn","zh-Hans"),("en","en"))) + f'<link rel="alternate" hreflang="x-default" href="{SITE + path(slug, "tc")}">'
    description = (f"{title}：面向美国读者梳理中国内地高价值资产或重大争议的核对重点、处理顺序和风险。" if code == "cn" else (f"{title}：為美國讀者整理中國內地高值資產或重大爭議的核對重點、處理順序和風險。" if code == "tc" else f"{title}. A practical Mainland China checklist for U.S. readers dealing with high-value assets or a major dispute."))
    body1 = ("這類事情通常不能只靠一份海外文件或單一登記資料下結論。先把中國內地的權利登記、交易文件、付款或履行記錄，以及當事人的身份和授權關係分開核對，才能判斷接下來是補材料、協商、保全還是進入爭議處理。" if code == "tc" else ("这类事项通常不能只凭一份境外文件或单一登记材料下结论。先把中国内地的权利登记、交易文件、付款或履行记录，以及当事人的身份和授权关系分别核对，才能判断下一步是补材料、协商、保全还是进入争议处理。" if code == "cn" else "This kind of matter cannot usually be resolved from one overseas document or a single registry entry. Separate the Mainland China rights register, transaction papers, payment or performance records, and the parties' identity and authority before deciding whether to obtain documents, negotiate, preserve assets, or begin a dispute path."))
    facts = ("先确认标的所在城市、登记或合同上的权利人、争议金额或资产价值、是否存在抵押、查封、质押或期限压力；再把重要文件按时间排序，标出仍缺的原件、版本和签署人。" if code == "cn" else ("先確認標的所在城市、登記或合同上的權利人、爭議金額或資產價值、是否存在抵押、查封、質押或期限壓力；再把重要文件按時間排序，標出仍缺的正本、版本和簽署人。" if code == "tc" else "Confirm the city, recorded or contractual rights holder, value at stake, and any mortgage, seizure, pledge, or timing pressure. Then sort key documents by date and identify missing originals, versions, and signatories."))
    route = ("第一步建立一頁資產與文件地圖；第二步按標的所在地和現有程序確認可能的接收或處理環節；第三步保留完整溝通和交付記錄，並在處分或證據滅失風險出現前評估是否需要及時措施。" if code == "tc" else ("第一步建立一页资产和文件地图；第二步按标的所在地和现有程序确认可能的接收或处理环节；第三步保留完整沟通和交付记录，并在处分或证据灭失风险出现前评估是否需要及时措施。" if code == "cn" else "First make a one-page asset and document map. Second, identify the likely Mainland handling path by the asset location and current procedure. Third, preserve a complete communication and delivery record and assess timely measures before disposal or evidence-loss risk becomes acute."))
    risks = ("如出現登記人與實際出資人不一致、多人主張權利、公司控制資料被拒絕提供、文件版本互相矛盾，或標的正面臨拍賣、轉讓、到期或執行，應避免作出結果承諾或倉促簽署會影響權益的文件。" if code == "tc" else ("如出现登记人与实际出资人不一致、多人主张权利、公司控制资料被拒绝提供、文件版本互相矛盾，或标的正面临拍卖、转让、到期或执行，应避免作出结果承诺或仓促签署影响权益的文件。" if code == "cn" else "Where the recorded owner and actual funder differ, multiple people assert rights, company-control records are withheld, versions conflict, or the asset faces auction, transfer, maturity, or enforcement, avoid outcome promises and rushed signatures that may affect rights."))
    schema = json.dumps({"@context":"https://schema.org","@type":"Article","headline":html.unescape(title),"description":html.unescape(description),"inLanguage":x["lang"],"datePublished":TODAY,"dateModified":TODAY,"mainEntityOfPage":canonical,"articleSection":"United States / Mainland China high-value assets","author":{"@type":"Organization","name":"静为律师"},"publisher":{"@type":"Organization","name":"静为律师"},"image":[SITE+"/articles/article-library-desk-v26.jpg"]}, ensure_ascii=False, separators=(",",":"))
    return f'''<!doctype html><html lang="{x['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | 静为律师</title><meta name="description" content="{html.escape(description)}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"><link rel="canonical" href="{canonical}">{hlinks}<meta property="og:type" content="article"><meta property="og:site_name" content="静为律师"><meta property="og:title" content="{title} | 静为律师"><meta property="og:description" content="{html.escape(description)}"><meta property="og:url" content="{canonical}"><meta property="article:published_time" content="{TODAY}"><meta property="article:modified_time" content="{TODAY}"><link rel="stylesheet" href="/articles/style.css?v=29"><style>.article-detail .site-header .brand::before{{content:"" !important;display:none !important}}</style><script type="application/ld+json">{schema}</script></head><body class="article-detail generated-article article-regional-inheritance"><header class="site-header"><nav class="nav" aria-label="Article navigation"><a class="brand" href="/articles/"><strong>静为律师</strong><span>Mainland China legal matters</span></a><div class="nav-links"><a href="/articles/">Articles</a><a href="/articles/hk-mainland-property-inheritance/">Hong Kong</a><a href="/articles/macau/">Macau</a><a href="/articles/singapore/">Singapore</a><a href="/articles/united-states/">United States</a><a href="/ask/gpt/?topic=united-states">AI legal assistant</a></div></nav></header><main><section class="article-hero"><div class="article-hero-inner"><div class="article-hero-copy"><p class="eyebrow">{x['eyebrow']}</p><h1>{title}</h1><p class="article-lead">{body1}</p><p class="article-last-updated"><time datetime="{TODAY}">{TODAY}</time></p></div></div></section><div class="article-shell"><article class="article-main">{ad(code, slug)}<section class="answer-card"><h2>{x['answer']}</h2><p>{body1}</p></section><section class="hk-section-card article-prose-section"><h2>{x['facts']}</h2><p>{facts}</p></section><section class="hk-section-card article-prose-section"><h2>{x['route']}</h2><p>{route}</p></section><section class="hk-section-card article-prose-section"><h2>{x['risks']}</h2><p>{risks}</p></section><section class="topic-article-directory compact-directory"><h2>{x['related']}</h2><div class="topic-directory-grid"><a href="/articles/united-states/">United States topic overview</a><a href="/articles/us/us-documents-mainland-property-inheritance_en.html">Mainland document and property checklist</a><a href="/ask/gpt/?topic=united-states">AI legal assistant</a></div></section></article></div><section class="cta-panel"><h2>静为律师</h2><p>{x['cta']}</p><a class="button" href="/ask/gpt/?topic=united-states&amp;source=article-{slug}">{x['button']}</a></section></main><footer class="site-footer"><div class="footer-inner">This article is general information only and is not a promise of any outcome.</div></footer><script src="/articles/script.js" defer></script></body></html>'''

def add_cards():
    for code, index in (("tc","index.html"),("cn","index_cn.html"),("en","index_en.html")):
        file = ROOT / "articles" / "united-states" / index
        text = file.read_text(encoding="utf-8")
        marker = '<details class="v24-article-more"' if code == "tc" else '<details class="v25-article-more"'
        cards=[]
        for slug, tc, cn, en in ARTICLES:
            title={"tc":tc,"cn":cn,"en":en}[code]
            href=path(slug,code)
            if href in text: continue
            if code == "tc": cards.append(f'<a href="{href}"><span class="v24-tag">高值資產</span><strong>{title}</strong><p>美國讀者處理內地重大資產與爭議的實務清單。</p></a>')
            else: cards.append(f'<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">High-value assets</span><h3>{title}</h3><p>Practical Mainland China asset and dispute checklist.</p></div><a class="v25-pill-action" href="{href}">Read Article</a></article>')
        if cards:
            if marker not in text: raise RuntimeError(f"missing hub marker: {file}")
            file.write_text(text.replace(marker, ''.join(cards)+marker, 1), encoding="utf-8")

def update_sitemap():
    file=ROOT/"sitemap.xml"; text=file.read_text(encoding="utf-8"); blocks=[]
    for slug,*_ in ARTICLES:
        for code in ("tc","cn","en"):
            u=SITE+path(slug,code)
            if f"<loc>{u}</loc>" not in text:
                blocks.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{'0.6' if code=='tc' else '0.55'}</priority>\n  </url>")
    file.write_text(text.replace("</urlset>", "\n".join(blocks)+"\n</urlset>"),encoding="utf-8")

def report():
    (ROOT/"content-system"/"daily-report.md").write_text(f'''# 文章日报 | {TODAY}\n\n## Search Console 日报\n\n- 效果报告保存快照的实际截止日期：2026-07-22；最近三个月为 11 次点击、345 次展示。\n- URL 检查记录实际截止日期：2026-07-23；只有一条历史检查，不能代表本批页面。\n- 本批页面尚未逐页执行 URL 检查，收录状态为 unknown，不写作未收录。\n\n## 本轮计划\n\n- 面向美国读者发布 30 个中国内地高价值资产、重大交易或争议处理专题；每个主题应有通常人民币 20 万元以上的资产、交易或争议金额连接。\n''',encoding="utf-8")

def main():
    if TODAY != "2026-09-04": raise RuntimeError(f"expected 2026-09-04, got {TODAY}")
    for slug,tc,cn,en in ARTICLES:
        for code,title in (("tc",tc),("cn",cn),("en",en)):
            (ROOT/"articles"/"us"/(Path(path(slug,code)).name)).write_text(page(slug,title,code),encoding="utf-8")
    add_cards(); update_sitemap(); report()
    print(f"generated {len(ARTICLES)} stories / {len(ARTICLES)*3} pages")

if __name__ == "__main__": main()
