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
        "slug": "undisputed-or-disputed-route",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門家屬與內地繼承分流",
                "title": "澳門家屬意見一致和有人反對，內地繼承要走哪條路",
                "description": "澳門家屬處理內地遺產時，先分清已同意、未回覆和明確反對，再決定文件辦理、協商或爭議處理路徑。",
                "lead": "一個人說不，和一個人還未回覆，不是同一種卡點。先把分歧寫準，才知道下一步要補文件還是處理爭議。",
                "key_title": "先分清三種狀態",
                "keys": [
                    "已確認同意：人、資產和方案都清楚",
                    "尚未回覆：仍要找人和確認意思",
                    "明確反對：知道他反對哪個具體問題",
                ],
                "answer_title": "意見一致可以整理文件，有實質反對就先處理分歧",
                "answer": [
                    "家屬全部同意，不代表一個人便能代替所有人簽字。協調人可以先收集死亡、親屬、遺囑和資產資料，但正式申請由誰提出、誰要到場、誰可授權，仍要按資產所在地和接收機構確認。",
                    "有人對繼承人、遺囑、資產是否屬於逝者或分配方案提出實質反對時，不要把它包裝成普通補件。先保留各方說法和證據，看看能否把爭點縮小；無法解決時，再由合適的調解或法院程序確認。",
                ],
                "sections": [
                    (
                        "一、把每個人的狀態放進同一張表",
                        [
                            "列出配偶、父母、子女、遺囑提到的人，以及可能涉及代位或轉繼承的人。每人只標記已確認同意、尚未回覆、明確反對或身份待核對，不要只寫合作、不合作。",
                            "再用一句話寫清反對內容：是不承認某位繼承人、質疑遺囑版本、認為房產含有配偶或他人份額，還是不同意如何分配。反對的問題不同，所需證據和下一步也不同。",
                        ],
                    ),
                    (
                        "二、家屬一致時，仍要逐項核對接收條件",
                        [
                            "澳門辦理確認繼承人資格文件的簡化條件，通常以成年繼承人、無繼承權爭議和文件齊備為重要前提；死者常居地不在澳門時，還可能要補外地繼承順位資料。先確認這份澳門文件能回答甚麼。",
                            "再向內地房產、銀行或公司所在地問清申請人、到場、委託、翻譯和查驗要求。有些城市的房產繼承查驗會要求相關繼承人共同確認；一人負責聯絡，不等於一人自動取得全部代表權。",
                        ],
                    ),
                    (
                        "三、有人反對時，不要繼續交互相矛盾的材料",
                        [
                            "若一方已明確否認繼承人、遺囑、資產範圍或分配方案，先停止要求他簽一份『全體無異議』的文件。保留訊息、信件、原件位置和每次提出反對的日期，不要代替對方改寫立場。",
                            "先嘗試把沒有爭議的事實固定下來，例如死亡、房產地址、目前登記、家屬名單和文件版本。若爭點不能協商解決，再評估由哪個地方的調解或法院處理；不能只因協調人在澳門，便假定所有爭議都在澳門處理。",
                        ],
                    ),
                    (
                        "四、用一頁分流表決定下一步",
                        [
                            "第一欄寫已確認事實，第二欄寫尚缺文件，第三欄寫明確爭點，第四欄寫目前可做的保存或查詢。把『未回覆』留在聯絡工作，不要過早當成反對；把『明確反對』留在爭議工作，不要混進普通補件。",
                            "如果涉及內地房產，先問登記城市遇到異議時會否中止查驗；如果需要法院確認，再核對逝者死亡時住所、主要遺產所在地和具體資產所在地。完成這張表後，家屬才適合決定協商、補件或訴訟的先後。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/family-coordinator-first-sheet.html", "大家庭先選協調人還是先收資料"),
                    ("/articles/am/macau-heir-qualification-deed.html", "何時值得辦確認繼承人資格文件"),
                    ("/articles/am/occupied-or-sold-property.html", "房子被佔用或疑似出售時怎樣保留證據"),
                ],
                "cta": "把家屬名單、每人狀態、資產城市、文件版本和具體反對理由列在一頁，我們先分清補件、協商和爭議處理。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门家属与内地继承分流",
                "title": "澳门家属意见一致和有人反对，内地继承要走哪条路",
                "description": "澳门家属处理内地遗产时，先分清已经同意、尚未回复和明确反对，再决定文件办理、协商或争议处理路径。",
                "lead": "一个人明确反对，和一个人还没有回复，并不是同一种卡点。先把分歧写准确，才知道下一步要补文件还是处理争议。",
                "key_title": "先分清三种状态",
                "keys": [
                    "已经确认同意：人物、资产和方案清楚",
                    "尚未回复：仍要联系和确认真实意思",
                    "明确反对：知道他反对哪个具体问题",
                ],
                "answer_title": "意见一致可以整理文件，有实质反对就先处理分歧",
                "answer": [
                    "家属全部同意，不代表一个人可以代替所有人签字。协调人可以先收集死亡、亲属、遗嘱和资产资料，但正式申请由谁提出、谁要到场、谁可以授权，仍要按照资产所在地和接收机构确认。",
                    "有人对继承人、遗嘱、资产是否属于逝者或者分配方案提出实质反对时，不要把它当成普通补件。先保留各方说法和证据，看看能否缩小争议；无法解决时，再由合适的调解或法院程序确认。",
                ],
                "sections": [
                    (
                        "一、把每个人的状态放进同一张表",
                        [
                            "列出配偶、父母、子女、遗嘱提到的人，以及可能涉及代位或转继承的人。每个人只标记已经确认同意、尚未回复、明确反对或者身份待核对，不要只写配合、不配合。",
                            "再用一句话写清反对内容：是不承认某位继承人、质疑遗嘱版本、认为房产含有配偶或他人份额，还是不同意怎样分配。问题不同，需要的证据和下一步也不同。",
                        ],
                    ),
                    (
                        "二、家属一致时，仍要逐项核对接收条件",
                        [
                            "澳门办理确认继承人资格文件的简化条件，通常把成年继承人、没有继承权争议和文件齐备作为重要前提；逝者常住地不在澳门时，还可能要补外地继承顺序资料。先确认这份澳门文件能回答什么。",
                            "再向内地房产、银行或公司所在地问清申请人、到场、委托、翻译和查验要求。有些城市的房产继承查验会要求相关继承人共同确认；一个人负责联系，不等于一个人自动取得全部代表权。",
                        ],
                    ),
                    (
                        "三、有人反对时，不要继续提交相互矛盾的材料",
                        [
                            "一方已经明确否认继承人、遗嘱、资产范围或者分配方案时，先停止要求他签署『全体无异议』的文件。保存信息、信件、原件位置和每次提出反对的日期，不要代替对方改写立场。",
                            "先把没有争议的事实固定下来，例如死亡、房产地址、目前登记、家属名单和文件版本。如果争议不能协商解决，再评估由哪个地方的调解或法院处理；不能只因为协调人在澳门，就假定所有争议都在澳门处理。",
                        ],
                    ),
                    (
                        "四、用一页分流表决定下一步",
                        [
                            "第一栏写已经确认的事实，第二栏写缺少的文件，第三栏写明确争议，第四栏写现在可以做的保存或查询。把『尚未回复』留在联系工作，不要过早当成反对；把『明确反对』留在争议工作，不要混进普通补件。",
                            "涉及内地房产时，先问登记城市遇到异议是否会停止查验；需要法院确认时，再核对逝者死亡时住所、主要遗产所在地和具体资产所在地。完成这张表后，再决定协商、补件或诉讼的顺序。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/family-coordinator-first-sheet_cn.html", "大家庭先选协调人还是先收资料"),
                    ("/articles/am/macau-heir-qualification-deed_cn.html", "什么时候值得办确认继承人资格文件"),
                    ("/articles/am/occupied-or-sold-property_cn.html", "房子被占用或疑似出售时怎样保存证据"),
                ],
                "cta": "把家属名单、每个人的状态、资产城市、文件版本和具体反对理由列在一页，我们先分清补件、协商和争议处理。",
            },
            "en": {
                "lang": "en",
                "locale": "en_HK",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau families choosing an estate route",
                "title": "When a Macau Family Agrees — and When Someone Objects",
                "description": "A practical guide for Macau families separating agreement, silence and a real objection before choosing a Mainland estate route.",
                "lead": "A relative who objects and a relative who has not replied create different problems. Name the issue before choosing a process.",
                "key_title": "Use three clear statuses",
                "keys": [
                    "Agreed: the people, assets and proposal are understood",
                    "No reply: contact and intention are still uncertain",
                    "Objected: the precise point of disagreement is recorded",
                ],
                "answer_title": "Agreement supports document work; a real objection needs its own route",
                "answer": [
                    "Family agreement does not allow one person to sign for everyone. A coordinator can collect death, family, will and asset records, but the receiving institution still decides who must apply, attend or provide authority papers.",
                    "If someone challenges an heir, a will, the deceased's ownership or the proposed distribution, do not present the case as a routine missing-document file. Preserve each position and the supporting records, narrow the issue if possible, and use mediation or a court process when the dispute cannot be resolved.",
                ],
                "sections": [
                    (
                        "1. Give every person a precise status",
                        [
                            "List the spouse, parents, children, anyone named in a will and any person affected by representation or a later death. Mark each person as agreed, no reply, objected or identity to be checked. Avoid a vague cooperative or uncooperative label.",
                            "State the objection in one sentence. Does the person dispute an heir, the last will, a spouse's pre-existing interest, the deceased's ownership or the distribution proposal? Each issue calls for different evidence and a different next step.",
                        ],
                    ),
                    (
                        "2. When the family agrees, check both receiving sides",
                        [
                            "Macau's simpler heir-qualification service generally depends on adult heirs, no dispute over heirship and a complete file. If the deceased was habitually resident elsewhere, evidence of the succession order there may also be needed. First identify what the Macau record can actually prove.",
                            "Then ask the Mainland property registry, bank or company about the applicant, attendance, authority and translation requirements. Some local property procedures ask the relevant heirs to confirm the inheritance materials together. One family coordinator does not automatically hold authority for everyone.",
                        ],
                    ),
                    (
                        "3. When someone objects, stop submitting inconsistent statements",
                        [
                            "Do not ask a person who has rejected an heir, will, asset boundary or distribution proposal to sign a no-objection statement. Keep the messages, letters, original-document locations and dates. Record the person's position without rewriting it for them.",
                            "Secure the common facts first: the death, asset address, current title, family list and document versions. If the remaining issue cannot be resolved, identify the appropriate mediation or court route. The coordinator's home in Macau does not by itself decide where a Mainland estate dispute belongs.",
                        ],
                    ),
                    (
                        "4. Use one route sheet for the next decision",
                        [
                            "Create columns for confirmed facts, missing records, stated objections and preservation or search work that can continue now. Keep no reply in the contact column rather than calling it opposition. Keep a real objection in the dispute column rather than treating it as ordinary paperwork.",
                            "For a Mainland home, ask the registration city what happens when an objection is raised during inheritance review. If a court decision may be needed, check the deceased's last domicile, the location of the principal estate and the location of the particular asset before choosing where to act.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"),
                    ("/articles/am/family-coordinator-first-sheet_en.html", "Choosing a coordinator for a large family"),
                    ("/articles/am/macau-heir-qualification-deed_en.html", "When a Macau heir-qualification deed is useful"),
                    ("/articles/am/occupied-or-sold-property_en.html", "Preserving evidence when a home is occupied or may have been sold"),
                ],
                "cta": "Put the family list, each person's status, asset city, document versions and exact objection on one page. We can separate paperwork, negotiation and dispute work.",
            },
        },
    },
    {
        "slug": "remitting-inherited-funds",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與內地繼承款",
                "title": "內地繼承款匯到新加坡前，哪些來源文件不能丟",
                "description": "內地遺產變成現金並準備匯到新加坡時，家屬應保留原始資產、繼承、變現、外匯和入賬資料的完整來源鏈。",
                "lead": "銀行看到的是一筆款，你要保留的是它從哪項遺產一路變成這筆款。",
                "key_title": "把來源分成四段",
                "keys": [
                    "原始遺產：房產、存款、股權或其他資產",
                    "取得權利：誰繼承、誰有權辦理",
                    "變成現金：出售、提取、分配和稅務資料",
                    "完成匯款：核准、銀行回單和新加坡入賬",
                ],
                "answer_title": "不要只留最後一張匯款回單",
                "answer": [
                    "一筆款可以有不同起點。房產出售所得要連回房產權屬、繼承和出售資料；銀行存款要連回賬戶、死亡和領取資料；股權所得則要分清股權轉讓、分紅或公司欠款。只留最終餘額，往往無法說明資金來源。",
                    "新加坡的收款銀行可能會問交易用途和資金來源，內地匯出一邊也會按身份、原始資產和辦理路徑要求文件。匯款前先讓兩邊銀行看一份資料清單，比款項到賬後再四處補證明更穩妥。",
                ],
                "sections": [
                    (
                        "一、先從原始遺產開始，不從現金餘額開始",
                        [
                            "如果來源是房產，保留權屬資料、繼承文件、出售合同、成交和收款紀錄；如果來源是存款，保留銀行確認、領取申請和入賬紀錄；如果來源是股權，分開持股、轉讓、分紅和股東借款。",
                            "每項資產用一個編號，記下原持有人、資產城市、原始價值、最後變現金額和款項進入哪個內地賬戶。幾項資產合成一筆款時，做一張加總表，不要只用『家庭資金』概括。",
                        ],
                    ),
                    (
                        "二、把繼承身份和辦理人接上來源鏈",
                        [
                            "保存死亡、親屬、遺囑或無遺囑處理、分配結果，以及誰獲授權領取或出售資產的文件。姓名有中英文拼法、舊證件或婚後變更時，另做一張姓名對照表。",
                            "不要只寫『人在新加坡』便假定適用同一匯出路徑。新加坡公民、永久居民或其他居留身份，以及逝者原戶籍和資產種類，都可能影響受理方式。先把身份資料交給內地受理方確認。",
                        ],
                    ),
                    (
                        "三、把變現、稅務和匯出資料留在同一檔案夾",
                        [
                            "保存成交結算、銀行流水、付款人、收款賬戶、扣費和實際到賬金額；按具體資產保留需要的稅務或完稅資料。金額與合同或權利文件不一致時，先寫明差額來自費用、稅款、還貸還是其他分配。",
                            "內地現行繼承財產轉移辦理資料通常會核對繼承證明、原始財產權利、變現說明和相關稅務文件。不要把繼承款拆成多筆、改寫成生活費或借款來避開詢問；如實說明來源和用途。",
                        ],
                    ),
                    (
                        "四、匯款前先問兩間銀行同一組問題",
                        [
                            "向內地匯出銀行問受理地、申請人、幣種、收款人姓名、匯款用途和核准文件；向新加坡收款銀行問賬戶姓名、可收幣種、中間行資料，以及大額入賬時可能要求的來源文件。",
                            "新加坡銀行會持續核對交易是否符合賬戶使用和已知資金來源，必要時可能要求說明。把四段資料各做一頁目錄，保留原件、完整掃描件和最終回單；不要只把零散照片放在聊天軟件裏。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/known-mainland-bank-account.html", "知道內地銀行和賬戶時先準備甚麼"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "內地房產怎樣放進新加坡遺產清單"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "新加坡遺產代表文件怎樣分"),
                ],
                "cta": "把原始資產、繼承文件、變現收款、稅務資料和預計入賬賬戶列在一頁，我們先檢查資金來源鏈在哪一段斷了。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与内地继承款",
                "title": "内地继承款汇到新加坡前，哪些来源文件不能丢",
                "description": "内地遗产变成现金并准备汇到新加坡时，家属应保存原始资产、继承、变现、外汇和入账资料的完整来源链。",
                "lead": "银行看到的是一笔款，你要保存的是它从哪项遗产一路变成这笔款。",
                "key_title": "把来源分成四段",
                "keys": [
                    "原始遗产：房产、存款、股权或其他资产",
                    "取得权利：谁继承、谁有权办理",
                    "变成现金：出售、提取、分配和税务资料",
                    "完成汇款：核准、银行回单和新加坡入账",
                ],
                "answer_title": "不要只保存最后一张汇款回单",
                "answer": [
                    "一笔款可以有不同起点。房产出售所得要连接房产权属、继承和出售资料；银行存款要连接账户、死亡和领取资料；股权所得则要分清股权转让、分红或者公司欠款。只留下最终余额，通常无法说明资金来源。",
                    "新加坡的收款银行可能询问交易用途和资金来源，内地汇出一方也会按照身份、原始资产和办理路径要求文件。汇款前先让两边银行查看一份资料清单，比款项到账后再到处补证明更稳妥。",
                ],
                "sections": [
                    (
                        "一、从原始遗产开始，不从现金余额开始",
                        [
                            "来源是房产时，保存权属资料、继承文件、出售合同、成交和收款记录；来源是存款时，保存银行确认、领取申请和入账记录；来源是股权时，分开持股、转让、分红和股东借款。",
                            "每项资产使用一个编号，记录原持有人、资产城市、原始价值、最后变现金额和款项进入哪个内地账户。几项资产合成一笔款时，做一张加总表，不要只写『家庭资金』。",
                        ],
                    ),
                    (
                        "二、把继承身份和办理人连接到来源链",
                        [
                            "保存死亡、亲属、遗嘱或者无遗嘱处理、分配结果，以及谁得到授权领取或出售资产的文件。姓名有中英文拼法、旧证件或者婚后变更时，另外制作姓名对照表。",
                            "不要只写『人在新加坡』便假定适用同一汇出路径。新加坡公民、永久居民或其他居留身份，以及逝者原户籍和资产种类，都可能影响受理方式。先把身份资料交给内地受理方确认。",
                        ],
                    ),
                    (
                        "三、把变现、税务和汇出资料放在同一文件夹",
                        [
                            "保存成交结算、银行流水、付款人、收款账户、扣费和实际到账金额；按照具体资产保留需要的税务或者完税资料。金额与合同或权利文件不一致时，先说明差额来自费用、税款、还贷还是其他分配。",
                            "内地现行继承财产转移办理资料通常会核对继承证明、原始财产权利、变现说明和相关税务文件。不要把继承款拆成多笔、改写成生活费或借款来避开询问；应当如实说明来源和用途。",
                        ],
                    ),
                    (
                        "四、汇款前先问两家银行同一组问题",
                        [
                            "向内地汇出银行询问受理地、申请人、币种、收款人姓名、汇款用途和核准文件；向新加坡收款银行询问账户姓名、可收币种、中间行资料，以及大额入账时可能要求的来源文件。",
                            "新加坡银行会持续核对交易是否符合账户用途和已知资金来源，必要时可能要求说明。把四段资料各做一页目录，保存原件、完整扫描件和最终回单；不要只把零散照片放在聊天软件中。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/known-mainland-bank-account_cn.html", "知道内地银行和账户时先准备什么"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "内地房产怎样放进新加坡遗产清单"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "新加坡遗产代表文件怎样区分"),
                ],
                "cta": "把原始资产、继承文件、变现收款、税务资料和预计入账账户列在一页，我们先检查资金来源链在哪一段中断。",
            },
            "en": {
                "lang": "en",
                "locale": "en_SG",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore families receiving Mainland inheritance proceeds",
                "title": "Before Moving Mainland Inheritance Proceeds to Singapore, Keep the Full Source Trail",
                "description": "A practical guide to preserving the original asset, inheritance, sale or withdrawal, foreign-exchange and receiving-bank records behind Mainland inheritance proceeds.",
                "lead": "The bank sees one incoming payment. Your file should show how a specific estate asset became that payment.",
                "key_title": "Keep four connected files",
                "keys": [
                    "Original asset: property, deposit, shares or another right",
                    "Entitlement: who inherited and who could act",
                    "Conversion: sale, withdrawal, distribution and tax records",
                    "Transfer: approval, bank advice and Singapore credit",
                ],
                "answer_title": "A final remittance receipt is not the whole explanation",
                "answer": [
                    "Sale proceeds from a home should link back to the title, inheritance and sale. A bank deposit should link back to the account and the estate withdrawal. Company-related money may be share-sale proceeds, dividends or a debt owed to the deceased. The final balance alone does not identify the source.",
                    "The Singapore receiving bank may ask about the purpose and source of a material transfer. The Mainland side may also require documents based on the applicant's status, the original asset and the route used. Show both banks a document index before the money moves, rather than rebuilding it after a query.",
                ],
                "sections": [
                    (
                        "1. Start with the estate asset, not the cash balance",
                        [
                            "For property, keep the title evidence, inheritance papers, sale agreement, completion statement and payment record. For a deposit, keep the bank confirmation, estate claim and credit record. For a company interest, separate share ownership, sale proceeds, dividends and shareholder loans.",
                            "Give each asset an identifier. Record the deceased owner, Mainland city, original value, net proceeds and the account that received the money. If several assets are combined, reconcile them in one schedule instead of describing the total as family funds.",
                        ],
                    ),
                    (
                        "2. Connect the beneficiary and the person who acted",
                        [
                            "Keep the death, family, will or intestacy, distribution and authority records that explain who received the asset and who could sell or withdraw it. Where Chinese and English names, old identity documents or married names differ, add a name-matching sheet.",
                            "Do not assume that everyone living in Singapore uses the same Mainland outward-transfer route. Citizenship, permanent residence or another status, the deceased's former household registration and the type of asset may affect the answer. Give the receiving Mainland office the actual identity documents first.",
                        ],
                    ),
                    (
                        "3. Keep the conversion and transfer records together",
                        [
                            "Retain the completion statement, bank statements, payer, receiving account, charges and net amount. Keep the tax or clearance records required for the particular asset. Where the figures differ, reconcile fees, tax, loan repayment and any distribution to another beneficiary.",
                            "Current Mainland inheritance-transfer materials commonly connect the inheritance evidence, the original property right, the conversion explanation and relevant tax records. Do not split the proceeds or relabel them as living expenses or a family loan to avoid questions. State the source and purpose accurately.",
                        ],
                    ),
                    (
                        "4. Ask both banks before the transfer",
                        [
                            "Ask the Mainland remitting bank about the receiving office, applicant, currency, beneficiary name, payment purpose and approval record. Ask the Singapore bank about the exact account name, accepted currencies, intermediary-bank details and source documents it may request for a material credit.",
                            "Singapore banks review whether account activity is consistent with the customer's profile and known source of funds, and may seek clarification. Create a one-page index for each of the four files, keep complete scans and originals, and retain the final remittance and credit advice.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling a Mainland estate"),
                    ("/articles/singapore/known-mainland-bank-account_en.html", "What to prepare when the Mainland bank is known"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Listing Mainland property in a Singapore estate schedule"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate and letters of administration in Singapore"),
                ],
                "cta": "Put the original asset, entitlement, conversion, tax and receiving-account records on one page. We can identify where the source trail is incomplete.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/macau/index.html": (
        "/articles/am/undisputed-or-disputed-route.html",
        '<a href="/articles/am/undisputed-or-disputed-route.html"><span class="v24-tag">路徑分流</span><strong>家屬意見一致和有人反對，要走哪條路</strong><p>先分清已同意、未回覆和明確反對。</p></a>',
    ),
    "articles/macau/index_cn.html": (
        "/articles/am/undisputed-or-disputed-route_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">路径分流</span><h3>家属意见一致和有人反对，要走哪条路</h3><p>先分清已经同意、尚未回复和明确反对。</p></div><a class="v25-pill-action" href="/articles/am/undisputed-or-disputed-route_cn.html">阅读文章</a></article>',
    ),
    "articles/macau/index_en.html": (
        "/articles/am/undisputed-or-disputed-route_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Choose a route</span><h3>When the family agrees — and when someone objects</h3><p>Separate agreement, silence and a real objection.</p></div><a class="v25-pill-action" href="/articles/am/undisputed-or-disputed-route_en.html">Read Article</a></article>',
    ),
    "articles/singapore/index.html": (
        "/articles/singapore/remitting-inherited-funds.html",
        '<a href="/articles/singapore/remitting-inherited-funds.html"><span class="v24-tag">繼承款</span><strong>匯到新加坡前，哪些來源文件不能丟</strong><p>把原始資產到最終入賬的四段資料接起來。</p></a>',
    ),
    "articles/singapore/index_cn.html": (
        "/articles/singapore/remitting-inherited-funds_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">继承款</span><h3>汇到新加坡前，哪些来源文件不能丢</h3><p>把原始资产到最终入账的四段资料连接起来。</p></div><a class="v25-pill-action" href="/articles/singapore/remitting-inherited-funds_cn.html">阅读文章</a></article>',
    ),
    "articles/singapore/index_en.html": (
        "/articles/singapore/remitting-inherited-funds_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Inheritance proceeds</span><h3>Keep the full source trail before a transfer</h3><p>Connect the estate asset to the final Singapore credit.</p></div><a class="v25-pill-action" href="/articles/singapore/remitting-inherited-funds_en.html">Read Article</a></article>',
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
    for base in ("/articles/macau/", "/articles/singapore/"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, SITE + base + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
