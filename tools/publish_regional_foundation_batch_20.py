from __future__ import annotations

from publish_regional_inheritance_foundations import (
    LANG_SUFFIX,
    ROOT,
    SITE,
    TODAY,
    article_path,
    render_article,
)


ARTICLES = [
    {
        "slug": "mortgaged-mainland-property",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門家屬與按揭房產",
                "title": "內地房產仍有按揭，澳門家屬先向誰查欠款和狀態",
                "description": "澳門家屬繼承仍有按揭的內地房產時，先分開查房產登記、抵押狀態、貸款餘額和目前供款安排。",
                "lead": "有人仍在供款，不代表貸款、抵押登記和扣款賬戶都處於同一個狀態。",
                "key_title": "先對清三份資料",
                "keys": [
                    "最新房產和抵押登記",
                    "銀行貸款餘額與逾期情況",
                    "目前由誰供款及款項來源",
                ],
                "answer_title": "銀行、登記和家屬賬目要分開查",
                "answer": [
                    "先不要只問還欠多少。房產登記回答誰擁有房屋、是否仍有抵押；貸款銀行回答借款人、餘額、還款和逾期；家屬還要記清去世後由誰繼續付款。三份資料對上後，才知道繼承、清償或日後出售卡在哪裏。",
                    "逝者留下的債務應放回整體遺產中核對，家屬不要在資料不全時先承諾以個人財產全部償還。澳門的繼承或管理身份文件也不會自動改變內地貸款合同和抵押登記。",
                ],
                "sections": [
                    (
                        "先做一張貸款事實表",
                        [
                            "先查逝者到底是借錢的人、與他人一起借錢的人、替人擔保的人，還是只把房屋拿來抵押的人。再記下銀行全名、經辦分行、合同或貸款編號、房屋地址、每月還款日和扣款賬戶，向銀行索取其接受申請人查閱的最新餘額、逾期、利息和提前清償資料。",
                            "同時找購房合同、貸款合同、還款流水、保險、銀行通知和最近一次繳款記錄。若只剩手機短訊或家人記憶，標成線索，不要把它寫成銀行已確認的結論。",
                        ],
                    ),
                    (
                        "不要突然停供，也不要私自登入逝者賬戶",
                        [
                            "先問銀行逝者去世後可用甚麼方式繼續付款、由誰提交死亡和身份資料，以及原扣款賬戶不能使用時怎樣處理。不要使用逝者密碼、驗證碼或人臉登入，也不要自行改動扣款安排。",
                            "若家人為避免逾期而暫時墊付，保留日期、金額、付款賬戶、銀行回單和家人之間的說明。墊付不會自動增加房產份額，能否由遺產償還也要在賬目和分配中另行處理。",
                        ],
                    ),
                    (
                        "一份澳門文件不能同時回答銀行和登記問題",
                        [
                            "澳門死亡、親屬、繼承人資格或管理身份文件，主要用來說明死亡、家屬和誰可代表遺產。交給內地銀行前，先問需要哪一種正式版本、翻譯、身份銜接和授權範圍。",
                            "房產所在地仍要核對現有權利人、共有份額、抵押權人和限制狀態。登記結果不等於即時貸款結單，銀行餘額也不等於房產已能辦繼承轉移，兩邊要分別取得可核對的回覆。",
                        ],
                    ),
                    (
                        "最後才比較繼續還款、清償或處理房屋",
                        [
                            "把房屋價值線索、貸款餘額、其他債務、共有情況、繼承人意見和現金來源放在同一頁，再問銀行及房產所在地可接受的方案。不要因為房屋有按揭就先假設只能放棄，也不要先承諾一定可以轉貸。",
                            "有些地方存在抵押未解除時配合轉移或出售的做法，但需要銀行、登記、買方和實際交易條件一起配合，不能當成每宗繼承都能使用的捷徑。先把欠款和權屬查清，再選路徑。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門家屬繼承內地房產先從哪一步開始"),
                    ("/articles/am/estate-manager-role-boundary.html", "待分割財產管理人能做甚麼"),
                    ("/articles/am/macau-heir-qualification-deed.html", "澳門繼承人資格文件能說明甚麼"),
                ],
                "cta": "把銀行、貸款編號、房屋地址、最近供款和現有澳門文件列在一頁，我們先找出應向銀行還是登記端確認。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门家属与按揭房产",
                "title": "内地房产仍有按揭，澳门家属先向谁查欠款和状态",
                "description": "澳门家属继承仍有按揭的内地房产时，先分开查询房产登记、抵押状态、贷款余额和目前还款安排。",
                "lead": "有人仍在还款，不代表贷款、抵押登记和扣款账户都处于同一个状态。",
                "key_title": "先对清三份材料",
                "keys": [
                    "最新房产和抵押登记",
                    "银行贷款余额与逾期情况",
                    "目前由谁还款及款项来源",
                ],
                "answer_title": "银行、登记和家属账目要分开查",
                "answer": [
                    "先不要只问还欠多少。房产登记回答谁拥有房屋、是否仍有抵押；贷款银行回答借款人、余额、还款和逾期；家属还要记清去世后由谁继续付款。三份材料对上后，才知道继承、清偿或以后出售卡在哪里。",
                    "逝者留下的债务应放回整体遗产中核对，家属不要在材料不全时先承诺用个人财产全部偿还。澳门的继承或管理身份文件也不会自动改变内地贷款合同和抵押登记。",
                ],
                "sections": [
                    (
                        "先做一张贷款事实表",
                        [
                            "先查逝者到底是借款的人、与他人共同借款的人、替人担保的人，还是只把房屋用于抵押的人。再记下银行全名、经办分行、合同或贷款编号、房屋地址、每月还款日和扣款账户，向银行索取其允许申请人查看的最新余额、逾期、利息和提前清偿材料。",
                            "同时寻找购房合同、贷款合同、还款流水、保险、银行通知和最近一次缴款记录。如果只剩手机短信或家人记忆，标成线索，不要写成银行已经确认的结论。",
                        ],
                    ),
                    (
                        "不要突然停供，也不要私自登录逝者账户",
                        [
                            "先问银行逝者去世后可以用什么方式继续付款、由谁提交死亡和身份材料，以及原扣款账户不能使用时怎样处理。不要使用逝者密码、验证码或人脸登录，也不要自行改动扣款安排。",
                            "如果家人为避免逾期而暂时垫付，保留日期、金额、付款账户、银行回单和家人之间的说明。垫付不会自动增加房产份额，能否由遗产偿还也要在账目和分配中另行处理。",
                        ],
                    ),
                    (
                        "一份澳门文件不能同时回答银行和登记问题",
                        [
                            "澳门死亡、亲属、继承人资格或管理身份文件，主要用来说明死亡、家属和谁可以代表遗产。交给内地银行前，先问需要哪一种正式版本、翻译、身份衔接和授权范围。",
                            "房产所在地仍要核对现有权利人、共有份额、抵押权人和限制状态。登记结果不等于即时贷款结单，银行余额也不等于房产已经可以办理继承转移，两边要分别取得可以核对的回复。",
                        ],
                    ),
                    (
                        "最后再比较继续还款、清偿或处理房屋",
                        [
                            "把房屋价值线索、贷款余额、其他债务、共有情况、继承人意见和现金来源放在同一页，再询问银行及房产所在地可以接受的方案。不要因为房屋有按揭就先假设只能放弃，也不要先承诺一定可以转贷。",
                            "有些地方存在抵押未解除时配合转移或出售的做法，但需要银行、登记、买方和实际交易条件共同配合，不能当成每宗继承都能使用的捷径。先把欠款和权属查清，再选择路径。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门家属继承内地房产先从哪一步开始"),
                    ("/articles/am/estate-manager-role-boundary_cn.html", "待分割财产管理人能做什么"),
                    ("/articles/am/macau-heir-qualification-deed_cn.html", "澳门继承人资格文件能说明什么"),
                ],
                "cta": "把银行、贷款编号、房屋地址、最近还款和现有澳门文件列在一页，我们先找出应该向银行还是登记端确认。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau families and mortgaged property",
                "title": "Mortgaged Mainland Home: What a Macau Family Should Check First",
                "description": "A practical guide for Macau families checking the title, mortgage registration, loan balance and payments before handling a Mainland inheritance.",
                "lead": "A continuing monthly payment does not prove that the loan, mortgage record and payment account are all in order.",
                "key_title": "Match three records first",
                "keys": [
                    "Current title and mortgage record",
                    "Loan balance and missed payments",
                    "Who is paying and where the money comes from",
                ],
                "answer_title": "Ask the bank, registry and family bookkeeper different questions",
                "answer": [
                    "The title record identifies the owner and registered mortgage. The lender confirms the borrower, current balance, payment status and arrears. The family must separately record who paid after the death. Those three records reveal whether the immediate issue is inheritance, repayment or a later sale.",
                    "Review the debt as part of the estate before anyone promises to repay it from personal funds. A Macau heirship or estate-management document does not by itself amend the Mainland loan contract or mortgage registration.",
                ],
                "sections": [
                    (
                        "Build a one-page loan record",
                        [
                            "First identify whether the deceased borrowed the money, borrowed with someone else, guaranteed another borrower or only provided the home as security. Then record the lender, branch, loan number, property address, payment date and debit account before asking what an eligible applicant may receive about the balance, arrears, interest and early settlement.",
                            "Find the purchase and loan contracts, payment statements, insurance, bank notices and latest receipt. Treat a text message or family recollection as a clue until the lender confirms it.",
                        ],
                    ),
                    (
                        "Do not stop payments suddenly or enter the deceased's account",
                        [
                            "Ask the lender how payments can be made after the death, who may submit death and identity records, and what happens if the original debit account cannot be used. Do not use the deceased's password, verification code or face login, and do not quietly change the payment arrangement.",
                            "If a relative advances a payment to avoid arrears, keep the date, amount, paying account, receipt and family explanation. An advance does not create a larger property share, and reimbursement from the estate must be considered separately.",
                        ],
                    ),
                    (
                        "A Macau document cannot answer both the bank and title questions",
                        [
                            "Macau death, relationship, heirship and estate-management records help explain the family and who may speak for the estate. Ask the Mainland lender which official version, translation, identity link and authority it requires.",
                            "The property city must still confirm the current owner, co-ownership, mortgagee and restrictions. A title search is not a live loan statement, and a balance letter does not mean that an inheritance transfer is ready. Obtain separate answers.",
                        ],
                    ),
                    (
                        "Compare repayment and property options only after the facts match",
                        [
                            "Place the estimated property value, loan balance, other debts, co-ownership, heirs' positions and available cash on one page. Then ask the lender and property city which routes are open. A mortgage does not automatically mean the family should disclaim the property, and refinancing should never be promised in advance.",
                            "Some cities support a transfer or sale while a mortgage remains, but that requires the lender, registry, buyer and transaction terms to align. It is not a standard shortcut for every inheritance. Confirm the debt and title before choosing a route.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Where to start with a Mainland property inheritance"),
                    ("/articles/am/estate-manager-role-boundary_en.html", "What an estate manager can and cannot decide"),
                    ("/articles/am/macau-heir-qualification-deed_en.html", "What a Macau heirship document establishes"),
                ],
                "cta": "List the lender, loan number, property address, latest payment and available Macau records on one page. We can then identify which questions belong to the bank and which to the registry.",
            },
        },
    },
    {
        "slug": "known-mainland-bank-deposit",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國家屬與內地存款",
                "title": "知道內地銀行和賬戶線索，美國家屬先準備甚麼",
                "description": "美國家屬知道逝者的內地銀行或賬戶線索時，先分清查詢、簡化提取、普通繼承和匯款四個不同步驟。",
                "lead": "找到銀行卡或短訊，只代表有一條存款線索，不代表任何家人都可以登入、查賬或提取。",
                "key_title": "先寫清三件事",
                "keys": [
                    "銀行全名、分行和產品線索",
                    "誰準備申請及與逝者的關係",
                    "美國文件由哪個州或法院簽發",
                ],
                "answer_title": "先向銀行要兩張清單",
                "answer": [
                    "第一張是查詢清單：誰可查、可查甚麼、要哪些死亡和親屬資料。第二張是提取清單：這宗存款能否用小額簡化方式，還是要走普通繼承程序。查到賬戶、取得款項和匯往美國，是三個不同問題。",
                    "美國遺囑中的受益人、被提名的執行人和法院正式任命的遺產代表，也不是同一身份。把州、縣、法院文件名稱和目前權限寫清楚，再問內地銀行實際接受哪一份。",
                ],
                "sections": [
                    (
                        "先認清銀行和產品，不要只看卡片外觀",
                        [
                            "記下銀行法定名稱、開戶分行線索、卡號或賬號末幾位、幣種、最近通知日期和客服來源。銀行曾改名、分行撤併或只知道手機應用名稱時，把每個版本保留，不要自行猜一個新分行。",
                            "分開標記活期、定期、理財、國債、黃金積存或其他產品。銀行通常按自己的同一法人機構合計，不一定只看家屬手上這張卡；申請人身份和產品是否到期或可贖回，也會影響能否使用簡化方式。",
                        ],
                    ),
                    (
                        "先問查詢，再決定辦哪一種提取",
                        [
                            "向銀行說明逝者姓名、證件線索、死亡地、申請人關係和目前只想核對甚麼。問清可否查餘額、產品種類或特定期間交易資料，以及是否必須本人到場或可以委託。餘額查詢和交易明細的條件及範圍可能不同，不要把能確認賬戶理解成可以取得完整流水。",
                            "符合現行小額簡化條件時，部分近親屬或指定人士可能不必先辦完整的普通繼承證明，但仍要提交死亡、關係、身份和承諾資料。超出條件、家屬有爭議或產品情況不同時，銀行會要求另一套辦理資料。",
                        ],
                    ),
                    (
                        "把內地資料和美國代表文件分成兩袋",
                        [
                            "內地袋放逝者的中文姓名、舊證件、銀行線索、死亡和親屬資料；美國袋放死亡記錄、遺囑、案件州和縣、法院命令及現行 Letters。申請書、法院命令和正式代表文件不要統稱為 probate papers。",
                            "美國法院文件通常只說明該州程序中的角色和權限，不會自動命令內地銀行付款。交件前先問銀行需要正本、正式副本、附加證明、翻譯和姓名銜接中的哪些項目。",
                        ],
                    ),
                    (
                        "收到款項後，保留去向和結清紀錄",
                        [
                            "不要把逝者資金先轉入某位家人的日常賬戶再慢慢分。確認銀行會付給誰、是否一次性提取及銷戶、未到期產品怎樣處理，並保存申請、回單、結息和賬戶狀態。",
                            "款項在美國一端應進遺產賬戶還是由某人直接接收，要按案件所在州、法院任命和實際受益安排確認。跨境匯款的來源證明和申報是下一步，不能用已成功提取來代替。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/letters-testamentary-or-administration.html", "先分清美國法院任命文件"),
                    ("/articles/us/us-death-certificate-for-mainland.html", "美國死亡證明交到內地前先查甚麼"),
                    ("/articles/us/mainland-asset-omitted-from-probate.html", "內地資產沒有寫進美國遺產文件怎樣處理"),
                ],
                "cta": "把銀行、分行、賬戶末幾位、申請人關係和美國法院文件列在一頁，我們先分清查詢和提取各缺甚麼。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国家属与内地存款",
                "title": "知道内地银行和账户线索，美国家属先准备什么",
                "description": "美国家属知道逝者的内地银行或账户线索时，先分清查询、简化提取、普通继承和汇款四个不同步骤。",
                "lead": "找到银行卡或短信，只代表有一条存款线索，不代表任何家人都可以登录、查账或提取。",
                "key_title": "先写清三件事",
                "keys": [
                    "银行全名、分行和产品线索",
                    "谁准备申请及与逝者的关系",
                    "美国文件由哪个州或法院签发",
                ],
                "answer_title": "先向银行要两张清单",
                "answer": [
                    "第一张是查询清单：谁可以查、可以查什么、要哪些死亡和亲属材料。第二张是提取清单：这笔存款能否使用小额简化方式，还是要走普通继承程序。查到账户、取得款项和汇往美国，是三个不同问题。",
                    "美国遗嘱中的受益人、被提名的执行人和法院正式任命的遗产代表，也不是同一个身份。把州、县、法院文件名称和目前权限写清楚，再问内地银行实际接受哪一份。",
                ],
                "sections": [
                    (
                        "先认清银行和产品，不要只看卡片外观",
                        [
                            "记下银行法定名称、开户分行线索、卡号或账号末几位、币种、最近通知日期和客服来源。银行曾改名、分行撤并或只知道手机应用名称时，把每个版本保留，不要自行猜一个新分行。",
                            "分开标记活期、定期、理财、国债、黄金积存或其他产品。银行通常按照自己的同一法人机构合计，不一定只看家属手里这张卡；申请人身份和产品是否到期或可以赎回，也会影响能否使用简化方式。",
                        ],
                    ),
                    (
                        "先问查询，再决定办理哪一种提取",
                        [
                            "向银行说明逝者姓名、证件线索、死亡地、申请人关系和目前只想核对什么。问清能否查询余额、产品种类或特定期间交易材料，以及是否必须本人到场或可以委托。余额查询和交易明细的条件及范围可能不同，不要把能够确认账户理解成可以取得完整流水。",
                            "符合现行小额简化条件时，部分近亲属或指定人士可能不必先办理完整的普通继承证明，但仍要提交死亡、关系、身份和承诺材料。超出条件、家属有争议或产品情况不同时，银行会要求另一套办理材料。",
                        ],
                    ),
                    (
                        "把内地材料和美国代表文件分成两袋",
                        [
                            "内地袋放逝者的中文姓名、旧证件、银行线索、死亡和亲属材料；美国袋放死亡记录、遗嘱、案件州和县、法院命令及现行 Letters。申请书、法院命令和正式代表文件不要统称为 probate papers。",
                            "美国法院文件通常只说明该州程序中的角色和权限，不会自动命令内地银行付款。交件前先问银行需要原件、正式副本、附加证明、翻译和姓名衔接中的哪些项目。",
                        ],
                    ),
                    (
                        "收到款项后，保留去向和结清记录",
                        [
                            "不要把逝者资金先转进某位家人的日常账户再慢慢分。确认银行会付给谁、是否一次性提取及销户、未到期产品怎样处理，并保存申请、回单、结息和账户状态。",
                            "款项在美国一端应该进入遗产账户还是由某人直接接收，要按照案件所在州、法院任命和实际受益安排确认。跨境汇款的来源证明和申报是下一步，不能用已经成功提取来替代。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/letters-testamentary-or-administration_cn.html", "先分清美国法院任命文件"),
                    ("/articles/us/us-death-certificate-for-mainland_cn.html", "美国死亡证明交到内地前先查什么"),
                    ("/articles/us/mainland-asset-omitted-from-probate_cn.html", "内地资产没有写进美国遗产文件怎样处理"),
                ],
                "cta": "把银行、分行、账户末几位、申请人关系和美国法院文件列在一页，我们先分清查询和提取各缺什么。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. families and Mainland bank deposits",
                "title": "Found a Mainland Bank Account? What a U.S. Family Should Prepare",
                "description": "A practical guide for U.S. families separating account enquiries, simplified small-balance withdrawal, ordinary inheritance and later remittance.",
                "lead": "A bank card or text message is an account clue. It is not permission for a relative to log in, inspect transactions or withdraw the money.",
                "key_title": "Write down three facts",
                "keys": [
                    "Bank's full name, branch and product clue",
                    "Applicant's relationship to the deceased",
                    "State and court that issued each U.S. record",
                ],
                "answer_title": "Ask the bank for two separate checklists",
                "answer": [
                    "One checklist should cover access to information: who may enquire, what the bank may disclose and which death and relationship records it needs. The other should cover payment: whether the account may use a simplified small-balance route or needs an ordinary inheritance file. Finding, receiving and remitting the money are separate steps.",
                    "A beneficiary under a U.S. will, a nominated executor and a court-appointed personal representative are also different roles. Record the state, county, document name and present authority before asking what the Mainland bank will accept.",
                ],
                "sections": [
                    (
                        "Identify the bank and product, not just the card",
                        [
                            "Record the bank's full name, possible branch, last digits of the card or account, currency, date of the latest notice and source of the clue. Preserve earlier names where a bank was renamed, branches merged or the family knows only the mobile-app label.",
                            "Label demand deposits, term deposits, investment products, government bonds, gold accumulation and other products separately. The bank may total holdings across the same legal institution rather than looking only at the card in the family's hand; the applicant and product status also affect the simplified route.",
                        ],
                    ),
                    (
                        "Ask about an enquiry before choosing a withdrawal route",
                        [
                            "Tell the bank the deceased's name, former identity clue, place of death, applicant's relationship and the limited information currently sought. Ask who may obtain a balance, product list or permitted transaction period, and whether attendance or an agent is required. A balance enquiry and transaction history can have different conditions and limits; confirming an account does not open the full statement history.",
                            "Where the current small-balance conditions are met, certain close relatives or designated persons may not need the full ordinary inheritance file. Death, relationship, identity and signed undertaking records are still required. A dispute, different product or account outside the conditions changes the route.",
                        ],
                    ),
                    (
                        "Keep Mainland evidence and U.S. authority papers in separate folders",
                        [
                            "The Mainland folder should hold the Chinese name, former identity record, bank clues, death and relationship evidence. The U.S. folder should identify the death record, will, state and county, court order and current Letters. A petition, order and operative Letters should not all be called probate papers.",
                            "A U.S. court record ordinarily describes authority within that state proceeding; it does not order a Mainland bank to release funds. Ask which original, certified copy, apostille, translation and name-connection records the bank needs before preparing the full set.",
                        ],
                    ),
                    (
                        "Preserve the payment and closing trail",
                        [
                            "Do not route the deceased's money through a relative's everyday account and divide it later. Confirm who the bank will pay, whether the account must be withdrawn and closed at once, and how an unmatured product will be handled. Keep the application, receipt, interest calculation and final account status.",
                            "Whether the money should enter a U.S. estate account or be received directly depends on the state case, court appointment and beneficiary arrangement. Source records and reporting for a later remittance are another step; a successful withdrawal does not answer them.",
                        ],
                    ),
                ],
                "related_title": "Continue with the U.S. topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling a Mainland estate"),
                    ("/articles/us/letters-testamentary-or-administration_en.html", "Letters Testamentary or Letters of Administration"),
                    ("/articles/us/us-death-certificate-for-mainland_en.html", "Using a U.S. death certificate for a Mainland estate"),
                    ("/articles/us/mainland-asset-omitted-from-probate_en.html", "A Mainland asset is missing from the U.S. probate papers"),
                ],
                "cta": "Put the bank, branch, last account digits, applicant's relationship and U.S. court papers on one page. We can then separate the enquiry and withdrawal requirements.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/macau/index.html": (
        "/articles/am/mortgaged-mainland-property.html",
        '<a href="/articles/am/mortgaged-mainland-property.html"><span class="v24-tag">按揭房產</span><strong>內地房產仍有按揭，先向誰查欠款和狀態</strong><p>分開核對房產登記、貸款餘額和家屬供款紀錄。</p></a>',
    ),
    "articles/macau/index_cn.html": (
        "/articles/am/mortgaged-mainland-property_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">按揭房产</span><h3>内地房产仍有按揭，先向谁查欠款和状态</h3><p>分开核对房产登记、贷款余额和家属还款记录。</p></div><a class="v25-pill-action" href="/articles/am/mortgaged-mainland-property_cn.html">阅读文章</a></article>',
    ),
    "articles/macau/index_en.html": (
        "/articles/am/mortgaged-mainland-property_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Mortgaged home</span><h3>What to check when a Mainland home still has a mortgage</h3><p>Separate the title, loan balance and payments made after death.</p></div><a class="v25-pill-action" href="/articles/am/mortgaged-mainland-property_en.html">Read Article</a></article>',
    ),
    "articles/united-states/index.html": (
        "/articles/us/known-mainland-bank-deposit.html",
        '<a href="/articles/us/known-mainland-bank-deposit.html"><span class="v24-tag">銀行存款</span><strong>知道內地銀行和賬戶線索，先準備甚麼</strong><p>先分清查詢、提取、美國代表身份和後續匯款。</p></a>',
    ),
    "articles/united-states/index_cn.html": (
        "/articles/us/known-mainland-bank-deposit_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">银行存款</span><h3>知道内地银行和账户线索，先准备什么</h3><p>先分清查询、提取、美国代表身份和后续汇款。</p></div><a class="v25-pill-action" href="/articles/us/known-mainland-bank-deposit_cn.html">阅读文章</a></article>',
    ),
    "articles/united-states/index_en.html": (
        "/articles/us/known-mainland-bank-deposit_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Bank deposit</span><h3>Found a Mainland bank account? What to prepare</h3><p>Separate enquiries, withdrawal, U.S. authority and later remittance.</p></div><a class="v25-pill-action" href="/articles/us/known-mainland-bank-deposit_en.html">Read Article</a></article>',
    ),
}


def write_articles() -> None:
    for article in ARTICLES:
        target_dir = ROOT / article["directory"]
        for lang in ("tc", "cn", "en"):
            target = target_dir / f"{article['slug']}{LANG_SUFFIX[lang]}.html"
            target.write_text(render_article(article, lang), encoding="utf-8")


def update_hubs() -> None:
    for relative_path, (href, card) in HUB_UPDATES.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        traditional = relative_path.endswith("index.html")
        marker = '<details class="v24-article-more"' if traditional else '<details class="v25-article-more"'
        if marker not in text:
            raise RuntimeError(f"Hub insertion marker missing: {relative_path}")
        href_at = text.find(href)
        if href_at < 0:
            text = text.replace(marker, card + marker, 1)
        else:
            if traditional:
                start = text.rfind('<a href="', 0, href_at)
                end = text.find("</a>", href_at) + len("</a>")
            else:
                start = text.rfind('<article class="v25-pillar-card">', 0, href_at)
                end = text.find("</article>", href_at) + len("</article>")
            if start < 0 or end <= href_at:
                raise RuntimeError(f"Existing hub card not found: {relative_path} {href}")
            text = text[:start] + card + text[end:]
        path.write_text(text, encoding="utf-8")


def update_lastmod(text: str, url: str) -> str:
    loc = f"<loc>{url}</loc>"
    start = text.find(loc)
    if start < 0:
        return text
    end = text.find("</url>", start)
    block = text[start:end]
    if "<lastmod>" not in block:
        return text
    old_date = block.split("<lastmod>", 1)[1].split("</lastmod>", 1)[0]
    return text[:start] + block.replace(
        f"<lastmod>{old_date}</lastmod>", f"<lastmod>{TODAY}</lastmod>"
    ) + text[end:]


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    blocks = []
    for article in ARTICLES:
        for lang in ("tc", "cn", "en"):
            url = SITE + article_path(article, lang)
            if f"<loc>{url}</loc>" in text:
                text = update_lastmod(text, url)
                continue
            priority = "0.6" if lang == "tc" else "0.55"
            blocks.append(
                "  <url>\n"
                f"    <loc>{url}</loc>\n"
                f"    <lastmod>{TODAY}</lastmod>\n"
                "    <changefreq>monthly</changefreq>\n"
                f"    <priority>{priority}</priority>\n"
                "  </url>"
            )
    if blocks:
        text = text.replace("</urlset>", "\n".join(blocks) + "\n</urlset>")
    for base in ("/articles/macau/", "/articles/united-states/"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, SITE + base + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
