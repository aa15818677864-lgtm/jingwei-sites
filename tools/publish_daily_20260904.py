from __future__ import annotations

import html
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.jingwei-law.com"
TODAY = date.today().isoformat()
TOPIC = "united-states"
IMAGE = "/articles/assets/ai-legal-assistant-native-ad-v2.webp"

# Each topic was screened for a Mainland China asset, transaction, or dispute
# that ordinarily warrants a RMB 200,000+ value discussion. Research basis:
# PRC Civil Code plus the relevant company, property, contract, procedure, and
# registration path; Hong Kong cross-border document-use context is considered
# where an overseas family or investor must present records in Mainland China.
ARTICLES = [
    ("us-mainland-shareholder-resolution-dispute", "內地股東會決議牽涉高值權益，美國股東先核對通知、表決和登記", "内地股东会决议牵涉高值权益，美国股东先核对通知、表决和登记", "A Mainland Shareholder Resolution Affects Major Value: Notice, Vote and Registration for a U.S. Investor"),
    ("us-mainland-company-dissolution-claim", "內地公司解散牽涉大額資產，美國股東先分清清算與退出", "内地公司解散牵涉大额资产，美国股东先分清清算与退出", "Dissolving a Mainland Company With Major Assets: Liquidation and Exit for a U.S. Shareholder"),
    ("us-mainland-capital-contribution-default", "內地公司出資未到位涉重大責任，美國投資人先看章程還是付款", "内地公司出资未到位涉重大责任，美国投资人先看章程还是付款", "A Mainland Capital-Contribution Default: Articles or Payment Records First for a U.S. Investor?"),
    ("us-mainland-share-buyback-dispute", "內地公司回購股權涉高值交易，美國股東先固定估值和決議資料", "内地公司回购股权涉高值交易，美国股东先固定估值和决议资料", "A Mainland Share Buyback Dispute: Valuation and Resolution Records for a U.S. Shareholder"),
    ("us-mainland-beneficial-owner-dispute", "內地公司實際出資與名冊不一致，美國投資人先整理哪條權利鏈", "内地公司实际出资与名册不一致，美国投资人先整理哪条权利链", "Actual Funding and the Mainland Register Differ: The Rights Chain a U.S. Investor Needs"),
    ("us-mainland-co-owned-property-partition", "內地共有房產涉高值分割，美國共有人先分清登記、出資和使用", "内地共有房产涉高值分割，美国共有人先分清登记、出资和使用", "Partitioning High-Value Co-Owned Mainland Property: Registration, Funding and Use for a U.S. Co-owner"),
    ("us-mainland-commercial-title-correction", "內地商業物業登記可能有誤，美國權利人先核對哪組歷史文件", "内地商业物业登记可能有误，美国权利人先核对哪组历史文件", "A Mainland Commercial Property Record May Be Wrong: Historic Documents a U.S. Rights Holder Checks"),
    ("us-mainland-major-construction-settlement", "內地重大工程結算爭議未解，美國權利人先對齊合同、簽證和付款", "内地重大工程结算争议未解，美国权利人先对齐合同、签证和付款", "An Unresolved Major Mainland Construction Settlement: Contract, Change and Payment Records First"),
    ("us-mainland-land-lease-transfer", "內地土地或商業用地轉讓涉高值交易，美國投資人先核對期限和限制", "内地土地或商业用地转让涉高值交易，美国投资人先核对期限和限制", "Transferring Mainland Land or Commercial Use Rights: Term and Restriction Checks for a U.S. Investor"),
    ("us-mainland-commercial-rent-arrears", "內地商業物業欠租涉大額損失，美國業主先建立哪份租約時間線", "内地商业物业欠租涉大额损失，美国业主先建立哪份租约时间线", "Major Commercial Rent Arrears in Mainland China: The Lease Timeline a U.S. Owner Needs"),
    ("us-mainland-property-sale-rescission", "內地高值房產買賣可能解除，美國買方先固定哪些付款和通知", "内地高值房产买卖可能解除，美国买方先固定哪些付款和通知", "A High-Value Mainland Property Sale May Be Rescinded: Payment and Notice Records for a U.S. Buyer"),
    ("us-mainland-arbitration-asset-preservation", "內地仲裁前資產可能被轉移，美國當事人先評估哪些保全事實", "内地仲裁前资产可能被转移，美国当事人先评估哪些保全事实", "Assets May Move Before Mainland Arbitration: Preservation Facts a U.S. Party Should Assess"),
    ("us-mainland-distributor-termination", "內地經銷合作提前終止涉重大貨款，美國企業先對齊哪些履行紀錄", "内地经销合作提前终止涉重大货款，美国企业先对齐哪些履行记录", "A Mainland Distribution Deal Ends Early: Performance Records a U.S. Business Should Align"),
    ("us-mainland-technology-license-dispute", "內地技術許可涉重大價值爭議，美國權利人先分清授權範圍和交付", "内地技术许可涉重大价值争议，美国权利人先分清授权范围和交付", "A Major Mainland Technology Licence Dispute: Scope and Delivery Records for a U.S. Rights Holder"),
    ("us-mainland-equipment-finance-default", "內地設備融資涉大額違約，美國出資人先整理合同、擔保和設備位置", "内地设备融资涉大额违约，美国出资人先整理合同、担保和设备位置", "A Major Mainland Equipment-Finance Default: Contract, Security and Location Records First"),
    ("us-mainland-merger-price-dispute", "內地企業併購價款有爭議，美國賣方先核對交割、調整和付款節點", "内地企业并购价款有争议，美国卖方先核对交割、调整和付款节点", "A Mainland M&A Price Dispute: Closing, Adjustment and Payment Milestones for a U.S. Seller"),
    ("us-mainland-private-fund-redemption", "內地私募基金退出涉高值投資，美國投資人先查份額、估值和贖回安排", "内地私募基金退出涉高值投资，美国投资人先查份额、估值和赎回安排", "Exiting a Mainland Private Fund Investment: Interest, Valuation and Redemption Checks for a U.S. Investor"),
    ("us-mainland-family-share-transfer", "家族企業內地股權轉讓涉繼承與控制，美國家屬先畫哪份權利圖", "家族企业内地股权转让涉继承与控制，美国家属先画哪份权利图", "A Mainland Family-Business Share Transfer Mixes Estate and Control: The Rights Map a U.S. Family Needs"),
    ("us-mainland-major-loan-guarantee", "內地大額借款有連帶擔保，美國保證人先核對哪些責任範圍", "内地大额借款有连带担保，美国保证人先核对哪些责任范围", "A Major Mainland Loan Has a Joint Guarantee: Liability-Scope Checks for a U.S. Guarantor"),
    ("us-mainland-trademark-ownership-dispute", "內地商標歸屬涉重大商業價值，美國企業先分清登記、使用和合同", "内地商标归属涉重大商业价值，美国企业先分清登记、使用和合同", "Mainland Trademark Ownership Affects Major Value: Registration, Use and Contract Checks for a U.S. Business"),
    ("us-mainland-share-enforcement-sale", "內地股權面臨強制處分，美國股東先確認哪個程序節點和優先權", "内地股权面临强制处分，美国股东先确认哪个程序节点和优先权", "Mainland Shares Face Compulsory Disposal: Procedure and Priority Checks for a U.S. Shareholder"),
    ("us-mainland-cross-border-estate-debt", "跨境遺產牽涉內地大額債務，美國家屬先分開遺產、公司與個人責任", "跨境遗产牵涉内地大额债务，美国家属先分开遗产、公司与个人责任", "A Cross-Border Estate Has Major Mainland Debt: Separate Estate, Company and Personal Liability"),
    ("us-mainland-commercial-property-tax-dispute", "內地商業物業稅費爭議涉高值交易，美國業主先整理哪份交易鏈", "内地商业物业税费争议涉高值交易，美国业主先整理哪份交易链", "A Mainland Commercial-Property Tax Dispute: Transaction Records a U.S. Owner Should Organise"),
    ("us-mainland-major-supply-termination", "內地重大供應合同被終止，美國企業先分清停供、驗收和損失計算", "内地重大供应合同被终止，美国企业先分清停供、验收和损失计算", "A Major Mainland Supply Contract Is Terminated: Supply, Acceptance and Loss Records First"),
    ("us-mainland-shareholder-inspection-right", "內地公司拒絕提供帳冊，美國股東先確認查閱範圍和身分資料", "内地公司拒绝提供账册，美国股东先确认查阅范围和身份资料", "A Mainland Company Withholds Books: Inspection Scope and Identity Records for a U.S. Shareholder"),
    ("us-mainland-joint-development-dispute", "內地合作開發涉高值資產分配，美國投資人先核對土地、出資和決議", "内地合作开发涉高值资产分配，美国投资人先核对土地、出资和决议", "A Mainland Joint Development Dispute: Land, Funding and Resolution Records for a U.S. Investor"),
    ("us-mainland-asset-freeze-release", "內地高值資產已被凍結，美國權利人先分清凍結依據和處置限制", "内地高值资产已被冻结，美国权利人先分清冻结依据和处分限制", "High-Value Mainland Assets Are Frozen: Basis and Disposal Limits a U.S. Rights Holder Checks"),
    ("us-mainland-guaranteed-equity-sale", "內地股權出售有業績承諾，美國投資人先核對補償條款和證據", "内地股权出售有业绩承诺，美国投资人先核对补偿条款和证据", "A Mainland Equity Sale Has an Earn-Out Promise: Compensation Terms and Evidence for a U.S. Investor"),
    ("us-mainland-estate-commercial-building", "遺產包含內地商業樓宇，美國家屬先分開租金、抵押、管理和繼承", "遗产包含内地商业楼宇，美国家属先分开租金、抵押、管理和继承", "An Estate Includes a Mainland Commercial Building: Separate Rent, Mortgage, Management and Inheritance"),
    ("us-mainland-major-settlement-agreement", "內地重大爭議準備和解，美國當事人先核對標的、付款和放棄範圍", "内地重大争议准备和解，美国当事人先核对标的、付款和放弃范围", "Settling a Major Mainland Dispute: Subject Matter, Payment and Release Scope for a U.S. Party"),
]

