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
        "slug": "us-document-translation-and-name",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國文件",
                "title": "美國英文文件翻成中文，姓名、日期和州縣資料怎樣核對",
                "description": "美國死亡、婚姻或法院文件翻成中文前，先核對姓名變化、日期格式、州縣層級、文件編號和完整頁面，避免譯本與內地資料對不上。",
                "lead": "先別急着把文件交給翻譯。做一張資料對照表，先把姓名、日期和地名對上；翻譯可以說明文字意思，卻不能替家屬證明兩個不同名字一定是同一個人。",
                "key_title": "先核對三組資料",
                "keys": [
                    "姓名原文、舊名和中文姓名從哪份文件取得",
                    "日期是月／日／年，還是日／月／年",
                    "城市、縣和州要分開記錄，不要互相替代",
                ],
                "answer_title": "先說最實用的做法",
                "answer": [
                    "不要拿到英文文件便直接逐句翻。先把每名相關人士的英文姓名、中文姓名、舊名、出生日期和證件號碼放在同一張表，再抄下文件的簽發州、縣、市、編號和頁數。譯本中的每一個名字和數字，都應能回到原文找到來源。",
                    "如果英文文件和內地資料使用不同姓名，譯者不應自行猜一個中文寫法。婚後改姓、法院改名、拼音次序不同或中間名縮寫，都要由婚姻文件、改名文件、舊證件或其他連接材料說明。翻譯只處理文字，身份連接是另一個證據問題。",
                ],
                "sections": [
                    (
                        "先認清這份文件由哪裏簽發",
                        [
                            "美國出生、死亡和婚姻記錄通常由事情發生地的州或地方記錄機關保存，不是全部由一個聯邦部門發出。先抄下簽發機關全名、州名、縣名、文件正式名稱和記錄編號，才知道原文中的地名和職務應怎樣處理。",
                            "法院文件再加法院全名、案件編號、簽署人職務和日期。若手上只是掃描件，先確認有沒有背頁、附頁、核證頁或更正頁，不要把不完整的版本交給譯者。",
                        ],
                    ),
                    (
                        "姓名不要憑讀音猜",
                        [
                            "英文姓名可能有婚前姓氏、婚後姓氏、中間名、縮寫和不同拼音次序。先照原文逐字記錄，再列出每一種寫法出現在哪份文件。中文姓名則以可核對的舊證件、內地登記或其他既有記錄為起點。",
                            "如果新舊姓名之間有婚姻證明、離婚文件、改名命令或長期使用記錄，把它們列成一條時間線。不要在譯本中直接把兩個不同姓名合併成同一個中文姓名，也不要用括號暗示同一人而沒有材料支持。",
                        ],
                    ),
                    (
                        "日期和州縣資料要逐項拆開",
                        [
                            "美國文件常見月／日／年格式。遇到 03/07/2024 這類日期，不要憑習慣判斷是 3 月 7 日還是 7 月 3 日；應結合月份英文、簽發時間和其他記錄核對。譯本可用完整中文年月日，減少歧義。",
                            "City、County 和 State 是不同層級。例如 Los Angeles County 是縣，California 才是州。法院所在地也不一定等於事情發生地。郵政縮寫、案件編號、登記編號和證件號碼要保留原有結構，不應為了看起來整齊而改寫。",
                        ],
                    ),
                    (
                        "不要只翻正文大段文字",
                        [
                            "頁眉、頁腳、邊註、背頁、印章、騎縫、簽署人職務、核證語句和手寫更正，都可能說明文件版本和簽發權限。看不清的地方應標明，而不是猜一個最可能的答案。",
                            "譯完後做兩次反向核對：先從原文逐欄查譯本有沒有漏項，再從譯本回到原文查每個姓名、日期、地名和號碼有沒有來源。空白、不適用和無法辨認的內容，也要用一致方式處理。",
                        ],
                    ),
                    (
                        "交件前先問內地接收方四個問題",
                        [
                            "問清楚需要完整文件還是指定頁面、是否要求譯者資格或譯本證明、姓名差異要用甚麼材料連接，以及原文和譯本是否要一併提交。不同城市、法院、登記或金融機構的實際接收要求可能不同。",
                            "最省時間的交件包包括：完整原文、完整譯本、姓名日期對照表、身份連接材料清單，以及一頁用途說明。先把缺口列出來，再決定要不要補領文件、辦理證明或重新翻譯。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/issuing-state-matters.html", "美國文件先看由哪一級機關簽發"),
                    ("/articles/us/state-or-federal-apostille.html", "州文件和聯邦文件怎樣分路徑"),
                    ("/articles/us/us-documents-mainland-property-inheritance.html", "美國死亡證明和遺囑用於內地房產前先核對甚麼"),
                ],
                "cta": "把英文文件首頁、簽署核證頁、姓名差異和內地用途放在一起，先做對照，再安排翻譯。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国文件",
                "title": "美国英文文件翻成中文，姓名、日期和州县信息怎样核对",
                "description": "美国死亡、婚姻或法院文件翻成中文前，先核对姓名变化、日期格式、州县层级、文件编号和完整页面，避免译本与内地资料对不上。",
                "lead": "先别急着把文件交给翻译。做一张资料对照表，先把姓名、日期和地名对上；翻译可以说明文字意思，却不能替家属证明两个不同名字一定是同一个人。",
                "key_title": "先核对三组资料",
                "keys": [
                    "姓名原文、旧名和中文姓名来自哪份文件",
                    "日期是月／日／年，还是日／月／年",
                    "城市、县和州要分开记录，不能互相替代",
                ],
                "answer_title": "先说最实用的做法",
                "answer": [
                    "不要拿到英文文件就直接逐句翻。先把每位相关人员的英文姓名、中文姓名、旧名、出生日期和证件号码放在同一张表，再抄下文件的签发州、县、市、编号和页数。译本中的每一个名字和数字，都应当能回到原文找到来源。",
                    "如果英文文件和内地资料使用不同姓名，译者不应自行猜一个中文写法。婚后改姓、法院改名、拼音顺序不同或中间名缩写，都要由婚姻文件、改名文件、旧证件或其他连接材料说明。翻译只处理文字，身份连接是另一个证据问题。",
                ],
                "sections": [
                    (
                        "先认清这份文件由哪里签发",
                        [
                            "美国出生、死亡和婚姻记录通常由事情发生地的州或地方记录机构保存，并不是全部由一个联邦部门发出。先抄下签发机构全名、州名、县名、文件正式名称和记录编号，才知道原文中的地名和职务应怎样处理。",
                            "法院文件还要记录法院全名、案件编号、签署人职务和日期。手上如果只有扫描件，先确认有没有背页、附页、核证页或更正页，不要把不完整的版本直接交给译者。",
                        ],
                    ),
                    (
                        "姓名不要凭读音猜",
                        [
                            "英文姓名可能有婚前姓氏、婚后姓氏、中间名、缩写和不同拼音顺序。先按原文逐字记录，再列出每一种写法出现在哪份文件。中文姓名则以可以核对的旧证件、内地登记或其他既有记录为起点。",
                            "如果新旧姓名之间有婚姻证明、离婚文件、改名命令或长期使用记录，把它们排成一条时间线。不要在译本中直接把两个不同姓名合并成同一个中文姓名，也不要用括号暗示同一人却没有材料支持。",
                        ],
                    ),
                    (
                        "日期和州县信息要逐项拆开",
                        [
                            "美国文件常见月／日／年格式。遇到 03/07/2024 这类日期，不能凭习惯判断是 3 月 7 日还是 7 月 3 日；要结合月份英文、签发时间和其他记录核对。译本可以使用完整中文年月日，减少歧义。",
                            "City、County 和 State 是不同层级。例如 Los Angeles County 是县，California 才是州。法院所在地也不一定等于事情发生地。邮政缩写、案件编号、登记编号和证件号码要保留原有结构，不要为了看起来整齐而改写。",
                        ],
                    ),
                    (
                        "不要只翻正文大段文字",
                        [
                            "页眉、页脚、边注、背页、印章、骑缝、签署人职务、核证语句和手写更正，都可能说明文件版本和签发权限。看不清的地方应当标明，不能猜一个最可能的答案。",
                            "译完后做两次反向核对：先从原文逐栏查译本有没有漏项，再从译本回到原文查每个姓名、日期、地名和号码有没有来源。空白、不适用和无法辨认的内容，也要用一致方式处理。",
                        ],
                    ),
                    (
                        "交件前先问内地接收方四个问题",
                        [
                            "问清楚需要完整文件还是指定页面、是否要求译者资格或译本证明、姓名差异要用什么材料连接，以及原文和译本是否要一起提交。不同城市、法院、登记或金融机构的实际接收要求可能不同。",
                            "最省时间的交件包包括：完整原文、完整译本、姓名日期对照表、身份连接材料清单，以及一页用途说明。先把缺口列出来，再决定是否补领文件、办理证明或重新翻译。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/issuing-state-matters_cn.html", "美国文件先看由哪一级机构签发"),
                    ("/articles/us/state-or-federal-apostille_cn.html", "州文件和联邦文件怎样分路径"),
                    ("/articles/us/us-documents-mainland-property-inheritance_cn.html", "美国死亡证明和遗嘱用于内地房产前先核对什么"),
                ],
                "cta": "把英文文件首页、签署核证页、姓名差异和内地用途放在一起，先做对照，再安排翻译。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. documents",
                "title": "Translating U.S. Documents into Chinese: Check Names, Dates and Places",
                "description": "A practical quality check for names, dates, states, counties, record numbers and complete pages before translating U.S. documents for Mainland use.",
                "lead": "Do not send the file straight to a translator. First make a fact sheet matching the names, dates and places. Translation can explain the text, but cannot create proof that two different names belong to the same person.",
                "key_title": "Check three groups of facts",
                "keys": [
                    "Where each English name, former name and Chinese name is recorded",
                    "Whether a numeric date uses month-day-year or another order",
                    "The city, county and state as separate places",
                ],
                "answer_title": "A practical starting point",
                "answer": [
                    "Do not begin with a line-by-line translation. First create one table showing every relevant person's English name, Chinese name, former name, date of birth and document number. Add the issuing state, county, city, record number and total pages for each source document. Every name and number in the translation should be traceable to the original.",
                    "When a U.S. record and a Mainland record use different names, the translator should not guess a Chinese equivalent. A married surname, court-ordered name change, different romanisation or middle initial may need marriage records, a name-change record, an earlier identity document or other connecting evidence. Translation and identity proof are separate tasks.",
                ],
                "sections": [
                    (
                        "Identify the issuing authority first",
                        [
                            "U.S. birth, death and marriage records are generally held by the state or local office for the place where the event occurred. They do not all come from one federal registry. Record the full issuing authority, state, county, formal document title and record number before translating place names or official titles.",
                            "For a court paper, add the full court name, case number, signer's title and date. If the family has only a scan, check for reverse pages, attachments, certification pages and later corrections before sending an incomplete version to the translator.",
                        ],
                    ),
                    (
                        "Do not guess a name from its sound",
                        [
                            "A record may show a birth surname, married surname, middle name, abbreviation or a different order of romanised names. Copy each version exactly and note the document where it appears. Begin the Chinese-name column with an earlier identity document, Mainland registration record or another source that can actually be checked.",
                            "If marriage, divorce, a court order or a history of public records links the old and current names, arrange those materials as a timeline. Do not silently merge two names in the translation or add an unsupported 'also known as' description.",
                        ],
                    ),
                    (
                        "Separate dates, cities, counties and states",
                        [
                            "Many U.S. records use month-day-year. A date such as 03/07/2024 is ambiguous outside its context, so check a written month, the issue date and related records before deciding what it means. Writing the month in words in the Chinese translation can remove that ambiguity.",
                            "A city, county and state are different levels. Los Angeles County, for example, is a county; California is the state. The court location may also differ from the place where the underlying event occurred. Keep postal abbreviations, case numbers, record numbers and identity numbers in their source structure.",
                        ],
                    ),
                    (
                        "Translate more than the main paragraphs",
                        [
                            "Headers, footers, marginal notes, reverse pages, seals, attached certificates, the signer's title and handwritten corrections may all affect the document's status. Mark illegible text rather than supplying the most likely wording.",
                            "Run the check in both directions. Compare the original with the translation for omissions, then compare every translated name, date, place and number back to its source. Use a consistent treatment for blanks, items marked not applicable and text that cannot be read.",
                        ],
                    ),
                    (
                        "Ask the Mainland recipient four questions before filing",
                        [
                            "Confirm whether the full document or selected pages are required, whether the translator or translation needs a particular certification, what evidence should connect different names, and whether the original and translation must be submitted together. The practical requirements can differ by city and receiving authority.",
                            "A useful filing pack contains the complete source, complete translation, name-and-date table, list of identity-linking records and a one-page purpose note. Identify the gap first, then decide whether to order a new record, obtain an authentication or revise the translation.",
                        ],
                    ),
                ],
                "related_title": "Continue with the United States topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling Mainland estates"),
                    ("/articles/us/issuing-state-matters_en.html", "Start with the authority that issued the U.S. document"),
                    ("/articles/us/state-or-federal-apostille_en.html", "Choosing the state or federal apostille route"),
                    ("/articles/us/us-documents-mainland-property-inheritance_en.html", "Using U.S. death and will documents for a Mainland property"),
                ],
                "cta": "Place the first page, certification page, name differences and Mainland purpose side by side before arranging the translation.",
            },
        },
    },
    {
        "slug": "sole-registered-mainland-property",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國家屬與內地房產",
                "title": "內地房產只登記已故親人姓名，美國家屬先查哪六件事",
                "description": "內地房產證只寫已故親人姓名時，美國家屬先核對登記、購房時間、婚姻與出資、限制、繼承人和美國文件用途。",
                "lead": "房產證上的姓名是重要起點，但不等於整套房屋一定全部屬於遺產。先分清原有權益，再談由誰繼承。",
                "key_title": "先別急着算份額",
                "keys": [
                    "先查房屋目前登記和權利限制",
                    "再看購房時間、婚姻情況和出資資料",
                    "最後才把繼承人和美國文件接上內地程序",
                ],
                "answer_title": "先說最直接的答案",
                "answer": [
                    "房產只登記在已故親人一人名下，不能省略前面的權益核對。先查房屋地址、登記人、登記份額和有沒有抵押、查封或其他共有人；再看房屋何時取得、當時是否已婚、購房款和書面約定從哪裏來。只有先分清哪些權益原本屬於誰，才能判斷哪些部分進入遺產。",
                    "不要套用『配偶固定先拿一半』或『房產證只寫一人便全是個人財產』這類口訣。婚前取得、婚後取得、贈與或繼承所得、夫妻書面約定、共同還款和其他實際情況，都可能令答案不同。",
                ],
                "sections": [
                    (
                        "一、查清楚房產證到底寫了甚麼",
                        [
                            "先找不動產權證、舊房產證、購房合同或準確地址。記錄房屋所在城市、完整地址、權利人姓名、證件號碼、登記份額、登記日期和權利性質。若只有舊照片或家人口述，先向房屋所在地查詢可行的登記資料和辦理要求。",
                            "同時看有沒有抵押、查封、居住權、共同權利人或歷史變更。即使最後要辦繼承，也要先看房屋目前登記成甚麼狀態。",
                        ],
                    ),
                    (
                        "二、把取得房屋的時間和來源排成時間線",
                        [
                            "記下簽合同、付款、收樓和登記的大致時間，再找首付款、貸款、轉帳、售房款、贈與或家庭協議的線索。房產證登記日期不一定等於實際取得和出資的全部經過。",
                            "如果資料不齊，先列出仍可找到的人和機構，例如銀行、開發商、物業、共同還款人或保管舊文件的親屬。不要在沒有付款與取得資料時，先用家人口述下結論。",
                        ],
                    ),
                    (
                        "三、核對當時的婚姻情況和書面約定",
                        [
                            "先確認購房或取得房屋時是否已婚，有沒有婚前或婚內書面財產約定，房屋是否來自指定給一人的贈與或遺產。這些材料會影響房屋原本屬於個人、夫妻共同或其他共有的判斷。",
                            "如果配偶健在，應先處理配偶本來可能享有的權益，再處理已故親人的遺產。這不是預先套一個固定比例，而是按取得時間、資金來源、約定和證據逐項判斷。",
                        ],
                    ),
                    (
                        "四、把房屋債務和實際使用情況一併列出",
                        [
                            "確認貸款是否結清、由誰還款、物業費和稅費是否拖欠、現在由誰居住或出租，以及有沒有其他人持有鑰匙和原件。這些情況未必決定繼承份額，但會直接影響後續交接和辦理難度。",
                            "有人占用、拒交文件或對房屋來源有爭議時，不要把所有問題都當成普通過戶材料不足。先保存合同、付款、聊天、租賃和物業記錄，再區分是資料補充、家人協商還是需要處理爭議。",
                        ],
                    ),
                    (
                        "五、畫出完整繼承人關係，不只列在美國的人",
                        [
                            "先列出配偶、父母、子女，以及已先去世的家屬和其後代；若這一層家屬不存在，再把可能涉及的其他親屬補上。另記錄有沒有遺囑、放棄安排、失聯或爭議。內地房產登記通常會關心死亡、親屬關係、全部相關人和已故權利人的權利資料。",
                            "家屬長住美國，不代表只看美國遺產程序列出的人。若內地房屋沒有出現在美國遺產文件中，應把內地資產另行列明，向房屋所在地確認需要哪一組文件。",
                        ],
                    ),
                    (
                        "六、分清美國文件能回答甚麼",
                        [
                            "美國死亡記錄可說明死亡事實；遺囑可記錄安排；法院任命文件可說明某人在特定遺產程序中的身份和當地法院授予的權限。它們各有作用，但不會自行改變內地房產登記，也不會替代房屋來源、配偶原有權益和全部繼承人的核對。",
                            "第一次諮詢可準備一頁資料：房屋城市和地址、房產證姓名、取得年份、當時婚姻狀況、現有貸款或占用、家屬關係，以及手上每份美國文件的簽發州。先把六項事實填完整，才容易看出真正缺口。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/mainland-asset-omitted-from-probate.html", "美國遺產程序漏了內地資產怎樣處理"),
                    ("/articles/us/letters-testamentary-or-administration.html", "常見美國法院任命文件分別說明甚麼"),
                    ("/articles/us/remote-china-lawyer.html", "人在美國怎樣整理內地法律事務"),
                ],
                "cta": "先把房產證、取得時間、婚姻與出資、貸款限制和完整家屬關係放在同一頁，再判斷下一步。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国家属与内地房产",
                "title": "内地房产只登记已故亲人姓名，美国家属先查哪六件事",
                "description": "内地房产证只写已故亲人姓名时，美国家属先核对登记、购房时间、婚姻与出资、限制、继承人和美国文件用途。",
                "lead": "房产证上的姓名是重要起点，但不等于整套房屋一定全部属于遗产。先分清原有权益，再谈由谁继承。",
                "key_title": "先别急着算份额",
                "keys": [
                    "先查房屋当前登记和权利限制",
                    "再看购房时间、婚姻情况和出资资料",
                    "最后才把继承人和美国文件接上内地程序",
                ],
                "answer_title": "先说最直接的答案",
                "answer": [
                    "房产只登记在已故亲人一人名下，不能省略前面的权益核对。先查房屋地址、登记人、登记份额和有没有抵押、查封或其他共有人；再看房屋何时取得、当时是否已婚、购房款和书面约定来自哪里。只有先分清哪些权益原本属于谁，才能判断哪些部分进入遗产。",
                    "不要套用『配偶固定先拿一半』或『房产证只写一人就全是个人财产』这类口诀。婚前取得、婚后取得、赠与或继承所得、夫妻书面约定、共同还款和其他实际情况，都可能让答案不同。",
                ],
                "sections": [
                    (
                        "一、查清房产证到底写了什么",
                        [
                            "先找不动产权证、旧房产证、购房合同或准确地址。记录房屋所在城市、完整地址、权利人姓名、证件号码、登记份额、登记日期和权利性质。如果只有旧照片或家人口述，先向房屋所在地了解可以查询的登记资料和办理要求。",
                            "同时看有没有抵押、查封、居住权、共同权利人或历史变更。即使最后要办继承，也要先看房屋目前登记成什么状态。",
                        ],
                    ),
                    (
                        "二、把取得房屋的时间和来源排成时间线",
                        [
                            "记下签合同、付款、收房和登记的大致时间，再找首付款、贷款、转账、售房款、赠与或家庭协议的线索。房产证登记日期不一定等于实际取得和出资的全部经过。",
                            "资料不齐时，先列出仍能找到的人和机构，例如银行、开发商、物业、共同还款人或保管旧文件的亲属。不要在没有付款与取得资料时，先按家人口述下结论。",
                        ],
                    ),
                    (
                        "三、核对当时的婚姻情况和书面约定",
                        [
                            "先确认购房或取得房屋时是否已婚，有没有婚前或婚内书面财产约定，房屋是否来自指定给一人的赠与或遗产。这些材料会影响房屋原本属于个人、夫妻共同或其他共有的判断。",
                            "配偶健在时，应当先处理配偶原本可能享有的权益，再处理已故亲人的遗产。这不是预先套用一个固定比例，而是根据取得时间、资金来源、约定和证据逐项判断。",
                        ],
                    ),
                    (
                        "四、把房屋债务和实际使用情况一起列出",
                        [
                            "确认贷款是否结清、由谁还款、物业费和税费是否拖欠、现在由谁居住或出租，以及有没有其他人持有钥匙和原件。这些情况未必决定继承份额，但会直接影响后续交接和办理难度。",
                            "有人占用、拒交文件或对房屋来源有争议时，不要把所有问题都当成普通过户材料不足。先保存合同、付款、聊天、租赁和物业记录，再区分是补资料、家人协商还是需要处理争议。",
                        ],
                    ),
                    (
                        "五、画出完整继承人关系，不只列在美国的人",
                        [
                            "先列出配偶、父母、子女，以及先去世的家属和其后代；如果这一层家属不存在，再把可能涉及的其他亲属补上。另记录有没有遗嘱、放弃安排、失联或争议。内地房产登记通常会关注死亡、亲属关系、全部相关人员和已故权利人的权利资料。",
                            "家属长期住在美国，不代表只看美国遗产程序列出的人。如果内地房屋没有出现在美国遗产文件中，应把内地资产另行列明，向房屋所在地确认需要哪一组文件。",
                        ],
                    ),
                    (
                        "六、分清美国文件能回答什么",
                        [
                            "美国死亡记录可以说明死亡事实；遗嘱可以记录安排；法院任命文件可以说明某人在特定遗产程序中的身份和当地法院授予的权限。它们各有作用，但不会自行改变内地房产登记，也不能替代房屋来源、配偶原有权益和全部继承人的核对。",
                            "第一次咨询可准备一页资料：房屋城市和地址、房产证姓名、取得年份、当时婚姻状况、现有贷款或占用、家属关系，以及手上每份美国文件的签发州。先把六项事实填完整，才容易看出真正缺口。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/mainland-asset-omitted-from-probate_cn.html", "美国遗产程序漏了内地资产怎样处理"),
                    ("/articles/us/letters-testamentary-or-administration_cn.html", "常见美国法院任命文件分别说明什么"),
                    ("/articles/us/remote-china-lawyer_cn.html", "人在美国怎样整理内地法律事务"),
                ],
                "cta": "先把房产证、取得时间、婚姻与出资、贷款限制和完整家属关系放在同一页，再判断下一步。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. families and Mainland property",
                "title": "Mainland Home in the Deceased's Name: Six Checks for U.S. Families",
                "description": "Six checks for U.S.-based family members when a Mainland title records only the deceased: title, acquisition, marriage, restrictions, heirs and U.S. documents.",
                "lead": "The registered name is an important starting point, but it does not always mean that the entire property falls into the estate. Identify the existing ownership interests before discussing inheritance.",
                "key_title": "Do not calculate shares yet",
                "keys": [
                    "Check the current title and any restrictions",
                    "Trace acquisition, marriage and funding",
                    "Then connect the heirs and U.S. records to the Mainland process",
                ],
                "answer_title": "The short answer",
                "answer": [
                    "A home registered only in the deceased's name still requires an ownership review. Confirm the address, registered owner, recorded share, mortgage, court restriction and any co-owner. Then establish when and how the home was acquired, whether the deceased was married at the time, how it was paid for and whether there was a written property agreement. Only the interest that belonged to the deceased can enter the estate.",
                    "Avoid shortcuts such as 'the spouse always takes half first' or 'one name on the title means separate property.' Property acquired before or during marriage, a gift or inheritance to one person, a written marital agreement, joint repayments and the available evidence can produce different results.",
                ],
                "sections": [
                    (
                        "1. Read the title record carefully",
                        [
                            "Find the current title certificate, an earlier property certificate, the purchase contract or at least an exact address. Record the city, full address, registered name, identity number, registered share, registration date and type of right. If the family has only a photograph or a memory, ask what title information can be checked in the city where the home is located.",
                            "Check for a mortgage, court restriction, right of residence, co-owner or earlier transfer. Even if the family eventually files an inheritance transfer, it still needs to understand the property's current title position first.",
                        ],
                    ),
                    (
                        "2. Build an acquisition and payment timeline",
                        [
                            "Record when the contract was signed, payments were made, possession was delivered and title was registered. Look for the down payment, loan records, bank transfers, proceeds from an earlier sale, a gift or a family agreement. The registration date alone may not show the full acquisition and funding history.",
                            "When documents are missing, list the people and organisations that may still hold evidence, such as the bank, developer, property manager, another person who repaid the loan or a relative who kept older papers. Do not turn a family recollection into a legal conclusion before checking the available records.",
                        ],
                    ),
                    (
                        "3. Check the marriage and any written agreement",
                        [
                            "Confirm whether the deceased was married when the home was acquired, whether there was a written pre-marital or marital property agreement, and whether the property came from a gift or inheritance directed to one person. Those facts can affect whether the pre-existing interest was separate, marital or otherwise co-owned.",
                            "If a spouse survives, any interest already belonging to that spouse should be addressed before the deceased's estate is distributed. This is not a fixed percentage chosen in advance. It depends on timing, source of funds, agreements and evidence.",
                        ],
                    ),
                    (
                        "4. Record debts, possession and practical control",
                        [
                            "Check whether the loan is paid, who made the repayments, whether property charges remain due, who occupies or rents out the home, and who holds the keys and originals. Those facts may not decide the inheritance shares, but they directly affect handover and the difficulty of the next steps.",
                            "If someone refuses to release documents, occupies the property or disputes how it was acquired, do not treat everything as a routine missing-document problem. Preserve the contract, payment, messages, lease and property-management records, then separate evidence work, family negotiation and any dispute route.",
                        ],
                    ),
                    (
                        "5. Map every relevant family member",
                        [
                            "Start with the spouse, parents and children, together with any family member who died earlier and their descendants. If none of those relatives exists, add the other relatives who may need to be considered. Note any will, proposed disclaimer, missing person or disagreement. A Mainland property process commonly needs the death, family relationship, relevant people and the deceased's title information to fit together.",
                            "Living in the United States does not make the list in a U.S. probate file the only family list that matters. If the Mainland home was omitted from the U.S. estate papers, identify it separately and ask the property's local receiving office which records are required.",
                        ],
                    ),
                    (
                        "6. Give each U.S. document its proper job",
                        [
                            "A U.S. death record addresses the fact of death. A will records testamentary intentions. A court appointment identifies a person's role and the authority granted in that particular local estate proceeding. Each can be useful, but none automatically changes a Mainland title or replaces evidence about acquisition, a spouse's existing interest and all relevant heirs.",
                            "For a first review, prepare one page with the property city and address, name on the title, acquisition year, marital status at that time, current loan or occupation, family map and issuing state for each U.S. document. Completing those six groups of facts usually reveals the real gap.",
                        ],
                    ),
                ],
                "related_title": "Continue with the United States topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling Mainland estates"),
                    ("/articles/us/mainland-asset-omitted-from-probate_en.html", "When a Mainland asset was omitted from U.S. probate"),
                    ("/articles/us/letters-testamentary-or-administration_en.html", "What common U.S. court appointment papers establish"),
                    ("/articles/us/remote-china-lawyer_en.html", "Organising Mainland legal work from the United States"),
                ],
                "cta": "Put the title, acquisition timeline, marriage and funding facts, restrictions and complete family map on one page before choosing the next step.",
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
    "articles/united-states/index.html": [
        (
            "/articles/us/us-document-translation-and-name.html",
            '<a href="/articles/us/us-document-translation-and-name.html"><span class="v24-tag">文件翻譯</span><strong>美國英文文件翻成中文，姓名、日期和州縣資料怎樣核對</strong><p>先做姓名日期對照，再翻完整頁面；翻譯不能代替身份連接證據。</p></a>',
        ),
        (
            "/articles/us/sole-registered-mainland-property.html",
            '<a href="/articles/us/sole-registered-mainland-property.html"><span class="v24-tag">房產登記</span><strong>內地房產只登記已故親人姓名，美國家屬先查哪六件事</strong><p>先分清原有權益、婚姻出資和登記限制，再談哪些部分進入遺產。</p></a>',
        ),
    ],
    "articles/united-states/index_cn.html": [
        (
            "/articles/us/us-document-translation-and-name_cn.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">文件翻译</span><h3>美国英文文件翻成中文，姓名、日期和州县信息怎样核对</h3><p>先做姓名日期对照，再翻完整页面；翻译不能代替身份连接证据。</p></div><a class="v25-pill-action" href="/articles/us/us-document-translation-and-name_cn.html">阅读文章</a></article>',
        ),
        (
            "/articles/us/sole-registered-mainland-property_cn.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">房产登记</span><h3>内地房产只登记已故亲人姓名，美国家属先查哪六件事</h3><p>先分清原有权益、婚姻出资和登记限制，再谈哪些部分进入遗产。</p></div><a class="v25-pill-action" href="/articles/us/sole-registered-mainland-property_cn.html">阅读文章</a></article>',
        ),
    ],
    "articles/united-states/index_en.html": [
        (
            "/articles/us/us-document-translation-and-name_en.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Translation check</span><h3>Checking names, dates and places in U.S. document translations</h3><p>Build a fact sheet first; translation does not replace identity evidence.</p></div><a class="v25-pill-action" href="/articles/us/us-document-translation-and-name_en.html">Read Article</a></article>',
        ),
        (
            "/articles/us/sole-registered-mainland-property_en.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Property title</span><h3>Mainland home in the deceased\'s name: six checks</h3><p>Identify existing ownership, marriage and funding before distributing the estate.</p></div><a class="v25-pill-action" href="/articles/us/sole-registered-mainland-property_en.html">Read Article</a></article>',
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
    for suffix in ("", "index_cn.html", "index_en.html"):
        text = update_lastmod(text, f"{SITE}/articles/united-states/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
