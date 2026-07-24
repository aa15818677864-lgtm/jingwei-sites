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
        "slug": "macau-will-mainland-property",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門遺囑與內地房產",
                "title": "澳門遺囑寫到內地房產，家屬先核對哪三件事",
                "description": "澳門遺囑提到內地房產時，家屬先核對最後版本、房產與權利範圍、相關家屬，再安排內地登記需要的文件。",
                "lead": "先不要因為遺囑寫了房子，便直接談由誰過戶。家屬要先確認這是不是最後一份完整遺囑、寫的是哪一套房，以及逝者實際擁有多少權利。",
                "key_title": "先核對三件事",
                "keys": [
                    "手上是不是最後一份完整遺囑，正本或正式內容證明在哪裏",
                    "遺囑所寫房產能否和內地登記資料準確對上",
                    "逝者可處理的權利範圍，以及仍需核對的家屬",
                ],
                "answer_title": "先說最實用的答案",
                "answer": [
                    "遺囑寫到內地房產，第一步不是翻譯，也不是先計算每人的份額。先把遺囑版本、房產資料和家屬關係分成三張小表，看看哪一項仍只是家人口述，哪一項已有文件支持。",
                    "遺囑可以記錄逝者的安排，但不會自行把內地房產轉到受益人名下。內地接收方仍要核對死亡、身份、親屬、房產登記、原有共有權益及其他可能影響辦理的事實。",
                ],
                "sections": [
                    (
                        "一、先找最後版本，不要只看手機照片",
                        [
                            "先記下遺囑日期、形式、頁數、簽署情況和保管地點，再問有沒有較後的遺囑、補充文件或撤回安排。澳門常見遺囑形式不只一種；如果屬於密封或由公證機構保管的遺囑，不要自行拆封或只憑家中的影印本下結論，應先確認正式啟封或取得內容證明的途徑。",
                            "照片可以用來初步辨認，但要檢查有沒有漏頁、背頁、附件、核准部分或手寫更改。正本暫時找不到時，先列明最後見過的人、可能的保管地點和已有副本來源，不要把『家人都看過』當成完整版本證明。",
                        ],
                    ),
                    (
                        "二、把遺囑中的房子和登記資料逐項對上",
                        [
                            "遺囑可能只寫『內地的房子』、舊地址或小區俗稱。家屬要另找房產證、購房合同、貸款資料、物業通知或可核對的登記資料，記下城市、完整地址、登記姓名、份額、證件號碼和是否仍有按揭或其他限制。",
                            "如果逝者有多套房、地址已變更，或遺囑中的姓名與房產證不同，先解決指向哪一項資產的問題。不要為了讓文字看似一致，擅自改寫地址、姓名或份額。",
                        ],
                    ),
                    (
                        "三、遺囑能安排的，只是逝者原本擁有的權利",
                        [
                            "房產只登記在逝者名下，也不宜立即推定整套房都屬於遺產。要看取得時間、婚姻情況、出資、書面財產安排、共有份額及其他人的既有權益。先分清原本屬於逝者的部分，再談遺囑怎樣安排。",
                            "遺囑寫了百分比，也不代表內地登記一定能直接照抄。若房產有共同權利人、按揭、查封、居住安排或來源爭議，這些問題需要和遺囑內容分開核對。",
                        ],
                    ),
                    (
                        "四、仍要畫出完整家屬關係",
                        [
                            "先列配偶、父母、子女，以及早於逝者離世的家屬及其後代；再記錄是否有人失聯、未成年、不同意或持有另一份遺囑。有些近親即使沒有在遺囑中獲分財產，仍可能需要核對其權益，所以這不是否定遺囑，而是避免漏掉仍可能影響辦理的人。",
                            "如果有人質疑遺囑真實性、簽署能力或最後版本，先保存正本、信封、保管記錄、醫療資料和相關通訊。此時不要把爭議當成一般補文件，也不要催促家屬先簽一份看不懂的分配聲明。",
                        ],
                    ),
                    (
                        "五、最後才安排翻譯和內地用件",
                        [
                            "把遺囑形式和日期、正本位置、房產城市和地址、登記姓名、家屬關係及現有澳門文件放在一頁。先交給房產所在地的接收方確認：需要整份還是內容證明、需要哪種中文文本，以及身份差異怎樣連接。",
                            "翻譯只能說明文字，不能補出遺囑正本、房產權利或家屬關係。先問清接收目的再辦文件，通常比把手上所有資料一次過翻譯更省時間。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-heir-qualification-deed.html", "澳門繼承資格公證書何時真正有用"),
                    ("/articles/am/macau-kinship-certificate-scope.html", "親屬關係證明能說明甚麼"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門家屬處理內地房產的起步方法"),
                ],
                "cta": "先說明遺囑日期和形式、正本位置、房產城市、登記姓名和家屬關係，再判斷哪項資料應先補齊。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门遗嘱与内地房产",
                "title": "澳门遗嘱写到内地房产，家属先核对哪三件事",
                "description": "澳门遗嘱提到内地房产时，家属先核对最后版本、房产与权利范围、相关家属，再准备内地登记需要的文件。",
                "lead": "先不要因为遗嘱写了房子，就直接谈由谁过户。家属要先确认这是不是最后一份完整遗嘱、写的是哪一套房，以及逝者实际拥有多少权利。",
                "key_title": "先核对三件事",
                "keys": [
                    "手上是不是最后一份完整遗嘱，原件或正式内容证明在哪里",
                    "遗嘱所写房产能不能和内地登记资料准确对应",
                    "逝者可以处理的权利范围，以及仍需核对的家属",
                ],
                "answer_title": "先说最实用的答案",
                "answer": [
                    "遗嘱写到内地房产，第一步不是翻译，也不是先计算每个人的份额。先把遗嘱版本、房产资料和家属关系分成三张小表，看看哪些还只是家人口述，哪些已经有文件支持。",
                    "遗嘱可以记录逝者的安排，但不会自动把内地房产转到受益人名下。内地接收方仍会核对死亡、身份、亲属、房产登记、原有共有权益以及其他可能影响办理的事实。",
                ],
                "sections": [
                    (
                        "一、先找最后版本，不要只看手机照片",
                        [
                            "先记下遗嘱日期、形式、页数、签署情况和保管地点，再问有没有更晚的遗嘱、补充文件或撤回安排。澳门常见遗嘱形式不只一种；如果属于密封或由公证机构保管的遗嘱，不要自行拆封或只凭家中的复印件下结论，应先确认正式启封或取得内容证明的途径。",
                            "照片可以用来初步辨认，但要检查有没有漏页、背页、附件、核准部分或手写更改。原件暂时找不到时，先列出最后见过的人、可能的保管地点和已有副本来源，不要把“家人都看过”当成完整版本证明。",
                        ],
                    ),
                    (
                        "二、把遗嘱中的房子和登记资料逐项对应",
                        [
                            "遗嘱可能只写“内地的房子”、旧地址或小区俗称。家属要另找房产证、购房合同、贷款资料、物业通知或可核对的登记资料，记下城市、完整地址、登记姓名、份额、证件号码和是否仍有按揭或其他限制。",
                            "如果逝者有多套房、地址已经变更，或遗嘱中的姓名与房产证不同，先解决究竟指向哪一项资产的问题。不要为了让文字看起来一致，擅自改写地址、姓名或份额。",
                        ],
                    ),
                    (
                        "三、遗嘱能安排的，只是逝者原本拥有的权利",
                        [
                            "房产只登记在逝者名下，也不能立即推定整套房都属于遗产。要看取得时间、婚姻情况、出资、书面财产安排、共有份额以及其他人的既有权益。先分清原本属于逝者的部分，再谈遗嘱如何安排。",
                            "遗嘱写了百分比，也不代表内地登记一定能够直接照抄。房产如有共同权利人、按揭、查封、居住安排或来源争议，这些问题需要与遗嘱内容分开核对。",
                        ],
                    ),
                    (
                        "四、仍要画出完整家属关系",
                        [
                            "先列配偶、父母、子女，以及先于逝者去世的家属和他们的后代；再记录是否有人失联、未成年、不同意或持有另一份遗嘱。有些近亲即使没有在遗嘱里分到财产，仍可能需要核对其权益，所以这不是否定遗嘱，而是为了避免漏掉仍可能影响办理的人。",
                            "如果有人质疑遗嘱真伪、签署能力或最后版本，先保存原件、信封、保管记录、医疗资料和相关沟通。此时不要把争议当成普通补文件，也不要催促家属先签一份看不懂的分配声明。",
                        ],
                    ),
                    (
                        "五、最后再安排翻译和内地用件",
                        [
                            "把遗嘱形式和日期、原件位置、房产城市和地址、登记姓名、家属关系以及现有澳门文件放在一页。先交给房产所在地的接收方确认：需要整份还是内容证明、需要哪种中文文本，以及身份差异怎样连接。",
                            "翻译只能说明文字，不能补出遗嘱原件、房产权利或家属关系。先问清接收目的再办理文件，通常比把手上所有资料一次性翻译更省时间。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-heir-qualification-deed_cn.html", "澳门继承资格公证书何时真正有用"),
                    ("/articles/am/macau-kinship-certificate-scope_cn.html", "亲属关系证明能够说明什么"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门家属处理内地房产的起步方法"),
                ],
                "cta": "先说明遗嘱日期和形式、原件位置、房产城市、登记姓名和家属关系，再判断哪项资料应该先补齐。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau wills and Mainland property",
                "title": "A Macau Will Mentions Mainland Property: Three Checks Before You Act",
                "description": "A practical first review of the final will, the exact Mainland property, the deceased's ownership and the family members who may still matter.",
                "lead": "A reference to the home in a will is not the same as a completed transfer. First confirm the final will, identify the exact property and establish what interest the deceased actually owned.",
                "key_title": "Make these three checks",
                "keys": [
                    "The final complete will and the location of the original or official record",
                    "The exact Mainland property described by the will",
                    "The deceased's own interest and the family members still to be checked",
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "Do not begin with translation or a calculation of shares. Make three short records: one for the will and its versions, one for the property, and one for the family. Mark which facts are supported by documents and which remain family recollections.",
                    "A will records the deceased's intentions. It does not by itself update a Mainland title. The receiving side will still need to connect the death, identities, family, title record, existing co-ownership and any other issue affecting the property.",
                ],
                "sections": [
                    (
                        "1. Find the final version, not just a phone photograph",
                        [
                            "Record the date, form, number of pages, signatures and place of safekeeping. Ask whether there was a later will, codicil or revocation. Macau recognises more than one form of will. If the will is sealed or held through a notarial office, confirm the proper opening or record process rather than opening it informally or relying on a household copy.",
                            "A photograph can help identify the document, but check for reverse pages, attachments, approval wording and handwritten changes. If the original is missing, list who last saw it, where it may be stored and where each copy came from.",
                        ],
                    ),
                    (
                        "2. Match the property to the Mainland title record",
                        [
                            "A will may refer only to 'my home in China', an old address or a development's informal name. Use the title certificate, purchase contract, mortgage papers, property-management notices or a current title enquiry to record the city, full address, registered name, share, identity number and restrictions.",
                            "If the deceased owned several homes, the address changed, or the name in the will differs from the title, resolve that link before translating. Do not quietly rewrite names, addresses or percentages to make the records appear consistent.",
                        ],
                    ),
                    (
                        "3. A will can deal only with the deceased's own interest",
                        [
                            "A sole name on the title is an important fact, but it does not always establish that the entire home belongs to the estate. Check acquisition, marriage, funding, written property arrangements, co-ownership and any existing interest of another person.",
                            "A percentage stated in the will may not be a percentage that the Mainland registry can simply copy. A co-owner, mortgage, court restriction, occupation arrangement or dispute about the source of funds must be reviewed separately from the will's wording.",
                        ],
                    ),
                    (
                        "4. Map the full family before choosing a filing route",
                        [
                            "List the spouse, parents and children, together with any relative who died earlier and their descendants. Note anyone who is missing, under age, in disagreement or holding another testamentary document. Certain close relatives may still have interests to check even if the will gives them nothing. This review does not disregard the will; it prevents a relevant person or document from being overlooked.",
                            "If the will's authenticity, capacity or finality is challenged, preserve the original, envelope, safekeeping record, medical material and communications. Do not treat that dispute as an ordinary missing-document exercise or press relatives to sign a distribution paper they do not understand.",
                        ],
                    ),
                    (
                        "5. Ask what the Mainland recipient needs before translating",
                        [
                            "Put the will's form and date, original location, property city and address, registered name, family map and available Macau records on one page. Ask the recipient in the property city whether it needs the complete will or an official record of its contents, what Chinese text is accepted and how name differences should be connected.",
                            "Translation can explain words. It cannot supply the original will, ownership or family evidence. Confirming the receiving purpose first is usually more useful than translating every document in the family's possession.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling Mainland estates"),
                    ("/articles/am/macau-heir-qualification-deed_en.html", "When a Macau heir qualification deed is useful"),
                    ("/articles/am/macau-kinship-certificate-scope_en.html", "What a kinship certificate can establish"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "A starting route for Macau families"),
                ],
                "cta": "Start with the will's date and form, location of the original, property city, title name and family map. Those facts show what must be verified next.",
            },
        },
    },
    {
        "slug": "mortgaged-mainland-property",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與內地按揭房產",
                "title": "內地房產仍有按揭，新加坡繼承人先取得哪些資料",
                "description": "新加坡家屬處理仍有按揭的內地房產時，先核對登記、貸款餘額、還款狀態、借款人與銀行要求，再判斷下一步。",
                "lead": "房主離世，不代表貸款自動消失，也不代表家屬現在就應自行清還全部款項。先把房產、抵押登記和貸款現況查清楚，再和銀行及房產所在地確認可行路徑。",
                "key_title": "先拿到這三組資料",
                "keys": [
                    "房產登記姓名、地址、份額和現有抵押狀態",
                    "貸款合同、剩餘本金、欠款和最近還款記錄",
                    "借款人、共同借款人、保證人及銀行聯絡窗口",
                ],
                "answer_title": "先說結論",
                "answer": [
                    "把『房產歸誰』、『欠銀行多少』和『銀行是否同意下一步安排』分開處理。繼承文件可證明家屬在遺產程序中的身份，但不會自動更改內地借款合同、抵押登記或銀行內部審批；家屬也不會只因為是繼承人便自動成為共同借款人。",
                    "第一輪資料不需要很複雜：一份可核對的房產登記、一份最新貸款資料、一張還款時間線和一個銀行正式聯絡窗口。未看清這四項前，不要只憑月供金額推算餘額，也不要用逝者的網上銀行帳戶自行操作。",
                ],
                "sections": [
                    (
                        "一、先看房產和抵押登記，不要只看房產證照片",
                        [
                            "記下城市、完整地址、登記姓名、證件號碼、份額、房產證或不動產權證資料。再確認目前登記的抵押權人、抵押範圍，以及有沒有查封、共有或其他限制。舊房產證照片未必反映現在狀態。",
                            "如果家屬只知道小區名或只有按揭短訊，先找購房合同、貸款合同、物業記錄、供款帳戶或房產所在地的查詢線索。先鎖定是哪一套房和哪一筆貸款，避免把兩筆債務混在一起。",
                        ],
                    ),
                    (
                        "二、向銀行問的是現況，不是先承諾怎樣還",
                        [
                            "準備借款合同編號、借款人和共同借款人姓名、貸款銀行和辦理分行，再請銀行提供可核對的剩餘本金、利息、是否逾期、下一個還款日、還款帳戶及是否有相關保險。不要只看很久以前的還款計劃表。",
                            "銀行通常要先核對查詢人的身份和文件，才會提供具體帳戶資料。第一次聯絡可以先問受理部門、所需文件和安全提交方式；不要在普通電郵、聊天群或公開表格中傳送完整帳號、密碼或一次性驗證碼。",
                        ],
                    ),
                    (
                        "三、做一條還款時間線，避免突然斷掉資訊",
                        [
                            "列出最近一次成功扣款、每月到期日、供款來源、帳戶餘額、已收到的催款或保險通知，以及目前由誰保管合同和銀行卡。這張表的作用是讓家屬知道發生了甚麼，不是替銀行或所有繼承人作付款決定。",
                            "不要把繼續供款、暫停供款或一次清還當成固定答案。不同合同、逾期狀態、共同借款人和保險安排會改變處理方式；需要先取得銀行對具體帳戶的書面說明。",
                        ],
                    ),
                    (
                        "四、新加坡遺產文件和內地按揭資料要互相對上",
                        [
                            "新加坡遺產程序通常會整理資產，也會關注有抵押擔保的債務。核對內地房產是否已列入資產資料、地址和估值從哪裏取得，以及按揭資料是否仍待補充。這有助遺產代表掌握整體，但不代替內地銀行和登記機構的要求。",
                            "新加坡法院發出的遺產代表文件（例如 Grant）、遺囑或資產清單，可以說明新加坡一邊的程序和代表身份；它們不會自行把借款人改名，也不會讓抵押自動註銷。文件用途要逐項問清，避免把同一份文件交到不同地方便假設作用相同。",
                        ],
                    ),
                    (
                        "五、最後才比較三種可能路徑",
                        [
                            "常見方向可能包括先結清再辦抵押註銷、由銀行評估債務或借款安排，或在銀行和當地登記條件允許時連同抵押狀態辦理轉移。這些只是待確認的方向，不是每個城市、每家銀行都會接受。",
                            "把房產登記、貸款現況、還款時間線、新加坡遺產代表文件和家屬意向放在同一頁，分別問銀行和房產所在地接收方。兩邊都回答後，才適合比較費用、時間和風險。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "資產清單怎樣列內地房產"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "Grant of Probate 和 Letters of Administration 的用途"),
                    ("/articles/singapore/mainland-property-inheritance.html", "新加坡家屬繼承內地房產先查甚麼"),
                ],
                "cta": "先準備房產地址、登記姓名、貸款銀行、合同編號、最近還款和新加坡遺產代表文件，再分別向銀行與房產所在地確認。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与内地按揭房产",
                "title": "内地房产仍有按揭，新加坡继承人先取得哪些资料",
                "description": "新加坡家属处理仍有按揭的内地房产时，先核对登记、贷款余额、还款状态、借款人与银行要求，再判断下一步。",
                "lead": "房主去世，不代表贷款自动消失，也不代表家属现在就应该自行还清全部款项。先把房产、抵押登记和贷款现状查清，再和银行以及房产所在地确认可行路径。",
                "key_title": "先拿到这三组资料",
                "keys": [
                    "房产登记姓名、地址、份额和现有抵押状态",
                    "贷款合同、剩余本金、欠款和最近还款记录",
                    "借款人、共同借款人、保证人以及银行联系窗口",
                ],
                "answer_title": "先说结论",
                "answer": [
                    "把“房产归谁”、“欠银行多少”和“银行是否同意下一步安排”分开处理。继承文件可以证明家属在遗产程序中的身份，但不会自动更改内地借款合同、抵押登记或银行内部审批；家属也不会只因为是继承人就自动成为共同借款人。",
                    "第一轮资料不需要很复杂：一份可以核对的房产登记、一份最新贷款资料、一张还款时间线和一个银行正式联系窗口。没有看清这四项之前，不要只凭月供金额推算余额，也不要使用逝者的网上银行账户自行操作。",
                ],
                "sections": [
                    (
                        "一、先看房产和抵押登记，不要只看房产证照片",
                        [
                            "记下城市、完整地址、登记姓名、证件号码、份额、房产证或不动产权证资料。再确认目前登记的抵押权人、抵押范围，以及有没有查封、共有或其他限制。旧房产证照片未必反映现在的状态。",
                            "如果家属只知道小区名或只有按揭短信，先找购房合同、贷款合同、物业记录、还款账户或房产所在地的查询线索。先锁定究竟是哪一套房和哪一笔贷款，避免把两笔债务混在一起。",
                        ],
                    ),
                    (
                        "二、向银行问的是现状，不是先承诺怎样还款",
                        [
                            "准备借款合同编号、借款人和共同借款人姓名、贷款银行和办理分行，再请银行提供可以核对的剩余本金、利息、是否逾期、下一个还款日、还款账户以及是否有相关保险。不要只看很久以前的还款计划表。",
                            "银行通常要先核对查询人的身份和文件，才会提供具体账户资料。第一次联系可以先问受理部门、所需文件和安全提交方式；不要在普通邮件、聊天群或公开表格里发送完整账号、密码或一次性验证码。",
                        ],
                    ),
                    (
                        "三、做一条还款时间线，避免突然失去信息",
                        [
                            "列出最近一次成功扣款、每月到期日、还款来源、账户余额、已经收到的催款或保险通知，以及目前由谁保管合同和银行卡。这张表是为了让家属知道发生了什么，并不是替银行或所有继承人作付款决定。",
                            "不要把继续还款、暂停还款或一次性结清当成固定答案。不同合同、逾期状态、共同借款人和保险安排会改变处理方式；需要先取得银行针对具体账户的书面说明。",
                        ],
                    ),
                    (
                        "四、新加坡遗产文件和内地按揭资料要相互对应",
                        [
                            "新加坡遗产程序通常会整理资产，也会关注有抵押担保的债务。核对内地房产是否已经列入资产资料、地址和估值来自哪里，以及按揭资料是否仍待补充。这有助于遗产代表掌握整体情况，但不能代替内地银行和登记机构的要求。",
                            "新加坡法院发出的遗产代表文件（例如 Grant）、遗嘱或资产清单，可以说明新加坡一侧的程序和代表身份；它们不会自动把借款人改名，也不会让抵押自动注销。文件用途要逐项问清，不能把同一份文件交到不同地方就假设作用相同。",
                        ],
                    ),
                    (
                        "五、最后再比较三种可能路径",
                        [
                            "常见方向可能包括先结清再办理抵押注销、由银行评估债务或借款安排，或者在银行和当地登记条件允许时连同抵押状态办理转移。这些只是需要确认的方向，并不是每个城市、每家银行都会接受。",
                            "把房产登记、贷款现状、还款时间线、新加坡遗产代表文件和家属意向放在同一页，分别询问银行和房产所在地接收方。两边都有回答之后，才适合比较费用、时间和风险。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "资产清单怎样列内地房产"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "Grant of Probate 和 Letters of Administration 的用途"),
                    ("/articles/singapore/mainland-property-inheritance_cn.html", "新加坡家属继承内地房产先查什么"),
                ],
                "cta": "先准备房产地址、登记姓名、贷款银行、合同编号、最近还款和新加坡遗产代表文件，再分别向银行与房产所在地确认。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore families and mortgaged Mainland property",
                "title": "Mainland Home Still Mortgaged: What Singapore Heirs Should Check",
                "description": "A practical fact check for Singapore families dealing with a mortgaged Mainland home: title, balance, repayments, borrowers and the lender's process.",
                "lead": "The owner's death does not make the loan disappear, but it also does not tell the family to pay everything immediately. Establish the title, registered mortgage and current loan position before choosing a route.",
                "key_title": "Collect these three groups of facts",
                "keys": [
                    "The registered owner, address, share and current mortgage entry",
                    "The loan agreement, current balance, arrears and recent repayments",
                    "Every borrower, co-borrower and guarantor, plus a verified lender contact",
                ],
                "answer_title": "The short answer",
                "answer": [
                    "Treat ownership, the debt balance and the lender's consent as three separate questions. Singapore estate papers may establish a representative's role, but they do not automatically amend a Mainland loan agreement, mortgage registration or bank approval. A relative does not become a co-borrower merely by being an heir.",
                    "The first review can be simple: obtain a reliable title record, current loan information, a repayment timeline and a verified contact at the lender. Do not estimate the balance from the monthly instalment or try to operate the deceased's online banking account.",
                ],
                "sections": [
                    (
                        "1. Read the title and mortgage records together",
                        [
                            "Record the city, full address, registered owner, identity number, share and title certificate details. Check the registered mortgagee, the scope of the mortgage and any court restriction, co-owner or other registered limitation. An old photograph of a title certificate may not show the current position.",
                            "If the family knows only the development name or has a loan text message, look for the purchase contract, loan agreement, property-management records, repayment account or a local title enquiry. Match the correct home to the correct loan before discussing the debt.",
                        ],
                    ),
                    (
                        "2. Ask the lender for facts before promising a payment plan",
                        [
                            "Prepare the loan number, names of the borrower and co-borrower, the lender and the original branch. Ask for a verifiable statement of principal, interest, arrears, next due date, repayment account and any linked insurance. An old amortisation schedule is not a current balance.",
                            "The lender will usually verify the enquirer's identity and authority before disclosing account details. The first contact can ask which team handles the matter, what documents are required and how to submit them securely. Never send a full account number, password or one-time code through a public form or family chat.",
                        ],
                    ),
                    (
                        "3. Build a repayment timeline without making assumptions",
                        [
                            "Record the last successful payment, monthly due date, source of funds, available account information, any arrears or insurance notice, and who holds the agreement and bank card. The timeline helps the family understand events; it does not make a payment decision for the lender or every heir.",
                            "Continuing payments, pausing them or paying the balance in full is not a universal answer. The agreement, arrears, co-borrower and insurance position may change the route. Obtain instructions for the actual account before acting.",
                        ],
                    ),
                    (
                        "4. Connect the Singapore estate file to the Mainland facts",
                        [
                            "A Singapore probate file commonly identifies estate assets and may also record debts secured by mortgage. Check whether the Mainland home has been included, where its address and value came from, and whether the mortgage information remains incomplete. This helps the estate representative see the whole estate, but does not replace the Mainland lender's requirements.",
                            "A Singapore court grant, will or Schedule of Assets can explain the local estate proceeding and the representative's role. It does not substitute a borrower, remove the registered mortgage or secure the lender's approval. Ask what each recipient needs rather than assuming one document has the same effect everywhere.",
                        ],
                    ),
                    (
                        "5. Compare possible routes only after both sides respond",
                        [
                            "Possible routes may include repayment followed by mortgage cancellation, a lender review of the loan arrangements, or a transfer with the mortgage continuing where the lender and local registration process permit it. These are questions to investigate, not options available in every city or bank.",
                            "Put the title, current loan position, repayment timeline, Singapore representative papers and family intention on one page. Ask the lender and the receiving office in the property city separately. Their answers provide the basis for comparing time, cost and risk.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling Mainland estates"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Recording Mainland property in a Schedule of Assets"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "What a probate or administration grant establishes"),
                    ("/articles/singapore/mainland-property-inheritance_en.html", "First checks for a Mainland property inheritance"),
                ],
                "cta": "Start with the property address, title name, lender, loan number, recent repayments and Singapore representative papers, then ask the lender and property-city recipient separately.",
            },
        },
    },
]


def write_articles() -> None:
    for article in ARTICLES:
        target_dir = ROOT / article["directory"]
        for lang in ("tc", "cn", "en"):
            target = target_dir / f"{article['slug']}{LANG_SUFFIX[lang]}.html"
            target.write_text(render_article(article, lang), encoding="utf-8")


HUB_UPDATES = {
    "articles/macau/index.html": [
        (
            "/articles/am/macau-will-mainland-property.html",
            '<a href="/articles/am/macau-will-mainland-property.html"><span class="v24-tag">遺囑核對</span><strong>澳門遺囑寫到內地房產，家屬先核對哪三件事</strong><p>先找最後版本、對準房產，再分清逝者真正擁有的權利。</p></a>',
        ),
    ],
    "articles/macau/index_cn.html": [
        (
            "/articles/am/macau-will-mainland-property_cn.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">遗嘱核对</span><h3>澳门遗嘱写到内地房产，家属先核对哪三件事</h3><p>先找最后版本、对应房产，再分清逝者真正拥有的权利。</p></div><a class="v25-pill-action" href="/articles/am/macau-will-mainland-property_cn.html">阅读文章</a></article>',
        ),
    ],
    "articles/macau/index_en.html": [
        (
            "/articles/am/macau-will-mainland-property_en.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Will review</span><h3>A Macau will mentions Mainland property: three checks</h3><p>Find the final will, identify the property and establish the deceased\'s actual interest.</p></div><a class="v25-pill-action" href="/articles/am/macau-will-mainland-property_en.html">Read Article</a></article>',
        ),
    ],
    "articles/singapore/index.html": [
        (
            "/articles/singapore/mortgaged-mainland-property.html",
            '<a href="/articles/singapore/mortgaged-mainland-property.html"><span class="v24-tag">按揭房產</span><strong>內地房產仍有按揭，新加坡繼承人先取得哪些資料</strong><p>先核對登記、餘額、還款和銀行窗口，再比較下一步。</p></a>',
        ),
    ],
    "articles/singapore/index_cn.html": [
        (
            "/articles/singapore/mortgaged-mainland-property_cn.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">按揭房产</span><h3>内地房产仍有按揭，新加坡继承人先取得哪些资料</h3><p>先核对登记、余额、还款和银行窗口，再比较下一步。</p></div><a class="v25-pill-action" href="/articles/singapore/mortgaged-mainland-property_cn.html">阅读文章</a></article>',
        ),
    ],
    "articles/singapore/index_en.html": [
        (
            "/articles/singapore/mortgaged-mainland-property_en.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Mortgaged property</span><h3>Mainland home still mortgaged: first checks</h3><p>Verify the title, balance, repayments and lender contact before choosing a route.</p></div><a class="v25-pill-action" href="/articles/singapore/mortgaged-mainland-property_en.html">Read Article</a></article>',
        ),
    ],
}


def update_hubs() -> None:
    for relative_path, updates in HUB_UPDATES.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        traditional = relative_path.endswith("index.html")
        marker = '<details class="v24-article-more"' if traditional else '<details class="v25-article-more"'
        if marker not in text:
            raise RuntimeError(f"Hub insertion marker missing: {relative_path}")
        for href, card in updates:
            href_at = text.find(href)
            if href_at < 0:
                text = text.replace(marker, card + marker, 1)
                continue
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
