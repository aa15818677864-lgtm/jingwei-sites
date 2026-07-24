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
        "slug": "estate-manager-role-boundary",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門遺產管理",
                "title": "待分割財產管理人能做甚麼，哪些事仍要繼承人決定",
                "description": "澳門家屬先分清待分割財產管理人的日常管理、資料整理和重大處分邊界，再處理內地房產或存款。",
                "lead": "家人推選一位聯絡人，不代表他已經是正式管理人，更不等於把房子、存款和分配決定都交給了他。",
                "key_title": "先分清三個角色",
                "keys": [
                    "聯絡人不等於正式管理人",
                    "管理人先保管和整理遺產",
                    "繼承人仍要決定怎樣分配",
                ],
                "answer_title": "把他看成遺產的臨時整理人",
                "answer": [
                    "家裏負責聯絡的人，不一定就是正式的待分割財產管理人。本文所說的管理人，是按實際繼承安排具有管理身份的人；他的核心工作，是在遺產正式分配前把財產保管好、資料列清楚，並處理必要的日常管理。他不會因此變成房屋或存款的所有人。",
                    "涉及最終分配、放棄權利、出售或轉名等重大決定時，仍要看全體繼承人的意見、現有授權和實際辦理程序。管理人在澳門具有某項身份，也不代表內地房產登記或銀行一定接受他單獨辦理。",
                ],
                "sections": [
                    (
                        "先做可以留下紀錄的日常工作",
                        [
                            "可以先列出房產、存款、保險、債務和重要文件，記下每項財產由誰保管、是否有到期付款，以及目前缺少甚麼資料。需要保住房屋、支付必要費用，或接收機構已明確接受管理人領取某項款項時，也應保存賬單、收據和家屬溝通紀錄。",
                            "遇到他人持有本應交回遺產的物件或文件，可以先正式要求交付。若對方拒絕，重點是保留要求、回覆和物件來源，不要用自行換鎖、取走財物等方式把整理工作變成新的爭議。",
                        ],
                    ),
                    (
                        "這些事不要由管理人一個人拍板",
                        [
                            "誰取得哪項財產、房屋是否出售、某位繼承人是否少分或不分，以及是否接受一項爭議和解，都不是普通保管工作。沒有清楚的共同決定、授權或相應程序時，管理人不應替其他繼承人作出這些選擇。",
                            "即使家人平日都由一人聯絡，也要把三件事分開：誰整理資料、誰對外簽署、誰有權作出最終決定。把三者寫在一頁分工表上，比一句“全權處理”更能避免誤會。",
                        ],
                    ),
                    (
                        "內地房產和存款要另做授權表",
                        [
                            "先逐項寫明資產所在地、接收機構、準備辦的事情和希望由誰辦理。例如查詢房產登記、領取銀行要求清單、提交文件、簽署分配安排或收取款項，所需身份和授權可能並不相同。",
                            "把澳門管理人文件交給內地接收方前，先問它能證明甚麼、還要哪些繼承人文件、是否接受受託人以及哪些決定必須本人確認。這一步能避免把一份管理身份文件誤當成所有資產的通行授權。",
                        ],
                    ),
                    (
                        "用一張六欄表交代每個行動",
                        [
                            "六欄可寫：要做的事、涉及資產、是否緊急、現有證明、需要誰同意，以及完成後要留下甚麼紀錄。日常保管和資料查詢可以先排在前面，出售、轉名、分配和和解則標成待確認。",
                            "若家人已經對賬目、財物去向或管理人是否盡責有意見，先暫停重大處分，保存清單、收支和交接資料，再處理管理人是否繼續任職。越早把賬目說清楚，越不容易把身份問題拖成家族爭議。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-heir-qualification-deed.html", "澳門繼承人資格文件能說明甚麼"),
                    ("/articles/am/macau-no-will-mainland-property.html", "沒有遺囑時先從哪一步開始"),
                    ("/articles/am/multiple-wills-across-regions.html", "家中找到多份遺囑怎樣整理"),
                ],
                "cta": "說明目前由誰保管財物、要辦哪項內地資產，以及家人已同意甚麼，我們先把管理和決定的邊界畫清楚。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门遗产管理",
                "title": "待分割财产管理人能做什么，哪些事仍要继承人决定",
                "description": "澳门家属先分清待分割财产管理人的日常管理、材料整理和重大处置边界，再处理内地房产或存款。",
                "lead": "家人推选一位联系人，不代表他已经是正式管理人，更不等于把房子、存款和分配决定都交给了他。",
                "key_title": "先分清三个角色",
                "keys": [
                    "联系人不等于正式管理人",
                    "管理人先保管和整理遗产",
                    "继承人仍要决定怎样分配",
                ],
                "answer_title": "把他看成遗产的临时整理人",
                "answer": [
                    "家里负责联系的人，不一定就是正式的待分割财产管理人。本文所说的管理人，是按照实际继承安排具有管理身份的人；他的主要工作，是在遗产正式分配前保管财产、列清材料，并处理必要的日常管理。他不会因此变成房屋或存款的所有人。",
                    "涉及最终分配、放弃权利、出售或转名等重大决定时，仍要看全体继承人的意见、现有授权和实际办理程序。管理人在澳门具有某项身份，也不代表内地房产登记或银行一定接受他单独办理。",
                ],
                "sections": [
                    (
                        "先做可以留下记录的日常工作",
                        [
                            "可以先列出房产、存款、保险、债务和重要文件，记下每项财产由谁保管、是否有到期付款，以及目前缺少什么材料。需要保住房屋、支付必要费用，或接收机构已经明确接受管理人领取某项款项时，也应保存账单、收据和家属沟通记录。",
                            "如果他人持有本应交回遗产的物件或文件，可以先正式要求交付。对方拒绝时，重点是保留要求、回复和物件来源，不要用自行换锁、取走财物等方式把整理工作变成新的争议。",
                        ],
                    ),
                    (
                        "这些事不要由管理人一个人拍板",
                        [
                            "谁取得哪项财产、房屋是否出售、某位继承人是否少分或不分，以及是否接受一项争议和解，都不是普通保管工作。没有清楚的共同决定、授权或相应程序时，管理人不应替其他继承人作出这些选择。",
                            "即使家人平时都由一人联系，也要把三件事分开：谁整理材料、谁对外签署、谁有权作出最终决定。把三者写在一页分工表上，比一句“全权处理”更能避免误会。",
                        ],
                    ),
                    (
                        "内地房产和存款要另做授权表",
                        [
                            "先逐项写明资产所在地、接收机构、准备办理的事情和希望由谁处理。例如查询房产登记、领取银行要求清单、提交文件、签署分配安排或收取款项，需要的身份和授权可能并不相同。",
                            "把澳门管理人文件交给内地接收方前，先问它能证明什么、还要哪些继承人文件、是否接受受托人以及哪些决定必须本人确认。这样可以避免把一份管理身份证明误当成所有资产的通行授权。",
                        ],
                    ),
                    (
                        "用一张六栏表交代每个行动",
                        [
                            "六栏可以写：要做的事、涉及资产、是否紧急、现有证明、需要谁同意，以及完成后要留下什么记录。日常保管和材料查询可以先排在前面，出售、转名、分配和和解则标成待确认。",
                            "如果家人已经对账目、财物去向或管理人是否尽责有意见，先暂停重大处置，保存清单、收支和交接材料，再处理管理人是否继续任职。越早把账目说清楚，越不容易把身份问题拖成家庭争议。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-heir-qualification-deed_cn.html", "澳门继承人资格文件能说明什么"),
                    ("/articles/am/macau-no-will-mainland-property_cn.html", "没有遗嘱时先从哪一步开始"),
                    ("/articles/am/multiple-wills-across-regions_cn.html", "家里找到多份遗嘱怎样整理"),
                ],
                "cta": "说明现在由谁保管财物、要办哪项内地资产，以及家人已经同意什么，我们先把管理和决定的边界画清楚。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau estate management",
                "title": "Macau Estate Manager: What They Can and Cannot Decide",
                "description": "A practical guide to the boundary between preserving a Macau estate, making family decisions and handling assets in Mainland China.",
                "lead": "Choosing one relative as the family contact does not make that person the formal estate manager or hand over every decision about the home, accounts and distribution.",
                "key_title": "Keep three roles separate",
                "keys": [
                    "A family contact is not the formal manager",
                    "The manager preserves and records the estate",
                    "The heirs still make distribution decisions",
                ],
                "answer_title": "Think of the manager as the estate's temporary organiser",
                "answer": [
                    "The relative taking phone calls is not necessarily the formal estate manager. Here, manager means a person appointed through the relevant estate arrangement. Before distribution, the manager keeps assets safe, records what exists and handles necessary routine administration. The role does not make the manager the owner of the home or the money.",
                    "Final distribution, a waiver of rights, a sale or a transfer requires a separate basis. That may involve the heirs' agreement, express authority or a formal process. A Macau appointment also does not guarantee that a Mainland property office or bank will let the manager act alone.",
                ],
                "sections": [
                    (
                        "Start with routine tasks that leave a record",
                        [
                            "List the property, accounts, insurance, debts and important papers. Record who holds each item, which payments are due and what evidence is missing. Keep bills, receipts and family messages for necessary payments, steps taken to protect a home and any sum an institution has expressly agreed to release to the manager.",
                            "If someone holds an item or paper that should be returned to the estate, make a clear written request. If they refuse, preserve the request, response and source of the item. Do not turn an information problem into a new dispute by changing locks or removing property without authority.",
                        ],
                    ),
                    (
                        "Do not let one organiser make the family's final choices",
                        [
                            "Who receives an asset, whether a home should be sold, whether an heir gives up a share and whether a dispute should be settled are not routine custody decisions. The manager should not make those choices for other heirs without a clear agreement, authority or applicable procedure.",
                            "Even if one relative handles every phone call, separate who gathers information, who may sign externally and who makes the final decision. A one-page responsibility sheet is much safer than saying that one person may 'handle everything.'",
                        ],
                    ),
                    (
                        "Create a separate authority sheet for each Mainland asset",
                        [
                            "For each asset, write down the city, receiving institution, proposed action and person expected to act. A title enquiry, a bank document request, a filing, a distribution agreement and receipt of funds may each require different evidence of authority.",
                            "Before sending the Macau appointment, ask the Mainland recipient what it proves, what heir records are still needed, whether an authorised agent may act and which decisions require personal confirmation. One management document is not a universal pass for every asset.",
                        ],
                    ),
                    (
                        "Use six columns to control every action",
                        [
                            "Use columns for the action, asset, urgency, evidence held, person whose approval is needed and record to keep afterwards. Routine preservation and information requests can come first. Mark a sale, transfer, distribution or settlement as awaiting confirmation.",
                            "If relatives already question the accounts, missing items or the manager's care, pause major transactions. Preserve the inventory, money trail and handover record before deciding whether the manager should continue. Clear accounts early are less likely to become a family dispute later.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"),
                    ("/articles/am/macau-heir-qualification-deed_en.html", "What a Macau heir qualification deed establishes"),
                    ("/articles/am/macau-no-will-mainland-property_en.html", "Where to start when no will has been found"),
                    ("/articles/am/multiple-wills-across-regions_en.html", "Organising several wills across regions"),
                ],
                "cta": "Tell us who currently holds the assets, which Mainland item needs attention and what the family has actually agreed. We can separate administration from final decisions.",
            },
        },
    },
    {
        "slug": "spousal-share-before-inheritance",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國家屬與內地房產",
                "title": "內地房產只寫逝者一人姓名，為甚麼仍要查配偶份額",
                "description": "美國家屬處理內地房產繼承時，先按購房、婚姻、出資和協議資料分清逝者份額，不把登記姓名直接等同全部遺產。",
                "lead": "房產證只有父親一個名字，並不等於整套房子一定都進入他的遺產。",
                "key_title": "先查三條線",
                "keys": [
                    "房屋在甚麼時候取得",
                    "買房和還款由誰出資",
                    "未查證據前不要先填一半",
                ],
                "answer_title": "登記姓名是起點，不是份額的最後答案",
                "answer": [
                    "處理繼承時，要先確認逝者生前真正擁有房屋的哪一部分，再把這一部分放進遺產。房屋只登記一人姓名是重要證據，但單靠姓名仍未必能確定最後份額；購買時間、資金來源、婚姻狀況和真實存在的書面安排也可能影響判斷。",
                    "不要先假設配偶一定有一半，也不要反過來認為配偶完全沒有份額。把事實時間線整理好，再由房產所在地按實際文件核對，比先做整套美國文件翻譯更可靠。",
                ],
                "sections": [
                    (
                        "先把購房和婚姻放在同一條時間線",
                        [
                            "列出結婚時間、購房合同日期、付款和貸款時間、登記日期，以及之後有沒有贈與、繼承、轉名或加名。再把首期、每期還款和大額裝修的付款來源接到時間線上。",
                            "婚前已取得、婚後共同出資、親屬明確只給一人，或夫妻確有書面安排，可能形成不同結果。先記錄並找原件，不要只憑“誰的名字在證上”、誰一直住在房裏，或家人的回憶下結論。",
                        ],
                    ),
                    (
                        "把配偶原有權益和逝者遺產分成兩格",
                        [
                            "如果核對後發現配偶本來已對房屋享有權益，這部分不是逝者去世後才繼承到的。應先把原有權益分出，再討論逝者剩餘份額由誰繼承。",
                            "這一步會影響遺囑能處理的範圍、繼承人之間的分配和後續轉名。若家人對出資或書面安排有不同說法，先保留銀行紀錄、合同、通訊和實際付款證據，不要急着在文件上填一個比例。",
                        ],
                    ),
                    (
                        "美國遺產文件不替內地房屋判定份額",
                        [
                            "美國法院文件可能列出資產、任命遺產代表，或顯示當地程序進行到哪一步。不同州對資產清單和夫妻財產的呈現也會不同。這些文件可以幫助說明背景，但不會自動改寫內地房產登記或直接決定房屋份額。",
                            "準備交到內地前，先分清文件的用途：證明死亡、說明誰是遺產代表、列出美國程序中的資產，還是連接中英文姓名。只有用途確定後，才知道哪些頁面值得做正式副本、附加證明和中文翻譯。",
                        ],
                    ),
                    (
                        "第一次詢問房產所在地時帶這六項",
                        [
                            "帶上房產證或登記資料、購房合同、付款與貸款線索、結婚和身份資料、可能存在的夫妻書面安排，以及現有美國死亡或遺產文件。若某項找不到，就清楚標為待查，不要用家人猜測代替。",
                            "直接問接收方：目前能否看出逝者可能擁有的份額、還缺哪類證據、配偶需要怎樣參與，以及美國文件分別用於哪一步。先把份額問題問清楚，再安排翻譯和簽署，能少走很多回頭路。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/sole-registered-mainland-property.html", "只登記逝者姓名時先查哪六件事"),
                    ("/articles/us/us-will-mainland-property.html", "美國遺囑寫到內地房產後怎樣處理"),
                    ("/articles/us/letters-testamentary-or-administration.html", "兩類美國法院任命文件分別說明甚麼"),
                ],
                "cta": "把購房時間、婚姻時間、付款線索和現有美國文件列在一頁，我們先判斷哪一部分可能真正進入遺產。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国家属与内地房产",
                "title": "内地房产只写逝者一人姓名，为什么仍要查配偶份额",
                "description": "美国家属处理内地房产继承时，先按购房、婚姻、出资和协议材料分清逝者份额，不把登记姓名直接等同全部遗产。",
                "lead": "房产证只有父亲一个名字，不等于整套房子一定都进入他的遗产。",
                "key_title": "先查三条线",
                "keys": [
                    "房屋在什么时间取得",
                    "买房和还款由谁出资",
                    "没有核对证据前不要先填一半",
                ],
                "answer_title": "登记姓名是起点，不是份额的最后答案",
                "answer": [
                    "处理继承时，要先确认逝者生前真正拥有房屋的哪一部分，再把这部分放进遗产。房屋只登记一人姓名是重要证据，但单靠姓名仍未必能确定最后份额；购买时间、资金来源、婚姻状况和真实存在的书面安排也可能影响判断。",
                    "不要先假设配偶一定有一半，也不要反过来认为配偶完全没有份额。把事实时间线整理好，再由房产所在地按照实际材料核对，比先做整套美国文件翻译更可靠。",
                ],
                "sections": [
                    (
                        "先把购房和婚姻放在同一条时间线",
                        [
                            "列出结婚时间、购房合同日期、付款和贷款时间、登记日期，以及后来有没有赠与、继承、转名或加名。再把首付款、每期还款和大额装修的付款来源接到时间线上。",
                            "婚前取得、婚后共同出资、亲属明确只给一人，或夫妻确有书面安排，可能形成不同结果。先记录并找原件，不要只凭“谁的名字在证上”、谁一直住在房里，或家人的回忆下结论。",
                        ],
                    ),
                    (
                        "把配偶原有权益和逝者遗产分成两格",
                        [
                            "如果核对后发现配偶原本已经对房屋享有权益，这部分不是逝者去世后才继承到的。应先把原有权益分出，再讨论逝者剩余份额由谁继承。",
                            "这会影响遗嘱能够处理的范围、继承人之间的分配和后续转名。家人对出资或书面安排有不同说法时，先保存银行记录、合同、通信和实际付款证据，不要急着在文件上填写一个比例。",
                        ],
                    ),
                    (
                        "美国遗产文件不替内地房屋判断份额",
                        [
                            "美国法院文件可能列出资产、任命遗产代表，或显示当地程序进行到哪一步。不同州对资产清单和夫妻财产的呈现也会不同。这些文件可以说明背景，但不会自动改写内地房产登记或直接决定房屋份额。",
                            "交到内地前，先分清每份文件的用途：证明死亡、说明谁是遗产代表、列出美国程序中的资产，还是连接中英文姓名。用途确定后，才知道哪些页面需要正式副本、附加证明和中文翻译。",
                        ],
                    ),
                    (
                        "第一次询问房产所在地时带这六项",
                        [
                            "带上房产证或登记材料、购房合同、付款与贷款线索、婚姻和身份材料、可能存在的夫妻书面安排，以及现有美国死亡或遗产文件。找不到的项目清楚标成待查，不要用家人猜测代替。",
                            "直接问接收方：现有材料能否看出逝者可能拥有的份额、还缺哪类证据、配偶需要怎样参与，以及美国文件分别用于哪一步。先把份额问题问清楚，再安排翻译和签署，能减少很多重复准备。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/sole-registered-mainland-property_cn.html", "只登记逝者姓名时先查哪六件事"),
                    ("/articles/us/us-will-mainland-property_cn.html", "美国遗嘱写到内地房产后怎样处理"),
                    ("/articles/us/letters-testamentary-or-administration_cn.html", "两类美国法院任命文件分别说明什么"),
                ],
                "cta": "把购房时间、婚姻时间、付款线索和现有美国文件列在一页，我们先判断哪一部分可能真正进入遗产。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. families and Mainland property",
                "title": "Sole Name on a Mainland Title: Check the Spouse's Share First",
                "description": "Why a U.S. family should reconstruct the purchase, marriage, funding and ownership history before treating a Mainland home as the deceased's estate.",
                "lead": "A Mainland title in the father's name alone does not necessarily mean that the entire home belongs in his estate.",
                "key_title": "Trace three timelines",
                "keys": [
                    "When the home was acquired",
                    "Who funded the purchase and mortgage",
                    "Check the evidence before choosing a percentage",
                ],
                "answer_title": "The registered name is the starting point, not the final share",
                "answer": [
                    "Before distributing an estate, identify the interest the deceased actually owned. A sole name on the title is important evidence, but it may not settle the share by itself. The acquisition date, source of funds, marriage history and any genuine written ownership agreement may also matter.",
                    "Do not assume that the spouse automatically owns one half, and do not assume that the spouse has no interest. Reconstruct the facts, then ask the receiving city to review the actual records before translating the entire U.S. file.",
                ],
                "sections": [
                    (
                        "Put the purchase and marriage on one timeline",
                        [
                            "List the marriage date, purchase contract, deposits, mortgage payments, registration and any later gift, inheritance or title change. Connect the source of the down payment, regular repayments and any major capital payment to the same timeline.",
                            "A home acquired before marriage, jointly funded after marriage, expressly given to one spouse or covered by a genuine written ownership agreement may require different treatment. Find the original records instead of relying on the title name, who lived there or a relative's memory.",
                        ],
                    ),
                    (
                        "Separate the spouse's existing interest from the estate",
                        [
                            "If the evidence shows that the spouse already had an interest, that interest was not inherited after the death. It should be identified first. Only the deceased's remaining interest is then considered for inheritance.",
                            "This affects what a will can dispose of, how the heirs divide the estate and what can be transferred. If relatives disagree about funding or an agreement, preserve bank records, contracts, messages and payment evidence rather than choosing a percentage for convenience.",
                        ],
                    ),
                    (
                        "U.S. probate papers do not decide the Mainland share",
                        [
                            "A U.S. court file may list assets, appoint a personal representative or show the stage of a local probate. The presentation of ownership and spousal property also varies by state. These records provide context, but they do not rewrite a Mainland title or determine the property share by themselves.",
                            "Define each document's job before using it in Mainland China: proving the death, identifying the personal representative, recording an asset in the U.S. case or connecting English and Chinese names. Only then decide which certified copies, apostilles and translations are worth preparing.",
                        ],
                    ),
                    (
                        "Take six items to the first review in the property city",
                        [
                            "Bring the title record, purchase contract, payment and mortgage clues, marriage and identity records, any written spousal property arrangement, and the available U.S. death or probate papers. Mark a missing item as unknown rather than replacing it with a family assumption.",
                            "Ask what the current evidence says about the deceased's possible share, what further proof is needed, how the spouse must participate and where each U.S. document fits. Resolve the ownership question before arranging translation and signatures to avoid repeating the work.",
                        ],
                    ),
                ],
                "related_title": "Continue with the U.S. topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling a Mainland estate"),
                    ("/articles/us/sole-registered-mainland-property_en.html", "Six checks for a home registered only to the deceased"),
                    ("/articles/us/us-will-mainland-property_en.html", "When a U.S. will names Mainland property"),
                    ("/articles/us/letters-testamentary-or-administration_en.html", "Letters Testamentary or Letters of Administration"),
                ],
                "cta": "Put the purchase date, marriage date, payment trail and U.S. papers on one page. We can then identify the interest that may actually form part of the estate.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/macau/index.html": (
        "/articles/am/estate-manager-role-boundary.html",
        '<a href="/articles/am/estate-manager-role-boundary.html"><span class="v24-tag">遺產管理</span><strong>待分割財產管理人能做甚麼，哪些事仍要繼承人決定</strong><p>分開日常保管、對外簽署和最終分配決定。</p></a>',
    ),
    "articles/macau/index_cn.html": (
        "/articles/am/estate-manager-role-boundary_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">遗产管理</span><h3>待分割财产管理人能做什么，哪些事仍要继承人决定</h3><p>分开日常保管、对外签署和最终分配决定。</p></div><a class="v25-pill-action" href="/articles/am/estate-manager-role-boundary_cn.html">阅读文章</a></article>',
    ),
    "articles/macau/index_en.html": (
        "/articles/am/estate-manager-role-boundary_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Estate manager</span><h3>What a Macau estate manager can and cannot decide</h3><p>Separate routine preservation, external signing and final distribution decisions.</p></div><a class="v25-pill-action" href="/articles/am/estate-manager-role-boundary_en.html">Read Article</a></article>',
    ),
    "articles/united-states/index.html": (
        "/articles/us/spousal-share-before-inheritance.html",
        '<a href="/articles/us/spousal-share-before-inheritance.html"><span class="v24-tag">配偶份額</span><strong>房產只寫逝者姓名，為甚麼仍要查配偶份額</strong><p>按購房、婚姻、出資和書面安排重建權益。</p></a>',
    ),
    "articles/united-states/index_cn.html": (
        "/articles/us/spousal-share-before-inheritance_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">配偶份额</span><h3>房产只写逝者姓名，为什么仍要查配偶份额</h3><p>按照购房、婚姻、出资和书面安排重建权益。</p></div><a class="v25-pill-action" href="/articles/us/spousal-share-before-inheritance_cn.html">阅读文章</a></article>',
    ),
    "articles/united-states/index_en.html": (
        "/articles/us/spousal-share-before-inheritance_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Spousal share</span><h3>Sole name on a Mainland title: check the spouse\'s share</h3><p>Reconstruct the purchase, marriage, funding and written arrangements.</p></div><a class="v25-pill-action" href="/articles/us/spousal-share-before-inheritance_en.html">Read Article</a></article>',
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
