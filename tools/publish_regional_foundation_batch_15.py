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
        "slug": "macau-name-mismatch-property-record",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門姓名資料與內地房產",
                "title": "澳門證件姓名對不上內地房產登記，先怎樣證明是同一人",
                "description": "澳門證件與內地房產登記姓名不同時，先分清寫法差異、真正改名和證件更換，再整理同一人資料鏈。",
                "lead": "先不要把每個不同寫法都當成錯名。中文、葡文、拼音、姓名次序或舊證件號碼不同，所需的連接資料並不一樣。",
                "key_title": "先抄下三組資料",
                "keys": [
                    "澳門現有身份證上的中文名、其他文字姓名和證件號碼",
                    "內地房產登記姓名、證件種類、號碼和最初登記年份",
                    "舊旅行證件、買房文件或曾經使用姓名的紀錄",
                ],
                "answer_title": "先說結論",
                "answer": [
                    "姓名不完全一樣，不代表一定是兩個人；但只做一份翻譯，也不能證明兩種寫法屬於同一人。先把現有澳門證件、舊證件、房產登記和買房時的身份資料逐項對照，再找能連接改名前後或不同文字姓名的正式紀錄。",
                    "內地登記機構真正要確認的是：現在提出申請的人，是否就是登記簿上的權利人或與該權利人相連的逝者。不同城市的收件做法可能不同，所以先用掃描件和對照表問清楚，再決定辦哪一份證明。",
                ],
                "sections": [
                    (
                        "一、把不同寫法放在同一張表",
                        [
                            "左邊抄澳門居民身份證、護照或旅行證件的姓名和號碼；中間抄內地房產證、登記查詢結果或買房合約上的資料；右邊列出生日期、父母姓名、舊地址和簽名等輔助線索。每一項旁邊寫明來自哪份文件，不要自行補字或統一拼音。",
                            "房產資料只有中文名，澳門證件同時有中文和其他文字姓名，通常先看能否由同一份官方身份紀錄把兩者連起來。若房產登記使用的是已失效證件號碼，還要另找舊證件或證件更換紀錄。",
                        ],
                    ),
                    (
                        "二、分清寫法不同，還是真的改過資料",
                        [
                            "空格、連字號、姓名次序、葡文拼法或拼音不同，可能只是書寫方式差異；增加中文名、婚後改姓、正式更名或證件號碼更換，則屬於身份資料曾經變動。兩類情況不能只用一句「翻譯不同」帶過。",
                            "如果只是文字轉寫，對照表和完整證件頁往往是起點；如果姓名或證件資料真的改過，則要找能說明變更前後屬於同一人的紀錄。翻譯負責把文字說清楚，不能代替身份連接證明。",
                        ],
                    ),
                    (
                        "三、澳門資料要按實際缺口補",
                        [
                            "澳門的個人資料證明書是可能的連接文件之一，某些歷史情況還可能涉及曾經使用的姓名。先向身份資料保管部門說明用途、舊姓名或舊證件線索，確認可申請的證明內容；若舊資料不在現有紀錄內，還要保留舊旅行證件、買房文件或其他變更紀錄。",
                            "如逝者已離世，還要分開處理誰有權申請資料、死亡紀錄和親屬關係。姓名銜接只回答「是不是同一人」，不會同時證明誰是繼承人，也不會直接完成房產轉名。",
                        ],
                    ),
                    (
                        "四、先讓房產所在地看對照表",
                        [
                            "把房產城市、登記姓名、舊證件號碼、現有澳門證件和差異說明放在一頁，先問接收方需要原件、正式副本、身份變更證明還是其他同一人資料。房產登記本身寫錯，和權利人後來改名，也可能走不同處理方式。",
                            "未確認要求前，不要把唯一舊證件寄出，也不要先把所有澳門文件翻譯或辦證。先補最短的一段身份連接，再處理親屬、遺囑和房產權利資料，通常較少重做。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/portuguese-documents-translation.html", "澳門葡文文件翻譯容易漏掉甚麼"),
                    ("/articles/am/macau-kinship-certificate-scope.html", "親屬關係文件能證明甚麼"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "繼承內地房產先分清兩套文件"),
                ],
                "cta": "說明房產城市、登記姓名、舊證件和現有澳門證件的寫法，先判斷缺的是翻譯、身份連接還是其他文件。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门姓名资料与内地房产",
                "title": "澳门证件姓名对不上内地房产登记，先怎样证明是同一个人",
                "description": "澳门证件与内地房产登记姓名不同时，先分清写法差异、真正改名和证件更换，再整理同一人资料链。",
                "lead": "先不要把每个不同写法都当成错名。中文、葡文、拼音、姓名顺序或旧证件号码不同，需要补的连接资料也不同。",
                "key_title": "先抄下三组资料",
                "keys": [
                    "澳门现有身份证上的中文名、其他文字姓名和证件号码",
                    "内地房产登记姓名、证件类型、号码和最初登记年份",
                    "旧旅行证件、购房文件或曾经使用姓名的记录",
                ],
                "answer_title": "先说结论",
                "answer": [
                    "姓名不完全一样，不代表一定是两个人；但只做一份翻译，也不能证明两种写法属于同一个人。先把现有澳门证件、旧证件、房产登记和购房时的身份资料逐项对照，再找能连接改名前后或不同文字姓名的正式记录。",
                    "内地登记机构真正要确认的是：现在提出申请的人，是否就是登记簿上的权利人，或能否与该权利人对应的逝者相连。不同城市的收件做法可能不同，先用扫描件和对照表问清楚，再决定办哪一份证明。",
                ],
                "sections": [
                    (
                        "一、把不同写法放在同一张表",
                        [
                            "左边抄澳门居民身份证、护照或旅行证件的姓名和号码；中间抄内地房产证、登记查询或购房合同上的资料；右边列出生日期、父母姓名、旧地址和签名等辅助线索。每一项旁边写明来自哪份文件，不要自行补字或统一拼音。",
                            "房产资料只有中文名，澳门证件同时有中文和其他文字姓名时，通常先看能否由同一份官方身份记录把两者连起来。房产登记使用已失效证件号码的，还要另找旧证件或证件更换记录。",
                        ],
                    ),
                    (
                        "二、分清写法不同，还是真的改过资料",
                        [
                            "空格、连字符、姓名顺序、葡文拼法或拼音不同，可能只是书写方式差异；增加中文名、婚后改姓、正式更名或证件号码更换，则属于身份资料发生过变化。两类情况不能只用一句“翻译不同”带过。",
                            "如果只是文字转写，对照表和完整证件页往往是起点；如果姓名或证件资料真的改过，就要找能说明变更前后属于同一个人的记录。翻译负责把文字说清楚，不能代替身份连接证明。",
                        ],
                    ),
                    (
                        "三、澳门资料要按实际缺口补",
                        [
                            "澳门的个人资料证明书是可能的连接材料之一，某些历史情况还可能涉及曾经使用的姓名。先向身份资料保管部门说明用途、旧姓名或旧证件线索，确认可以申请的证明内容；如果旧资料不在现有记录内，还要保留旧旅行证件、购房文件或其他变更记录。",
                            "如果逝者已经离世，还要分开处理谁有权申请资料、死亡记录和亲属关系。姓名衔接只回答“是不是同一个人”，不会同时证明谁是继承人，也不会直接完成房产过户。",
                        ],
                    ),
                    (
                        "四、先让房产所在地看对照表",
                        [
                            "把房产城市、登记姓名、旧证件号码、现有澳门证件和差异说明放在一页，先问接收方需要原件、正式副本、身份变更证明还是其他同一人资料。房产登记本身写错，和权利人后来改名，也可能走不同处理方式。",
                            "没有确认要求前，不要把唯一旧证件寄出，也不要先把所有澳门文件翻译或办证。先补最短的一段身份连接，再处理亲属、遗嘱和房产权利资料，通常更少返工。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/portuguese-documents-translation_cn.html", "澳门葡文文件翻译容易漏掉什么"),
                    ("/articles/am/macau-kinship-certificate-scope_cn.html", "亲属关系文件能证明什么"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "继承内地房产先分清两套文件"),
                ],
                "cta": "说明房产城市、登记姓名、旧证件和现有澳门证件的写法，先判断缺的是翻译、身份连接还是其他文件。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau identity records and Mainland property",
                "title": "When a Macau Name Does Not Match a Mainland Property Record",
                "description": "A practical way to connect a Macau identity record to a different name or document number in a Mainland property record.",
                "lead": "Do not treat every difference as a mistake. A Chinese name, Portuguese spelling, name order or old document number may require a different link in the evidence.",
                "key_title": "Copy three sets of details",
                "keys": [
                    "The Chinese and other-script names on the current Macau identity record",
                    "The name, document type and number in the Mainland property record",
                    "Any earlier travel document, purchase paper or former-name record",
                ],
                "answer_title": "The short answer",
                "answer": [
                    "A partial name match does not necessarily mean two different people. A translation alone, however, does not establish that two versions identify the same person. Compare the current Macau record, earlier documents, the property record and the identity used for the original purchase.",
                    "The Mainland recipient needs a reliable link between the current applicant and the person recorded as owner, or between the deceased and that owner. Prepare a one-page comparison first, then ask the property registry or receiving adviser in the relevant city what form of connecting evidence it will review.",
                ],
                "sections": [
                    (
                        "1. Put every version on one page",
                        [
                            "Copy the name and number from the Macau identity card, passport or travel document in the first column. Add the Mainland title record, registry search or purchase contract in the second. Use the third for date of birth, parents' names, former address and signature clues. Label the source of every entry instead of silently standardising the spelling.",
                            "If the property record has only a Chinese name while the Macau document carries both Chinese and another-script names, look for an official record that connects them. If the property was registered with an expired document number, keep the old document or a record of its replacement.",
                        ],
                    ),
                    (
                        "2. Separate spelling variation from an actual change",
                        [
                            "Spaces, hyphens, name order, Portuguese spelling and romanisation may be presentation differences. Adding a Chinese name, changing a family name or replacing an identity number is a change in the underlying record. The two situations should not be explained in the same way.",
                            "A full copy and comparison sheet may start a spelling review. An actual name or document change calls for a record connecting the old and new details. Translation explains words; it does not replace evidence that both records identify one person.",
                        ],
                    ),
                    (
                        "3. Ask for the Macau record that fits the gap",
                        [
                            "A Macau personal-data certificate may form one part of the link, and certain historical cases may involve a formerly used name. Explain the intended use and the old-name or old-document clue before applying. If the earlier detail is not held in the current record, keep the former travel document, purchase papers or another change record.",
                            "Where the person has died, authority to request records, the death record and family relationship are separate questions. Solving the name link does not identify every heir or transfer the Mainland property.",
                        ],
                    ),
                    (
                        "4. Show the comparison before ordering every document",
                        [
                            "Send the property city, registered name, old document number, current Macau record and a short explanation to the receiving side. Ask whether it needs an original, official copy, change record or another record linking the identities. A registry error and a later name change may follow different routes.",
                            "Keep the only original old document until the route is confirmed. Build the shortest reliable identity link first, then address family, will and property-entitlement papers. This usually avoids unnecessary translation and repeat applications.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"),
                    ("/articles/am/portuguese-documents-translation_en.html", "Translating a Macau Portuguese estate document"),
                    ("/articles/am/macau-kinship-certificate-scope_en.html", "What Macau family records establish"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Keeping the Macau and Mainland property files separate"),
                ],
                "cta": "Start with the property city, registered name, old document and current Macau identity details, then identify the missing link.",
            },
        },
    },
    {
        "slug": "known-mainland-bank-account",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與內地銀行存款",
                "title": "知道內地銀行帳戶，新加坡家屬先準備甚麼",
                "description": "新加坡家屬已知道內地銀行和帳戶時，先整理帳戶線索、身份、代表權限和跨境文件，再問銀行收件要求。",
                "lead": "知道銀行名稱和帳戶，只代表已有一條明確線索，不等於任何家屬都可以查餘額或提取款項。先分清要問甚麼、由誰去問。",
                "key_title": "先準備三組資料",
                "keys": [
                    "銀行全名、開戶分行、帳戶或存摺線索和產品種類",
                    "逝者姓名、證件號碼，以及新加坡和內地資料的差異",
                    "申請人身份、親屬關係、遺囑和現有遺產代表文件",
                ],
                "answer_title": "最重要的答案",
                "answer": [
                    "先不要嘗試登入逝者的網上銀行、使用密碼或把款項轉走。把銀行、分行、帳戶、產品和持有人資料寫成一張線索卡，再由有合理身份的人向銀行詢問：目前可以查甚麼，提取又另需甚麼。",
                    "新加坡的遺產授予文件可以說明誰在當地代表遺產，資產清單也可記錄境外資產；但它們不會自動命令內地銀行付款。涉及新加坡家屬或境外身份時，也不能直接套用只看金額的小額簡化做法，應先由開戶銀行確認跨境文件。",
                ],
                "sections": [
                    (
                        "一、先做一張帳戶線索卡",
                        [
                            "寫下銀行的完整名稱、開戶分行或城市、帳號尾數、存摺或銀行卡照片來源、幣種、定期或活期、理財或其他產品，以及最後一筆可核對的交易。不要在多人聊天群傳完整帳號、密碼或驗證碼。",
                            "同一個銀行品牌下，實際開立帳戶的銀行機構未必相同；存款、理財和代銷產品的處理窗口也可能不同。先讓銀行確認帳戶歸哪個機構、屬哪類資產，不要只憑標誌或手機應用程式猜分行。",
                        ],
                    ),
                    (
                        "二、分清查詢的人和領款的人",
                        [
                            "申請查詢、代表遺產辦事和最後取得款項，可能不是同一個角色。先列出逝者、遺囑執行人或遺產管理人、配偶、子女、父母和其他受益人，再標明每人手上有甚麼身份或關係文件。",
                            "新加坡法院發出的遺產授予文件，通常在申請和資產資料獲處理後才發出；銀行或其他機構還可能要求正式副本。先確認現有文件是申請文件、法院命令、正式授予文件還是資產清單，不要把它們都叫成一張「繼承證明」。",
                        ],
                    ),
                    (
                        "三、跨境個案不要先套小額做法",
                        [
                            "內地一般的小額存款簡化安排設有金額、申請人和文件條件；現行安排沿用的原有框架，明確把涉及境外個人的個案放在簡化範圍以外。新加坡家屬、外籍或境外定居身份是否適用其他做法，不能只看帳戶是否少於某個金額。",
                            "向銀行說清逝者和申請人的國籍、居留和證件情況，並問明死亡文件、親屬或遺囑資料、遺產代表文件、中文翻譯、跨境證明和委託是否需要。銀行文件不齊時，要求對方一次列出缺口，較適合遠程準備。",
                        ],
                    ),
                    (
                        "四、第一次聯絡銀行問清六件事",
                        [
                            "一次問清：受理分行、可先查的資料、查詢和提取分別由誰申請、境外文件要甚麼版本、能否由代理人遞交、款項最後可付到甚麼帳戶。把回覆日期、部門和所需文件逐項記下。",
                            "若家屬對繼承人、遺囑或款項分配有爭議，先保留餘額和交易線索，不要讓其中一人先領走再自行分配。銀行確認的只是付款條件，家屬之間的權利和分配仍要另外處理。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "有遺囑和無遺囑的法院文件有甚麼不同"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "境外資產怎樣放入資產清單"),
                    ("/articles/singapore/singapore-family-first-fact-sheet.html", "第一次整理遺產的一頁事實表"),
                ],
                "cta": "先寫下銀行、分行、帳戶線索、逝者身份和現有代表文件，再判斷應先查詢還是準備提取。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与内地银行存款",
                "title": "知道内地银行账户，新加坡家属先准备什么",
                "description": "新加坡家属已经知道内地银行和账户时，先整理账户线索、身份、代表权限和跨境文件，再向银行确认要求。",
                "lead": "知道银行名称和账户，只说明已经有一条明确线索，不等于任何家属都可以查询余额或提取款项。先分清要问什么、由谁去问。",
                "key_title": "先准备三组资料",
                "keys": [
                    "银行全名、开户网点、账户或存折线索和产品类型",
                    "逝者姓名、证件号码，以及新加坡和内地资料的差异",
                    "申请人身份、亲属关系、遗嘱和现有遗产代表文件",
                ],
                "answer_title": "最重要的答案",
                "answer": [
                    "先不要尝试登录逝者的网上银行、使用密码或把款项转走。把银行、网点、账户、产品和持有人资料写成一张线索卡，再由有合理身份的人向银行询问：目前可以查询什么，提取又另外需要什么。",
                    "新加坡的遗产授予文件可以说明谁在当地代表遗产，资产清单也可以记录境外资产；但它们不会自动要求内地银行付款。涉及新加坡家属或境外身份时，也不能直接套用只看金额的小额简化做法，应先由开户银行确认跨境材料。",
                ],
                "sections": [
                    (
                        "一、先做一张账户线索卡",
                        [
                            "写下银行的完整名称、开户网点或城市、账号尾号、存折或银行卡照片来源、币种、定期或活期、理财或其他产品，以及最后一笔可以核对的交易。不要在多人聊天群发送完整账号、密码或验证码。",
                            "同一个银行品牌下，实际开立账户的银行机构不一定相同；存款、理财和代销产品的处理窗口也可能不同。先让银行确认账户归哪个机构、属于哪类资产，不要只凭标志或手机应用猜开户网点。",
                        ],
                    ),
                    (
                        "二、分清查询的人和领款的人",
                        [
                            "申请查询、代表遗产办理事务和最后取得款项，可能不是同一个角色。先列出逝者、遗嘱执行人或遗产管理人、配偶、子女、父母和其他受益人，再标明每个人手上有什么身份或关系文件。",
                            "新加坡法院发出的遗产授予文件，通常在申请和资产资料得到处理后才发出；银行或其他机构还可能要求正式副本。先确认现有文件是申请材料、法院命令、正式授予文件还是资产清单，不要把它们都叫成一张“继承证明”。",
                        ],
                    ),
                    (
                        "三、跨境情况不要先套小额做法",
                        [
                            "内地一般的小额存款简化安排设有金额、申请人和文件条件；现行安排沿用的原有框架，明确把涉及境外个人的情况放在简化范围以外。新加坡家属、外籍或境外定居身份是否适用其他做法，不能只看账户是否少于某个金额。",
                            "向银行说明逝者和申请人的国籍、居留和证件情况，并问清死亡文件、亲属或遗嘱资料、遗产代表文件、中文翻译、跨境证明和委托是否需要。材料不齐时，请银行一次列出缺口，更方便远程准备。",
                        ],
                    ),
                    (
                        "四、第一次联系银行问清六件事",
                        [
                            "一次问清：受理网点、可以先查询的资料、查询和提取分别由谁申请、境外文件需要什么版本、能否由代理人提交、款项最后可以支付到什么账户。把回复日期、部门和所需文件逐项记下。",
                            "如果家属对继承人、遗嘱或款项分配有争议，先保留余额和交易线索，不要让其中一人先领取后自行分配。银行确认的是付款条件，家属之间的权利和分配仍要另外处理。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "有遗嘱和无遗嘱的法院文件有什么不同"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "境外资产怎样放入资产清单"),
                    ("/articles/singapore/singapore-family-first-fact-sheet_cn.html", "第一次整理遗产的一页事实表"),
                ],
                "cta": "先写下银行、网点、账户线索、逝者身份和现有代表文件，再判断应先查询还是准备提取。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore families and Mainland bank funds",
                "title": "A Singapore Family Knows the Mainland Bank Account: What Comes First?",
                "description": "What a Singapore family should organise before asking a Mainland bank about a deceased person's known account.",
                "lead": "A bank name and account number are useful clues. They do not allow every relative to see the balance or withdraw the funds. First decide what is being requested and who should make the request.",
                "key_title": "Prepare three groups of information",
                "keys": [
                    "The bank, branch, account clue and type of product",
                    "The deceased's name, identity number and any cross-border mismatch",
                    "The applicant's role, family evidence, will and current grant papers",
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "Do not log into the deceased's online banking, use a password or move the money. Make a short account card covering the bank, branch, account clue, product and account holder. A person with a proper basis can then ask the bank what may be disclosed and what separate documents would be needed for release.",
                    "A Singapore grant may identify the local estate representative, and the Schedule of Assets may record overseas property. Neither document automatically directs a Mainland bank to pay. A cross-border applicant should also not assume that a simplified small-balance process applies merely because the amount is low; the account-holding institution should confirm its overseas-document route.",
                ],
                "sections": [
                    (
                        "1. Create a one-page account card",
                        [
                            "Record the full bank name, branch or city, final account digits, source of any passbook or card image, currency, deposit term and any wealth-management or other product. Add the last transaction that can be verified. Do not circulate full account numbers, passwords or verification codes in a family group chat.",
                            "Accounts under the same banking brand may be held by different banking entities, while deposits, bank-issued products and third-party products may use different service channels. Ask which entity holds the account and what kind of asset it is before guessing the branch from a logo or mobile app.",
                        ],
                    ),
                    (
                        "2. Separate the enquirer from the recipient",
                        [
                            "The person asking for information, the estate representative and the person ultimately entitled to money may not be the same. List the deceased, executor or administrator, spouse, children, parents and other beneficiaries, then note the identity and relationship evidence held by each person.",
                            "A Singapore grant is issued after the application and supporting estate information have been addressed. A bank may still ask for a certified copy. Identify whether the family currently has an application paper, court order, issued grant or Schedule of Assets instead of calling all of them an inheritance certificate.",
                        ],
                    ),
                    (
                        "3. Do not assume a small-balance shortcut applies",
                        [
                            "The Mainland simplified process for certain small balances has conditions concerning the amount, applicant and supporting documents. The framework retained by the current arrangement excludes cases involving overseas individuals from that simplified route. A Singapore, foreign or overseas-resident connection should therefore be disclosed rather than tested only against a monetary threshold.",
                            "Tell the bank the citizenship, residence and identity documents of the deceased and applicant. Ask about the death record, family or will evidence, estate-representative papers, Chinese translation, cross-border certification and any power of attorney. If something is missing, request one consolidated list for remote preparation.",
                        ],
                    ),
                    (
                        "4. Ask six questions in the first bank contact",
                        [
                            "Confirm the receiving branch, information available before release, who may apply for enquiry and withdrawal, the required form of overseas documents, whether an agent may submit them, and the type of account to which funds may be paid. Record the date, department and exact response.",
                            "If the family disputes the heirs, will or distribution, preserve the balance and transaction clues instead of allowing one relative to collect first and divide later. The bank's payment conditions do not decide every entitlement issue within the family.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling a Mainland estate"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate with and without a will"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Recording overseas property in the asset schedule"),
                    ("/articles/singapore/singapore-family-first-fact-sheet_en.html", "A first one-page estate fact sheet"),
                ],
                "cta": "Start with the bank, branch, account clue, deceased's identity and current representative papers, then decide whether the first request is an enquiry or release.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/macau/index.html": (
        "/articles/am/macau-name-mismatch-property-record.html",
        '<a href="/articles/am/macau-name-mismatch-property-record.html"><span class="v24-tag">姓名銜接</span><strong>澳門證件姓名對不上內地房產登記，先怎樣證明是同一人</strong><p>先分清文字寫法、真正改名和證件更換，再補最短的身份連接。</p></a>',
    ),
    "articles/macau/index_cn.html": (
        "/articles/am/macau-name-mismatch-property-record_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">姓名衔接</span><h3>澳门证件姓名对不上内地房产登记，先怎样证明是同一个人</h3><p>先分清文字写法、真正改名和证件更换，再补最短的身份连接。</p></div><a class="v25-pill-action" href="/articles/am/macau-name-mismatch-property-record_cn.html">阅读文章</a></article>',
    ),
    "articles/macau/index_en.html": (
        "/articles/am/macau-name-mismatch-property-record_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Identity link</span><h3>When a Macau name does not match a Mainland property record</h3><p>Separate spelling differences, actual changes and old document numbers.</p></div><a class="v25-pill-action" href="/articles/am/macau-name-mismatch-property-record_en.html">Read Article</a></article>',
    ),
    "articles/singapore/index.html": (
        "/articles/singapore/known-mainland-bank-account.html",
        '<a href="/articles/singapore/known-mainland-bank-account.html"><span class="v24-tag">銀行存款</span><strong>知道內地銀行帳戶，新加坡家屬先準備甚麼</strong><p>先整理帳戶線索、申請人身份和代表文件，再問銀行跨境要求。</p></a>',
    ),
    "articles/singapore/index_cn.html": (
        "/articles/singapore/known-mainland-bank-account_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">银行存款</span><h3>知道内地银行账户，新加坡家属先准备什么</h3><p>先整理账户线索、申请人身份和代表文件，再向银行确认跨境要求。</p></div><a class="v25-pill-action" href="/articles/singapore/known-mainland-bank-account_cn.html">阅读文章</a></article>',
    ),
    "articles/singapore/index_en.html": (
        "/articles/singapore/known-mainland-bank-account_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Bank funds</span><h3>A Singapore family knows the Mainland bank account: what comes first?</h3><p>Organise the account clue, applicant and representative papers before contacting the bank.</p></div><a class="v25-pill-action" href="/articles/singapore/known-mainland-bank-account_en.html">Read Article</a></article>',
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
