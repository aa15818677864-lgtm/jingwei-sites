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
        "slug": "digital-payment-clues",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與數碼賬戶線索",
                "title": "只找到手機和付款紀錄，新加坡家屬怎樣整理內地賬戶線索",
                "description": "新加坡家屬只找到手機、短訊、電郵或付款紀錄時，先保存原始資料，再把銀行、支付平台和交易線索整理成可查清單。",
                "lead": "手機可以幫你找到線索，但不是讓家屬繼續使用逝者賬戶的通行證。",
                "key_title": "先保住三類資料",
                "keys": [
                    "原手機、SIM 卡和取得資料的經過",
                    "銀行短訊、電郵、月結單和付款回單",
                    "機構名稱、賬號尾數和交易日期",
                ],
                "answer_title": "先把手機內容變成一張可核對的線索表",
                "answer": [
                    "不要只截一張餘額畫面。每條線索要連同應用程式或寄件人、日期、賬號尾數、交易對手、幣種和原始位置一起記下。手機通知只能說明可能存在某個賬戶或交易，正式餘額和權利人仍要由相關機構確認。",
                    "不要猜密碼、使用逝者的人臉或驗證碼登入，也不要在整理前重設手機、刪除應用程式或清理訊息。先保留原狀，再決定由誰持正式遺產身份向銀行或平台查詢。",
                ],
                "sections": [
                    (
                        "一、先記錄手機從哪裏來和目前狀態",
                        [
                            "寫下手機型號、電話號碼、SIM 卡、發現日期、保管人和當時是否已解鎖。拍下機身和目前畫面，記錄誰曾經接觸或複製資料。不要為了找賬戶而恢復出廠設定、更新系統或大量試密碼。",
                            "持有手機不等於有權查看全部內容。確認保管和查看依據後，如果畫面本來已打開，也只整理與資產線索直接相關的通知、已保存文件和可見紀錄。遇到私隱、工作資料或其他家人賬戶時停下來，不要把整部手機內容轉發到家庭群組。",
                        ],
                    ),
                    (
                        "二、按來源找線索，不按應用程式圖標猜",
                        [
                            "先看銀行短訊寄件人、電郵寄件網域、月結單 PDF、付款回單、扣款通知和手機相簿中的卡片照片。支付平台、網購平台和數碼錢包可能只顯示付款渠道，未必就是資金真正存放的銀行。",
                            "每找到一條便記下原始位置，例如哪一封電郵、哪一條短訊或哪一個檔案夾。保留完整畫面和前後內容，不要只裁走一個金額；日後銀行需要的是可核對身份和賬戶的資料，而不是孤立數字。",
                        ],
                    ),
                    (
                        "三、用九欄表把零散紀錄放回同一頁",
                        [
                            "九欄分別寫機構名稱、產品或平台、賬號尾數、幣種、最近日期、交易對手、金額、資料來源和核實狀態。核實狀態只用三種：銀行已確認、正式文件，或尚待核實的手機線索。",
                            "同一個賬號尾數在不同畫面出現時先合併，不要重複當成多個賬戶；同一品牌下的銀行、理財和代銷產品則可能要分開問。把逝者去世後仍發生的扣款或轉賬另列一組。",
                        ],
                    ),
                    (
                        "四、最後才把線索交給銀行或平台確認",
                        [
                            "先確認新加坡方面誰可代表遺產、手上只是申請文件，還是已有法院最後簽發的代表文件，再向每間機構問受理分行、申請人、死亡和親屬資料、中文翻譯、委託方式，以及可提供哪一段交易紀錄。",
                            "部分內地小額存款安排容許合資格申請人在特定條件下取得有限期間的交易明細，但跨境身份、產品和文件要求仍要逐戶確認。手機線索的用途是幫銀行找到賬戶，不是繞過銀行審核。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/known-mainland-bank-account.html", "知道內地銀行和賬戶時先準備甚麼"),
                    ("/articles/singapore/unknown-mainland-bank-accounts.html", "不知道存款在哪家銀行怎樣找線索"),
                    ("/articles/singapore/joint-mainland-bank-account.html", "內地聯名賬戶有人去世先查甚麼"),
                ],
                "cta": "把手機來源、銀行或平台名稱、賬號尾數、最近日期和新加坡遺產文件列在一頁，我們先分出可直接查和仍要補資料的線索。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与数字账户线索",
                "title": "只找到手机和付款记录，新加坡家属怎样整理内地账户线索",
                "description": "新加坡家属只找到手机、短信、邮件或付款记录时，先保存原始资料，再把银行、支付平台和交易线索整理成可查清单。",
                "lead": "手机可以帮助你找到线索，但不是让家属继续使用逝者账户的通行证。",
                "key_title": "先保住三类资料",
                "keys": [
                    "原手机、SIM 卡和取得资料的经过",
                    "银行短信、邮件、账单和付款回单",
                    "机构名称、账号尾数和交易日期",
                ],
                "answer_title": "先把手机内容变成一张可核对的线索表",
                "answer": [
                    "不要只截一张余额画面。每条线索要连同应用程序或发件人、日期、账号尾数、交易对手、币种和原始位置一起记下。手机通知只能说明可能存在某个账户或交易，正式余额和权利人仍要由相关机构确认。",
                    "不要猜密码、使用逝者的人脸或验证码登录，也不要在整理前重置手机、删除应用程序或清理信息。先保留原状，再决定由谁持正式遗产身份向银行或平台查询。",
                ],
                "sections": [
                    (
                        "一、先记录手机从哪里来和目前状态",
                        [
                            "写下手机型号、电话号码、SIM 卡、发现日期、保管人和当时是否已经解锁。拍下机身和目前画面，记录谁曾经接触或复制资料。不要为了找账户而恢复出厂设置、更新系统或大量尝试密码。",
                            "持有手机不等于有权查看全部内容。确认保管和查看依据后，如果画面原本已经打开，也只整理与资产线索直接相关的通知、已经保存的文件和可见记录。遇到隐私、工作资料或其他家人账户时停下来，不要把整部手机内容转发到家庭群组。",
                        ],
                    ),
                    (
                        "二、按来源找线索，不按应用程序图标猜",
                        [
                            "先看银行短信发件人、邮件发件域名、账单 PDF、付款回单、扣款通知和手机相册中的卡片照片。支付平台、网购平台和数字钱包可能只显示付款渠道，未必就是资金真正存放的银行。",
                            "每找到一条便记下原始位置，例如哪一封邮件、哪一条短信或哪一个文件夹。保留完整画面和前后内容，不要只裁出一个金额；以后银行需要的是可核对身份和账户的资料，而不是孤立数字。",
                        ],
                    ),
                    (
                        "三、用九栏表把零散记录放回同一页",
                        [
                            "九栏分别写机构名称、产品或平台、账号尾数、币种、最近日期、交易对手、金额、资料来源和核实状态。核实状态只用三种：银行已经确认、正式文件，或尚待核实的手机线索。",
                            "同一个账号尾数在不同画面出现时先合并，不要重复当成多个账户；同一品牌下的银行、理财和代销产品则可能要分开询问。把逝者去世后仍发生的扣款或转账另列一组。",
                        ],
                    ),
                    (
                        "四、最后才把线索交给银行或平台确认",
                        [
                            "先确认新加坡方面谁可以代表遗产、手上只是申请文件，还是已有法院最后签发的代表文件，再向每家机构询问受理分行、申请人、死亡和亲属资料、中文翻译、委托方式，以及可以提供哪一段交易记录。",
                            "部分内地小额存款安排允许符合条件的申请人在特定条件下取得有限期间的交易明细，但跨境身份、产品和文件要求仍要逐户确认。手机线索的用途是帮助银行找到账户，不是绕过银行审核。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/known-mainland-bank-account_cn.html", "知道内地银行和账户时先准备什么"),
                    ("/articles/singapore/unknown-mainland-bank-accounts_cn.html", "不知道存款在哪家银行怎样找线索"),
                    ("/articles/singapore/joint-mainland-bank-account_cn.html", "内地联名账户有人去世先查什么"),
                ],
                "cta": "把手机来源、银行或平台名称、账号尾数、最近日期和新加坡遗产文件列在一页，我们先分出可直接查询和仍要补资料的线索。",
            },
            "en": {
                "lang": "en",
                "locale": "en_SG",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore families and digital account clues",
                "title": "Only a Phone and Payment Records Remain: Build a Mainland Account Clue List",
                "description": "A practical guide for Singapore families preserving phone, message, email and payment clues before asking Mainland banks or platforms to confirm an account.",
                "lead": "A phone may reveal where to look. It is not permission to keep using the deceased person's accounts.",
                "key_title": "Preserve three sets of records",
                "keys": [
                    "The original phone, SIM and custody history",
                    "Bank messages, emails, statements and receipts",
                    "Institution, last account digits and transaction date",
                ],
                "answer_title": "Turn the phone into a verifiable clue sheet",
                "answer": [
                    "Do not keep only one balance screenshot. Record the app or sender, date, last account digits, counterparty, currency and original location for each clue. A notification may point to an account or transaction; only the institution can confirm the current balance and account holder.",
                    "Do not guess passwords, use the deceased person's face scan or enter verification codes. Do not reset the phone, delete apps or clear messages before the material is organised. Preserve the source first, then identify who can approach the institution for the estate.",
                ],
                "sections": [
                    (
                        "1. Record where the phone came from and its current state",
                        [
                            "Write down the phone model, number, SIM, discovery date, custodian and whether it was already unlocked. Photograph the device and visible screen, and record who handled or copied material. Do not factory-reset it, update the system or repeatedly try passwords to look for accounts.",
                            "Physical possession of the phone is not authority to inspect everything on it. After confirming the basis for custody and review, limit any already-open screen to notifications, saved documents and visible records directly relevant to asset clues. Stop when private work material or another person's account appears.",
                        ],
                    ),
                    (
                        "2. Follow the source, not the app icon",
                        [
                            "Check bank-message senders, email domains, statement PDFs, payment receipts, debit notices and card photographs. A payment app, shopping platform or digital wallet may show only the payment channel, not the bank where funds are actually held.",
                            "For every clue, record its original location: the email, message or folder. Keep the full screen and surrounding context instead of cropping out one amount. A bank needs information that can be matched to a person and account, not an isolated number.",
                        ],
                    ),
                    (
                        "3. Organise the clues in one nine-column table",
                        [
                            "Use columns for institution, product or platform, last account digits, currency, latest date, counterparty, amount, source and verification status. Keep the status simple: bank-confirmed, formal document or unverified phone clue.",
                            "Merge repeated appearances of the same last account digits instead of counting them as separate accounts. Deposits, investments and third-party products under one brand may still require different enquiries. List debits or transfers made after the death separately.",
                        ],
                    ),
                    (
                        "4. Ask the institution to confirm the clue",
                        [
                            "First identify who represents the Singapore estate and whether the family has only an application or the final court-issued grant. Ask each institution which branch handles the case, who may apply, which death and relationship records are needed, whether Chinese translation or authority papers are required, and what transaction period can be provided.",
                            "Some Mainland small-deposit arrangements allow an eligible applicant to request a limited transaction period in specific circumstances. Cross-border identity, product and document requirements still need an account-by-account answer. A phone clue helps the bank find an account; it does not bypass review.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling a Mainland estate"),
                    ("/articles/singapore/known-mainland-bank-account_en.html", "What to prepare when the Mainland bank is known"),
                    ("/articles/singapore/unknown-mainland-bank-accounts_en.html", "How to look for an unknown Mainland account"),
                    ("/articles/singapore/joint-mainland-bank-account_en.html", "What to check with a joint Mainland bank account"),
                ],
                "cta": "Put the phone source, institution, last account digits, latest date and Singapore estate papers on one page. We can separate actionable clues from missing information.",
            },
        },
    },
    {
        "slug": "mainland-company-shares",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國家屬與內地公司股權",
                "title": "親人在內地公司持股，美國家屬先查股權還是先辦遺產程序",
                "description": "美國家屬處理逝者持有的內地公司股權時，並行核對公司、股權和公司章程，同時確認美國遺產代表身份。",
                "lead": "兩條線要同時走：先查逝者真正持有甚麼，再確認誰有權代表美國遺產。",
                "key_title": "先分開三個角色",
                "keys": [
                    "股東：持有多少股權和有何限制",
                    "遺產代表：誰可管理逝者權益",
                    "公司職務：董事、經理或法定代表人",
                ],
                "answer_title": "繼承股權不等於立即接管公司",
                "answer": [
                    "股權可能進入遺產，但能否承接股東資格、如何登記和公司是否有特別安排，要看公司類型、章程、股東名冊和現有爭議。逝者同時擔任董事、經理或法定代表人時，這些職務也不能和股權混成一件事。",
                    "美國法院發出的遺產代表文件可以說明誰管理遺產，卻不會自動把內地公司登記改到繼承人名下。家屬應一邊整理美國遺產文件，一邊向公司所在地核對股權和公司程序。",
                ],
                "sections": [
                    (
                        "一、先把公司和股權查準",
                        [
                            "記下公司完整名稱、統一代碼、登記城市、公司類型、目前狀態，以及公開資料中的股東姓名和出資情況。再核對逝者姓名、舊證件或英文拼法是否能與登記資料對上。",
                            "公開系統是起點，不一定完整反映股東名冊、實際出資、代持、質押、凍結或公司內部爭議。認繳金額不等於已實繳金額，也不能直接當成股權價值。把公開頁面保存日期和來源，再向公司、其他股東或現有文件核對。",
                        ],
                    ),
                    (
                        "二、找公司章程和股東原始文件",
                        [
                            "優先找公司章程、股東名冊、出資證明、股東協議、歷次決議、分紅紀錄和股權質押資料。公司章程可能對股東資格承接另有安排，不能只憑公開持股比例決定下一步。",
                            "同時分開公司欠逝者的借款、尚未支付的分紅、逝者欠公司的款項和真正股權價值。公司名下的銀行存款、房產和設備屬於公司，不等於逝者可按持股比例直接拿走。",
                        ],
                    ),
                    (
                        "三、美國遺產清單只列逝者的權益",
                        [
                            "在美國遺產程序中，先記逝者持有的股權或其他公司權益、持有方式、估計價值和相關債務，不要把整間內地公司的資產總額直接寫成逝者個人遺產。估值不清時先標記待核對。",
                            "確認現有的是遺囑執行人提名、法院命令，還是已簽發的正式代表文件。美國代表身份、受益人權利和內地股東登記可能由不同文件回答，不能只交一份 probate 文件便假設兩地都已完成。",
                        ],
                    ),
                    (
                        "四、通知公司，但不要先拿公章或操作賬戶",
                        [
                            "已有正式代表文件時，由該代表向公司發出書面通知；仍在申請時，不要冒充代表，可先詢問通知方式。說明死亡和現有文件，請公司保留股東資料，並列出章程、股東名冊、未發分紅和待決議事項。",
                            "在股權、代表身份和公司程序未核對前，不要私自取走公章、網銀工具、賬冊或以逝者職務簽文件。若其他股東反對、公司失聯、股權被轉移或公司正在清算，應把證據和時間線交給所在地專業人員另行處理。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/letters-testamentary-or-administration.html", "美國遺產代表文件怎樣分"),
                    ("/articles/us/mainland-asset-omitted-from-probate.html", "內地資產沒有寫進美國遺產文件怎樣辦"),
                    ("/articles/us/missing-mainland-title.html", "找不到內地資產文件時怎樣補線索"),
                ],
                "cta": "把公司名稱、持股比例、章程、分紅、公司職務和美國遺產文件列在一頁，我們先分清股權、債權和公司管理問題。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国家属与内地公司股权",
                "title": "亲人在内地公司持股，美国家属先查股权还是先办遗产程序",
                "description": "美国家属处理逝者持有的内地公司股权时，并行核对公司、股权和公司章程，同时确认美国遗产代表身份。",
                "lead": "两条线要同时走：先查逝者真正持有什么，再确认谁有权代表美国遗产。",
                "key_title": "先分开三个角色",
                "keys": [
                    "股东：持有多少股权和有什么限制",
                    "遗产代表：谁可以管理逝者权益",
                    "公司职务：董事、经理或法定代表人",
                ],
                "answer_title": "继承股权不等于立即接管公司",
                "answer": [
                    "股权可能进入遗产，但能否承接股东资格、怎样登记和公司是否有特别安排，要看公司类型、章程、股东名册和现有争议。逝者同时担任董事、经理或法定代表人时，这些职务也不能和股权混成一件事。",
                    "美国法院出具的遗产代表文件可以说明谁管理遗产，却不会自动把内地公司登记改到继承人名下。家属应一边整理美国遗产文件，一边向公司所在地核对股权和公司程序。",
                ],
                "sections": [
                    (
                        "一、先把公司和股权查准",
                        [
                            "记下公司完整名称、统一代码、登记城市、公司类型、目前状态，以及公开资料中的股东姓名和出资情况。再核对逝者姓名、旧证件或英文拼法是否能与登记资料对应。",
                            "公开系统是起点，不一定完整反映股东名册、实际出资、代持、质押、冻结或公司内部争议。认缴金额不等于已经实缴的金额，也不能直接当成股权价值。把公开页面保存日期和来源，再向公司、其他股东或现有文件核对。",
                        ],
                    ),
                    (
                        "二、找公司章程和股东原始文件",
                        [
                            "优先找公司章程、股东名册、出资证明、股东协议、历次决议、分红记录和股权质押资料。公司章程可能对股东资格承接另有安排，不能只凭公开持股比例决定下一步。",
                            "同时分开公司欠逝者的借款、尚未支付的分红、逝者欠公司的款项和真正股权价值。公司名下的银行存款、房产和设备属于公司，不等于逝者可以按持股比例直接拿走。",
                        ],
                    ),
                    (
                        "三、美国遗产清单只列逝者的权益",
                        [
                            "在美国遗产程序中，先记录逝者持有的股权或其他公司权益、持有方式、估计价值和相关债务，不要把整家内地公司的资产总额直接写成逝者个人遗产。估值不清时先标记待核对。",
                            "确认现有的是遗嘱执行人提名、法院命令，还是已经签发的正式代表文件。美国代表身份、受益人权利和内地股东登记可能由不同文件回答，不能只交一份 probate 文件便假设两地都已完成。",
                        ],
                    ),
                    (
                        "四、通知公司，但不要先拿公章或操作账户",
                        [
                            "已经有正式代表文件时，由该代表向公司发出书面通知；仍在申请时，不要冒充代表，可以先询问通知方式。说明死亡和现有文件，请公司保留股东资料，并列出章程、股东名册、未发分红和待决议事项。",
                            "在股权、代表身份和公司程序没有核对前，不要私自取走公章、网银工具、账簿或以逝者职务签署文件。如果其他股东反对、公司失联、股权被转移或公司正在清算，应把证据和时间线交给所在地专业人员另行处理。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/letters-testamentary-or-administration_cn.html", "美国遗产代表文件怎样区分"),
                    ("/articles/us/mainland-asset-omitted-from-probate_cn.html", "内地资产没有写进美国遗产文件怎么办"),
                    ("/articles/us/missing-mainland-title_cn.html", "找不到内地资产文件时怎样补线索"),
                ],
                "cta": "把公司名称、持股比例、章程、分红、公司职务和美国遗产文件列在一页，我们先分清股权、债权和公司管理问题。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. families and shares in a Mainland company",
                "title": "The Deceased Owned Shares in a Mainland Company: What a U.S. Family Should Check",
                "description": "A practical guide for U.S. families checking a deceased person's interest in a Mainland company while establishing estate authority in the United States.",
                "lead": "Do both at the same time: confirm what the deceased actually owned, and identify who can represent the U.S. estate.",
                "key_title": "Separate three roles",
                "keys": [
                    "Shareholder: the interest and any restriction",
                    "Estate representative: authority over the deceased's interest",
                    "Company office: director, manager or legal representative",
                ],
                "answer_title": "Inheriting shares does not mean taking over the company",
                "answer": [
                    "A company interest may be an estate asset, but succession to shareholder status and the registration path depend on the entity type, articles, shareholder register and any existing dispute. A director, manager or legal-representative role must be examined separately from ownership.",
                    "A U.S. court document may identify the personal representative. It does not automatically change a Mainland company record. Build the U.S. estate-authority file while checking the shares and company process where the company is registered.",
                ],
                "sections": [
                    (
                        "1. Confirm the company and the interest",
                        [
                            "Record the company's full registered name, business code, city, entity type and current status. Note the shareholder name and contribution shown in public information, then check whether the deceased's Chinese name, former identity document or English spelling matches that record.",
                            "Public information is a starting point. It may not fully show the shareholder register, paid contributions, nominee arrangements, pledges, freezes or internal disputes. A subscribed amount is not proof of payment or the value of the interest. Save the page with its date and source, then compare it with company and family records.",
                        ],
                    ),
                    (
                        "2. Find the governing documents and shareholder records",
                        [
                            "Look for the articles of association, shareholder register, contribution certificate, shareholder agreement, resolutions, dividend records and any share pledge. These governing documents may contain a specific arrangement for succession to shareholder status, so a public percentage alone is not enough.",
                            "Separate loans owed by the company to the deceased, unpaid dividends, money the deceased owed the company and the value of the shares. Cash, real estate and equipment held by the company belong to the company; the family cannot take a percentage of each asset directly.",
                        ],
                    ),
                    (
                        "3. List only the deceased's interest in the U.S. estate",
                        [
                            "Record the shares or other company interest, how it was held, an estimated value and related liabilities. Do not enter the Mainland company's total asset value as the deceased person's property. Mark the value as pending when the records are incomplete.",
                            "Identify whether the family has only an executor nomination, a court order or the issued document establishing the personal representative. U.S. authority, beneficiary rights and Mainland shareholder registration may be answered by different papers.",
                        ],
                    ),
                    (
                        "4. Notify the company without taking control",
                        [
                            "If the final representative document has issued, the representative should notify the company in writing. While the U.S. application is pending, do not claim authority that has not been granted; first ask how the company will accept notice. Identify the death and current papers, and ask the company to preserve shareholder records.",
                            "Before ownership and authority are confirmed, do not take the company seal, online-banking device or books, and do not sign in the deceased's former company role. If other shareholders object, the company is unreachable, the interest moved or the company is in liquidation, preserve the timeline for local review.",
                        ],
                    ),
                ],
                "related_title": "Continue with the U.S. topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling a Mainland estate"),
                    ("/articles/us/letters-testamentary-or-administration_en.html", "Letters Testamentary and Letters of Administration"),
                    ("/articles/us/mainland-asset-omitted-from-probate_en.html", "A Mainland asset is missing from the U.S. probate papers"),
                    ("/articles/us/missing-mainland-title_en.html", "Rebuilding clues when a Mainland asset document is missing"),
                ],
                "cta": "Put the company name, ownership percentage, articles, dividends, company offices and U.S. estate papers on one page. We can separate shares, debts and management issues.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/singapore/index.html": (
        "/articles/singapore/digital-payment-clues.html",
        '<a href="/articles/singapore/digital-payment-clues.html"><span class="v24-tag">數碼線索</span><strong>只找到手機和付款紀錄，怎樣找內地賬戶</strong><p>保留原始資料，再整理成銀行可核對的清單。</p></a>',
    ),
    "articles/singapore/index_cn.html": (
        "/articles/singapore/digital-payment-clues_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">数字线索</span><h3>只找到手机和付款记录，怎样找内地账户</h3><p>保留原始资料，再整理成银行可核对的清单。</p></div><a class="v25-pill-action" href="/articles/singapore/digital-payment-clues_cn.html">阅读文章</a></article>',
    ),
    "articles/singapore/index_en.html": (
        "/articles/singapore/digital-payment-clues_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Digital clues</span><h3>Only a phone and payment records remain</h3><p>Preserve the source, then build a bank-ready clue sheet.</p></div><a class="v25-pill-action" href="/articles/singapore/digital-payment-clues_en.html">Read Article</a></article>',
    ),
    "articles/united-states/index.html": (
        "/articles/us/mainland-company-shares.html",
        '<a href="/articles/us/mainland-company-shares.html"><span class="v24-tag">公司股權</span><strong>親人在內地公司持股，先查甚麼</strong><p>分開股權、遺產代表和公司職務。</p></a>',
    ),
    "articles/united-states/index_cn.html": (
        "/articles/us/mainland-company-shares_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">公司股权</span><h3>亲人在内地公司持股，美国家属先查什么</h3><p>分开股权、遗产代表和公司职务。</p></div><a class="v25-pill-action" href="/articles/us/mainland-company-shares_cn.html">阅读文章</a></article>',
    ),
    "articles/united-states/index_en.html": (
        "/articles/us/mainland-company-shares_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Company shares</span><h3>The deceased owned shares in a Mainland company</h3><p>Separate ownership, estate authority and company office.</p></div><a class="v25-pill-action" href="/articles/us/mainland-company-shares_en.html">Read Article</a></article>',
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
    for base in ("/articles/singapore/", "/articles/united-states/"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, SITE + base + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
