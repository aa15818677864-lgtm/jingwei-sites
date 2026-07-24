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
        "slug": "original-will-verification",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_SG",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡與內地遺產",
                "title": "新加坡原始遺囑為甚麼要先保管好，掃描件能說明多少",
                "description": "新加坡家屬整理內地遺產時，先分清原始遺囑和掃描件各自能做甚麼，原件找不到時又應保存哪些線索。",
                "lead": "先不要在遺囑原件上寫字、釘裝或過膠。掃描件可以幫家屬先看清內容，但普通的法院核對仍要看原件。",
                "key_title": "先記住三件事",
                "keys": [
                    "原件先保全，掃描和寄送可以稍後安排",
                    "掃描件能保存內容，不等於已經核對原件",
                    "找不到原件時，保留副本和尋找經過都很重要",
                ],
                "answer_title": "先說最直接的答案",
                "answer": [
                    "新加坡的一般遺囑認證程序會核對實體原件，家屬持有的普通掃描件不能直接代替這一步。不過，掃描件仍然很有用：它可以先確認立遺囑人、執行人、見證人、簽署日期、頁數和有沒有附加文件，讓家屬知道下一步應向誰查問。",
                    "如果原件一時找不到，不代表掃描件完全沒有價值，也不代表法院一定接受副本。這時已經不是普通的文件整理，家屬要保存副本、保管線索和尋找經過，再判斷是否需要走另一條以副本證明遺囑內容的程序。",
                ],
                "sections": [
                    (
                        "先做的不是寄件，而是保全原件",
                        [
                            "先拍下遺囑現時放在哪個信封、文件夾或保險箱，再記錄由誰取出、誰保管和共有多少頁。如果另有修改遺囑的文件，也要分別拍照和編號。原件應平放、保持乾燥，不要在空白處寫註記，也不要重新釘裝、拆釘或過膠。",
                            "如要交給律師或其他人核對，先做一份清晰掃描和交接記錄。寄送原件前再確認收件人、用途、追蹤方式和退回安排。家屬越早把保管經過記清楚，日後越容易回答原件有沒有被改動、缺頁或由誰接觸過。",
                        ],
                    ),
                    (
                        "掃描件可以先完成哪些工作",
                        [
                            "先逐頁看姓名、日期、簽名、見證人和頁碼，並核對有沒有提到另一份附件或較後日期的修改文件。掃描件也可以用來向家屬確認名字、尋找原來協助立遺囑的人，以及請內地接收方先說明它真正需要哪一類文件。",
                            "掃描件的邊界也要說清楚。它通常不能單靠畫面證明紙張就是原件、簽名沒有後來變動、所有頁面都完整，或原件仍然存在。因此，家屬可以用掃描件先整理問題，但不要在沒有核對原件的情況下對外說遺囑已經完成驗證。",
                        ],
                    ),
                    (
                        "原件找不到時，問題已不是普通文件整理",
                        [
                            "先回想原件最後一次由誰看過、是否交給律師或保管機構、是否放在家中保險箱，以及搬家、清理遺物或郵寄時有沒有交接。保存電郵、短訊、收據、舊掃描、信封照片和與見證人的聯絡線索，不要只留一句『找不到』。",
                            "新加坡程序容許在特定情況下申請以副本或其他證據說明遺囑內容，但要交代原件為何不在、遺囑曾經存在、內容是否準確，以及有沒有被撤回或毀棄的疑問。這不是把普通掃描件上載便完成。",
                            "如果原件其實由境外法院或機關保管，該機關出具、確認與所存原件一致的副本又屬另一種情況。應按原件去向和現有證據判斷路徑。",
                        ],
                    ),
                    (
                        "交到內地前，仍要分開兩組問題",
                        [
                            "新加坡遺囑和法院文件主要回答誰被指定處理遺產、遺囑內容怎樣得到確認。內地房產、存款或公司權益，則要另外核對登記人、城市、資產狀態、可能涉及的家屬和實際接收單位。新加坡文件辦好，不等於內地資產已經轉名。",
                            "先向內地接收方說清楚資產是甚麼、在哪個城市、現時要證明的是遺囑內容還是代表權限，再問它需要原件、核證副本、翻譯或其他形式。不要在用途未清楚前反覆寄送原件。",
                        ],
                    ),
                    (
                        "做一張原件保管記錄",
                        [
                            "一頁紙寫下：原件保管人、保管地點、遺囑日期、總頁數、見證人、附加文件、現時狀況、掃描日期和曾經接觸原件的人。再加一欄記錄仍待確認的姓名差異、缺頁、手寫改動或附件。",
                            "這張記錄不替代法院文件，但能讓家屬、律師和內地接收方看到同一組事實。若原件完整，便按正常路徑準備；若有缺頁、改動或原件失蹤，則先保全證據，再決定是否需要處理特殊程序。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "有遺囑和無遺囑的法院文件有甚麼不同"),
                    ("/articles/singapore/singapore-death-certificate.html", "新加坡死亡證明交到內地前先核對甚麼"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "內地房產有沒有列入新加坡資產清單"),
                ],
                "cta": "說明原件現在哪裡、由誰保管、有沒有清晰掃描，以及內地涉及哪一項資產，才容易判斷下一步。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡与内地遗产",
                "title": "新加坡原始遗嘱为什么要先保管好，扫描件能说明多少",
                "description": "新加坡家属整理内地遗产时，先分清原始遗嘱和扫描件分别能做什么，原件找不到时又应保存哪些线索。",
                "lead": "先不要在遗嘱原件上写字、装订或过塑。扫描件能帮助家属先看清内容，但普通的法院核对仍然要看原件。",
                "key_title": "先记住三件事",
                "keys": [
                    "原件先保全，扫描和寄送可以稍后安排",
                    "扫描件能保存内容，不等于已经核对原件",
                    "找不到原件时，副本和寻找经过都要保存",
                ],
                "answer_title": "先说最直接的答案",
                "answer": [
                    "新加坡的一般遗嘱认证程序会核对实物原件，家属持有的普通扫描件不能直接替代这一步。不过，扫描件仍然很有用：可以先确认立遗嘱人、执行人、见证人、签署日期、页数和有没有附加文件，让家属知道下一步应该向谁询问。",
                    "如果原件一时找不到，不表示扫描件完全没用，也不表示法院一定接受副本。这时已经不只是普通文件整理，家属要保存副本、保管线索和寻找经过，再判断是否需要通过另一种程序证明遗嘱内容。",
                ],
                "sections": [
                    (
                        "先做的不是寄件，而是保全原件",
                        [
                            "先拍下遗嘱目前放在哪个信封、文件夹或保险箱，再记录由谁取出、谁保管和一共有多少页。如果另有修改遗嘱的文件，也要分别拍照、编号。原件应平放、保持干燥，不要在空白处写备注，也不要重新装订、拆钉或过塑。",
                            "如需交给律师或其他人核对，先做一份清晰扫描和交接记录。寄送原件前，再确认收件人、用途、追踪方式和退回安排。越早记清保管经过，日后越容易回答原件有没有被改动、缺页或由谁接触过。",
                        ],
                    ),
                    (
                        "扫描件可以先完成哪些工作",
                        [
                            "先逐页看姓名、日期、签名、见证人和页码，并核对有没有提到其他附件或日期更晚的修改文件。扫描件也可以用于向家属确认名字、寻找当初协助立遗嘱的人，以及请内地接收方先说明它真正需要哪类文件。",
                            "扫描件的边界也要说清。它通常不能只凭画面证明纸张就是原件、签名没有后来变动、所有页面都完整，或者原件仍然存在。因此，家属可以用扫描件先整理问题，但不要在没有核对原件时对外说遗嘱已经完成验证。",
                        ],
                    ),
                    (
                        "原件找不到时，问题已经不是普通文件整理",
                        [
                            "先回想原件最后由谁看过，是否交给律师或保管机构，是否放在家中保险箱，以及搬家、整理遗物或邮寄时有没有交接。保存邮件、短信、收据、旧扫描、信封照片和见证人的联络线索，不要只留一句‘找不到’。",
                            "新加坡程序在特定情况下允许申请用副本或其他证据说明遗嘱内容，但需要交代原件为什么不在、遗嘱是否曾经存在、内容是否准确，以及有没有被撤回或毁损的疑问。这不是上传普通扫描件就能完成。",
                            "如果原件实际由境外法院或机构保管，该机构出具、确认与所存原件一致的副本又属于另一种情况。应当根据原件去向和现有证据判断路径。",
                        ],
                    ),
                    (
                        "交到内地前，仍要分开两组问题",
                        [
                            "新加坡遗嘱和法院文件主要回答谁被指定处理遗产、遗嘱内容怎样得到确认。内地房产、存款或公司权益，则要另外核对登记人、城市、资产状态、可能涉及的家属和实际接收单位。新加坡文件办好，不等于内地资产已经转名。",
                            "先向内地接收方说清楚资产是什么、在哪个城市、现在要证明的是遗嘱内容还是代表权限，再问它需要原件、核证副本、翻译或其他形式。不要在用途不清楚时反复寄送原件。",
                        ],
                    ),
                    (
                        "做一张原件保管记录",
                        [
                            "用一页纸写下原件保管人、保管地点、遗嘱日期、总页数、见证人、附加文件、目前状况、扫描日期和接触过原件的人。再加一栏，记录仍待确认的姓名差异、缺页、手写改动或附件。",
                            "这张记录不能替代法院文件，但能让家属、律师和内地接收方看到同一组事实。原件完整时按普通路径准备；如有缺页、改动或原件失踪，则先保全证据，再判断是否需要处理特殊程序。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "有遗嘱和无遗嘱的法院文件有什么不同"),
                    ("/articles/singapore/singapore-death-certificate_cn.html", "新加坡死亡证明交到内地前先核对什么"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "内地房产有没有列入新加坡资产清单"),
                ],
                "cta": "说明原件现在在哪里、由谁保管、有没有清晰扫描，以及内地涉及哪项资产，才容易判断下一步。",
            },
            "en": {
                "lang": "en",
                "locale": "en_SG",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore and Mainland estates",
                "title": "Why the Original Singapore Will Matters, and What a Scan Can Still Tell You",
                "description": "A practical guide to preserving an original Singapore will, using a scan responsibly and recording evidence if the original cannot be found.",
                "lead": "Do not write on, laminate or re-staple the original will. A scan can answer useful preliminary questions, but ordinary probate verification still involves the physical original.",
                "key_title": "Three points to remember",
                "keys": [
                    "Preserve the original before arranging delivery",
                    "A scan records content but is not verification of the original",
                    "If the original is missing, preserve the search trail as well as the copy",
                ],
                "answer_title": "The short answer",
                "answer": [
                    "In an ordinary Singapore probate application, the physical original will is presented for verification. A family's ordinary scan does not replace that step. It is still valuable: it can identify the testator, executor, witnesses, execution date, page count and any codicil, meaning a later document that changes the will. The family can then ask focused questions before moving papers across borders.",
                    "A missing original does not make the scan worthless, and it does not mean that the court will automatically accept a copy. It changes the problem. The family should preserve the copy, the custody history and evidence of its search, then assess whether a separate application concerning the will's contents is required.",
                ],
                "sections": [
                    (
                        "Preserve the document before sending it anywhere",
                        [
                            "Photograph the envelope, folder, safe or other place where the will was found. Record who removed it, who now holds it and the number of pages. Photograph and number every codicil separately. Keep the paper flat and dry. Do not add notes, remove or replace staples, or laminate it.",
                            "Before giving the original to a lawyer or another reviewer, make a clear scan and a custody note. Before posting it, confirm the recipient, purpose, tracked delivery and return arrangements. A simple custody record can later answer whether pages were missing, markings changed or several people handled the document.",
                        ],
                    ),
                    (
                        "What a scan can help the family do",
                        [
                            "Review each page for names, dates, signatures, witnesses and page numbers. Check for references to an attachment or a later codicil. The scan can also help relatives confirm identities, locate the person who prepared the will and ask a Mainland recipient what evidence it actually requires.",
                            "A scan normally cannot establish by appearance alone that the paper is the original, every page is present, no later alteration exists or the original still survives. Use it to organise the enquiry, but do not describe the will as verified before the original or the appropriate evidence has been examined.",
                        ],
                    ),
                    (
                        "When the original cannot be found",
                        [
                            "Reconstruct the last known custody. Ask who last saw the original, whether a lawyer or storage service held it, and what happened during a move, house clearance or delivery. Keep emails, messages, receipts, earlier scans, envelope photographs and witness contact details. A bare statement that the document is missing explains very little.",
                            "Singapore procedure allows a copy or other evidence of a will's contents to be considered in specific circumstances. The evidence must address why the original is unavailable, whether it continued to exist, whether the copy is accurate and whether revocation or destruction is in issue. This is not an ordinary upload of a family scan.",
                            "An original retained by a foreign court or authority raises a different route involving a copy certified against the document held there. The route depends on where the original is and what evidence is available.",
                        ],
                    ),
                    (
                        "Keep the Singapore and Mainland questions separate",
                        [
                            "The Singapore will and court papers help establish the testamentary plan and authority to administer the estate. A Mainland home, bank balance or company interest still requires its own ownership, location, family and recipient checks. Completing the Singapore process does not itself change a Mainland title record.",
                            "Tell the Mainland recipient what the asset is, where it is located and whether the current question concerns the will's contents or a representative's authority. Only then ask whether it needs an original, certified copy, translation or another form. Repeatedly sending the original before the purpose is clear creates unnecessary risk.",
                        ],
                    ),
                    (
                        "Make a one-page custody record",
                        [
                            "List the custodian, storage place, will date, total pages, witnesses, codicils, physical condition, scan date and everyone who has handled the original. Add a separate line for name differences, missing pages, handwritten changes or unexplained attachments.",
                            "The record is not a court document. Its value is practical: the family, lawyer and Mainland recipient begin with the same facts. An intact original can follow the ordinary preparation route. Missing pages, alterations or a lost original should trigger evidence preservation before any special application is considered.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling Mainland estates"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate or letters of administration"),
                    ("/articles/singapore/singapore-death-certificate_en.html", "Checks for a Singapore death certificate"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "A Mainland property in the Schedule of Assets"),
                ],
                "cta": "Tell us where the original is, who holds it, whether a clear scan exists and which Mainland asset is involved. Those facts usually identify the next question.",
            },
        },
    },
    {
        "slug": "state-or-federal-apostille",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國與內地遺產",
                "title": "美國州文件和聯邦文件，Apostille 應該交給誰辦",
                "description": "美國文件交到內地前，先按實際簽發機關分清州、地方、聯邦和聯邦法院文件，再選擇相應的 Apostille 路徑。",
                "lead": "辦理路徑跟文件由誰簽發有關，不是看申請人住在哪一州，也不是看文件將寄去哪個城市。",
                "key_title": "先看三個地方",
                "keys": [
                    "文件頂部的簽發機關和州名",
                    "簽署人的姓名、職務和印章",
                    "內地接收方要用文件證明甚麼",
                ],
                "answer_title": "先說最直接的判斷方法",
                "answer": [
                    "先看文件由哪一級機關或哪一名公職人員簽發。州和地方公共文件，一般由所屬州指定的機關處理；聯邦機關文件通常走聯邦層級；聯邦法院文件則可能由該法院的書記官體系處理。不要只憑『這是一份法院文件』或『申請人住在加州』來決定送件地點。",
                    "Apostille（通常中文稱為附加證明）主要確認簽名、簽署身份和印章來源，不會替家屬證明文件內容一定真實、某人一定是內地繼承人，或內地房產一定可以過戶。選對辦理機關只是其中一步，文件版本和內地用途也要同時核對。",
                ],
                "sections": [
                    (
                        "先把文件分成三類",
                        [
                            "先問一句：誰在這張紙上以官方身份簽名？把完整簽發機關、簽署人職務、州名和日期抄下來，再分類。",
                            "州或地方保存的死亡記錄、部分州法院文件，通常屬州或地方文件。聯邦機關或聯邦公職人員簽發的文件屬另一類。聯邦法院文件也要單獨看，不能因為有『Federal』字樣便一概寄往同一辦公室。",
                            "如果文件只是一張普通影印件，或看不清簽名和印章，先向簽發處詢問可供外地使用的正式版本。不要先找公證人把每份政府文件重新公證；錯誤地在原始聯邦文件上再做公證，反而可能令文件不能按原來路徑處理。",
                        ],
                    ),
                    (
                        "公證人文件和政府簽發文件不要混在一起",
                        [
                            "私人聲明、授權書或翻譯件，可能先由公證人見證簽署，再按該州規則核對公證人資格。死亡記錄、法院核證副本和聯邦機關文件，本身已有簽發人和印章，準備方法並不相同。看到『Notary』或『Certified Copy』幾個字，仍要讀完整證明頁。",
                            "有些州在 Apostille 前還有縣級或其他核對步驟，有些沒有；聯邦文件也有自己的版本和簽名要求。最穩妥的做法不是套用朋友的清單，而是按文件實際來源查當前要求。",
                        ],
                    ),
                    (
                        "送件前用六項資料核對路徑",
                        [
                            "列出：文件正式名稱、簽發機關、簽署人職務、簽發州或聯邦來源、現有版本是原件還是核證副本、準備在內地用來做甚麼。若是法院文件，再加法院全名和案件編號；若是死亡記錄，再看具體由哪一州或地方記錄機關出具。",
                            "把這一頁同時交給美國辦理機關和內地接收方核對。前者回答文件可否由它加 Apostille，後者回答這個版本能不能用於目前的內地程序。兩邊都得到明確答案後，再安排翻譯、付款和寄送。",
                        ],
                    ),
                    (
                        "Apostille 沒有替你證明甚麼",
                        [
                            "它不判斷遺囑是否有效、不確認遺產如何分配，也不證明一名美國遺產代表自然有權處理某套內地房產。姓名、家屬關係、代表權限和內地資產登記，仍要由各自的文件和實際程序回答。",
                            "如果文件姓名與內地登記不同、法院任命有限制、房產多人共有或有家屬爭議，不能靠多辦一張 Apostille 補上缺口。先把差異和爭議列清楚，再判斷要補哪一組證據。",
                        ],
                    ),
                    (
                        "最省時間的準備順序",
                        [
                            "第一步，問內地接收方需要證明的具體事項。第二步，向原簽發處取得合適的原件或核證副本。第三步，按簽發機關判斷州、聯邦或聯邦法院路徑。第四步，核對姓名和日期後再翻譯。第五步，保留送件表、付款和追蹤記錄。",
                            "若手上同時有死亡記錄、遺囑、法院命令和代表任命文件，不要綁成一套一起辦。逐份寫明簽發來源和內地用途，因為同一個家庭的幾份文件可以分別走不同路徑。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/issuing-state-matters.html", "美國文件先看由哪一級機關簽發"),
                    ("/articles/us/us-documents-mainland-property-inheritance.html", "死亡證明和遺囑用於內地房產前先核對甚麼"),
                    ("/articles/us/letters-testamentary-or-administration.html", "兩種常見法院任命文件分別說明甚麼"),
                ],
                "cta": "把文件首頁、簽名印章頁、簽發州和內地用途放在一起，才可以準確判斷應走哪條路徑。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国与内地遗产",
                "title": "美国州文件和联邦文件，Apostille 应该交给谁办",
                "description": "美国文件交到内地前，先按实际签发机构分清州、地方、联邦和联邦法院文件，再选择相应的 Apostille 路径。",
                "lead": "办理路径取决于文件由谁签发，不是看申请人住在哪个州，也不是看文件准备寄到哪个城市。",
                "key_title": "先看三个位置",
                "keys": [
                    "文件顶部的签发机构和州名",
                    "签字人的姓名、职务和印章",
                    "内地接收方要用文件证明什么",
                ],
                "answer_title": "先说最直接的判断方法",
                "answer": [
                    "先看文件由哪一级机构或哪位公职人员签发。州和地方公共文件，一般由所在州指定的机构处理；联邦机构文件通常走联邦层级；联邦法院文件则可能由该法院的书记官体系处理。不要只凭‘这是一份法院文件’或‘申请人住在加州’决定送件地点。",
                    "Apostille（通常中文称为附加证明）主要确认签名、签署身份和印章来源，不会替家属证明文件内容一定真实、某人一定是内地继承人，或者内地房产一定可以过户。选对办理机构只是其中一步，文件版本和内地用途也要同时核对。",
                ],
                "sections": [
                    (
                        "先把文件分成三类",
                        [
                            "先问一句：谁在这张纸上以官方身份签字？把完整签发机构、签字人职务、州名和日期抄下来，再进行分类。",
                            "州或地方保存的死亡记录、部分州法院文件，通常属于州或地方文件。联邦机构或联邦公职人员签发的文件属于另一类。联邦法院文件也要单独看，不能因为带有‘Federal’字样就一概寄往同一个办公室。",
                            "如果文件只是一张普通复印件，或者签名和印章看不清，先向签发处询问可供境外使用的正式版本。不要先找公证人把每份政府文件重新公证；错误地在原始联邦文件上再做公证，反而可能让文件无法按原来的路径处理。",
                        ],
                    ),
                    (
                        "公证人文件和政府签发文件不要混在一起",
                        [
                            "私人声明、授权书或翻译件，可能先由公证人见证签署，再按该州规则核对公证人资格。死亡记录、法院核证副本和联邦机构文件，本身已经有签发人和印章，准备方法并不相同。看到‘Notary’或‘Certified Copy’几个字，仍要读完整的证明页。",
                            "有些州在 Apostille 前还有县级或其他核对步骤，有些没有；联邦文件也有自己的版本和签名要求。最稳妥的办法不是套用朋友的清单，而是按照文件实际来源核对当前要求。",
                        ],
                    ),
                    (
                        "送件前用六项资料核对路径",
                        [
                            "列出文件正式名称、签发机构、签字人职务、签发州或联邦来源、现有版本是原件还是核证副本、准备在内地用来做什么。法院文件再加法院全名和案件编号；死亡记录再看具体由哪个州或地方记录机构出具。",
                            "把这一页同时交给美国办理机构和内地接收方核对。前者回答文件能否由它加 Apostille，后者回答这个版本能不能用于目前的内地程序。两边都给出明确答复后，再安排翻译、付款和寄送。",
                        ],
                    ),
                    (
                        "Apostille 没有替你证明什么",
                        [
                            "它不判断遗嘱是否有效，不确认遗产怎样分配，也不证明一名美国遗产代表自然有权处理某套内地房产。姓名、家属关系、代表权限和内地资产登记，仍要由各自的文件和实际程序回答。",
                            "如果文件姓名与内地登记不同、法院任命有限制、房产多人共有或有家属争议，不能靠多办一张 Apostille 补上缺口。先把差异和争议列清楚，再判断要补哪一组证据。",
                        ],
                    ),
                    (
                        "最省时间的准备顺序",
                        [
                            "第一步，问内地接收方需要证明的具体事项。第二步，向原签发处取得合适的原件或核证副本。第三步，按签发机构判断州、联邦或联邦法院路径。第四步，核对姓名和日期后再翻译。第五步，保留送件表、付款和追踪记录。",
                            "如果手上同时有死亡记录、遗嘱、法院命令和代表任命文件，不要绑成一套一起办理。逐份写明签发来源和内地用途，因为同一个家庭的几份文件可能分别走不同路径。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/issuing-state-matters_cn.html", "美国文件先看由哪一级机构签发"),
                    ("/articles/us/us-documents-mainland-property-inheritance_cn.html", "死亡证明和遗嘱用于内地房产前先核对什么"),
                    ("/articles/us/letters-testamentary-or-administration_cn.html", "两种常见法院任命文件分别说明什么"),
                ],
                "cta": "把文件首页、签名印章页、签发州和内地用途放在一起，才可以准确判断应该走哪条路径。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / United States and Mainland estates",
                "title": "State or Federal Document? Choose the Right U.S. Apostille Route",
                "description": "A practical guide to identifying state, local, federal agency and federal court documents before choosing a U.S. apostille route for Mainland use.",
                "lead": "The route follows the issuing authority, not the applicant's home state and not the city where the document will eventually be used.",
                "key_title": "Start with three details",
                "keys": [
                    "The issuing authority and state shown on the document",
                    "The signer's printed name, title and seal",
                    "The fact the Mainland recipient needs the document to prove",
                ],
                "answer_title": "A practical way to choose the route",
                "answer": [
                    "Begin with the authority or official who issued the document. State and local public records generally use the designated authority for the relevant state. Federal agency documents usually follow the federal route. Federal court records may be handled through the issuing court's clerk system. A document is not routed by the applicant's address, and the word 'court' alone is not enough to choose an office.",
                    "An apostille is a certificate addressing the origin of a public document, including the signature, official capacity and seal. It does not establish that every statement is true, identify a Mainland heir or guarantee a property transfer. The correct office, an acceptable document version and the Mainland recipient's purpose all need to align.",
                ],
                "sections": [
                    (
                        "Sort the documents by their actual source",
                        [
                            "Start with one plain question: who signed this paper in an official capacity? Record the full issuer, signer's title, state and date before choosing a category.",
                            "A vital record held by a state or local office and many state-court records are state or local documents. A record signed by a federal agency or official belongs to a different group. Federal-court records need their own check and should not be sent automatically to one central office merely because the heading says 'Federal'.",
                            "If the family has only an ordinary photocopy, or the signature and seal are unclear, ask the issuing office which official version is available for overseas use. Do not begin by notarising every government record. Adding a notarial act to an original federal public document can make it unsuitable for its proper route.",
                        ],
                    ),
                    (
                        "Do not treat a notarised paper and a public record as the same thing",
                        [
                            "A private declaration, power of attorney or translated statement may first be signed before a notary and then pass through the steps required by that state. A vital record, certified court copy or federal agency document already has its own issuer and seal. The words 'Notary' or 'Certified Copy' do not answer the question unless the complete certificate is read.",
                            "Some states require an additional county or other verification step for particular documents; others do not. Federal records have their own version and signature requirements. Use the document's true source and the current instructions of the responsible office, rather than another family's checklist.",
                        ],
                    ),
                    (
                        "Use six facts to check the route before paying",
                        [
                            "List the formal document name, issuing authority, signer's title, state or federal source, whether the family has an original or certified copy, and the precise Mainland purpose. For a court record, add the full court and case number. For a death record, identify the state or local records office that issued it.",
                            "Send that page to both the U.S. office and the Mainland recipient. The U.S. office can confirm whether it is responsible for the apostille. The recipient can confirm whether that document version addresses the current Mainland procedure. Arrange translation, payment and delivery only after both questions are answered.",
                        ],
                    ),
                    (
                        "What an apostille does not prove",
                        [
                            "It does not decide whether a will is valid, how an estate must be divided, or whether a U.S. personal representative can deal with a particular Mainland home. Identity, family relationship, representative authority and Mainland title each require their own evidence and procedural checks.",
                            "A name mismatch, restricted court appointment, co-owned property or family dispute is not cured by obtaining another apostille. Record the discrepancy or dispute first, then identify the missing evidence instead of treating authentication as a complete answer.",
                        ],
                    ),
                    (
                        "A preparation order that avoids repeat work",
                        [
                            "First, ask what the Mainland recipient needs proved. Second, obtain the appropriate original or certified copy from the issuer. Third, identify the state, federal agency or federal-court route from the issuer and signer. Fourth, compare names and dates before translating. Fifth, retain the application, payment and tracking record.",
                            "A family may hold a death record, will, court order and appointment document at the same time. Do not bind them into one packet and assume they share a route. Record the source and Mainland purpose of each document because several papers in one estate may require different offices.",
                        ],
                    ),
                ],
                "related_title": "Continue with the United States topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling Mainland estates"),
                    ("/articles/us/issuing-state-matters_en.html", "Start with the authority that issued the U.S. document"),
                    ("/articles/us/us-documents-mainland-property-inheritance_en.html", "Using U.S. death and will documents for a Mainland property"),
                    ("/articles/us/letters-testamentary-or-administration_en.html", "Letters Testamentary or Letters of Administration"),
                ],
                "cta": "Place the first page, signature and seal page, issuing state and Mainland purpose side by side before choosing an apostille route.",
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
    "articles/singapore/index.html": {
        "href": "/articles/singapore/original-will-verification.html",
        "card": '<a href="/articles/singapore/original-will-verification.html"><span class="v24-tag">遺囑原件</span><strong>新加坡原始遺囑為甚麼要先保管好，掃描件能說明多少</strong><p>掃描件可先看內容和找線索，但不能直接代替法院核對原件。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/singapore/index_cn.html": {
        "href": "/articles/singapore/original-will-verification_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">遗嘱原件</span><h3>新加坡原始遗嘱为什么要先保管好，扫描件能说明多少</h3><p>扫描件可以先看内容、找线索，但不能直接替代法院核对原件。</p></div><a class="v25-pill-action" href="/articles/singapore/original-will-verification_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index_en.html": {
        "href": "/articles/singapore/original-will-verification_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Original will</span><h3>Why the original Singapore will should be preserved</h3><p>A scan preserves clues, but it does not simply replace the original for probate verification.</p></div><a class="v25-pill-action" href="/articles/singapore/original-will-verification_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index.html": {
        "href": "/articles/us/state-or-federal-apostille.html",
        "card": '<a href="/articles/us/state-or-federal-apostille.html"><span class="v24-tag">文件證明</span><strong>美國州文件和聯邦文件，Apostille 應該交給誰辦</strong><p>先看簽發機關，不要按申請人住在哪一州猜辦理路徑。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/united-states/index_cn.html": {
        "href": "/articles/us/state-or-federal-apostille_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">文件证明</span><h3>美国州文件和联邦文件，Apostille 应该交给谁办</h3><p>先看签发机构，不要按申请人住在哪个州猜办理路径。</p></div><a class="v25-pill-action" href="/articles/us/state-or-federal-apostille_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index_en.html": {
        "href": "/articles/us/state-or-federal-apostille_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Apostille route</span><h3>State or federal document: choose the right route</h3><p>Follow the issuing authority, not the applicant\'s address.</p></div><a class="v25-pill-action" href="/articles/us/state-or-federal-apostille_en.html">Read Article</a></article>',
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
    for hub in ("singapore", "united-states"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, f"{SITE}/articles/{hub}/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
