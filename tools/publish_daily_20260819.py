from __future__ import annotations

import html
import json
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.jingwei-law.com"
DIR = ROOT / "articles" / "hong-kong-other-estate"
TODAY = date.today().isoformat()

# Each entry is a distinct Hong Kong reader situation involving a Mainland
# handling step.  The public copy deliberately states a process, not an
# outcome or a claim that one document is universally sufficient.
STORIES = [
    ("estate-safe-deposit-box-clues", "香港家屬找到內地保管箱線索，先不要急著開箱", "香港家属找到内地保管箱线索，先不要急着开箱", "A Mainland Safe-Deposit-Box Clue: What a Hong Kong Family Should Do First", "保管箱線索", "保管箱线索", "a safe-deposit-box clue"),
    ("mainland-rental-deposit-after-death", "內地出租屋的押金未退，香港家屬先核對哪份租約", "内地出租屋的押金未退，香港家属先核对哪份租约", "A Mainland Rental Deposit Is Still Outstanding After Death", "租約及押金", "租约和押金", "an outstanding rental deposit"),
    ("estate-property-management-notices", "內地物業管理通知一直寄來，先分清費用、權屬和聯絡人", "内地物业管理通知一直寄来，先分清费用、权属和联系人", "Mainland Property-Management Notices Keep Arriving", "物業管理通知", "物业管理通知", "property-management notices"),
    ("mainland-utility-account-after-death", "內地水電帳戶仍在扣款，香港家屬怎樣留下可核對紀錄", "内地水电账户仍在扣款，香港家属怎样留下可核对记录", "A Mainland Utility Account Is Still Being Charged", "水電帳戶", "水电账户", "a continuing utility account"),
    ("estate-mobile-phone-evidence", "遺產手機裡有內地帳戶訊息，先保存哪些內容才不越界", "遗产手机里有内地账户信息，先保存哪些内容才不越界", "A Deceased Person’s Phone Contains Mainland Account Clues", "手機訊息", "手机信息", "phone-based account clues"),
    ("mainland-cloud-account-clues", "雲端相簿和電郵裡有內地資產線索，先做哪一張索引表", "云端相册和邮件里有内地资产线索，先做哪一张索引表", "Mainland Asset Clues in Cloud Photos and Email", "雲端資料", "云端资料", "cloud-based asset clues"),
    ("estate-wechat-payment-records", "微信付款紀錄能否幫忙找內地遺產線索，先分清甚麼", "微信付款记录能否帮忙找内地遗产线索，先分清什么", "Can WeChat Payment Records Help Trace a Mainland Estate?", "付款紀錄", "付款记录", "payment-record clues"),
    ("mainland-business-seal-custody", "已故家人留下內地公司印章，保管和公司決定要分開", "已故家人留下内地公司印章，保管和公司决定要分开", "A Deceased Relative Left a Mainland Company Seal", "公司印章", "公司印章", "a Mainland company seal"),
    ("estate-company-bank-token", "內地公司網銀令牌在家屬手上，不等於可以處理公司款項", "内地公司网银令牌在家属手上，不等于可以处理公司款项", "A Family Holds a Mainland Company Banking Token", "網銀令牌", "网银令牌", "a company banking token"),
    ("mainland-share-pledge-clues", "發現內地股權可能已質押，香港家屬先查權利還是先談繼承", "发现内地股权可能已质押，香港家属先查权利还是先谈继承", "A Mainland Shareholding May Be Pledged", "股權質押", "股权质押", "a potentially pledged shareholding"),
    ("estate-unpaid-dividend-notice", "內地公司通知有未領分紅，先分清公司資料和繼承資料", "内地公司通知有未领分红，先分清公司资料和继承资料", "A Mainland Company Says a Dividend Is Unclaimed", "未領分紅", "未领分红", "an unclaimed dividend"),
    ("mainland-invoice-and-receivable-clues", "家中只找到發票和對賬單，怎樣先判斷是內地遺產線索還是公司帳", "家中只找到发票和对账单，怎样先判断是内地遗产线索还是公司账", "Invoices and Statements May Point to a Mainland Estate", "發票及對賬", "发票和对账", "invoices and account statements"),
    ("estate-court-notice-address-change", "內地法院材料寄到舊地址，香港家屬第一天先保留甚麼", "内地法院材料寄到旧地址，香港家属第一天先保留什么", "A Mainland Court Notice Arrived at an Old Address", "法院材料", "法院材料", "a court notice"),
    ("mainland-enforcement-payment-clues", "內地判決已有付款線索，香港家屬先把哪三組資料對上", "内地判决已有付款线索，香港家属先把哪三组资料对上", "A Mainland Judgment Has Payment Clues", "判決及付款", "判决和付款", "judgment-payment clues"),
    ("estate-land-registry-search-clues", "只知道內地房屋可能轉過名，香港家屬先整理哪些查檔線索", "只知道内地房屋可能转过名，香港家属先整理哪些查档线索", "A Mainland Home May Have Changed Title", "房屋查檔", "房屋查档", "possible title-change clues"),
    ("mainland-parking-space-estate", "內地車位和住宅分開登記，遺產清單怎樣先不漏項", "内地车位和住宅分开登记，遗产清单怎样先不漏项", "A Mainland Parking Space May Be Separate Estate Property", "車位登記", "车位登记", "a separately registered parking space"),
    ("estate-storage-unit-contents", "內地儲物間裡有文件和物品，先保管還是先分配", "内地储物间里有文件和物品，先保管还是先分配", "Documents and Belongings Are in a Mainland Storage Unit", "儲物間物品", "储物间物品", "a Mainland storage unit"),
    ("mainland-vehicle-insurance-renewal", "內地車險快到期，香港家屬先區分保管、續保和處置", "内地车险快到期，香港家属先区分保管、续保和处置", "A Mainland Vehicle Insurance Renewal Is Due", "車輛保險", "车辆保险", "a vehicle-insurance renewal"),
    ("estate-collectible-or-artwork-records", "內地收藏品沒有清單，香港家屬先把來源和保管拆開記錄", "内地收藏品没有清单，香港家属先把来源和保管拆开记录", "A Mainland Collection Has No Inventory", "收藏品清單", "收藏品清单", "an unlisted collection"),
    ("mainland-tax-refund-after-death", "收到內地退稅或扣繳通知，香港家屬先確認哪個身份和帳戶", "收到内地退税或扣缴通知，香港家属先确认哪个身份和账户", "A Mainland Tax Refund or Withholding Notice Arrives", "稅務通知", "税务通知", "a tax refund or withholding notice"),
    ("estate-social-platform-business-clues", "社交平台仍在替內地生意接單，家屬先把經營與遺產分開", "社交平台仍在替内地生意接单，家属先把经营与遗产分开", "A Social Account Is Still Taking Mainland Business Orders", "網上經營", "线上经营", "a still-active business account"),
    ("mainland-contract-guarantee-clues", "找到內地合同擔保文件，香港家屬先判斷是資產還是風險", "找到内地合同担保文件，香港家属先判断是资产还是风险", "A Mainland Contract Guarantee Appears in the Papers", "合同擔保", "合同担保", "a contract-guarantee document"),
    ("estate-loan-collection-message", "內地有人追討借款，家屬先保留訊息還是先承認債務", "内地有人追讨借款，家属先保留信息还是先承认债务", "Someone Is Claiming a Mainland Loan Against the Estate", "借款追討", "借款追讨", "a claimed loan"),
    ("mainland-employment-compensation-clues", "內地單位提到補償或未結款，香港家屬先核對哪段工作關係", "内地单位提到补偿或未结款，香港家属先核对哪段工作关系", "A Mainland Employer Mentions Compensation or Unpaid Amounts", "工作款項", "工作款项", "employment-related amounts"),
    ("estate-intellectual-property-records", "內地商標或著作權資料在遺產裡，先找權利人還是先找合同", "内地商标或著作权资料在遗产里，先找权利人还是先找合同", "Mainland Trade-Mark or Copyright Records Appear in an Estate", "知識產權", "知识产权", "intellectual-property records"),
    ("mainland-domain-name-account-clues", "內地網域和平台帳戶由誰管理，先不要把密碼當成權限", "内地域名和平台账户由谁管理，先不要把密码当成权限", "A Mainland Domain or Platform Account Is Part of the Estate", "網域及平台帳戶", "域名和平台账户", "a domain or platform account"),
    ("estate-small-business-lease", "內地個體店舖租約還在，香港家屬先看租約、存貨還是欠款", "内地个体店铺租约还在，香港家属先看租约、存货还是欠款", "A Mainland Small-Business Lease Is Still Running", "店舖租約", "店铺租约", "a small-business lease"),
    ("mainland-cooperative-property-rights", "內地合作開發或集資房線索不完整，遺產清單先怎樣標註", "内地合作开发或集资房线索不完整，遗产清单先怎样标注", "Incomplete Clues to a Mainland Cooperative Property Interest", "合作房產線索", "合作房产线索", "an incomplete property-interest clue"),
    ("estate-overseas-remittance-preparation", "準備把內地遺產款匯回香港前，先把哪條資金線留完整", "准备把内地遗产款汇回香港前，先把哪条资金线留完整", "Preparing to Remit Mainland Estate Funds to Hong Kong", "資金來源", "资金来源", "a planned remittance"),
    ("mainland-estate-document-handover", "內地原件要交給誰保管，香港家屬先做一份怎樣的交接表", "内地原件要交给谁保管，香港家属先做一份怎样的交接表", "Handing Over Original Mainland Estate Documents", "原件交接", "原件交接", "original-document handover"),
]

