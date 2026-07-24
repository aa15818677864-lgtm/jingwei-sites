from __future__ import annotations

from publish_regional_inheritance_foundations import (
    LANG_SUFFIX,
    ROOT,
    SITE,
    TODAY,
    render_article,
    visual_svg,
)


ARTICLES = [
    {
        "slug": "remote-china-lawyer",
        "directory": "articles/us",
        "topic": "united-states",
        "date_published": {"tc": "2026-05-16", "cn": TODAY, "en": TODAY},
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務文章庫",
                "eyebrow": "美國專題 · 遠程處理內地繼承",
                "title": "人在美國處理內地繼承，哪些可以遠程做，哪些要自己決定",
                "description": "人在美國處理內地繼承時，先分清可遠程整理、需要書面授權、仍由家屬決定及須向接收方確認的事項。",
                "lead": "家人過世後，人在美國未必需要立刻飛回內地。資料整理、資產定位和初步法律判斷通常可以先遠程開始；但授權書不是一張『甚麼都能做』的通行證。",
                "key_title": "先記住這四點",
                "keys": [
                    "先寫清楚要處理哪一項遺產，不用一開始把所有事情混在一起。",
                    "家屬是否同意分配、出售或和解，不能用一句『全權代理』含糊帶過。",
                    "授權文件先給內地接收方看內容，再在美國簽署和辦理證明。",
                    "州級、聯邦級文件的出具和證明路徑不同，不能只按居住州猜。",
                ],
                "visuals": [
                    (
                        "遠程可以開始，但決定仍要分清",
                        "律師整理與核對",
                        "家屬作出關鍵決定",
                        "遠程協作不等於把全部權利交出去。",
                    ),
                    (
                        "一份授權文件的準備順序",
                        "列明任務和資產",
                        "向接收方確認",
                        "再簽署與辦證",
                        "先確認內容和用途，能減少重簽。",
                    ),
                    (
                        "第一次溝通先備好",
                        "內地資產城市",
                        "遺囑與家屬名單",
                        "要代辦的具體事項",
                        "美國文件簽發州",
                        "四項資料足以開始判斷遠程路徑。",
                    ),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "可以先遠程開始，但要把『律師可以替你做的程序工作』和『家屬必須自己作出的決定』分開。核對房產城市、整理死亡和親屬文件、列出可能繼承人、詢問內地接收方的材料要求，通常不必等到本人回內地才開始。",
                    "真正要簽授權書時，不要只寫『全權代理』。應按資產和任務列明：可否查詢資料、提交申請、接收文件、參與訴訟、調解或簽署分配文件。涉及放棄權利、改變主張、和解、收取款項或處分房產的事項，更要逐項確認。接收方如要求本人視頻核驗、親筆簽署或到場，仍要按該項程序另外處理。",
                ],
                "sections": [
                    (
                        "哪些事情通常可以先遠程做",
                        [
                            "第一步不是辦一份很寬的授權，而是把事實做成一頁清單：逝者姓名和曾用名、死亡時間、家屬關係、是否有遺囑、內地房產或賬戶所在城市，以及目前誰保管原件。這些資料足夠律師先判斷缺口。",
                            "家屬也可以遠程確認內地哪個機構或程序會接收材料。房產登記、銀行領款、法院程序和公證核實，各自需要的文件並不相同；先找接收方，再準備文件，比先做完一套證明再四處試用更穩妥。",
                        ],
                    ),
                    (
                        "哪些決定不能含糊地交出去",
                        [
                            "律師可以解釋方案、整理證據和代辦獲授權的程序，但不能替家屬憑空決定遺產怎樣分、是否放棄份額、是否出售房屋，或是否接受和解。家屬之間意見不一致時，應先把爭議寫清楚。",
                            "如果已進入訴訟，承認或放棄主張、變更請求、和解、反訴或上訴等事項通常需要特別寫明。只寫『全權代理』，往往不足以讓代理人完成這些動作。即使不是訴訟，也應把收取文件、領取款項和處分資產等高風險權限逐項列出。",
                        ],
                    ),
                    (
                        "授權書要按任務寫，不要按想像寫",
                        [
                            "一份實用的授權書至少要對應四個問題：處理哪項資產、面向哪個接收方、可以做哪些動作、何時終止。房產和銀行賬戶最好分開寫；查詢資料和處分資產也不要混成一句。",
                            "簽署前先把草稿交給將要接收文件的內地機構或辦理人核對。對方可能要求特定稱呼、身份資料、房屋地址、是否可轉委託，以及原件或譯本形式。這一步放在美國簽字之前，通常最省時間。",
                        ],
                    ),
                    (
                        "在美國簽文件，先看由哪裏出具",
                        [
                            "美國州或縣級機關簽發的死亡、婚姻紀錄，以及在某州完成公證的授權書，通常由簽發或公證所在州的主管機關處理附加證明；聯邦機關出具的文件則走聯邦路徑。附加證明主要確認簽名、職銜或印章的真實性，不替內地接收方判斷文件內容是否足夠。",
                            "以加州為例，州務卿只處理符合其要求的加州公文書或經公證文件。其他州做法、費用和受理方式可能不同。先確認文件的簽發州、簽署方式、中文譯本和內地用途，再決定在哪裏辦理，不要只因本人住在洛杉磯就把所有文件送到加州。",
                        ],
                    ),
                ],
                "related_title": "繼續看美國繼承專題",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/us-documents-mainland-property-inheritance.html", "美國死亡證明和遺囑用於內地房產前先核對甚麼"),
                    ("/articles/us/issuing-state-matters.html", "美國文件先看由州級還是聯邦機關出具"),
                    ("/articles/us/domicile-and-mainland-asset-location.html", "住所州和內地資產所在地分別影響甚麼"),
                ],
                "cta": "說明你所在州、逝者和家屬情況、內地資產城市，以及希望代辦的具體事項，便可先判斷哪些步驟能遠程開始。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务文章库",
                "eyebrow": "美国专题 · 远程处理内地继承",
                "title": "人在美国处理内地继承，哪些可以远程做，哪些要自己决定",
                "description": "人在美国处理内地继承时，先分清可远程整理、需要书面授权、仍由家属决定以及要向接收方确认的事项。",
                "lead": "家人去世后，人在美国不一定要马上飞回内地。资料整理、资产定位和初步判断通常可以先远程开始，但授权书并不是一张“什么都能做”的通行证。",
                "key_title": "先记住这四点",
                "keys": [
                    "先明确要处理哪一项遗产，不要一开始把所有事情混在一起。",
                    "家属是否同意分配、出售或和解，不能用一句“全权代理”带过。",
                    "授权文件先给内地接收方核对内容，再在美国签署和办理证明。",
                    "州级和联邦文件的出具、证明路径不同，不能只看本人住在哪个州。",
                ],
                "visuals": [
                    ("远程可以开始，决定仍要分清", "律师整理和核对", "家属作出关键决定", "远程协作不等于把全部权利交出去。"),
                    ("授权文件的准备顺序", "列明任务和资产", "向接收方确认", "再签署和办证", "先确认内容和用途，可以减少重签。"),
                    ("第一次沟通先备好", "内地资产城市", "遗嘱和家属名单", "要代办的具体事项", "美国文件签发州", "四项资料足以开始判断远程路径。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "可以先远程开始，但要把“律师可以代办的程序工作”和“家属必须自己作出的决定”分开。核对房产城市、整理死亡和亲属材料、列出可能继承人、询问内地接收方的材料要求，通常不必等到本人回内地才开始。",
                    "真正需要签授权书时，不要只写“全权代理”。应当按资产和任务列明：能否查询资料、提交申请、接收文件、参加诉讼、调解或签署分配文件。涉及放弃权利、改变主张、和解、收款或处分房产的事项，更要逐项确认。接收方如果要求本人视频核验、亲笔签署或者到场，仍要按该项程序另外处理。",
                ],
                "sections": [
                    (
                        "哪些事情通常可以先远程做",
                        [
                            "第一步不是办理一份范围很宽的授权，而是把事实整理成一页：逝者姓名和曾用名、去世时间、家属关系、是否有遗嘱、内地房产或账户所在城市，以及目前谁保管原件。这些信息已经足够律师先判断缺口。",
                            "家属也可以远程确认内地由哪个机构或程序接收材料。房产登记、银行领款、法院程序和公证核实各有要求；先确定接收方，再准备文件，比先做完一套证明再到处试用更稳妥。",
                        ],
                    ),
                    (
                        "哪些决定不能含糊地交出去",
                        [
                            "律师可以解释方案、整理证据和代办授权范围内的程序，但不能替家属凭空决定遗产怎么分、是否放弃份额、是否出售房屋，或者是否接受和解。家属之间意见不一致时，先把争议写清楚。",
                            "如果已经进入诉讼，承认或放弃主张、变更请求、和解、反诉或上诉等事项通常需要特别写明。只写“全权代理”，往往不足以完成这些动作。即使不是诉讼，收取文件、领取款项和处分资产等高风险权限也应逐项列出。",
                        ],
                    ),
                    (
                        "授权书要按任务写，不要按想象写",
                        [
                            "一份实用的授权书至少要回答四个问题：处理哪项资产、面向哪个接收方、可以做哪些动作、什么时候终止。房产和银行账户最好分开写，查询资料和处分资产也不要混成一句。",
                            "签署前先把草稿交给将要接收文件的内地机构或办理人员核对。对方可能要求特定称呼、身份信息、房屋地址、是否可转委托，以及原件或译本形式。把这一步放在美国签字之前，通常更省时间。",
                        ],
                    ),
                    (
                        "在美国签文件，先看由哪里出具",
                        [
                            "美国州或县级机构签发的死亡、婚姻记录，以及在某州完成公证的授权书，通常由签发或公证所在州的主管机构处理附加证明；联邦机构出具的文件则走联邦路径。附加证明主要确认签名、职衔或印章的真实性，不替内地接收方判断文件内容是否足够。",
                            "以加州为例，州务卿只处理符合要求的加州公文书或经公证文件。其他州的做法、费用和受理方式可能不同。先确认文件签发州、签署方式、中文译本和内地用途，再决定在哪里办理，不要因为本人住在洛杉矶就把所有文件送到加州。",
                        ],
                    ),
                ],
                "related_title": "继续看美国继承专题",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/us-documents-mainland-property-inheritance_cn.html", "美国死亡证明和遗嘱用于内地房产前先核对什么"),
                    ("/articles/us/issuing-state-matters_cn.html", "美国文件先看由州级还是联邦机构出具"),
                    ("/articles/us/domicile-and-mainland-asset-location_cn.html", "住所州和内地资产所在地分别影响什么"),
                ],
                "cta": "说明你所在州、逝者和家属情况、内地资产城市，以及希望代办的具体事项，就可以先判断哪些步骤能远程开始。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "United States · Remote Mainland estate work",
                "title": "Can a Family Handle a Mainland China Inheritance from the United States?",
                "description": "A practical guide to the work that can begin remotely, the decisions the family must retain, and the authority a Mainland lawyer actually needs.",
                "lead": "A family in the United States can usually begin the fact review, asset mapping and document checks without flying to Mainland China. The important distinction is between work a lawyer may carry out and decisions the heirs must still make themselves.",
                "key_title": "Four boundaries to set first",
                "keys": [
                    "Identify the specific estate asset or procedure before drafting any authority.",
                    "A broad phrase such as “full authority” does not safely cover every family decision.",
                    "Have the Mainland recipient review the wording before the document is signed in the United States.",
                    "The issuing authority, not the family's current address, determines the U.S. certification route.",
                ],
                "visuals": [
                    ("Remote work and family decisions", "Lawyer reviews and acts", "Family keeps key decisions", "Remote instructions do not transfer every right."),
                    ("Prepare the authority in this order", "Define task and asset", "Confirm with recipient", "Sign and certify", "Confirm the wording before anyone signs."),
                    ("Facts for the first call", "Mainland asset city", "Will and family list", "Exact delegated tasks", "U.S. issuing state", "These four facts are enough to map the next step."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "Yes, much of the work can begin remotely. A Mainland lawyer can review the family structure, map properties or accounts, identify missing records and check what a bank, registry, notary office or court expects. None of that requires the family to sign a sweeping power of attorney at the outset.",
                    "When authority is needed, define it by asset, recipient and task. State whether the representative may request records, file documents, receive notices, appear in proceedings or sign a particular instrument. Decisions about giving up a claim, settling a dispute, receiving money or disposing of property should never be left to a vague catch-all phrase. If a recipient requires live identity verification, a personal signature or attendance, that requirement must still be handled separately.",
                ],
                "sections": [
                    (
                        "Work that can usually begin remotely",
                        [
                            "Start with a one-page fact sheet: the deceased's English and Chinese names, date of death, family members, any will, the Mainland city of each known property or account, and who currently holds the original records. A lawyer can identify the first evidence gaps from that sheet.",
                            "The family can also confirm the actual Mainland recipient before preparing U.S. documents. A property registry, bank, court and notary office may each ask for a different combination of records. Recipient-first preparation is more reliable than producing one expensive packet and hoping every institution accepts it.",
                        ],
                    ),
                    (
                        "Decisions the family should not hand over vaguely",
                        [
                            "A lawyer may explain options, organise evidence and carry out authorised procedural steps. The lawyer cannot invent the family's decision on distribution, renunciation, sale of property or settlement. If relatives disagree, record the disagreement rather than hiding it inside broad authority.",
                            "In court proceedings, admitting or abandoning a claim, changing the relief sought, settling, counterclaiming or appealing generally calls for specific authority. Outside court, it is still prudent to list high-risk acts separately, including receiving money, accepting original documents and signing a transfer or distribution instrument.",
                        ],
                    ),
                    (
                        "Draft authority around the task",
                        [
                            "A useful instruction answers four questions: which asset is involved, who will receive the document, what the representative may do, and when the authority ends. Keep property and bank work separate, and do not combine a records request with authority to dispose of the asset.",
                            "Send the draft to the Mainland recipient or handling professional before it is signed. The recipient may require a particular institution name, property address, identity wording, permission to subdelegate, or a specific original and translation format. That check is far cheaper before notarisation and certification than after it.",
                        ],
                    ),
                    (
                        "The U.S. document route follows its source",
                        [
                            "A vital record issued by a state or county, and a power of attorney notarised within a state, normally follow the route of the issuing or notarising state. A federal record follows the federal route. An apostille authenticates the relevant signature, official capacity or seal; it does not prove that the document's contents satisfy a Mainland inheritance procedure.",
                            "California, for example, apostilles qualifying California public records and notarised documents. Other states have their own submission methods and requirements. Confirm the issuing state, signature, translation and Mainland use before filing. Living in Los Angeles does not turn an out-of-state or federal document into a California document.",
                        ],
                    ),
                ],
                "related_title": "Continue with the U.S. estate topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling Mainland estate matters"),
                    ("/articles/us/us-documents-mainland-property-inheritance_en.html", "Using U.S. death and will records for Mainland property"),
                    ("/articles/us/issuing-state-matters_en.html", "Why the U.S. issuing authority changes the apostille route"),
                    ("/articles/us/domicile-and-mainland-asset-location_en.html", "U.S. domicile and Mainland asset location answer different questions"),
                ],
                "cta": "Tell us the state, the deceased's names, the Mainland asset city and the exact task you want handled. That is enough to identify which steps can begin remotely.",
            },
        },
    },
    {
        "slug": "unknown-mainland-property-city",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_MO",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務文章庫",
                "eyebrow": "澳門專題 · 內地房產線索",
                "title": "只知道家人在內地有房，澳門家屬先怎樣找城市和地址線索",
                "description": "只知道逝者在內地有房時，澳門家屬怎樣從房屋、付款、居住和通訊記錄建立線索，再向可能城市確認查詢途徑。",
                "lead": "家人只記得『在珠海買過房』，沒有房產證，也說不出小區名稱。這時不要先找人承諾全國查房，先把零散記憶變成可核對的城市和地址線索。",
                "key_title": "先做這四件事",
                "keys": [
                    "把家人記憶、文件和付款記錄分開標明，不把猜測寫成事實。",
                    "先找可能城市、登記姓名和共同權利人，再問當地查詢途徑。",
                    "每項線索記下來源、日期和可信程度，避免家屬反覆爭論。",
                    "不要借用他人賬號或委託不明人士查私人登記資料。",
                ],
                "visuals": [
                    ("先把記憶變成證據線索", "家人模糊記憶", "可核對文件與記錄", "線索要有來源，不把猜測當地址。"),
                    ("找到查詢城市的路徑", "收集四類線索", "圈出可能城市", "再問當地查詢條件", "先縮小城市，再決定正式查詢。"),
                    ("一間可能房產記一行", "姓名與曾用名", "城市或小區", "付款或管理記錄", "線索來源與日期", "一行一間房，家屬才不會混淆。"),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "先做一張『資產線索表』，不是先猜一個完整地址。把房屋文件、銀行付款、物業或水電記錄、照片和聊天信息分成四組，每找到一條就記下來源和日期。最先要確認的是可能城市、登記姓名和是否有共同權利人。",
                    "內地房產登記資料並不是任何人都能用姓名隨意查。權利人、能證明利害關係的人，以及依法獲授權的代理人，可按現行規則申請相應範圍的資料；具體入口和材料由實際辦理登記的當地機構核對。城市尚未鎖定前，沒有人應承諾『全國查到』。",
                ],
                "sections": [
                    (
                        "四組線索，比只問家人更有用",
                        [
                            "第一組是房屋文件：舊房產證、購房合同、收樓信、按揭通知、裝修單、保險單或物業信件。即使只有半張照片，也可能看出開發商、小區、銀行或城市。",
                            "第二組是付款記錄：首期、按揭、管理費、維修款、水電或租金。第三組是生活記錄：快遞地址、停車證、門禁卡、搬家或裝修照片。第四組是通訊記錄：與中介、租客、物業、鄰居或共同購房人的聊天。每組都可能只提供一小段，但拼在一起常能縮小城市和小區。",
                        ],
                    ),
                    (
                        "線索表要分清『看見』和『聽說』",
                        [
                            "一間可能房產記一行：可能城市、小區或道路、登記姓名、可能共同權利人、線索來源、文件日期和保管人。原件寫『已見』，照片寫『有影像』，家人回憶寫『待核對』。這樣可以避免一句『我記得在珠海』被抄成確定地址。",
                            "姓名也要列出澳門證件姓名、內地舊姓名、拼音或曾用字。很多家庭卡住，不是沒有房，而是付款人、合同買受人和家屬口中的姓名未必完全一致。先把差異並排放好，不要自行把它們改成同一個人。",
                        ],
                    ),
                    (
                        "圈出可能城市後，再問正式查詢條件",
                        [
                            "有了較可靠的城市或小區線索，再向該地實際辦理登記的機構確認：誰可以查、需要甚麼身份和利害關係材料、可查到哪一類結果、能否由代理人申請，以及是否需要具體坐落或其他識別資料。不同城市的線上入口和受理方式可能不同。",
                            "現行規則允許權利人、利害關係人及其代理人按條件查詢，但查詢範圍會隨身份和證明材料而變。繼承家屬要準備的，不只是逝者姓名，還包括死亡、親屬關係、授權和現有房屋線索。若已指定遺產管理人，也應一併說明。",
                        ],
                    ),
                    (
                        "家屬不配合或線索在別人手裏時",
                        [
                            "如果銀行信、物業單或手機在另一名家屬手裏，先列明對方持有哪些資料和你已經掌握甚麼，不要使用對方賬號或冒充本人查詢。可以要求對方只提供遮去敏感資料的地址頁或付款摘要，先確認城市。",
                            "有人否認房產存在、拒絕交資料，或多個姓名和共同購房人互相衝突時，問題已不只是『找地址』。這時要保留原始聊天、付款和持有資料的證據，再判斷是否需要律師調查、保全證據或進入爭議程序。",
                        ],
                    ),
                ],
                "related_title": "繼續看澳門繼承專題",
                "related": [
                    ("/articles/macau/", "澳門家屬繼承內地遺產專題"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門家屬繼承內地房產先分清兩套文件"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance.html", "澳門死亡紀錄用於內地房產前先核對甚麼"),
                    ("/articles/am/macau-kinship-certificate-scope.html", "澳門親屬關係文件能證明甚麼"),
                ],
                "cta": "把你知道的城市、姓名、舊地址、付款或物業線索逐項寫下，便可以先判斷還缺哪一條關鍵線索。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务文章库",
                "eyebrow": "澳门专题 · 内地房产线索",
                "title": "只知道家人在内地有房，澳门家属先怎样找城市和地址线索",
                "description": "只知道逝者在内地有房时，澳门家属如何从房屋、付款、居住和通信记录建立线索，再向可能城市确认查询途径。",
                "lead": "家人只记得“在珠海买过房”，没有房产证，也说不出小区名称。这时不要先找人承诺全国查房，先把零散记忆变成可以核对的城市和地址线索。",
                "key_title": "先做这四件事",
                "keys": [
                    "把家人记忆、文件和付款记录分开标明，不把猜测写成事实。",
                    "先找可能城市、登记姓名和共同权利人，再问当地查询途径。",
                    "每条线索记下来源、日期和可信程度，避免家属反复争论。",
                    "不要借用他人账号或委托不明人员查询私人登记资料。",
                ],
                "visuals": [
                    ("先把记忆变成证据线索", "家人模糊记忆", "可核对文件和记录", "线索要有来源，不把猜测当地址。"),
                    ("找到查询城市的路径", "收集四类线索", "圈出可能城市", "再问当地查询条件", "先缩小城市，再决定正式查询。"),
                    ("一套可能房产记一行", "姓名和曾用名", "城市或小区", "付款或物业记录", "线索来源和日期", "一行一套房，家属才不会混淆。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "先做一张“资产线索表”，不要急着猜完整地址。把房屋文件、银行付款、物业或水电记录、照片和聊天信息分成四组，每找到一条就记下来源和日期。最先要确认的是可能城市、登记姓名和是否存在共同权利人。",
                    "内地房产登记资料并不是任何人都能用姓名随意查询。权利人、能证明利害关系的人，以及依法获得授权的代理人，可以按现行规则申请相应范围的资料；具体入口和材料要由实际办理登记的当地机构确认。城市还没有锁定时，不应相信“全国查到”的承诺。",
                ],
                "sections": [
                    (
                        "四组线索，比只问家人更有用",
                        [
                            "第一组是房屋文件：旧房产证、购房合同、收楼信、按揭通知、装修单、保险单或物业信件。即使只有半张照片，也可能看出开发商、小区、银行或城市。",
                            "第二组是付款记录：首付款、按揭、管理费、维修款、水电或租金。第三组是生活记录：快递地址、停车证、门禁卡、搬家或装修照片。第四组是通信记录：与中介、租客、物业、邻居或共同购房人的聊天。每组可能只提供一小段，但合起来常能缩小城市和小区。",
                        ],
                    ),
                    (
                        "线索表要分清“看见”和“听说”",
                        [
                            "一套可能房产记一行：可能城市、小区或道路、登记姓名、可能共同权利人、线索来源、文件日期和保管人。原件写“已见”，照片写“有影像”，家人回忆写“待核对”。这样可以避免一句“我记得在珠海”被抄成确定地址。",
                            "姓名也要列出澳门证件姓名、内地旧姓名、拼音或曾用字。很多家庭卡住，不是没有房，而是付款人、合同买受人和家人口中的姓名未必完全一致。先把差异并排列出，不要自行认定是同一个人。",
                        ],
                    ),
                    (
                        "圈出可能城市后，再问正式查询条件",
                        [
                            "有了较可靠的城市或小区线索，再向当地实际办理登记的机构确认：谁可以查、需要什么身份和利害关系材料、可以查到哪一类结果、能否由代理人申请，以及是否需要具体坐落或其他识别信息。不同城市的线上入口和受理方式可能不同。",
                            "现行规则允许权利人、利害关系人及其代理人按条件查询，但查询范围会随身份和证明材料变化。继承家属要准备的不只是逝者姓名，还包括死亡、亲属关系、授权和现有房屋线索。如果已经指定遗产管理人，也应一并说明。",
                        ],
                    ),
                    (
                        "家属不配合或线索在别人手里时",
                        [
                            "如果银行信、物业单或手机在另一名家属手里，先列明对方持有哪些资料和你已经掌握什么，不要使用对方账号或冒充本人查询。可以请对方只提供遮住敏感信息的地址页或付款摘要，先确认城市。",
                            "有人否认房产存在、拒绝交资料，或者多个姓名和共同购房人相互冲突时，问题已经不只是“找地址”。应当保留原始聊天、付款和资料持有情况的证据，再判断是否需要律师调查、证据保全或争议程序。",
                        ],
                    ),
                ],
                "related_title": "继续看澳门继承专题",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属继承内地遗产专题"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门家属继承内地房产先分清两套材料"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_cn.html", "澳门死亡记录用于内地房产前先核对什么"),
                    ("/articles/am/macau-kinship-certificate-scope_cn.html", "澳门亲属关系材料能证明什么"),
                ],
                "cta": "把你知道的城市、姓名、旧地址、付款或物业线索逐项写下，就可以先判断还缺哪一条关键信息。",
            },
            "en": {
                "lang": "en",
                "locale": "en_MO",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Macau · Tracing Mainland property",
                "title": "A Macau Family Knows There Is Property in Mainland China but Not Where: How to Start",
                "description": "How a Macau family can turn old papers, payment records and family memories into a reliable property clue sheet before making a lawful local enquiry.",
                "lead": "The family remembers that the deceased bought an apartment, perhaps in Zhuhai, but no one has the title record or even the estate name. The useful first step is not a promise of a nationwide search. It is a disciplined record of what the family actually knows.",
                "key_title": "Four steps before any search",
                "keys": [
                    "Separate family memory from documents and payment records.",
                    "Identify a likely city, registered name and possible co-owner first.",
                    "Record the source, date and reliability of every clue.",
                    "Do not use another person's account or an unverified private search service.",
                ],
                "visuals": [
                    ("Turn memory into evidence", "Uncertain family memory", "Records that can be checked", "A clue needs a source before it becomes useful."),
                    ("From clues to a lawful enquiry", "Collect four clue groups", "Identify likely city", "Confirm local conditions", "Narrow the city before choosing the enquiry route."),
                    ("Use one row per possible property", "Names and aliases", "City or estate", "Payment or management", "Source and date", "One property per row prevents family confusion."),
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "Build an asset clue sheet before trying to reconstruct a complete address. Group the evidence into property papers, payments, occupation or management records, and messages or photographs. Record where each clue came from and when it was created. The first targets are a likely city, the registered name and any possible co-owner.",
                    "Mainland property registration information is not an open database that anyone may search by a person's name. Rights holders, people who can establish a relevant legal interest and properly authorised representatives may request defined information under the applicable rules. The local registry that handled the property confirms the identity, evidence and enquiry method it accepts.",
                ],
                "sections": [
                    (
                        "Four groups of clues are better than repeated family guesses",
                        [
                            "Start with property papers: an old title record, purchase agreement, handover letter, mortgage notice, renovation invoice, insurance policy or property-management correspondence. Even part of a photograph may reveal a developer, estate, bank or city.",
                            "Then review payments such as a deposit, mortgage, management fee, repair fund, utilities or rent. Add everyday records such as delivery addresses, parking permits, access cards and renovation photographs. Finally, check messages with agents, tenants, neighbours, management staff or a co-purchaser. Each group may be incomplete, but together they can identify a plausible city and estate.",
                        ],
                    ),
                    (
                        "Distinguish what was seen from what was heard",
                        [
                            "Give each possible property one row: city, estate or street, registered name, possible co-owner, source, date and current holder. Mark an original as seen, a photograph as image only, and a relative's recollection as unverified. A memory such as 'somewhere in Zhuhai' should never silently become a confirmed address.",
                            "List the Macau identity name, any former Mainland name, romanisation and known character variants. The payer, named purchaser and person remembered by the family may not appear in exactly the same form. Keep the variants visible until evidence connects them.",
                        ],
                    ),
                    (
                        "Confirm the local enquiry conditions after identifying a city",
                        [
                            "Once a city or estate is reasonably supported, ask the local registration authority that would hold the record who may enquire, what identity and interest evidence is required, what result may be disclosed, whether a representative can apply, and whether a property location or other identifier is needed. Online access and appointment methods differ by city.",
                            "Current rules allow rights holders, qualifying interested persons and their representatives to seek information within the permitted scope. An inheritance enquiry therefore needs more than the deceased's name. The family should be ready to show death, relationship, authority and the property clues already found. If an estate administrator has been appointed, explain that status as well.",
                        ],
                    ),
                    (
                        "When another relative controls the clues",
                        [
                            "If another relative holds the bank letters, management bills or phone, record exactly what is held and what you already know. Do not log into that person's account or impersonate them. A redacted address page or payment summary may be enough to confirm the city without exposing unrelated private information.",
                            "If someone denies the property exists, refuses to share records, or the names and possible co-owners conflict, the problem is no longer a simple address search. Preserve the original messages, payment trail and evidence of who holds the records, then assess whether a lawyer-led investigation, evidence preservation or dispute process is appropriate.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau estate topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling Mainland estate matters"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Keep the Macau and Mainland property files separate"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_en.html", "Using a Macau death record for Mainland property"),
                    ("/articles/am/macau-kinship-certificate-scope_en.html", "What Macau family records can prove"),
                ],
                "cta": "List every known city, name, old address, payment and property-management clue. That is enough to identify the most important missing fact.",
            },
        },
    },
]


