from __future__ import annotations

from publish_regional_inheritance_foundations import (
    LANG_SUFFIX,
    ROOT,
    SITE,
    TODAY,
    render_article,
)


ARTICLES = [
    {
        "slug": "family-coordinator-first-sheet",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_MO",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門與內地遺產",
                "title": "繼承人很多，澳門家庭先選聯絡人時要分清哪三件事",
                "description": "澳門家庭處理內地遺產時，怎樣選一名聯絡人整理家屬、文件和資產線索，又不讓他越過其他家屬作決定。",
                "lead": "找一個人集中資料很有用，但「負責聯絡」不等於可以替所有人決定誰繼承、怎樣分或簽甚麼文件。先把整理、決定和正式代表三件事分開。",
                "key_title": "先把三種角色分開",
                "keys": [
                    "聯絡人：收集資料、記錄來源、安排核對",
                    "家屬溝通：確認不同說法和未解問題",
                    "正式代表：按有效文件和具體程序行事",
                    "任何一人都不能把家人記憶寫成已確認事實",
                ],
                "visuals": [
                    ("聯絡人可以做甚麼", "收集影像和線索", "更新家屬問題表", "整理不是代替大家作決定。"),
                    ("三層工作不要混在一起", "整理事實", "家屬確認", "正式簽署", "每一層都由適合的人完成。"),
                    ("每條資料標記狀態", "已見原件", "只有影像", "家人憶述", "仍有爭議", "不確定的內容保留問號。"),
                ],
                "answer_title": "先說最實用的答案",
                "answer": [
                    "聯絡人最好是願意做記錄、能保持中立、方便聯絡各地家屬的人，不一定是最年長的人，也不一定是保管房產證或銀行信件的人。他可以建立家屬名單、文件目錄和資產線索表，但不應自行判斷誰沒有繼承權、替別人放棄權利，或把未取得的授權寫成已有授權。",
                    "澳門的正式繼承文件可能由特定人士申請或簽署，內地房產登記也會另外核對死亡、親屬關係、房屋權屬和其他繼承人。家庭工作表的作用，是讓兩邊看到同一套事實；它不會因為寫得完整，就自動成為公證書、授權書或遺產管理文件。",
                ],
                "sections": [
                    (
                        "第一步：按做事能力選人，不要按家庭排行選人",
                        [
                            "合適的聯絡人通常能固定回覆、保存版本、把不同家屬的說法分開記錄，也願意承認自己不知道。若長子女身在海外、配偶不熟悉內地房產，或目前已有爭議，可以由另一名較中立的家屬負責整理，必要時再設一名共同覆核人。",
                            "一開始就在群組寫明範圍：聯絡人只收集資料、列問題和轉達回覆；出售、分配、放棄、簽署或委託，仍要由有權的人按實際文件處理。這句話能避免日後把方便聯絡誤解成已獲全家授權。",
                        ],
                    ),
                    (
                        "第二步：只做三張表，不要先建一個巨大檔案庫",
                        [
                            "第一張是家屬表：姓名、與逝者關係、所在城市、聯絡狀況、是否看過遺囑。第二張是文件表：文件名稱、原件保管人、簽發地、日期和目前只有原件還是影像。第三張是資產表：每項內地房產、存款或公司線索各佔一行。",
                            "澳門確認繼承資格的程序會按配偶、子女、父母、兄弟姊妹、遺囑和個別情況要求不同證明；內地接收機構也會看資產所在地和登記資料。因此先畫完整家屬關係，比先猜哪一張證明一定足夠更實際。",
                        ],
                    ),
                    (
                        "第三步：把事實、推測和爭議分開標記",
                        [
                            "「已見原件」和「家人說有」不能放在同一欄。每條資料標記來源，例如原件、清晰影像、舊訊息、家人憶述或待機構核對。房屋地址、登記姓名、婚姻狀況和家屬去世時間尤其不要靠記憶補齊。",
                            "若兩人對遺囑、家屬身份或某項資產有不同說法，聯絡人應把兩種說法和各自資料並列，不替任何一方下結論。原件可由目前保管人妥善保存，工作表只寫存放位置，不要在家庭群組散發完整身份證號或銀行帳號。",
                        ],
                    ),
                    (
                        "甚麼時候應停止整理，轉為處理正式問題",
                        [
                            "當家屬表已能顯示逝者、配偶、子女、父母和已故家屬，資產表也能指出房產城市與登記姓名，就可以帶着這三張表向實際接收機構核對，不必等所有證明都辦好才問。",
                            "若有人拒絕透露原件、否認其他繼承人、擅自收取租金或處分財產，或家屬要求聯絡人代簽文件，便不再只是整理問題。先保存現有記錄，分清澳門文件與內地資產兩條程序，再取得針對個案的意見。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門文件和內地房產資料怎樣分開整理"),
                    ("/articles/am/macau-kinship-certificate-scope.html", "澳門親屬關係文件能證明甚麼"),
                    ("/articles/am/unknown-mainland-property-city.html", "不知道內地房產城市時先找哪些線索"),
                ],
                "cta": "先選一名整理者，寫清他的工作範圍，再用家屬、文件和資產三張表找出下一個真正需要核對的問題。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门与内地遗产",
                "title": "继承人很多，澳门家庭先选联络人时要分清哪三件事",
                "description": "澳门家庭处理内地遗产时，怎样选一名联络人整理家属、文件和资产线索，又不让他越过其他家属作决定。",
                "lead": "找一个人集中资料很有用，但“负责联络”不等于可以替所有人决定谁继承、怎样分或签什么文件。先把整理、决定和正式代表三件事分开。",
                "key_title": "先把三种角色分开",
                "keys": [
                    "联络人：收集资料、记录来源、安排核对",
                    "家属沟通：确认不同说法和未解问题",
                    "正式代表：按有效文件和具体程序行事",
                    "任何一人都不能把家人记忆写成已确认事实",
                ],
                "visuals": [
                    ("联络人可以做什么", "收集影像和线索", "更新家属问题表", "整理不是代替大家作决定。"),
                    ("三层工作不要混在一起", "整理事实", "家属确认", "正式签署", "每一层都由合适的人完成。"),
                    ("每条资料标记状态", "已见原件", "只有影像", "家人讲述", "仍有争议", "不确定的内容保留问号。"),
                ],
                "answer_title": "先说最实用的答案",
                "answer": [
                    "联络人最好是愿意做记录、能保持中立、方便联系各地家属的人，不一定是最年长的人，也不一定是保管房产证或银行信件的人。他可以建立家属名单、文件目录和资产线索表，但不应自行判断谁没有继承权、替别人放弃权利，或把尚未取得的授权写成已经授权。",
                    "澳门的正式继承文件可能由特定人士申请或签署，内地房产登记也会另外核对死亡、亲属关系、房屋权属和其他继承人。家庭工作表的作用，是让两边看到同一套事实；它不会因为写得完整，就自动成为公证书、授权书或遗产管理文件。",
                ],
                "sections": [
                    (
                        "第一步：按做事能力选人，不要按家庭排行选人",
                        [
                            "合适的联络人通常能固定回复、保存版本、把不同家属的说法分开记录，也愿意承认自己不知道。如果长子女身在海外、配偶不熟悉内地房产，或者目前已经有争议，可以由另一名较中立的家属负责整理，必要时再设一名共同复核人。",
                            "一开始就在群里写明范围：联络人只收集资料、列问题和转达回复；出售、分配、放弃、签署或委托，仍要由有权的人按实际文件处理。这句话能避免日后把方便联络误解成已经得到全家授权。",
                        ],
                    ),
                    (
                        "第二步：只做三张表，不要先建一个巨大文件库",
                        [
                            "第一张是家属表：姓名、与逝者关系、所在城市、联系状况、是否看过遗嘱。第二张是文件表：文件名称、原件保管人、签发地、日期和目前只有原件还是影像。第三张是资产表：每项内地房产、存款或公司线索各占一行。",
                            "澳门确认继承资格的程序会按配偶、子女、父母、兄弟姐妹、遗嘱和个别情况要求不同证明；内地接收机构也会看资产所在地和登记资料。因此先画完整家属关系，比先猜哪一张证明一定足够更实际。",
                        ],
                    ),
                    (
                        "第三步：把事实、推测和争议分开标记",
                        [
                            "“已见原件”和“家人说有”不能放在同一栏。每条资料标记来源，例如原件、清晰影像、旧信息、家人讲述或待机构核对。房屋地址、登记姓名、婚姻状况和家属去世时间尤其不要靠记忆补齐。",
                            "如果两个人对遗嘱、家属身份或某项资产有不同说法，联络人应把两种说法和各自资料并列，不替任何一方下结论。原件可由目前保管人妥善保存，工作表只写存放位置，不要在家庭群里散发完整身份证号或银行账号。",
                        ],
                    ),
                    (
                        "什么时候应停止整理，转为处理正式问题",
                        [
                            "当家属表已经能显示逝者、配偶、子女、父母和已故家属，资产表也能指出房产城市与登记姓名，就可以带着这三张表向实际接收机构核对，不必等所有证明都办好才问。",
                            "如果有人拒绝透露原件、否认其他继承人、擅自收取租金或处分财产，或者家属要求联络人代签文件，就不再只是整理问题。先保存现有记录，分清澳门文件与内地资产两条程序，再取得针对个案的意见。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门文件和内地房产资料怎样分开整理"),
                    ("/articles/am/macau-kinship-certificate-scope_cn.html", "澳门亲属关系文件能证明什么"),
                    ("/articles/am/unknown-mainland-property-city_cn.html", "不知道内地房产城市时先找哪些线索"),
                ],
                "cta": "先选一名整理者，写清他的工作范围，再用家属、文件和资产三张表找出下一个真正需要核对的问题。",
            },
            "en": {
                "lang": "en",
                "locale": "en_MO",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau and Mainland estates",
                "title": "Too Many Family Members, Too Many Messages: Choosing One Estate Coordinator in Macau",
                "description": "A practical way for a Macau family to appoint one information coordinator without confusing that role with legal authority over a Mainland estate.",
                "lead": "One person should keep the file moving. That person should not quietly become the family's decision-maker. Separate information gathering, family decisions and formal authority from the beginning.",
                "key_title": "Keep three roles separate",
                "keys": [
                    "Coordinator: collects documents, sources and questions",
                    "Family: confirms different accounts and unresolved facts",
                    "Formal representative: acts under the relevant appointment or authority",
                    "No one upgrades family recollection into a verified fact",
                ],
                "visuals": [
                    ("What the coordinator can do", "Collect copies and clues", "Maintain the question list", "Organising information is not making decisions."),
                    ("Three layers of work", "Organise facts", "Confirm with family", "Sign with authority", "Use the right person at each layer."),
                    ("Give every fact a status", "Original seen", "Image only", "Family account", "Still disputed", "Keep a question mark where one belongs."),
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "Choose the person who can keep a neutral record, contact relatives in different places and admit when a fact is unknown. The coordinator need not be the oldest child or the person holding the property papers. The role is to maintain a family map, document index and asset clue sheet, not to exclude an heir, waive another person's rights or sign without authority.",
                    "A formal Macau succession document may have its own applicant and signatory requirements. A Mainland property office will separately examine the death, family links, title record and other heirs. The coordinator's sheets help both sides work from the same facts, but they do not turn into a notarial deed, power of attorney or estate appointment merely because the family uses them.",
                ],
                "sections": [
                    (
                        "Choose for reliability, not family rank",
                        [
                            "A good coordinator answers consistently, keeps dated versions and records different family accounts separately. If the eldest child lives abroad, the surviving spouse does not know the Mainland property, or conflict has already started, another relative may be better placed to organise the information. A second person can check important updates.",
                            "State the limits in the family chat at the outset. The coordinator may collect, list and relay information. Sale, distribution, waiver, signature and appointment decisions remain with the person or people legally entitled to make them. This avoids treating convenience as a blanket family mandate.",
                        ],
                    ),
                    (
                        "Use three small sheets instead of one enormous archive",
                        [
                            "The family sheet lists each person, relationship to the deceased, location, contact status and whether they have seen a will. The document sheet records the paper, issuing place, date, current custodian and whether the family has an original or only an image. The asset sheet gives every possible Mainland property, account or company interest one row.",
                            "Macau heir-confirmation work can require different civil-status records depending on the family structure, while a Mainland recipient will focus on the particular asset and its registration. A complete family map is therefore more useful at the start than guessing that one certificate will answer every question.",
                        ],
                    ),
                    (
                        "Label facts, assumptions and disputes differently",
                        [
                            "Do not place 'original seen' and 'a relative remembers this' in the same column. Label each item as original, clear image, old message, family account or institution to confirm. Addresses, registered names, marital status and the death dates of earlier family members should not be completed from memory alone.",
                            "If relatives disagree about a will, a family relationship or an asset, record both accounts and the supporting material without choosing a winner. Note where an original is stored instead of circulating full identity numbers or bank details in a large family group.",
                        ],
                    ),
                    (
                        "Know when organisation has become a legal problem",
                        [
                            "Once the family map shows the spouse, children, parents and any deceased relatives, and the asset sheet identifies the city and registered owner, the family can ask the actual receiving institution focused questions. There is no need to complete every certificate before making that first enquiry.",
                            "Refusal to disclose originals, concealment of another heir, unilateral rent collection or disposal, and requests for the coordinator to sign are no longer filing problems. Preserve the current record, separate the Macau document work from the Mainland asset process, and obtain advice directed to the actual dispute.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau estate topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling Mainland estates"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Separate Macau family papers from Mainland property records"),
                    ("/articles/am/macau-kinship-certificate-scope_en.html", "What Macau family relationship records can establish"),
                    ("/articles/am/unknown-mainland-property-city_en.html", "Trace a Mainland property when the city is unknown"),
                ],
                "cta": "Choose one organiser, write down the limits of the role, and use three short sheets to identify the next question that genuinely needs an answer.",
            },
        },
    },
    {
        "slug": "singapore-death-certificate",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_SG",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡與內地遺產",
                "title": "新加坡死亡證明交到內地前，先核對哪六項",
                "description": "新加坡家屬使用數字死亡證明或死亡紀錄摘錄處理內地遺產前，先核對文件種類、姓名、編號、日期和驗證線索。",
                "lead": "先不要急着翻譯整份文件。第一步是認清手上究竟是數字死亡證明、死亡紀錄摘錄，還是系統暫時無法使用時發出的死亡確認文件。",
                "key_title": "先核對這六項",
                "keys": [
                    "文件種類、證明編號和可驗證狀態",
                    "逝者英文全名、身份號碼和曾用姓名",
                    "出生日期、死亡日期與時間",
                    "死亡地點或地址是否與其他資料一致",
                    "中文姓名怎樣連到內地登記姓名",
                    "內地接收機構實際需要證明哪一件事",
                ],
                "visuals": [
                    ("先認清手上文件", "數字死亡證明", "死亡紀錄摘錄", "名稱相近，用途和取得方式不一定相同。"),
                    ("六項逐欄核對", "姓名和身份號碼", "日期和地點", "編號和驗證", "先找差異，再決定怎樣處理。"),
                    ("死亡事實不是全部", "死亡文件", "親屬關係", "內地資產記錄", "代表權文件", "四條資料線要逐一連上。"),
                ],
                "answer_title": "先說最實用的答案",
                "answer": [
                    "新加坡在當地完成死亡登記後，現時通常簽發數字死亡證明。現行安排下，家屬要在 30 日內下載並保存檔案；錯過後可按程序申請死亡紀錄摘錄。若醫生在系統暫時無法使用時先給死亡確認文件，該文件主要解決當時的殯葬安排，不能只憑名稱相似便假定它與正式死亡證明用途相同。",
                    "死亡證明可以說明死亡記錄，但通常不能單獨證明誰是全部繼承人、誰已獲權代表遺產，或內地房產屬於逝者。把姓名、身份號碼、日期和地點核對好後，還要另接親屬關係、代表文件及內地資產登記資料。",
                ],
                "sections": [
                    (
                        "第一步：看文件名稱和取得方式",
                        [
                            "先記下文件抬頭、證明編號、下載或申領日期，以及檔案能否通過原有驗證方式核對。不要把醫生或醫院暫時提供的死亡確認文件、數字死亡證明和後來申請的死亡紀錄摘錄混成同一份文件。",
                            "因此收到下載資料後應盡快把原始檔案存到安全位置。若家屬只剩截圖、列印件或轉發影像，先問清原始檔案在哪裏，再決定是否需要重新取得可核對的版本。",
                        ],
                    ),
                    (
                        "第二步：逐欄核對姓名、號碼、日期和地點",
                        [
                            "把英文全名、身份文件號碼、出生日期、死亡日期、死亡時間和地點，與護照、身份文件、遺囑及新加坡法院文件逐項對照。常見問題不是文件完全錯誤，而是中間名、連字號、曾用姓名或日期格式在不同文件中寫法不同。",
                            "若一份文件寫醫院名稱，另一份寫完整地址，不要立即判定矛盾；先查兩者是否指向同一地點。若身份號碼或死亡日期確實不一致，應在翻譯和後續使用前處理，不要靠譯文把兩個版本勉強寫成一樣。",
                        ],
                    ),
                    (
                        "第三步：另外做一張中英文姓名連接表",
                        [
                            "新加坡死亡文件可能只顯示英文姓名，而內地房產證、舊戶籍資料或銀行記錄使用中文姓名。姓名連接表可列出每個寫法出現在哪份文件、使用哪個身份號碼或出生日期作旁證，以及目前還缺哪一段。",
                            "音譯相近並不足以自行證明是同一人。若中文姓名曾變更、護照次序不同，或內地登記含曾用名，應先向實際接收機構說明現有文件，再問需要補哪類連接資料。",
                        ],
                    ),
                    (
                        "第四步：先問用途，再做翻譯和後續手續",
                        [
                            "新加坡法院在當地遺產申請中會要求相應死亡證明材料，但內地房產登記、銀行或公司所問的並不只是一句「有沒有死亡證明」。接收方可能要核對死亡事實、文件真實性、親屬關係、代表權或房屋登記姓名，這些是不同問題。",
                            "先把接收城市、資產種類、登記姓名和手上文件版本說清楚，再確認要提交原始數字檔、列印件、摘錄或其他處理。這樣能避免把一份不對用途的文件先翻譯、辦理後，才發現真正缺的是姓名連接或代表文件。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/singapore-family-first-fact-sheet.html", "家屬第一次整理內地遺產的一頁事實表"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "有遺囑和無遺囑時法院文件有甚麼不同"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "內地房產有沒有列入 Schedule of Assets"),
                ],
                "cta": "先把文件種類和六項資料核對好，再帶着內地資產所在地與登記姓名去問實際接收機構，會比先做整套文件更省時間。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡与内地遗产",
                "title": "新加坡死亡证明交到内地前，先核对哪六项",
                "description": "新加坡家属使用数字死亡证明或死亡记录摘录处理内地遗产前，先核对文件种类、姓名、编号、日期和验证线索。",
                "lead": "先不要急着翻译整份文件。第一步是认清手上究竟是数字死亡证明、死亡记录摘录，还是系统暂时无法使用时发出的死亡确认文件。",
                "key_title": "先核对这六项",
                "keys": [
                    "文件种类、证明编号和可验证状态",
                    "逝者英文全名、身份号码和曾用姓名",
                    "出生日期、死亡日期与时间",
                    "死亡地点或地址是否与其他资料一致",
                    "中文姓名怎样连到内地登记姓名",
                    "内地接收机构实际需要证明哪一件事",
                ],
                "visuals": [
                    ("先认清手上文件", "数字死亡证明", "死亡记录摘录", "名称相近，用途和取得方式不一定相同。"),
                    ("六项逐栏核对", "姓名和身份号码", "日期和地点", "编号和验证", "先找差异，再决定怎样处理。"),
                    ("死亡事实不是全部", "死亡文件", "亲属关系", "内地资产记录", "代表权文件", "四条资料线要逐一连上。"),
                ],
                "answer_title": "先说最实用的答案",
                "answer": [
                    "新加坡在当地完成死亡登记后，现在通常签发数字死亡证明。现行安排下，家属要在 30 日内下载并保存文件；错过后可按程序申请死亡记录摘录。如果医生在系统暂时无法使用时先给死亡确认文件，该文件主要解决当时的殡葬安排，不能只凭名称相似就假定它和正式死亡证明用途相同。",
                    "死亡证明可以说明死亡记录，但通常不能单独证明谁是全部继承人、谁已经有权代表遗产，或者内地房产属于逝者。把姓名、身份号码、日期和地点核对好后，还要另外连接亲属关系、代表文件及内地资产登记资料。",
                ],
                "sections": [
                    (
                        "第一步：看文件名称和取得方式",
                        [
                            "先记下文件抬头、证明编号、下载或申领日期，以及文件能否通过原有验证方式核对。不要把医生或医院暂时提供的死亡确认文件、数字死亡证明和后来申请的死亡记录摘录混成同一份文件。",
                            "因此收到下载资料后应尽快把原始文件存到安全位置。如果家属只剩截图、打印件或转发影像，先问清原始文件在哪里，再决定是否需要重新取得可以核对的版本。",
                        ],
                    ),
                    (
                        "第二步：逐栏核对姓名、号码、日期和地点",
                        [
                            "把英文全名、身份文件号码、出生日期、死亡日期、死亡时间和地点，与护照、身份文件、遗嘱及新加坡法院文件逐项对照。常见问题不是文件完全错误，而是中间名、连字符、曾用姓名或日期格式在不同文件中写法不同。",
                            "如果一份文件写医院名称，另一份写完整地址，不要马上判断矛盾；先查两者是否指向同一地点。如果身份号码或死亡日期确实不一致，应在翻译和后续使用前处理，不要靠译文把两个版本勉强写成一样。",
                        ],
                    ),
                    (
                        "第三步：另外做一张中英文姓名连接表",
                        [
                            "新加坡死亡文件可能只显示英文姓名，而内地房产证、旧户籍资料或银行记录使用中文姓名。姓名连接表可以列出每个写法出现在哪份文件、使用哪个身份号码或出生日期作旁证，以及目前还缺哪一段。",
                            "音译相近并不足以自行证明是同一个人。如果中文姓名曾经变更、护照次序不同，或者内地登记含曾用名，应先向实际接收机构说明现有文件，再问需要补哪类连接资料。",
                        ],
                    ),
                    (
                        "第四步：先问用途，再做翻译和后续手续",
                        [
                            "新加坡法院在当地遗产申请中会要求相应死亡证明材料，但内地房产登记、银行或公司所问的并不只是一句“有没有死亡证明”。接收方可能要核对死亡事实、文件真实性、亲属关系、代表权或房屋登记姓名，这些是不同问题。",
                            "先把接收城市、资产种类、登记姓名和手上文件版本说清楚，再确认要提交原始数字文件、打印件、摘录或其他处理。这样能避免把一份不对用途的文件先翻译、办理后，才发现真正缺的是姓名连接或代表文件。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/singapore-family-first-fact-sheet_cn.html", "家属第一次整理内地遗产的一页事实表"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "有遗嘱和无遗嘱时法院文件有什么不同"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "内地房产有没有列入 Schedule of Assets"),
                ],
                "cta": "先把文件种类和六项资料核对好，再带着内地资产所在地与登记姓名去问实际接收机构，会比先做整套文件更省时间。",
            },
            "en": {
                "lang": "en",
                "locale": "en_SG",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore and Mainland estates",
                "title": "Six Checks Before Using a Singapore Death Certificate for a Mainland Estate",
                "description": "How a Singapore family can review a digital death certificate or death extract before using it for a Mainland property, account or company interest.",
                "lead": "Do not begin with translation. Begin by identifying the document: a digital death certificate, a later death extract, or a temporary Confirmation of Death issued when the registration system was unavailable.",
                "key_title": "Check six items first",
                "keys": [
                    "Document type, certificate number and verification status",
                    "Full English name, identity number and former names",
                    "Birth date, death date and time",
                    "Place or address of death",
                    "The link to the Chinese name in the Mainland record",
                    "The exact fact the Mainland recipient needs proved",
                ],
                "visuals": [
                    ("Identify the document", "Digital death certificate", "Death extract", "Similar names do not guarantee the same use."),
                    ("Check six fields", "Name and identity number", "Dates and place", "Number and verification", "Find differences before choosing a remedy."),
                    ("Death is only one fact", "Death record", "Family relationship", "Mainland asset record", "Representative authority", "Connect four separate evidence lines."),
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "After a death is registered in Singapore, the current process normally produces a digital death certificate. Under the current arrangement, the family has 30 days to download and save the file; a death extract can be requested later if necessary. A manual Confirmation of Death may be issued when the online system is unavailable, but it principally supports the immediate funeral process and should not be treated as interchangeable with the registered certificate merely because the names sound alike.",
                    "A death certificate records the death. It does not, by itself, identify every heir, appoint an estate representative or prove that a Mainland property belonged to the deceased. Once the names, identity number, dates and place are consistent, the family still has to connect the relationship evidence, representative papers and asset record.",
                ],
                "sections": [
                    (
                        "First identify the document and how it was obtained",
                        [
                            "Record the heading, certificate number, download or issue date, and whether the file can still be checked through its original verification method. Keep a digital death certificate, a death extract and a temporary Confirmation of Death as three distinct records in the file index.",
                            "Save the original file securely as soon as the download details arrive. If the family only has a screenshot, printout or forwarded image, locate the original file before deciding whether a new verifiable record is needed.",
                        ],
                    ),
                    (
                        "Compare names, numbers, dates and place line by line",
                        [
                            "Compare the full English name, identification number, birth date, death date, time and place with the passport, identity papers, will and any Singapore court documents. The usual problem is not a completely false record. It is a middle name, hyphen, former name or date format that appears differently across the file.",
                            "A hospital name on one paper and a street address on another may describe the same place. Verify that before treating them as a conflict. A genuine difference in the identity number or death date should be addressed before translation; a translator should not silently force two versions to match.",
                        ],
                    ),
                    (
                        "Build a separate English-to-Chinese name bridge",
                        [
                            "The Singapore record may show only an English name, while the Mainland property certificate, old household record or bank file uses Chinese characters. List every spelling, the document where it appears, and the identity number or birth date that supports the connection. Mark the missing link rather than guessing it.",
                            "A similar transliteration is not conclusive proof of identity. Where a Chinese name changed, passport order differs or the Mainland record contains a former name, show the receiving institution the documents already available and ask what kind of connecting evidence it needs.",
                        ],
                    ),
                    (
                        "Ask about the purpose before translation and further processing",
                        [
                            "Singapore probate applications use the appropriate death certificate material, but a Mainland property office, bank or company is not asking only whether a death certificate exists. It may need proof of death, authenticity, family relationship, representative authority or the link to a registered owner. Those are separate questions.",
                            "Identify the receiving city, asset type, registered name and document version first. Then confirm whether the recipient wants the original digital file, a printout, an extract or another treatment. This avoids processing the wrong document before discovering that the real gap is a name bridge or an appointment paper.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore estate topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling Mainland estates"),
                    ("/articles/singapore/singapore-family-first-fact-sheet_en.html", "A one-page estate fact sheet for the family"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate and administration papers serve different roles"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Check whether a Mainland property appears in the Schedule of Assets"),
                ],
                "cta": "Check the document type and six key details, then ask the actual Mainland recipient about the asset and registered name before processing the whole file.",
            },
        },
    },
]


def article_path(article: dict, lang: str) -> str:
    return f"/{article['directory']}/{article['slug']}{LANG_SUFFIX[lang]}.html"


def write_articles() -> None:
    for article in ARTICLES:
        target_dir = ROOT / article["directory"]
        for lang in ("tc", "cn", "en"):
            suffix = LANG_SUFFIX[lang]
            page = render_article(article, lang)
            (target_dir / f"{article['slug']}{suffix}.html").write_text(
                page, encoding="utf-8"
            )


HUB_UPDATES = {
    "articles/macau/index.html": {
        "href": "/articles/am/family-coordinator-first-sheet.html",
        "card": '<a href="/articles/am/family-coordinator-first-sheet.html"><span class="v24-tag">家庭整理</span><strong>繼承人很多，先選聯絡人時要分清哪三件事</strong><p>分開資料整理、家屬決定和正式代表，避免聯絡人無意中越權。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/macau/index_cn.html": {
        "href": "/articles/am/family-coordinator-first-sheet_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">家庭整理</span><h3>继承人很多，先选联络人时要分清哪三件事</h3><p>分开资料整理、家属决定和正式代表，避免联络人无意中越权。</p></div><a class="v25-pill-action" href="/articles/am/family-coordinator-first-sheet_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/macau/index_en.html": {
        "href": "/articles/am/family-coordinator-first-sheet_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Family file</span><h3>Choosing one estate coordinator in a large Macau family</h3><p>Separate information gathering, family decisions and formal authority.</p></div><a class="v25-pill-action" href="/articles/am/family-coordinator-first-sheet_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index.html": {
        "href": "/articles/singapore/singapore-death-certificate.html",
        "card": '<a href="/articles/singapore/singapore-death-certificate.html"><span class="v24-tag">死亡文件</span><strong>新加坡死亡證明交到內地前，先核對哪六項</strong><p>先分清文件種類，再核對姓名、編號、日期、地點和驗證線索。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/singapore/index_cn.html": {
        "href": "/articles/singapore/singapore-death-certificate_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">死亡文件</span><h3>新加坡死亡证明交到内地前，先核对哪六项</h3><p>先分清文件种类，再核对姓名、编号、日期、地点和验证线索。</p></div><a class="v25-pill-action" href="/articles/singapore/singapore-death-certificate_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index_en.html": {
        "href": "/articles/singapore/singapore-death-certificate_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Death record</span><h3>Six checks before using a Singapore death certificate</h3><p>Identify the document, then compare names, numbers, dates, place and verification.</p></div><a class="v25-pill-action" href="/articles/singapore/singapore-death-certificate_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
}


SG_UPCOMING = {
    "articles/singapore/index.html": (
        '<span>3 個方向</span></summary><div class="topic-upcoming-grid"><span>新加坡死亡文件交內地前先問甚麼</span><span>家人不能回內地時誰來簽署和收件</span><span>有人反對遺囑或申請人時先保存哪些資料</span>',
        '<span>2 個方向</span></summary><div class="topic-upcoming-grid"><span>家人不能回內地時誰來簽署和收件</span><span>有人反對遺囑或申請人時先保存哪些資料</span>',
    ),
    "articles/singapore/index_cn.html": (
        '<span>3 个方向</span></summary><div class="topic-upcoming-grid"><span>新加坡死亡文件交内地前先问什么</span><span>家人不能回内地时谁来签署和收件</span><span>有人反对遗嘱或申请人时先保存哪些资料</span>',
        '<span>2 个方向</span></summary><div class="topic-upcoming-grid"><span>家人不能回内地时谁来签署和收件</span><span>有人反对遗嘱或申请人时先保存哪些资料</span>',
    ),
    "articles/singapore/index_en.html": (
        '<span>3 directions</span></summary><div class="topic-upcoming-grid"><span>Preparing a Singapore death record for Mainland use</span><span>Signing and receiving documents when no one can travel</span><span>Preserving evidence when the will or applicant is challenged</span>',
        '<span>2 directions</span></summary><div class="topic-upcoming-grid"><span>Signing and receiving documents when no one can travel</span><span>Preserving evidence when a will or applicant is challenged</span>',
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
        if relative_path in SG_UPCOMING:
            old, new = SG_UPCOMING[relative_path]
            if old not in text and new not in text:
                raise RuntimeError(f"Singapore upcoming marker missing: {relative_path}")
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
    for hub in ("macau", "singapore"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, f"{SITE}/articles/{hub}/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
