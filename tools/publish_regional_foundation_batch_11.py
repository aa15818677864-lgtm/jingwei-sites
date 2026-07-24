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
        "slug": "portuguese-documents-translation",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_MO",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門與內地遺產",
                "title": "澳門葡文文件交到內地前，翻譯最容易漏掉甚麼",
                "description": "澳門家屬整理葡文死亡、婚姻或公證文件時，先核對姓名、日期、附註、印章和譯本用途，避免翻完仍被要求重做。",
                "lead": "不要只翻正文。文件名稱、編號、姓名、日期、邊註、印章和簽署身份，任何一項漏掉都可能令內地接收方看不懂文件。",
                "key_title": "先記住三件事",
                "keys": [
                    "先問清楚內地接收方要證明哪一件事",
                    "先做姓名和日期對照，再開始翻譯",
                    "翻譯、譯本證明和文件接納是三個問題",
                ],
                "answer_title": "先說最直接的做法",
                "answer": [
                    "先把葡文原件或認證副本完整掃描，再列一張姓名、日期和文件編號對照表。翻譯時不只處理大段正文，頁眉、附註、手寫內容、印章、簽署人職務和背頁也要逐項看。",
                    "澳門的譯本證明程序要同時交原文正本或認證繕本和譯本，而且原文或譯本其中一份須為中文或葡文。辦好譯本證明仍不等於內地每一個接收單位都接受同一份材料，所以要先問用途和接收要求。",
                ],
                "sections": [
                    (
                        "先辨認手上究竟是哪一份文件",
                        [
                            "先寫下文件正式名稱、簽發機關、簽發日期、頁數和編號。死亡紀錄、婚姻紀錄、出生紀錄、公證書和物業資料回答的問題不同，不要只按封面顏色或家人口頭叫法分類。",
                            "同一項登記可能有簡短證明、較完整副本或後加附註，頁數和內容範圍並不一樣。先讓內地接收方確認它要看死亡事實、親屬關係、婚姻狀況還是代表身份，才知道應取哪個版本。",
                        ],
                    ),
                    (
                        "翻譯前先做一張姓名和日期表",
                        [
                            "把每名相關人士的葡文姓名、中文姓名、證件號碼、出生日期和身份關係放在同一行。不要自行把葡文姓名猜成一個看似接近的中文姓名；有舊證件、出生證明或婚姻文件時，先用原有記錄對照。",
                            "日期要同時看日、月、年排列和文件語境。門牌、堂區、簽發地、卷宗號、登記號和頁碼也不要省略。譯者看不清的字應先回到清晰原件核對，不宜用最可能的答案補上。",
                        ],
                    ),
                    (
                        "正文之外最容易漏掉的內容",
                        [
                            "最常被忽略的是頁邊附註、背頁續文、刪改標記、騎縫位置、印章文字、簽署人職務和證明語。這些內容可能說明婚姻變更、姓名更新、文件副本性質或簽發權限，不能只當作版面裝飾。",
                            "翻譯完成後逐頁對照：原文每一個可見文字區域，在譯本是否都有對應；譯本每一個姓名和數字，能否在原文找到來源。空白、看不清或不適用的地方，要用一致方式標示，不要悄悄省略。",
                        ],
                    ),
                    (
                        "翻譯、證明和接納不要混在一起",
                        [
                            "翻譯先回答文字是甚麼意思；譯本證明處理譯者對譯文忠於原文的聲明；內地接收方則按具體用途判斷文件版本和材料組合是否足夠。完成其中一步，不代表另外兩步自然完成。",
                            "如果接收方要求中文譯本，先問是否指定譯者資格、是否要連同原件或認證副本、姓名採用哪一種寫法，以及印章和附註是否必須全譯。不要在要求未清楚時只翻一個節錄。",
                        ],
                    ),
                    (
                        "交件前做一次雙向核對",
                        [
                            "從原文往譯本查一次，確定沒有漏頁、漏章、漏附註；再從譯本回到原文查一次，確定沒有多寫、猜寫或改變身份關係。最後把姓名表交給家屬再看，特別留意同一人有多種拼音或婚前姓名的情況。",
                            "交件包可包括完整原文、完整譯本、姓名日期對照表和接收方要求的其他證明。每份文件分開編號，不要把不同人的記錄混成一個檔案，日後補件會容易很多。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance.html", "澳門死亡紀錄交到內地前先核對甚麼"),
                    ("/articles/am/macau-kinship-certificate-scope.html", "澳門親屬關係文件能證明甚麼"),
                    ("/articles/am/macau-heir-qualification-deed.html", "確認繼承人資格文件甚麼時候值得先辦"),
                ],
                "cta": "把葡文文件首頁、背頁、印章頁和姓名資料放在一起，先說明內地用途，才容易判斷翻譯範圍。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门与内地遗产",
                "title": "澳门葡文文件交到内地前，翻译最容易漏掉什么",
                "description": "澳门家属整理葡文死亡、婚姻或公证文件时，先核对姓名、日期、附注、印章和译本用途，避免翻完仍被要求重做。",
                "lead": "不要只翻正文。文件名称、编号、姓名、日期、边注、印章和签署身份，任何一项漏掉都可能让内地接收方看不懂文件。",
                "key_title": "先记住三件事",
                "keys": [
                    "先问清内地接收方要证明哪件事",
                    "先做姓名和日期对照，再开始翻译",
                    "翻译、译本证明和文件接纳是三个问题",
                ],
                "answer_title": "先说最直接的做法",
                "answer": [
                    "先把葡文原件或认证副本完整扫描，再列一张姓名、日期和文件编号对照表。翻译时不只处理大段正文，页眉、附注、手写内容、印章、签署人职务和背页也要逐项查看。",
                    "澳门的译本证明程序要同时提交原文正本或认证缮本和译本，而且原文或译本其中一份须为中文或葡文。办好译本证明仍不等于内地每个接收单位都接受同一份材料，所以要先问用途和接收要求。",
                ],
                "sections": [
                    (
                        "先辨认手上究竟是哪份文件",
                        [
                            "先写下文件正式名称、签发机构、签发日期、页数和编号。死亡记录、婚姻记录、出生记录、公证书和物业资料回答的问题不同，不要只按封面颜色或家人口头叫法分类。",
                            "同一项登记可能有简短证明、较完整副本或后来增加的附注，页数和内容范围并不一样。先让内地接收方确认它要看死亡事实、亲属关系、婚姻状况还是代表身份，才知道应该取得哪个版本。",
                        ],
                    ),
                    (
                        "翻译前先做一张姓名和日期表",
                        [
                            "把每名相关人员的葡文姓名、中文姓名、证件号码、出生日期和身份关系放在同一行。不要自行把葡文姓名猜成一个看起来接近的中文姓名；有旧证件、出生证明或婚姻文件时，先用原有记录对照。",
                            "日期要同时看日、月、年排列和文件语境。门牌、堂区、签发地、卷宗号、登记号和页码也不要省略。译者看不清的字应先回到清晰原件核对，不宜用最可能的答案补上。",
                        ],
                    ),
                    (
                        "正文之外最容易漏掉的内容",
                        [
                            "最常被忽略的是页边附注、背页续文、删改标记、骑缝位置、印章文字、签署人职务和证明语。这些内容可能说明婚姻变化、姓名更新、文件副本性质或签发权限，不能只当成版面装饰。",
                            "翻译完成后逐页对照：原文每个可见文字区域，在译本中是否都有对应；译本中的每个姓名和数字，能否在原文找到来源。空白、看不清或不适用的地方，要用一致方式标明，不要直接省略。",
                        ],
                    ),
                    (
                        "翻译、证明和接纳不要混在一起",
                        [
                            "翻译先回答文字是什么意思；译本证明处理译者对译文忠于原文的声明；内地接收方则按具体用途判断文件版本和材料组合是否足够。完成其中一步，不代表另外两步自然完成。",
                            "如果接收方要求中文译本，先问是否指定译者资格、是否要连同原件或认证副本、姓名采用哪种写法，以及印章和附注是否必须全部翻译。不要在要求不清楚时只翻一个节选。",
                        ],
                    ),
                    (
                        "交件前做一次双向核对",
                        [
                            "从原文向译本检查一次，确定没有漏页、漏章、漏附注；再从译本回到原文检查一次，确定没有多写、猜写或改变身份关系。最后把姓名表交给家属再看，尤其留意同一人有多种拼音或婚前姓名的情况。",
                            "交件材料可以包括完整原文、完整译本、姓名日期对照表和接收方要求的其他证明。每份文件分开编号，不要把不同人员的记录混成一个文件，日后补件会容易很多。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_cn.html", "澳门死亡记录交到内地前先核对什么"),
                    ("/articles/am/macau-kinship-certificate-scope_cn.html", "澳门亲属关系文件能证明什么"),
                    ("/articles/am/macau-heir-qualification-deed_cn.html", "确认继承人资格文件什么时候值得先办"),
                ],
                "cta": "把葡文文件首页、背页、印章页和姓名资料放在一起，先说明内地用途，才容易判断翻译范围。",
            },
            "en": {
                "lang": "en",
                "locale": "en_MO",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau and Mainland estates",
                "title": "Using a Macau Portuguese Estate Document in the Mainland: What Must Be Translated?",
                "description": "A practical guide to translating Macau Portuguese death, marriage and notarial records for Mainland estate use without losing names, dates, annotations or seals.",
                "lead": "Do not translate only the main paragraphs. A title, record number, name, marginal note, seal or signer's capacity may be the detail the Mainland recipient needs.",
                "key_title": "Three points to remember",
                "keys": [
                    "Ask what the Mainland recipient needs proved",
                    "Build a name and date table before translating",
                    "Translation, certification and acceptance are separate questions",
                ],
                "answer_title": "A practical starting point",
                "answer": [
                    "Make a complete scan of the Portuguese original or certified transcript, then prepare a table of names, dates and document numbers. The translation should cover headings, annotations, handwriting, seals, the signer's official capacity and any text on the reverse, not only the longest paragraphs.",
                    "For a Macau translation certificate, the source original or certified transcript and the translation are submitted together, and either the source or translation must be in Chinese or Portuguese. The certificate does not decide whether every Mainland recipient will accept the same document set, so confirm the purpose and recipient requirements first.",
                ],
                "sections": [
                    (
                        "Identify the exact record before translating it",
                        [
                            "Record the formal document name, issuing office, issue date, page count and reference number. A death record, marriage record, birth record, notarial instrument and property record answer different questions. Do not classify a document only by its cover or the name relatives use for it.",
                            "The same registration may be available as a short certificate, a fuller copy or a record carrying later annotations. They do not contain the same range of information. Ask whether the Mainland recipient needs evidence of death, kinship, marital status or representative authority before choosing the version.",
                        ],
                    ),
                    (
                        "Build a name and date table first",
                        [
                            "Place each person's Portuguese name, Chinese name, identity number, date of birth and family role on one line. Do not invent a Chinese form because it sounds similar to the Portuguese name. Compare existing identity papers, birth records and marriage papers whenever available.",
                            "Check whether dates follow day-month-year order and read them in context. Preserve address numbers, parish names, place of issue, file references, registration numbers and page numbers. If a word is unclear, return to a better copy instead of inserting the most likely guess.",
                        ],
                    ),
                    (
                        "The details most often missed outside the main text",
                        [
                            "Marginal notes, continuation text on the reverse, deletion marks, text crossing a page joint, seal wording, the signer's title and certification clauses are easy to overlook. They may record a marriage change, updated name, the nature of a copy or the issuing authority. They are not decorative elements.",
                            "Review page by page in both directions. Every visible text area in the source should have a treatment in the translation, and every name and number in the translation should be traceable to the source. Use a consistent notation for blanks, illegible text and entries that do not apply.",
                        ],
                    ),
                    (
                        "Keep translation, certification and acceptance separate",
                        [
                            "Translation explains the words. Certification addresses the translator's statement that the translated text is faithful to the source. The Mainland recipient decides whether the version and the complete evidence set are suitable for the particular purpose. Finishing one step does not automatically finish the other two.",
                            "If a Chinese translation is requested, ask whether the recipient specifies a translator, requires the source original or certified copy, expects a particular form of a name, and wants every seal and annotation translated. A short extract prepared before those questions are answered often has to be redone.",
                        ],
                    ),
                    (
                        "Run a two-way check before delivery",
                        [
                            "Read from source to translation to catch a missing page, seal or annotation. Then read from translation back to source to catch added words, guesses or changes in family role. Ask the family to review the name table, especially where one person used several romanisations or a former name.",
                            "A clear delivery set may contain the complete source, complete translation, name-and-date table and any additional evidence requested by the recipient. Number each document separately. Keeping different people's records apart makes a later supplementary request much easier to answer.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling Mainland estates"),
                    ("/articles/am/macau-death-record-for-mainland-inheritance_en.html", "Checking a Macau death record before Mainland use"),
                    ("/articles/am/macau-kinship-certificate-scope_en.html", "What a Macau kinship record can establish"),
                    ("/articles/am/macau-heir-qualification-deed_en.html", "When an heir-qualification deed is worth preparing"),
                ],
                "cta": "Place the first page, reverse, seal pages and identity records together, then state the Mainland purpose before deciding the translation scope.",
            },
        },
    },
    {
        "slug": "singapore-apostille-for-mainland-use",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_SG",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡與內地遺產",
                "title": "新加坡文件交到內地前，甚麼時候要辦 Apostille",
                "description": "新加坡家屬先按接收用途分清公共文件、私人文件和電子文件，再判斷是否需要 SAL Apostille。",
                "lead": "不是看到英文文件便先辦 Apostille。第一步是問內地接收方需要哪個版本、用來證明甚麼，以及是否接受紙本或電子形式。",
                "key_title": "先問三個問題",
                "keys": [
                    "內地接收方是否要求 Apostille",
                    "文件是公共文件還是私人文件",
                    "接收方接受紙本還是 e-Apostille",
                ],
                "answer_title": "先說最直接的答案",
                "answer": [
                    "是否需要 Apostille，先由文件用途和內地接收方的要求決定。SAL 是新加坡辦理這類文件證明的指定機構，但它不替接收方決定哪一份文件足夠。先拿文件名稱、版本和用途去問，得到明確答覆後才安排。",
                    "可核驗的新加坡公共文件通常可以按 SAL 路徑處理；私人聲明、授權書或私人製作的副本，如確實需要辦理，通常要先經新加坡公證人處理，再由 SAL 加上相應證明。兩類文件不要混成同一條流程。",
                ],
                "sections": [
                    (
                        "先問接收方，而不是先找辦理機構",
                        [
                            "向內地接收方提供文件正式名稱、簽發人、簽發日期、現有版本和準備證明的事項。直接問：這份文件是否要 Apostille、是否接受核證副本、是否另要中文譯本，以及電子形式能否使用。",
                            "不要只問『新加坡文件能不能用』。死亡證明、法院文件、私人授權書和家屬自行整理的聲明來源不同，接收方可能給出不同答案。把問題問得具體，才能避免多辦或漏辦。",
                        ],
                    ),
                    (
                        "先看是誰發出的文件",
                        [
                            "先問：這份文件由公共機構或法院簽發，還是由家屬或其他私人製作？出生、婚姻、死亡和部分法院文件通常屬前一類。電腦生成的版本有時要先由簽發部門確認，普通打印、截圖或自行掃描的副本不會自然符合要求。",
                            "私人授權書、私人聲明或自行製作的副本屬後一類。如接收方要求辦理，一般先由新加坡公證人處理並附上公證證明，再進入 SAL 的證明步驟。SAL 本身不是替家屬草擬或公證私人文件的地方。",
                        ],
                    ),
                    (
                        "紙本和電子形式要先問是否接受",
                        [
                            "e-Apostille 是電子形式的證明，並不等於把紙本證明掃描成 PDF。部分文件可以走電子流程，但接收方是否接受電子形式，仍要在申請前確認。需要紙本時，不要先辦電子版本再假設可以直接轉換。",
                            "收到電子文件後要保留完整連結、驗證資料和原始檔案，不要只截取畫面。紙本文件則保留證明頁、裝訂和文件編號。無論哪一種形式，接收方都應能核對簽發來源。",
                        ],
                    ),
                    (
                        "Apostille 沒有替家屬證明的事情",
                        [
                            "它主要核對簽名、簽署身份和印章來源，不判斷文件內每一句話是否真實，也不確認誰一定是內地繼承人。遺囑效力、家屬關係、代表權限和內地資產登記仍要分別處理。",
                            "如果姓名不同、文件缺頁、法院任命有限制或家屬有爭議，多辦一張 Apostille 不會補上這些問題。先把差異列出，再找能真正回答差異的文件。",
                        ],
                    ),
                    (
                        "用一頁清單安排順序",
                        [
                            "第一欄寫文件名稱和簽發來源，第二欄寫內地用途，第三欄記錄接收方是否要求 Apostille、翻譯和紙本，第四欄才填公證人或 SAL 的下一步。每份文件單獨一行。",
                            "同一個家庭可能同時有死亡證明、法院任命文件、遺囑副本和授權書。它們未必走同一條路。逐份確認後再付款、翻譯和寄送，通常比整疊一起辦更省時間。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/original-will-verification.html", "新加坡原始遺囑和掃描件分別能做甚麼"),
                    ("/articles/singapore/singapore-death-certificate.html", "新加坡死亡證明交到內地前先核對甚麼"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "有遺囑和無遺囑的法院文件有甚麼不同"),
                ],
                "cta": "說明文件名稱、簽發來源、內地用途和需要紙本或電子形式，才容易判斷是否走 SAL Apostille。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡与内地遗产",
                "title": "新加坡文件交到内地前，什么时候要办 Apostille",
                "description": "新加坡家属先按接收用途分清公共文件、私人文件和电子文件，再判断是否需要 SAL Apostille。",
                "lead": "不是看到英文文件就先办 Apostille。第一步是问内地接收方需要哪个版本、用来证明什么，以及是否接受纸质或电子形式。",
                "key_title": "先问三个问题",
                "keys": [
                    "内地接收方是否要求 Apostille",
                    "文件是公共文件还是私人文件",
                    "接收方接受纸质还是 e-Apostille",
                ],
                "answer_title": "先说最直接的答案",
                "answer": [
                    "是否需要 Apostille，先由文件用途和内地接收方的要求决定。SAL 是新加坡办理这类文件证明的指定机构，但它不能替接收方决定哪份文件足够。先拿文件名称、版本和用途去询问，得到明确答复后再安排。",
                    "可以核验的新加坡公共文件通常可以按 SAL 路径处理；私人声明、授权书或私人制作的副本，如果确实需要办理，通常要先由新加坡公证人处理，再由 SAL 加上相应证明。两类文件不要混成同一条流程。",
                ],
                "sections": [
                    (
                        "先问接收方，不要先找办理机构",
                        [
                            "向内地接收方提供文件正式名称、签发人、签发日期、现有版本和准备证明的事项。直接问这份文件是否要 Apostille、是否接受认证副本、是否另要中文译本，以及电子形式能否使用。",
                            "不要只问‘新加坡文件能不能用’。死亡证明、法院文件、私人授权书和家属自行整理的声明来源不同，接收方可能给出不同答案。问题越具体，越能避免多办或漏办。",
                        ],
                    ),
                    (
                        "先看文件是谁发出的",
                        [
                            "先问这份文件由公共机构或法院签发，还是由家属或其他私人制作。出生、婚姻、死亡和部分法院文件通常属于前一类。电脑生成的版本有时要先由签发部门确认，普通打印、截图或自行扫描的副本不会自然符合要求。",
                            "私人授权书、私人声明或自行制作的副本属于后一类。如果接收方要求办理，一般先由新加坡公证人处理并附上公证证明，再进入 SAL 的证明步骤。SAL 本身不是替家属起草或公证私人文件的地方。",
                        ],
                    ),
                    (
                        "纸质和电子形式要先问是否接受",
                        [
                            "e-Apostille 是电子形式的证明，并不是把纸质证明扫描成 PDF。部分文件可以通过电子流程办理，但接收方是否接受电子形式，仍然要在申请前确认。需要纸质文件时，不要先办电子版本再假设可以直接转换。",
                            "收到电子文件后，要保留完整链接、验证资料和原始文件，不要只截取画面。纸质文件则保留证明页、装订和文件编号。无论哪种形式，接收方都应当可以核对签发来源。",
                        ],
                    ),
                    (
                        "Apostille 没有替家属证明的事情",
                        [
                            "它主要核对签名、签署身份和印章来源，不判断文件中每句话是否真实，也不确认谁一定是内地继承人。遗嘱效力、家属关系、代表权限和内地资产登记仍要分别处理。",
                            "如果姓名不同、文件缺页、法院任命有限制或家属有争议，多办一张 Apostille 不会补上这些问题。先把差异列出来，再找能真正回答差异的文件。",
                        ],
                    ),
                    (
                        "用一页清单安排顺序",
                        [
                            "第一栏写文件名称和签发来源，第二栏写内地用途，第三栏记录接收方是否要求 Apostille、翻译和纸质文件，第四栏才填写公证人或 SAL 的下一步。每份文件单独一行。",
                            "同一个家庭可能同时有死亡证明、法院任命文件、遗嘱副本和授权书。它们不一定走同一条路。逐份确认后再付款、翻译和寄送，通常比整套一起办理更节省时间。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/original-will-verification_cn.html", "新加坡原始遗嘱和扫描件分别能做什么"),
                    ("/articles/singapore/singapore-death-certificate_cn.html", "新加坡死亡证明交到内地前先核对什么"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "有遗嘱和无遗嘱的法院文件有什么不同"),
                ],
                "cta": "说明文件名称、签发来源、内地用途和需要纸质或电子形式，才容易判断是否走 SAL Apostille。",
            },
            "en": {
                "lang": "en",
                "locale": "en_SG",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore and Mainland estates",
                "title": "When Does a Singapore Estate Document Need an Apostille for Mainland Use?",
                "description": "A practical guide to checking the recipient, document type and paper or electronic format before obtaining an SAL apostille for Mainland estate use.",
                "lead": "Do not order an apostille simply because a document is in English. First ask the Mainland recipient which version it needs, what fact the document must prove and whether it accepts paper or electronic form.",
                "key_title": "Ask three questions first",
                "keys": [
                    "Does the Mainland recipient require an apostille?",
                    "Is this a public document or a private document?",
                    "Will the recipient accept paper or an e-Apostille?",
                ],
                "answer_title": "The short answer",
                "answer": [
                    "The document's purpose and the Mainland recipient's requirements determine whether an apostille is needed. The Singapore Academy of Law, or SAL, is Singapore's designated authority for this work, but it does not decide which evidence a particular recipient should accept. Ask with the document name, version and intended use before applying.",
                    "A verifiable Singapore public document can generally follow the SAL public-document route. A private declaration, power of attorney or privately made copy usually needs a Singapore notary first if legalisation is required, followed by SAL authentication. The two categories should not be treated as one process.",
                ],
                "sections": [
                    (
                        "Ask the recipient before choosing a service",
                        [
                            "Give the Mainland recipient the formal document name, issuer, issue date, version held and the fact it is intended to prove. Ask whether it requires an apostille, accepts a certified copy, also needs a Chinese translation, and can receive an electronic form.",
                            "Do not ask only whether a 'Singapore document' can be used. A death certificate, court record, private power of attorney and family-prepared statement have different sources. A precise question is more likely to prevent unnecessary or missing steps.",
                        ],
                    ),
                    (
                        "Start with who issued the document",
                        [
                            "Ask whether the document was issued by a public authority or court, or made by the family or another private person. Birth, marriage and death records and some court documents usually fall into the first group. A computer-generated version may first need certification by its issuer; an ordinary printout, screenshot or family scan does not qualify merely because its words look the same.",
                            "A private power of attorney, declaration or privately made copy belongs to the second group. If legalisation is required, it generally goes first to a Singapore notary and receives a notarial certificate before the SAL step. SAL does not draft or notarise the family's private document.",
                        ],
                    ),
                    (
                        "Confirm whether paper or electronic form is accepted",
                        [
                            "An e-Apostille is an apostille issued electronically; it is not a scan of a paper certificate. Some documents can use an electronic route, but the recipient should confirm acceptance before the application. If paper is required, do not assume an electronic certificate can simply be converted later.",
                            "Keep the original file, full link and verification information for an electronic document rather than only a screenshot. For paper documents, preserve the certificate page, binding and document number. In either form, the recipient should be able to verify the issuing source.",
                        ],
                    ),
                    (
                        "What an apostille does not prove",
                        [
                            "It addresses the origin of the document, including the signature, signer's capacity and seal. It does not decide whether every statement is true, identify a Mainland heir, validate a will or transfer a Mainland asset. Those questions require their own evidence and procedures.",
                            "A name mismatch, missing page, restricted court appointment or family dispute is not cured by another apostille. Record the discrepancy first and find the evidence that actually answers it.",
                        ],
                    ),
                    (
                        "Use a one-page route sheet",
                        [
                            "Give each document one row. Record its name and issuer, Mainland purpose, whether the recipient requires an apostille, translation and paper form, and only then the next step with a notary or SAL.",
                            "One estate may include a death certificate, court appointment, will copy and power of attorney. They may not share the same route. Confirm each item before paying, translating or delivering the set.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling Mainland estates"),
                    ("/articles/singapore/original-will-verification_en.html", "The original Singapore will and a family scan"),
                    ("/articles/singapore/singapore-death-certificate_en.html", "Checking a Singapore death certificate before Mainland use"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate and letters of administration in Singapore"),
                ],
                "cta": "State the document name, issuer, Mainland purpose and paper or electronic requirement before deciding whether to use the SAL apostille route.",
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
    "articles/macau/index.html": {
        "href": "/articles/am/portuguese-documents-translation.html",
        "card": '<a href="/articles/am/portuguese-documents-translation.html"><span class="v24-tag">葡文翻譯</span><strong>澳門葡文文件交到內地前，翻譯最容易漏掉甚麼</strong><p>姓名、日期、附註、印章和背頁都要逐項核對。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/macau/index_cn.html": {
        "href": "/articles/am/portuguese-documents-translation_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">葡文翻译</span><h3>澳门葡文文件交到内地前，翻译最容易漏掉什么</h3><p>姓名、日期、附注、印章和背页都要逐项核对。</p></div><a class="v25-pill-action" href="/articles/am/portuguese-documents-translation_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/macau/index_en.html": {
        "href": "/articles/am/portuguese-documents-translation_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Portuguese records</span><h3>Using a Macau Portuguese estate document: what must be translated?</h3><p>Check names, dates, annotations, seals and reverse pages before delivery.</p></div><a class="v25-pill-action" href="/articles/am/portuguese-documents-translation_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index.html": {
        "href": "/articles/singapore/singapore-apostille-for-mainland-use.html",
        "card": '<a href="/articles/singapore/singapore-apostille-for-mainland-use.html"><span class="v24-tag">文件證明</span><strong>新加坡文件交到內地前，甚麼時候要辦 Apostille</strong><p>先問接收方，再分清公共、私人和電子文件。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/singapore/index_cn.html": {
        "href": "/articles/singapore/singapore-apostille-for-mainland-use_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">文件证明</span><h3>新加坡文件交到内地前，什么时候要办 Apostille</h3><p>先问接收方，再分清公共、私人和电子文件。</p></div><a class="v25-pill-action" href="/articles/singapore/singapore-apostille-for-mainland-use_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index_en.html": {
        "href": "/articles/singapore/singapore-apostille-for-mainland-use_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">SAL apostille</span><h3>When does a Singapore estate document need an apostille?</h3><p>Ask the recipient, then identify the document type and format.</p></div><a class="v25-pill-action" href="/articles/singapore/singapore-apostille-for-mainland-use_en.html">Read Article</a></article>',
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
    for hub in ("macau", "singapore"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, f"{SITE}/articles/{hub}/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
