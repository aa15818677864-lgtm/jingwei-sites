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
        "slug": "multiple-wills-across-regions",
        "directory": "articles/am",
        "topic": "macau",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門遺囑與內地房產",
                "title": "家中找到幾份遺囑，澳門和內地文件先怎樣排時間線",
                "description": "家中找到多份澳門遺囑時，先保留原件、查明來源和日期，再核對哪些內容互相影響及內地房產需要哪些文件。",
                "lead": "清理文件時找到公證遺囑副本、密封信封和手寫紙，不要先選看起來最新的一份。先保住原件，再把每份文件放回它的時間和來源。",
                "key_title": "先做三件事",
                "keys": [
                    "每份原件保持原狀，另做清晰掃描和保管紀錄",
                    "按日期、來源、形式、保管人和涉及資產排表",
                    "把澳門遺囑判斷和內地房產收件分成兩個環節",
                ],
                "answer_title": "不要只問哪一份日期最遲",
                "answer": [
                    "較後的遺囑不一定把較早遺囑全部抹去。有時它只更改某項財產或某位受益人的安排；有時文件明確寫明全部或部分廢止。真正要比較的是每一項內容是否衝突，而不是只看封面日期。",
                    "如果內地房產正準備轉名，接收方也可能要求家屬交代完整的遺囑鏈和全部可能繼承人。先把文件排清楚，再決定由哪個環節核實效力，會比拿一份文件直接嘗試辦理穩妥。",
                ],
                "sections": [
                    (
                        "一、先保持原狀，不要替文件作整理",
                        [
                            "先為每份文件編一個暫時號碼，拍攝封面、每一頁、簽名、裝訂和信封。不要拆釘、補寫日期、重排頁次，也不要自行打開看似仍然密封的遺囑。原件由誰發現、在甚麼位置找到、之後交給誰保管，也一併寫下。",
                            "掃描本只用於閱讀和比較，原件另行保存。如果文件交給家人、律師或其他人查看，記下交接日期和用途。這份簡單紀錄可以避免後來出現少頁、加註或保管來源說不清的爭議。",
                        ],
                    ),
                    (
                        "二、用一張六欄表把幾份遺囑排在一起",
                        [
                            "六欄分別寫日期、文件形式、來源或保管人、簽署或見證資料、提到的資產，以及有沒有寫明廢止舊安排。另把補充遺囑、廢止文件、律師來信和只有影印本的版本放在同一條時間線上，但清楚標明它們不是同一類文件。",
                            "比較時逐項看房產、存款和其他資產怎樣分配。後一份文件沒有提到某套房，不代表前一份關於該房的安排必然失效；同一天的文件如果互相衝突，也不能靠家人猜先後。這些位置應直接標成待核實。",
                        ],
                    ),
                    (
                        "三、再查有沒有家中尚未找到的正式紀錄",
                        [
                            "利害關係人可帶同逝者身份資料和死亡文件，向澳門三間公共公證署查詢有否公證遺囑或存放的密封遺囑。公證遺囑通常由辦理的公證署保存；密封遺囑則可能由逝者、公證署或第三人保管。",
                            "查詢結果和家中找到的原件要並排記錄。沒有查到公證紀錄，不等於家中其他文件自動無效；查到一份公證遺囑，也不等於再沒有後續文件。先把查詢日期、範圍和取得的證明保存好。",
                        ],
                    ),
                    (
                        "四、內地房產不要只交家人選中的一份",
                        [
                            "先查房產城市、登記姓名、取得時間、共有和限制，再向所在地接收方說明家中有幾份遺囑、是否有原件、澳門方面正在核實甚麼。請對方列明需要完整文件、正式副本、中文文本、親屬資料或到場核實中的哪些項目。",
                            "如果家屬對遺囑真假、先後、房產份額或受益人有不同意見，先停止把任何一份說成已確定的最後安排。保存完整文件鏈和各方說法，再判斷應先處理遺囑爭議，還是先補房產和身份資料。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門家屬處理內地遺產專題"),
                    ("/articles/am/macau-will-mainland-property.html", "一份澳門遺囑提到內地房產先查甚麼"),
                    ("/articles/am/macau-no-will-mainland-property.html", "沒有找到遺囑時從哪一步開始"),
                    ("/articles/am/macau-heir-qualification-deed.html", "澳門繼承人資格文件能說明甚麼"),
                ],
                "cta": "說明每份文件的日期、形式、原件位置和內地房產城市，先把真正衝突的位置找出來。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门遗嘱与内地房产",
                "title": "家里找到几份遗嘱，澳门和内地文件先怎样排时间线",
                "description": "家里找到多份澳门遗嘱时，先保留原件、查明来源和日期，再核对哪些内容互相影响以及内地房产需要哪些文件。",
                "lead": "清理文件时找到公证遗嘱副本、密封信封和手写纸，不要先选择看起来最新的一份。先保护原件，再把每份文件放回它的时间和来源。",
                "key_title": "先做三件事",
                "keys": [
                    "每份原件保持原状，另做清晰扫描和保管记录",
                    "按日期、来源、形式、保管人和涉及资产列表",
                    "把澳门遗嘱判断和内地房产收件分成两个环节",
                ],
                "answer_title": "不要只问哪一份日期最晚",
                "answer": [
                    "较后的遗嘱不一定把较早遗嘱全部抹去。有时它只更改某项财产或某位受益人的安排；有时文件明确写明全部或者部分撤销。真正需要比较的是每一项内容是否冲突，而不是只看封面日期。",
                    "如果内地房产正准备过户，接收方也可能要求家属说明完整的遗嘱链和全部可能继承人。先把文件排清楚，再决定由哪个环节核实效力，会比拿一份文件直接尝试办理更稳妥。",
                ],
                "sections": [
                    (
                        "一、先保持原状，不要替文件作整理",
                        [
                            "先给每份文件编一个临时号码，拍摄封面、每一页、签名、装订和信封。不要拆订、补写日期、重排页次，也不要自行打开看起来仍然密封的遗嘱。原件由谁发现、在哪里找到、后来交给谁保管，也一起写下。",
                            "扫描件只用于阅读和比较，原件另外保存。如果文件交给家人、律师或其他人查看，记下交接日期和用途。这份简单记录可以避免后来出现缺页、加注或者保管来源说不清的问题。",
                        ],
                    ),
                    (
                        "二、用一张六列表格把几份遗嘱放在一起",
                        [
                            "六列分别写日期、文件形式、来源或保管人、签署或见证资料、提到的资产，以及有没有写明撤销以前的安排。补充遗嘱、撤销文件、律师来信和只有复印件的版本也放在同一条时间线上，但要明确标注它们不是同一类文件。",
                            "比较时逐项查看房产、存款和其他资产怎样分配。后一份文件没有提到某套房，不代表前一份关于该房的安排一定失效；同一天的文件如果互相冲突，也不能由家人猜测先后。这些位置应当直接标为待核实。",
                        ],
                    ),
                    (
                        "三、再查有没有家里尚未找到的正式记录",
                        [
                            "利害关系人可以带逝者身份资料和死亡文件，向澳门三家公共公证署查询是否有公证遗嘱或者存放的密封遗嘱。公证遗嘱通常由办理的公证署保存；密封遗嘱则可能由逝者、公证署或第三人保管。",
                            "查询结果和家里找到的原件要并列记录。没有查到公证记录，不等于家里其他文件自动无效；查到一份公证遗嘱，也不等于没有后续文件。先把查询日期、范围和取得的证明保存好。",
                        ],
                    ),
                    (
                        "四、内地房产不要只交家人选中的一份",
                        [
                            "先核对房产城市、登记姓名、取得时间、共有和限制，再向所在地接收方说明家里有几份遗嘱、是否有原件、澳门方面正在核实什么。请对方列明需要完整文件、正式副本、中文文本、亲属资料或者到场核实中的哪些项目。",
                            "如果家属对遗嘱真假、先后、房产份额或受益人有不同意见，先停止把任何一份说成已经确定的最后安排。保存完整文件链和各方说法，再判断应先处理遗嘱争议，还是先补房产和身份资料。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门家属处理内地遗产专题"),
                    ("/articles/am/macau-will-mainland-property_cn.html", "一份澳门遗嘱提到内地房产先查什么"),
                    ("/articles/am/macau-no-will-mainland-property_cn.html", "没有找到遗嘱时从哪一步开始"),
                    ("/articles/am/macau-heir-qualification-deed_cn.html", "澳门继承人资格文件能说明什么"),
                ],
                "cta": "说明每份文件的日期、形式、原件位置和内地房产城市，先找出真正冲突的位置。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau wills and Mainland property",
                "title": "Several Wills and Mainland Property: Build the Timeline First",
                "description": "A practical way for a Macau family to preserve and compare several wills before dealing with property in Mainland China.",
                "lead": "A notarised copy, a sealed envelope and a handwritten paper can all turn up in the same drawer. Do not begin by choosing the document with the latest visible date.",
                "key_title": "Begin with three tasks",
                "keys": [
                    "Preserve each original and make a separate scan and custody note",
                    "List the date, source, form, custodian and assets mentioned",
                    "Keep the Macau will review separate from the Mainland property process",
                ],
                "answer_title": "The latest date does not answer every question",
                "answer": [
                    "A later will does not necessarily erase every part of an earlier one. It may change one asset or one beneficiary, or expressly revoke all or part of the earlier arrangements. The useful comparison is provision by provision, not date alone.",
                    "A Mainland property recipient may also need the complete testamentary history and information about every person who may be relevant to the estate. Build a reliable record first, then decide where the effect of each document has to be resolved.",
                ],
                "sections": [
                    (
                        "1. Preserve the papers exactly as found",
                        [
                            "Give each item a temporary number and photograph the cover, every page, signatures, binding and envelope. Do not remove staples, add dates, reorder pages or open a document that still appears sealed. Record who found it, where it was found and who now holds it.",
                            "Use a scan for reading and comparison, while keeping the original separately. If an item is passed to a relative, lawyer or another reviewer, note the date and purpose. This small custody record can later answer questions about missing pages, later markings and document source.",
                        ],
                    ),
                    (
                        "2. Put every item on one six-column timeline",
                        [
                            "Use columns for the date, document form, source or custodian, signing or witness details, assets mentioned and any express revocation wording. Add codicils, revocation records, lawyer correspondence and copy-only versions to the same timeline, while labelling them for what they are.",
                            "Compare the treatment of each property, account and other asset. Silence about a home in the later document does not automatically dispose of an earlier provision about that home. If two same-day documents conflict and their order is unknown, mark the conflict for review rather than guessing.",
                        ],
                    ),
                    (
                        "3. Check whether an official Macau record is still missing",
                        [
                            "A person with an interest in the estate may use the deceased's identity and death records to ask Macau's three public notarial offices whether a notarised will or deposited sealed will is recorded. A notarised will is ordinarily retained by the office that handled it, while a sealed will may be held by the deceased, an office or another custodian.",
                            "Record that search beside the documents found at home. A negative public-record search does not decide the status of every private paper, and finding one official will does not prove that there was no later document. Keep the search date, scope and result.",
                        ],
                    ),
                    (
                        "4. Do not send only the family's preferred will for the property",
                        [
                            "Identify the Mainland city, registered owner, acquisition date, co-ownership and restrictions. Tell the receiving side how many testamentary documents exist, which originals are available and what is still being checked in Macau. Ask exactly which complete records, official copies, Chinese text, family evidence or attendance it requires.",
                            "If the family disputes authenticity, sequence, ownership share or beneficiary, do not describe any one paper as the settled final answer. Preserve the full document chain and each person's position, then decide whether the will dispute or the missing property and identity evidence must be handled first.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Macau topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"),
                    ("/articles/am/macau-will-mainland-property_en.html", "Three checks when a Macau will names Mainland property"),
                    ("/articles/am/macau-no-will-mainland-property_en.html", "Where to start when no will has been found"),
                    ("/articles/am/macau-heir-qualification-deed_en.html", "What a Macau heir qualification deed establishes"),
                ],
                "cta": "List the date, form, original location and Mainland property city for every document, then identify the provisions that actually conflict.",
            },
        },
    },
    {
        "slug": "unknown-mainland-bank-accounts",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與內地存款線索",
                "title": "不知道存款在哪家內地銀行，新加坡家屬先怎樣找線索",
                "description": "新加坡家屬不知道逝者在哪家內地銀行有存款時，先從舊文件和交易痕跡找機構線索，再逐家確認查詢要求。",
                "lead": "家中沒有存摺和銀行卡，只剩一張匯款截圖或幾條舊短訊，也可以開始整理。先找可能的銀行，不要先猜餘額。",
                "key_title": "先分清三件事",
                "keys": [
                    "線索只代表可能有往來，不等於已確認有賬戶",
                    "新加坡遺產文件可支持身份說明，不是跨銀行搜尋按鈕",
                    "找到銀行後，查詢和支取仍是兩個不同步驟",
                ],
                "answer_title": "先做一張銀行線索表",
                "answer": [
                    "不要把所有銀行一次列成收件清單。先從逝者留下的信件、短訊、手機應用、匯款紀錄、工資或退休金資料、物業繳費和舊卡片中找出具體機構名稱、城市或分行，再逐家確認是否有適合繼承人的查詢方式。",
                    "如果家屬在新加坡申請遺囑認證或遺產管理，程序會要求整理資產清單；在資料未齊時，也可先處理前段程序，再向相關機構補取資料。這些文件有助於說明誰代表遺產，但不會自動讓內地所有銀行交出資料。",
                ],
                "sections": [
                    (
                        "一、從日常痕跡找銀行，不要嘗試登入賬戶",
                        [
                            "查看銀行信件和信封、短訊發件人、手機應用圖標、工資或退休金入賬資料、匯款回單、利息或理財通知、按揭還款、物業管理費和水電扣款。只記錄看得見的機構名稱、城市、尾號和日期，不要使用逝者密碼、驗證碼或人臉登入。",
                            "家人如果只記得銀行顏色、附近地標或曾去過的城市，也可另列為口述線索，但不要寫成已確認事實。把截圖原圖、完整短訊和信封一起保存，避免只截取一行文字後失去來源。",
                        ],
                    ),
                    (
                        "二、把可能機構和已確認賬戶分開",
                        [
                            "線索表可設六欄：機構、城市或分行、可能產品、線索來源、最後日期和目前狀態。狀態只用待核實、已聯絡、需補資料、已確認或排除，不先填估算餘額。",
                            "一筆內地匯款可能只是曾經收款，一條扣款短訊也可能來自已關閉的卡。只有銀行按自己的查詢程序確認後，才把它列為遺產資產。這樣可以防止家屬把時間花在幾十家沒有具體線索的機構。",
                        ],
                    ),
                    (
                        "三、新加坡文件是身份和程序資料，不是統一搜尋工具",
                        [
                            "在新加坡申請遺囑認證或遺產管理時，需要整理資產清單。資料未齊時，申請人可先向相關機構取得資料，部分情況也可在前段申請後補交資產清單；若之後才發現資產，還要查看當地程序是否需要補充或更新。",
                            "法院命令、遺囑認證書或遺產管理文件，可以幫助說明誰是獲認可的遺產代表，但它們不會自動成為查遍內地銀行的許可。向每家可能的銀行聯絡時，要如實說明文件目前處於申請、命令還是正式授權階段。",
                        ],
                    ),
                    (
                        "四、逐家問清查詢材料，再談如何支取",
                        [
                            "向有具體線索的銀行先問查詢需要甚麼：逝者身份和死亡資料、申請人身份、親屬或遺產代表文件、中文翻譯、原件核對，以及能否由受託人辦理。請對方把查詢資料和日後支取資料分開說明。",
                            "內地小額存款有較簡化的處理情形，但跨境身份、非居民家屬或資料不完整時，未必能直接使用。不要先以餘額不大為由承諾可以快捷取款；找到賬戶後，再按銀行、金額、產品和家屬身份確認實際路徑。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/known-mainland-bank-account.html", "已知內地銀行和賬號時先準備甚麼"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "內地資產怎樣放入新加坡資產清單"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "先分清遺囑認證和遺產管理文件"),
                ],
                "cta": "列出逝者姓名、可能銀行、城市、線索來源和新加坡遺產程序狀態，先判斷應聯絡哪幾家機構。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与内地存款线索",
                "title": "不知道存款在哪家内地银行，新加坡家属先怎样找线索",
                "description": "新加坡家属不知道逝者在哪家内地银行有存款时，先从旧文件和交易痕迹寻找机构线索，再逐家确认查询要求。",
                "lead": "家里没有存折和银行卡，只剩一张汇款截图或者几条旧短信，也可以开始整理。先找可能的银行，不要先猜余额。",
                "key_title": "先分清三件事",
                "keys": [
                    "线索只代表可能有往来，不等于已经确认有账户",
                    "新加坡遗产文件可以支持身份说明，不是跨银行搜索按钮",
                    "找到银行后，查询和支取仍是两个不同步骤",
                ],
                "answer_title": "先做一张银行线索表",
                "answer": [
                    "不要把所有银行一次列成材料寄送清单。先从逝者留下的信件、短信、手机应用、汇款记录、工资或退休金资料、物业缴费和旧卡片中找出具体机构名称、城市或网点，再逐家确认是否有适合继承人的查询方式。",
                    "如果家属在新加坡申请遗嘱认证或遗产管理，程序会要求整理资产清单；在资料不完整时，也可以先处理前面的程序，再向相关机构补取资料。这些文件有助于说明谁代表遗产，但不会自动要求内地所有银行交出资料。",
                ],
                "sections": [
                    (
                        "一、从日常痕迹找银行，不要尝试登录账户",
                        [
                            "查看银行信件和信封、短信发送方、手机应用图标、工资或退休金入账资料、汇款回单、利息或理财通知、按揭还款、物业管理费和水电扣款。只记录能看见的机构名称、城市、尾号和日期，不要使用逝者密码、验证码或者人脸登录。",
                            "家人如果只记得银行颜色、附近地标或曾经去过的城市，也可以另外列为口述线索，但不要写成已经确认的事实。把截图原图、完整短信和信封一起保存，避免只截取一行文字后失去来源。",
                        ],
                    ),
                    (
                        "二、把可能机构和已确认账户分开",
                        [
                            "线索表可以设置六列：机构、城市或网点、可能产品、线索来源、最后日期和目前状态。状态只使用待核实、已联系、需补资料、已确认或者排除，不要先填写估算余额。",
                            "一笔内地汇款可能只是曾经收款，一条扣款短信也可能来自已经关闭的卡。只有银行按照自己的查询程序确认后，才把它列为遗产资产。这样可以避免家属把时间花在几十家没有具体线索的机构。",
                        ],
                    ),
                    (
                        "三、新加坡文件是身份和程序资料，不是统一搜索工具",
                        [
                            "在新加坡申请遗嘱认证或遗产管理时，需要整理资产清单。资料不完整时，申请人可以先向相关机构取得资料，部分情况也可以在前段申请后补交资产清单；如果以后才发现资产，还要查看当地程序是否需要补充或者更新。",
                            "法院命令、遗嘱认证书或遗产管理文件，可以帮助说明谁是获得认可的遗产代表，但它们不会自动成为查遍内地银行的许可。向每家可能的银行联系时，要如实说明文件目前处于申请、命令还是正式授权文件阶段。",
                        ],
                    ),
                    (
                        "四、逐家问清查询材料，再谈如何支取",
                        [
                            "向有具体线索的银行先询问查询需要什么：逝者身份和死亡资料、申请人身份、亲属或遗产代表文件、中文翻译、原件核对，以及是否可以委托办理。请对方把查询资料和以后支取资料分别说明。",
                            "内地小额存款有相对简化的处理情形，但跨境身份、非居民家属或资料不完整时，未必可以直接使用。不要因为估计余额不大就承诺能够快速取款；找到账户后，再按银行、金额、产品和家属身份确认实际路径。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/known-mainland-bank-account_cn.html", "已知内地银行和账号时先准备什么"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "内地资产怎样放入新加坡资产清单"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "先分清遗嘱认证和遗产管理文件"),
                ],
                "cta": "列出逝者姓名、可能银行、城市、线索来源和新加坡遗产程序状态，先判断应联系哪几家机构。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / A Singapore family tracing Mainland deposits",
                "title": "The Mainland Bank Is Unknown: Where a Singapore Family Can Start",
                "description": "How a Singapore family can trace likely Mainland banks from records and transaction clues before asking each institution about an estate account.",
                "lead": "A remittance screenshot or an old text message may be enough to begin. Identify likely institutions first; do not begin by guessing the balance or contacting every bank.",
                "key_title": "Keep three distinctions clear",
                "keys": [
                    "A clue suggests a relationship; it does not confirm an open account",
                    "Singapore estate papers establish context, not a universal bank search",
                    "An account enquiry and release of funds are separate steps",
                ],
                "answer_title": "Build a short bank-clue register first",
                "answer": [
                    "Review letters, message senders, phone apps, remittance records, salary or pension papers, property payments and old cards for a specific institution, city or branch. Contact the institutions supported by real clues and ask which estate-enquiry route they accept.",
                    "A Singapore probate or administration application requires an asset schedule, and missing details may sometimes be obtained from relevant institutions or supplied later in the process. Those papers can explain who is dealing with the estate, but they do not compel every Mainland bank to conduct a combined search.",
                ],
                "sections": [
                    (
                        "1. Follow ordinary records without accessing the account",
                        [
                            "Check bank letters and envelopes, message senders, app icons, salary or pension credits, remittance slips, interest or investment notices, mortgage payments, management fees and utility debits. Record only the institution, city, visible final digits and date. Do not use the deceased's password, one-time code or facial login.",
                            "A relative may remember only a bank colour, nearby landmark or city. Keep that as an unverified recollection, not a confirmed fact. Preserve the original screenshot, complete message and envelope so that the clue still has a source.",
                        ],
                    ),
                    (
                        "2. Separate possible institutions from confirmed accounts",
                        [
                            "Use columns for institution, city or branch, possible product, source of the clue, latest date and current status. Useful status labels are unverified, contacted, more information needed, confirmed and ruled out. Leave the balance blank until the institution confirms it.",
                            "A Mainland remittance may show only a past recipient, and a debit message may relate to a closed card. Add an item to the estate asset list only after the institution's own enquiry process confirms it. This keeps the family focused on evidence rather than sending papers to dozens of banks.",
                        ],
                    ),
                    (
                        "3. Singapore estate papers are not a cross-bank search tool",
                        [
                            "A Singapore probate or administration application calls for a Schedule of Assets. Where information is missing, the applicant may seek details from relevant institutions and, in some circumstances, provide the schedule later. An asset found later may also require a further filing or amendment in Singapore.",
                            "An Order in Terms, Grant of Probate or administration grant can help establish the recognised estate representative. It does not automatically authorise a search across Mainland banks. When writing to a possible institution, state accurately whether the Singapore file is at the application, court-order or issued-grant stage.",
                        ],
                    ),
                    (
                        "4. Ask about the enquiry first and release requirements second",
                        [
                            "Ask each bank supported by a real clue what it needs for an enquiry: the deceased's identity and death records, the applicant's identity, family or representative papers, Chinese translations, original inspection and any permitted use of an authorised agent. Ask for the later release requirements separately.",
                            "Some smaller Mainland deposits may have a simplified release route, but cross-border identity, non-resident relatives or incomplete records may take the case outside it. Do not promise a quick withdrawal because the expected balance is modest. Confirm the bank, product, balance and family status first.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling a Mainland estate"),
                    ("/articles/singapore/known-mainland-bank-account_en.html", "When the Mainland bank and account are already known"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Recording a Mainland asset in the Singapore schedule"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Grant of Probate or Letters of Administration"),
                ],
                "cta": "List the deceased's names, likely institutions, cities, clue sources and current Singapore estate stage to identify the first banks worth contacting.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/macau/index.html": (
        "/articles/am/multiple-wills-across-regions.html",
        '<a href="/articles/am/multiple-wills-across-regions.html"><span class="v24-tag">多份遺囑</span><strong>家中找到幾份遺囑，先怎樣排時間線</strong><p>保留原件，逐項比較內容，再處理內地房產收件。</p></a>',
    ),
    "articles/macau/index_cn.html": (
        "/articles/am/multiple-wills-across-regions_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">多份遗嘱</span><h3>家里找到几份遗嘱，先怎样排时间线</h3><p>保留原件，逐项比较内容，再处理内地房产材料。</p></div><a class="v25-pill-action" href="/articles/am/multiple-wills-across-regions_cn.html">阅读文章</a></article>',
    ),
    "articles/macau/index_en.html": (
        "/articles/am/multiple-wills-across-regions_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Several wills</span><h3>Several wills and Mainland property: build the timeline first</h3><p>Preserve the originals, compare each provision and then check the property file.</p></div><a class="v25-pill-action" href="/articles/am/multiple-wills-across-regions_en.html">Read Article</a></article>',
    ),
    "articles/singapore/index.html": (
        "/articles/singapore/unknown-mainland-bank-accounts.html",
        '<a href="/articles/singapore/unknown-mainland-bank-accounts.html"><span class="v24-tag">存款線索</span><strong>不知道存款在哪家內地銀行，先怎樣找線索</strong><p>從文件和交易痕跡找機構，再逐家確認查詢要求。</p></a>',
    ),
    "articles/singapore/index_cn.html": (
        "/articles/singapore/unknown-mainland-bank-accounts_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">存款线索</span><h3>不知道存款在哪家内地银行，先怎样找线索</h3><p>从文件和交易痕迹寻找机构，再逐家确认查询要求。</p></div><a class="v25-pill-action" href="/articles/singapore/unknown-mainland-bank-accounts_cn.html">阅读文章</a></article>',
    ),
    "articles/singapore/index_en.html": (
        "/articles/singapore/unknown-mainland-bank-accounts_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Bank clues</span><h3>The Mainland bank is unknown: where a Singapore family can start</h3><p>Follow document and transaction clues, then ask each likely institution about its enquiry route.</p></div><a class="v25-pill-action" href="/articles/singapore/unknown-mainland-bank-accounts_en.html">Read Article</a></article>',
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