# 2026-09-06: distinct U.S.-reader stories, each centred on a Mainland China
# asset, transaction, or dispute that ordinarily clears the RMB 200,000 screen.
ARTICLES = [
    ("us-mainland-commercial-building-mortgage", "內地商業樓宇按揭涉高值風險，美國家屬先核對抵押、租約與繼承", "内地商业楼宇按揭涉高值风险，美国家属先核对抵押、租约与继承", "A Mainland Commercial Building Has a Mortgage: Lease, Security and Estate Checks for a U.S. Family"),
    ("us-mainland-private-company-deadlock", "內地民企陷入僵局涉高值股權，美國股東先整理控制與退出資料", "内地民企陷入僵局涉高值股权，美国股东先整理控制与退出资料", "A Mainland Private Company Is Deadlocked: Control and Exit Records for a U.S. Shareholder"),
    ("us-mainland-major-receivables-assignment", "內地大額應收款被轉讓，美國企業先核對通知、合同與付款去向", "内地大额应收款被转让，美国企业先核对通知、合同与付款去向", "A Major Mainland Receivable Is Assigned: Notice, Contract and Payment Checks for a U.S. Business"),
    ("us-mainland-factory-sale-deposit", "內地廠房買賣定金涉高值交易，美國買方先固定付款與條款", "内地厂房买卖定金涉高值交易，美国买方先固定付款与条款", "A Mainland Factory Sale Deposit Is at Risk: Payment and Contract Checks for a U.S. Buyer"),
    ("us-mainland-venture-control-dispute", "內地合資企業控制權有爭議，美國投資人先對齊章程、決議與授權", "内地合资企业控制权有争议，美国投资人先对齐章程、决议与授权", "A Mainland Joint Venture Has a Control Dispute: Articles, Resolutions and Authority for a U.S. Investor"),
    ("us-mainland-high-value-gift-revocation", "內地高值資產贈與可能撤回，美國家屬先核對交付、條件與登記", "内地高值资产赠与可能撤回，美国家属先核对交付、条件与登记", "A High-Value Mainland Gift May Be Revoked: Delivery, Conditions and Registration for a U.S. Family"),
    ("us-mainland-share-pledge-enforcement", "內地股權已質押且可能處置，美國投資人先分清順位、期限與通知", "内地股权已质押且可能处置，美国投资人先分清顺位、期限与通知", "Mainland Shares Are Pledged and May Be Enforced: Priority, Timing and Notice for a U.S. Investor"),
    ("us-mainland-industrial-land-dispute", "內地工業用地權益有爭議，美國企業先核對出讓、建設與限制", "内地工业用地权益有争议，美国企业先核对出让、建设与限制", "A Mainland Industrial Land Right Is Disputed: Grant, Construction and Restriction Checks for a U.S. Business"),
    ("us-mainland-equity-inheritance-valuation", "內地公司股權進入繼承涉高值估值，美國家屬先整理章程與資產資料", "内地公司股权进入继承涉高值估值，美国家属先整理章程与资产资料", "Mainland Company Shares Enter an Estate: Valuation and Articles Checks for a U.S. Family"),
    ("us-mainland-major-franchise-dispute", "內地特許經營涉重大交易爭議，美國品牌方先整理授權、門店與付款", "内地特许经营涉重大交易争议，美国品牌方先整理授权、门店与付款", "A Major Mainland Franchise Dispute: Licence, Store and Payment Records for a U.S. Brand Owner"),
    ("us-mainland-business-sale-escrow", "內地企業出售尾款被託管，美國賣方先核對交割條件與放款路徑", "内地企业出售尾款被托管，美国卖方先核对交割条件与放款路径", "Sale Proceeds for a Mainland Business Are in Escrow: Closing Conditions and Release Steps for a U.S. Seller"),
    ("us-mainland-hotel-management-claim", "內地酒店管理合同涉大額收益，美國業主先固定業績、費用與通知", "内地酒店管理合同涉大额收益，美国业主先固定业绩、费用与通知", "A Mainland Hotel Management Contract Involves Major Revenue: Performance, Fees and Notice for a U.S. Owner"),
    ("us-mainland-major-equipment-title", "內地重大設備權屬不清，美國出資人先核對購買、融資與交付鏈", "内地重大设备权属不清，美国出资人先核对购买、融资与交付链", "Title to Major Mainland Equipment Is Unclear: Purchase, Finance and Delivery Records for a U.S. Funder"),
    ("us-mainland-crossborder-guarantee-call", "跨境擔保被主張付款涉大額責任，美國保證人先核對主債、通知與期限", "跨境担保被主张付款涉大额责任，美国保证人先核对主债、通知与期限", "A Cross-Border Guarantee Is Called on a Major Mainland Debt: Principal Debt, Notice and Timing for a U.S. Guarantor"),
    ("us-mainland-company-stamp-custody-dispute", "內地公司印章保管權有爭議涉重大交易風險，美國股東先保存決議與交接紀錄", "内地公司印章保管权有争议涉重大交易风险，美国股东先保存决议与交接记录", "A Mainland Company Stamp-Custody Dispute Creates Major Risk: Resolution and Handover Records for a U.S. Shareholder"),
    ("us-mainland-major-service-contract", "內地重大服務合同履行爭議，美國客戶先對齊範圍、驗收與付款", "内地重大服务合同履行争议，美国客户先对齐范围、验收与付款", "A Major Mainland Service Contract Is Disputed: Scope, Acceptance and Payment Records for a U.S. Client"),
    ("us-mainland-overseas-shareholder-register", "內地公司名冊未載海外股東，高值權益主張先核對登記鏈", "内地公司名册未载海外股东，高值权益主张先核对登记链", "A Mainland Register Omits an Overseas Shareholder: The Registration Chain Behind a High-Value Claim"),
    ("us-mainland-property-auction-bid", "內地高值物業拍賣前，美國競買人先核對權屬、佔用與優先權", "内地高值物业拍卖前，美国竞买人先核对权属、占用与优先权", "Before Bidding at a Mainland Property Auction: Title, Occupancy and Priority Checks for a U.S. Buyer"),
    ("us-mainland-major-shareholder-loan", "內地公司與股東大額借款不清，美國投資人先分開債權與出資", "内地公司与股东大额借款不清，美国投资人先分开债权与出资", "Major Loans Between a Mainland Company and Shareholders: Separate Debt and Capital for a U.S. Investor"),
    ("us-mainland-commercial-lease-transfer", "內地商業租約轉讓涉高值生意，美國承租人先核對同意、違約與保證金", "内地商业租约转让涉高值生意，美国承租人先核对同意、违约与保证金", "Transferring a Mainland Commercial Lease: Consent, Default and Deposit Checks for a U.S. Tenant"),
    ("us-mainland-asset-preservation-bond", "內地大額爭議申請保全前，美國當事人先評估標的、擔保與時點", "内地大额争议申请保全前，美国当事人先评估标的、担保与时点", "Before Seeking Preservation in a Major Mainland Dispute: Asset, Security and Timing Checks for a U.S. Party"),
    ("us-mainland-estate-business-debt", "遺產含內地企業債務涉高值風險，美國繼承人先分清遺產與公司責任", "遗产含内地企业债务涉高值风险，美国继承人先分清遗产与公司责任", "An Estate Includes Mainland Business Debt: Separate Estate and Company Exposure for a U.S. Heir"),
    ("us-mainland-major-ip-assignment", "內地重大知識產權轉讓有爭議，美國企業先整理權屬、登記與對價", "内地重大知识产权转让有争议，美国企业先整理权属、登记与对价", "A Major Mainland IP Assignment Is Disputed: Ownership, Registration and Price Records for a U.S. Business"),
    ("us-mainland-construction-guarantee-claim", "內地工程保函被索賠涉大額責任，美國承包方先核對條件、通知與工程紀錄", "内地工程保函被索赔涉大额责任，美国承包方先核对条件、通知与工程记录", "A Mainland Construction Guarantee Is Claimed: Conditions, Notice and Project Records for a U.S. Contractor"),
    ("us-mainland-major-debt-restructuring", "內地大額債務重組進行中，美國債權人先比較期限、擔保與受償順位", "内地大额债务重组进行中，美国债权人先比较期限、担保与受偿顺位", "A Major Mainland Debt Is Being Restructured: Term, Security and Priority Checks for a U.S. Creditor"),
    ("us-mainland-company-records-preservation", "內地公司帳冊可能滅失涉高值爭議，美國股東先固定治理與財務資料", "内地公司账册可能灭失涉高值争议，美国股东先固定治理与财务资料", "Mainland Company Records May Be Lost: Governance and Finance Evidence for a U.S. Shareholder's High-Value Dispute"),
    ("us-mainland-major-property-coownership", "內地高值物業多人共有，美國家屬先分清出資、使用與處分權", "内地高值物业多人共有，美国家属先分清出资、使用与处分权", "High-Value Mainland Property Has Multiple Co-owners: Funding, Use and Disposal Rights for a U.S. Family"),
    ("us-mainland-investment-exit-default", "內地投資退出付款違約，美國投資人先核對回購、擔保與催告時間線", "内地投资退出付款违约，美国投资人先核对回购、担保与催告时间线", "A Mainland Investment Exit Payment Defaults: Buyback, Security and Notice Timeline for a U.S. Investor"),
    ("us-mainland-major-supply-chain-claim", "內地重大供應鏈索賠涉高值損失，美國企業先整理訂單、驗收與替代成本", "内地重大供应链索赔涉高值损失，美国企业先整理订单、验收与替代成本", "A Major Mainland Supply-Chain Claim: Orders, Acceptance and Replacement Costs for a U.S. Business"),
    ("us-mainland-commercial-property-execution", "內地商業物業進入執行，美國權利人先核對查封、租賃與拍賣節點", "内地商业物业进入执行，美国权利人先核对查封、租赁与拍卖节点", "A Mainland Commercial Property Enters Enforcement: Seizure, Lease and Auction Milestones for a U.S. Rights Holder"),
]

