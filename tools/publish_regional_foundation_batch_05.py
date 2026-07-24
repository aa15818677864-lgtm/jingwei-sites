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
        "slug": "habitual-residence-and-mainland-assets",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_MO",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門與內地遺產",
                "title": "親人在澳門離世，常居地和內地資產所在地分別影響甚麼",
                "description": "親人在澳門離世並留有內地資產時，怎樣分開核對實際生活中心、澳門遺產安排和內地資產所在地。",
                "lead": "先不要把離世地點直接當成常居地。把逝者實際而固定的生活中心，以及每項內地資產所在城市，分開寫成兩欄。",
                "key_title": "先分清三件事",
                "keys": [
                    "在澳門離世，不等於常居地一定在澳門",
                    "常居地先影響澳門一邊的繼承與代表安排",
                    "內地資產所在地仍決定登記和接收問題",
                ],
                "visuals": [
                    ("兩個地點回答兩個問題", "常居地：固定生活中心", "資產地：房屋或賬戶城市", "不要讓離世地點代替兩項事實判斷。"),
                    ("先理清生活，再處理資產", "整理居住時間線", "確認代表文件", "逐項核對內地資產", "澳門文件和內地辦理要銜接，但回答的問題不同。"),
                    ("第一次先寫四項", "近年居住與生活重心", "家人工作及日常安排", "內地資產城市", "登記姓名和共有情況", "資料不完整也可以先列線索，不要急着下結論。"),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "親人在澳門離世，只能證明離世地點，不能單憑這一點認定常居地。澳門處理個人和繼承問題時，關心的是逝者實際而固定的生活中心：近年長期住在哪裏、家庭和日常生活重心在哪裏，以及多地往返的原因。身份證地址、通訊地址或住院地址都只是線索。",
                    "內地資產所在地回答另一組問題。房屋在哪個城市登記、賬戶由哪家機構管理、公司在哪裏登記，會影響接收材料和辦理方式。即使澳門一邊已確認誰可代表遺產，也不會自動完成內地房產轉名、存款提取或股權變更。",
                ],
                "sections": [
                    (
                        "離世地點、證件地址和常居地不是同一件事",
                        [
                            "常居地看的是實際而固定的生活中心，不是從一張證件直接抄答案。可以先記近三至五年的居住時間、主要住所、配偶和子女在哪裏、工作或退休生活在哪裏，以及日常醫療和賬戶通常在哪裏使用。不能只憑一張證件、一次住院或一個地址下結論。",
                            "如果逝者因住院、照顧家人、探親或短期工作留在澳門，尤其要保存到澳門的原因和原本生活安排。若長期在多地生活，也不要先刪掉看似矛盾的資料；把每段時間和用途寫清楚，讓處理遺產的人逐項核對。",
                        ],
                    ),
                    (
                        "常居地先影響澳門一邊怎樣開始",
                        [
                            "常居地是澳門一邊判斷繼承規則和遺產代表權限的起點。它不是一句『人在澳門離世』就能替代的結論，也不能取代內地資產所在地的登記要求。若家人對生活中心有不同看法，應先保留住所、家庭、工作和生活安排的原始資料。",
                            "有遺囑時，先找原件並記錄保管人；沒有遺囑時，先列配偶、子女、父母等家屬線索。這一層是為了看清澳門文件和代表安排，不是直接判定每項內地資產最後歸誰。",
                        ],
                    ),
                    (
                        "內地資產所在地仍要逐項核對",
                        [
                            "房產先寫城市、地址、登記姓名、共有情況和現有產權線索；存款先寫銀行名稱、分行或賬號線索；公司權益先寫公司名稱和登記地。不同資產面對不同接收機構，不能把同一套澳門文件寄往所有地方。",
                            "特別是內地房產，資產所在城市會影響登記和材料核驗。先問清楚準備辦哪一步、由誰接收、每份境外文件要證明甚麼，再處理翻譯或其他核驗，通常比先做整套文件更穩妥。",
                        ],
                    ),
                    (
                        "先做一張時間線和一張資產表",
                        [
                            "時間線只記事實：何時住在哪裏、為何遷居、家人和日常生活在哪裏。資產表逐項記內地城市、登記姓名、共有狀態、現有證明和目前卡點。兩張表之間再標出哪份澳門文件可能用於哪項資產。",
                            "若家屬失聯、對常居地有爭議、逝者姓名寫法不一致，或房產只剩舊地址，先保留原始文件和不同人的說法。這些情況需要個別判斷，不適合先套一條固定結論。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門繼承專題總覽"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門家屬繼承內地房產先分清兩套文件"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance.html", "澳門死亡紀錄用於內地房產繼承先核對哪五項"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list.html", "資料零散時先做內地資產線索表"),
                ],
                "cta": "先寫下逝者近年的實際生活安排和每項內地資產所在城市，再判斷澳門文件與內地辦理怎樣銜接。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门与内地遗产",
                "title": "亲人在澳门离世，常居地和内地资产所在地分别影响什么",
                "description": "亲人在澳门离世并留有内地资产时，怎样分别核对实际生活中心、澳门遗产安排和内地资产所在地。",
                "lead": "先不要把离世地点直接当成常居地。把逝者实际而固定的生活中心，以及每项内地资产所在城市，分开写成两栏。",
                "key_title": "先分清三件事",
                "keys": [
                    "在澳门离世，不等于常居地一定在澳门",
                    "常居地先影响澳门一边的继承与代表安排",
                    "内地资产所在地仍决定登记和接收问题",
                ],
                "visuals": [
                    ("两个地点回答两个问题", "常居地：固定生活中心", "资产地：房屋或账户城市", "不要让离世地点代替两项事实判断。"),
                    ("先理清生活，再处理资产", "整理居住时间线", "确认代表文件", "逐项核对内地资产", "澳门文件和内地办理要衔接，但回答的问题不同。"),
                    ("第一次先写四项", "近年居住与生活重心", "家人工作及日常安排", "内地资产城市", "登记姓名和共有情况", "资料不完整也可以先列线索，不要急着下结论。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "亲人在澳门离世，只能证明离世地点，不能单凭这一点认定常居地。澳门处理个人和继承问题时，关心的是逝者实际而固定的生活中心：近年长期住在哪里、家庭和日常生活重心在哪里，以及多地往返的原因。身份证地址、通信地址或住院地址都只是线索。",
                    "内地资产所在地回答另一组问题。房屋在哪个城市登记、账户由哪家机构管理、公司在哪里登记，会影响接收材料和办理方式。即使澳门一边已经确认谁可以代表遗产，也不会自动完成内地房产过户、存款提取或股权变更。",
                ],
                "sections": [
                    (
                        "离世地点、证件地址和常居地不是同一件事",
                        [
                            "常居地看的是实际而固定的生活中心，不是从一张证件直接抄答案。可以先记录近三至五年的居住时间、主要住所、配偶和子女在哪里、工作或退休生活在哪里，以及日常医疗和账户通常在哪里使用。不能只凭一张证件、一次住院或一个地址下结论。",
                            "如果逝者因住院、照顾家人、探亲或短期工作留在澳门，尤其要保存到澳门的原因和原本生活安排。若长期在多地生活，也不要先删除看似矛盾的资料；把每段时间和用途写清楚，让处理遗产的人逐项核对。",
                        ],
                    ),
                    (
                        "常居地先影响澳门一边怎样开始",
                        [
                            "常居地是澳门一边判断继承规则和遗产代表权限的起点。它不是一句‘在澳门离世’就能替代的结论，也不能取代内地资产所在地的登记要求。如果家人对生活中心有不同看法，应先保留住所、家庭、工作和生活安排的原始资料。",
                            "有遗嘱时，先找原件并记录保管人；没有遗嘱时，先列配偶、子女、父母等家属线索。这一层是为了看清澳门文件和代表安排，不是直接判定每项内地资产最后归谁。",
                        ],
                    ),
                    (
                        "内地资产所在地仍要逐项核对",
                        [
                            "房产先写城市、地址、登记姓名、共有情况和现有产权线索；存款先写银行名称、分行或账号线索；公司权益先写公司名称和登记地。不同资产面对不同接收机构，不能把同一套澳门文件寄往所有地方。",
                            "特别是内地房产，资产所在城市会影响登记和材料核验。先问清楚准备办理哪一步、由谁接收、每份境外文件要证明什么，再处理翻译或其他核验，通常比先做整套文件更稳妥。",
                        ],
                    ),
                    (
                        "先做一张时间线和一张资产表",
                        [
                            "时间线只记录事实：何时住在哪里、为什么迁居、家人和日常生活在哪里。资产表逐项记录内地城市、登记姓名、共有状态、现有证明和当前卡点。两张表之间再标出哪份澳门文件可能用于哪项资产。",
                            "如果家属失联、对常居地有争议、逝者姓名写法不一致，或房产只剩旧地址，先保留原始文件和不同人的说法。这些情况需要个别判断，不适合先套一条固定结论。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门继承专题总览"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门家属继承内地房产先分清两套材料"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_cn.html", "澳门死亡记录用于内地房产继承先核对哪五项"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list_cn.html", "资料零散时先做内地资产线索表"),
                ],
                "cta": "先写下逝者近年的实际生活安排和每项内地资产所在城市，再判断澳门文件与内地办理怎样衔接。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau and a Mainland estate",
                "title": "A Death in Macau and Assets in Mainland China: Why Two Locations Matter",
                "description": "How to separate habitual residence, the Macau estate file and the location of each Mainland asset after a death in Macau.",
                "lead": "Do not treat the place of death as the habitual residence. Record the person's actual, settled centre of life and the city of each Mainland asset as two separate facts.",
                "key_title": "Keep three points separate",
                "keys": [
                    "A death in Macau does not prove habitual residence there",
                    "Habitual residence first affects the Macau estate analysis",
                    "The Mainland asset location still controls local handling",
                ],
                "visuals": [
                    ("Two locations answer two questions", "Habitual residence: settled life centre", "Asset location: property or account city", "The place of death cannot replace either factual enquiry."),
                    ("Clarify the life pattern before the asset route", "Build a residence timeline", "Identify estate authority", "Check each Mainland asset", "The Macau and Mainland files connect, but they answer different questions."),
                    ("Start with four facts", "Recent homes and life centre", "Family work and daily routine", "Mainland asset city", "Registered name and co-ownership", "Record the clues before drawing a legal conclusion."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "A death in Macau proves the place of death, not the habitual residence. The relevant starting point in Macau is the person's actual and settled centre of life: where the person lived over time, where family and daily life were centred, and why the person moved between places. An identity-card address, mailing address or hospital address is evidence, but not the entire answer.",
                    "The location of a Mainland asset answers a separate set of questions. The city of the property, the institution holding an account or the place where a company is registered affects who receives the papers and what must be shown. Macau estate authority does not by itself transfer a Mainland property, release an account or change a shareholding.",
                ],
                "sections": [
                    (
                        "The place of death, a document address and habitual residence can differ",
                        [
                            "Habitual residence concerns the actual and settled centre of life. A practical first record should cover the last three to five years: each home, how long it was used, where the spouse and children lived, where work or retirement life was based, and where ordinary healthcare and accounts were used. Do not draw the conclusion from one identity document, one hospital stay or one address.",
                            "If the person was in Macau for hospital care, family support, a visit or a temporary assignment, keep the reason for that stay and the earlier living arrangements. Where several places were used over time, preserve the apparent contradictions and explain the purpose of each stay instead of choosing an answer too early.",
                        ],
                    ),
                    (
                        "Habitual residence first shapes the Macau side of the file",
                        [
                            "Habitual residence is the Macau starting point for the law governing succession and the authority of the person managing or representing the estate. It cannot be replaced by the phrase 'died in Macau', and it does not displace the registration requirements where a Mainland asset is located. If family members disagree, retain the original housing, family, work and daily-life records for proper review.",
                            "Where a will exists, locate the original and record who holds it. Where there is no will, list the spouse, children, parents and any earlier deaths in the family. This step clarifies the Macau estate and representative file; it does not decide the final ownership of every Mainland asset.",
                        ],
                    ),
                    (
                        "The location of each Mainland asset still matters",
                        [
                            "For a property, record the city, address, registered name, co-ownership and title clues. For money, record the bank and any reliable branch or account clue. For a company interest, record the company name and registration place. Different recipients will ask different questions, so one Macau bundle should not be sent everywhere.",
                            "For Mainland real estate in particular, the asset city matters to registration and document review. Ask what step is proposed, who will receive the papers and what each overseas document must prove before arranging translation or further verification.",
                        ],
                    ),
                    (
                        "Build one timeline and one asset sheet",
                        [
                            "The timeline should state facts only: when and why the person lived in each place, and where family and ordinary life were based. The asset sheet should list each Mainland city, registered name, co-ownership, available record and current obstacle. Then link each Macau document to the particular asset for which it may be needed.",
                            "If relatives cannot be contacted, the habitual residence is disputed, names differ across records or only an old property address remains, preserve the source documents and the different accounts. Those cases need individual assessment rather than a standard conclusion.",
                        ],
                    ),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau estate topic overview"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Separating the Macau family file from the Mainland property file"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_en.html", "Checking a Macau death record before Mainland use"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list_en.html", "Building a Mainland asset clue list from incomplete records"),
                ],
                "cta": "List the recent living arrangements and the city of each Mainland asset before deciding how the Macau and Mainland files should connect.",
            },
        },
    },
    {
        "slug": "mainland-property-in-schedule-of-assets",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡資產清單",
                "title": "內地房產有沒有列入新加坡 Schedule of Assets，先核對哪四項",
                "description": "核對新加坡遺產資產清單是否列入內地房產、應看哪一欄，以及發現遺漏後怎樣分清補正與內地過戶。",
                "lead": "先找 Schedule of Assets 的境外財產部分，不要只看新加坡本地資產，也不要憑記憶補房屋地址或估值。",
                "key_title": "先問四個問題",
                "keys": [
                    "逝者離世時是否以新加坡為住所",
                    "內地房產是否列在境外財產部分",
                    "地址、登記姓名和估值是否有依據",
                    "清單已提交，還是法院 grant 已經發出",
                ],
                "visuals": [
                    ("先找對資產清單欄目", "新加坡境內財產", "新加坡境外財產", "內地房產通常要在境外財產部分核對。"),
                    ("發現遺漏後先看進度", "核對清單內容", "確認提交階段", "按程序補正", "不要直接改動已封存或附於 grant 的文件。"),
                    ("核對內地房產四項", "逝者住所", "城市地址", "登記姓名及份額", "清單和 grant 狀態", "資產清單是遺產申報文件，不是內地房產證明。"),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "Schedule of Assets 是新加坡遺產程序中的資產清單。現行表格把新加坡境內財產和境外財產分開；逝者離世時以新加坡為住所的個案，內地房產應在境外財產部分核對。先確認清單版本和逝者住所，再看房屋城市、地址、登記姓名、持有份額及離世時估值是否準確。",
                    "這份清單用來申報遺產，並不等於內地房產證明，也不會完成內地過戶。若發現遺漏，先看清單和 grant（法院發出的遺產代表文件）進行到哪一步。清單已提交時，需要用修訂清單和補充宣誓文件說明原因；grant 已發出時，還要申請把正式修訂清單附於 grant。不要自行改動封存文件。",
                ],
                "sections": [
                    (
                        "第一步不是找地址，而是找對欄目",
                        [
                            "現行資產清單先列新加坡境內財產，另設境外財產部分。境外部分有一個重要前提：它針對離世時以新加坡為住所的逝者。家屬不要只因在新加坡申請 grant，就直接假定這個前提已經成立。",
                            "找到境外部分後，再核對內地房產是否逐項列出。若只有『中國房產』四個字，往往不足以辨認具體資產；至少要回到現有產權、購房、按揭、管理費或地址資料，核對城市、房屋線索和登記姓名。",
                        ],
                    ),
                    (
                        "地址、登記姓名、份額和估值要有來源",
                        [
                            "地址應盡量與可靠房產資料一致，姓名要留意中文、英文或拼音差異，共有房產還要記逝者持有的方式和份額。若只知道小區或舊地址，可以先標示待核實，不宜為了填表而猜一個完整地址。",
                            "資產清單要求填報離世時的價值。估值未完成時，應保留估值日期、來源和假設；法院程序本身也容許在需要估值時再處理。不要把今日市價、購房價和離世時價值混在一起。",
                        ],
                    ),
                    (
                        "遺漏房產時，先分清清單進度",
                        [
                            "如果最初申請和首份確認申請資料的宣誓文件都沒有附上資產清單，可以之後提交清單，再以補充宣誓文件對清單真實準確作書面確認。若已提交但資料需要增加或修正，可以提交修訂清單，說明改了甚麼、為何需要修改，並以補充宣誓文件確認內容。",
                            "如果 grant 已經發出，處理方式再多一步：要申請提取正式的修訂資產清單，附於原有 grant。這不是在 PDF 上改字，也不應自行拼接新舊頁面。實際提交方式會因是否有律師代表而不同。",
                        ],
                    ),
                    (
                        "清單列了房產，也不等於內地已可過戶",
                        [
                            "Schedule of Assets 主要讓新加坡法院和相關人士看見遺產範圍與價值。它不代替內地的房產登記資料，也不單獨證明誰是繼承人、房屋最後歸誰或當地已接受境外文件。",
                            "完成清單核對後，另做一份內地房產辦理表：城市、登記姓名、共有情況、遺囑或家屬資料、現有 grant，以及準備向哪個接收機構辦甚麼事情。把兩份表分開，反而更容易找出真正缺的資料。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡繼承專題總覽"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "有遺囑和無遺囑時法院文件有甚麼不同"),
                    ("/articles/singapore/domicile-and-mainland-asset-location.html", "住所和內地資產所在地分別影響甚麼"),
                    ("/articles/singapore/mainland-property-inheritance.html", "新加坡遺產文件可否直接辦內地房產過戶"),
                ],
                "cta": "先確認逝者住所、資產清單欄目、房屋資料來源，以及清單和 grant 的進度，再決定是否需要補正。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡资产清单",
                "title": "内地房产有没有列入新加坡 Schedule of Assets，先核对哪四项",
                "description": "核对新加坡遗产资产清单是否列入内地房产、应看哪一栏，以及发现遗漏后怎样区分补正与内地过户。",
                "lead": "先找 Schedule of Assets 的境外财产部分，不要只看新加坡本地资产，也不要凭记忆补房屋地址或估值。",
                "key_title": "先问四个问题",
                "keys": [
                    "逝者离世时是否以新加坡为住所",
                    "内地房产是否列在境外财产部分",
                    "地址、登记姓名和估值是否有依据",
                    "清单已提交，还是法院 grant 已经发出",
                ],
                "visuals": [
                    ("先找对资产清单栏目", "新加坡境内财产", "新加坡境外财产", "内地房产通常要在境外财产部分核对。"),
                    ("发现遗漏后先看进度", "核对清单内容", "确认提交阶段", "按程序补正", "不要直接改动已封存或附于 grant 的文件。"),
                    ("核对内地房产四项", "逝者住所", "城市地址", "登记姓名及份额", "清单和 grant 状态", "资产清单是遗产申报文件，不是内地房产证明。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "Schedule of Assets 是新加坡遗产程序中的资产清单。现行表格把新加坡境内财产和境外财产分开；逝者离世时以新加坡为住所的案件，内地房产应在境外财产部分核对。先确认清单版本和逝者住所，再看房屋城市、地址、登记姓名、持有份额及离世时估值是否准确。",
                    "这份清单用于申报遗产，并不等于内地房产证明，也不会完成内地过户。如果发现遗漏，先看清单和 grant（法院发出的遗产代表文件）进行到哪一步。清单已经提交时，需要用修订清单和补充宣誓文件说明原因；grant 已经发出时，还要申请把正式修订清单附于 grant。不要自行改动封存文件。",
                ],
                "sections": [
                    (
                        "第一步不是找地址，而是找对栏目",
                        [
                            "现行资产清单先列新加坡境内财产，另设境外财产部分。境外部分有一个重要前提：它针对离世时以新加坡为住所的逝者。家属不要只因为在新加坡申请 grant，就直接假定这个前提已经成立。",
                            "找到境外部分后，再核对内地房产是否逐项列出。如果只有‘中国房产’四个字，往往不足以辨认具体资产；至少要回到现有产权、购房、按揭、管理费或地址资料，核对城市、房屋线索和登记姓名。",
                        ],
                    ),
                    (
                        "地址、登记姓名、份额和估值要有来源",
                        [
                            "地址应尽量与可靠房产资料一致，姓名要留意中文、英文或拼音差异，共有房产还要记录逝者持有的方式和份额。如果只知道小区或旧地址，可以先标注待核实，不要为了填表而猜一个完整地址。",
                            "资产清单要求填报离世时的价值。估值没有完成时，应保留估值日期、来源和假设；法院程序本身也允许在需要估值时再处理。不要把今日市价、购房价和离世时价值混在一起。",
                        ],
                    ),
                    (
                        "遗漏房产时，先分清清单进度",
                        [
                            "如果最初申请和第一份用于确认申请资料的宣誓文件都没有附上资产清单，可以之后提交清单，再用补充宣誓文件对清单真实准确作书面确认。如果已经提交但资料需要增加或修正，可以提交修订清单，说明改了什么、为什么需要修改，并以补充宣誓文件确认内容。",
                            "如果 grant 已经发出，处理方式再多一步：要申请提取正式的修订资产清单，附于原有 grant。这不是在 PDF 上改字，也不应自行拼接新旧页面。实际提交方式会因是否有律师代表而不同。",
                        ],
                    ),
                    (
                        "清单列了房产，也不等于内地已经可以过户",
                        [
                            "Schedule of Assets 主要让新加坡法院和相关人士看到遗产范围与价值。它不代替内地房产登记资料，也不单独证明谁是继承人、房屋最后归谁或当地已经接受境外文件。",
                            "完成清单核对后，另做一份内地房产办理表：城市、登记姓名、共有情况、遗嘱或家属资料、现有 grant，以及准备向哪个接收机构办理什么事情。把两份表分开，反而更容易找出真正缺的资料。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡继承专题总览"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "有遗嘱和无遗嘱时法院文件有什么不同"),
                    ("/articles/singapore/domicile-and-mainland-asset-location_cn.html", "住所和内地资产所在地分别影响什么"),
                    ("/articles/singapore/mainland-property-inheritance_cn.html", "新加坡遗产文件能否直接办理内地房产过户"),
                ],
                "cta": "先确认逝者住所、资产清单栏目、房屋资料来源，以及清单和 grant 的进度，再决定是否需要补正。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore Schedule of Assets",
                "title": "Is the Mainland Property Listed in the Singapore Schedule of Assets?",
                "description": "How to check whether a Mainland property appears in a Singapore Schedule of Assets, and what changes when the schedule or grant has already been issued.",
                "lead": "Start with the overseas-property section of the Schedule of Assets. Do not search only the Singapore assets or fill a property address and value from memory.",
                "key_title": "Ask four questions first",
                "keys": [
                    "Was the deceased domiciled in Singapore at death?",
                    "Is the property in the overseas-property section?",
                    "Are the address, ownership and value supported?",
                    "Was the schedule filed, or has the grant issued?",
                ],
                "visuals": [
                    ("Find the correct section first", "Property in Singapore", "Property outside Singapore", "A Mainland property should be checked in the overseas-property section."),
                    ("If an asset is missing, check the filing stage", "Review the schedule", "Confirm the filing stage", "Use the amendment route", "Do not edit a sealed schedule or a document attached to a grant."),
                    ("Check four property facts", "Singapore domicile", "City and address", "Registered name and share", "Schedule and grant status", "The asset schedule is not proof of Mainland title."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "The Schedule of Assets is the estate asset list used in Singapore probate and administration. The current form separates property in Singapore from property outside Singapore. For a person domiciled in Singapore at death, a Mainland property should be checked in the overseas-property section. Confirm the form, domicile, city, address, registered name, ownership share and value at death.",
                    "The schedule declares estate assets. It is not a Mainland title record and does not transfer the property. If an asset is missing, first identify the filing stage. An amended schedule and supplementary affidavit are used to explain a correction; if the grant has already issued, a formal engrossed amended schedule must also be extracted for attachment to the grant. Do not edit sealed documents yourself.",
                ],
                "sections": [
                    (
                        "Find the correct section before searching for the address",
                        [
                            "The current form has separate sections for property in Singapore and property outside Singapore. The overseas section carries an important condition: it applies where the deceased was domiciled in Singapore at death. A Singapore grant application should not be treated as proof that this domicile condition is satisfied.",
                            "Once the correct section is found, check whether each Mainland property is identifiable. A line saying only 'property in China' may not be enough. Return to reliable title, purchase, mortgage, management-fee or address records to confirm the city, property clue and registered name.",
                        ],
                    ),
                    (
                        "The address, ownership and value need a source",
                        [
                            "Match the address to reliable property records where possible. Check differences between Chinese names, English names and romanisation, and record how the deceased held any co-owned property. If only an estate name or old address is known, mark it for verification instead of inventing a complete address.",
                            "The schedule calls for the value at death. Keep the valuation date, source and assumptions. A current market estimate, the original purchase price and the value at death are not interchangeable. If a valuation is still needed, record that clearly rather than presenting an unsupported figure as final.",
                        ],
                    ),
                    (
                        "If the property is missing, identify the filing stage",
                        [
                            "Where no schedule was filed with the initial application and first supporting affidavit, the schedule may be filed later and its accuracy confirmed by a supplementary affidavit. Where a filed schedule needs a new asset or correction, an amended schedule can be filed with a supplementary affidavit stating what changed, why the amendment is needed and confirming the schedule's accuracy.",
                            "If the grant has already issued, there is an additional step: request an engrossed amended schedule for attachment to the grant. This is not a handwritten edit to a PDF or a replacement page assembled at home. The practical filing channel differs depending on whether a lawyer acts.",
                        ],
                    ),
                    (
                        "A listed property is not yet a Mainland transfer",
                        [
                            "The Schedule of Assets helps the Singapore court, beneficiaries and creditors understand the estate and its value. It does not replace the Mainland title record or prove on its own who inherits, how the property should be divided or whether a local recipient accepts the overseas papers.",
                            "After checking the schedule, make a separate Mainland property sheet: city, registered name, co-ownership, will or family records, existing grant, intended recipient and proposed step. Keeping the two sheets separate makes the real missing evidence easier to see.",
                        ],
                    ),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore estate topic overview"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Which Singapore grant applies with or without a will"),
                    ("/articles/singapore/domicile-and-mainland-asset-location_en.html", "Why domicile and the Mainland asset location answer different questions"),
                    ("/articles/singapore/mainland-property-inheritance_en.html", "Can a Singapore grant transfer Mainland property?"),
                ],
                "cta": "Confirm domicile, the correct schedule section, the source of the property details and the filing stage before deciding whether an amendment is needed.",
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
                    svg.replace(".item{font-size:29px", ".item{font-size:34px")
                    .replace(".compact{font-size:24px", ".compact{font-size:30px")
                    .replace(".small{font-size:23px", ".small{font-size:29px")
                    .replace(".caption{font-size:24px", ".caption{font-size:26px")
                )
                (image_dir / f"{index:02d}-{name}{suffix}.svg").write_text(svg, encoding="utf-8")


HUB_UPDATES = {
    "articles/macau/index.html": {
        "href": "/articles/am/habitual-residence-and-mainland-assets.html",
        "card": '<a href="/articles/am/habitual-residence-and-mainland-assets.html"><span class="v24-tag">先分地點</span><strong>親人在澳門離世，常居地和內地資產所在地分別影響甚麼</strong><p>先分開實際生活中心和每項內地資產所在城市。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/macau/index_cn.html": {
        "href": "/articles/am/habitual-residence-and-mainland-assets_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">先分地点</span><h3>亲人在澳门离世，常居地和内地资产所在地分别影响什么</h3><p>先分开实际生活中心和每项内地资产所在城市。</p></div><a class="v25-pill-action" href="/articles/am/habitual-residence-and-mainland-assets_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/macau/index_en.html": {
        "href": "/articles/am/habitual-residence-and-mainland-assets_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Two locations</span><h3>A Macau habitual residence and a Mainland asset answer different questions</h3><p>Separate the settled centre of life from the city of each Mainland asset.</p></div><a class="v25-pill-action" href="/articles/am/habitual-residence-and-mainland-assets_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index.html": {
        "href": "/articles/singapore/mainland-property-in-schedule-of-assets.html",
        "card": '<a href="/articles/singapore/mainland-property-in-schedule-of-assets.html"><span class="v24-tag">資產清單</span><strong>內地房產有沒有列入新加坡 Schedule of Assets，先核對哪四項</strong><p>先找境外財產部分，再核對房屋資料和清單進度。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/singapore/index_cn.html": {
        "href": "/articles/singapore/mainland-property-in-schedule-of-assets_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">资产清单</span><h3>内地房产有没有列入新加坡 Schedule of Assets，先核对哪四项</h3><p>先找境外财产部分，再核对房屋资料和清单进度。</p></div><a class="v25-pill-action" href="/articles/singapore/mainland-property-in-schedule-of-assets_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index_en.html": {
        "href": "/articles/singapore/mainland-property-in-schedule-of-assets_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Asset schedule</span><h3>Is the Mainland property listed in the Singapore Schedule of Assets?</h3><p>Find the overseas-property section, then check the property details and filing stage.</p></div><a class="v25-pill-action" href="/articles/singapore/mainland-property-in-schedule-of-assets_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
}


SINGAPORE_UPCOMING = {
    "articles/singapore/index.html": (
        '<span>4 個方向</span></summary><div class="topic-upcoming-grid"><span>Schedule of Assets 沒列內地房產怎樣補</span>',
        '<span>3 個方向</span></summary><div class="topic-upcoming-grid">',
    ),
    "articles/singapore/index_cn.html": (
        '<span>4 个方向</span></summary><div class="topic-upcoming-grid"><span>资产清单没有列内地房产怎样补</span>',
        '<span>3 个方向</span></summary><div class="topic-upcoming-grid">',
    ),
    "articles/singapore/index_en.html": (
        '<span>4 directions</span></summary><div class="topic-upcoming-grid"><span>Adding a Mainland property missing from the asset schedule</span>',
        '<span>3 directions</span></summary><div class="topic-upcoming-grid">',
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
        if relative_path in SINGAPORE_UPCOMING:
            old, new = SINGAPORE_UPCOMING[relative_path]
            if old in text:
                text = text.replace(old, new, 1)
        path.write_text(text, encoding="utf-8")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    blocks = []
    for article in ARTICLES:
        for lang in ("tc", "cn", "en"):
            url = SITE + article_path(article, lang)
            if f"<loc>{url}</loc>" in text:
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
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
