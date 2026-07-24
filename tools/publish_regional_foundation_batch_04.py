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
        "slug": "domicile-and-mainland-asset-location",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡與內地遺產",
                "title": "親人在新加坡離世，住所和內地資產所在地分別影響甚麼",
                "description": "親人在新加坡離世但留有內地資產時，怎樣分開確認逝者住所、新加坡遺產程序和內地資產所在地。",
                "lead": "先不要只記住「在新加坡離世」。把逝者在哪裏安頓長期生活，以及內地每項資產在哪個城市，分開寫成兩行。",
                "key_title": "先分開三件事",
                "keys": [
                    "離世地點不一定就是逝者的住所",
                    "住所會影響新加坡遺產程序怎樣開始",
                    "內地資產所在地決定另一組辦理問題",
                ],
                "visuals": [
                    (
                        "兩個地點回答兩個問題",
                        "住所：長期的家在哪裏",
                        "資產：房屋或賬戶在哪裏",
                        "不要用一個地址同時回答兩個問題。",
                    ),
                    (
                        "先釐清人，再對接資產",
                        "確認住所事實",
                        "整理代表文件",
                        "逐項核對內地資產",
                        "境外程序和內地辦理要前後銜接，但不能混為一件事。",
                    ),
                    (
                        "第一次先列四項",
                        "長期居所和生活安排",
                        "新加坡遺產程序資料",
                        "內地資產城市",
                        "登記姓名和共有狀態",
                        "先把事實列清楚，再決定需要哪一套文件。",
                    ),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "親人在新加坡離世，不代表他的住所一定在新加坡。這裏所說的住所，不是普通通訊地址，而是法律上認定的長期家園。離世地點、當時住址和住所可能不同；住所會影響新加坡的遺產程序由誰申請、要交甚麼資料，以及是否需要說明其他地方的法律和代表安排。",
                    "內地資產所在地則回答另一組問題：房屋在哪個城市登記、賬戶由哪家機構管理、公司在哪裏登記，以及當地接收甚麼文件。新加坡取得的遺產代表文件可以是重要材料，但不會自動把內地房屋、存款或股權轉到繼承人名下；它是否被接收、用於哪一步，仍要按資產所在地和具體用途核對。",
                ],
                "sections": [
                    (
                        "在新加坡離世，不等於住所一定在新加坡",
                        [
                            "住所不是看護照上的國籍，也不只看最後一張水電單。通常要綜合逝者長期住在哪裏、家庭和工作重心在哪裏、有沒有固定居所，以及他是否打算把那裏當作長期的家。住院、探親或短期工作期間離世，尤其不能只憑離世地址下結論。",
                            "家屬可以先做一頁時間線：近幾年在哪裏居住、每處住了多久、配偶或子女在哪裏、主要房屋和日常賬戶在哪裏。這張時間線不是用來自己作法律結論，而是讓處理遺產的人看見哪些事實需要核對。",
                        ],
                    ),
                    (
                        "住所先影響新加坡程序怎樣開始",
                        [
                            "新加坡的簡化網上遺產申請只適用於符合條件的個案，其中會看逝者是否以新加坡為住所。若逝者的住所其實在其他地方，申請人身份、所需證明和程序可能不同，有時還要交代住所地的遺產代表或法律資料。",
                            "有遺囑時，先找原件並確認遺囑指定誰處理遺產；沒有遺囑時，則要確認誰適合申請管理遺產。這一步處理的是誰能代表遺產和怎樣開始新加坡程序，不是直接判定內地每項資產最後歸誰。",
                        ],
                    ),
                    (
                        "內地資產所在地回答另一組問題",
                        [
                            "內地房屋要先記城市、登記人、共有狀態和產權資料；存款要記銀行名稱、已知賬號線索和開戶資料；公司權益要記公司名稱和登記地。不同資產面對的接收機構和核對重點並不一樣。",
                            "尤其是內地房屋，所在地會直接影響登記和材料核驗。家屬不宜把一份新加坡文件翻譯後就寄往所有地方。先問清楚當地準備辦理哪一步、需要該文件證明甚麼，再處理翻譯、核驗或補充材料，通常更省時間。",
                        ],
                    ),
                    (
                        "先做一張兩欄表，不要急着翻譯整套文件",
                        [
                            "左欄寫逝者的住所線索：長期居所、家庭和工作重心、遺囑、新加坡程序編號和遺產代表。右欄逐項寫內地資產：城市、登記姓名、共有情況、現有證明和準備辦理的事情。兩欄之間再標出哪份境外文件需要用於哪一項資產。",
                            "如果逝者長期往返多地、家屬對住所看法不同、原遺囑找不到，或內地資產登記姓名與新加坡文件不一致，先保留原始資料和不同人的說法。這些情況需要逐項判斷，不適合先套用一條固定路線。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡專題總覽"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "新加坡 Probate 和 Letters of Administration 有甚麼分別"),
                    ("/articles/singapore/mainland-property-inheritance.html", "新加坡家庭處理內地房產繼承先分清兩套文件"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list.html", "只有零散資料時，先做一張內地資產線索表"),
                ],
                "cta": "先列出逝者近幾年的居住安排、新加坡遺產程序資料，以及每項內地資產所在城市，再判斷兩邊文件怎樣銜接。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡与内地遗产",
                "title": "亲人在新加坡离世，住所和内地资产所在地分别影响什么",
                "description": "亲人在新加坡离世但留有内地资产时，怎样分别确认逝者住所、新加坡遗产程序和内地资产所在地。",
                "lead": "先不要只记住“在新加坡离世”。把逝者在哪里安顿长期生活，以及内地每项资产在哪个城市，分开写成两行。",
                "key_title": "先分开三件事",
                "keys": [
                    "离世地点不一定就是逝者的住所",
                    "住所会影响新加坡遗产程序怎样开始",
                    "内地资产所在地决定另一组办理问题",
                ],
                "visuals": [
                    ("两个地点回答两个问题", "住所：长期的家在哪里", "资产：房屋或账户在哪里", "不要用一个地址同时回答两个问题。"),
                    ("先厘清人，再对接资产", "确认住所事实", "整理代表文件", "逐项核对内地资产", "境外程序和内地办理要前后衔接，但不能混为一件事。"),
                    ("第一次先列四项", "长期居所和生活安排", "新加坡遗产程序资料", "内地资产城市", "登记姓名和共有状态", "先把事实列清楚，再决定需要哪一套文件。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "亲人在新加坡离世，不代表他的住所一定在新加坡。这里所说的住所，不是普通通信地址，而是法律上认定的长期家园。离世地点、当时住址和住所可能不同；住所会影响新加坡的遗产程序由谁申请、需要提交什么资料，以及是否需要说明其他地方的法律和代表安排。",
                    "内地资产所在地则回答另一组问题：房屋在哪个城市登记、账户由哪家机构管理、公司在哪里登记，以及当地接收什么文件。新加坡取得的遗产代表文件可以是重要材料，但不会自动把内地房屋、存款或股权转到继承人名下；它是否被接收、用于哪一步，仍要按资产所在地和具体用途核对。",
                ],
                "sections": [
                    (
                        "在新加坡离世，不等于住所一定在新加坡",
                        [
                            "住所不是看护照上的国籍，也不只看最后一张水电单。通常要综合逝者长期住在哪里、家庭和工作重心在哪里、有没有固定居所，以及他是否打算把那里当作长期的家。住院、探亲或短期工作期间离世，尤其不能只凭离世地址下结论。",
                            "家属可以先做一页时间线：近几年在哪里居住、每处住了多久、配偶或子女在哪里、主要房屋和日常账户在哪里。这张时间线不是用来自己作法律结论，而是让处理遗产的人看见哪些事实需要核对。",
                        ],
                    ),
                    (
                        "住所先影响新加坡程序怎样开始",
                        [
                            "新加坡的简化网上遗产申请只适用于符合条件的个案，其中会看逝者是否以新加坡为住所。如果逝者的住所其实在其他地方，申请人身份、所需证明和程序可能不同，有时还要说明住所地的遗产代表或法律资料。",
                            "有遗嘱时，先找原件并确认遗嘱指定谁处理遗产；没有遗嘱时，则要确认谁适合申请管理遗产。这一步处理的是谁能代表遗产和怎样开始新加坡程序，不是直接判定内地每项资产最后归谁。",
                        ],
                    ),
                    (
                        "内地资产所在地回答另一组问题",
                        [
                            "内地房屋要先记城市、登记人、共有状态和产权资料；存款要记银行名称、已知账号线索和开户资料；公司权益要记公司名称和登记地。不同资产面对的接收机构和核对重点并不一样。",
                            "尤其是内地房屋，所在地会直接影响登记和材料核验。家属不宜把一份新加坡文件翻译后就寄往所有地方。先问清楚当地准备办理哪一步、需要该文件证明什么，再处理翻译、核验或补充材料，通常更省时间。",
                        ],
                    ),
                    (
                        "先做一张两栏表，不要急着翻译整套文件",
                        [
                            "左栏写逝者的住所线索：长期居所、家庭和工作重心、遗嘱、新加坡程序编号和遗产代表。右栏逐项写内地资产：城市、登记姓名、共有情况、现有证明和准备办理的事项。两栏之间再标出哪份境外文件需要用于哪一项资产。",
                            "如果逝者长期往返多地、家属对住所看法不同、原遗嘱找不到，或内地资产登记姓名与新加坡文件不一致，先保留原始资料和不同人的说法。这些情况需要逐项判断，不适合先套用一条固定路线。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡专题总览"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "新加坡 Probate 和 Letters of Administration 有什么区别"),
                    ("/articles/singapore/mainland-property-inheritance_cn.html", "新加坡家庭处理内地房产继承先分清两套材料"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list_cn.html", "只有零散资料时，先做一张内地资产线索表"),
                ],
                "cta": "先列出逝者近几年的居住安排、新加坡遗产程序资料，以及每项内地资产所在城市，再判断两边文件怎样衔接。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore and a Mainland estate",
                "title": "A Death in Singapore and Assets in Mainland China: Why Location Matters Twice",
                "description": "How to separate domicile, the Singapore estate process and the location of each Mainland asset after a death in Singapore.",
                "lead": "“Died in Singapore” is not enough for the first fact sheet. Record where the person made a lasting home and where each Mainland asset is located as two separate answers.",
                "key_title": "Keep three points separate",
                "keys": [
                    "The place of death may not be the domicile",
                    "Domicile can change the Singapore probate route",
                    "The Mainland asset location raises a different set of questions",
                ],
                "visuals": [
                    ("Two places answer two questions", "Domicile: where was the lasting home?", "Asset: where is the property, account or company?", "Do not make one address answer both questions."),
                    ("Identify the representative, then match the asset", "Establish domicile facts", "Organise will or grant papers", "Check each Mainland asset", "The two processes connect, but they do not merge into one."),
                    ("Start with four entries", "Lasting home and life pattern", "Singapore estate file", "Mainland asset city", "Registered name and ownership", "Clarify the facts before preparing the full document set."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "A person who died in Singapore was not necessarily domiciled there. Domicile here means the legal connection to the place treated as a lasting home, not an ordinary mailing address. The place of death, current address and domicile can differ; domicile can affect who applies in Singapore, what evidence is required and whether a connection to another legal system must be explained.",
                    "The location of a Mainland asset answers a different question: which city holds the property record, which institution holds the account, where the company is registered and what the local recipient requires. A Singapore grant may be important evidence, but it does not transfer Mainland property, money or shares by itself. Its use still has to be checked with the recipient for the particular asset and step.",
                ],
                "sections": [
                    (
                        "A Singapore death does not prove a Singapore domicile",
                        [
                            "Domicile is not simply nationality or the address on the latest bill. The practical enquiry may include where the person lived over time, where family and work were centred, whether there was a settled home and whether that place was intended to remain home. A hospital, family visit or temporary assignment should not become the answer by default.",
                            "A useful first step is a one-page timeline showing each residence, how long it was used, where the immediate family lived and where the main home and everyday accounts were kept. The timeline is not a legal conclusion. It gives the estate adviser a clear set of facts to test.",
                        ],
                    ),
                    (
                        "Domicile affects how the Singapore file begins",
                        [
                            "Singapore's simplified online probate service is limited to qualifying cases and includes a Singapore-domicile condition. Where the deceased was domiciled elsewhere, the appropriate applicant, supporting evidence and procedure may differ. Evidence about the foreign domicile, law or estate representative may also be relevant.",
                            "If there is a will, locate the original and identify the person named to deal with the estate. If there is no will, identify who may apply to administer it. This work establishes representation and the starting route in Singapore; it does not decide ownership of every Mainland asset.",
                        ],
                    ),
                    (
                        "The Mainland asset location answers the next question",
                        [
                            "For a property, record the city, registered owner, co-ownership and title information. For money, record the bank and any reliable account clues. For a company interest, record the company name and registration place. Each asset may have a different recipient and a different evidential question.",
                            "The location of Mainland real estate is especially important to registration and document review. Do not translate and send the same Singapore bundle everywhere. Ask what step the local recipient is being asked to take and what fact each foreign document must prove before arranging translation or further verification.",
                        ],
                    ),
                    (
                        "Build a two-column sheet before translating the whole file",
                        [
                            "In the left column, list the domicile clues, family and work centre, will, Singapore file number and estate representative. In the right column, list each Mainland asset, city, registered name, ownership status and intended action. Then connect each foreign document to the particular asset for which it may be needed.",
                            "If the deceased lived across several places, family members disagree about the lasting home, the original will is missing or the Mainland registered name differs from the Singapore records, preserve the source documents and the different accounts. Those facts need individual review rather than a standard route chosen too early.",
                        ],
                    ),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore estate topic overview"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate or Letters of Administration in Singapore"),
                    ("/articles/singapore/mainland-property-inheritance_en.html", "Separating the Singapore estate file from the Mainland property file"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list_en.html", "Building a Mainland asset clue list from incomplete records"),
                ],
                "cta": "List the recent residence history, Singapore estate file and city of each Mainland asset before deciding how the two document sets should connect.",
            },
        },
    },
    {
        "slug": "domicile-and-mainland-asset-location",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國與內地遺產",
                "title": "親人在美國離世，住所州和內地資產所在地分別影響甚麼",
                "description": "親人在美國離世但留有內地資產時，怎樣分開確認住所州、美國遺產程序和內地資產所在地。",
                "lead": "先不要把死亡證明上的州當成全部答案。美國哪個州是逝者長期的家，以及內地資產在哪個城市，要分開核對。",
                "key_title": "先分開三件事",
                "keys": [
                    "離世州、郵寄地址和住所州可以不同",
                    "美國遺產程序要按相關州和縣核對",
                    "內地資產所在地決定另一組辦理步驟",
                ],
                "visuals": [
                    (
                        "兩個地點，兩套問題",
                        "住所州：主要的家在哪裏",
                        "資產：內地房屋在哪裏",
                        "死亡證明上的州不能代替完整判斷。",
                    ),
                    (
                        "把兩邊程序接起來",
                        "確認州和縣",
                        "取得遺產代表文件",
                        "逐項對接內地資產",
                        "美國代表身份是起點，不是內地資產已完成轉移。",
                    ),
                    (
                        "第一次先找四類資料",
                        "主要居所和返回意圖",
                        "州、縣和案件編號",
                        "遺產代表文件",
                        "內地資產城市和登記姓名",
                        "先核對位置和身份，再準備跨境文件。",
                    ),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "親人在美國哪一州離世，不一定代表那一州就是他的住所州。這裏的住所州，是法律上認定的主要、長期家園，不只是郵寄地址。若他在另一州保留主要居所、家人和生活重心，或者只是到離世州住院、探親，遺產程序應在哪裏開始，不能只看死亡地點。美國各州規則不同，具體還要核對相關州和縣。",
                    "內地資產所在地則影響房屋登記、銀行或公司資料核對，以及當地接收甚麼文件。美國法院任命的遺囑執行人或遺產管理人，並不因為已在美國取得代表身份，就自動有權完成內地房屋轉名或提取所有內地資產；任命文件能否用、用於哪一步，仍要按接收地和資產類型核對。",
                ],
                "sections": [
                    (
                        "離世州、現住址和住所州可能不同",
                        [
                            "住所州通常關心逝者把哪一州視為主要、長期的家，而不只是去世當天身在哪裏。可以先看長期居所、家人在哪裏、駕駛證和選民或稅務資料、主要賬戶，以及他離開後打算回到哪裏。任何單一資料都不一定能獨立作結論。",
                            "例如逝者長住紐約，最後在加州子女家附近接受治療；也可能在一州工作，卻一直保留另一州作為主要的家。家屬先把近幾年的居住和搬遷原因寫成時間線，通常比只交一張死亡證明更能說清問題。",
                        ],
                    ),
                    (
                        "美國程序要按相關州和縣核對",
                        [
                            "美國的遺囑認證和遺產管理主要由各州制度處理，提交到哪個法院、誰可申請、需要哪些表格，不能用一條全國統一答案概括。有些州會以逝者住所所在縣開始；若逝者住在外州但在當地有財產，還可能出現另一種當地程序。",
                            "因此，先記下州、縣、法院名稱、案件編號和法院任命的代表。不要只寫「已經辦了 probate」。內地接收方需要看的是哪個法院作出甚麼任命、文件是否生效，以及該文件準備用來證明甚麼。",
                        ],
                    ),
                    (
                        "內地資產所在地回答下一組問題",
                        [
                            "內地房屋要記城市、登記人、共有狀態和房產資料；存款要記銀行和可靠的賬戶線索；公司權益要記公司名稱和登記地。資產在哪裏，會影響向誰查詢、哪個部門核對，以及後續材料怎樣準備。",
                            "境外代表身份和內地資產權利是兩個層次。美國法院文件可以幫助說明誰代表遺產，但內地還要核對繼承人、遺囑、親屬關係、資產登記和當地辦理要求。不要把美國任命文件理解成一張可以直接完成內地過戶的通行證。",
                        ],
                    ),
                    (
                        "用兩欄表把美國文件和內地資產對上",
                        [
                            "左欄列住所州線索和美國案件：主要居所、居住時間線、州和縣、遺囑、代表姓名和任命文件。右欄列每項內地資產：城市、登記姓名、共有情況、現有線索和希望完成的事情。然後逐項標出哪份美國文件要交給哪個接收方。",
                            "若家屬對住所州有分歧、不同州同時有程序、內地登記姓名和英文文件對不上，或有人質疑遺囑和代表身份，先保留原件和法院進度。這些情況不適合為了趕快過戶而先選一個方便的州或自行拼接結論。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國專題總覽"),
                    ("/articles/us/us-documents-mainland-property-inheritance.html", "美國文件用於內地繼承，先分清哪份證明甚麼"),
                    ("/articles/us/issuing-state-matters.html", "美國文件先看由哪一級機關簽發"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list.html", "只有零散資料時，先做一張內地資產線索表"),
                ],
                "cta": "先列出逝者的住所州線索、美國州縣和代表文件，再按城市逐項整理內地資產，才能看清兩邊怎樣銜接。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国与内地遗产",
                "title": "亲人在美国离世，住所州和内地资产所在地分别影响什么",
                "description": "亲人在美国离世但留有内地资产时，怎样分别确认住所州、美国遗产程序和内地资产所在地。",
                "lead": "先不要把死亡证明上的州当成全部答案。美国哪个州是逝者长期的家，以及内地资产在哪个城市，需要分开核对。",
                "key_title": "先分开三件事",
                "keys": [
                    "离世州、邮寄地址和住所州可以不同",
                    "美国遗产程序要按相关州和县核对",
                    "内地资产所在地决定另一组办理步骤",
                ],
                "visuals": [
                    ("两个地点，两套问题", "住所州：主要的家在哪里", "资产：内地房屋在哪里", "死亡证明上的州不能代替完整判断。"),
                    ("把两边程序接起来", "确认州和县", "取得遗产代表文件", "逐项对接内地资产", "美国代表身份是起点，不是内地资产已经完成转移。"),
                    ("第一次先找四类资料", "主要居所和返回意图", "州、县和案件编号", "遗产代表文件", "内地资产城市和登记姓名", "先核对位置和身份，再准备跨境文件。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "亲人在美国哪一州离世，不一定代表那一州就是他的住所州。这里的住所州，是法律上认定的主要、长期家园，不只是邮寄地址。如果他在另一州保留主要居所、家人和生活重心，或者只是到离世州住院、探亲，遗产程序应在哪里开始，不能只看死亡地点。美国各州规则不同，具体还要核对相关州和县。",
                    "内地资产所在地则影响房屋登记、银行或公司资料核对，以及当地接收什么文件。美国法院任命的遗嘱执行人或遗产管理人，并不因为已经在美国取得代表身份，就自动有权完成内地房屋转名或提取所有内地资产；任命文件能否使用、用于哪一步，仍要按接收地和资产类型核对。",
                ],
                "sections": [
                    (
                        "离世州、现住址和住所州可能不同",
                        [
                            "住所州通常关注逝者把哪一州视为主要、长期的家，而不只是去世当天身在哪里。可以先看长期居所、家人在哪里、驾驶证和选民或税务资料、主要账户，以及他离开后打算回到哪里。任何单一资料都不一定能独立作结论。",
                            "例如逝者长期住在纽约，最后在加州子女家附近接受治疗；也可能在一州工作，却一直保留另一州作为主要的家。家属先把近几年的居住和搬迁原因写成时间线，通常比只交一张死亡证明更能说明问题。",
                        ],
                    ),
                    (
                        "美国程序要按相关州和县核对",
                        [
                            "美国的遗嘱认证和遗产管理主要由各州制度处理，提交到哪个法院、谁可以申请、需要哪些表格，不能用一条全国统一答案概括。有些州会从逝者住所所在县开始；如果逝者住在外州但在当地有财产，还可能出现另一种当地程序。",
                            "因此，先记下州、县、法院名称、案件编号和法院任命的代表。不要只写“已经办了 probate”。内地接收方需要看的是哪个法院作出什么任命、文件是否生效，以及该文件准备用来证明什么。",
                        ],
                    ),
                    (
                        "内地资产所在地回答下一组问题",
                        [
                            "内地房屋要记城市、登记人、共有状态和房产资料；存款要记银行和可靠的账户线索；公司权益要记公司名称和登记地。资产在哪里，会影响向谁查询、哪个部门核对，以及后续材料怎样准备。",
                            "境外代表身份和内地资产权利是两个层次。美国法院文件可以帮助说明谁代表遗产，但内地还要核对继承人、遗嘱、亲属关系、资产登记和当地办理要求。不要把美国任命文件理解成一张可以直接完成内地过户的通行证。",
                        ],
                    ),
                    (
                        "用两栏表把美国文件和内地资产对上",
                        [
                            "左栏列住所州线索和美国案件：主要居所、居住时间线、州和县、遗嘱、代表姓名和任命文件。右栏列每项内地资产：城市、登记姓名、共有情况、现有线索和希望完成的事项。然后逐项标出哪份美国文件要交给哪个接收方。",
                            "如果家属对住所州有分歧、不同州同时有程序、内地登记姓名和英文文件对不上，或有人质疑遗嘱和代表身份，先保留原件和法院进度。这些情况不适合为了尽快过户而先选一个方便的州或自行拼接结论。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国专题总览"),
                    ("/articles/us/us-documents-mainland-property-inheritance_cn.html", "美国文件用于内地继承，先分清哪份证明什么"),
                    ("/articles/us/issuing-state-matters_cn.html", "美国文件先看由哪一级机构签发"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list_cn.html", "只有零散资料时，先做一张内地资产线索表"),
                ],
                "cta": "先列出逝者的住所州线索、美国州县和代表文件，再按城市逐项整理内地资产，才能看清两边怎样衔接。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / United States and a Mainland estate",
                "title": "A U.S. Domicile and a Mainland China Asset: Two Locations, Two Questions",
                "description": "How to separate the U.S. domicile, state probate file and location of each Mainland asset after a death in the United States.",
                "lead": "The state on the death certificate is not the whole answer. Record the state treated as the person's lasting home and the Mainland city of each asset separately.",
                "key_title": "Keep three points separate",
                "keys": [
                    "State of death, mailing address and domicile can differ",
                    "Probate procedure must be checked by state and county",
                    "The Mainland asset location creates a separate workstream",
                ],
                "visuals": [
                    ("Two locations, two sets of questions", "Domicile: which state was the lasting home?", "Asset: where is the Mainland property, account or company?", "The state on a death record cannot answer both."),
                    ("Connect the two workstreams", "Confirm state and county", "Obtain representative papers", "Match each Mainland asset", "U.S. authority is a starting point, not a completed Mainland transfer."),
                    ("Start with four categories", "Primary home and intent to return", "State, county and case number", "Representative papers", "Mainland city and registered name", "Check location and authority before preparing the cross-border set."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "The state where a person died was not necessarily the state of domicile. Domicile here means the legal connection to the state treated as the main and lasting home, not simply a mailing address. A main home, family life and an intention to return may point to another state, especially where the person travelled for treatment or a visit. Because probate rules differ by state, the correct court and county cannot be chosen from the place of death alone.",
                    "The Mainland asset location raises a separate question about property records, bank or company information and the local recipient. An executor or administrator appointed by a U.S. court does not gain an automatic power to retitle Mainland property or collect every Mainland asset merely by holding the U.S. appointment. The receiving office must still confirm how the appointment can be used for that asset and step.",
                ],
                "sections": [
                    (
                        "State of death, current address and domicile may differ",
                        [
                            "Domicile usually concerns the state treated as the person's main and lasting home, not simply the place occupied on the date of death. Relevant facts may include the long-term home, where close family lived, driving, voting or tax records, the main accounts and where the person intended to return. No single item necessarily settles the question.",
                            "For example, someone may have lived in New York but received final treatment near a child in California. Another person may have worked in one state while retaining a different state as home. A timeline of residences and reasons for each move is more useful than treating the death certificate as a complete answer.",
                        ],
                    ),
                    (
                        "Check the U.S. procedure by state and county",
                        [
                            "Probate and estate administration in the United States are primarily state matters. The court, eligible applicant and forms cannot be reduced to one nationwide rule. A domicile county may be the starting point in one situation, while local property owned by an out-of-state resident may create another proceeding.",
                            "Record the state, county, court name, case number and appointed representative. “Probate completed” is too vague for cross-border use. A Mainland recipient needs to know which court made which appointment, whether the document is effective and what fact it is being offered to prove.",
                        ],
                    ),
                    (
                        "The Mainland asset location answers the next question",
                        [
                            "For real estate, record the city, registered owner, co-ownership and title information. For funds, record the bank and reliable account clues. For a company interest, record the company name and registration place. Location affects the recipient, available records and the next practical step.",
                            "Authority to represent the estate abroad and entitlement to a Mainland asset are different layers. The U.S. appointment can help establish representation, but the Mainland file may still need the heirship, will, family, asset and local registration evidence. A U.S. appointment is not a universal transfer order.",
                        ],
                    ),
                    (
                        "Use a two-column sheet to match the papers to the assets",
                        [
                            "In the left column, list the domicile clues and U.S. case: main home, residence timeline, state and county, will, representative and appointment. In the right column, list each Mainland asset, city, registered name, ownership status, available clue and intended action. Then mark which U.S. document is intended for each recipient.",
                            "If relatives disagree about domicile, proceedings exist in more than one state, the Mainland registered name does not match the English record, or the will or representative is challenged, preserve the original papers and court status. Do not select a convenient state or force a single conclusion merely to accelerate the transfer.",
                        ],
                    ),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/united-states/index_en.html", "United States estate topic overview"),
                    ("/articles/us/us-documents-mainland-property-inheritance_en.html", "What each U.S. estate document proves for a Mainland asset"),
                    ("/articles/us/issuing-state-matters_en.html", "Start with the U.S. authority that issued the document"),
                    ("/articles/hk-mainland-property-inheritance/asset-clue-list_en.html", "Building a Mainland asset clue list from incomplete records"),
                ],
                "cta": "List the domicile clues, U.S. state, county and representative papers, then organise each Mainland asset by city before connecting the two files.",
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
    "articles/singapore/index.html": {
        "href": "/articles/singapore/domicile-and-mainland-asset-location.html",
        "card": '<a href="/articles/singapore/domicile-and-mainland-asset-location.html"><span class="v24-tag">先分地點</span><strong>親人在新加坡離世，住所和內地資產所在地分別影響甚麼</strong><p>先把逝者長期的家和每項內地資產所在城市分開核對。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/singapore/index_cn.html": {
        "href": "/articles/singapore/domicile-and-mainland-asset-location_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">先分地点</span><h3>亲人在新加坡离世，住所和内地资产所在地分别影响什么</h3><p>先把逝者长期的家和每项内地资产所在城市分开核对。</p></div><a class="v25-pill-action" href="/articles/singapore/domicile-and-mainland-asset-location_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index_en.html": {
        "href": "/articles/singapore/domicile-and-mainland-asset-location_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Two locations</span><h3>A Singapore domicile and a Mainland asset answer different questions</h3><p>Separate the lasting home from the city of each Mainland asset before preparing documents.</p></div><a class="v25-pill-action" href="/articles/singapore/domicile-and-mainland-asset-location_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index.html": {
        "href": "/articles/us/domicile-and-mainland-asset-location.html",
        "card": '<a href="/articles/us/domicile-and-mainland-asset-location.html"><span class="v24-tag">先分地點</span><strong>親人在美國離世，住所州和內地資產所在地分別影響甚麼</strong><p>先分清住所州、美國案件所在州縣和內地資產城市。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/united-states/index_cn.html": {
        "href": "/articles/us/domicile-and-mainland-asset-location_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">先分地点</span><h3>亲人在美国离世，住所州和内地资产所在地分别影响什么</h3><p>先分清住所州、美国案件所在州县和内地资产城市。</p></div><a class="v25-pill-action" href="/articles/us/domicile-and-mainland-asset-location_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index_en.html": {
        "href": "/articles/us/domicile-and-mainland-asset-location_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Two locations</span><h3>A U.S. domicile and a Mainland asset answer different questions</h3><p>Separate the domicile state and county from the city of each Mainland asset.</p></div><a class="v25-pill-action" href="/articles/us/domicile-and-mainland-asset-location_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
}


def update_hubs() -> None:
    for relative_path, update in HUB_UPDATES.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if update["href"] in text:
            continue
        if update["marker"] not in text:
            raise RuntimeError(f"Hub insertion marker missing: {relative_path}")
        text = text.replace(update["marker"], update["card"] + update["marker"], 1)
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