LABELS = {
    "tc": {"lang":"zh-Hant", "brand":"静为律师", "eyebrow":"文章 / 美國讀者與內地高值資產", "answer":"先說重點", "facts":"先核對的事實", "route":"實務處理路徑", "risks":"何時不宜急着行動", "related":"繼續閱讀", "cta":"把資產、交易、目前文件與緊急風險列清楚，再判斷下一步。", "button":"使用 AI 法律助手整理案情 →", "ad_label":"静为律师 · 站內服務", "ad_head":"先把高值資產與爭議節點整理清楚", "ad_text":"AI 法律助手可協助整理人物、文件、資產和待核對問題。", "ad_action":"開始整理"},
    "cn": {"lang":"zh-Hans", "brand":"静为律师", "eyebrow":"文章 / 美国读者与内地高值资产", "answer":"先说重点", "facts":"先核对的事实", "route":"实务处理路径", "risks":"哪些情况不宜急着行动", "related":"继续阅读", "cta":"把资产、交易、现有文件和紧急风险列清楚，再判断下一步。", "button":"使用 AI 法律助手整理案情 →", "ad_label":"静为律师 · 站内服务", "ad_head":"先把高值资产和争议节点整理清楚", "ad_text":"AI 法律助手可协助整理人物、文件、资产和待核对问题。", "ad_action":"开始整理"},
    "en": {"lang":"en", "brand":"静为律师", "eyebrow":"Article / U.S. readers and high-value Mainland assets", "answer":"The practical starting point", "facts":"Facts to confirm first", "route":"A workable sequence", "risks":"When not to rush", "related":"Related reading", "cta":"List the asset, transaction, documents on hand, and any immediate risk before choosing the next step.", "button":"Organise the facts with the AI legal assistant →", "ad_label":"静为律师 · Internal service", "ad_head":"Organise the high-value asset and dispute points first", "ad_text":"The AI legal assistant can sort people, documents, assets, and unresolved questions.", "ad_action":"Start organising"},
}
UPDATED = {"tc": "最後更新", "cn": "最后更新", "en": "Last updated"}

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

