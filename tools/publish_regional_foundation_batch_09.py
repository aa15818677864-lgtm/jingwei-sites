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
        "slug": "macau-heir-qualification-deed",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_MO",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門與內地遺產",
                "title": "澳門確認繼承人資格公證書，甚麼時候值得先辦",
                "description": "澳門家屬處理內地遺產時，先判斷確認繼承人資格公證書是否回答了內地接收方真正需要的問題。",
                "lead": "不要因為家裏有遺產便立刻辦。先問清內地接收方要確認繼承人身份、代表權限，還是某項房產的登記資料。",
                "key_title": "先看三個判斷點",
                "keys": [
                    "家屬是否成年、無爭議且關係資料大致齊全",
                    "內地接收方是否需要一份正式的繼承人身份文件",
                    "公證書只處理它能證明的事項，不等於完成房產過戶",
                ],
                "answer_title": "先說最實用的答案",
                "answer": [
                    "如果所有可能繼承人都已成年、對繼承人範圍沒有爭議，出生、婚姻、死亡、遺囑等關係資料也大致齊全，而內地的實際接收方又明確需要一份正式文件說明誰具有繼承人身份，這份公證書值得較早考慮。它可以把分散的家屬關係整理成一個較清楚的證明入口。",
                    "但它不是內地房產證，也不會自動證明逝者名下有哪一套房、每人最後取得多少份額，或任何家屬都有權代其他人簽署。若房產城市、登記人或接收要求仍不清楚，先查清這些事，再決定是否辦理，通常更省時間。",
                ],
                "sections": [
                    (
                        "先問內地接收方：它要證明的是誰，還是房產",
                        [
                            "同一句「要繼承文件」，可能指完全不同的問題。房產登記窗口可能在核對繼承人範圍，銀行可能在核對領取人和授權，受託律師則可能先要確認誰能提供指示。先把接收單位、資產城市、登記姓名和用途寫在一頁紙上，再問現有澳門文件分別能回答甚麼。",
                            "如果對方真正缺的是內地房屋的準確地址、登記份額、抵押或共有情況，先辦繼承人資格公證書並不會補上這個缺口。若對方要的是一份清楚列明繼承人的正式文件，才進一步核對澳門申請條件和所需記錄。",
                        ],
                    ),
                    (
                        "這四種情況，值得較早考慮辦理",
                        [
                            "第一，家屬對配偶、子女、父母或其他可能涉及的人沒有不同說法。第二，所有可能繼承人均已成年並能處理自己的事務。第三，出生、婚姻、死亡、遺囑和已故家屬等記錄有清楚來源。第四，內地接收方已表示需要核對正式的繼承人身份。",
                            "在這種情況下，可先按家屬關係列出每一份記錄和原件保管人。澳門辦理時，所需資料會隨配偶、子女、父母、兄弟姊妹、遺囑、已故繼承人或代位情況而變化；不要拿另一個家庭的清單直接套用。",
                        ],
                    ),
                    (
                        "出現這些情況，不要把公證書當成捷徑",
                        [
                            "有未成年人、有人不能自行處理事務、家屬失聯、關係記錄缺失，或對遺囑和繼承人範圍已有爭議時，辦理路徑可能需要另外處理，不能假定補幾張聲明便會完成。逝者生前主要居住地不在澳門時，也可能要補充外地繼承規則或相關證明。",
                            "若有人要求一名家屬先簽全部文件，還要分開看他只是負責聯絡、是依法負責管理未分割遺產的人，還是真的取得其他人的有效授權。公證書確認繼承人，不等於把所有人的決定權集中到一個人手上。",
                        ],
                    ),
                    (
                        "申請前先做一張家屬和文件缺口表",
                        [
                            "第一欄列逝者、配偶、子女、父母和已故家屬；第二欄列每段關係的證明來源；第三欄寫原件、清晰影像或只有家人憶述；第四欄寫需要向哪個機構補取。若文件不是中文或葡文，另加一欄記錄語言和翻譯安排。",
                            "再把內地資產分開列：城市、地址、登記人、可能份額、現有證明和接收單位。這張表能讓家屬看出，現在缺的是澳門家屬證明，還是內地資產資料，不必把兩套問題混成一大疊文件。",
                        ],
                    ),
                    (
                        "辦好之後，仍要核對三件事",
                        [
                            "先核對姓名、日期、親屬關係和任何已故家屬是否與內地資料一致；再問接收方要正本、核證本、翻譯還是其他形式；最後確認房產過戶、銀行領取或遠程委託還缺甚麼。不同城市和不同資產不一定接受完全相同的材料組合。",
                            "最重要的是保留文件的邊界：它可以協助說明繼承人身份，但不替代房屋權屬資料、不處理家屬爭議，也不保證某個內地窗口必然受理。把這個邊界說清楚，反而更容易安排下一步。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-kinship-certificate-scope.html", "澳門親屬關係文件能證明甚麼"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門文件和內地房產資料怎樣分開"),
                    ("/articles/am/family-coordinator-first-sheet.html", "繼承人很多時先選誰負責整理"),
                ],
                "cta": "先說清楚家屬結構、現有澳門文件和內地資產城市，再判斷這份公證書是不是現在最需要的一步。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门与内地遗产",
                "title": "澳门确认继承人资格公证书，什么时候值得先办",
                "description": "澳门家属处理内地遗产时，先判断确认继承人资格公证书是否回答了内地接收方真正需要的问题。",
                "lead": "不要因为家里有遗产就立刻办理。先问清内地接收方要确认继承人身份、代表权限，还是某项房产的登记资料。",
                "key_title": "先看三个判断点",
                "keys": [
                    "家属是否成年、无争议，关系资料是否大致齐全",
                    "内地接收方是否需要正式的继承人身份证明",
                    "公证书不等于房产过户，也不自动产生代理权限",
                ],
                "answer_title": "先说最实用的答案",
                "answer": [
                    "如果所有可能继承人都已成年，对继承人范围没有争议，出生、婚姻、死亡、遗嘱等关系资料也大致齐全，而内地的实际接收方又明确需要一份正式文件说明谁具有继承人身份，这份公证书值得较早考虑。它可以把分散的家属关系整理成一个比较清楚的证明入口。",
                    "但它不是内地房产证，也不会自动证明逝者名下有哪套房、每个人最后取得多少份额，或者某位家属有权替其他人签字。如果房产城市、登记人或接收要求仍不清楚，先查清这些问题，再决定是否办理，通常更省时间。",
                ],
                "sections": [
                    (
                        "先问内地接收方：它要证明的是谁，还是房产",
                        [
                            "同一句“要继承文件”，可能指完全不同的问题。房产登记窗口可能在核对继承人范围，银行可能在核对领取人和授权，受托律师可能先要确认谁能提供指示。先把接收单位、资产城市、登记姓名和用途写在一页纸上，再问现有澳门文件分别能回答什么。",
                            "如果对方真正缺的是内地房屋的准确地址、登记份额、抵押或共有情况，先办继承人资格公证书并不会补上这个缺口。只有当对方需要一份清楚列明继承人的正式文件时，才继续核对澳门的申请条件和所需记录。",
                        ],
                    ),
                    (
                        "这四种情况，值得较早考虑办理",
                        [
                            "第一，家属对配偶、子女、父母或其他可能涉及的人没有不同说法。第二，所有可能继承人均已成年并能处理自己的事务。第三，出生、婚姻、死亡、遗嘱和已故家属等记录有清楚来源。第四，内地接收方已经表示需要核对正式的继承人身份。",
                            "在这种情况下，可以按家属关系列出每份记录和原件保管人。澳门办理时，所需资料会随着配偶、子女、父母、兄弟姐妹、遗嘱、已故继承人或者代位情况变化，不要直接套用另一个家庭的清单。",
                        ],
                    ),
                    (
                        "出现这些情况，不要把公证书当成捷径",
                        [
                            "有未成年人、有人不能自行处理事务、家属失联、关系记录缺失，或者对遗嘱和继承人范围已经有争议时，办理路径可能需要另行处理，不能认为补几份声明就能完成。逝者生前主要居住地不在澳门时，也可能要补充外地继承规则或相关证明。",
                            "如果有人要求一名家属先签全部文件，还要分开看他只是负责联络，是依法负责管理未分割遗产的人，还是已经取得其他人的有效授权。公证书确认继承人，不等于把所有人的决定权集中给一个人。",
                        ],
                    ),
                    (
                        "申请前先做一张家属和文件缺口表",
                        [
                            "第一栏列逝者、配偶、子女、父母和已经去世的家属；第二栏列每段关系的证明来源；第三栏写原件、清晰影像或者只有家人讲述；第四栏写需要向哪个机构补取。如果文件不是中文或葡文，再增加语言和翻译安排。",
                            "内地资产另做一张表，写明城市、地址、登记人、可能份额、现有证明和接收单位。这样可以直接看出，现在缺的是澳门家属证明，还是内地资产资料，不必把两套问题混成一大叠文件。",
                        ],
                    ),
                    (
                        "办好之后，仍要核对三件事",
                        [
                            "先核对姓名、日期、亲属关系和已经去世的家属是否与内地资料一致；再问接收方需要原件、核证本、翻译还是其他形式；最后确认房产过户、银行领取或远程委托还缺什么。不同城市和不同资产不一定使用完全相同的材料组合。",
                            "最重要的是保留文件的边界：它可以帮助说明继承人身份，但不代替房屋权属资料、不处理家属争议，也不保证某个内地窗口一定受理。把这个边界说清楚，反而更容易安排下一步。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-kinship-certificate-scope_cn.html", "澳门亲属关系文件能证明什么"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门文件和内地房产资料怎样分开"),
                    ("/articles/am/family-coordinator-first-sheet_cn.html", "继承人很多时先选谁负责整理"),
                ],
                "cta": "先说清家属结构、现有澳门文件和内地资产城市，再判断这份公证书是不是现在最需要的一步。",
            },
            "en": {
                "lang": "en",
                "locale": "en_MO",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau and Mainland estates",
                "title": "When Should a Macau Family Obtain a Notarial Heir Qualification Deed?",
                "description": "A practical guide to deciding whether a Macau heir qualification deed answers the question raised by a Mainland property or estate recipient.",
                "lead": "Do not order the document simply because an estate exists. First identify what the Mainland recipient needs the family to prove.",
                "key_title": "Three decision points",
                "keys": [
                    "Are all relevant family members adults and in agreement?",
                    "Does the Mainland recipient need formal evidence identifying the heirs?",
                    "The deed does not itself transfer a Mainland property or appoint a representative",
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "The deed is worth considering early when the family agrees about who may inherit, all potential heirs are adults who can manage their own affairs, the civil-status records are largely available, and the actual Mainland recipient wants formal evidence identifying the heirs. In that setting, the deed can turn a scattered family history into one clearer evidential starting point.",
                    "It is not a Mainland title certificate. It does not identify every property owned by the deceased, settle the final share taken by each heir, or give one relative authority to sign for everybody else. If the family does not yet know the property city, registered owner or receiving requirement, investigate those points before commissioning the deed.",
                ],
                "sections": [
                    (
                        "Ask what the Mainland recipient is trying to establish",
                        [
                            "A request for an 'inheritance document' is too vague to act on. A property registration office may be checking the class of heirs. A bank may be checking the person entitled to receive funds and the authority of a representative. A lawyer may first need to know who can give instructions. Put the receiving institution, asset city, registered name and stated purpose on one page, then ask what each Macau document is expected to prove.",
                            "If the missing information is the Mainland property's address, ownership share, mortgage or co-ownership position, an heir qualification deed will not fill that gap. The deed becomes relevant when the missing fact is the formally established identity of the heirs.",
                        ],
                    ),
                    (
                        "Four signs that the deed may be useful now",
                        [
                            "First, the family has one account of the spouse, children, parents and any other potentially relevant relatives. Second, all potential heirs are adults and there is no active disagreement about heirship. Third, the family can trace the birth, marriage, death, will and other records needed to connect the family tree. Fourth, the Mainland recipient has said that formal evidence of heir identity is required.",
                            "The supporting file changes with the family structure. A spouse, child, parent, sibling, deceased intermediate relative, will or representation situation may each call for a different record. The family should map its own relationships and document sources rather than reuse a checklist prepared for another estate.",
                        ],
                    ),
                    (
                        "When not to treat the deed as a shortcut",
                        [
                            "A minor heir, a person unable to manage their own affairs, a missing relative, incomplete civil-status records, or a dispute about a will or family relationship may require a different route. A deceased person whose habitual residence was outside Macau may also create an additional question about the succession material that must be produced. These are not problems to solve by adding informal family declarations to an otherwise incomplete file.",
                            "Be equally careful when one relative is asked to sign everything. A family coordinator, a person managing an undivided estate and a representative acting under authority are different roles. A deed identifying the heirs does not silently transfer every heir's decision-making power to one person.",
                        ],
                    ),
                    (
                        "Prepare two short gap sheets before applying",
                        [
                            "The family sheet should list the deceased, spouse, children, parents and any earlier deaths in the family line. Beside each relationship, record the supporting document, where the original is kept, whether the family has only an image, and which office must provide a replacement. Add the language and translation plan for any record that is not in Chinese or Portuguese.",
                            "The asset sheet should remain separate. Give each Mainland property or account one row with the city, address, registered owner, possible ownership share, existing evidence and receiving institution. The two sheets reveal whether the current gap concerns the Macau family evidence or the Mainland asset itself.",
                        ],
                    ),
                    (
                        "After the deed is issued, keep its limits visible",
                        [
                            "Compare every name, date, relationship and earlier family death against the Mainland records. Ask whether the recipient needs the original, a certified copy, a translation or another form. Then identify what remains for the particular property transfer, bank release or remote instruction. Different cities and different assets may not use the same document package.",
                            "The deed may help establish heir identity, but it does not replace the title record, resolve a family dispute or guarantee acceptance by a particular Mainland office. Treating it as one piece of a purpose-built file is more reliable than treating it as a universal inheritance certificate.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau estate topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling Mainland estates"),
                    ("/articles/am/macau-kinship-certificate-scope_en.html", "What Macau family relationship records can establish"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Separate Macau family evidence from the Mainland property file"),
                    ("/articles/am/family-coordinator-first-sheet_en.html", "Choosing one family coordinator without giving away authority"),
                ],
                "cta": "Describe the family structure, the Macau papers already available and the Mainland asset city before deciding whether this deed is the next useful step.",
            },
        },
    },
    {
        "slug": "letters-testamentary-or-administration",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國與內地遺產",
                "title": "Letters Testamentary 與 Letters of Administration 分別說明甚麼",
                "description": "美國遺產法院簽發的兩類 Letters，主要證明誰獲法院任命處理遺產，以及交到內地前還要核對甚麼。",
                "lead": "先看法院文件的正式抬頭，不要只聽家人把它稱為遺囑證明、執行人文件或管理人證書。",
                "key_title": "先記住三件事",
                "keys": [
                    "兩類 Letters 的核心都是法院任命代表",
                    "有遺囑不一定只會出現 Letters Testamentary",
                    "法院任命不等於完成內地繼承或房產過戶",
                ],
                "answer_title": "先把差別說清楚",
                "answer": [
                    "Letters Testamentary 通常表示遺囑已在相關法院程序中獲接納，法院任命了遺囑中提名並符合條件的執行人。Letters of Administration 通常表示法院任命了遺產管理人，常見於沒有遺囑獲接納的情況。若有遺囑但原定執行人不能或不會任職，文件也可能寫成 with will annexed，意思是法院另行任命管理人依遺囑處理。",
                    "兩類文件首先證明的是誰獲某州、某縣的法院正式任命，以及他在該遺產程序中的權限。它們不會自動列清所有內地繼承人，不會證明逝者名下有哪套內地房產，也不會單憑文件名稱完成內地過戶。",
                ],
                "sections": [
                    (
                        "先看文件抬頭，不要只看家人怎樣稱呼它",
                        [
                            "美國遺產程序由各州及當地法院處理，名稱、版式和權限限制會有差異。先讀簽發法院、州和縣、案件編號、逝者姓名、獲任命人士及簽發日期。不要因為家人說「這是遺囑文件」，就假定它一定是 Letters Testamentary。",
                            "同一遺產檔案中可能同時有遺囑、法院命令、Letters、資產清單和後續報告。遺囑表達安排，法院命令記錄裁定，Letters 則通常是代表向銀行、產權機構或其他接收方證明任命的工作文件。",
                        ],
                    ),
                    (
                        "兩種 Letters 的核心差別",
                        [
                            "Letters Testamentary 一般與已獲接納的遺囑和執行人任命相連。Letters of Administration 一般與管理人任命相連，常見於沒有遺囑獲接納的遺產。若遺囑存在，但提名的執行人已去世、拒絕或不能任職，文件可能出現 with will annexed 等字樣，不能只用「有遺囑」和「沒有遺囑」兩格硬分。",
                            "最可靠的方法是把 Letters 和任命命令一起看。確認法院實際任命了誰、職位名稱是甚麼、是否需要共同簽署、是否有資產或交易限制，以及文件是否仍是接收方願意使用的核證版本。",
                        ],
                    ),
                    (
                        "交到內地前核對六項",
                        [
                            "逐項寫下：一，簽發法院和州；二，案件編號；三，逝者全名；四，獲任命代表的全名和身份；五，簽發日期及目前持有的是原件、核證本還是普通影像；六，文件或命令上列明的權限和限制。姓名有中文、拼音、婚後姓氏或中間名差異時，另做對照表。",
                            "這六項先核對，才能向內地接收方提出具體問題：它是否需要這份任命證明、是否要連同法院命令或遺囑、應如何翻譯和證明，以及代表能否就某項內地資產簽署。",
                        ],
                    ),
                    (
                        "Letters 沒有替你證明的事項",
                        [
                            "它通常不處理內地房屋的登記人、共有份額、抵押、佔用或歷史地址；也不必然列出每名按內地程序需要參與的家屬。若美國遺產程序的資產清單沒有提到內地房屋，也不能因此推定房屋不存在或已由 Letters 處理。",
                            "把三套資料分開：美國法院任命文件回答誰是代表；家屬和遺囑資料協助核對誰可能涉及繼承；內地產權資料回答具體資產是甚麼。三套資料對得上，才判斷下一步文件和簽署安排。",
                        ],
                    ),
                    (
                        "準備文件的實用順序",
                        [
                            "先取得清晰的 Letters 和相關任命命令，確認是否需要近期核證本；再列出中英文姓名和證件對照；同時找出內地資產城市、地址和登記資料。把這一頁情況交給實際接收方核對後，才安排翻譯、附加證明或遠程授權。",
                            "若不同家屬爭執代表資格、有人要求撤換代表、法院文件有限制，或內地房屋被他人佔用，就不要把問題縮小成翻譯哪一張 Letters。先保存完整法院文件和資產資料，再分別處理代表權和內地資產爭議。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/issuing-state-matters.html", "為甚麼美國文件的簽發州很重要"),
                    ("/articles/us/mainland-asset-omitted-from-probate.html", "美國遺產程序沒有列出內地資產怎樣辦"),
                    ("/articles/us/remote-china-lawyer.html", "人在美國怎樣遠程整理內地法律事務"),
                ],
                "cta": "把 Letters 首頁、任命命令和內地資產城市放在一起，再判斷這份法院任命能回答哪一個問題。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国与内地遗产",
                "title": "Letters Testamentary 和 Letters of Administration 分别说明什么",
                "description": "美国遗产法院签发的两类 Letters，主要证明谁被法院任命处理遗产，以及交到内地前还要核对什么。",
                "lead": "先看法院文件的正式标题，不要只听家人把它称作遗嘱证明、执行人文件或者管理人证书。",
                "key_title": "先记住三件事",
                "keys": [
                    "两类 Letters 的核心都是法院任命代表",
                    "有遗嘱不一定只会出现 Letters Testamentary",
                    "法院任命不等于完成内地继承或者房产过户",
                ],
                "answer_title": "先把差别说清楚",
                "answer": [
                    "Letters Testamentary 通常表示遗嘱已经在相关法院程序中被接纳，法院任命了遗嘱中提名并符合条件的执行人。Letters of Administration 通常表示法院任命了遗产管理人，常见于没有遗嘱被接纳的情况。如果有遗嘱，但原定执行人不能或者不愿任职，文件也可能写成 with will annexed，意思是法院另行任命管理人依遗嘱处理。",
                    "两类文件首先证明的是谁被某个州、某个县的法院正式任命，以及他在该遗产程序中的权限。它们不会自动列清所有内地继承人，不会证明逝者名下有哪套内地房产，也不会只凭文件标题完成内地过户。",
                ],
                "sections": [
                    (
                        "先看文件标题，不要只看家人怎样称呼它",
                        [
                            "美国遗产程序由各州和当地法院处理，名称、格式和权限限制可能不同。先读签发法院、州和县、案件编号、逝者姓名、被任命人员和签发日期。不要因为家人说“这是遗嘱文件”，就认为它一定是 Letters Testamentary。",
                            "同一遗产档案中可能同时有遗嘱、法院命令、Letters、资产清单和后续报告。遗嘱表达安排，法院命令记录裁定，Letters 通常是代表向银行、产权机构或者其他接收方证明任命的工作文件。",
                        ],
                    ),
                    (
                        "两种 Letters 的核心差别",
                        [
                            "Letters Testamentary 一般与已经被接纳的遗嘱和执行人任命相连。Letters of Administration 一般与管理人任命相连，常见于没有遗嘱被接纳的遗产。如果遗嘱存在，但提名执行人已经去世、拒绝或者不能任职，文件可能出现 with will annexed 等字样，不能只用“有遗嘱”和“没有遗嘱”两格来硬分。",
                            "最可靠的做法是把 Letters 和任命命令一起看。确认法院实际任命了谁、职位名称是什么、是否需要共同签字、有没有资产或交易限制，以及文件是否仍是接收方愿意使用的核证版本。",
                        ],
                    ),
                    (
                        "交到内地前核对六项",
                        [
                            "逐项写下：一，签发法院和州；二，案件编号；三，逝者全名；四，被任命代表的全名和身份；五，签发日期，以及现在持有的是原件、核证本还是普通影像；六，文件或者命令列明的权限和限制。姓名有中文、拼音、婚后姓氏或者中间名差异时，另做对照表。",
                            "先核对这六项，才能向内地接收方提出具体问题：它是否需要这份任命证明，是否要连同法院命令或遗嘱，应当怎样翻译和证明，以及代表能不能就某项内地资产签字。",
                        ],
                    ),
                    (
                        "Letters 没有替你证明的事项",
                        [
                            "它通常不处理内地房屋的登记人、共有份额、抵押、占用或者历史地址，也不一定列出每个按照内地程序需要参与的家属。如果美国遗产程序的资产清单没有提到内地房屋，也不能因此认为房屋不存在或者已经被 Letters 处理。",
                            "把三组资料分开：美国法院任命文件回答谁是代表；家属和遗嘱资料帮助核对哪些人可能涉及继承；内地产权资料回答具体资产是什么。三组资料能够对应，才判断下一步文件和签字安排。",
                        ],
                    ),
                    (
                        "准备文件的实用顺序",
                        [
                            "先取得清晰的 Letters 和相关任命命令，确认是否需要近期核证本；再列出中英文姓名和证件对照；同时找出内地资产城市、地址和登记资料。把这一页情况交给实际接收方核对后，再安排翻译、附加证明或者远程授权。",
                            "如果不同家属争议代表资格、有人要求撤换代表、法院文件有限制，或者内地房屋被他人占用，就不要把问题缩小成翻译哪一份 Letters。先保存完整法院文件和资产资料，再分别处理代表权限和内地资产争议。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/issuing-state-matters_cn.html", "为什么美国文件的签发州很重要"),
                    ("/articles/us/mainland-asset-omitted-from-probate_cn.html", "美国遗产程序没有列出内地资产怎么办"),
                    ("/articles/us/remote-china-lawyer_cn.html", "人在美国怎样远程整理内地法律事务"),
                ],
                "cta": "把 Letters 首页、任命命令和内地资产城市放在一起，再判断这份法院任命能回答哪一个问题。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. and Mainland estates",
                "title": "Letters Testamentary or Letters of Administration: What Do They Actually Prove?",
                "description": "A plain-English guide to the two common U.S. probate appointment documents and the checks needed before using them for a Mainland China asset.",
                "lead": "Read the formal heading and issuing court before relying on the family's shorthand description of the document.",
                "key_title": "Three points to remember",
                "keys": [
                    "Both documents primarily evidence a court appointment",
                    "A will does not always mean the document will be Letters Testamentary",
                    "A U.S. appointment does not complete a Mainland inheritance transfer",
                ],
                "answer_title": "The distinction in plain language",
                "answer": [
                    "Letters Testamentary generally follow the admission of a will and the court's appointment of a qualified executor nominated in that will. Letters of Administration generally evidence the appointment of an administrator, often where no will has been admitted to probate. A will may still exist where the named executor cannot or will not serve; the appointment may then use wording such as administration with the will annexed.",
                    "The central fact proved by either document is that a particular state or county probate court appointed the named personal representative, subject to the authority and restrictions shown in the court file. The document does not automatically identify every person who must participate in a Mainland inheritance, prove ownership of a Mainland property, or transfer that property.",
                ],
                "sections": [
                    (
                        "Start with the heading, court and case number",
                        [
                            "Probate is administered under state law through local courts, so names, formats and limitations vary. Read the issuing court, state and county, case number, decedent, appointed representative and issue date. Do not assume that a paper is Letters Testamentary merely because a relative calls it 'the will document'.",
                            "One probate file may contain the will, an appointment order, the Letters, an inventory and later accounts. The will records the deceased's plan. The court order records the appointment decision. The Letters are commonly the working evidence used by the representative when dealing with banks, title companies and other institutions.",
                        ],
                    ),
                    (
                        "What separates the two common forms of Letters",
                        [
                            "Letters Testamentary usually connect an admitted will with the appointment of the nominated executor. Letters of Administration usually connect the estate with an administrator appointed by the court, often where no will has been admitted. That is a useful starting distinction, not a rule to apply without reading the file.",
                            "Where a will exists but the nominated executor has died, declined or is unable to serve, the court may appoint another representative and use wording referring to administration with the will annexed. Read the Letters together with the appointment order to confirm the actual office, whether representatives must act jointly, and whether a bond, special restriction or limited power appears in the record.",
                        ],
                    ),
                    (
                        "Six checks before presenting the document in Mainland China",
                        [
                            "Create one line for each of these items: the issuing court and state; the probate case number; the decedent's full name; the representative's full name and capacity; the issue date and whether the family holds an original, certified copy or ordinary scan; and every stated power or restriction. Add a separate identity table for Chinese names, romanisation, married surnames and middle-name differences.",
                            "These checks turn a vague enquiry into a useful one. The Mainland recipient can then say whether it needs evidence of the appointment, the underlying order or will, a certified copy, translation or additional authentication, and whether the representative may sign for the particular Mainland asset.",
                        ],
                    ),
                    (
                        "What the Letters do not establish",
                        [
                            "The document does not normally establish the registered owner, co-ownership share, mortgage, occupation or historical address of a Mainland home. It may not identify every family member whose participation is relevant to the Mainland procedure. The absence of the Mainland property from a U.S. probate inventory does not prove that the property does not exist or has already been dealt with.",
                            "Keep three files separate. The U.S. court file answers who was appointed as personal representative. The will and family records help identify the succession questions. The Mainland title file establishes the particular asset. Only after those files are compared can the family decide what translation, evidence and signatures are actually required.",
                        ],
                    ),
                    (
                        "A practical preparation order",
                        [
                            "Obtain a clear copy of the Letters and the related appointment order, and ask whether a recently certified copy is needed. Build the English-Chinese identity table. At the same time, locate the Mainland asset city, address and title information. Send that one-page summary to the actual recipient before arranging translation, an apostille or remote authority.",
                            "If relatives challenge the representative, seek removal, point to a restriction in the court file, or dispute control of the Mainland property, the issue is no longer a document-format exercise. Preserve the complete court record and property evidence, then assess the representative's authority and the Mainland asset dispute as separate but connected problems.",
                        ],
                    ),
                ],
                "related_title": "Continue with the United States topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling Mainland estates"),
                    ("/articles/us/issuing-state-matters_en.html", "Why the issuing state matters for a U.S. document"),
                    ("/articles/us/mainland-asset-omitted-from-probate_en.html", "When a Mainland asset is missing from the U.S. probate file"),
                    ("/articles/us/remote-china-lawyer_en.html", "Organising Mainland legal work from the United States"),
                ],
                "cta": "Place the first page of the Letters, the appointment order and the Mainland asset city side by side before deciding what the court appointment proves.",
            },
        },
    },
]


