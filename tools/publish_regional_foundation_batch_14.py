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
        "slug": "us-death-certificate-for-mainland",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國文件與內地繼承",
                "title": "美國死亡證明交到內地前，先看州、版本和姓名",
                "description": "美國死亡證明用於內地繼承或資產查詢前，先核對簽發來源、正式版本、姓名差異和接收用途。",
                "lead": "先不要拿着一張掃描件便安排翻譯。死亡證明由哪裏簽發、手上是哪種副本，以及姓名能否和內地資料對上，會直接影響下一步。",
                "key_title": "先回答三個問題",
                "keys": [
                    "死亡發生在哪裏，文件由州、地方還是領事機構簽發",
                    "手上是普通影印件，還是由登記部門發出的正式副本",
                    "英文姓名、日期和地點能否和內地資產資料連接",
                ],
                "answer_title": "最實用的答案",
                "answer": [
                    "美國沒有一個聯邦部門統一簽發所有死亡證明。一般先按死亡發生的州或地方找出生及死亡記錄部門；若美國公民在境外離世，家屬手上的文件還可能屬於另一類領事死亡記錄。先分清來源，才知道應申領哪種正式副本和向哪裏查詢後續證明。",
                    "死亡證明主要說明死亡事實，不會單獨證明誰是繼承人、誰有權代表遺產，也不會直接把內地房產轉名。家屬仍要另行整理身份、親屬、遺囑或代表文件，以及具體資產資料。",
                ],
                "sections": [
                    (
                        "一、先找簽發來源，不要只看死亡地點",
                        [
                            "先記下死亡城市、縣和州，再看文件上的簽發機構、簽署人職銜、印章和簽發日期。死亡發生地、逝者長期居住的州和美國遺產程序所在州可以不同；死亡證明回答的首先是死亡記錄在哪裏，而不是全部遺產問題。",
                            "如果逝者是在美國境外離世，先確認家屬拿到的是當地死亡文件，還是美國領事機構製作的死亡記錄。這兩類文件的申領和證明路徑不同，不能都交給逝者住所州處理。",
                        ],
                    ),
                    (
                        "二、確認是哪種副本，再談附加證明",
                        [
                            "手機照片、普通影印件和由登記部門發出的正式副本用途不同。檢查有沒有完整頁面、背頁、修訂註記、簽發日期、簽名和印章；若資料曾更正，也要保留更正前後的連接記錄。",
                            "州或地方簽發的文件通常按簽發州的現行要求處理；領事或其他聯邦來源的文件另有路徑。不要先替原件加做不必要的公證，也不要把普通列印件當成正式副本。先讓簽發方和內地接收方分別確認。",
                        ],
                    ),
                    (
                        "三、用一張表對照姓名、日期和地點",
                        [
                            "左邊抄錄死亡證明上的全名、中間名、曾用名、出生和死亡日期、死亡地點；右邊列內地房產證、銀行資料、舊身份證明和護照上的寫法。每一個不同拼法旁邊都寫明來源，不要為了看起來一致而自行改名或補字。",
                            "常見差異包括婚後姓氏、中間名縮寫、拼音順序、舊護照號碼，以及中文姓名只出現在內地資料。翻譯可以轉換文字，卻不能代替證明兩種姓名屬於同一人的材料。",
                        ],
                    ),
                    (
                        "四、分清死亡證明能證明甚麼",
                        [
                            "死亡證明可以作為死亡事實的基礎材料，但通常不會列出完整繼承人，也不會確認某套內地房屋屬於遺產。配偶、父母、子女、先於逝者離世的家屬，以及遺囑或遺產代表，仍要用其他資料核對。",
                            "內地接收方還可能要看房屋城市、登記人、共有份額、抵押或限制。即使死亡證明已辦好附加證明，也只解決文件來源的真實性鏈條，不等於整套繼承材料已經齊全。",
                        ],
                    ),
                    (
                        "五、最後才安排翻譯和寄送",
                        [
                            "把簽發來源、副本類型、姓名差異、內地資產城市和準備辦理的事情放在一頁。先問接收方需要整份還是特定版本、是否要附加證明、翻譯由誰完成，以及原件怎樣安全提交。",
                            "如果死亡記錄、遺囑、遺產代表文件和內地登記姓名互相對不上，先停在掃描件階段補連接材料。未確認用途前，不要把唯一原件寄出，也不要一次把所有美國文件全部翻譯。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/issuing-state-matters.html", "為甚麼簽發州會改變文件路徑"),
                    ("/articles/us/state-or-federal-apostille.html", "州文件和聯邦文件怎樣分開處理"),
                    ("/articles/us/us-document-translation-and-name.html", "英文文件的姓名和日期怎樣核對"),
                ],
                "cta": "先說明死亡地點、簽發機構、副本類型、姓名差異和內地資產城市，再判斷哪份文件應先處理。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国文件与内地继承",
                "title": "美国死亡证明交到内地前，先看州、版本和姓名",
                "description": "美国死亡证明用于内地继承或资产查询前，先核对签发来源、正式版本、姓名差异和接收用途。",
                "lead": "先不要拿着一张扫描件就安排翻译。死亡证明由哪里签发、手上是哪种副本，以及姓名能否和内地资料对上，会直接影响下一步。",
                "key_title": "先回答三个问题",
                "keys": [
                    "死亡发生在哪里，文件由州、地方还是领事机构签发",
                    "手上是普通复印件，还是可供正式使用的认证副本",
                    "英文姓名、日期和地点能否和内地资产资料连接",
                ],
                "answer_title": "最实用的答案",
                "answer": [
                    "美国没有一个联邦部门统一签发所有死亡证明。一般先按死亡发生的州或地方找出生和死亡记录部门；如果美国公民在境外离世，家属手上的文件还可能属于另一类领事死亡记录。先分清来源，才知道应该申请哪种正式副本和向哪里查询后续证明。",
                    "死亡证明主要说明死亡事实，不会单独证明谁是继承人、谁有权代表遗产，也不会直接把内地房产转名。家属仍要另外整理身份、亲属、遗嘱或代表文件，以及具体资产资料。",
                ],
                "sections": [
                    (
                        "一、先找签发来源，不要只看死亡地点",
                        [
                            "先记下死亡城市、县和州，再看文件上的签发机构、签字人职务、印章和签发日期。死亡发生地、逝者长期居住的州和美国遗产程序所在州可能不同；死亡证明首先回答死亡记录在哪里，而不是全部遗产问题。",
                            "如果逝者在美国境外离世，先确认家属拿到的是当地死亡文件，还是美国领事机构制作的死亡记录。这两类文件的申请和证明路径不同，不能都交给逝者住所州处理。",
                        ],
                    ),
                    (
                        "二、确认是哪种副本，再谈附加证明",
                        [
                            "手机照片、普通复印件和由保管机构签发的认证副本用途不同。检查有没有完整页面、背页、更正说明、签发日期、签名和印章；如果资料改过，也要保留更正前后的连接记录。",
                            "州或地方签发的文件通常按签发州的现行要求处理；领事或其他联邦来源的文件另有路径。不要先替原件加做不必要的公证，也不要把普通打印件当成正式副本。先让签发方和内地接收方分别确认。",
                        ],
                    ),
                    (
                        "三、用一张表对照姓名、日期和地点",
                        [
                            "左边抄录死亡证明上的全名、中间名、曾用名、出生和死亡日期、死亡地点；右边列内地房产证、银行资料、旧身份证明和护照上的写法。每个不同拼法旁边都写明来源，不要为了看起来一致而自行改名或补字。",
                            "常见差异包括婚后姓氏、中间名缩写、拼音顺序、旧护照号码，以及中文姓名只出现在内地资料。翻译可以转换文字，却不能代替证明两种姓名属于同一人的材料。",
                        ],
                    ),
                    (
                        "四、分清死亡证明能证明什么",
                        [
                            "死亡证明可以作为死亡事实的基础材料，但通常不会列出完整继承人，也不会确认某套内地房屋属于遗产。配偶、父母、子女、先于逝者离世的家属，以及遗嘱或遗产代表，仍要用其他资料核对。",
                            "内地接收方还可能要看房屋城市、登记人、共有份额、抵押或限制。即使死亡证明已经办好附加证明，也只解决文件来源的真实性链条，不等于整套继承材料已经齐全。",
                        ],
                    ),
                    (
                        "五、最后再安排翻译和寄送",
                        [
                            "把签发来源、副本类型、姓名差异、内地资产城市和准备办理的事情放在一页。先问接收方需要整份还是特定版本、是否要附加证明、翻译由谁完成，以及原件怎样安全提交。",
                            "如果死亡记录、遗嘱、遗产代表文件和内地登记姓名互相对不上，先停在扫描件阶段补连接材料。没有确认用途前，不要把唯一原件寄出，也不要一次把所有美国文件全部翻译。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/issuing-state-matters_cn.html", "为什么签发州会改变文件路径"),
                    ("/articles/us/state-or-federal-apostille_cn.html", "州文件和联邦文件怎样分开处理"),
                    ("/articles/us/us-document-translation-and-name_cn.html", "英文文件的姓名和日期怎样核对"),
                ],
                "cta": "先说明死亡地点、签发机构、副本类型、姓名差异和内地资产城市，再判断哪份文件应该先处理。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. records for a Mainland estate",
                "title": "Using a U.S. Death Certificate for a Mainland Estate",
                "description": "Before using a U.S. death certificate for a Mainland China estate or asset enquiry, check its issuing source, certified copy and identity details.",
                "lead": "Do not begin with a scan and a translation order. The issuing source, the kind of copy and the match to the Mainland identity record determine the next step.",
                "key_title": "Answer three questions first",
                "keys": [
                    "Was the record issued by a state, locality or U.S. consular office?",
                    "Is this a photocopy or an official certified copy?",
                    "Do the name, dates and place match the Mainland records?",
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "There is no federal office that issues every U.S. death certificate. A death within the United States is generally recorded in the state or local system where it occurred. A U.S. citizen who died abroad may instead have a consular death record. Identify the source before ordering a copy or planning an apostille.",
                    "A death certificate establishes the death. It does not, by itself, identify every heir, appoint an estate representative or transfer a Mainland property. Keep the family, will, representative and asset evidence as separate parts of the file.",
                ],
                "sections": [
                    (
                        "1. Identify the issuing source, not only the place of death",
                        [
                            "Record the city, county and state of death, then read the issuing office, signatory, seal and issue date. The place of death, the deceased's domicile and the state handling the U.S. estate may be different. The certificate records the death; it does not answer every estate question.",
                            "If the person died outside the United States, determine whether the family has the local country's death record or a U.S. consular report. Those records are obtained and authenticated through different channels and should not both be sent to the domicile state.",
                        ],
                    ),
                    (
                        "2. Check the copy before planning an apostille",
                        [
                            "A phone image, an ordinary photocopy and a certified copy issued by the record custodian are not interchangeable. Check every page, reverse side, amendment, issue date, signature and seal. If the record was corrected, preserve the documents connecting the versions.",
                            "A state or local record normally follows the current process of its issuing state. A consular or other federal record follows a different route. Do not notarise the original without a clear reason or assume a printout is an official copy. Confirm the requirements with both the issuing and receiving sides.",
                        ],
                    ),
                    (
                        "3. Match the name, dates and place on one sheet",
                        [
                            "Copy the full name, middle name, former name, birth and death dates, and place of death into the left column. In the right column, list the names on the Mainland title, bank record, old identity paper and passports. Give a source for every variation rather than editing the names to look consistent.",
                            "Common issues include a married surname, middle initial, reversed order, older romanisation, an expired passport and a Chinese name that appears only in Mainland records. Translation converts text; it does not prove that two names belong to the same person.",
                        ],
                    ),
                    (
                        "4. Keep the certificate within its proper role",
                        [
                            "The certificate is evidence of death, but it will not usually list the complete family or establish that a particular Mainland asset belonged to the deceased. The spouse, parents, children, predeceased relatives, will and estate representative may all require separate records.",
                            "The Mainland recipient may also need the asset city, registered owner, ownership share and any mortgage or restriction. Even an apostilled certificate addresses the document's authentication chain, not the completeness of the inheritance file.",
                        ],
                    ),
                    (
                        "5. Arrange translation and delivery last",
                        [
                            "Put the issuing source, copy type, name differences, Mainland asset city and intended use on one page. Ask the recipient which version is required, whether an apostille is needed, who may translate it and how an original should be delivered safely.",
                            "Where the death record, will, representative paper and Mainland registered name do not align, work from scans while gathering the missing links. Do not send the only original or translate every U.S. document before the purpose is confirmed.",
                        ],
                    ),
                ],
                "related_title": "Continue with the United States topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling Mainland estates"),
                    ("/articles/us/issuing-state-matters_en.html", "Why the issuing state changes the document route"),
                    ("/articles/us/state-or-federal-apostille_en.html", "Separating state and federal apostille routes"),
                    ("/articles/us/us-document-translation-and-name_en.html", "Matching names and dates before translation"),
                ],
                "cta": "Start with the place of death, issuing office, copy type, name differences and Mainland asset city, then identify the first document to prepare.",
            },
        },
    },
    {
        "slug": "rented-mainland-property",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與內地出租房",
                "title": "內地遺產房仍在出租，新加坡家屬先整理哪五件事",
                "description": "內地遺產房仍有租客時，新加坡家屬先整理租約、租金、押金、聯絡權限和房屋狀況，不要急着換收款帳戶。",
                "lead": "房東離世不等於租約立即消失，也不表示任何一名家屬都能改收款帳戶。先把租約、錢和聯絡權限分開整理。",
                "key_title": "先留住三組資料",
                "keys": [
                    "完整租約、租客資料、租期、押金和交付清單",
                    "每期租金、收款帳戶、欠租、物業費和維修記錄",
                    "誰只是聯絡人，誰已有權代表遺產或處理房屋",
                ],
                "answer_title": "先說最重要的答案",
                "answer": [
                    "先不要通知租客把租金轉到某位家屬的私人帳戶，也不要因房東離世便要求立即搬走。內地房屋在租期內發生繼承或其他權利變動，一般不會僅因此令原租約失效；但誰可以收款、退押金、續租或解約，仍要看代表權限和具體文件。",
                    "最穩妥的起步方法，是做一張五欄表：房屋、租約、租金、押金與支出、聯絡與權限。先保存現狀，再把新加坡遺產文件和內地房屋資料交給兩邊接收方核對。",
                ],
                "sections": [
                    (
                        "一、先把租約和房屋對上",
                        [
                            "找出完整租約、續租或補充協議、租客姓名和聯絡方式、租期、用途、月租、付款日、押金、家具清單、鑰匙和中介資料。再核對房屋城市、完整地址、登記姓名、共有情況和是否仍有按揭。",
                            "如果家屬只有聊天截圖或每月入帳記錄，先問租客和中介索取現有租約副本，但不要要求對方簽新的內容。先確認原約定是甚麼，才知道哪些只是口頭說法。",
                        ],
                    ),
                    (
                        "二、做一條租金時間線",
                        [
                            "分開記錄逝者離世前和離世後的租金：每期應付、實付、入帳日期、收款帳戶、欠租和收據。押金另列，不要把它當作最後一個月租金；物業費、維修、貸款和代管費也各自保存憑證。",
                            "新加坡一方的遺產代表通常要整理管理期間的收入帳目；是否還涉及當地申報，要再看收入來源和實際流向。內地房屋的租金怎樣收取和處理，也要按房屋所在地及具體權利狀態另行核對，所以第一步是保留完整流水，而不是先分給家屬。",
                        ],
                    ),
                    (
                        "三、指定聯絡人，不等於授權他收款",
                        [
                            "家屬可以先指定一人負責收集租約、維修通知和租客問題，但要在記錄上寫清楚：他只是資料聯絡人，還是已有遺囑、法院文件、正式委託或內地程序支持其代表權限。兩種身份不能混在一起。",
                            "向租客說明情況時，只提供必要事實和可核對的聯絡方式。不要讓多名家屬分別催租或作不同承諾；未確認權限前，也不要以個人名義收租、減租、退押金或簽署解除文件。",
                        ],
                    ),
                    (
                        "四、不要突然換帳戶或要求搬走",
                        [
                            "房屋權利因繼承而變動，通常不會單憑這一點終止租客在有效租約下的使用。租客仍要按約履行，家屬也要保存房屋維修、安全和交付記錄。若有漏水、停電等急事，可先安排必要處理並保存報價、付款和現場照片。",
                            "收款帳戶失效或無法繼續使用時，先向銀行、租客和房屋所在地的處理人員確認安全方案。不要要求租客把錢轉到來源不明的私人帳戶，也不要用換鎖、停水電或扣物品的方法自行解決爭議。",
                        ],
                    ),
                    (
                        "五、把新加坡文件和內地房屋接起來",
                        [
                            "新加坡的遺產授予文件和資產清單可以幫助說明誰在當地管理遺產，以及是否已把這套房屋列入資料。它們不會自行更改內地房屋登記，也不會自動令其中一名家屬成為新出租人。",
                            "把房屋、租約、租金時間線、押金與支出、代表文件放在一頁，分別詢問新加坡遺產處理人和房屋所在地的接收方。遇到欠租、長期佔用、多人爭租金或租約真偽爭議時，先保存證據，再決定協商或其他處理方式。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "資產清單怎樣記錄內地房產"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "遺產授予文件分別說明甚麼"),
                    ("/articles/singapore/mortgaged-mainland-property.html", "房屋仍有按揭時先取得哪些資料"),
                ],
                "cta": "先說明房屋地址、租期、租金帳戶、押金、欠租和現有代表文件，再判斷哪些事情可以先做。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与内地出租房",
                "title": "内地遗产房仍在出租，新加坡家属先整理哪五件事",
                "description": "内地遗产房仍有租客时，新加坡家属先整理租约、租金、押金、联系权限和房屋状况，不要急着更换收款账户。",
                "lead": "房东离世不等于租约立即消失，也不表示任何一名家属都能更换收款账户。先把租约、钱和联系权限分开整理。",
                "key_title": "先留住三组资料",
                "keys": [
                    "完整租约、租客资料、租期、押金和交付清单",
                    "每期租金、收款账户、欠租、物业费和维修记录",
                    "谁只是联系人，谁已经有权代表遗产或处理房屋",
                ],
                "answer_title": "先说最重要的答案",
                "answer": [
                    "先不要通知租客把租金转到某位家属的私人账户，也不要因为房东离世就要求立即搬走。内地房屋在租期内发生继承或其他权利变动，一般不会仅因此让原租约失效；但谁可以收款、退押金、续租或解约，仍要看代表权限和具体文件。",
                    "最稳妥的起步方法，是做一张五栏表：房屋、租约、租金、押金与支出、联系与权限。先保存现状，再把新加坡遗产文件和内地房屋资料交给两边接收方核对。",
                ],
                "sections": [
                    (
                        "一、先把租约和房屋对上",
                        [
                            "找出完整租约、续租或补充协议、租客姓名和联系方式、租期、用途、月租、付款日、押金、家具清单、钥匙和中介资料。再核对房屋城市、完整地址、登记姓名、共有情况和是否仍有按揭。",
                            "如果家属只有聊天截图或每月入账记录，先问租客和中介索取现有合同副本，但不要要求对方签新的内容。先确认原约定是什么，才知道哪些只是口头说法。",
                        ],
                    ),
                    (
                        "二、做一条租金时间线",
                        [
                            "分开记录逝者离世前和离世后的租金：每期应付、实付、入账日期、收款账户、欠租和收据。押金单独列出，不要把它当作最后一个月租金；物业费、维修、贷款和代管费也分别保存凭证。",
                            "新加坡一方的遗产代表通常要整理管理期间的收入账目；是否还涉及当地申报，要再看收入来源和实际流向。内地房屋的租金怎样收取和处理，也要按房屋所在地和具体权利状态另行核对，所以第一步是保留完整流水，而不是先分给家属。",
                        ],
                    ),
                    (
                        "三、指定联系人，不等于授权他收款",
                        [
                            "家属可以先指定一人负责收集合同、维修通知和租客问题，但要在记录上写清楚：他只是信息联系人，还是已经有遗嘱、法院文件、正式委托或内地程序支持其代表权限。两种身份不能混在一起。",
                            "向租客说明情况时，只提供必要事实和可核对的联系方式。不要让多名家属分别催租或作出不同承诺；没有确认权限前，也不要以个人名义收租、减租、退押金或签署解除文件。",
                        ],
                    ),
                    (
                        "四、不要突然换账户或要求搬走",
                        [
                            "房屋权利因为继承而变动，通常不会仅凭这一点终止租客在有效租约下的使用。租客仍要按约履行，家属也要保存房屋维修、安全和交付记录。如果出现漏水、停电等急事，可以先安排必要处理并保存报价、付款和现场照片。",
                            "收款账户失效或无法继续使用时，先向银行、租客和房屋所在地的处理人员确认安全方案。不要要求租客把钱转到来源不明的私人账户，也不要用换锁、停水电或扣留物品的方法自行解决争议。",
                        ],
                    ),
                    (
                        "五、把新加坡文件和内地房屋接起来",
                        [
                            "新加坡的遗产授予文件和资产清单可以帮助说明谁在当地管理遗产，以及是否已经把这套房屋列入资料。它们不会自行更改内地房屋登记，也不会自动让其中一名家属成为新出租人。",
                            "把房屋、租约、租金时间线、押金与支出、代表文件放在一页，分别询问新加坡遗产处理人和房屋所在地的接收方。遇到欠租、长期占用、多人争租金或租约真伪争议时，先保存证据，再决定协商或其他处理方式。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "资产清单怎样记录内地房产"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "遗产授予文件分别说明什么"),
                    ("/articles/singapore/mortgaged-mainland-property_cn.html", "房屋仍有按揭时先取得哪些资料"),
                ],
                "cta": "先说明房屋地址、租期、租金账户、押金、欠租和现有代表文件，再判断哪些事情可以先做。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore families and a rented Mainland home",
                "title": "A Mainland Estate Property Is Still Rented: Five First Checks",
                "description": "Five practical checks for a Singapore family when a Mainland estate property still has a tenant: lease, rent, deposit, authority and condition.",
                "lead": "The owner's death does not automatically end the lease or authorise any relative to redirect the rent. Preserve the arrangement before changing it.",
                "key_title": "Preserve three groups of records",
                "keys": [
                    "The complete lease, tenant, term, deposit and handover inventory",
                    "The rent ledger, receiving account, arrears, charges and repairs",
                    "The difference between a family contact and an authorised representative",
                ],
                "answer_title": "The important answer",
                "answer": [
                    "Do not immediately ask the tenant to pay a relative's personal account or leave the home. A change of ownership through an estate does not ordinarily end a valid Mainland lease by itself. Authority is still needed to receive rent, refund a deposit, renew or terminate the lease.",
                    "Begin with one five-column sheet: property, lease, rent, deposit and expenses, and authority to communicate. Preserve the current position, then connect the Singapore estate papers to the Mainland property with the relevant advisers or recipients.",
                ],
                "sections": [
                    (
                        "1. Match the lease to the property",
                        [
                            "Collect the complete lease, renewal or addendum, tenant details, term, use, monthly rent, payment date, deposit, inventory, keys and agent information. Match these against the Mainland city, full address, registered owner, co-ownership and any mortgage.",
                            "If the family has only chat messages or monthly credits, ask the tenant or agent for the existing contract. Do not ask for a new signature before establishing the original terms and identifying which arrangements were merely oral.",
                        ],
                    ),
                    (
                        "2. Build a rent timeline",
                        [
                            "Separate rent due and received before and after death. Record each due date, amount, receiving account, arrears and receipt. Keep the deposit separate from rent, and preserve evidence of management fees, repairs, loan payments and agent charges.",
                            "A Singapore estate representative normally keeps accounts of income received during the administration period. Any Singapore reporting question still depends on the source and movement of the income. Collection and treatment of the Mainland rent also need a location-specific review, so preserve the ledger rather than distributing the money immediately.",
                        ],
                    ),
                    (
                        "3. A family contact is not automatically authorised to collect",
                        [
                            "One relative can coordinate copies, repair notices and tenant questions. The record should state whether that person is only an information contact or holds a will, court grant, formal authority or a recognised Mainland role. Those are not the same position.",
                            "Give the tenant only the necessary facts and a verifiable contact. Avoid competing demands from several relatives. Until authority is clear, no relative should collect rent personally, reduce it, refund the deposit or sign a termination in their own name.",
                        ],
                    ),
                    (
                        "4. Do not suddenly redirect rent or demand possession",
                        [
                            "An inheritance-related ownership change does not ordinarily remove a tenant's rights under a valid lease. The tenant should continue to perform the agreement, while the family preserves repair, safety and handover records. Urgent leaks or electrical problems can be addressed with quotations, payment evidence and photographs.",
                            "If the original receiving account no longer works, confirm a secure arrangement with the bank, tenant and Mainland adviser. Do not use an unexplained personal account, change the locks, cut utilities or withhold belongings to force a result.",
                        ],
                    ),
                    (
                        "5. Connect the Singapore estate file to the Mainland home",
                        [
                            "A Singapore grant and Schedule of Assets may identify the estate representative and show whether the property was included. They do not update the Mainland title automatically or make one relative the new landlord without the necessary local steps.",
                            "Put the property, lease, rent timeline, deposit and expenses, and representative papers on one page. Ask the Singapore estate adviser and the Mainland receiving side separately. Where rent, occupation or the lease itself is disputed, preserve evidence before choosing negotiation or another route.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling Mainland estates"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Recording Mainland property in a Schedule of Assets"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "What a probate or administration grant establishes"),
                    ("/articles/singapore/mortgaged-mainland-property_en.html", "First checks for a mortgaged Mainland home"),
                ],
                "cta": "Start with the property, lease term, rent account, deposit, arrears and representative papers, then identify which decisions can safely be made.",
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
            "/articles/us/us-death-certificate-for-mainland.html",
            '<a href="/articles/us/us-death-certificate-for-mainland.html"><span class="v24-tag">死亡證明</span><strong>美國死亡證明交到內地前，先看州、版本和姓名</strong><p>先找簽發來源和正式副本，再核對中英文姓名與內地用途。</p></a>',
        ),
    ],
    "articles/united-states/index_cn.html": [
        (
            "/articles/us/us-death-certificate-for-mainland_cn.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">死亡证明</span><h3>美国死亡证明交到内地前，先看州、版本和姓名</h3><p>先找签发来源和正式副本，再核对中英文姓名与内地用途。</p></div><a class="v25-pill-action" href="/articles/us/us-death-certificate-for-mainland_cn.html">阅读文章</a></article>',
        ),
    ],
    "articles/united-states/index_en.html": [
        (
            "/articles/us/us-death-certificate-for-mainland_en.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Death certificate</span><h3>Using a U.S. death certificate for a Mainland estate</h3><p>Check the issuing source, certified copy and identity match before translation.</p></div><a class="v25-pill-action" href="/articles/us/us-death-certificate-for-mainland_en.html">Read Article</a></article>',
        ),
    ],
    "articles/singapore/index.html": [
        (
            "/articles/singapore/rented-mainland-property.html",
            '<a href="/articles/singapore/rented-mainland-property.html"><span class="v24-tag">出租房屋</span><strong>內地遺產房仍在出租，新加坡家屬先整理哪五件事</strong><p>先保留租約、租金和押金記錄，再分清聯絡人與代表權限。</p></a>',
        ),
    ],
    "articles/singapore/index_cn.html": [
        (
            "/articles/singapore/rented-mainland-property_cn.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">出租房屋</span><h3>内地遗产房仍在出租，新加坡家属先整理哪五件事</h3><p>先保留租约、租金和押金记录，再分清联系人与代表权限。</p></div><a class="v25-pill-action" href="/articles/singapore/rented-mainland-property_cn.html">阅读文章</a></article>',
        ),
    ],
    "articles/singapore/index_en.html": [
        (
            "/articles/singapore/rented-mainland-property_en.html",
            '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Rented property</span><h3>A Mainland estate property is still rented: five first checks</h3><p>Preserve the lease, rent and deposit before changing the arrangement.</p></div><a class="v25-pill-action" href="/articles/singapore/rented-mainland-property_en.html">Read Article</a></article>',
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
    for base in ("/articles/united-states/", "/articles/singapore/"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, SITE + base + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
