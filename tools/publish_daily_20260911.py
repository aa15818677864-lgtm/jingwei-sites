from __future__ import annotations

"""Publish the 2026-09-11 high-value U.S./Mainland China article batch.

This intentionally reuses the established page, sitemap, research-log and
verified-publication plumbing while supplying a distinct, screened topic set.
"""

import sys
from pathlib import Path

import publish_daily_20260904 as base


TODAY = "2026-09-11"

# Each topic concerns a Mainland China commercial asset, equity interest,
# major transaction, debt, or enforcement issue that ordinarily has a
# RMB 200,000+ value or dispute-value connection.
ARTICLES = [
    ("us-mainland-commercial-property-deposit-forfeit", "內地商業物業訂金可能被沒收，美國買方先核對違約、通知與付款", "内地商业物业定金可能被没收，美国买方先核对违约、通知与付款", "A Mainland Commercial Property Deposit May Be Forfeited: Default, Notice and Payment Checks"),
    ("us-mainland-company-equity-inheritance-registration", "繼承內地公司高值股權，美國家屬先核對章程、身分與登記", "继承内地公司高值股权，美国家属先核对章程、身份与登记", "Inheriting Major Equity in a Mainland Company: Articles, Identity and Registration Checks"),
    ("us-mainland-major-loan-acceleration-notice", "內地大額貸款被宣布提前到期，美國借款人先核對條款、送達與擔保", "内地大额贷款被宣布提前到期，美国借款人先核对条款、送达与担保", "A Major Mainland Loan Is Accelerated: Terms, Notice and Security Checks"),
    ("us-mainland-commercial-property-right-of-first-refusal", "內地商業物業出售觸及優先購買權，美國權利人先整理通知、價格與期限", "内地商业物业出售触及优先购买权，美国权利人先整理通知、价格与期限", "A Mainland Commercial Property Sale Triggers First-Refusal Rights: Notice, Price and Timing"),
    ("us-mainland-company-profit-transfer-dispute", "內地公司利潤分配有爭議，美國股東先分清帳目、決議與付款依據", "内地公司利润分配有争议，美国股东先分清账目、决议与付款依据", "A Mainland Company Profit Distribution Is Disputed: Accounts, Resolutions and Payment Basis"),
    ("us-mainland-major-contract-oral-change", "內地重大合同的變更指示未入書面，美國企業先固定誰授權、何時履行", "内地重大合同的变更指示未入书面，美国企业先固定谁授权、何时履行", "A Major Mainland Contract Change Was Not Put in Writing: Authority and Performance Records"),
    ("us-mainland-industrial-property-tenant-insolvency", "內地工業物業承租人資不抵債，美國業主先核對租約、占用與債權位置", "内地工业物业承租人资不抵债，美国业主先核对租约、占用与债权位置", "An Industrial Mainland Tenant Becomes Insolvent: Lease, Possession and Claim Position"),
    ("us-mainland-equity-transfer-price-holdback", "內地股權交易保留價款未釋放，美國賣方先核對條件、帳目與通知", "内地股权交易保留价款未释放，美国卖方先核对条件、账目与通知", "A Mainland Equity Deal Holdback Is Not Released: Conditions, Accounts and Notice"),
    ("us-mainland-major-receivable-assignment", "內地大額應收款被轉讓，美國債權人先核對原債權、通知與回款帳戶", "内地大额应收款被转让，美国债权人先核对原债权、通知与回款账户", "A Major Mainland Receivable Is Assigned: Original Claim, Notice and Collection Account"),
    ("us-mainland-commercial-property-coowner-mortgage", "內地商業物業共有人擬抵押高值資產，美國共有人先看登記、授權與債務", "内地商业物业共有人拟抵押高值资产，美国共有人先看登记、授权与债务", "A Co-owner Plans to Mortgage Mainland Commercial Property: Registration, Authority and Debt"),
    ("us-mainland-company-business-license-control", "內地公司營業執照與印章控制失衡，美國股東先整理保管、決議與交接", "内地公司营业执照与印章控制失衡，美国股东先整理保管、决议与交接", "A Mainland Company Loses Control of Its Licence and Seal: Custody, Resolutions and Handover"),
    ("us-mainland-major-supply-inventory-recovery", "內地重大供貨合作終止後要收回庫存，美國品牌方先分清貨權、倉儲與通知", "内地重大供货合作终止后要收回库存，美国品牌方先分清货权、仓储与通知", "Recovering Inventory After a Major Mainland Supply Deal Ends: Title, Storage and Notice"),
    ("us-mainland-commercial-lease-guarantor-scope", "內地商業租約附有大額保證，美國保證人先核對範圍、續期與違約通知", "内地商业租约附有大额保证，美国保证人先核对范围、续期与违约通知", "A Mainland Commercial Lease Has a Major Guarantee: Scope, Renewal and Default Notice"),
    ("us-mainland-company-share-pledge-priority", "內地公司股權被多重質押，美國出資人先核對登記順序與主債範圍", "内地公司股权被多重质押，美国出资人先核对登记顺序与主债范围", "Mainland Company Equity Has Multiple Pledges: Registration Order and Secured-Debt Scope"),
    ("us-mainland-major-construction-delay-extension", "內地重大工程工期一再延長，美國業主先對齊變更、工期與費用紀錄", "内地重大工程工期一再延长，美国业主先对齐变更、工期与费用记录", "A Major Mainland Construction Project Keeps Extending: Change, Time and Cost Records"),
    ("us-mainland-commercial-property-eviction-enforcement", "內地商業物業騰退進入執行，美國業主先整理判決、占用與現場資料", "内地商业物业腾退进入执行，美国业主先整理判决、占用与现场资料", "Commercial Property Eviction Reaches Mainland Enforcement: Judgment, Occupancy and Site Records"),
    ("us-mainland-crossborder-estate-company-debt", "跨境遺產持有內地公司又有大額債務，美國家屬先分開股權、遺產與責任", "跨境遗产持有内地公司又有大额债务，美国家属先分开股权、遗产与责任", "A Cross-Border Estate Holds a Mainland Company With Major Debt: Equity, Estate and Liability"),
    ("us-mainland-major-asset-sale-payment-security", "出售內地重大資產的尾款缺乏保障，美國賣方先核對付款、擔保與交割", "出售内地重大资产的尾款缺乏保障，美国卖方先核对付款、担保与交割", "Final Payment for a Major Mainland Asset Sale Lacks Security: Payment, Security and Closing"),
    ("us-mainland-company-director-duty-claim", "內地公司董事決策引發高值損失爭議，美國股東先保留決議、帳目與授權", "内地公司董事决策引发高值损失争议，美国股东先保留决议、账目与授权", "A Mainland Director Decision Leads to a Major-Loss Dispute: Resolutions, Accounts and Authority"),
    ("us-mainland-commercial-property-insurance-proceeds", "內地商業物業重大事故後保險款有爭議，美國業主先核對保單、損失與收款權", "内地商业物业重大事故后保险款有争议，美国业主先核对保单、损失与收款权", "Insurance Proceeds After a Major Mainland Commercial Property Loss: Policy, Damage and Payee Rights"),
    ("us-mainland-major-joint-venture-deadlock", "內地合資企業陷入重大僵局，美國投資人先核對章程、表決與退出資料", "内地合资企业陷入重大僵局，美国投资人先核对章程、表决与退出资料", "A Major Mainland Joint Venture Is Deadlocked: Articles, Voting and Exit Records"),
    ("us-mainland-equity-sale-disclosure-breach", "出售內地高值股權後出現披露爭議，美國買方先固定保證、資料室與通知", "出售内地高值股权后出现披露争议，美国买方先固定保证、资料室与通知", "A High-Value Mainland Equity Sale Has a Disclosure Dispute: Warranties, Data Room and Notice"),
    ("us-mainland-major-service-contract-nonpayment", "內地重大服務合同已履行但未付款，美國企業先整理交付、驗收與對帳", "内地重大服务合同已履行但未付款，美国企业先整理交付、验收与对账", "A Major Mainland Service Contract Was Performed but Not Paid: Delivery, Acceptance and Reconciliation"),
    ("us-mainland-commercial-property-redevelopment-consent", "內地商業物業重建需要多方同意，美國權利人先核對登記、協議與補償安排", "内地商业物业重建需要多方同意，美国权利人先核对登记、协议与补偿安排", "Redeveloping Mainland Commercial Property Needs Multiple Consents: Registration, Agreements and Compensation"),
    ("us-mainland-company-capital-reduction-creditor", "內地公司減資牽涉大額債權，美國債權人先核對通知、期限與擔保", "内地公司减资牵涉大额债权，美国债权人先核对通知、期限与担保", "A Mainland Company Reduces Capital While Major Debt Is Owed: Notice, Timing and Security"),
    ("us-mainland-major-technology-acceptance-dispute", "內地重大技術項目驗收有爭議，美國權利人先對齊規格、測試與付款節點", "内地重大技术项目验收有争议，美国权利人先对齐规格、测试与付款节点", "A Major Mainland Technology Project Has an Acceptance Dispute: Specifications, Testing and Payment Milestones"),
    ("us-mainland-industrial-land-use-transfer", "轉讓內地工業用地使用權涉高值交易，美國投資人先核對用途、期限與限制", "转让内地工业用地使用权涉高值交易，美国投资人先核对用途、期限与限制", "Transferring Mainland Industrial Land-Use Rights: Use, Term and Restriction Checks"),
    ("us-mainland-major-debt-enforcement-settlement", "內地大額債務進入執行後擬和解，美國當事人先核對標的、付款與解除範圍", "内地大额债务进入执行后拟和解，美国当事人先核对标的、付款与解除范围", "Settling a Major Mainland Debt After Enforcement Begins: Subject, Payment and Release Scope"),
    ("us-mainland-commercial-property-sale-occupancy", "出售內地商業物業時仍有人占用，美國賣方先核對租約、交付與違約安排", "出售内地商业物业时仍有人占用，美国卖方先核对租约、交付与违约安排", "A Mainland Commercial Property Is Still Occupied at Sale: Lease, Delivery and Default Arrangements"),
    ("us-mainland-family-business-control-succession", "家族企業控制權交接牽涉內地高值資產，美國家屬先整理股權、授權與決議", "家族企业控制权交接牵涉内地高值资产，美国家属先整理股权、授权与决议", "Family-Business Control Succession Affects Major Mainland Assets: Equity, Authority and Resolutions"),
]


def configure() -> None:
    base.TODAY = TODAY
    base.ARTICLES = ARTICLES


def main() -> None:
    configure()
    for slug, tc, cn, en in ARTICLES:
        for code, title in (("tc", tc), ("cn", cn), ("en", en)):
            content = base.page(slug, title, code).replace(
                f'<p class="article-last-updated"><time datetime="{TODAY}">{TODAY}</time></p>',
                f'<p class="article-last-updated">{base.UPDATED[code]}: <time datetime="{TODAY}">{TODAY}</time></p>',
            )
            (base.ROOT / "articles" / "us" / Path(base.path(slug, code)).name).write_text(content, encoding="utf-8")
    base.add_cards()
    base.update_sitemap()
    base.report()
    base.write_research_log()
    print(f"generated {len(ARTICLES)} stories / {len(ARTICLES) * 3} pages")


if __name__ == "__main__":
    configure()
    base.record_verified_publication() if "--record" in sys.argv else main()
