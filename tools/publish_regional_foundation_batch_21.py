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
        "slug": "joint-mainland-bank-account",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與內地聯名賬戶",
                "title": "內地聯名賬戶有人去世，新加坡家屬先別只看持卡人",
                "description": "新加坡家屬處理內地聯名銀行賬戶時，先核對開戶約定、操作方式、資金來源和銀行要求，不憑賬戶姓名直接判斷餘額歸屬。",
                "lead": "賬戶上有兩個姓名，只能先說明兩人與銀行都有關係，不能直接回答每一筆錢屬於誰。",
                "key_title": "先找齊三組資料",
                "keys": [
                    "開戶文件和賬戶操作規則",
                    "主要入賬來源與大額轉賬紀錄",
                    "誰代表遺產，以及銀行要甚麼",
                ],
                "answer_title": "先分清操作權、資金來源和遺產份額",
                "answer": [
                    "聯名賬戶可以約定單獨操作，也可以要求共同簽署；有人能提款，不代表賬內全部款項都歸他。先看開戶約定，再按流水追查薪金、租金、售房款或家庭轉賬從哪裏來，才有條件討論哪些款項可能進入遺產。",
                    "新加坡法院發出的遺產代表文件可以說明誰管理遺產，但不會自動替內地銀行決定賬戶餘額。家屬仍要向開戶銀行確認查詢、限制操作和提取分別需要甚麼文件。",
                ],
                "sections": [
                    (
                        "一、先做一張聯名賬戶事實卡",
                        [
                            "先按開戶文件確認銀行對這個產品的正式名稱；不同銀行可能使用聯名、共管或其他安排。再記下銀行完整名稱、開戶城市、賬號尾數、全部賬戶人、哪一人持卡，以及平日是任何一人可以操作，還是需要兩人共同確認。另列出活期、定期、理財和代銷產品。",
                            "找開戶申請、賬戶條款、簽名樣式、近年流水和銀行通知。只有手機截圖或家人記憶時，先標成線索，不要寫成銀行已確認的事實，也不要把完整賬號、密碼或驗證碼放進家庭群組。",
                        ],
                    ),
                    (
                        "二、逐筆看錢從哪裏來，不只看賬戶姓名",
                        [
                            "把較大的入賬按日期、付款人和用途分類，例如逝者薪金、房屋租金、資產出售款、另一名賬戶人的收入或家庭共同開支。賬戶名稱是一條線索，資金來源和雙方原有約定才是判斷的重要材料。",
                            "逝者去世後的提款、轉賬和自動扣款要另列一欄，保存銀行回單和用途說明。不要使用逝者的密碼、人臉或驗證碼登入，也不要讓其中一人先把錢全部取走，再口頭承諾日後分配。",
                        ],
                    ),
                    (
                        "三、新加坡文件和內地銀行要分開核對",
                        [
                            "先看手上的文件走到哪一步：只是申請、已有法院命令，還是已拿到能證明誰代表遺產的最終文件。即使代表身份已確認，銀行仍可能要求死亡、親屬、遺囑、新舊證件姓名對照、中文翻譯和委託材料。",
                            "新加坡有些聯名賬戶會按開戶時的特別約定處理，但這不能直接套用到內地賬戶。把逝者和申請人的居留、國籍及證件情況完整告知開戶銀行，請對方按本賬戶列出清單。",
                        ],
                    ),
                    (
                        "四、第一次聯絡銀行問清六件事",
                        [
                            "一次問清受理分行、誰可先查資料、賬戶目前能否繼續操作、查詢和提取是否由不同人申請、境外文件需要甚麼版本，以及能否由代理人遞交。把回覆日期、部門和文件缺口逐項記下。",
                            "如果生存賬戶人、遺產代表和其他繼承人說法不同，先保留流水和書面回覆，再處理歸屬或分配。銀行的操作答案只解決銀行怎樣辦，不等於已經替家人判定每一筆錢屬於誰。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/known-mainland-bank-account.html", "知道內地銀行和賬戶時先準備甚麼"),
                    ("/articles/singapore/unknown-mainland-bank-accounts.html", "不知道存款在哪家銀行怎樣找線索"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "遺囑認證和遺產管理文件有甚麼不同"),
                ],
                "cta": "把銀行、賬戶人、操作方式、主要入賬和新加坡遺產文件列在一頁，我們先分開查詢、操作和歸屬問題。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与内地联名账户",
                "title": "内地联名账户有人去世，新加坡家属先别只看持卡人",
                "description": "新加坡家属处理内地联名银行账户时，先核对开户约定、操作方式、资金来源和银行要求，不凭账户姓名直接判断余额归属。",
                "lead": "账户上有两个姓名，只能先说明两人与银行都有关系，不能直接回答每一笔钱属于谁。",
                "key_title": "先找齐三组资料",
                "keys": [
                    "开户文件和账户操作规则",
                    "主要入账来源与大额转账记录",
                    "谁代表遗产，以及银行要什么",
                ],
                "answer_title": "先分清操作权、资金来源和遗产份额",
                "answer": [
                    "联名账户可以约定单独操作，也可以要求共同签署；有人能取款，不代表账户中的全部款项都归他。先看开户约定，再按流水追查工资、租金、售房款或家庭转账从哪里来，才有条件讨论哪些款项可能进入遗产。",
                    "新加坡法院出具的遗产代表文件可以说明谁管理遗产，但不会自动替内地银行决定账户余额。家属仍要向开户银行确认查询、限制操作和提取分别需要什么文件。",
                ],
                "sections": [
                    (
                        "一、先做一张联名账户事实卡",
                        [
                            "先按开户文件确认银行对这个产品的正式名称；不同银行可能使用联名、共管或其他安排。再记下银行完整名称、开户城市、账号尾数、全部账户人、哪一人持卡，以及平时是任何一人可以操作，还是需要两人共同确认。另列出活期、定期、理财和代销产品。",
                            "找开户申请、账户条款、签名样式、近年流水和银行通知。只有手机截图或家人记忆时，先标成线索，不要写成银行已确认的事实，也不要把完整账号、密码或验证码放进家庭群组。",
                        ],
                    ),
                    (
                        "二、逐笔看钱从哪里来，不只看账户姓名",
                        [
                            "把较大的入账按日期、付款人和用途分类，例如逝者工资、房屋租金、资产出售款、另一名账户人的收入或家庭共同开支。账户名称是一条线索，资金来源和双方原有约定才是判断的重要材料。",
                            "逝者去世后的取款、转账和自动扣款要另列一栏，保存银行回单和用途说明。不要使用逝者的密码、人脸或验证码登录，也不要让其中一人先把钱全部取走，再口头承诺以后分配。",
                        ],
                    ),
                    (
                        "三、新加坡文件和内地银行要分开核对",
                        [
                            "先看手上的文件走到哪一步：只是申请、已有法院命令，还是已经拿到能证明谁代表遗产的最终文件。即使代表身份已经确认，银行仍可能要求死亡、亲属、遗嘱、新旧证件姓名对照、中文翻译和委托材料。",
                            "新加坡有些联名账户会按开户时的特别约定处理，但这不能直接套用到内地账户。把逝者和申请人的居留、国籍及证件情况完整告知开户银行，请对方按本账户列出清单。",
                        ],
                    ),
                    (
                        "四、第一次联系银行问清六件事",
                        [
                            "一次问清受理分行、谁可先查资料、账户目前能否继续操作、查询和提取是否由不同人申请、境外文件需要什么版本，以及能否由代理人递交。把回复日期、部门和文件缺口逐项记下。",
                            "如果生存账户人、遗产代表和其他继承人说法不同，先保留流水和书面回复，再处理归属或分配。银行的操作答案只解决银行怎样办理，不等于已经替家人判定每一笔钱属于谁。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/known-mainland-bank-account_cn.html", "知道内地银行和账户时先准备什么"),
                    ("/articles/singapore/unknown-mainland-bank-accounts_cn.html", "不知道存款在哪家银行怎样找线索"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "遗嘱认证和遗产管理文件有什么不同"),
                ],
                "cta": "把银行、账户人、操作方式、主要入账和新加坡遗产文件列在一页，我们先分开查询、操作和归属问题。",
            },
            "en": {
                "lang": "en",
                "locale": "en_SG",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore families and joint Mainland accounts",
                "title": "When a Joint Mainland Bank Account Holder Dies: A Singapore Family's First Checks",
                "description": "A practical guide for Singapore families checking a joint Mainland bank account, including the account mandate, source of funds, estate authority and bank requirements.",
                "lead": "Two names on an account show a banking relationship. They do not, by themselves, identify who owns every dollar in it.",
                "key_title": "Find three sets of records",
                "keys": [
                    "Account-opening terms and signing rules",
                    "Main deposits and large transfers",
                    "Who represents the estate, and what the bank needs",
                ],
                "answer_title": "Separate account access from ownership of the money",
                "answer": [
                    "A joint account may allow either holder to act alone, or it may require both holders to approve a transaction. The ability to withdraw does not prove ownership of the entire balance. Start with the account mandate, then trace salary, rent, sale proceeds and family transfers through the statements.",
                    "A Singapore grant can identify the person authorised to administer the estate. It does not automatically tell a Mainland bank how to classify the balance. Ask the opening bank separately about enquiries, account controls and withdrawals after a death.",
                ],
                "sections": [
                    (
                        "1. Make a one-page account record",
                        [
                            "Start with the product name used in the opening papers. Different banks may describe a joint, co-managed or similar arrangement differently. Then record the bank, opening city, last account digits, every holder, who has the card and whether one holder could normally act alone. List other deposit and investment products separately.",
                            "Look for the opening form, account terms, signature instructions, recent statements and bank notices. Label a screenshot or family recollection as a clue until the bank confirms it. Never circulate a full account number, password or verification code in a family chat.",
                        ],
                    ),
                    (
                        "2. Trace the money, not only the names",
                        [
                            "Sort larger deposits by date, sender and purpose. Common examples include the deceased's salary, rent, property-sale proceeds, the other holder's income and money used for shared household expenses. The account name is one fact; the funding history and the holders' arrangement provide the context.",
                            "Put withdrawals, transfers and automatic payments made after the death in a separate list. Keep receipts and note the purpose. Do not log in with the deceased's password, face scan or verification code, and do not let one holder empty the account on a promise to divide it later.",
                        ],
                    ),
                    (
                        "3. Find out what the Mainland bank still needs from Singapore",
                        [
                            "Check how far the Singapore process has reached: an application, a court order, or the final grant naming the estate representative. Even with the representative confirmed, the bank may still ask for death, relationship, will, old-and-new identity, Chinese translation and authority documents.",
                            "Some Singapore joint accounts are dealt with under a specific survivorship instruction signed at opening. That instruction cannot simply be carried across to a Mainland account. Disclose the deceased's and applicant's residence, nationality and identity documents, then ask for a checklist for this account.",
                        ],
                    ),
                    (
                        "4. Ask six questions on the first bank contact",
                        [
                            "Ask which branch handles the case, who may receive initial information, whether the account can still be operated, whether enquiry and withdrawal have different applicants, which version of foreign documents is accepted and whether an authorised representative may submit them. Record the date, department and missing items.",
                            "If the surviving holder, estate representative and other beneficiaries disagree, preserve the statements and written bank replies before addressing ownership or distribution. The bank's operational answer explains what the bank can do; it does not decide every dispute between family members.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling a Mainland estate"),
                    ("/articles/singapore/known-mainland-bank-account_en.html", "What to prepare when the Mainland bank is known"),
                    ("/articles/singapore/unknown-mainland-bank-accounts_en.html", "How to look for an unknown Mainland account"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate and letters of administration"),
                ],
                "cta": "Put the bank, account holders, signing rules, main deposits and Singapore estate papers on one page. We can then separate enquiry, access and ownership questions.",
            },
        },
    },
    {
        "slug": "occupied-or-sold-property",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門家屬與內地房產狀態",
                "title": "內地房子被親屬佔用或疑似出售，澳門家屬先保留甚麼",
                "description": "澳門家屬發現內地遺產房被人居住或疑似出售時，先核對登記、整理佔用和交易線索，再判斷是否需要採取措施。",
                "lead": "先不要換鎖、斷水電或只靠家人對質。把登記、實際居住和疑似交易分成三條線查。",
                "key_title": "先固定三類事實",
                "keys": [
                    "現在登記在誰名下，有沒有抵押或限制",
                    "誰在住、何時入住及有何依據",
                    "出售、收款或中介聯絡線索",
                ],
                "answer_title": "有人住和房子已被賣掉是兩個不同問題",
                "answer": [
                    "親屬住在房子裏，可能涉及共同居住、租賃、照料安排、共有或繼承爭議；家屬聽到“已經賣了”，也可能只是有放盤、簽約、收款或正在辦登記。先查目前登記，再保存佔用和交易證據，才能知道真正要處理哪一層。",
                    "澳門的死亡、親屬和繼承身份文件有助說明誰可代表遺產，但不等於拿到文件便可自行入屋、趕人或阻止交易。房產所在城市接受甚麼查詢和措施，仍要按當地狀態核對。",
                ],
                "sections": [
                    (
                        "一、先畫一張房屋現況圖",
                        [
                            "寫下城市、完整地址、樓盤和房號、登記姓名，以及手上的房產證號或購房文件。另列最後一次確認房屋狀態的日期、目前居住人、入住時間、是否交租、誰保管鎖匙、誰繳管理費和水電。",
                            "保存有日期的門牌和室內照片、物業管理回覆、租金紀錄、維修單、鎖匙交接和家人對話。不要為取證私自闖入、跟蹤或公開對方身份資料；來源不明的說法標成待核實。",
                        ],
                    ),
                    (
                        "二、先查最新登記，不要只看舊房產證",
                        [
                            "繼承人通常要帶死亡、親屬、遺囑或其他繼承線索，按房產所在地要求申請查詢。重點看目前權利人、共有份額、抵押、預告、異議和其他限制，不要把家中舊證件當成今天的登記結果。",
                            "如果懷疑出售，保存放盤截圖、買賣文件照片、收款紀錄、中介姓名和聯絡日期。先問清楚只是談價、已簽文件、已付款，還是登記已經變更；這四種情況的下一步不同。",
                        ],
                    ),
                    (
                        "三、有人佔用不等於他已取得房屋",
                        [
                            "先問居住人根據甚麼入住：原業主同意、租約、照料安排、共有身份，還是只說自己也是繼承人。保留對方說法和文件，不要急着把每一種情況都叫做霸佔。",
                            "即使家屬認為對方沒有權利，也不要自行換鎖、搬走物品或切斷水電。先確認誰對房屋有現有權利、誰可代表遺產，以及是否需要協商、書面通知或司法處理。",
                        ],
                    ),
                    (
                        "四、風險明確時再選保護措施",
                        [
                            "如果登記、收款或中介資料顯示交易正在推進，把時間線、房產查詢、身份文件和原始對話交給房產所在地的專業人員核對。更正或異議登記通常要先指向登記記載錯誤等特定問題，訴訟中的保護措施也另有條件；它們都不是憑一句“怕被賣”便能啟動的通用凍結按鈕。",
                            "若只是家人長期居住而權屬尚未分清，先處理遺產範圍、代表身份和各方說法。把誰住、誰收租、誰付費和房屋有無受損記清楚，往往比先爭吵更能保住後續選擇。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門家屬處理內地房產先從哪一步開始"),
                    ("/articles/am/mortgaged-mainland-property.html", "房產仍有按揭時怎樣核對欠款和登記"),
                    ("/articles/am/estate-manager-role-boundary.html", "待分割財產管理人能做甚麼"),
                ],
                "cta": "把房屋地址、目前居住人、最新登記、疑似交易和現有澳門文件列在一頁，我們先判斷最急的是查詢、保存證據還是處理爭議。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门家属与内地房产状态",
                "title": "内地房子被亲属占用或疑似出售，澳门家属先保留什么",
                "description": "澳门家属发现内地遗产房被人居住或疑似出售时，先核对登记、整理占用和交易线索，再判断是否需要采取措施。",
                "lead": "先不要换锁、断水电或只靠家人对质。把登记、实际居住和疑似交易分成三条线查。",
                "key_title": "先固定三类事实",
                "keys": [
                    "现在登记在谁名下，有没有抵押或限制",
                    "谁在住、何时入住及有什么依据",
                    "出售、收款或中介联系线索",
                ],
                "answer_title": "有人住和房子已被卖掉是两个不同问题",
                "answer": [
                    "亲属住在房子里，可能涉及共同居住、租赁、照料安排、共有或继承争议；家属听到“已经卖了”，也可能只是有挂牌、签约、收款或正在办理登记。先查目前登记，再保存占用和交易证据，才能知道真正要处理哪一层。",
                    "澳门的死亡、亲属和继承身份文件有助于说明谁可以代表遗产，但不等于拿到文件便可以自行入屋、赶人或阻止交易。房产所在城市接受什么查询和措施，仍要按当地状态核对。",
                ],
                "sections": [
                    (
                        "一、先画一张房屋现状图",
                        [
                            "写下城市、完整地址、小区和房号、登记姓名，以及手上的房产证号或购房文件。另列最后一次确认房屋状态的日期、目前居住人、入住时间、是否交租、谁保管钥匙、谁缴物业费和水电费。",
                            "保存有日期的门牌和室内照片、物业管理回复、租金记录、维修单、钥匙交接和家人对话。不要为了取证私自闯入、跟踪或公开对方身份资料；来源不明的说法标成待核实。",
                        ],
                    ),
                    (
                        "二、先查最新登记，不要只看旧房产证",
                        [
                            "继承人通常要带死亡、亲属、遗嘱或其他继承线索，按房产所在地要求申请查询。重点看目前权利人、共有份额、抵押、预告、异议和其他限制，不要把家中旧证件当成今天的登记结果。",
                            "如果怀疑出售，保存挂牌截图、买卖文件照片、收款记录、中介姓名和联系日期。先问清楚只是谈价、已经签署文件、已经付款，还是登记已经变更；这四种情况的下一步不同。",
                        ],
                    ),
                    (
                        "三、有人占用不等于他已经取得房屋",
                        [
                            "先问居住人根据什么入住：原业主同意、租约、照料安排、共有身份，还是只说自己也是继承人。保留对方说法和文件，不要急着把每一种情况都叫作霸占。",
                            "即使家属认为对方没有权利，也不要自行换锁、搬走物品或切断水电。先确认谁对房屋有现有权利、谁可以代表遗产，以及是否需要协商、书面通知或司法处理。",
                        ],
                    ),
                    (
                        "四、风险明确时再选择保护措施",
                        [
                            "如果登记、收款或中介资料显示交易正在推进，把时间线、房产查询、身份文件和原始对话交给房产所在地的专业人员核对。更正或异议登记通常要先指向登记记载错误等特定问题，诉讼中的保护措施也另有条件；它们都不是凭一句“怕被卖”便能启动的通用冻结按钮。",
                            "如果只是家人长期居住而权属尚未分清，先处理遗产范围、代表身份和各方说法。把谁住、谁收租、谁付费和房屋有无受损记清楚，往往比先争吵更能保留后续选择。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门家属处理内地房产先从哪一步开始"),
                    ("/articles/am/mortgaged-mainland-property_cn.html", "房产仍有按揭时怎样核对欠款和登记"),
                    ("/articles/am/estate-manager-role-boundary_cn.html", "待分割财产管理人能做什么"),
                ],
                "cta": "把房屋地址、目前居住人、最新登记、疑似交易和现有澳门文件列在一页，我们先判断最急的是查询、保存证据还是处理争议。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau families and a Mainland property at risk",
                "title": "A Relative Occupies or May Have Sold the Mainland Home: What to Preserve",
                "description": "A practical guide for Macau families checking the title, occupation and possible sale of a Mainland estate property before choosing a response.",
                "lead": "Do not begin by changing the locks, cutting utilities or confronting the family. Check title, physical occupation and any sale evidence as three separate tracks.",
                "key_title": "Preserve three sets of facts",
                "keys": [
                    "Whose name is on the current record, and any mortgage or restriction",
                    "Who occupies the home and on what basis",
                    "Sale, payment or agent communications",
                ],
                "answer_title": "Occupation and a possible sale are different problems",
                "answer": [
                    "A relative may be living in the property under a family arrangement, tenancy, care arrangement, co-ownership claim or inheritance dispute. A report that the home was “sold” may mean only a listing, a signed paper, a payment or a pending registration. Check the current record before deciding what happened.",
                    "Macau death, relationship and heirship papers can help identify the family and estate representative. They do not give anyone an automatic right to enter the home, remove an occupant or stop a transaction. The available steps depend on the current records and procedures where the property is located.",
                ],
                "sections": [
                    (
                        "1. Draw a current property map",
                        [
                            "Record the city, full address, development and unit, registered name, any title-number clue and the last date the property's status was confirmed. List the current occupants, when they moved in, whether rent is paid, who holds keys and who pays management fees and utilities.",
                            "Preserve dated doorplate and interior photographs, management-office replies, rent records, repair bills, key handovers and family messages. Do not trespass, follow an occupant or publish personal information to collect evidence. Mark an unverified statement as a lead, not a fact.",
                        ],
                    ),
                    (
                        "2. Obtain the current record instead of relying on an old certificate",
                        [
                            "An heir will usually need death, relationship, will or other inheritance material to request information under the rules where the property is located. Check the current owner, shares, mortgage, advance notice, objection and other recorded restrictions. An old certificate at home is not today's search result.",
                            "If a sale is suspected, preserve listing screenshots, photographs of transaction papers, payment records, the agent's identity and contact dates. Find out whether the family only discussed a price, signed papers, received money or completed a registration. Each stage calls for a different response.",
                        ],
                    ),
                    (
                        "3. Living in the home does not prove ownership",
                        [
                            "Ask what the occupant relies on: the former owner's permission, a lease, a care arrangement, co-ownership or a claim to be an heir. Preserve the answer and any document. Do not label every unclear occupation as unlawful before checking the underlying arrangement.",
                            "Even if the family believes the occupant has no right to stay, do not change the locks, remove belongings or cut utilities. First identify the current rights, the person authorised to act for the estate and whether negotiation, a written notice or court action is appropriate.",
                        ],
                    ),
                    (
                        "4. Choose a protective step only when the risk is clear",
                        [
                            "If the title, payment or agent records show that a transaction is moving forward, give the timeline, property search, identity papers and original messages to a professional where the property is located. A correction or objection entry usually needs a specific problem in the register, and court protection has separate conditions. None is a general freeze button.",
                            "If the only confirmed fact is that a relative has lived there for years, first clarify the estate, the representative and each person's account. A clean record of occupation, rent, expenses and damage usually preserves more options than an immediate family confrontation.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Where a Macau family should start with Mainland property"),
                    ("/articles/am/mortgaged-mainland-property_en.html", "Checking the loan and title when a mortgage remains"),
                    ("/articles/am/estate-manager-role-boundary_en.html", "What an estate manager can and cannot decide"),
                ],
                "cta": "Put the address, occupants, current title result, suspected transaction and available Macau documents on one page. We can then identify whether the urgent task is a search, evidence preservation or a dispute response.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/singapore/index.html": (
        "/articles/singapore/joint-mainland-bank-account.html",
        '<a href="/articles/singapore/joint-mainland-bank-account.html"><span class="v24-tag">聯名賬戶</span><strong>內地聯名賬戶有人去世，先別只看持卡人</strong><p>分開核對操作規則、資金來源和遺產份額。</p></a>',
    ),
    "articles/singapore/index_cn.html": (
        "/articles/singapore/joint-mainland-bank-account_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">联名账户</span><h3>内地联名账户有人去世，先别只看持卡人</h3><p>分开核对操作规则、资金来源和遗产份额。</p></div><a class="v25-pill-action" href="/articles/singapore/joint-mainland-bank-account_cn.html">阅读文章</a></article>',
    ),
    "articles/singapore/index_en.html": (
        "/articles/singapore/joint-mainland-bank-account_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Joint account</span><h3>When a joint Mainland bank account holder dies</h3><p>Separate signing rules, source of funds and estate ownership.</p></div><a class="v25-pill-action" href="/articles/singapore/joint-mainland-bank-account_en.html">Read Article</a></article>',
    ),
    "articles/macau/index.html": (
        "/articles/am/occupied-or-sold-property.html",
        '<a href="/articles/am/occupied-or-sold-property.html"><span class="v24-tag">房產風險</span><strong>房子被親屬佔用或疑似出售，先保留甚麼</strong><p>先查登記，再整理佔用和交易線索。</p></a>',
    ),
    "articles/macau/index_cn.html": (
        "/articles/am/occupied-or-sold-property_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">房产风险</span><h3>房子被亲属占用或疑似出售，先保留什么</h3><p>先查登记，再整理占用和交易线索。</p></div><a class="v25-pill-action" href="/articles/am/occupied-or-sold-property_cn.html">阅读文章</a></article>',
    ),
    "articles/macau/index_en.html": (
        "/articles/am/occupied-or-sold-property_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Property risk</span><h3>A relative occupies or may have sold the home</h3><p>Check the title, occupation and transaction evidence separately.</p></div><a class="v25-pill-action" href="/articles/am/occupied-or-sold-property_en.html">Read Article</a></article>',
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
    for base in ("/articles/singapore/", "/articles/macau/"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, SITE + base + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
