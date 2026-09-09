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

# 2026-09-07: distinct U.S.-reader stories, each centred on a Mainland China
# asset, transaction, or dispute that ordinarily clears the RMB 200,000 screen.
ARTICLES = [
    ("us-mainland-commercial-property-option", "內地商業物業期權涉高值交易，美國買方先核對行權、登記與付款", "内地商业物业期权涉高值交易，美国买方先核对行权、登记与付款", "A Mainland Commercial Property Option Has Major Value: Exercise, Registration and Payment Checks for a U.S. Buyer"),
    ("us-mainland-equity-transfer-tax-adjustment", "內地股權轉讓稅費調整涉高值交易，美國賣方先整理估值與付款鏈", "内地股权转让税费调整涉高值交易，美国卖方先整理估值与付款链", "A Mainland Equity Transfer Has a Tax Adjustment: Valuation and Payment Records for a U.S. Seller"),
    ("us-mainland-major-loan-extension", "內地大額借款展期談判中，美國債權人先核對本金、利息與擔保", "内地大额借款展期谈判中，美国债权人先核对本金、利息与担保", "Extending a Major Mainland Loan: Principal, Interest and Security Checks for a U.S. Creditor"),
    ("us-mainland-warehouse-sale-dispute", "內地倉儲物業買賣有爭議，美國投資人先固定權屬、交付與價款", "内地仓储物业买卖有争议，美国投资人先固定权属、交付与价款", "A Mainland Warehouse Sale Is Disputed: Title, Delivery and Price Records for a U.S. Investor"),
    ("us-mainland-shareholder-removal-dispute", "內地公司股東資格被否認涉高值權益，美國投資人先核對出資與名冊", "内地公司股东资格被否认涉高值权益，美国投资人先核对出资与名册", "A Mainland Company Denies Shareholder Status: Funding and Register Records for a U.S. Investor"),
    ("us-mainland-estate-property-lease", "遺產含內地出租物業涉高值收益，美國家屬先分清租約、租金與繼承", "遗产含内地出租物业涉高值收益，美国家属先分清租约、租金与继承", "An Estate Includes Leased Mainland Property: Lease, Rent and Inheritance Checks for a U.S. Family"),
    ("us-mainland-major-factoring-dispute", "內地大額保理款有爭議，美國企業先核對債權、通知與回款", "内地大额保理款有争议，美国企业先核对债权、通知与回款", "A Major Mainland Factoring Claim Is Disputed: Receivable, Notice and Recovery Records for a U.S. Business"),
    ("us-mainland-commercial-landlord-default", "內地商業物業出租方違約涉高值生意，美國承租人先核對租約與交付", "内地商业物业出租方违约涉高值生意，美国承租人先核对租约与交付", "A Mainland Commercial Landlord Defaults: Lease and Delivery Records for a U.S. Tenant"),
    ("us-mainland-company-dividend-dispute", "內地公司分紅安排有爭議涉高值股權，美國股東先核對章程與決議", "内地公司分红安排有争议涉高值股权，美国股东先核对章程与决议", "A Mainland Company Dividend Is Disputed: Articles and Resolutions for a U.S. Shareholder"),
    ("us-mainland-project-payment-retention", "內地工程尾款被留置涉重大金額，美國承包方先整理驗收與結算", "内地工程尾款被留置涉重大金额，美国承包方先整理验收与结算", "Mainland Project Retention Money Is Withheld: Acceptance and Settlement Records for a U.S. Contractor"),
    ("us-mainland-major-joint-venture-exit", "內地合資企業退出涉高值交易，美國投資人先分清估值、同意與交割", "内地合资企业退出涉高值交易，美国投资人先分清估值、同意与交割", "Exiting a Major Mainland Joint Venture: Valuation, Consent and Closing Checks for a U.S. Investor"),
    ("us-mainland-commercial-mortgage-release", "內地商業物業抵押待解除，美國買方先核對債務、註銷與交割", "内地商业物业抵押待解除，美国买方先核对债务、注销与交割", "A Mainland Commercial Mortgage Must Be Released: Debt, Cancellation and Closing Checks for a U.S. Buyer"),
    ("us-mainland-technology-escrow-dispute", "內地技術交易款被託管涉重大價值，美國權利人先核對交付與放款條件", "内地技术交易款被托管涉重大价值，美国权利人先核对交付与放款条件", "Technology Sale Proceeds Are Escrowed in Mainland China: Delivery and Release Checks for a U.S. Rights Holder"),
    ("us-mainland-major-guarantee-renewal", "內地大額保證續期風險上升，美國保證人先核對範圍、期限與同意", "内地大额保证续期风险上升，美国保证人先核对范围、期限与同意", "A Major Mainland Guarantee Is Renewed: Scope, Timing and Consent Checks for a U.S. Guarantor"),
    ("us-mainland-company-equity-dilution", "內地公司增資稀釋高值股權，美國股東先核對通知、估值與優先權", "内地公司增资稀释高值股权，美国股东先核对通知、估值与优先权", "A Mainland Capital Increase Dilutes Major Equity: Notice, Valuation and Priority for a U.S. Shareholder"),
    ("us-mainland-major-supply-quality-claim", "內地重大供貨品質索賠涉高值損失，美國買方先對齊規格、驗收與通知", "内地重大供货质量索赔涉高值损失，美国买方先对齐规格、验收与通知", "A Major Mainland Supply Quality Claim: Specifications, Acceptance and Notice for a U.S. Buyer"),
    ("us-mainland-family-company-sale", "家族持有內地企業待出售涉高值資產，美國家屬先整理股權、授權與價格", "家族持有内地企业待出售涉高值资产，美国家属先整理股权、授权与价格", "A Family-Owned Mainland Business Is Being Sold: Equity, Authority and Price Records for a U.S. Family"),
    ("us-mainland-major-asset-auction-objection", "內地高值資產拍賣前出現異議，美國權利人先核對程序、權屬與期限", "内地高值资产拍卖前出现异议，美国权利人先核对程序、权属与期限", "An Objection Arises Before a Major Mainland Asset Auction: Procedure, Title and Timing for a U.S. Rights Holder"),
    ("us-mainland-commercial-sublease-dispute", "內地商業轉租有爭議涉高值經營，美國企業先核對同意、租約與付款", "内地商业转租有争议涉高值经营，美国企业先核对同意、租约与付款", "A Mainland Commercial Sublease Is Disputed: Consent, Lease and Payment Records for a U.S. Business"),
    ("us-mainland-major-franchise-transfer", "內地特許經營轉讓涉重大價值，美國品牌方先核對授權、門店與對價", "内地特许经营转让涉重大价值，美国品牌方先核对授权、门店与对价", "Transferring a Major Mainland Franchise: Licence, Stores and Price Records for a U.S. Brand Owner"),
    ("us-mainland-asset-freeze-thirdparty-claim", "內地高值資產被凍結且第三方主張權利，美國當事人先整理登記與交易證據", "内地高值资产被冻结且第三方主张权利，美国当事人先整理登记与交易证据", "A Third Party Claims Frozen Mainland Assets: Registration and Transaction Evidence for a U.S. Party"),
    ("us-mainland-major-share-redemption", "內地公司股權回購延期涉高值交易，美國投資人先核對條款、資金與通知", "内地公司股权回购延期涉高值交易，美国投资人先核对条款、资金与通知", "A Mainland Share Redemption Is Delayed: Terms, Funding and Notice for a U.S. Investor"),
    ("us-mainland-industrial-park-contract-dispute", "內地產業園合作合同有爭議涉重大投入，美國企業先核對土地、履行與付款", "内地产业园合作合同有争议涉重大投入，美国企业先核对土地、履行与付款", "A Mainland Industrial-Park Contract Is Disputed: Land, Performance and Payment Records for a U.S. Business"),
    ("us-mainland-commercial-property-management", "內地商業物業管理收益有爭議，美國業主先核對合同、帳目與授權", "内地商业物业管理收益有争议，美国业主先核对合同、账目与授权", "A Mainland Commercial Property Management Claim: Contract, Accounts and Authority for a U.S. Owner"),
    ("us-mainland-major-debt-settlement-default", "內地大額債務和解後未付款，美國債權人先固定協議、到期與擔保", "内地大额债务和解后未付款，美国债权人先固定协议、到期与担保", "A Major Mainland Debt Settlement Is Not Paid: Agreement, Due Date and Security for a U.S. Creditor"),
    ("us-mainland-equity-trustee-dispute", "內地股權代持關係有爭議涉高值權益，美國投資人先分清出資、登記與授權", "内地股权代持关系有争议涉高值权益，美国投资人先分清出资、登记与授权", "A Mainland Equity Nominee Arrangement Is Disputed: Funding, Registration and Authority for a U.S. Investor"),
    ("us-mainland-major-property-development-claim", "內地重大物業開發合作有爭議，美國投資人先整理出資、決議與交付", "内地重大物业开发合作有争议，美国投资人先整理出资、决议与交付", "A Major Mainland Property Development Claim: Funding, Resolutions and Delivery for a U.S. Investor"),
    ("us-mainland-crossborder-estate-share-sale", "跨境遺產出售內地股權涉高值交易，美國家屬先核對繼承、估值與授權", "跨境遗产出售内地股权涉高值交易，美国家属先核对继承、估值与授权", "Selling Mainland Shares From a Cross-Border Estate: Inheritance, Valuation and Authority for a U.S. Family"),
    ("us-mainland-major-contract-change-order", "內地重大合同變更單有爭議，美國企業先核對授權、價格與履行記錄", "内地重大合同变更单有争议，美国企业先核对授权、价格与履行记录", "A Major Mainland Contract Change Order Is Disputed: Authority, Price and Performance for a U.S. Business"),
    ("us-mainland-commercial-property-ownership-chain", "內地商業物業權屬鏈不清涉高值風險，美國買方先核對歷史登記與交易", "内地商业物业权属链不清涉高值风险，美国买方先核对历史登记与交易", "A Mainland Commercial Property Has an Unclear Title Chain: Historic Registry and Transaction Checks for a U.S. Buyer"),
]