def article_path(article: dict, lang: str) -> str:
    return f"/{article['directory']}/{article['slug']}{LANG_SUFFIX[lang]}.html"


def write_articles() -> None:
    for article in ARTICLES:
        target_dir = ROOT / article["directory"]
        image_dir = target_dir / "images" / article["slug"]
        image_dir.mkdir(parents=True, exist_ok=True)
        for lang in ("tc", "cn", "en"):
            suffix = LANG_SUFFIX[lang]
            (target_dir / f"{article['slug']}{suffix}.html").write_text(
                render_article(article, lang), encoding="utf-8"
            )
            for index, name in enumerate(("context", "path", "checklist"), start=1):
                svg = visual_svg(article["copy"][lang]["visuals"][index - 1], index)
                svg = (
                    svg.replace(".item{font-size:29px", ".item{font-size:42px")
                    .replace(".compact{font-size:24px", ".compact{font-size:38px")
                    .replace(".small{font-size:23px", ".small{font-size:36px")
                    .replace(".caption{font-size:24px", ".caption{font-size:32px")
                )
                (image_dir / f"{index:02d}-{name}{suffix}.svg").write_text(
                    svg, encoding="utf-8"
                )


HUB_UPDATES = {
    "articles/united-states/index.html": {
        "href": "/articles/us/remote-china-lawyer.html",
        "card": '<a href="/articles/us/remote-china-lawyer.html"><span class="v24-tag">遠程委託</span><strong>人在美國，可以委託內地律師處理繼承嗎</strong><p>先分清可遠程代辦的程序和仍由家屬作出的決定。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/united-states/index_cn.html": {
        "href": "/articles/us/remote-china-lawyer_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">远程委托</span><h3>人在美国，可以委托内地律师处理继承吗</h3><p>先分清可远程代办的程序和仍由家属作出的决定。</p></div><a class="v25-pill-action" href="/articles/us/remote-china-lawyer_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index_en.html": {
        "href": "/articles/us/remote-china-lawyer_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Remote authority</span><h3>Can a family handle a Mainland inheritance from the United States?</h3><p>Separate remote procedural work from the decisions the family must retain.</p></div><a class="v25-pill-action" href="/articles/us/remote-china-lawyer_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/macau/index.html": {
        "href": "/articles/am/unknown-mainland-property-city.html",
        "card": '<a href="/articles/am/unknown-mainland-property-city.html"><span class="v24-tag">房產線索</span><strong>只知道家人在內地有房，先怎樣找城市和地址線索</strong><p>先把房屋、付款、居住和通訊記錄整理成可核對的線索表。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/macau/index_cn.html": {
        "href": "/articles/am/unknown-mainland-property-city_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">房产线索</span><h3>只知道家人在内地有房，先怎样找城市和地址线索</h3><p>把房屋、付款、居住和通信记录整理成可以核对的线索表。</p></div><a class="v25-pill-action" href="/articles/am/unknown-mainland-property-city_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/macau/index_en.html": {
        "href": "/articles/am/unknown-mainland-property-city_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Property clues</span><h3>How to trace a Mainland property when the city is uncertain</h3><p>Turn property, payment, occupation and message records into a reliable clue sheet.</p></div><a class="v25-pill-action" href="/articles/am/unknown-mainland-property-city_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
}


MACAU_UPCOMING = {
    "articles/macau/index.html": (
        '<span>3 個方向</span></summary><div class="topic-upcoming-grid"><span>有遺囑時先核對哪些人和資產</span><span>不能回內地時授權範圍怎樣寫</span><span>只知道舊地址時怎樣找房產或存款線索</span>',
        '<span>2 個方向</span></summary><div class="topic-upcoming-grid"><span>有遺囑時先核對哪些人和資產</span><span>不能回內地時授權範圍怎樣寫</span>',
    ),
    "articles/macau/index_cn.html": (
        '<span>3 个方向</span></summary><div class="topic-upcoming-grid"><span>有遗嘱时先核对哪些人和资产</span><span>不能回内地时授权范围怎样写</span><span>只知道旧地址时怎样找房产或存款线索</span>',
        '<span>2 个方向</span></summary><div class="topic-upcoming-grid"><span>有遗嘱时先核对哪些人和资产</span><span>不能回内地时授权范围怎样写</span>',
    ),
    "articles/macau/index_en.html": (
        '<span>3 directions</span></summary><div class="topic-upcoming-grid"><span>What to check first when a will is found</span><span>Defining authority when no one can travel</span><span>Tracing property or accounts from an old address</span>',
        '<span>2 directions</span></summary><div class="topic-upcoming-grid"><span>What to check first when a will is found</span><span>Defining authority when no one can travel</span>',
    ),
}


def update_hubs() -> None:
    for relative_path, update in HUB_UPDATES.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if update["href"] not in text:
            if update["marker"] not in text:
                raise RuntimeError(f"Hub insertion marker missing: {relative_path}")
            text = text.replace(update["marker"], update["card"] + update["marker"], 1)
        if relative_path in MACAU_UPCOMING:
            old, new = MACAU_UPCOMING[relative_path]
            if old not in text and new not in text:
                raise RuntimeError(f"Macau upcoming marker missing: {relative_path}")
            text = text.replace(old, new, 1)
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
    for hub in ("macau", "united-states"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, f"{SITE}/articles/{hub}/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