def write_articles() -> None:
    for article in ARTICLES:
        target_dir = ROOT / article["directory"]
        for lang in ("tc", "cn", "en"):
            suffix = LANG_SUFFIX[lang]
            target = target_dir / f"{article['slug']}{suffix}.html"
            target.write_text(render_article(article, lang), encoding="utf-8")


HUB_UPDATES = {
    "articles/macau/index.html": {
        "href": "/articles/am/macau-heir-qualification-deed.html",
        "card": '<a href="/articles/am/macau-heir-qualification-deed.html"><span class="v24-tag">繼承文件</span><strong>澳門確認繼承人資格公證書，甚麼時候值得先辦</strong><p>先看家屬是否無爭議、文件是否齊全，再問內地接收方是否需要。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/macau/index_cn.html": {
        "href": "/articles/am/macau-heir-qualification-deed_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">继承文件</span><h3>澳门确认继承人资格公证书，什么时候值得先办</h3><p>先看家属是否无争议、资料是否齐全，再问内地接收方是否需要。</p></div><a class="v25-pill-action" href="/articles/am/macau-heir-qualification-deed_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/macau/index_en.html": {
        "href": "/articles/am/macau-heir-qualification-deed_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Heir evidence</span><h3>When a Macau heir qualification deed is worth obtaining</h3><p>Check family agreement, available records and the Mainland recipient\'s actual purpose.</p></div><a class="v25-pill-action" href="/articles/am/macau-heir-qualification-deed_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index.html": {
        "href": "/articles/us/letters-testamentary-or-administration.html",
        "card": '<a href="/articles/us/letters-testamentary-or-administration.html"><span class="v24-tag">法院文件</span><strong>Letters Testamentary 與 Letters of Administration 分別說明甚麼</strong><p>先確認法院任命了誰，再分開處理繼承人、資產和內地接收用途。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/united-states/index_cn.html": {
        "href": "/articles/us/letters-testamentary-or-administration_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">法院文件</span><h3>Letters Testamentary 和 Letters of Administration 分别说明什么</h3><p>先确认法院任命了谁，再分开处理继承人、资产和内地接收用途。</p></div><a class="v25-pill-action" href="/articles/us/letters-testamentary-or-administration_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index_en.html": {
        "href": "/articles/us/letters-testamentary-or-administration_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Court appointment</span><h3>Letters Testamentary or Letters of Administration?</h3><p>Identify the court-appointed representative before addressing heirs and Mainland assets.</p></div><a class="v25-pill-action" href="/articles/us/letters-testamentary-or-administration_en.html">Read Article</a></article>',
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
    updated = block.replace(
        f"<lastmod>{old_date}</lastmod>", f"<lastmod>{TODAY}</lastmod>"
    )
    return text[:start] + updated + text[end:]


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
    for hub in ("macau", "united-states"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, f"{SITE}/articles/{hub}/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