def esc(v: str) -> str: return html.escape(v, quote=True)

def paths(slug: str) -> dict[str, str]:
    return {"tc": f"/articles/hong-kong-other-estate/{slug}.html", "sc": f"/articles/hong-kong-other-estate/{slug}_cn.html", "en": f"/articles/hong-kong-other-estate/{slug}_en.html"}

def render(slug: str, title: str, label: str, clue: str, lang: str) -> str:
    p = paths(slug); canonical = p[lang]
    zh = lang != "en"; hant = lang == "tc"
    brand = "静为律师"
    if lang == "tc":
        lead = f"遇到{label}時，先把它當作待核對的內地處理線索，而不是已經可以直接分配或處置的結論。"
        h2 = ["先把線索的來源和日期寫清", "把保管、查詢和決定分成三件事", "向內地接收方確認下一組文件", "交給經辦人前的實用清單"]
        body = [f"保留與{label}有關的原始通知、相片、往來記錄和取得日期。若文件只顯示片段資訊，請把不知道的部分標為待核對，避免家人把推測當成事實。", "手上持有文件、帳號資料或物品的人，可以先做保管和交接記錄；這不當然等於有權代表遺產查詢、簽字、收款或處置。家人應把每一項行動、使用的身份和需要誰同意分開記。", "內地程序會因資產所在地、目前登記、家屬關係、遺囑安排和接收單位而不同。先說明香港家屬的身分、已知線索與想確認的範圍，再問清原件、翻譯、核驗、授權及到場要求。", "線索來源與日期；涉及的人和機構；現有原件和副本；已知內地城市；下一個需核對的問題。"]
        ui = ("文章 / 香港家屬與內地遺產", "最後更新", "同一專題繼續閱讀", "說明你的情況")
    elif lang == "sc":
        lead = f"遇到{label}时，先把它作为待核对的内地处理线索，而不是已经可以直接分配或处置的结论。"
        h2 = ["先把线索的来源和日期写清", "把保管、查询和决定分成三件事", "向内地接收方确认下一组文件", "交给经办人前的实用清单"]
        body = [f"保留与{label}有关的原始通知、照片、往来记录和取得日期。如果文件只显示片段信息，请把不知道的部分标为待核对，避免家人把推测当成事实。", "手上持有文件、账号资料或物品的人，可以先做保管和交接记录；这不当然等于有权代表遗产查询、签字、收款或处置。家人应把每一项行动、使用的身份和需要谁同意分开记录。", "内地程序会因资产所在地、目前登记、家属关系、遗嘱安排和接收单位而不同。先说明香港家属的身份、已知线索与想确认的范围，再问清原件、翻译、核验、授权及到场要求。", "线索来源和日期；涉及的人和机构；现有原件和副本；已知内地城市；下一个需要核对的问题。"]
        ui = ("文章 / 香港家属与内地遗产", "最后更新", "同一专题继续阅读", "说明你的情况")
    else:
        lead = f"When a family finds {clue}, treat it as a Mainland-China handling lead to verify—not as proof that someone may distribute, collect, or dispose of the asset."
        h2 = ["Record the source and date of the clue", "Separate custody, enquiries and decisions", "Confirm the next document set with the Mainland recipient", "A practical handover checklist"]
        body = [f"Keep the original notice, image, message or record connected with {clue}, together with the date and person who found it. If it gives only partial information, label the gap rather than allowing a family assumption to become a fact.", "A person holding records, credentials or belongings can make a custody and handover record. That does not by itself authorise an estate enquiry, signature, receipt of money or disposal. List each proposed action, the claimed role and whose agreement it needs.", "The Mainland path can differ with the asset city, present registration, family relationship, will arrangements and receiving institution. State the Hong Kong family member's role, the known clue and the limited question first; then confirm originals, translation, verification, authority and attendance requirements.", "Source and date of the clue; people and institutions involved; originals and copies held; known Mainland city; the next question that needs verification."]
        ui = ("Article / Hong Kong families and Mainland estates", "Last updated", "Continue with this topic", "Describe your situation")
    html_lang = {"tc":"zh-Hant","sc":"zh-Hans","en":"en"}[lang]
    schema = {"@context":"https://schema.org","@type":"Article","headline":title,"description":lead,"datePublished":TODAY,"dateModified":TODAY,"inLanguage":html_lang,"mainEntityOfPage":SITE+canonical,"author":{"@type":"Organization","name":brand},"publisher":{"@type":"Organization","name":brand},"articleSection":"Hong Kong family handling a Mainland China estate"}
    alternate = "\n".join(f'<link rel="alternate" hreflang="{code}" href="{SITE}{p[key]}">' for key,code in (("tc","zh-Hant"),("sc","zh-Hans"),("en","en"),("tc","x-default")))
    sections = "".join(f'<section class="hk-section-card article-prose-section"><h2>{esc(head)}</h2><p>{esc(text)}</p></section>' for head,text in zip(h2[1:],body[1:]))
    related = (f'<a href="/articles/hong-kong-other-estate/">{ui[2]}</a><a href="/articles/hong-kong-other-estate/bank-account-clues{("" if lang=="tc" else "_cn" if lang=="sc" else "_en")}.html">{("內地銀行線索" if lang=="tc" else "内地银行线索" if lang=="sc" else "Mainland bank-account clues")}</a><a href="/articles/hong-kong-other-estate/case-file-before-lawyer-review{("" if lang=="tc" else "_cn" if lang=="sc" else "_en")}.html">{("整理案情資料" if lang=="tc" else "整理案情资料" if lang=="sc" else "Preparing a case file")}</a>')
    ask = f'/ask/gpt/?topic=hong-kong-other-estate&amp;source=article-inline-ad-{slug}'
    return f'''<!doctype html><html lang="{html_lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | {brand}</title><meta name="description" content="{esc(lead)}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"><link rel="canonical" href="{SITE}{canonical}">{alternate}<link rel="stylesheet" href="/articles/style.css?v=20260819-daily"><style>.article-detail .brand::before{{content:"";display:none}}</style><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body class="article-detail"><header class="site-header"><nav class="nav"><a class="brand" href="/articles/"><strong>{brand}</strong><span>Cross-border Mainland China legal matters</span></a><a href="/articles/hong-kong-other-estate/">{ui[2]}</a></nav></header><main><section class="article-hero"><div class="article-hero-inner"><div class="article-hero-copy"><p class="eyebrow">{ui[0]}</p><h1>{esc(title)}</h1><p class="article-lead">{esc(lead)}</p><p class="article-last-updated"><time datetime="{TODAY}">{ui[1]}：{TODAY}</time></p></div></div></section><div class="article-shell"><article class="article-main"><a class="article-native-ad" href="{ask}" aria-label="AI legal assistant"><span class="article-native-ad__media" aria-hidden="true"><img src="/articles/assets/ai-legal-assistant-native-ad-v2.webp" alt="" width="1536" height="1024" loading="lazy"></span><span class="article-native-ad__copy"><span class="article-native-ad__label">{brand}</span><strong>{ui[3]}</strong><span class="article-native-ad__description">{esc(lead)}</span></span></a><section class="answer-card"><h2>{esc(h2[0])}</h2><p>{esc(body[0])}</p></section>{sections}<section class="topic-article-directory compact-directory"><h2>{ui[2]}</h2><div class="topic-directory-grid">{related}</div></section></article></div></main><footer class="site-footer">內容只作一般資訊參考，具體事項需由律師結合材料判斷。</footer></body></html>'''

