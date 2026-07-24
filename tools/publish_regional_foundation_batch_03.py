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
        "slug": "macau-kinship-certificate-scope",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門親屬文件",
                "title": "澳門親屬關係文件用於內地繼承，能證明甚麼",
                "description": "澳門家屬處理內地遺產時，怎樣用出生、婚姻、死亡和身份文件串起親屬關係，以及這些文件不能代替甚麼。",
                "lead": "通常不是找一張叫做「親屬關係證明」的文件，而是用幾份紀錄，把逝者與每名家屬逐段連起來。",
                "key_title": "先記住三件事",
                "keys": [
                    "每份紀錄只證明其中一段關係",
                    "姓名、日期和身份資料要前後銜接",
                    "親屬關係不等於已確定繼承份額",
                ],
                "visuals": [
                    (
                        "親屬關係要逐段證明",
                        "出生、婚姻或收養紀錄",
                        "死亡、身份或姓名紀錄",
                        "幾份文件接在一起，才看得出完整關係。",
                    ),
                    (
                        "由家屬關係走到內地遺產",
                        "畫出家屬關係",
                        "核對遺囑與繼承安排",
                        "對接內地資產",
                        "關係證據只是整個辦理路徑的一部分。",
                    ),
                    (
                        "第一次整理四欄",
                        "要證明哪段關係",
                        "文件及簽發資料",
                        "姓名日期差異",
                        "內地資產與用途",
                        "先找缺口，再申領或補充文件。",
                    ),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "澳門家屬處理內地繼承時，出生紀錄可以連接父母與子女，婚姻紀錄可以說明婚姻關係，死亡紀錄可以交代某名家屬已去世，身份和姓名紀錄則用來確認幾份文件說的是同一個人。多數家庭需要的是一條證明鏈，不是一張包辦全部關係的證明。",
                    "這條證明鏈仍不會自動決定誰取得哪項內地資產，也不能代替遺囑、繼承人資格文件或房產、賬戶本身的資料。先列清楚要證明哪一段關係，再找對應紀錄，通常比先問「辦哪一張親屬證明」更有效。",
                ],
                "sections": [
                    (
                        "先把家庭畫成一張簡單關係圖",
                        [
                            "從逝者開始，列出配偶、子女、父母，以及已先去世的家屬。每一條連線旁邊寫上可以支持它的紀錄，例如出生、婚姻、收養、死亡或姓名變更資料。這樣很快就會看到哪一段已有文件，哪一段仍然空白。",
                            "再婚、收養、家屬在不同地方出生或同一人曾使用不同姓名時，不要用口頭稱呼代替正式關係。把每種姓名、日期和證件號碼原樣抄下，標明它出現在哪一份文件上。",
                        ],
                    ),
                    (
                        "每份文件回答的問題都有限",
                        [
                            "出生紀錄通常用來說明父母與子女，婚姻紀錄說明婚姻事實，死亡紀錄說明死亡，身份資料用來把姓名和本人連起來。某一份紀錄沒有列出其他家屬，不代表那些家屬不存在；它可能本來就不是用來提供完整家屬名單。",
                            "因此，看到一份文件上有父母或配偶姓名時，不要直接把它當成全部繼承人名單。還要看家屬結構、是否有人先去世、是否有遺囑，以及辦理時真正需要確認的是哪一層關係。",
                        ],
                    ),
                    (
                        "證明誰是家屬，仍不等於分好遺產",
                        [
                            "全體繼承人均已成年、能自行處理而且沒有爭議時，澳門用來確認誰具有繼承身份的安排，仍會按家庭情況要求死亡、婚姻、出生、身份和遺囑等不同資料。這正好說明，繼承身份通常來自一組互相銜接的證據，而不是單憑其中一張紀錄。",
                            "即使家屬關係已經清楚，內地房產、存款或股權仍要另查登記人、共有狀況、賬戶或公司資料，以及當地接收文件的要求。關係證據回答「人怎樣連起來」，資產資料回答「遺產是甚麼」，兩邊不能互相代替。",
                        ],
                    ),
                    (
                        "有爭議或資料缺失時，先不要硬補結論",
                        [
                            "如果家屬對關係或遺囑有爭議、有人失聯、繼承人包括未成年人或需要協助作決定的人，或關鍵紀錄確實無法取得，普通的無爭議整理方式未必合適。先保留現有文件和不同家屬的說法，再判斷要補資料還是處理爭議。",
                            "現在可以先做一頁表：第一欄寫要證明的兩個人，第二欄寫現有文件，第三欄圈出姓名和日期差異，第四欄寫內地哪個城市、哪項資產、哪一步要使用。接收方看到這張表，才容易指出真正缺的是哪一段。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門專題總覽"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance.html", "澳門死亡紀錄用於內地繼承先核對甚麼"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門家屬繼承內地房產，先分清兩套文件"),
                    ("/articles/hk-mainland-property-inheritance/family-relationship-evidence.html", "對照閱讀：家屬關係資料怎樣接成證明鏈"),
                ],
                "cta": "把逝者、家屬關係、現有澳門文件和內地資產城市列清楚，再判斷缺的是哪一段證據。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门亲属材料",
                "title": "澳门亲属关系材料用于内地继承，能证明什么",
                "description": "澳门家属处理内地遗产时，怎样用出生、婚姻、死亡和身份材料连接亲属关系，以及这些材料不能代替什么。",
                "lead": "通常不是找一张叫“亲属关系证明”的材料，而是用几份记录，把逝者和每位家属一段一段连起来。",
                "key_title": "先记住三件事",
                "keys": [
                    "每份记录只证明其中一段关系",
                    "姓名、日期和身份信息要前后衔接",
                    "亲属关系不等于已经确定继承份额",
                ],
                "visuals": [
                    ("亲属关系要逐段证明", "出生、婚姻或收养记录", "死亡、身份或姓名记录", "几份材料连在一起，才能看出完整关系。"),
                    ("从家属关系走到内地遗产", "画出家属关系", "核对遗嘱与继承安排", "对接内地资产", "关系证据只是整个办理路径的一部分。"),
                    ("第一次整理四栏", "要证明哪段关系", "材料和签发信息", "姓名日期差异", "内地资产和用途", "先找缺口，再申领或补充材料。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "澳门家属处理内地继承时，出生记录可以连接父母和子女，婚姻记录可以说明婚姻关系，死亡记录可以交代某位家属已经去世，身份和姓名记录则用来确认几份材料说的是同一个人。多数家庭需要的是一条证据链，不是一张包办全部关系的证明。",
                    "这条证据链仍不会自动决定谁取得哪项内地资产，也不能代替遗嘱、继承人资格材料或房产、账户本身的资料。先写清楚要证明哪一段关系，再找对应记录，通常比先问“办哪一张亲属证明”更有效。",
                ],
                "sections": [
                    ("先把家庭画成一张简单关系图", ["从逝者开始，列出配偶、子女、父母，以及已经先去世的家属。每一条连线旁边写上可以支持它的记录，例如出生、婚姻、收养、死亡或姓名变更材料。这样很快就能看到哪一段已有文件，哪一段仍然空白。", "再婚、收养、家属在不同地方出生，或者同一个人曾经使用不同姓名时，不要用口头称呼代替正式关系。把每种姓名、日期和证件号码原样抄下，并标明它出现在哪份材料上。"]),
                    ("每份材料回答的问题都有限", ["出生记录通常用来说明父母和子女，婚姻记录说明婚姻事实，死亡记录说明死亡，身份材料用来把姓名和本人连起来。某份记录没有列出其他家属，不代表那些家属不存在；它可能本来就不是用来提供完整家属名单。", "所以，看到一份材料上有父母或配偶姓名时，不要直接把它当成全部继承人名单。还要看家属结构、是否有人先去世、是否有遗嘱，以及办理时真正需要确认的是哪一层关系。"]),
                    ("证明谁是家属，还不等于分好遗产", ["全体继承人都已成年、能够自行处理并且没有争议时，澳门用于确认谁具有继承身份的安排，仍会根据家庭情况要求死亡、婚姻、出生、身份和遗嘱等不同材料。这说明继承身份通常来自一组互相衔接的证据，不是只凭其中一张记录。", "即使家属关系已经清楚，内地房产、存款或股权仍要另查登记人、共有状态、账户或公司资料，以及当地接收材料的要求。关系证据回答“人怎样连起来”，资产资料回答“遗产是什么”，两边不能互相代替。"]),
                    ("有争议或材料缺失时，先不要硬补结论", ["如果家属对关系或遗嘱有争议、有人失联、继承人包括未成年人或需要协助作决定的人，或者关键记录确实无法取得，普通的无争议整理方式未必合适。先保留现有材料和不同家属的说法，再判断是补材料还是处理争议。", "现在可以先做一页表：第一栏写要证明的两个人，第二栏写现有材料，第三栏圈出姓名和日期差异，第四栏写内地哪个城市、哪项资产、哪一步要使用。接收方看到这张表，才容易指出真正缺的是哪一段。"]),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门专题总览"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_cn.html", "澳门死亡记录用于内地继承先核对什么"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门家属继承内地房产，先分清两套材料"),
                    ("/articles/hk-mainland-property-inheritance/family-relationship-evidence_cn.html", "对照阅读：家属关系材料怎样连成证据链"),
                ],
                "cta": "把逝者、家属关系、现有澳门材料和内地资产城市列清楚，再判断缺的是哪一段证据。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau family records",
                "title": "Macau Family Records for a Mainland Estate: What Do They Prove?",
                "description": "How Macau birth, marriage, death and identity records can establish a family chain for a Mainland estate, and what they cannot decide.",
                "lead": "Most families do not need one all-purpose kinship certificate. They need several records that connect the deceased to each relative, one link at a time.",
                "key_title": "Three points to keep separate",
                "keys": [
                    "Each record proves a particular fact or relationship",
                    "Names, dates and identity details must connect",
                    "Family evidence does not decide each person's share",
                ],
                "visuals": [
                    ("Prove the family chain link by link", "Birth, marriage or adoption record", "Death, identity or name record", "Several records may be needed to show the full relationship."),
                    ("Connect the family to the Mainland estate", "Map the family", "Check the will and estate route", "Match the Mainland asset", "Family evidence is one part of the estate file."),
                    ("Build a four-column working sheet", "Relationship", "Record and issuer", "Name or date gap", "Mainland use", "Find the missing link before ordering more documents."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "A birth record may connect a child to the parents, a marriage record may establish a marriage, and a death record may explain why a relative is no longer living. Identity and name records help show that different documents refer to the same person. Together, these records can form a family evidence chain; no single record normally answers every inheritance question.",
                    "That chain does not by itself identify every heir, decide each person's share or transfer a Mainland property, account or company interest. Start by naming the exact relationship that must be proved, then match a record to each link rather than ordering a generic certificate first.",
                ],
                "sections": [
                    ("Draw a simple family map first", ["Begin with the deceased and add the spouse, children, parents and any relative who died earlier. Beside each line, note the record that supports it: birth, marriage, adoption, death or a name-change record. The empty lines then show where evidence is actually missing.", "A remarriage, adoption, birth outside Macau or a former name can make the chain less obvious. Copy every name, date and identity number exactly as it appears, and record which official document contains it. Do not make the papers look consistent by editing a translation."]),
                    ("Each record has a limited job", ["A birth record ordinarily addresses parentage, a marriage record addresses the marriage, and a death record addresses the death. An identity record helps connect a name to a person. A document's silence about other relatives does not prove that they do not exist; listing the whole family may never have been its purpose.", "A record naming a spouse or parent should therefore not be treated as a complete list of heirs. The family structure, earlier deaths, any will and the precise question in the estate process still matter."]),
                    ("Proving the family does not distribute the estate", ["Even where all heirs are adults, able to act for themselves and in agreement, Macau's process for identifying who has heirship status may require different combinations of death, marriage, birth, identity and will records. Status is assessed from a connected file, not from one document in isolation.", "Even a clear family chain does not establish what the deceased owned in Mainland China. The registered owner, any co-ownership, the bank or company records and the receiving city's requirements form a separate asset file. One file explains the people; the other explains the estate."]),
                    ("Do not force a tidy conclusion when the facts are disputed", ["A disagreement over the family or a will, a missing relative, a minor or a person who needs support in decision-making, or an unavailable key record may take the matter outside a routine uncontested route. Preserve the available records and each person's position before deciding whether the next step is evidence gathering or dispute work.", "A practical first sheet has four columns: the two people to be connected, the supporting record, any name or date mismatch, and the Mainland asset and intended use. A recipient can respond far more precisely to that sheet than to the question, 'Which kinship certificate do I need?' "]),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau estate topic overview"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_en.html", "Using a Macau death record for a Mainland estate"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Separating the Macau family file from the Mainland property file"),
                    ("/articles/hk-mainland-property-inheritance/family-relationship-evidence_en.html", "Comparison: building a family evidence chain"),
                ],
                "cta": "List the deceased, the family links, the Macau records already available and the Mainland asset city. The missing part of the evidence chain will then be easier to identify.",
            },
        },
    },
    {
        "slug": "issuing-state-matters",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國文件",
                "title": "美國文件用於內地繼承，先看由哪一級機關簽發",
                "description": "美國死亡、法院或其他文件交到內地繼承程序前，先分清州級與聯邦文件，避免走錯附加證明路徑。",
                "lead": "先別急着支付認證或郵寄費。把文件完整拍下來，看清簽發單位和州名，才知道應走州級還是聯邦路徑。",
                "key_title": "先分清三件事",
                "keys": [
                    "州或地方文件通常沿簽發州的路徑辦理",
                    "聯邦文件通常不交州務卿處理",
                    "附加證明只核驗文件來源，不決定繼承結果",
                ],
                "visuals": [
                    ("先分清文件來源", "州、縣、市或州法院文件", "美國聯邦機關文件", "兩類文件通常由不同機關處理附加證明。"),
                    ("正確的準備順序", "確認簽發機關與州", "取得合適正式版本", "確認內地接收用途", "先問清楚，再支付認證、翻譯或郵寄費用。"),
                    ("文件送出前核對四項", "簽發機關與州", "正本或正式副本", "姓名日期與印章", "內地城市與用途", "不要只憑文件名稱猜辦理路徑。"),
                ],
                "answer_title": "最短的判斷方法",
                "answer": [
                    "由州簽發的死亡證明、州法院文件或其他州級公共文件，通常要沿簽發州的程序取得附加證明；由美國聯邦機關簽發的文件，則通常由聯邦層面的主管機關處理。先看文件上的簽發機關、州名、印章和簽署人，而不是看家屬現在住在哪一州。",
                    "還要分清文件是否為可接受的正本或正式核證副本。附加證明確認的是簽名、印章或文件來源，不會替內地接收方判斷家屬是否具有繼承權，也不會令一份內容不足的文件自動變成可過戶材料。",
                ],
                "sections": [
                    ("先在文件上找四個答案", ["把文件完整頁面放在眼前，找出簽發機關、所屬州或聯邦部門、簽發日期，以及印章或簽署人的身份。死亡證明通常會寫州、縣或市的出生及死亡登記部門；法院文件會寫出具體法院；聯邦文件則會顯示聯邦部門或機關。", "私人授權書等文件若由州公證員見證，通常還要看該公證員在哪一州獲授權。家屬住在加州，不代表紐約州簽發的死亡證明可以在加州辦理；真正重要的是文件或簽名由哪個有權機關核驗。"]),
                    ("州級文件也要先看正式版本", ["州簽發的生命紀錄通常要向簽發州申領合適的正式副本，再按該州的路徑辦理。縣、市或法院文件有時還要先完成當地或州內的前置核證；各州、各文件種類並不完全相同。", "不要把普通影印件送去公證後，就假定它等同州簽發的正式副本。先把文件種類、簽發州和副本形式說清楚，再向該州主管機關確認步驟。"]),
                    ("聯邦文件不要送錯到州級機關", ["如果文件由美國聯邦部門、聯邦法院或其他聯邦機關簽發，附加證明一般走聯邦路徑，而不是交給某一州的州務卿。使用正本還是正式核證副本，也要按該文件的聯邦要求準備。", "同一個家庭可能同時有州簽發的死亡證明和聯邦文件，兩份文件因此可能走不同路徑。最省時間的做法是逐份標註來源，不要把所有美國文件放進同一個申請。"]),
                    ("最後才是翻譯和交到內地", ["取得附加證明前，先向內地接收方說清楚文件名稱、簽發機關、內地城市和用途，確認要正本、正式副本、翻譯還是其他配套資料。姓名、日期或舊證件資料對不上時，也應先列出差異，不要等翻譯完成後才發現。", "附加證明解決的是文件來源核驗，不是內容是否足夠。死亡證明不能單獨列出全部繼承人，法院文件也未必已處理內地房產的登記和共有狀況。文件路徑走對之後，仍要把家屬、遺囑和內地資產資料接起來。"]),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國專題總覽"),
                    ("/articles/us/us-documents-mainland-property-inheritance.html", "美國死亡證明和遺囑用於內地房產先核對甚麼"),
                    ("/articles/hk-mainland-property-inheritance/name-mismatch-across-records.html", "中英文姓名對不上時怎樣整理"),
                    ("/articles/hk-mainland-property-inheritance/property-transfer-checklist.html", "內地房產繼承過戶前的資料清單"),
                ],
                "cta": "把文件名稱、簽發機關、簽發州和內地使用城市列清楚，再判斷走州級還是聯邦路徑。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国文件",
                "title": "美国文件用于内地继承，先看由哪一级机构签发",
                "description": "美国死亡、法院或其他文件交到内地继承程序前，先分清州级和联邦文件，避免走错附加证明路径。",
                "lead": "先别急着支付认证或邮寄费用。把文件完整拍下来，看清签发机构和州名，才能判断应走州级还是联邦路径。",
                "key_title": "先分清三件事",
                "keys": ["州或地方文件通常沿签发州的路径办理", "联邦文件通常不交州务卿处理", "附加证明只核验文件来源，不决定继承结果"],
                "visuals": [
                    ("先分清文件来源", "州、县、市或州法院文件", "美国联邦机构文件", "两类文件通常由不同机构处理附加证明。"),
                    ("正确的准备顺序", "确认签发机构和州", "取得合适正式版本", "确认内地接收用途", "先问清楚，再支付认证、翻译或邮寄费用。"),
                    ("文件寄出前核对四项", "签发机构和州", "原件或正式副本", "姓名日期和印章", "内地城市和用途", "不要只凭文件名称猜办理路径。"),
                ],
                "answer_title": "最短的判断方法",
                "answer": ["由州签发的死亡证明、州法院文件或其他州级公共文件，通常要沿签发州的程序取得附加证明；由美国联邦机构签发的文件，通常由联邦层面的主管机构处理。先看文件上的签发机构、州名、印章和签署人，不要只看家属现在住在哪个州。", "还要分清文件是不是可以接受的原件或正式认证副本。附加证明确认的是签名、印章或文件来源，不会替内地接收方判断家属是否具有继承权，也不会让一份内容不足的材料自动变成过户文件。"],
                "sections": [
                    ("先在文件上找四个答案", ["把文件完整页面放在眼前，找出签发机构、所属州或联邦部门、签发日期，以及印章或签署人的身份。死亡证明通常会写州、县或市的出生和死亡登记部门；法院文件会写明具体法院；联邦文件会显示联邦部门或机构。", "私人授权书等材料如果由州公证员见证，通常还要看公证员在哪个州获得授权。家属住在加州，不代表纽约州签发的死亡证明可以在加州办理；真正重要的是文件或签名由哪个有权机构核验。"]),
                    ("州级文件也要先看正式版本", ["州签发的生命记录通常要向签发州申领合适的正式副本，再按该州的路径办理。县、市或法院文件有时还要先完成当地或州内的前置认证；各州、各类文件并不完全相同。", "不要把普通复印件拿去公证后，就假定它等同于州签发的正式副本。先把文件种类、签发州和副本形式说明清楚，再向该州主管机构确认步骤。"]),
                    ("联邦文件不要送错州级机构", ["如果文件由美国联邦部门、联邦法院或其他联邦机构签发，附加证明一般走联邦路径，不是交给某个州的州务卿。使用原件还是正式认证副本，也要按照该文件的联邦要求准备。", "同一个家庭可能同时有州签发的死亡证明和联邦文件，两份材料就可能走不同路径。最省时间的做法是逐份标注来源，不要把所有美国文件放进同一个申请。"]),
                    ("最后再安排翻译和内地使用", ["办理附加证明前，先向内地接收方说明文件名称、签发机构、内地城市和用途，确认需要原件、正式副本、翻译还是其他配套材料。姓名、日期或旧证件资料对不上时，也应当先列出差异。", "附加证明解决的是文件来源核验，不是内容是否充分。死亡证明不能单独列出全部继承人，法院文件也未必已经处理内地房产的登记和共有情况。文件路径走对以后，仍要把家属、遗嘱和内地资产材料连接起来。"]),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国专题总览"),
                    ("/articles/us/us-documents-mainland-property-inheritance_cn.html", "美国死亡证明和遗嘱用于内地房产先核对什么"),
                    ("/articles/hk-mainland-property-inheritance/name-mismatch-across-records_cn.html", "中英文姓名对不上时怎样整理"),
                    ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_cn.html", "内地房产继承过户前的材料清单"),
                ],
                "cta": "把文件名称、签发机构、签发州和内地使用城市列清楚，再判断走州级还是联邦路径。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. estate documents",
                "title": "U.S. Estate Documents for Mainland China: Start With the Issuing Authority",
                "description": "How the issuing authority determines the apostille route for U.S. state and federal documents used in a Mainland China estate matter.",
                "lead": "Before paying for certification or courier services, photograph the full document and identify the issuer and state. Those details determine whether the route is state or federal.",
                "key_title": "Make three distinctions first",
                "keys": ["State and local records usually follow the issuing state's route", "Federal documents ordinarily do not go to a state Secretary of State", "An apostille verifies origin, not the inheritance outcome"],
                "visuals": [
                    ("Identify the source first", "State, county, city or state-court record", "U.S. federal document", "The two groups ordinarily use different apostille authorities."),
                    ("Prepare in the right order", "Identify issuer and state", "Obtain the right official copy", "Confirm the Mainland use", "Clarify the route before paying for certification, translation or courier services."),
                    ("Four checks before sending the document", "Issuer and state", "Official copy", "Names, dates and seal", "Mainland use", "Do not choose the route from the document title alone."),
                ],
                "answer_title": "The practical rule",
                "answer": [
                    "A death certificate, state-court record or other public document issued under state authority will generally follow the apostille process of the issuing state. A document issued by a U.S. federal authority will generally use the federal authentication route. The issuing authority matters; the state where the family now lives does not determine the answer.",
                    "The document must also be in a form that the relevant authority will accept, often an original or an appropriate certified copy. An apostille verifies a signature, seal or source. It does not decide who inherits or turn an incomplete record into a sufficient Mainland property-transfer file.",
                ],
                "sections": [
                    ("Find four facts on the document", ["Read the full page and record the issuing authority, the state or federal department, the issue date, and the signer or seal. A vital record may name a state, county or city office; a court paper should identify the court; a federal document should identify the federal department or agency.", "For a private instrument such as a power of attorney, the relevant state is ordinarily the state that commissioned the notary. A California resident therefore cannot assume that California will apostille a New York death certificate; the key question is which authority can verify the document or signature."]),
                    ("A state document still needs the right official version", ["State vital records ordinarily begin with an appropriate official copy from the issuing state. A county, city or court record may also require a local or state-level preliminary certification. The details vary by state and document type.", "A notarised photocopy should not be assumed to replace an official state copy. Identify the record, issuing state and copy type, then confirm the steps with that state's competent authority."]),
                    ("Do not send a federal document to the wrong state office", ["A document issued by a federal department, federal court or other federal authority will ordinarily use the federal route rather than a state Secretary of State. Whether the original or a certified copy is required depends on the federal document involved.", "One estate may contain both a state-issued death certificate and a federal document. They may therefore need separate applications. Label the source of each paper instead of sending every U.S. document through one route."]),
                    ("Translation and Mainland use come after the route is clear", ["Before ordering an apostille, tell the Mainland recipient the document name, issuer, destination city and intended estate use. Ask whether it expects the original, a certified copy, a translation or additional family evidence. Identify name, date or old-ID differences before the translation is finalised.", "An apostille resolves a document-origin question, not a content question. A death certificate does not list every heir, and a probate paper may not address ownership or co-ownership of a Mainland property. The family, will and Mainland asset files must still be connected after the document takes the correct route."]),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/united-states/index_en.html", "United States estate topic overview"),
                    ("/articles/us/us-documents-mainland-property-inheritance_en.html", "Using U.S. estate documents for Mainland property"),
                    ("/articles/hk-mainland-property-inheritance/name-mismatch-across-records_en.html", "Connecting English and Chinese names"),
                    ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_en.html", "First checklist for a Mainland property inheritance"),
                ],
                "cta": "List the document, issuing authority, issuing state and Mainland destination. That is the starting point for choosing the state or federal route.",
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
        "href": "/articles/am/macau-kinship-certificate-scope.html",
        "card": '<a href="/articles/am/macau-kinship-certificate-scope.html"><span class="v24-tag">親屬文件</span><strong>澳門親屬關係文件用於內地繼承，能證明甚麼</strong><p>用出生、婚姻、死亡和身份紀錄，把逝者與家屬逐段連起來。</p></a>',
        "upcoming": "<span>澳門親屬關係文件怎樣連到內地繼承人</span>",
        "old_summary": "<summary>接下來會整理的問題 <span>4 個方向</span></summary>",
        "new_summary": "<summary>接下來會整理的問題 <span>3 個方向</span></summary>",
        "marker": '<details class="v24-article-more"',
    },
    "articles/macau/index_cn.html": {
        "href": "/articles/am/macau-kinship-certificate-scope_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">亲属材料</span><h3>澳门亲属关系材料用于内地继承，能证明什么</h3><p>用出生、婚姻、死亡和身份记录，把逝者与家属一段一段连起来。</p></div><a class="v25-pill-action" href="/articles/am/macau-kinship-certificate-scope_cn.html">阅读文章</a></article>',
        "upcoming": "<span>澳门亲属关系文件怎样连接到内地继承人</span>",
        "old_summary": "<summary>接下来会整理的问题 <span>4 个方向</span></summary>",
        "new_summary": "<summary>接下来会整理的问题 <span>3 个方向</span></summary>",
        "marker": '<details class="v25-article-more"',
    },
    "articles/macau/index_en.html": {
        "href": "/articles/am/macau-kinship-certificate-scope_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Family records</span><h3>What Macau family records prove in a Mainland estate</h3><p>Connect the deceased to each relative with birth, marriage, death and identity records.</p></div><a class="v25-pill-action" href="/articles/am/macau-kinship-certificate-scope_en.html">Read Article</a></article>',
        "upcoming": "<span>Connecting Macau family records to the heirship file</span>",
        "old_summary": "<summary>Questions being prepared next <span>4 directions</span></summary>",
        "new_summary": "<summary>Questions being prepared next <span>3 directions</span></summary>",
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index.html": {
        "href": "/articles/us/issuing-state-matters.html",
        "card": '<a href="/articles/us/issuing-state-matters.html"><span class="v24-tag">文件來源</span><strong>美國文件用於內地繼承，先看由哪一級機關簽發</strong><p>分清州級與聯邦文件，避免把附加證明送錯機關。</p></a>',
        "upcoming": "<span>死亡證明由不同州簽發，附加證明找誰辦</span>",
        "old_summary": "<summary>接下來會整理的問題 <span>4 個方向</span></summary>",
        "new_summary": "<summary>接下來會整理的問題 <span>3 個方向</span></summary>",
        "marker": '<details class="v24-article-more"',
    },
    "articles/united-states/index_cn.html": {
        "href": "/articles/us/issuing-state-matters_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">文件来源</span><h3>美国文件用于内地继承，先看由哪一级机构签发</h3><p>分清州级和联邦文件，避免把附加证明送错机构。</p></div><a class="v25-pill-action" href="/articles/us/issuing-state-matters_cn.html">阅读文章</a></article>',
        "upcoming": "<span>死亡证明由不同州签发，附加证明找谁办理</span>",
        "old_summary": "<summary>接下来会整理的问题 <span>4 个方向</span></summary>",
        "new_summary": "<summary>接下来会整理的问题 <span>3 个方向</span></summary>",
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index_en.html": {
        "href": "/articles/us/issuing-state-matters_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Document source</span><h3>Start with the authority that issued the U.S. document</h3><p>Separate state and federal records before choosing an apostille route.</p></div><a class="v25-pill-action" href="/articles/us/issuing-state-matters_en.html">Read Article</a></article>',
        "upcoming": "<span>Which authority apostilles a state-issued death certificate?</span>",
        "old_summary": "<summary>Questions being prepared next <span>4 directions</span></summary>",
        "new_summary": "<summary>Questions being prepared next <span>3 directions</span></summary>",
        "marker": '<details class="v25-article-more"',
    },
}


def update_hubs() -> None:
    for relative_path, update in HUB_UPDATES.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if update["href"] not in text:
            if update["marker"] not in text:
                raise RuntimeError(f"Hub insertion marker missing: {relative_path}")
            text = text.replace(update["marker"], update["card"] + update["marker"], 1)
        text = text.replace(update["upcoming"], "", 1)
        text = text.replace(update["old_summary"], update["new_summary"], 1)
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