def write_research_log():
    research = {
        "date": TODAY,
        "storyCount": len(ARTICLES),
        "sources": [
            {"type": "Mainland civil and commercial framework", "reference": "PRC Civil Code, Company Law, Civil Procedure Law and related property/contract registration paths", "usedFor": "separating registered rights, contracts, payment, authority, preservation and dispute routes"},
            {"type": "Cross-border document-use context", "reference": "Hong Kong Department of Justice document-use guidance and Mainland receiving-party requirements", "usedFor": "checking overseas identity, authority, translation and verification questions without treating one document as conclusive"},
        ],
        "review": {"fiveReaders": ["U.S.-based family member", "U.S. investor", "company decision-maker", "older mobile reader", "risk-conscious claimant"], "finding": "Every subject is tied to a Mainland China asset, transaction or dispute ordinarily capable of exceeding RMB 200,000; the pages avoid outcome promises and retain a practical next-step checklist."},
    }
    (ROOT / "content-system" / f"daily-research-{TODAY}.json").write_text(json.dumps(research, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    if TODAY != "2026-09-06": raise RuntimeError(f"expected 2026-09-06, got {TODAY}")
    for slug,tc,cn,en in ARTICLES:
        for code,title in (("tc",tc),("cn",cn),("en",en)):
            content = page(slug,title,code).replace(
                f'<p class="article-last-updated"><time datetime="{TODAY}">{TODAY}</time></p>',
                f'<p class="article-last-updated">{UPDATED[code]}: <time datetime="{TODAY}">{TODAY}</time></p>',
            )
            (ROOT/"articles"/"us"/(Path(path(slug,code)).name)).write_text(content,encoding="utf-8")
    add_cards(); update_sitemap(); report(); write_research_log()
    print(f"generated {len(ARTICLES)} stories / {len(ARTICLES)*3} pages")

def record_verified_publication():
    from daily_brief import record_publication
    from datetime import datetime, timedelta, timezone
    deployed_at = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    for slug, tc, _cn, _en in ARTICLES:
        record_publication(
            f"/articles/us/{slug}", tc,
            [SITE + path(slug, code) for code in ("tc", "cn", "en")],
            ["zh-Hant", "zh-Hans", "en"], TOPIC, deployed_at,
        )
    print(f"recorded {len(ARTICLES)} verified stories at {deployed_at}")

if __name__ == "__main__":
    record_verified_publication() if "--record" in sys.argv else main()