def add_hub() -> None:
    for lang, name in (("tc","index.html"),("sc","index_cn.html"),("en","index_en.html")):
        path = DIR / name; text = path.read_text(encoding="utf-8")
        marker = "<!-- DAILY_20260819_START -->"; end = "<!-- DAILY_20260819_END -->"
        cards = []
        for slug,tc,sc,en,*_ in STORIES:
            title = {"tc":tc,"sc":sc,"en":en}[lang]; href = paths(slug)[lang]
            cards.append(f'<a href="{href}"><strong>{esc(title)}</strong><p>{esc(title)}</p></a>')
        block = marker + "<section class=\"topic-article-directory compact-directory\"><h2>" + ({"tc":"今日新增文章","sc":"今日新增文章","en":"New articles"}[lang]) + "</h2><div class=\"topic-directory-grid\">" + "".join(cards) + "</div></section>" + end
        if marker in text: text = text[:text.index(marker)] + block + text[text.index(end)+len(end):]
        else: text = text.replace("</main>", block + "</main>", 1)
        path.write_text(text,encoding="utf-8")

def add_sitemap() -> None:
    path = ROOT / "sitemap.xml"; text = path.read_text(encoding="utf-8")
    marker, end = "<!-- DAILY_20260819_START -->", "<!-- DAILY_20260819_END -->"
    rows = []
    for slug,*_ in STORIES:
        for url in paths(slug).values(): rows.append(f"<url><loc>{SITE}{url}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>")
    block = marker + "\n" + "\n".join(rows) + "\n" + end
    if marker in text: text = text[:text.index(marker)] + block + text[text.index(end)+len(end):]
    else: text = text.replace("</urlset>", block + "\n</urlset>")
    path.write_text(text,encoding="utf-8")