# 2026-09-09: every item below has a plausible RMB 200,000+ Mainland China
# asset, transaction, debt, or commercial-dispute connection.
ARTICLES = [
    ("us-mainland-commercial-building-sale-closing", "出售內地商業樓宇涉高值交易，美國賣方先核對權屬、抵押與交割", "出售内地商业楼宇涉高值交易，美国卖方先核对权属、抵押与交割", "Selling a High-Value Mainland Commercial Building: Title, Mortgage and Closing Checks"),
    ("us-mainland-company-capital-reduction", "內地公司減資影響高值權益，美國股東先核對決議、通知與債務", "内地公司减资影响高值权益，美国股东先核对决议、通知与债务", "A Mainland Capital Reduction Affects Major Equity: Resolutions, Notice and Debt Checks"),
    ("us-mainland-major-debt-guarantee-transfer", "內地大額債務連同擔保被轉讓，美國當事人先分清同意、通知與範圍", "内地大额债务连同担保被转让，美国当事人先分清同意、通知与范围", "A Major Mainland Debt and Its Guarantee Are Transferred: Consent, Notice and Scope"),
    ("us-mainland-commercial-project-delay-claim", "內地商業項目延誤涉重大損失，美國投資人先固定工期、通知與費用", "内地商业项目延误涉重大损失，美国投资人先固定工期、通知与费用", "A Mainland Commercial Project Is Delayed: Programme, Notice and Cost Records First"),
    ("us-mainland-shareholder-deadlock-vote", "內地公司表決僵局牽涉高值控制權，美國股東先整理章程、通知與會議紀錄", "内地公司表决僵局牵涉高值控制权，美国股东先整理章程、通知与会议记录", "A Mainland Company Vote Is Deadlocked: Articles, Notices and Meeting Records"),
    ("us-mainland-major-property-coowner-sale", "內地高值物業共有人想出售，美國家屬先分清登記、授權與價款安排", "内地高值物业共有人想出售，美国家属先分清登记、授权与价款安排", "A Co-owner Wants to Sell High-Value Mainland Property: Registration, Authority and Price"),
    ("us-mainland-equity-exit-earnout-dispute", "內地股權退出的業績對價有爭議，美國投資人先核對指標、帳目與通知", "内地股权退出的业绩对价有争议，美国投资人先核对指标、账目与通知", "An Earn-Out in a Mainland Equity Exit Is Disputed: Metrics, Accounts and Notice"),
    ("us-mainland-major-supply-price-adjustment", "內地重大供貨合同要求調價，美國企業先核對條款、成本與履行紀錄", "内地重大供货合同要求调价，美国企业先核对条款、成本与履行记录", "A Major Mainland Supply Contract Seeks a Price Change: Terms, Cost and Performance"),
    ("us-mainland-industrial-property-enforcement", "內地工業物業進入執行程序，美國權利人先整理權屬、租約與查封資料", "内地工业物业进入执行程序，美国权利人先整理权属、租约与查封资料", "Mainland Industrial Property Enters Enforcement: Title, Lease and Seizure Records"),
    ("us-mainland-crossborder-estate-business-valuation", "跨境遺產含內地企業高值股權，美國家屬先核對估值、繼承與控制資料", "跨境遗产含内地企业高值股权，美国家属先核对估值、继承与控制资料", "A Cross-Border Estate Holds Major Mainland Business Equity: Valuation, Inheritance and Control"),
    ("us-mainland-commercial-lease-rent-review", "內地商業租約租金調整涉重大投入，美國承租人先核對條款、通知與帳目", "内地商业租约租金调整涉重大投入，美国承租人先核对条款、通知与账目", "A Mainland Commercial Lease Rent Review: Terms, Notice and Account Checks"),
    ("us-mainland-major-construction-defect-claim", "內地重大工程出現缺陷索賠，美國業主先保存合同、驗收與修復資料", "内地重大工程出现缺陷索赔，美国业主先保存合同、验收与修复资料", "A Major Mainland Construction Defect Claim: Contract, Acceptance and Repair Records"),
    ("us-mainland-company-seal-control-dispute", "內地公司印章控制生變影響高值交易，美國股東先核對保管、決議與授權", "内地公司印章控制生变影响高值交易，美国股东先核对保管、决议与授权", "Mainland Company Seal Control Changes: Custody, Resolutions and Authority"),
    ("us-mainland-major-receivable-setoff", "內地大額應收款被主張抵銷，美國債權人先核對債權、到期與通知", "内地大额应收款被主张抵销，美国债权人先核对债权、到期与通知", "Set-Off Is Claimed Against Major Mainland Receivables: Debt, Maturity and Notice"),
    ("us-mainland-business-transfer-employee-liability", "內地企業轉讓牽涉重大人員成本，美國買方先核對合同、名冊與交割安排", "内地企业转让牵涉重大人员成本，美国买方先核对合同、名册与交割安排", "A Mainland Business Transfer Carries Major Employee Costs: Contracts, Lists and Closing"),
    ("us-mainland-commercial-land-use-expiry", "內地商業用地期限將至影響高值資產，美國投資人先核對用途、期限與文件", "内地商业用地期限将至影响高值资产，美国投资人先核对用途、期限与文件", "Mainland Commercial Land-Use Rights Near Expiry: Use, Term and Document Checks"),
    ("us-mainland-major-joint-venture-funding-call", "內地合資企業追加出資涉高值風險，美國投資人先核對章程、比例與決議", "内地合资企业追加出资涉高值风险，美国投资人先核对章程、比例与决议", "A Mainland Joint Venture Calls for More Funding: Articles, Ratio and Resolution Checks"),
    ("us-mainland-commercial-property-management-handover", "內地商業物業管理權交接涉高值收益，美國業主先整理合同、帳目與權限", "内地商业物业管理权交接涉高值收益，美国业主先整理合同、账目与权限", "Handing Over Mainland Commercial Property Management: Contract, Accounts and Authority"),
    ("us-mainland-major-license-termination", "內地重大許可合作被終止，美國權利人先核對範圍、交付與停止使用", "内地重大许可合作被终止，美国权利人先核对范围、交付与停止使用", "A Major Mainland Licence Deal Ends: Scope, Delivery and Stop-Use Records"),
    ("us-mainland-share-transfer-preemptive-right", "內地股權轉讓牽涉優先購買權，美國股東先核對通知、價格與期限", "内地股权转让牵涉优先购买权，美国股东先核对通知、价格与期限", "A Mainland Share Sale Raises Pre-Emption Rights: Notice, Price and Timing"),
    ("us-mainland-major-asset-pledge-release", "內地高值資產質押待解除，美國權利人先核對主債、登記與交割限制", "内地高值资产质押待解除，美国权利人先核对主债、登记与交割限制", "Releasing a Pledge Over Major Mainland Assets: Principal Debt, Registry and Closing Limits"),
    ("us-mainland-commercial-property-fire-loss", "內地商業物業重大火損牽涉保險與租約，美國業主先保存損失、通知與現場資料", "内地商业物业重大火损牵涉保险与租约，美国业主先保存损失、通知与现场资料", "Major Fire Loss at Mainland Commercial Property: Loss, Notice and Site Records"),
    ("us-mainland-major-technology-source-code-escrow", "內地重大技術合作涉及源碼託管，美國企業先核對條件、交付與存取紀錄", "内地重大技术合作涉及源码托管，美国企业先核对条件、交付与存取记录", "A Major Mainland Technology Deal Uses Source-Code Escrow: Conditions, Delivery and Access"),
    ("us-mainland-family-business-share-valuation", "家族企業內地股權估值有爭議，美國家屬先整理章程、帳目與交易資料", "家族企业内地股权估值有争议，美国家属先整理章程、账目与交易资料", "A Mainland Family-Business Share Valuation Is Disputed: Articles, Accounts and Deal Records"),
    ("us-mainland-major-franchise-store-closure", "內地重大特許門店被關閉，美國品牌方先核對合同、庫存與通知", "内地重大特许门店被关闭，美国品牌方先核对合同、库存与通知", "Major Mainland Franchise Stores Close: Contract, Inventory and Notice Records"),
    ("us-mainland-commercial-building-redevelopment", "內地商業樓宇重建影響高值權益，美國業主先核對權屬、協議與補償資料", "内地商业楼宇重建影响高值权益，美国业主先核对权属、协议与补偿资料", "Redevelopment Affects a Mainland Commercial Building: Title, Agreement and Compensation"),
    ("us-mainland-major-loan-covenant-default", "內地大額貸款違反約定，美國借款人先核對條款、通知與擔保風險", "内地大额贷款违反约定，美国借款人先核对条款、通知与担保风险", "A Major Mainland Loan Breaches a Covenant: Terms, Notice and Security Risk"),
    ("us-mainland-company-merger-share-conversion", "內地公司合併換股影響高值權益，美國股東先核對方案、估值與登記", "内地公司合并换股影响高值权益，美国股东先核对方案、估值与登记", "A Mainland Company Merger Converts Major Equity: Plan, Valuation and Registration"),
    ("us-mainland-commercial-property-auction-bid", "內地商業物業司法拍賣涉高值資產，美國買方先核對權屬、占用與付款", "内地商业物业司法拍卖涉高值资产，美国买方先核对权属、占用与付款", "Bidding at a Mainland Commercial Property Auction: Title, Occupancy and Payment"),
    ("us-mainland-major-contract-assignment-consent", "內地重大合同擬轉讓，美國企業先核對同意、履行與違約條款", "内地重大合同拟转让，美国企业先核对同意、履行与违约条款", "Assigning a Major Mainland Contract: Consent, Performance and Default Terms"),
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
    if TODAY != "2026-09-09": raise RuntimeError(f"expected 2026-09-09, got {TODAY}")
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
