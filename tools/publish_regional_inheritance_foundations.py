from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-07-24"
SITE = "https://www.jingwei-law.com"


ARTICLES = [
    {
        "slug": "macau-family-mainland-property-inheritance",
        "directory": "articles/am",
        "topic": "macau",
        "topic_urls": {"tc": "/articles/macau/", "cn": "/articles/macau/index_cn.html", "en": "/articles/macau/index_en.html"},
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門繼承",
                "title": "澳門家屬繼承內地房產，先分清兩套文件",
                "description": "澳門家屬處理內地房產繼承時，先分清證明繼承人身份的澳門文件，以及內地房產過戶要核對的資料。",
                "lead": "手上有澳門死亡證明或繼承人資格文件，不等於已經備齊內地房產過戶資料。",
                "key_title": "先記住三件事",
                "keys": ["澳門文件先回答誰是繼承人", "內地資料再回答房子怎樣登記", "先問房產所在地，再決定文件怎樣準備"],
                "visuals": [
                    ("兩套文件不要混在一起", "澳門文件", "內地房產資料", "先分清用途，才知道缺哪一張。"),
                    ("先核對，再準備", "身份與關係", "房屋與城市", "接收要求", "不要一開始把所有文件重做。"),
                    ("第一次整理清單", "死亡與親屬資料", "遺囑或繼承文件", "房產地址與登記人", "姓名差異與翻譯", "一頁表格能省下多次往返。"),
                ],
                "answer_title": "先把答案說清楚",
                "answer": [
                    "不能只拿一份澳門繼承文件，就假定可以直接把內地房產轉到家屬名下。澳門文件主要用來說明死亡、親屬關係、遺囑或哪些人具有繼承人身份；內地房產過戶還要另外核對房屋在哪個城市、登記在誰名下、是否共有、是否有抵押，以及當地接收材料的具體要求。",
                    "最省時間的做法，是先把文件分成兩疊：一疊證明人和關係，一疊證明房子和登記情況。兩邊對得上，才決定哪些澳門文件需要正本、翻譯或進一步證明。",
                ],
                "sections": [
                    ("先確認房子和家人的四個基本事實", [
                        "第一，房子位於哪個內地城市，房產證或舊合同上的地址是否一致。第二，登記人是不是已故家屬，還是夫妻或多人共有。第三，家人之間對繼承人和分配有沒有爭議。第四，已故家屬生前主要居住在哪裏，有沒有遺囑或其他安排。",
                        "這四件事會改變後面的路徑。房子若不是完整登記在已故家屬名下，先要分清真正進入遺產的是哪一部分；有人反對、失聯或文件說法不一致時，也不能把無爭議的文件準備方式硬套上去。",
                    ]),
                    ("澳門文件按用途整理，不要只看文件名稱", [
                        "第一組是死亡資料，用來確認何人、何時離世。第二組是親屬與身份資料，例如婚姻、出生、收養或姓名變更記錄。第三組是繼承資料，包括遺囑、繼承人資格文件或已有的裁判文件。第四組是每名家屬目前使用的身份證明。",
                        "澳門的繼承人資格文件通常着重確認哪些人具有繼承身份，但它不會替你查清一套內地房屋的登記狀態。反過來，內地房產證也不會說明澳門家屬之間的完整親屬關係。把每張文件旁邊寫上「它證明甚麼」，比只列一串文件名稱更有用。",
                    ]),
                    ("翻譯和證明先問用途，再安排", [
                        "澳門文件可能使用中文或葡文，也可能夾有其他地區簽發的資料。準備交到內地前，先把接收單位、用途和文件語言說清楚。需要翻譯時，姓名、日期、證件號碼、地址和印章文字要逐項對照，不能只看大意。",
                        "有些澳門文件可以核驗真偽，但能核驗不代表任何城市、任何程序都會自動接受同一份材料。最穩妥的順序，是先拿文件清單和清晰掃描件詢問房產所在地，再按回覆準備正本、翻譯或其他證明。",
                    ]),
                    ("先問房產所在地的四個問題", [
                        "聯絡房產所在地的登記窗口、公證辦理人員或受託律師時，可以直接問四件事：這類繼承由哪個窗口受理；現有澳門文件分別能否使用；哪些材料必須正本或翻譯；繼承人不能到場時，授權文件要寫到什麼程度。",
                        "不要只問“澳門文件認不認”。把房屋地址、登記人、家屬關係、是否有遺囑和現有文件名稱一起說明，對方才可能給出有用的材料方向。若需要遠程安排，可再看 <a href=\"/articles/am/macau-client-mainland-lawyer.html\">澳門客戶怎樣整理委託資料</a>。",
                    ]),
                    ("有人不配合或資料缺失時，先停下補證據", [
                        "如果家人對繼承人範圍有爭議、有人拒絕交出房產證、澳門文件與內地登記姓名不一致，或房子多年沒有完整資料，就不要急着承諾“做一份文件便能過戶”。先保存身份、親屬、付款、居住、房屋地址和歷史聯絡記錄，再判斷問題是在文件補充、身份核對，還是已經進入爭議處理。",
                        "現在可以先做三件事：拍清楚每份澳門文件的首頁和簽發信息；列出每名家屬與已故者的關係；找出內地房產證、購房合同或至少一個可核對的地址。這一頁資料準備好後，再去確認具體辦理路徑。",
                    ]),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門專題總覽"),
                    ("/articles/am/macau-client-mainland-lawyer.html", "人在澳門，怎樣委託內地律師處理事情"),
                    ("/articles/hk-mainland-property-inheritance/documents.html", "對照閱讀：香港文件按用途怎樣整理"),
                    ("/articles/hk-mainland-property-inheritance/property-transfer-checklist.html", "內地房產過戶前先核對哪些資料"),
                ],
                "cta": "把澳門文件、家屬關係和內地房屋城市說清楚，我們再判斷先補資料還是先確認接收要求。",
            },
            "cn": {
                "lang": "zh-Hans", "locale": "zh_CN", "brand": "刘毅律师团队", "brand_sub": "跨境中国法律事务", "eyebrow": "文章 / 澳门继承",
                "title": "澳门家属继承内地房产，先分清两套材料", "description": "澳门家属处理内地房产继承时，先分清证明继承人身份的澳门文件，以及内地房产过户要核对的材料。",
                "lead": "手上有澳门死亡证明或继承人资格文件，不等于已经备齐内地房产过户材料。", "key_title": "先记住三件事",
                "keys": ["澳门文件先回答谁是继承人", "内地材料再回答房子怎样登记", "先问房产所在地，再决定文件怎样准备"],
                "visuals": [("两套材料不要混在一起", "澳门文件", "内地房产材料", "先分清用途，才知道缺哪一份。"), ("先核对，再准备", "身份与关系", "房屋与城市", "接收要求", "不要一开始把所有文件重做。"), ("第一次整理清单", "死亡与亲属材料", "遗嘱或继承文件", "房产地址与登记人", "姓名差异与翻译", "一页表格能省下多次往返。")],
                "answer_title": "先把答案说清楚", "answer": ["不能只拿一份澳门继承文件，就认为可以直接把内地房产转到家属名下。澳门文件主要用来说明死亡、亲属关系、遗嘱或哪些人具有继承人身份；内地房产过户还要另外核对房屋所在城市、登记人、共有情况、抵押状态和当地材料要求。", "最省时间的做法，是先把材料分成两组：一组证明人和关系，一组证明房子和登记情况。两边对得上，再决定哪些澳门文件需要原件、翻译或进一步证明。"],
                "sections": [
                    ("先确认房子和家人的四个基本事实", ["第一，房子位于哪个内地城市，房产证或旧合同上的地址是否一致。第二，登记人是不是已故家属，还是夫妻或多人共有。第三，家人之间对继承人和分配有没有争议。第四，已故家属生前主要居住在哪里，有没有遗嘱或其他安排。", "这四件事会改变后面的办理路径。房子如果不是完整登记在已故家属名下，先要分清真正进入遗产的是哪一部分；有人反对、失联或材料说法不一致时，也不能照搬无争议案件的准备方式。"]),
                    ("澳门文件按用途整理，不要只看名称", ["第一组是死亡材料。第二组是亲属与身份材料，例如婚姻、出生、收养或姓名变更记录。第三组是继承材料，包括遗嘱、继承人资格文件或已有的裁判材料。第四组是每名家属现在使用的身份证明。", "澳门的继承人资格文件通常着重确认哪些人具有继承身份，但它不会替你查清内地房屋的登记状态。内地房产证也不会说明澳门家属之间的完整亲属关系。在每份文件旁写上“它证明什么”，比只列一串名称更有用。"]),
                    ("翻译和证明先问用途，再安排", ["澳门文件可能使用中文或葡文，也可能夹有其他地区签发的材料。交到内地前，先把接收单位、用途和文件语言说清楚。需要翻译时，姓名、日期、证件号码、地址和印章文字要逐项核对。", "有些澳门文件可以核验真伪，但能核验不代表所有城市、所有程序都会自动接受同一份材料。先拿材料清单和清晰扫描件询问房产所在地，再按反馈准备原件、翻译或其他证明。"]),
                    ("先问房产所在地四个问题", ["可以直接问：这类继承由哪个窗口受理；现有澳门文件分别能否使用；哪些材料必须原件或翻译；继承人不能到场时，授权文件要写到什么程度。", "不要只问“澳门文件认不认”。把房屋地址、登记人、家属关系、是否有遗嘱和现有文件名称一起说明，才容易得到有用的材料方向。需要远程安排时，可再看 <a href=\"/articles/am/macau-client-mainland-lawyer.html\">澳门客户怎样整理委托材料</a>。"]),
                    ("有人不配合或材料缺失时，先补证据", ["如果家人对继承人范围有争议、有人拒绝交出房产证、澳门文件与内地登记姓名不一致，或房子多年没有完整材料，就不要急着承诺“做一份文件就能过户”。先保存身份、亲属、付款、居住、房屋地址和历史联系记录。", "现在可以先做三件事：拍清楚每份澳门文件的首页和签发信息；列出每名家属与已故者的关系；找出内地房产证、购房合同或至少一个可核对的地址。"]),
                ],
                "related_title": "同一专题继续阅读", "related": [("/articles/macau/index_cn.html", "澳门专题总览"), ("/articles/am/macau-client-mainland-lawyer.html", "人在澳门，怎样委托内地律师处理事情"), ("/articles/hk-mainland-property-inheritance/documents_cn.html", "对照阅读：香港文件按用途怎样整理"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_cn.html", "内地房产过户前先核对哪些材料")],
                "cta": "把澳门文件、家属关系和内地房屋城市说清楚，我们再判断先补材料还是先确认接收要求。",
            },
            "en": {
                "lang": "en", "locale": "en_US", "brand": "Liu Yi Lawyer Team", "brand_sub": "Cross-border Mainland China legal matters", "eyebrow": "Article / Macau inheritance",
                "title": "Inheriting Mainland Property from Macau: Keep the Two Document Files Separate", "description": "A practical first guide for Macau families who need to connect Macau estate documents with a property inheritance in Mainland China.",
                "lead": "A Macau death record or heirship document may identify the family, but it does not by itself complete a Mainland property transfer.", "key_title": "Three points to keep in mind",
                "keys": ["Macau papers establish people and relationships", "Mainland records establish the property position", "Ask the receiving city before remaking documents"],
                "visuals": [("Do not mix the two files", "Macau estate papers", "Mainland property file", "Separate purpose before chasing missing papers."), ("Check before preparing", "Identity and family", "Property and city", "Receiving requirements", "Do not remake every document at the outset."), ("First-pass checklist", "Death and family records", "Will or heirship paper", "Property address and owner", "Name differences and translation", "One clear sheet prevents repeated requests.")],
                "answer_title": "The short answer", "answer": ["Do not assume that one Macau heirship document can transfer a home in Mainland China. Macau documents may establish the death, family relationships, a will, or the identity of the heirs. The Mainland file must separately establish where the property is located, whose name is on the registration, whether the home is jointly owned or mortgaged, and what the receiving office requires.", "The practical starting point is to create two files: one for people and family relationships, and one for the property and its registration history. Once the two files match, you can decide which Macau papers need originals, translation, or further certification."],
                "sections": [
                    ("Confirm four facts before ordering documents", ["Identify the Mainland city and the exact property address. Check whether the deceased was the sole registered owner or shared ownership with a spouse or another person. Record whether the family agrees on the heirs and distribution. Finally, note where the deceased mainly lived and whether any will or prior estate arrangement exists.", "These facts change the route. If the deceased owned only a share, the whole property is not automatically part of the estate. If an heir objects, cannot be found, or the documents conflict, a straightforward non-disputed document route may no longer fit."]),
                    ("Sort Macau papers by what they prove", ["Use four groups: death records; family and identity records; wills, heirship instruments or court papers; and the current identification of each family member. Write one sentence beside every item explaining what it proves.", "A Macau heirship instrument can help identify the heirs, but it does not investigate the registration of a Mainland apartment. A Mainland property certificate does not prove the full family tree in Macau. Both sides of the file are needed."]),
                    ("Plan translation and certification around the destination", ["Macau records may be in Chinese or Portuguese, and the family may also hold papers issued elsewhere. Before arranging translation, identify the receiving office and the intended use. Names, dates, identity numbers, addresses and seals should be checked line by line.", "A document that can be verified online is not automatically accepted for every purpose in every Mainland city. Send a clear scan and a short document list to the receiving side first, then prepare originals, translations or further certification in the form actually requested."]),
                    ("Ask the property city four focused questions", ["Ask which office handles this inheritance, whether each existing Macau document can be used, which items must be original or translated, and what a power of attorney must cover if an heir cannot attend.", "Avoid the vague question, “Are Macau documents accepted?” Give the property address, registered owner, family structure, will status and current document list. For remote arrangements, see <a href=\"/articles/am/macau-client-mainland-lawyer.html\">how a Macau client can organise a Mainland legal instruction</a>."]),
                    ("Pause and preserve evidence when the file does not match", ["Do not promise a quick transfer if relatives dispute the heirs, someone withholds the title papers, names differ across Macau and Mainland records, or only fragments of the property history remain. Preserve identity, family, payment, residence, address and communication records first.", "A useful first task is simple: scan the first page and issuing details of every Macau document, draw the family relationship on one page, and locate the Mainland title certificate, purchase contract or at least one reliable address. That is enough to obtain a meaningful first review."]),
                ],
                "related_title": "Continue with this topic", "related": [("/articles/macau/index_en.html", "Macau topic overview"), ("/articles/am/macau-client-mainland-lawyer.html", "Organising a remote Mainland legal instruction from Macau"), ("/articles/hk-mainland-property-inheritance/documents_en.html", "Comparison: organising Hong Kong documents by purpose"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_en.html", "What to check before a Mainland property transfer")],
                "cta": "Tell us what Macau documents you hold, how the family is related, and where the Mainland property is located. We can then identify the first missing step.",
            },
        },
    },
    {
        "slug": "mainland-property-inheritance",
        "directory": "articles/singapore",
        "topic": "singapore",
        "topic_urls": {"tc": "/articles/singapore/", "cn": "/articles/singapore/index_cn.html", "en": "/articles/singapore/index_en.html"},
        "copy": {
            "tc": {
                "lang": "zh-Hant", "locale": "zh_HK", "brand": "劉毅律師團隊", "brand_sub": "跨境中國法律事務", "eyebrow": "文章 / 新加坡繼承",
                "title": "新加坡遺產文件，可以直接辦內地房產過戶嗎", "description": "新加坡家屬持有遺囑認證或遺產管理文件時，怎樣判斷能否用於內地房產繼承。",
                "lead": "新加坡的遺產文件通常先確認誰有權管理遺產；內地房產過戶仍要另外核對繼承人、房屋和接收要求。", "key_title": "先分清三件事",
                "keys": ["誰有權管理新加坡遺產", "誰有權繼承內地房產", "文件怎樣交到房產所在地"],
                "visuals": [("一份文件，兩個不同問題", "管理遺產的人", "房產最後給誰", "身份和分配不能混為一談。"), ("跨境文件路徑", "新加坡原始文件", "翻譯與附加證明", "內地接收核對", "先確認用途，再辦理文件。"), ("第一次核對清單", "死亡與遺囑", "遺產管理人身份", "內地房產資料", "家屬與姓名差異", "四組資料先對齊。")],
                "answer_title": "先把答案說清楚", "answer": ["通常不能把新加坡的遺囑認證或遺產管理文件，當成內地房產的直接過戶指令。這類文件首先說明誰可以代表遺產處理事務；內地房屋由誰繼承、需要哪些親屬和房產材料，仍要按房屋所在地和家庭實際情況另行核對。", "最容易出錯的地方，是把「有權管理遺產」理解成「房子已經歸這個人」。先分清管理身份、受益或繼承安排、內地不動產登記三層問題，文件才不會做錯方向。"],
                "sections": [
                    ("先看你手上的新加坡文件在回答甚麼", ["有遺囑時，家屬可能持有確認遺囑執行人身份的文件；沒有有效遺囑時，可能是確認遺產管理人身份的文件。兩者都可能附有遺產清單、死亡資料和身份資料，但它們的主要作用，是讓某人可以代表遺產採取行動。", "先把文件首頁、案號、死者姓名、管理人姓名和遺產清單找出來。若內地房屋沒有列在現有清單中，也不代表房屋不存在，更不代表可以跳過內地的房產核對。"]),
                    ("管理人身份和房屋歸屬要分開", ["新加坡文件中被確認的執行人或管理人，可能負責收集資料、聯絡機構和處理遺產，但房屋最終怎樣分配，還要看遺囑內容、家屬關係、房屋登記和適用的處理路徑。", "例如女兒被確認為遺產管理人，不等於內地房屋必然只轉到女兒名下。若還有配偶、其他子女、共有產權或家屬爭議，應先把這些事實列清楚，再討論過戶。"]),
                    ("姓名、證件和遺產清單要逐項對齊", ["新加坡文件上的英文姓名、中文姓名、護照號碼和內地房產登記資料可能不完全一致。常見情況包括拼音順序不同、婚後姓氏變化、舊護照號碼或房產證只寫中文名。", "不要靠一封說明信把所有差異帶過。先做一張姓名對照表，列出每種寫法出現在哪份文件、使用哪個證件號碼、是否有能連接兩種身份的歷史材料。文件中的人物對不上，後面的翻譯和證明做得再完整也可能退回。"]),
                    ("文件用於內地前，先確認三個環節", ["第一，拿到可供使用的正本或經確認的副本。第二，按接收用途安排中文翻譯。第三，根據文件種類和簽發方式，確認是否需要由新加坡指定機構辦理附加證明書。附加證明主要確認簽署或印章的真實性，不替接收單位判斷內容是否足以完成過戶。", "所以順序應是先問內地房產所在地需要哪一類文件，再安排新加坡端的副本、翻譯和證明。不要先把整套材料全部辦完，才發現窗口只需要其中兩份，或姓名仍然對不上。"]),
                    ("這些情況要先做個別判斷", ["如果遺囑涉及多地資產、家屬對遺囑有效性有分歧、死者在新加坡的遺產程序仍未完成、管理人拒絕提供文件，或內地房屋本身存在共有、抵押和占用問題，就不能只研究文件格式。", "現在可先準備四樣資料：新加坡死亡資料；遺囑及管理人文件；一頁家屬關係表；內地房產證、合同或地址線索。再到 <a href=\"/articles/singapore/\">新加坡專題</a> 對照下一步，或先說明目前卡在哪一層。"]),
                ],
                "related_title": "同一專題繼續閱讀", "related": [("/articles/singapore/", "新加坡專題總覽"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist.html", "內地房產過戶前先核對哪些資料"), ("/articles/hk-mainland-property-inheritance/documents.html", "跨境繼承文件怎樣按用途整理"), ("/articles/hk-mainland-property-inheritance/dispute.html", "家屬不配合時，先分清文件問題還是爭議")],
                "cta": "把新加坡遺產文件首頁、家屬關係和內地房產城市說清楚，再判斷文件能否直接使用。",
            },
            "cn": {
                "lang": "zh-Hans", "locale": "zh_CN", "brand": "刘毅律师团队", "brand_sub": "跨境中国法律事务", "eyebrow": "文章 / 新加坡继承",
                "title": "新加坡遗产文件，可以直接办理内地房产过户吗", "description": "新加坡家属持有遗嘱认证或遗产管理文件时，怎样判断能否用于内地房产继承。",
                "lead": "新加坡的遗产文件通常先确认谁有权管理遗产；内地房产过户仍要另外核对继承人、房屋和接收要求。", "key_title": "先分清三件事",
                "keys": ["谁有权管理新加坡遗产", "谁有权继承内地房产", "文件怎样交到房产所在地"],
                "visuals": [("一份文件，两个不同问题", "管理遗产的人", "房产最后给谁", "身份和分配不能混为一谈。"), ("跨境文件路径", "新加坡原始文件", "翻译与附加证明", "内地接收核对", "先确认用途，再办理文件。"), ("第一次核对清单", "死亡与遗嘱", "遗产管理人身份", "内地房产资料", "家属与姓名差异", "四组资料先对齐。")],
                "answer_title": "先把答案说清楚", "answer": ["通常不能把新加坡的遗嘱认证或遗产管理文件，当成内地房产的直接过户指令。这类文件首先说明谁可以代表遗产处理事务；内地房屋由谁继承、需要哪些亲属和房产材料，仍要按房屋所在地和家庭实际情况另行核对。", "最容易出错的地方，是把“有权管理遗产”理解成“房子已经归这个人”。先分清管理身份、受益或继承安排、内地不动产登记三层问题，材料才不会做错方向。"],
                "sections": [
                    ("先看新加坡文件在回答什么", ["有遗嘱时，家属可能持有确认遗嘱执行人身份的文件；没有有效遗嘱时，可能是确认遗产管理人身份的文件。两者都可能附有遗产清单、死亡和身份材料，主要作用是让某人可以代表遗产采取行动。", "先找出文件首页、案号、死者姓名、管理人姓名和遗产清单。内地房屋没有列在现有清单中，不代表房屋不存在，也不代表可以跳过内地房产核对。"]),
                    ("管理人身份和房屋归属要分开", ["新加坡文件中确认的执行人或管理人，可能负责收集资料、联系机构和处理遗产，但房屋最后怎样分配，还要看遗嘱内容、家属关系、房屋登记和适用路径。", "例如女儿被确认为遗产管理人，不等于内地房屋必然只转到女儿名下。如果还有配偶、其他子女、共有产权或家属争议，应先把事实列清楚。"]),
                    ("姓名、证件和遗产清单逐项对齐", ["新加坡文件上的英文姓名、中文姓名、护照号码和内地房产登记资料可能不完全一致。常见情况包括拼音顺序不同、婚后姓氏变化、旧护照号码或房产证只写中文名。", "先做一张姓名对照表，列出每种写法出现在哪份文件、使用哪个证件号码、是否有历史材料能连接两种身份。人物对不上，后面的翻译和证明再完整也可能退回。"]),
                    ("用于内地前，先确认三个环节", ["第一，拿到可供使用的原件或经确认的副本。第二，按接收用途安排中文翻译。第三，根据文件种类和签发方式，确认是否需要由新加坡指定机构办理附加证明书。附加证明主要确认签名或印章，不替接收单位判断内容是否足以过户。", "先问内地房产所在地需要哪类文件，再安排新加坡端的副本、翻译和证明。不要整套办完以后，才发现窗口只需要其中两份，或姓名仍然对不上。"]),
                    ("这些情况要单独判断", ["遗嘱涉及多地资产、家属对遗嘱有效性有分歧、新加坡遗产程序未完成、管理人拒绝提供文件，或内地房屋存在共有、抵押和占用问题时，不能只研究文件格式。", "先准备新加坡死亡资料、遗嘱和管理人文件、一页家属关系表、内地房产证或地址线索。再到 <a href=\"/articles/singapore/index_cn.html\">新加坡专题</a> 对照下一步。"]),
                ],
                "related_title": "同一专题继续阅读", "related": [("/articles/singapore/index_cn.html", "新加坡专题总览"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_cn.html", "内地房产过户前先核对哪些材料"), ("/articles/hk-mainland-property-inheritance/documents_cn.html", "跨境继承文件怎样按用途整理"), ("/articles/hk-mainland-property-inheritance/dispute_cn.html", "家属不配合时，先分清文件问题还是争议")],
                "cta": "把新加坡遗产文件首页、家属关系和内地房产城市说清楚，再判断文件能否直接使用。",
            },
            "en": {
                "lang": "en", "locale": "en_US", "brand": "Liu Yi Lawyer Team", "brand_sub": "Cross-border Mainland China legal matters", "eyebrow": "Article / Singapore inheritance",
                "title": "Can a Singapore Probate Grant Transfer Property in Mainland China?", "description": "How Singapore probate and estate-administration documents fit into a Mainland China property inheritance.",
                "lead": "A Singapore grant may identify the person who can administer an estate. It does not automatically transfer a Mainland property to that person.", "key_title": "Keep three questions separate",
                "keys": ["Who can administer the Singapore estate?", "Who is entitled to the Mainland property?", "What will the property city accept?"],
                "visuals": [("One document, two different questions", "Estate administrator", "Ultimate property owner", "Authority to act is not the same as entitlement."), ("Cross-border document path", "Singapore source paper", "Translation and apostille", "Mainland acceptance check", "Confirm the destination before preparing papers."), ("First review checklist", "Death and will", "Administrator authority", "Mainland property record", "Family and name differences", "Align four information sets first.")],
                "answer_title": "The short answer", "answer": ["A Singapore Grant of Probate or Letters of Administration is not normally a direct instruction to change the registered owner of a property in Mainland China. It first identifies the person authorised to deal with the estate. The heirs, the property title and the receiving city's document requirements still need a separate review.", "The most common mistake is to treat authority to administer the estate as ownership of the property. Keep the administrator's role, the beneficial or inheritance position, and the Mainland registration process as three distinct questions."],
                "sections": [
                    ("Identify what the Singapore document actually establishes", ["Where there is a will, the family may have a grant recognising the executor. Without a valid will, the document may recognise an administrator. The file may also include death information, identity documents and a schedule of assets. Its central function is to authorise someone to act for the estate.", "Record the case number, the deceased's name, the personal representative's name and the assets listed. If the Mainland home does not appear in the current schedule, that does not prove the property is irrelevant, and it does not remove the need for a Mainland title review."]),
                    ("Separate the representative's role from ownership", ["An executor or administrator may collect documents, contact institutions and manage estate steps. The final treatment of a Mainland property still depends on the will, family relationships, the registered title and the route accepted where the property is located.", "For example, a daughter named as administrator does not necessarily become the sole owner. A surviving spouse, other children, co-ownership or a family dispute may materially change the position."]),
                    ("Match names, identity documents and the asset record", ["English and Chinese names, passport numbers and old Mainland registration details often do not match perfectly. Word order, a married surname, an expired passport or a title certificate using only Chinese characters can create a gap.", "Build a name table showing every version, the document on which it appears, the identity number used and any historical record connecting the two identities. Translation and apostille cannot cure an unexplained identity mismatch."]),
                    ("Confirm three document steps before use in Mainland China", ["First obtain the original or an acceptable certified copy. Then arrange Chinese translation for the receiving purpose. Finally, check whether the document type and signature require an apostille from Singapore's designated authority. An apostille authenticates the signature or seal; it does not decide whether the contents are sufficient to transfer the property.", "Ask the receiving property city what it needs before completing the Singapore-side formalities. This prevents paying to prepare a large bundle when only part is needed or when a name issue remains unresolved."]),
                    ("Obtain individual advice when the facts are no longer routine", ["A will covering several countries, a challenge to the will, an unfinished Singapore estate process, a representative withholding papers, or a Mainland home with co-ownership, a mortgage or an occupant all require more than a document-format check.", "Start with four items: the Singapore death record, the will and grant, a one-page family chart, and the Mainland title certificate, contract or address. Then use the <a href=\"/articles/singapore/index_en.html\">Singapore topic overview</a> to identify the next practical question."]),
                ],
                "related_title": "Continue with this topic", "related": [("/articles/singapore/index_en.html", "Singapore topic overview"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_en.html", "What to check before a Mainland property transfer"), ("/articles/hk-mainland-property-inheritance/documents_en.html", "Organising cross-border inheritance papers by purpose"), ("/articles/hk-mainland-property-inheritance/dispute_en.html", "When a family document problem has become a dispute")],
                "cta": "Share the first page of the Singapore grant, the family structure and the Mainland property city. We can then identify what the document does and does not establish.",
            },
        },
    },
    {
        "slug": "us-documents-mainland-property-inheritance",
        "directory": "articles/us",
        "topic": "united-states",
        "topic_urls": {"tc": "/articles/united-states/", "cn": "/articles/united-states/index_cn.html", "en": "/articles/united-states/index_en.html"},
        "copy": {
            "tc": {
                "lang": "zh-Hant", "locale": "zh_HK", "brand": "劉毅律師團隊", "brand_sub": "跨境中國法律事務", "eyebrow": "文章 / 美國繼承",
                "title": "美國死亡證明和遺囑，用於內地房產繼承前先核對甚麼", "description": "美國家屬使用死亡證明、遺囑或遺產文件處理內地房產繼承時，先核對簽發州、文件版本、姓名和內地接收要求。",
                "lead": "美國文件不是全國同一條辦理路線；先看哪個州、哪個機構簽發，再決定證明和翻譯。", "key_title": "先核對三件事",
                "keys": ["文件由哪個州或機構簽發", "手上是不是可供使用的正式版本", "內地房產所在地要它證明甚麼"],
                "visuals": [("先找簽發來源", "州或縣簽發", "聯邦簽發", "來源不同，後續路徑不同。"), ("文件準備順序", "正式副本", "附加證明與翻譯", "內地用途核對", "附加證明不判斷文件內容。"), ("姓名對照清單", "英文與中文姓名", "新舊護照號碼", "死亡與遺產文件", "房產登記資料", "每一種寫法都要有來源。")],
                "answer_title": "先把答案說清楚", "answer": ["美國死亡證明、遺囑或遺產法院文件，通常都不能單獨完成內地房產過戶。先要確認文件由哪個州、縣或聯邦機構簽發，手上是普通影印件還是可供正式使用的版本，再按文件來源辦理相應證明和中文翻譯。", "附加證明書主要確認簽署人的身份、職權和印章，不會替內地接收單位判斷文件內容是否足以證明繼承。因此，先確認內地需要甚麼，再回美國準備文件，通常比「所有文件先做一遍」更穩妥。"],
                "sections": [
                    ("第一步不是翻譯，而是找出簽發來源", ["美國死亡證明多由州或地方生命記錄機構簽發，遺產文件則可能來自某一州的法院。不同州對可辦理附加證明的簽名、正式副本和前置確認要求不完全一樣。即使都是死亡證明，紐約簽發的文件和加州簽發的文件，也不能假定走完全相同的步驟。", "先看文件底部的簽發機構、簽署人職銜、印章和副本標記。若只有掃描件，先向簽發地確認應申領哪種正式版本，不要直接拿打印件去辦後續手續。"]),
                    ("遺囑、遺產管理文件和房產過戶各有作用", ["遺囑表達死者的安排；遺產法院文件可能確認執行人、管理人或某項遺產程序；內地房產登記則要處理具體房屋和繼承人的資料。三者有關聯，但不是同一張文件。", "家屬在美國已完成一部分遺產程序，也不表示內地房子會自動出現在結果裏。先把遺囑、法院文件中的資產描述和內地房產證逐項比對，看看地址、登記人和份額是否能連上。"]),
                    ("附加證明解決真偽鏈條，不解決內容缺口", ["文件用於內地時，符合條件的美國公文書通常按簽發來源辦理附加證明。州或地方簽發的文件一般從相應州的路徑處理；聯邦文件則走聯邦層面的路徑。具體前置要求仍要以簽發地的現行說明為準。", "附加證明不會證明某人一定有權取得內地房屋，也不會把普通影印件變成完整的繼承證據。文件裏缺少親屬關係、姓名對照或房產信息時，仍要另外補充。"]),
                    ("姓名差異要在翻譯前解決", ["美國文件可能只有英文名，內地房產證卻是中文名；還可能出現婚後改姓、中間名縮寫、拼音順序變化和舊護照號碼。翻譯人員只能翻譯現有內容，不能替家屬解釋為甚麼兩個名字是同一個人。", "先做姓名與證件對照表，再找能連接兩種寫法的護照、舊身份證明、出生或婚姻資料。所有日期和號碼也應逐項核對，避免把原文件的小差異放大到整套材料中。"]),
                    ("拿着一頁資料去問內地接收要求", ["這一頁應包括房產城市和地址、登記人、已故家屬的中英文姓名、家屬關係、現有美國文件名稱和簽發地。再問：哪些文件要正式副本；哪些要附加證明；翻譯由誰完成；繼承人不能到場時怎樣授權。", "需要遠程委託時，可先看 <a href=\"/articles/us/remote-china-lawyer.html\">人在美國怎樣整理內地法律事務</a>。如果家屬已經爭執、文件被扣或房屋被他人佔用，就應把文件準備和爭議處理分開評估。"]),
                    ("現在先做的三件小事", ["把每份美國文件的簽發州、簽發機構和版本寫在文件名旁；找出內地房產證或至少一個準確地址；畫一張家屬關係和姓名對照表。", "這三步不需要先決定最終由誰繼承，卻能很快暴露真正的缺口：是缺正式副本、缺身份連接、缺房產線索，還是家人之間已有爭議。確認缺口後，再安排翻譯和證明，通常會少走很多彎路。"]),
                ],
                "related_title": "同一專題繼續閱讀", "related": [("/articles/united-states/", "美國專題總覽"), ("/articles/us/remote-china-lawyer.html", "人在美國怎樣遠程委託內地律師"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist.html", "內地房產過戶前先核對哪些資料"), ("/articles/hk-mainland-property-inheritance/documents.html", "跨境文件按用途整理的方法")],
                "cta": "把文件簽發州、家屬姓名和內地房屋城市說清楚，再判斷哪一份材料先處理。",
            },
            "cn": {
                "lang": "zh-Hans", "locale": "zh_CN", "brand": "刘毅律师团队", "brand_sub": "跨境中国法律事务", "eyebrow": "文章 / 美国继承",
                "title": "美国死亡证明和遗嘱，用于内地房产继承前先核对什么", "description": "美国家属使用死亡证明、遗嘱或遗产文件处理内地房产继承时，先核对签发州、文件版本、姓名和内地接收要求。",
                "lead": "美国文件不是全国同一条办理路线；先看哪个州、哪个机构签发，再决定证明和翻译。", "key_title": "先核对三件事",
                "keys": ["文件由哪个州或机构签发", "手上是不是可供使用的正式版本", "内地房产所在地要它证明什么"],
                "visuals": [("先找签发来源", "州或县签发", "联邦签发", "来源不同，后续路径不同。"), ("文件准备顺序", "正式副本", "附加证明与翻译", "内地用途核对", "附加证明不判断文件内容。"), ("姓名对照清单", "英文与中文姓名", "新旧护照号码", "死亡与遗产文件", "房产登记资料", "每一种写法都要有来源。")],
                "answer_title": "先把答案说清楚", "answer": ["美国死亡证明、遗嘱或遗产法院文件，通常都不能单独完成内地房产过户。先要确认文件由哪个州、县或联邦机构签发，手上是普通复印件还是可供正式使用的版本，再按文件来源办理相应证明和中文翻译。", "附加证明书主要确认签字人的身份、职权和印章，不会替内地接收单位判断文件内容是否足以证明继承。先确认内地需要什么，再回美国准备文件，通常比把所有文件先做一遍更稳妥。"],
                "sections": [
                    ("第一步不是翻译，而是找出签发来源", ["美国死亡证明多由州或地方生命记录机构签发，遗产文件可能来自某个州的法院。各州对可办理附加证明的签名、正式副本和前置确认要求不完全一样。即使都是死亡证明，纽约和加州的文件也不能假定走完全相同的步骤。", "先看文件底部的签发机构、签字人职务、印章和副本标记。如果只有扫描件，先向签发地确认应该申领哪种正式版本。"]),
                    ("遗嘱、遗产管理文件和房产过户作用不同", ["遗嘱表达死者安排；遗产法院文件可能确认执行人、管理人或某项遗产程序；内地房产登记则处理具体房屋和继承人的材料。三者有关联，但不是同一份文件。", "美国家属已经完成部分遗产程序，也不代表内地房子会自动出现在结果中。把遗嘱、法院材料中的资产描述和内地房产证逐项比对，确认地址、登记人和份额能否对应。"]),
                    ("附加证明解决真伪链条，不解决内容缺口", ["符合条件的美国公文书用于内地时，通常按签发来源办理附加证明。州或地方签发的文件一般从相应州的路径处理；联邦文件走联邦层面的路径。前置要求以签发地现行说明为准。", "附加证明不会证明某人一定有权取得内地房屋，也不会把普通复印件变成完整继承证据。缺少亲属关系、姓名对照或房产信息时，仍要另行补充。"]),
                    ("姓名差异要在翻译前解决", ["美国文件可能只有英文名，内地房产证却是中文名；还可能出现婚后改姓、中间名缩写、拼音顺序变化和旧护照号码。翻译人员只能翻译现有内容，不能替家属解释两个名字为什么是同一个人。", "先做姓名和证件对照表，再找能连接两种写法的护照、旧身份证明、出生或婚姻材料。日期和号码也要逐项核对。"]),
                    ("拿一页资料去问内地接收要求", ["列出房产城市和地址、登记人、已故家属的中英文姓名、家属关系、现有美国文件名称和签发地。再问哪些要正式副本、哪些要附加证明、翻译由谁完成、继承人不能到场时怎样授权。", "需要远程委托时，可先看 <a href=\"/articles/us/remote-china-lawyer.html\">人在美国怎样整理内地法律事务</a>。如果已经出现家属争执或房屋占用，应把材料准备和争议处理分开评估。"]),
                    ("现在先做三件小事", ["把每份美国文件的签发州、签发机构和版本写在文件名旁；找出内地房产证或准确地址；画一张家属关系和姓名对照表。", "这三步能很快看出真正缺的是正式副本、身份连接、房产线索，还是家人之间已有争议。确认缺口后再安排翻译和证明，会少走很多弯路。"]),
                ],
                "related_title": "同一专题继续阅读", "related": [("/articles/united-states/index_cn.html", "美国专题总览"), ("/articles/us/remote-china-lawyer.html", "人在美国怎样远程委托内地律师"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_cn.html", "内地房产过户前先核对哪些材料"), ("/articles/hk-mainland-property-inheritance/documents_cn.html", "跨境文件按用途整理的方法")],
                "cta": "把文件签发州、家属姓名和内地房屋城市说清楚，再判断哪一份材料先处理。",
            },
            "en": {
                "lang": "en", "locale": "en_US", "brand": "Liu Yi Lawyer Team", "brand_sub": "Cross-border Mainland China legal matters", "eyebrow": "Article / U.S. inheritance",
                "title": "Using a U.S. Death Certificate or Will for a Mainland China Property Inheritance", "description": "What a U.S.-based family should check before using a death certificate, will or probate paper in a Mainland China property inheritance.",
                "lead": "There is no single nationwide document route for every U.S. record. Start with the issuing state or authority, then plan certification and translation.", "key_title": "Check three things first",
                "keys": ["Which state or authority issued the document?", "Do you have an official usable version?", "What must the Mainland document prove?"],
                "visuals": [("Start with the issuing authority", "State or county record", "Federal record", "Different sources follow different routes."), ("Document preparation order", "Official copy", "Apostille and translation", "Mainland purpose check", "An apostille does not validate the contents."), ("Identity matching checklist", "English and Chinese names", "Current and old passports", "Death and probate papers", "Mainland title record", "Every variation needs a source.")],
                "answer_title": "The short answer", "answer": ["A U.S. death certificate, will or probate order will not normally transfer a Mainland China property on its own. First identify the state, county or federal authority that issued the document and confirm whether you have a certified or otherwise usable version. Certification and Chinese translation should then follow the source and the receiving purpose.", "An apostille authenticates the signature, official capacity and seal. It does not decide that the document proves inheritance or entitles someone to the Mainland home. Confirm the Mainland requirement first, then prepare the U.S. record that answers it."],
                "sections": [
                    ("Start with the issuing authority, not the translation", ["U.S. death certificates are generally issued through state or local vital-record systems, while probate papers come from a court in a particular state. The signature, certified copy and preliminary authentication requirements can differ from one state to another. A New York record and a California record should not be assumed to follow an identical route.", "Read the issuing office, signatory title, seal and copy certification at the bottom of the document. If the family has only a scan, ask the issuing jurisdiction which certified version is suitable for use abroad before arranging anything else."]),
                    ("A will, probate authority and property transfer do different jobs", ["The will records the deceased's intentions. A probate paper may recognise an executor or administrator or record a step in the estate proceeding. The Mainland registration process deals with a specific property and the people claiming it. These documents connect, but none replaces all the others.", "A completed U.S. estate step does not automatically pull a Mainland apartment into the result. Compare the asset description in the will or probate file with the Mainland title certificate, including address, registered owner and ownership share."]),
                    ("An apostille authenticates the paper, not the inheritance claim", ["Eligible U.S. public documents used in Mainland China generally follow an apostille route based on their source. State and local records ordinarily go through the relevant state process, while federal records use the federal route. The current instructions of the issuing jurisdiction still control the preliminary steps.", "An apostille does not prove that the named person must receive the Mainland property, and it does not turn an ordinary photocopy into a complete inheritance file. Missing family links, name matching and property information must still be addressed separately."]),
                    ("Resolve identity differences before translation", ["The U.S. record may show only an English name while the Mainland title uses Chinese characters. Married surnames, middle initials, reversed name order, different romanisation and an expired passport are common sources of mismatch.", "Create an identity table before translation. Show every name version, the document where it appears, the identity number used and the historical record that connects the names. A translator can translate the text but cannot invent the evidence that two identities belong to the same person."]),
                    ("Use one fact sheet to ask the Mainland receiving side", ["List the property city and address, registered owner, the deceased's English and Chinese names, family structure, each U.S. document and its issuing state. Then ask which items need certified copies, which require an apostille, who may translate them, and how an heir who cannot attend should authorise someone.", "For remote work, see <a href=\"/articles/us/remote-china-lawyer.html\">how to organise a Mainland legal instruction from the United States</a>. If documents are being withheld or the property is occupied, assess the evidence and dispute separately from the certification work."]),
                ],
                "related_title": "Continue with this topic", "related": [("/articles/united-states/index_en.html", "United States topic overview"), ("/articles/us/remote-china-lawyer.html", "Organising remote Mainland legal work from the United States"), ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_en.html", "What to check before a Mainland property transfer"), ("/articles/hk-mainland-property-inheritance/documents_en.html", "A practical method for sorting cross-border documents")],
                "cta": "Tell us the issuing state, the family names and the Mainland property city. We can then identify which document should be prepared first.",
            },
        },
    },
]


LANG_SUFFIX = {"tc": "", "cn": "_cn", "en": "_en"}


def article_path(article: dict, lang: str) -> str:
    return f"/{article['directory']}/{article['slug']}{LANG_SUFFIX[lang]}.html"


def published_date(article: dict, lang: str) -> str:
    value = article.get("date_published", TODAY)
    if isinstance(value, dict):
        return value.get(lang, TODAY)
    return value


def json_ld(article: dict, lang: str, copy: dict) -> str:
    canonical = SITE + article_path(article, lang)
    image_base = f"{SITE}/{article['directory']}/images/{article['slug']}"
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": copy["title"],
        "description": copy["description"],
        "inLanguage": copy["lang"],
        "datePublished": published_date(article, lang),
        "dateModified": TODAY,
        "mainEntityOfPage": canonical,
        "articleSection": f"{article['topic']} inheritance",
        "author": {"@type": "Organization", "name": copy["brand"], "url": f"{SITE}/"},
        "publisher": {"@type": "Organization", "@id": f"{SITE}/#organization", "name": copy["brand"], "url": f"{SITE}/"},
        "image": [f"{image_base}/{i:02d}-{name}{LANG_SUFFIX[lang]}.svg" for i, name in [(1, "context"), (2, "path"), (3, "checklist")]],
    }
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def nav(copy: dict, article: dict, lang: str) -> str:
    if lang == "en":
        labels = ["Hong Kong inheritance", "Macau", "Singapore", "United States", "Ask the AI legal assistant"]
        nav_aria = "Article navigation"
        switch_aria = "Language switch"
    elif lang == "cn":
        labels = ["香港房产继承", "澳门专题", "新加坡专题", "美国专题", "咨询 AI 法律助手"]
        nav_aria = "文章导航"
        switch_aria = "语言切换"
    else:
        labels = ["香港房產繼承", "澳門專題", "新加坡專題", "美國專題", "諮詢 AI 法律助手"]
        nav_aria = "文章導覽"
        switch_aria = "語言切換"
    urls = ["/articles/", "/articles/macau/", "/articles/singapore/", "/articles/united-states/", "/ask/gpt/?topic=articles&amp;source=article-nav"]
    links = "".join(f'<a href="{u}">{html.escape(label)}</a>' for u, label in zip(urls, labels))
    language_labels = {"tc": ("繁", "zh-Hant"), "cn": ("简", "zh-Hans"), "en": ("EN", "en")}
    lang_switch = "".join(
        f'<span aria-current="true">{label}</span>' if key == lang else f'<a href="{article_path(article, key)}" lang="{code}">{label}</a>'
        for key, (label, code) in language_labels.items()
    )
    return f'''<header class="site-header"><nav class="nav" aria-label="{nav_aria}"><a class="brand" href="/articles/"><strong>{html.escape(copy['brand'])}</strong><span>{html.escape(copy['brand_sub'])}</span></a><div class="nav-links">{links}</div><div class="article-lang-switch" aria-label="{switch_aria}">{lang_switch}</div></nav></header>'''


def render_article(article: dict, lang: str) -> str:
    copy = article["copy"][lang]
    canonical = SITE + article_path(article, lang)
    default_url = SITE + article_path(article, "tc")
    current = SITE + article_path(article, lang)
    alternates = "".join(
        f'  <link rel="alternate" hreflang="{code}" href="{SITE + article_path(article, key)}">\n'
        for key, code in [("tc", "zh-Hant"), ("cn", "zh-Hans"), ("en", "en")]
    ) + f'  <link rel="alternate" hreflang="x-default" href="{default_url}">\n'
    image_base = f"/{article['directory']}/images/{article['slug']}"
    image_names = ["context", "path", "checklist"]
    figures = "".join(
        f'<figure><img src="{image_base}/{i:02d}-{image_names[i-1]}{LANG_SUFFIX[lang]}.svg" alt="{html.escape(v[0])}" width="1200" height="720" loading="lazy" decoding="async"><figcaption>{html.escape(v[-1])}</figcaption></figure>'
        for i, v in enumerate(copy["visuals"], 1)
    )
    answer = "".join(f"<p>{p}</p>" for p in copy["answer"])
    sections = ""
    toc = f'<a href="#answer">{html.escape(copy["answer_title"])}</a>'
    for idx, (title, paragraphs) in enumerate(copy["sections"], 1):
        body = "".join(f"<p>{p}</p>" for p in paragraphs)
        sections += f'<section id="section-{idx}" class="hk-section-card article-prose-section"><h2>{html.escape(title)}</h2>{body}</section>'
        toc += f'<a href="#section-{idx}">{html.escape(title)}</a>'
    related = "".join(f'<a href="{url}">{html.escape(label)}</a>' for url, label in copy["related"])
    key_items = "".join(f"<li>{html.escape(item)}</li>" for item in copy["keys"])
    ask_topic = article["topic"]
    ask = f'/ask/gpt/?topic={ask_topic}&amp;source=article-{article["slug"]}'
    title = html.escape(copy["title"])
    desc = html.escape(copy["description"])
    footer = "文章內容僅作初步信息參考，具體事項需由律師結合材料進一步判斷。" if lang == "tc" else ("文章内容仅作初步信息参考，具体事项需由律师结合材料进一步判断。" if lang == "cn" else "This article provides general information only. Specific matters require review of the actual documents and facts.")
    contents_heading = "這篇文章會說甚麼" if lang == "tc" else ("这篇文章会说什么" if lang == "cn" else "In this article")
    if lang == "tc":
        hero_aria = "文章導讀"
        key_aria = "重點"
        visuals_aria = "文章配圖"
        related_aria = "相關文章"
        toc_aria = "文章目錄"
    elif lang == "cn":
        hero_aria = "文章导读"
        key_aria = "重点"
        visuals_aria = "文章配图"
        related_aria = "相关文章"
        toc_aria = "文章目录"
    else:
        hero_aria = "Article introduction"
        key_aria = "Key points"
        visuals_aria = "Article visuals"
        related_aria = "Related articles"
        toc_aria = "Article contents"
    cta_title = "需要進一步判斷時" if lang == "tc" else ("需要进一步判断时" if lang == "cn" else "When you need a closer review")
    cta_button = "說明你的情況 →" if lang == "tc" else ("说明你的情况 →" if lang == "cn" else "Describe your situation →")
    return f'''<!DOCTYPE html>
<html lang="{copy['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | {html.escape(copy['brand'])}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta property="og:locale" content="{copy['locale']}">
  <meta property="og:type" content="article"><meta property="og:site_name" content="{html.escape(copy['brand'])}">
  <meta property="og:title" content="{title} | {html.escape(copy['brand'])}"><meta property="og:description" content="{desc}">
  <meta property="og:url" content="{current}"><meta property="og:image" content="{SITE}/articles/article-library-desk-v26.jpg"><meta property="og:image:alt" content="{title}">
  <meta property="article:published_time" content="{published_date(article, lang)}"><meta property="article:modified_time" content="{TODAY}">
  <meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title} | {html.escape(copy['brand'])}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}/articles/article-library-desk-v26.jpg">
  <link rel="canonical" href="{canonical}">
{alternates}  <link rel="stylesheet" href="/articles/style.css?v=27">
  <script type="application/ld+json">{json_ld(article, lang, copy)}</script>
</head>
<body class="article-detail generated-article article-regional-inheritance">
  {nav(copy, article, lang)}
  <main>
    <section class="article-hero" aria-label="{hero_aria}"><div class="article-hero-inner"><div class="article-hero-copy"><p class="eyebrow">{html.escape(copy['eyebrow'])}</p><h1>{title}</h1><p class="article-lead">{html.escape(copy['lead'])}</p><p class="article-last-updated"><time datetime="{TODAY}">{'最後更新' if lang == 'tc' else ('最后更新' if lang == 'cn' else 'Last updated')}: {TODAY}</time></p></div><aside class="article-key-card" aria-label="{key_aria}"><h2>{html.escape(copy['key_title'])}</h2><ul class="article-key-list">{key_items}</ul></aside></div></section>
    <div class="article-shell"><article class="article-main">
      <section class="article-image-grid" aria-label="{visuals_aria}">{figures}</section>
      <section id="answer" class="answer-card"><h2>{html.escape(copy['answer_title'])}</h2>{answer}</section>
      {sections}
      <section class="topic-article-directory compact-directory" aria-label="{related_aria}"><h2>{html.escape(copy['related_title'])}</h2><div class="topic-directory-grid">{related}</div></section>
    </article><aside class="toc" aria-label="{toc_aria}"><h2>{contents_heading}</h2>{toc}<a class="toc-cta" href="{ask}">{cta_button}</a></aside></div>
    <section class="cta-panel"><h2>{cta_title}</h2><p>{html.escape(copy['cta'])}</p><a class="button" href="{ask}">{cta_button}</a></section>
  </main>
  <footer class="site-footer"><div class="footer-inner">{footer}</div></footer><script src="/articles/script.js" defer></script>
</body>
</html>
'''


def visual_label(value: str, x: int, y: int, max_chars: int, css_class: str = "item compact") -> str:
    if len(value) <= max_chars:
        lines = [value]
    elif " " in value:
        words = value.split()
        lines = []
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if current and len(candidate) > max_chars:
                lines.append(current)
                current = word
            else:
                current = candidate
        if current:
            lines.append(current)
    else:
        split_at = max_chars
        lines = [value[:split_at], value[split_at:]]
    if len(lines) > 2:
        lines = [lines[0], " ".join(lines[1:])]
    start_y = y if len(lines) == 1 else y - 17
    tspans = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else 34}">{html.escape(line)}</tspan>' for i, line in enumerate(lines))
    return f'<text x="{x}" y="{start_y}" text-anchor="middle" class="{css_class}">{tspans}</text>'


def visual_svg(parts: tuple, number: int) -> str:
    title = html.escape(parts[0])
    caption = html.escape(parts[-1])
    items = list(parts[1:-1])
    if number == 1:
        boxes = f'''<rect x="110" y="250" width="390" height="220" rx="16" fill="#fffdf8" stroke="#c8a25e" stroke-width="3"/>{visual_label(items[0], 305, 355, 23)}<rect x="700" y="250" width="390" height="220" rx="16" fill="#fffdf8" stroke="#c8a25e" stroke-width="3"/>{visual_label(items[1], 895, 355, 23)}<path d="M510 360 H690" stroke="#a71930" stroke-width="5"/><circle cx="600" cy="360" r="22" fill="#a71930"/><text x="600" y="368" text-anchor="middle" class="plus">+</text>'''
    elif number == 2:
        xs = [95, 420, 745]
        boxes = "".join(f'<rect x="{x}" y="260" width="270" height="170" rx="14" fill="#fffdf8" stroke="#c8a25e" stroke-width="3"/>{visual_label(item, x+135, 350, 16)}' + (f'<path d="M{x+278} 345 H{x+320}" stroke="#a71930" stroke-width="4"/>' if i < 2 else "") for i,(x,item) in enumerate(zip(xs, items)))
    else:
        positions = [(90,245),(620,245),(90,410),(620,410)]
        boxes = "".join(f'<rect x="{x}" y="{y}" width="490" height="125" rx="12" fill="#fffdf8" stroke="#d7c49c" stroke-width="2"/><circle cx="{x+42}" cy="{y+62}" r="21" fill="#a71930"/><text x="{x+42}" y="{y+70}" text-anchor="middle" class="num">{i}</text>{visual_label(item, x+285, y+70, 28, "item small")}' for i,((x,y),item) in enumerate(zip(positions,items),1))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{caption}</desc><style>text{{font-family:Arial,"Microsoft JhengHei","PingFang TC",sans-serif;fill:#0e2235}}.title{{font-size:46px;font-weight:700}}.item{{font-size:29px;font-weight:700}}.compact{{font-size:24px}}.small{{font-size:23px}}.caption{{font-size:24px;fill:#5d6b77}}.plus,.num{{font-size:24px;font-weight:700;fill:white}}</style><rect width="1200" height="720" fill="#f6f2e8"/><rect x="55" y="55" width="1090" height="610" rx="22" fill="#fbfaf6" stroke="#d6c8a6" stroke-width="2"/><text x="90" y="145" class="title">{title}</text><rect x="90" y="180" width="92" height="5" fill="#a71930"/>{boxes}<text x="90" y="620" class="caption">{caption}</text></svg>'''


def write_all() -> None:
    for article in ARTICLES:
        target_dir = ROOT / article["directory"]
        image_dir = target_dir / "images" / article["slug"]
        image_dir.mkdir(parents=True, exist_ok=True)
        for lang in ("tc", "cn", "en"):
            suffix = LANG_SUFFIX[lang]
            (target_dir / f"{article['slug']}{suffix}.html").write_text(render_article(article, lang), encoding="utf-8")
            for idx, name in enumerate(("context", "path", "checklist"), 1):
                (image_dir / f"{idx:02d}-{name}{suffix}.svg").write_text(visual_svg(article["copy"][lang]["visuals"][idx - 1], idx), encoding="utf-8")


def update_secondary_hubs() -> None:
    cards = {
        "articles/macau/index_cn.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">房产继承</span><h3>澳门家属继承内地房产，先分清两套材料</h3><p>把证明家属身份的澳门文件，和内地房产过户材料分开整理。</p></div><a class="v25-pill-action" href="/articles/am/macau-family-mainland-property-inheritance_cn.html">阅读文章</a></article>',
        "articles/macau/index_en.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Property inheritance</span><h3>Inheriting Mainland property from Macau: keep the two document files separate</h3><p>Separate the Macau family and estate papers from the Mainland property registration file.</p></div><a class="v25-pill-action" href="/articles/am/macau-family-mainland-property-inheritance_en.html">Read Article</a></article>',
        "articles/singapore/index_cn.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">房产继承</span><h3>新加坡遗产文件，可以直接办理内地房产过户吗</h3><p>先分清遗产管理人身份、房屋归属和内地登记三层问题。</p></div><a class="v25-pill-action" href="/articles/singapore/mainland-property-inheritance_cn.html">阅读文章</a></article>',
        "articles/singapore/index_en.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Property inheritance</span><h3>Can a Singapore probate grant transfer property in Mainland China?</h3><p>Separate the personal representative\'s authority from entitlement and Mainland registration.</p></div><a class="v25-pill-action" href="/articles/singapore/mainland-property-inheritance_en.html">Read Article</a></article>',
        "articles/united-states/index_cn.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">房产继承</span><h3>美国死亡证明和遗嘱，用于内地房产继承前先核对什么</h3><p>先看签发州、正式版本、姓名对照和内地接收用途。</p></div><a class="v25-pill-action" href="/articles/us/us-documents-mainland-property-inheritance_cn.html">阅读文章</a></article>',
        "articles/united-states/index_en.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Property inheritance</span><h3>Using a U.S. death certificate or will for a Mainland China property inheritance</h3><p>Start with the issuing state, official copy, identity match and Mainland purpose.</p></div><a class="v25-pill-action" href="/articles/us/us-documents-mainland-property-inheritance_en.html">Read Article</a></article>',
    }
    empty_markers = {
        "articles/singapore/index_cn.html": '<div class="topic-empty-v25">目前还没有完成全部质量检查的正式文章。不会用相似标题或薄内容填满列表。</div>',
        "articles/singapore/index_en.html": '<div class="topic-empty-v25">No article has completed the full quality process yet. Similar titles and thin pages will not be used to fill the list.</div>',
    }
    detail_replacements = {
        "articles/macau/index_cn.html": ("<span>4 个方向</span></summary><div class=\"topic-upcoming-grid\"><span>澳门文件交到内地前要先核对什么</span>", "<span>3 个方向</span></summary><div class=\"topic-upcoming-grid\">") ,
        "articles/macau/index_en.html": ("<span>4 directions</span></summary><div class=\"topic-upcoming-grid\"><span>What to check before using Macau documents in Mainland China</span>", "<span>3 directions</span></summary><div class=\"topic-upcoming-grid\">") ,
        "articles/singapore/index_cn.html": ("<span>4 个方向</span></summary><div class=\"topic-upcoming-grid\"><span>第一次咨询要先准备哪些基本事实</span><span>新加坡文件用于内地事务时先看什么</span>", "<span>3 个方向</span></summary><div class=\"topic-upcoming-grid\"><span>第一次咨询要先准备哪些基本事实</span>"),
        "articles/singapore/index_en.html": ("<span>4 directions</span></summary><div class=\"topic-upcoming-grid\"><span>Which facts to prepare for a first consultation</span><span>What to check before using Singapore documents in Mainland China</span>", "<span>3 directions</span></summary><div class=\"topic-upcoming-grid\"><span>Which facts to prepare for a first consultation</span>"),
        "articles/united-states/index_cn.html": ("<span>4 个方向</span></summary><div class=\"topic-upcoming-grid\"><span>第一次跨时区咨询怎样把事情说清楚</span><span>美国文件用于内地事务时先核对哪些细节</span>", "<span>3 个方向</span></summary><div class=\"topic-upcoming-grid\"><span>第一次跨时区咨询怎样把事情说清楚</span>"),
        "articles/united-states/index_en.html": ("<span>4 directions</span></summary><div class=\"topic-upcoming-grid\"><span>How to explain the matter clearly across time zones</span><span>What to check before using U.S. documents in Mainland China</span>", "<span>3 directions</span></summary><div class=\"topic-upcoming-grid\"><span>How to explain the matter clearly across time zones</span>"),
    }
    for rel, card in cards.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if card not in text:
            marker = empty_markers.get(rel)
            if marker and marker in text:
                text = text.replace(marker, card, 1)
            else:
                first_card = '<article class="v25-pillar-card">'
                text = text.replace(first_card, card + first_card, 1)
        old, new = detail_replacements[rel]
        text = text.replace(old, new, 1)
        text = text.replace("这里是专题列表页。文章通过研究、审阅和三语改写后才会加入。", "先看最接近当前情况的一篇，文章按继承文件、委托和资产问题逐步增加。")
        text = text.replace("This is the collection page. Articles appear only after research, review and multilingual rewriting are complete.", "Start with the article closest to the current document or property problem.")
        path.write_text(text, encoding="utf-8")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    blocks = []
    for article in ARTICLES:
        for lang in ("tc", "cn", "en"):
            url = SITE + article_path(article, lang)
            if f"<loc>{url}</loc>" in text:
                continue
            priority = "0.6" if lang == "tc" else "0.55"
            blocks.append(f'''  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>''')
    if blocks:
        text = text.replace("</urlset>", "\n".join(blocks) + "\n</urlset>")
    for hub in ("macau", "singapore", "united-states"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            url = f"{SITE}/articles/{hub}/" + suffix
            start = text.find(f"<loc>{url}</loc>")
            if start >= 0:
                end = text.find("</url>", start)
                block = text[start:end]
                if "<lastmod>" in block:
                    old_date = block.split("<lastmod>", 1)[1].split("</lastmod>", 1)[0]
                    text = text[:start] + block.replace(f"<lastmod>{old_date}</lastmod>", f"<lastmod>{TODAY}</lastmod>") + text[end:]
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_all()
    update_secondary_hubs()
    update_sitemap()