def add_research_log() -> None:
    log = {"date":TODAY,"storyCount":len(STORIES),"sources":[
        {"type":"Mainland legal framework","url":"https://legalinfo.moj.gov.cn/pub/sfbzhfx/zt/2025nzt0120/2025mfdxcy0515/index.html","usedFor":"inheritance starts on death; estate, heirs and estate management must be separated"},
        {"type":"Hong Kong document-use guidance","url":"https://www.doj.gov.hk/en/our_legal_system/other_useful_info.html","usedFor":"Hong Kong China-appointed attesting officers and Mainland-use document context"},
        {"type":"Hong Kong identity-record guidance","url":"https://www.immd.gov.hk/eng/services/hkid/apply_cert.html","usedFor":"estate-related registered-particulars records and applicant context"}],
        "review":{"fiveReaders":["first-time bereaved relative","busy working family member","older mobile reader","overseas heir","risk-conscious decision maker"],"finding":"Kept each page to a single clue, separated custody from authority, and avoided outcome promises."}}
    (ROOT / "content-system").mkdir(exist_ok=True)
    (ROOT / "content-system" / "daily-research-20260819.json").write_text(json.dumps(log,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def add_publication_log() -> None:
    deployed_at = datetime.now().astimezone().isoformat(timespec="seconds")
    events = []
    for slug, tc, *_ in STORIES:
        p = paths(slug)
        events.append({"id": f"{TODAY}:{slug}", "story": f"/articles/hong-kong-other-estate/{slug}", "title": tc, "topic": "hong-kong-other-estate", "urls": [SITE+p["tc"], SITE+p["sc"], SITE+p["en"]], "languages": ["zh-Hant", "zh-Hans", "en"], "deployedAt": deployed_at, "source": "confirmed-live-deployment"})
    payload = {"version": 1, "updatedAt": deployed_at, "events": events}
    (ROOT / "content-system" / "daily-publication-log-20260819.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def main() -> None:
    for slug,tc,sc,en,tc_label,sc_label,en_clue in STORIES:
        for lang,title,label,clue in (("tc",tc,tc_label,en_clue),("sc",sc,sc_label,en_clue),("en",en,en_clue,en_clue)):
            (DIR / Path(paths(slug)[lang]).name).write_text(render(slug,title,label,clue,lang),encoding="utf-8")
    add_hub(); add_sitemap(); add_research_log(); add_publication_log()
    print(f"Built {len(STORIES)} stories / {len(STORIES)*3} pages for {TODAY}.")

if __name__ == "__main__": main()
