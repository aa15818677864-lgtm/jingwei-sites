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
        "slug": "macau-no-will-mainland-property",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門家屬與無遺囑繼承",
                "title": "沒有遺囑，澳門家屬處理內地房產從哪一步開始",
                "description": "澳門家屬確認沒有遺囑後，先核對全部可能繼承人、親屬文件和內地房產登記，再選擇辦理路徑。",
                "lead": "家人說「沒有遺囑」，只是起點。先查遺囑、畫家庭關係，再找房產登記；三件事分開做，才不會一開始便補錯文件。",
                "key_title": "先整理三張表",
                "keys": [
                    "遺囑查詢結果、死亡文件和逝者身份資料",
                    "配偶、子女、父母及已故家人的完整關係圖",
                    "內地房產城市、登記姓名、共有和按揭情況",
                ],
                "answer_title": "先做的不是直接轉名",
                "answer": [
                    "沒有遺囑，不代表只要配偶或一名子女簽字便可處理房產。第一步是確認誰可能參與繼承，哪些人的關係和死亡情況已有文件，哪些仍然只有家人口述。",
                    "澳門的繼承人資格文件和內地房產登記是兩個環節。前者用來整理繼承人身份，後者仍會查看房產登記、逝者權益、其他繼承人和當地收件要求。先把兩套資料分開，較容易知道真正缺哪一段。",
                ],
                "sections": [
                    (
                        "一、先確認真的沒有可處理的遺囑",
                        [
                            "不要只問家人有沒有看過遺囑。先保留逝者身份證明和死亡文件，向澳門公共公證署查詢有否繕立遺囑的紀錄，同時查看家中保險箱、文件袋、律師往來和曾經保管文件的人。公共紀錄查詢和尋找私人保管的原件，不能互相代替。",
                            "如找到不同日期的遺囑、補充文件或未確認版本，先按日期和保管來源列出，不要自行挑一份使用。公共公證署沒有查到紀錄，也只代表該次查詢結果；仍要記下日期、查詢範圍和家中搜尋情況。",
                        ],
                    ),
                    (
                        "二、畫出完整家庭關係，不要只寫眼前家人",
                        [
                            "從逝者開始，列出配偶、所有子女和父母，再補上收養、以前的婚姻和已故家人的情況。有人先於逝者離世，或在逝者離世後、房產尚未處理前再離世，都可能令文件關係增加一層。",
                            "每個名字旁邊標記已有的出生、婚姻、收養、死亡和身份文件。資料只有家人口述的，另標為待核對；不要為了讓關係圖看起來完整而猜出生年份、婚姻狀況或是否放棄繼承。",
                        ],
                    ),
                    (
                        "三、把澳門繼承人文件和內地房產文件分開",
                        [
                            "澳門現行公證服務在繼承人均成年、彼此沒有繼承權爭議並能交齊所需文件時，可以由其中一名繼承人先申請確認繼承人資格。家中有未成年人、無行為能力人，或關鍵關係文件仍找不到時，可能需要改走司法程序。",
                            "這份澳門文件不等於內地房產已經轉名。房產所在地仍可能核對死亡、親屬關係、房屋登記、共有份額、是否有其他繼承人，以及所有相關人士是否同意所提交的資料。",
                        ],
                    ),
                    (
                        "四、先問房產城市，再決定辦哪一套文件",
                        [
                            "先取得房產登記查詢或至少確認城市、地址、登記姓名和證件號碼，再向當地接收方說明逝者在澳門離世、沒有已知遺囑和家屬分布。請對方分開列出身份、關係、房產和不能到場時的要求。",
                            "如家屬對誰是繼承人、房產是否屬於逝者或分配方式有異議，先保存資料，不要為了趕進度讓一人代替全家作決定。沒有爭議時可以集中補文件；有爭議時則要先處理爭議本身。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-will-mainland-property.html", "有遺囑時先核對哪三件事"),
                    ("/articles/am/macau-kinship-certificate-scope.html", "親屬關係文件能證明甚麼"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "先分清澳門和內地兩套文件"),
                ],
                "cta": "說明逝者、配偶、子女、父母和內地房產城市，先看缺的是遺囑查詢、關係文件還是房產資料。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门家属与无遗嘱继承",
                "title": "没有遗嘱，澳门家属处理内地房产从哪一步开始",
                "description": "澳门家属确认没有遗嘱后，先核对全部可能继承人、亲属文件和内地房产登记，再选择办理路径。",
                "lead": "家人说“没有遗嘱”，只是起点。先查遗嘱、画家庭关系，再找房产登记；三件事分开做，才不会一开始就补错文件。",
                "key_title": "先整理三张表",
                "keys": [
                    "遗嘱查询结果、死亡文件和逝者身份资料",
                    "配偶、子女、父母及已经去世家人的完整关系图",
                    "内地房产城市、登记姓名、共有和抵押情况",
                ],
                "answer_title": "先做的不是直接过户",
                "answer": [
                    "没有遗嘱，不代表只要配偶或一名子女签字就能处理房产。第一步是确认谁可能参与继承，哪些人的关系和死亡情况已经有文件，哪些仍然只有家人口述。",
                    "澳门的继承人资格文件和内地房产登记是两个环节。前者用于整理继承人身份，后者仍会核对房产登记、逝者权益、其他继承人和当地材料要求。先把两套资料分开，更容易知道真正缺哪一段。",
                ],
                "sections": [
                    (
                        "一、先确认真的没有可以处理的遗嘱",
                        [
                            "不要只问家人有没有看过遗嘱。先保留逝者身份证明和死亡文件，向澳门公共公证署查询是否有订立遗嘱的记录，同时查看家中保险箱、文件袋、律师往来和曾经保管文件的人。公共记录查询和寻找私人保管的原件，不能互相代替。",
                            "如果找到不同日期的遗嘱、补充文件或未经确认的版本，先按日期和保管来源列出，不要自行选择一份使用。公共公证署没有查到记录，也只代表这次查询结果；仍要记下日期、查询范围和家中寻找情况。",
                        ],
                    ),
                    (
                        "二、画出完整家庭关系，不要只写眼前家人",
                        [
                            "从逝者开始，列出配偶、所有子女和父母，再补上收养、以前的婚姻和已经去世家人的情况。有人先于逝者去世，或者在逝者去世后、房产尚未处理前又去世，都可能让文件关系增加一层。",
                            "每个姓名旁边标明已有的出生、婚姻、收养、死亡和身份文件。只有家人口述的内容，另外标为待核对；不要为了让关系图看起来完整而猜出生年份、婚姻状况或是否放弃继承。",
                        ],
                    ),
                    (
                        "三、把澳门继承人文件和内地房产文件分开",
                        [
                            "澳门现行公证服务在继承人都已经成年、彼此没有继承权争议并能交齐所需文件时，可以由其中一名继承人先申请确认继承人资格。家中有未成年人、无行为能力人，或者关键关系文件仍找不到时，可能需要改走司法程序。",
                            "这份澳门文件不等于内地房产已经过户。房产所在地仍可能核对死亡、亲属关系、房屋登记、共有份额、是否有其他继承人，以及所有相关人员是否认可提交的资料。",
                        ],
                    ),
                    (
                        "四、先问房产城市，再决定办理哪一套文件",
                        [
                            "先取得房产登记查询结果，或者至少确认城市、地址、登记姓名和证件号码，再向当地接收方说明逝者在澳门去世、没有已知遗嘱和家属分布。请对方分别列出身份、关系、房产和不能到场时的要求。",
                            "如果家属对谁是继承人、房产是否属于逝者或分配方式有争议，先保存资料，不要为了赶进度让一个人代替全家作决定。没有争议时可以集中补文件；有争议时要先处理争议本身。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-will-mainland-property_cn.html", "有遗嘱时先核对哪三件事"),
                    ("/articles/am/macau-kinship-certificate-scope_cn.html", "亲属关系文件能证明什么"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "先分清澳门和内地两套文件"),
                ],
                "cta": "说明逝者、配偶、子女、父母和内地房产城市，先看缺的是遗嘱查询、关系文件还是房产资料。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / A Macau family and an estate without a will",
                "title": "No Will and Mainland Property: Macau Family First Steps",
                "description": "A practical starting order for a Macau family dealing with Mainland property where no will has been found.",
                "lead": "A family statement that there is no will is only a starting point. Check for a will, draw the family map and identify the property record as three separate tasks before ordering documents.",
                "key_title": "Build three short records",
                "keys": [
                    "The will-search result, death record and the deceased's identity details",
                    "A full family map covering spouse, children, parents and earlier deaths",
                    "The property city, registered owner, co-ownership and mortgage clues",
                ],
                "answer_title": "Do not begin with a transfer application",
                "answer": [
                    "No will does not mean that a spouse or one child can sign for the whole family. Start by identifying everyone who may need to be considered, then mark which relationships and deaths are already supported by records and which remain family recollections.",
                    "A Macau record identifying heirs and a Mainland property transfer serve different purposes. The receiving side may still examine the title, the deceased's share, the wider family and the local procedure. Keeping those two files separate makes the real gap easier to see.",
                ],
                "sections": [
                    (
                        "1. Confirm that the will search is complete",
                        [
                            "Do not rely only on whether a relative has seen a will. Preserve the deceased's identity and death records, ask the Macau public notarial offices whether they hold a record of a will, and review any safe, document folder, lawyer correspondence or person who may have held an original. A public-record enquiry does not replace the search for a privately held document.",
                            "If several dated documents, amendments or unconfirmed versions appear, list their dates and sources without choosing one yourself. A negative public-record result proves only what that enquiry covered, so record its date and scope alongside the family's own search.",
                        ],
                    ),
                    (
                        "2. Map the whole family, including earlier deaths",
                        [
                            "Start with the deceased and add marriages, spouse, every child, parents, adoptions, earlier marriages and relatives who have died. A person who died before the deceased, or after the death but before the property was dealt with, may add another documentary link.",
                            "Mark the birth, marriage, adoption, death and identity record held for each person. Label family recollections as unverified. Do not guess a birth year, marital status or renunciation merely to complete the diagram.",
                        ],
                    ),
                    (
                        "3. Keep the Macau heir file separate from the property file",
                        [
                            "The current Macau notarial service may be available where the heirs are adults, there is no dispute over heirship and the required records can be supplied. A minor, a person without capacity or a material documentary gap may require a judicial route instead.",
                            "The resulting Macau document does not itself change the Mainland title. The property recipient may still examine the death, family links, registered ownership, co-owned share, other heirs and whether the people concerned accept the submitted account.",
                        ],
                    ),
                    (
                        "4. Ask the property city before ordering the full file",
                        [
                            "Obtain a registry search if possible, or at least confirm the city, address, registered name and identity number. Tell the receiving side that the deceased died in Macau, no will is known and the family is dispersed. Ask for separate lists covering identity, relationships, property and remote participation.",
                            "If the family disputes the heirs, the deceased's ownership or the proposed distribution, preserve the records instead of allowing one person to decide for everyone. An agreed file can move into document preparation; a disputed file needs the disagreement identified first.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"),
                    ("/articles/am/macau-will-mainland-property_en.html", "When a will mentions Mainland property"),
                    ("/articles/am/macau-kinship-certificate-scope_en.html", "What Macau family records establish"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Separate the Macau and Mainland property files"),
                ],
                "cta": "Start with the deceased, spouse, children, parents and the property city, then identify whether the gap is the will search, family evidence or title record.",
            },
        },
    },
    {
        "slug": "us-will-mainland-property",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國遺囑與內地房產",
                "title": "美國遺囑寫到內地房產，為甚麼不能直接辦轉名",
                "description": "美國遺囑提到內地房產時，先分清遺囑內容、法院任命的代表權限和內地房產登記要求。",
                "lead": "遺囑寫了房產和受益人，仍不代表房產登記已經改變，也不代表遺囑中提名的人已取得對外辦事權限。",
                "key_title": "先核對三組資料",
                "keys": [
                    "遺囑訂立的州、原件、補充遺囑和有否啟動遺產程序",
                    "法院是否已任命遺產代表，以及現有哪份授權文件",
                    "內地房產城市、登記姓名、共有和婚姻資料",
                ],
                "answer_title": "遺囑只是其中一層",
                "answer": [
                    "美國遺囑可以表達分配意願，也可提名負責處理遺產的人；但是否需要法院程序、走哪種程序和誰有權辦事，要看相關州份及遺產情況。處理內地房產前，要先分清手上的只是遺囑、尚未啟動程序，還是已有法院接納遺囑並確認代表權限的文件。",
                    "內地接收方還會看房產是否確實登記在逝者名下、逝者擁有多少份額，以及遺囑、親屬和其他繼承資料如何互相銜接。不要只把遺囑翻成中文便直接提交。",
                ],
                "sections": [
                    (
                        "一、先找原件、州和最後版本",
                        [
                            "記下逝者最後居住的州和縣、遺囑日期、簽署頁、見證資料、保管人，以及是否有補充遺囑或後來版本。不要在原件上寫字；原件已有釘裝或封套的，也不要自行拆開或重新裝訂。",
                            "房產地址寫得不完整、使用舊中文姓名，或遺囑只寫「海外資產」時，先如實標記，不要自行把內地房產補進遺囑內容。遺囑是否涵蓋該資產，要與完整文件和當地程序一起判斷。",
                        ],
                    ),
                    (
                        "二、分清受益人和有權辦事的人",
                        [
                            "遺囑中的受益人是獲分配財產的人，遺囑提名的執行人則負責處理遺產；兩者可能是同一人，也可能不是。更重要的是，被遺囑提名並不必然等於已能代表遺產向外辦事。",
                            "向家屬或美國律師確認該州和這宗遺產是否需要法院程序；如已提出案件，再核對遺囑是否獲法院接納，以及是否已有法院裁定、Letters Testamentary 或其他代表權限文件。把申請文件、法院裁定和正式授權分開標記。",
                        ],
                    ),
                    (
                        "三、再核對內地房產到底有多少屬於逝者",
                        [
                            "取得房產登記查詢，核對權利人姓名、證件號碼、購買時間、共有方式、按揭和限制。房產只登記一人，也仍要查看取得時間、婚姻和出資資料；遺囑不能分配本來不屬於逝者的份額。",
                            "把遺囑中的房產描述與登記資料逐項對照。地址變更、門牌調整、中英文姓名不同或只寫舊房產證號時，先補一張對照表，不要直接改動翻譯來迎合現有登記。",
                        ],
                    ),
                    (
                        "四、由接收城市確認美國文件版本",
                        [
                            "把遺囑、遺產程序狀態、代表文件和房產查詢的清單先發給房產所在地，問明需要原件、正式副本、附加證明（Apostille）、中文翻譯或補充關係資料中的哪些項目。不同州和不同簽發機關的文件，辦理來源並不相同。",
                            "如有多份遺囑、有人反對遺囑、法院尚未任命代表，或家屬對房產份額有爭議，先停止把文件當成已確定結論。把爭議點寫清楚，再決定由美國程序還是內地房產環節先處理。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/letters-testamentary-or-administration.html", "兩類法院權限文件分別說明甚麼"),
                    ("/articles/us/state-or-federal-apostille.html", "州文件和聯邦文件怎樣分路徑"),
                    ("/articles/us/sole-registered-mainland-property.html", "房產只登記一人先查哪六件事"),
                ],
                "cta": "說明遺囑訂立州、遺產程序狀態、現有權限文件和房產城市，先找出卡在美國程序還是內地登記。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国遗嘱与内地房产",
                "title": "美国遗嘱写到内地房产，为什么不能直接办理过户",
                "description": "美国遗嘱提到内地房产时，先分清遗嘱内容、法院任命的代表权限和内地房产登记要求。",
                "lead": "遗嘱写了房产和受益人，仍不代表房产登记已经改变，也不代表遗嘱中提名的人已经取得对外办理事务的权限。",
                "key_title": "先核对三组资料",
                "keys": [
                    "遗嘱订立的州、原件、补充遗嘱和是否启动遗产程序",
                    "法院是否已经任命遗产代表，以及现有哪份授权文件",
                    "内地房产城市、登记姓名、共有和婚姻资料",
                ],
                "answer_title": "遗嘱只是其中一层",
                "answer": [
                    "美国遗嘱可以表达分配意愿，也可以提名负责处理遗产的人；但是否需要法院程序、走哪种程序和谁有权办理事务，要看相关州和遗产情况。处理内地房产前，要先分清手上只有遗嘱、尚未启动程序，还是已有法院接纳遗嘱并确认代表权限的文件。",
                    "内地接收方还会核对房产是否确实登记在逝者名下、逝者拥有多少份额，以及遗嘱、亲属和其他继承资料怎样衔接。不要只把遗嘱翻成中文就直接提交。",
                ],
                "sections": [
                    (
                        "一、先找原件、州和最后版本",
                        [
                            "记下逝者最后居住州和县、遗嘱日期、签字页、见证资料、保管人，以及是否有补充遗嘱或后来版本。不要拆除装订、写字、重新装订，也不要只扫描涉及房产的那一页。",
                            "房产地址写得不完整、使用旧中文姓名，或者遗嘱只写“海外资产”时，先如实标记，不要自行把内地房产补进遗嘱内容。遗嘱是否覆盖该资产，要结合完整文件和当地程序判断。",
                        ],
                    ),
                    (
                        "二、分清受益人和有权办理事务的人",
                        [
                            "遗嘱中的受益人是得到财产分配的人，遗嘱提名的执行人负责处理遗产；两者可能是同一个人，也可能不是。更重要的是，被遗嘱提名并不一定代表已经可以对外代表遗产。",
                            "向家属或美国律师确认该州和这宗遗产是否需要法院程序；如果已经提交案件，再核对遗嘱是否得到法院接纳，以及是否已有法院裁定、Letters Testamentary 或其他代表权限文件。把申请文件、法院裁定和正式授权分开标记。",
                        ],
                    ),
                    (
                        "三、再核对内地房产究竟有多少属于逝者",
                        [
                            "取得房产登记查询结果，核对权利人姓名、证件号码、购房时间、共有方式、抵押和限制。房产只登记一个人，也仍要查看取得时间、婚姻和出资资料；遗嘱不能分配原本不属于逝者的份额。",
                            "把遗嘱中的房产描述与登记资料逐项对照。地址变更、门牌调整、中英文姓名不同或只写旧房产证号时，先补一张对照表，不要直接改动翻译来迎合现有登记。",
                        ],
                    ),
                    (
                        "四、由接收城市确认美国文件版本",
                        [
                            "把遗嘱、遗产程序状态、代表文件和房产查询清单先发给房产所在地，问清需要原件、正式副本、附加证明（Apostille）、中文翻译或补充关系资料中的哪些内容。不同州和不同签发机构的文件，办理来源并不相同。",
                            "如果有多份遗嘱、有人反对遗嘱、法院尚未任命代表，或者家属对房产份额有争议，先不要把文件当成已经确定的结论。把争议点写清楚，再判断先处理美国程序还是内地房产环节。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/letters-testamentary-or-administration_cn.html", "两类法院权限文件分别说明什么"),
                    ("/articles/us/state-or-federal-apostille_cn.html", "州文件和联邦文件怎样分路径"),
                    ("/articles/us/sole-registered-mainland-property_cn.html", "房产只登记一人先查哪六件事"),
                ],
                "cta": "说明遗嘱订立州、遗产程序状态、现有权限文件和房产城市，先找出问题在美国程序还是内地登记。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / A U.S. will and Mainland property",
                "title": "A U.S. Will Names Mainland Property: What Comes Next?",
                "description": "Separate the will, the court-appointed representative and the Mainland title review before using U.S. estate papers for a property transfer.",
                "lead": "Naming a property and beneficiary in a will does not change the property record. It also does not necessarily give the nominated executor authority to act for the estate.",
                "key_title": "Check three parts of the file",
                "keys": [
                    "The state, original will, codicils and whether an estate proceeding has begun",
                    "Whether a court appointed a representative and what authority record was issued",
                    "The Mainland city, registered owner, co-ownership and marriage records",
                ],
                "answer_title": "The will is only one layer",
                "answer": [
                    "A U.S. will can state the intended distribution and nominate an executor. Whether a court proceeding is required, which process applies and who may act depend on the relevant state and estate. Identify whether the family has only the will, no proceeding has begun, or a court has issued current proof of a representative's authority.",
                    "The Mainland recipient will separately examine the registered owner, the share that actually belonged to the deceased and the connection between the will, family and other estate records. Translating the will alone does not answer those questions.",
                ],
                "sections": [
                    (
                        "1. Preserve the original and identify the final version",
                        [
                            "Record the deceased's last state and county of residence, the will date, signature and witness pages, custodian and any codicil or later version. Do not remove staples, write on the original, reassemble it or scan only the page that mentions property.",
                            "If the address is incomplete, an earlier Chinese name is used or the will says only overseas assets, record that wording as it stands. Do not add the Mainland property to the document. Whether it is covered must be considered with the complete will and the relevant state process.",
                        ],
                    ),
                    (
                        "2. Separate the beneficiary from the person authorised to act",
                        [
                            "A beneficiary receives something under the will; an executor is nominated to administer the estate. They may be the same person, but a nomination in the will does not necessarily establish present authority to deal with third parties.",
                            "First confirm whether this state and estate call for a court proceeding. If a case has been filed, check whether the will has been admitted and a decree, Letters Testamentary or another state-specific authority record has been issued. Label a petition, court order and current letters separately instead of calling all of them probate papers.",
                        ],
                    ),
                    (
                        "3. Check how much of the Mainland property belonged to the deceased",
                        [
                            "Obtain a registry search and compare the owner name, identity number, acquisition date, co-ownership, mortgage and restrictions. A sole name on the record may still call for marriage and funding evidence. A will cannot distribute a share the deceased did not own.",
                            "Compare the will's property description with the registry item by item. Where an address changed, numbering was revised, names differ or an old certificate number is used, prepare a comparison sheet rather than changing the translation to match the current record.",
                        ],
                    ),
                    (
                        "4. Ask the receiving city which U.S. records it needs",
                        [
                            "Send a list of the will, estate-proceeding status, representative papers and property search to the receiving side. Ask whether it needs an original, certified copy, apostille, Chinese translation or additional family evidence. The route follows the issuing state and authority, not a single nationwide document office.",
                            "If several wills exist, probate is contested, no representative has been appointed or the property share is disputed, do not present the file as settled. State the dispute clearly, then decide whether the U.S. proceeding or the Mainland property issue has to move first.",
                        ],
                    ),
                ],
                "related_title": "Continue with the U.S. topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling a Mainland estate"),
                    ("/articles/us/letters-testamentary-or-administration_en.html", "What court-issued letters establish"),
                    ("/articles/us/state-or-federal-apostille_en.html", "State and federal apostille routes"),
                    ("/articles/us/sole-registered-mainland-property_en.html", "Six checks for a solely registered home"),
                ],
                "cta": "Start with the will state, estate-proceeding status, current authority record and property city, then identify which side of the file is holding up the transfer.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/macau/index.html": (
        "/articles/am/macau-no-will-mainland-property.html",
        '<a href="/articles/am/macau-no-will-mainland-property.html"><span class="v24-tag">無遺囑</span><strong>沒有遺囑，澳門家屬處理內地房產從哪一步開始</strong><p>先確認遺囑查詢、完整家庭關係和房產登記，再選辦理路徑。</p></a>',
    ),
    "articles/macau/index_cn.html": (
        "/articles/am/macau-no-will-mainland-property_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">无遗嘱</span><h3>没有遗嘱，澳门家属处理内地房产从哪一步开始</h3><p>先确认遗嘱查询、完整家庭关系和房产登记，再选择办理路径。</p></div><a class="v25-pill-action" href="/articles/am/macau-no-will-mainland-property_cn.html">阅读文章</a></article>',
    ),
    "articles/macau/index_en.html": (
        "/articles/am/macau-no-will-mainland-property_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">No will</span><h3>No will and Mainland property: Macau family first steps</h3><p>Confirm the will search, full family map and property record before choosing a route.</p></div><a class="v25-pill-action" href="/articles/am/macau-no-will-mainland-property_en.html">Read Article</a></article>',
    ),
    "articles/united-states/index.html": (
        "/articles/us/us-will-mainland-property.html",
        '<a href="/articles/us/us-will-mainland-property.html"><span class="v24-tag">美國遺囑</span><strong>美國遺囑寫到內地房產，為甚麼不能直接辦轉名</strong><p>分清遺囑內容、法院任命的代表和內地房產登記。</p></a>',
    ),
    "articles/united-states/index_cn.html": (
        "/articles/us/us-will-mainland-property_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">美国遗嘱</span><h3>美国遗嘱写到内地房产，为什么不能直接办理过户</h3><p>分清遗嘱内容、法院任命的代表和内地房产登记。</p></div><a class="v25-pill-action" href="/articles/us/us-will-mainland-property_cn.html">阅读文章</a></article>',
    ),
    "articles/united-states/index_en.html": (
        "/articles/us/us-will-mainland-property_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">U.S. will</span><h3>A U.S. will names Mainland property: what comes next?</h3><p>Separate the will, court-appointed representative and property record.</p></div><a class="v25-pill-action" href="/articles/us/us-will-mainland-property_en.html">Read Article</a></article>',
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
    for base in ("/articles/macau/", "/articles/united-states/"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, SITE + base + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
