from __future__ import annotations

import json
import re
from pathlib import Path

from publish_regional_inheritance_foundations import (
    LANG_SUFFIX,
    ROOT,
    SITE,
    TODAY,
    render_article,
    visual_svg,
)


ARTICLES = [
    {
        "slug": "macau-death-record-for-mainland-inheritance",
        "directory": "articles/am",
        "topic": "macau",
        "topic_urls": {
            "tc": "/articles/macau/",
            "cn": "/articles/macau/index_cn.html",
            "en": "/articles/macau/index_en.html",
        },
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 澳門繼承文件",
                "title": "澳門死亡紀錄用於內地房產繼承，先核對哪五項",
                "description": "澳門家屬準備內地房產繼承時，先核對死亡文件種類、姓名、日期、身份銜接和內地接收用途。",
                "lead": "死亡紀錄是整套繼承資料的起點，但它不會單獨回答誰是繼承人，也不會直接完成房產轉名。",
                "key_title": "先記住三件事",
                "keys": [
                    "先辨認手上是哪一種死亡文件",
                    "姓名與身份資料要能前後連起來",
                    "死亡事實、繼承人和房產是三層問題",
                ],
                "visuals": [
                    (
                        "先看手上是哪一種文件",
                        "澳門死亡紀錄證明",
                        "外地死亡證明或其他記錄",
                        "名稱相近，不代表申領和使用路徑相同。",
                    ),
                    (
                        "三層資料要接得上",
                        "死亡事實",
                        "親屬與遺囑",
                        "內地房產",
                        "每一層都回答不同問題。",
                    ),
                    (
                        "第一次核對五項",
                        "文件種類與簽發資料",
                        "姓名和身份銜接",
                        "死亡日期與記錄資料",
                        "內地接收方與用途",
                        "先做清單，再決定正本、翻譯或其他證明。",
                    ),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "澳門死亡紀錄可以證明死亡這件事，但不能單獨證明全部繼承人，也不能替代內地房屋的登記資料。拿到文件後，先核對它究竟是澳門死亡紀錄證明、外地死亡證明，還是因澳門沒有相關登記而取得的其他證明。文件種類不同，後面要補的資料也可能不同。",
                    "實際整理時，把死亡文件和親屬、遺囑、繼承人資格、內地房產資料分開放。這樣一看就知道，現在缺的是死亡事實、家屬關係，還是房屋本身的資料，不會反覆重做同一份文件。",
                ],
                "sections": [
                    (
                        "第一步不是問能不能用，而是先認清文件",
                        [
                            "如果死亡已在澳門登記，家屬手上通常會有相應的死亡紀錄證明。若親人在其他地方離世，家屬可能拿的是外地死亡證明，或需要處理澳門沒有死亡登記的情況。這些文件都與死亡有關，但簽發來源和證明內容並不相同。",
                            "先拍下文件完整頁面，不要只截取姓名和日期。把文件名稱、簽發單位、紀錄編號、簽發日期和語言列成一行，再向內地房產所在地說明用途。對方看到完整資料，才容易回答需要正本、核證副本、翻譯或其他補充。",
                        ],
                    ),
                    (
                        "五項資料要逐一對照",
                        [
                            "第一，確認文件種類。第二，把死者姓名與澳門身份資料、內地房產資料連起來。第三，核對死亡日期和紀錄編號。第四，記下簽發單位、簽發日期和文件語言。第五，寫清楚文件要交到哪個內地城市、用於房產繼承的哪一步。",
                            "最常見的問題不是文件真假，而是同一個人在不同年代用了不同中文寫法、葡文拼法、舊證件號碼或地址。遇到這種情況，不要自行在翻譯上改成一樣；先把每一種寫法出現在哪份正式資料上列清楚，再準備能把它們連起來的身份或姓名記錄。",
                        ],
                    ),
                    (
                        "死亡紀錄不等於繼承人名單",
                        [
                            "內地房產過戶還要知道誰具有繼承身份。澳門家屬通常要另外整理婚姻、出生、收養、已故家屬父母狀況、遺囑和現有繼承人資格文件。家屬關係不同，需要串起來的證明也不同。",
                            "全體成年繼承人沒有爭議時，澳門有確認繼承人資格的公證安排；申請時仍要按家庭情況提交死亡、婚姻、出生、遺囑等資料。這說明死亡紀錄只是其中一張，不是完整答案。若有人反對或家屬範圍不清，就不要先把無爭議文件當成既定路徑。",
                        ],
                    ),
                    (
                        "交到內地前，先讓接收方看到清單",
                        [
                            "不同城市、不同房屋狀態和不同辦理路徑，對文件形式的要求可能不同。把死亡文件清晰掃描件、家屬關係圖、是否有遺囑、房屋地址和登記人一起交給房產所在地核對，比只問一句“澳門死亡證明能不能用”更有效。",
                            "先問四件事：接收哪一種死亡文件；是否需要正本或核證副本；非中文內容怎樣翻譯；姓名或證件資料有差異時還要補甚麼。確認後再辦，才不會把時間花在接收方不需要的文件上。",
                        ],
                    ),
                    (
                        "資料不齊時，先把能確認的部分固定下來",
                        [
                            "找不到死亡文件原件時，先記錄死者完整姓名、可能的死亡日期和地點、澳門身份資料，以及由哪一名家屬申領。若死亡發生在外地，也要保留外地簽發資料和與死者的親屬證明。",
                            "現在可以先做一頁表：左邊列澳門死亡和親屬文件，右邊列內地房屋地址、登記姓名和現有產權資料。兩邊出現的姓名、日期或身份號碼有差異，就圈出來逐項處理。整套繼承文件的起點會因此清楚很多。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/macau/", "澳門專題總覽"),
                    ("/articles/am/macau-family-mainland-property-inheritance.html", "澳門家屬繼承內地房產，先分清兩套文件"),
                    ("/articles/hk-mainland-property-inheritance/hong-kong-death-certificate-details.html", "對照閱讀：香港死亡證明先核對哪些資料"),
                    ("/articles/hk-mainland-property-inheritance/family-relationship-evidence.html", "家屬關係資料怎樣接成一條證明鏈"),
                ],
                "cta": "把死亡文件種類、死者姓名、家屬關係和內地房屋城市說清楚，再判斷先補哪一層資料。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 澳门继承文件",
                "title": "澳门死亡记录用于内地房产继承，先核对哪五项",
                "description": "澳门家属准备内地房产继承时，先核对死亡文件种类、姓名、日期、身份衔接和内地接收用途。",
                "lead": "死亡记录是整套继承材料的起点，但它不能单独回答谁是继承人，也不能直接完成房产过户。",
                "key_title": "先记住三件事",
                "keys": ["先辨认手上是哪一种死亡文件", "姓名与身份材料要能前后连起来", "死亡事实、继承人和房产是三层问题"],
                "visuals": [
                    ("先看手上是哪一种文件", "澳门死亡记录证明", "外地死亡证明或其他记录", "名称相近，不代表申领和使用路径相同。"),
                    ("三层材料要接得上", "死亡事实", "亲属与遗嘱", "内地房产", "每一层都回答不同问题。"),
                    ("第一次核对五项", "文件种类与签发信息", "姓名和身份衔接", "死亡日期与记录信息", "内地接收方与用途", "先做清单，再决定原件、翻译或其他证明。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "澳门死亡记录可以证明死亡事实，但不能单独证明全部继承人，也不能替代内地房屋登记材料。拿到文件后，先核对它究竟是澳门死亡记录证明、外地死亡证明，还是因澳门没有相关登记而取得的其他证明。文件种类不同，后面要补的材料也可能不同。",
                    "实际整理时，把死亡文件和亲属、遗嘱、继承人资格、内地房产材料分开存放。这样可以直接看出，现在缺的是死亡事实、家属关系，还是房屋本身的材料，避免反复重做同一份文件。",
                ],
                "sections": [
                    ("第一步不是问能不能用，而是先认清文件", ["如果死亡已在澳门登记，家属手上通常会有相应的死亡记录证明。亲人在其他地方去世时，家属可能拿的是外地死亡证明，或需要处理澳门没有死亡登记的情况。这些文件都与死亡有关，但签发来源和证明内容并不相同。", "先拍下文件完整页面，不要只截取姓名和日期。把文件名称、签发单位、记录编号、签发日期和语言列成一行，再向内地房产所在地说明用途。"]),
                    ("五项信息要逐一对照", ["第一，确认文件种类。第二，把死者姓名与澳门身份材料、内地房产材料连接起来。第三，核对死亡日期和记录编号。第四，记下签发单位、签发日期和文件语言。第五，写清楚文件要交到哪个内地城市、用于房产继承的哪一步。", "同一个人在不同年代可能使用不同中文写法、葡文拼法、旧证件号码或地址。不要自行在翻译上改成一致；先列明每一种写法出现在哪份正式材料上，再准备能够连接身份的记录。"]),
                    ("死亡记录不等于继承人名单", ["内地房产过户还要知道谁具有继承身份。澳门家属通常要另行整理婚姻、出生、收养、已故家属父母情况、遗嘱和现有继承人资格文件。", "全体成年继承人没有争议时，澳门有确认继承人资格的公证安排；申请时仍要按家庭情况提交死亡、婚姻、出生、遗嘱等材料。死亡记录只是其中一份。如果有人反对或家属范围不清，不要先按无争议路径准备。"]),
                    ("交到内地前，先让接收方看到清单", ["不同城市、房屋状态和办理路径，对文件形式的要求可能不同。把死亡文件扫描件、家属关系图、遗嘱情况、房屋地址和登记人一起交给房产所在地核对，比只问“澳门死亡证明能不能用”更有效。", "先问四件事：接收哪一种死亡文件；是否需要原件或核证副本；非中文内容怎样翻译；姓名或证件信息有差异时还要补什么。"]),
                    ("材料不齐时，先固定能够确认的部分", ["找不到死亡文件原件时，先记录死者完整姓名、可能的死亡日期和地点、澳门身份信息，以及由哪一名家属申领。死亡发生在外地时，也要保留外地签发信息和亲属证明。", "先做一页表：左边列澳门死亡和亲属文件，右边列内地房屋地址、登记姓名和现有产权材料。两边出现的姓名、日期或身份号码有差异，就圈出来逐项处理。"]),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/macau/index_cn.html", "澳门专题总览"),
                    ("/articles/am/macau-family-mainland-property-inheritance_cn.html", "澳门家属继承内地房产，先分清两套材料"),
                    ("/articles/hk-mainland-property-inheritance/hong-kong-death-certificate-details_cn.html", "对照阅读：香港死亡证明先核对哪些信息"),
                    ("/articles/hk-mainland-property-inheritance/family-relationship-evidence_cn.html", "家属关系材料怎样接成证明链"),
                ],
                "cta": "把死亡文件种类、死者姓名、家属关系和内地房屋城市说明清楚，再判断先补哪一层材料。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Macau estate records",
                "title": "Using a Macau Death Record for a Mainland Property Inheritance",
                "description": "A practical check for Macau families connecting a death record to a property inheritance in Mainland China.",
                "lead": "The death record starts the estate file. It does not, by itself, identify every heir or transfer the property.",
                "key_title": "Three points to keep in mind",
                "keys": ["Identify the exact death document", "Connect every name to the same person", "Keep death, heirship and property in separate files"],
                "visuals": [
                    ("Identify the document first", "Macau death record", "Death record issued elsewhere", "Similar labels can lead to different preparation steps."),
                    ("Connect three separate files", "Death facts", "Family and will", "Mainland property", "Each file answers a different question."),
                    ("First review checklist", "Document and issuing details", "Names and identity trail", "Date and record details", "Mainland recipient and purpose", "Confirm the destination before ordering copies or translations."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "A Macau death record can establish the death, but it does not establish the full list of heirs and it does not replace the Mainland property file. First identify whether you hold a Macau death record, a death certificate issued elsewhere, or another record connected with the absence of a Macau death registration. The preparation route may differ.",
                    "Keep four folders from the outset: death, family relationships, will or heirship, and Mainland property. This makes the actual gap visible and prevents the family from repeatedly ordering the wrong document.",
                ],
                "sections": [
                    ("Identify the document before asking whether it can be used", ["A death registered in Macau and a death recorded elsewhere do not produce the same paper trail. The family may also be dealing with a situation where there is no Macau death registration. Do not treat every document that mentions the death as interchangeable.", "Scan the complete page, including the title, issuing body, record number, issue date and language. Send that full description to the office or adviser dealing with the Mainland property rather than sending a cropped name and date."]),
                    ("Check five points line by line", ["First, identify the type of death document. Second, connect the deceased's name across the Macau identity and Mainland property records. Third, record the date of death and record number. Fourth, note the issuing body, issue date and language. Fifth, identify the Mainland city and the exact step for which the document is requested.", "The real difficulty is often continuity of identity: an older Chinese name, Portuguese spelling, former identity number or address may appear in a different record. Do not silently standardise those differences in a translation. List each variation and the official record in which it appears."]),
                    ("A death record is not an heir list", ["The property file still needs evidence showing who may inherit. Depending on the family, that may involve marriage, birth, adoption, records about the deceased's parents, a will and any existing heirship instrument.", "Where all adult heirs agree, Macau has a notarial route for confirming heir status, but that application still draws on the relevant death and family records. If the family tree is disputed or incomplete, do not assume that a non-contentious document route will solve the disagreement."]),
                    ("Show the receiving side a one-page file list", ["The required form can vary with the Mainland city, property status and procedural route. A scan of the death record, a simple family tree, the will position, property address and registered owner will usually produce a more useful response than the question, “Is a Macau death certificate accepted?”", "Ask which death document is required, whether an original or certified copy is needed, how non-Chinese text should be translated, and what bridges any difference in names or identity numbers."]),
                    ("When records are missing, secure the facts that still exist", ["If the original cannot be found, record the deceased's full name, likely date and place of death, Macau identity details and the relative who can request the record. If the death occurred elsewhere, preserve the foreign issuing details and proof of the requester's relationship.", "Create one sheet with the Macau death and family records on the left and the Mainland address, registered name and title records on the right. Circle every difference in names, dates or identity numbers. That sheet becomes a practical starting point for the next review."]),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/macau/index_en.html", "Macau topic overview"),
                    ("/articles/am/macau-family-mainland-property-inheritance_en.html", "Keep the Macau family file separate from the Mainland property file"),
                    ("/articles/hk-mainland-property-inheritance/hong-kong-death-certificate-details_en.html", "Comparison: checking a Hong Kong death certificate"),
                    ("/articles/hk-mainland-property-inheritance/family-relationship-evidence_en.html", "Building a family relationship evidence chain"),
                ],
                "cta": "Tell us which death record you have, how the family is related, and where the Mainland property is located. The first missing layer can then be identified.",
            },
        },
    },
    {
        "slug": "probate-or-letters-of-administration",
        "directory": "articles/singapore",
        "topic": "singapore",
        "topic_urls": {
            "tc": "/articles/singapore/",
            "cn": "/articles/singapore/index_cn.html",
            "en": "/articles/singapore/index_en.html",
        },
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡繼承文件",
                "title": "新加坡繼承有遺囑和無遺囑，法院文件有甚麼不同",
                "description": "新加坡家屬處理內地房產繼承時，先分清遺囑認證和遺產管理書各自確認甚麼。",
                "lead": "有沒有有效遺囑，通常先決定由遺囑執行人還是遺產管理人代表遺產；內地房產仍要另行核對。",
                "key_title": "先分清三件事",
                "keys": ["有有效遺囑先看指定執行人", "沒有有效遺囑通常看可申請的受益人", "法院文件確認管理權，不自動完成內地過戶"],
                "visuals": [
                    ("先看有沒有有效遺囑", "有遺囑與指定執行人", "沒有有效遺囑", "兩種情況的申請人和法院文件不同。"),
                    ("拿到法院文件後再接內地", "確認代表身份", "核對繼承與資產", "確認內地接收要求", "法院文件不是內地房產證。"),
                    ("第一次準備清單", "死亡與遺囑資料", "法院文件與資產清單", "家屬關係和身份", "內地房產地址與登記", "把新加坡和內地兩邊的資料分開整理。"),
                ],
                "answer_title": "最短的判斷方法",
                "answer": [
                    "如果死者留下有效遺囑，並在遺囑中指定執行人，通常由該執行人申請 Grant of Probate（遺囑認證）。沒有有效遺囑時，通常由符合條件的受益人申請 Letters of Administration（遺產管理書），獲委任為遺產管理人。兩者都與誰有權管理遺產有關，但起點不同。",
                    "家屬還要分開處理內地房產的三個問題：房屋是否確屬死者、真正進入遺產的是全部還是部分份額，以及哪些人最終具有繼承權。不要把新加坡法院文件直接理解成內地房產的轉名批文。",
                ],
                "sections": [
                    ("有遺囑和沒有遺囑，先找的人不同", ["有有效遺囑時，先找遺囑正本和其中指定的執行人。新加坡的申請過程會核對遺囑和執行人身份。沒有有效遺囑時，則要先梳理哪些受益人有資格申請管理遺產，以及是否有人需要放棄優先申請。", "如果只找到遺囑掃描件、家屬對遺囑效力有爭議，或有人已提出反對，就不適合把它當成普通無爭議申請。先保存遺囑來源、保管人、簽署資料和家屬的不同說法。"]),
                    ("法院文件主要確認誰能代表遺產", ["Grant of Probate 通常確認遺囑所指定的執行人可以管理遺產；Letters of Administration 通常確認由法院委任的管理人處理沒有有效遺囑的遺產。代表人可整理資產、處理債務並按適用安排進行分配。", "這不等於新加坡法院已經替內地登記機關判斷房屋歸誰。房產在內地哪個城市、登記在誰名下、是否夫妻或多人共有、是否有按揭，仍要另外核對。"]),
                    ("再看 Schedule of Assets 是否說到內地資產", ["新加坡申請文件通常會配合資產清單，讓法院了解遺產的組成和價值。家屬應核對內地房產是否已被列明，地址、估值和持有方式是否有基本資料。", "如果法院文件簽發後才發現內地房產，或原來的資產資料不完整，不要自行在舊文件上加字。先向處理新加坡遺產程序的人員確認是否需要補充或取得新的法院文件，再和內地接收方核對用途。"]),
                    ("電子文件、正式副本和跨境使用要分開問", ["新加坡法院的 grant 可以電子形式簽發；如其他機構需要，也可能另行取得正式副本。要交到內地使用時，先問接收方要電子核驗、正式副本還是其他形式，並確認是否需要翻譯和附加證明。", "新加坡的跨境文件有指定主管機關處理附加證明，但附加證明只核驗簽名、印章或文件來源，不會替接收方確認內容足以完成房產繼承。先確認接收用途，再走文件程序。"]),
                    ("家屬意見不一時，不要只追一張 grant", ["有人質疑遺囑、反對申請人、拒絕提供資產資料，或家屬對內地房產分配沒有共識時，問題已不只是缺一張法院文件。新加坡程序中的 caveat（反對記錄），也可能使法院不能按普通無爭議方式簽發 grant。", "先把爭議寫成三欄：誰反對、反對哪一件事、手上有甚麼文件。這比反覆問“哪一張 grant 才能過戶”更接近真正要解決的問題。"]),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡專題總覽"),
                    ("/articles/singapore/mainland-property-inheritance.html", "新加坡遺產文件能否直接辦內地房產過戶"),
                    ("/articles/hk-mainland-property-inheritance/will-first-review.html", "找到遺囑後先核對哪幾件事"),
                    ("/articles/hk-mainland-property-inheritance/property-transfer-checklist.html", "內地房產過戶前先查哪些資料"),
                ],
                "cta": "把遺囑情況、現有新加坡法院文件和內地房產城市說清楚，再判斷缺的是代表權、繼承資料還是房屋資料。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡继承文件",
                "title": "新加坡继承有遗嘱和无遗嘱，法院文件有什么不同",
                "description": "新加坡家属处理内地房产继承时，先分清遗嘱认证和遗产管理书分别确认什么。",
                "lead": "有没有有效遗嘱，通常先决定由遗嘱执行人还是遗产管理人代表遗产；内地房产仍要另外核对。",
                "key_title": "先分清三件事",
                "keys": ["有有效遗嘱先看指定执行人", "没有有效遗嘱通常看可申请的受益人", "法院文件确认管理权，不自动完成内地过户"],
                "visuals": [
                    ("先看有没有有效遗嘱", "有遗嘱与指定执行人", "没有有效遗嘱", "两种情况的申请人和法院文件不同。"),
                    ("拿到法院文件后再衔接内地", "确认代表身份", "核对继承与资产", "确认内地接收要求", "法院文件不是内地房产证。"),
                    ("第一次准备清单", "死亡与遗嘱材料", "法院文件与资产清单", "家属关系和身份", "内地房产地址与登记", "把新加坡和内地两边的材料分开整理。"),
                ],
                "answer_title": "最短的判断方法",
                "answer": ["死者留下有效遗嘱并指定执行人时，通常由该执行人申请 Grant of Probate（遗嘱认证）。没有有效遗嘱时，通常由符合条件的受益人申请 Letters of Administration（遗产管理书），获委任为遗产管理人。两者都与谁有权管理遗产有关，但起点不同。", "家属还要单独处理内地房产的三个问题：房屋是否属于死者、真正进入遗产的是全部还是部分份额，以及哪些人最终具有继承权。不要把新加坡法院文件直接理解为内地房产的过户批文。"],
                "sections": [
                    ("有遗嘱和没有遗嘱，先找的人不同", ["有有效遗嘱时，先找遗嘱原件和其中指定的执行人。新加坡申请过程会核对遗嘱和执行人身份。没有有效遗嘱时，要先梳理哪些受益人有资格申请管理遗产，以及是否有人需要放弃优先申请。", "如果只找到遗嘱扫描件、家属对遗嘱效力有争议，或有人已提出反对，就不适合按普通无争议申请处理。先保存遗嘱来源、保管人、签署信息和家属的不同说法。"]),
                    ("法院文件主要确认谁能代表遗产", ["Grant of Probate 通常确认遗嘱指定的执行人可以管理遗产；Letters of Administration 通常确认法院委任的管理人处理没有有效遗嘱的遗产。", "这不等于新加坡法院已经替内地登记机构判断房屋归属。房产所在城市、登记人、共有情况和按揭状态仍要另外核对。"]),
                    ("再看 Schedule of Assets 是否提到内地资产", ["新加坡申请材料通常配有资产清单，家属应核对内地房产是否已列明，地址、估值和持有方式是否有基本信息。", "如果法院文件签发后才发现内地房产，或原来的资产信息不完整，不要自行在旧文件上添加内容。先向处理新加坡遗产程序的人员确认是否需要补充或取得新的法院文件。"]),
                    ("电子文件、正式副本和跨境使用要分开问", ["新加坡法院的 grant 可以电子形式签发；如机构需要，也可能另行取得正式副本。交到内地前，先问接收方需要电子核验、正式副本还是其他形式，并确认翻译和附加证明要求。", "附加证明只核验签名、印章或文件来源，不会替接收方确认内容足以完成房产继承。先确认接收用途，再安排文件程序。"]),
                    ("家属意见不一致时，不要只追一张 grant", ["有人质疑遗嘱、反对申请人、拒绝提供资产材料，或家属对内地房产分配没有共识时，问题已经不只是缺少法院文件。新加坡程序中的 caveat（反对记录）也可能影响 grant 的签发。", "先把争议写成三栏：谁反对、反对哪件事、手上有什么文件。这比反复问“哪一张 grant 才能过户”更接近真正的问题。"]),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡专题总览"),
                    ("/articles/singapore/mainland-property-inheritance_cn.html", "新加坡遗产文件能否直接办理内地房产过户"),
                    ("/articles/hk-mainland-property-inheritance/will-first-review_cn.html", "找到遗嘱后先核对哪几件事"),
                    ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_cn.html", "内地房产过户前先查哪些材料"),
                ],
                "cta": "把遗嘱情况、现有新加坡法院文件和内地房产城市说明清楚，再判断缺的是代表权、继承材料还是房屋材料。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore estate papers",
                "title": "Singapore Probate: Which Court Grant Applies With or Without a Will?",
                "description": "A clear guide to the two Singapore grants and how either may fit into a Mainland China property inheritance file.",
                "lead": "The presence of a valid will usually determines whether the estate begins with an executor or an administrator. The Mainland property still requires a separate review.",
                "key_title": "Start with three distinctions",
                "keys": ["A valid will points to the named executor", "No valid will usually points to an eligible beneficiary", "A grant gives authority to act; it is not a Mainland transfer order"],
                "visuals": [
                    ("Start with the will", "Valid will and executor", "No valid will", "Different starting facts lead to different grants."),
                    ("Connect the grant to the property file", "Authority to represent", "Heirs and assets", "Mainland requirements", "A court grant is not a property title."),
                    ("First document checklist", "Death record and will", "Grant and asset schedule", "Family and identity records", "Mainland address and title", "Keep the Singapore estate file separate from the property file."),
                ],
                "answer_title": "The practical distinction",
                "answer": [
                    "Where the deceased left a valid will naming an executor, that executor will ordinarily apply for a Grant of Probate. If there is no valid will, an eligible beneficiary will usually apply for Letters of Administration and, if appointed, act as administrator. Both grants identify the person authorised to deal with the estate, but they arise from different facts.",
                    "Neither document should be treated as an automatic transfer of a home in Mainland China. The family must still establish what the deceased owned, whether only a share enters the estate, who is entitled to inherit, and what the property office in the relevant Mainland city requires.",
                ],
                "sections": [
                    ("A will changes who should act first", ["With a valid original will, begin with the person named as executor. The Singapore application will address the will and that person's appointment. Without a valid will, the family must instead identify which beneficiary may apply to administer the estate and whether anyone with a prior right needs to renounce that application.", "A scan of a will, a dispute over its validity, or an existing objection is not a routine uncontested file. Preserve where the will came from, who held it, the signing information and each family member's position before choosing the application route."]),
                    ("The grant identifies the estate's representative", ["A Grant of Probate ordinarily confirms the authority of the executor named in the will. Letters of Administration ordinarily appoint an administrator for an estate without a valid will. That representative can gather assets, address liabilities and administer the estate.", "The grant does not ask a Mainland registration office to accept that the entire property belonged to the deceased or that it should pass to a particular heir. The city, registered owner, co-ownership and mortgage position still need a separate property review."]),
                    ("Check the Schedule of Assets", ["The Singapore probate file generally includes a Schedule of Assets. Check whether the Mainland property appears and whether the address, value and manner of ownership are described consistently with the records now available.", "If the property was discovered only after the grant or the original asset information was incomplete, do not annotate an old court paper yourself. Ask the Singapore probate professional whether a further filing or updated court document is needed, then confirm the purpose with the Mainland recipient."]),
                    ("Electronic grants, official copies and overseas use are separate questions", ["Singapore grants are issued electronically, while an official printed or certified copy may also be obtained where a receiving institution requires one. Ask the Mainland recipient which version it can verify and whether translation or an apostille is required.", "An apostille verifies the relevant signature, seal or origin of a public document. It does not decide that the document contains everything required for a property inheritance. Confirm the destination and purpose before ordering the formal document chain."]),
                    ("A family disagreement is not solved by collecting another grant", ["A challenge to the will, an objection to the applicant, withheld asset information or disagreement over the Mainland property may prevent the matter from remaining straightforward. A caveat in the Singapore process can also stop an uncontested grant from being issued in the ordinary way.", "Write the dispute in three columns: who objects, what they object to, and which document supports each position. That list exposes the actual problem more clearly than repeatedly asking which grant will transfer the property."]),
                ],
                "related_title": "Continue with this topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore topic overview"),
                    ("/articles/singapore/mainland-property-inheritance_en.html", "Can a Singapore probate grant transfer Mainland property?"),
                    ("/articles/hk-mainland-property-inheritance/will-first-review_en.html", "What to check when the family finds a will"),
                    ("/articles/hk-mainland-property-inheritance/property-transfer-checklist_en.html", "Mainland property transfer: first document check"),
                ],
                "cta": "Tell us whether there is a valid will, which Singapore grant exists, and where the Mainland property is located. We can then identify whether the gap concerns authority, heirship or the property file.",
            },
        },
    },
]


def article_path(article: dict, lang: str) -> str:
    return f"/{article['directory']}/{article['slug']}{LANG_SUFFIX[lang]}.html"


def write_articles() -> None:
    for article in ARTICLES:
        target_dir = ROOT / article["directory"]
        image_dir = target_dir / "images" / article["slug"]
        image_dir.mkdir(parents=True, exist_ok=True)
        for lang in ("tc", "cn", "en"):
            suffix = LANG_SUFFIX[lang]
            (target_dir / f"{article['slug']}{suffix}.html").write_text(
                render_article(article, lang), encoding="utf-8"
            )
            for index, name in enumerate(("context", "path", "checklist"), start=1):
                (image_dir / f"{index:02d}-{name}{suffix}.svg").write_text(
                    visual_svg(article["copy"][lang]["visuals"][index - 1], index),
                    encoding="utf-8",
                )


HUB_CARDS = {
    "articles/macau/index.html": '<a href="/articles/am/macau-death-record-for-mainland-inheritance.html"><span class="v24-tag">死亡文件</span><strong>澳門死亡紀錄用於內地房產繼承，先核對哪五項</strong><p>先認清文件種類，再把死亡、家屬關係和房產資料分開整理。</p></a>',
    "articles/macau/index_cn.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">死亡文件</span><h3>澳门死亡记录用于内地房产继承，先核对哪五项</h3><p>先认清文件种类，再把死亡、家属关系和房产材料分开整理。</p></div><a class="v25-pill-action" href="/articles/am/macau-death-record-for-mainland-inheritance_cn.html">阅读文章</a></article>',
    "articles/macau/index_en.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Death records</span><h3>Using a Macau death record for a Mainland property inheritance</h3><p>Identify the document, then separate the death, family and property files.</p></div><a class="v25-pill-action" href="/articles/am/macau-death-record-for-mainland-inheritance_en.html">Read Article</a></article>',
    "articles/singapore/index.html": '<a href="/articles/singapore/probate-or-letters-of-administration.html"><span class="v24-tag">法院文件</span><strong>Grant of Probate 還是 Letters of Administration？</strong><p>先看有沒有有效遺囑，再分清誰能代表遺產和內地房產還缺甚麼。</p></a>',
    "articles/singapore/index_cn.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">法院文件</span><h3>Grant of Probate 还是 Letters of Administration？</h3><p>先看有没有有效遗嘱，再分清谁能代表遗产和内地房产还缺什么。</p></div><a class="v25-pill-action" href="/articles/singapore/probate-or-letters-of-administration_cn.html">阅读文章</a></article>',
    "articles/singapore/index_en.html": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Court grants</span><h3>Grant of Probate or Letters of Administration?</h3><p>Start with the will, then separate authority to act from the Mainland property file.</p></div><a class="v25-pill-action" href="/articles/singapore/probate-or-letters-of-administration_en.html">Read Article</a></article>',
}


HUB_INHERITANCE_COPY = {
    "macau": {
        "tc": {
            "path": "articles/macau/index.html",
            "title": "澳門家屬處理內地遺產，先從哪裏開始 | 劉毅律師團隊",
            "name": "澳門家屬處理內地遺產，先從哪裏開始",
            "description": "澳門家屬處理內地房產、存款或股權繼承，先分清死亡與親屬文件、遺囑或繼承安排，以及內地資產所在地，再按實際卡點閱讀。",
            "eyebrow": "首頁&nbsp;&gt;&nbsp;文章&nbsp;&gt;&nbsp;澳門繼承專題",
            "h1": "澳門家屬處理內地遺產<br>先從哪裏開始",
            "lead": "家人在澳門、遺產在內地時，先把死亡文件、親屬關係、遺囑或繼承安排，以及房產、存款或股權所在城市分開整理。找到最接近目前卡點的一篇，再準備文件。",
            "trust": ["澳門家屬", "內地遺產", "身份與文件", "房產與賬戶"],
            "guide": [
                ("先列清遺產", "房產、存款、股權和其他線索分開記。"),
                ("再核對澳門文件", "死亡、婚姻、出生和姓名資料各有用途。"),
                ("確認誰要參與", "遺囑、親屬範圍和家人意見不能混在一起。"),
                ("最後安排內地步驟", "按資產城市確認文件、簽署和到場方式。"),
            ],
            "checks": [
                ("遺產在哪", "先寫清內地城市、房屋地址、銀行或公司名稱。"),
                ("誰已去世", "核對死亡文件、姓名寫法和身份資料。"),
                ("誰是家屬", "列出配偶、子女、父母及已故家屬情況。"),
                ("現在卡哪一步", "是文件不齊、家人不配合，還是不清楚資產。"),
            ],
            "section_title": "澳門家屬繼承內地遺產<br>專題文章",
            "section_lead": "每篇只回答一個實際問題，從文件核對、繼承人範圍到房產和其他資產逐步整理。",
            "upcoming": ["澳門親屬關係文件怎樣連到內地繼承人", "有遺囑時先核對哪些人和資產", "不能回內地時授權範圍怎樣寫", "只知道舊地址時怎樣找房產或存款線索"],
            "other_title": "其他地區的內地遺產專題",
            "other": [("/articles/", "香港居民繼承內地房產", "香港"), ("/articles/singapore/", "新加坡家屬處理內地遺產", "新加坡"), ("/articles/united-states/", "美國家屬處理內地遺產", "美國")],
            "bottom_title": "仍不確定先看哪篇？",
            "bottom_text": "把逝者、家屬、內地資產和現有澳門文件說清楚，先判斷缺的是哪一層資料。",
            "cards": [
                ("房產繼承", "澳門家屬繼承內地房產，先分清兩套文件", "把證明家屬身份的澳門文件，和內地房產過戶資料分開整理。", "/articles/am/macau-family-mainland-property-inheritance.html"),
                ("死亡文件", "澳門死亡紀錄用於內地房產繼承，先核對哪五項", "先認清文件種類，再把死亡、家屬關係和房產資料分開整理。", "/articles/am/macau-death-record-for-mainland-inheritance.html"),
            ],
        },
        "cn": {
            "path": "articles/macau/index_cn.html",
            "title": "澳门家属处理内地遗产，先从哪里开始 | 刘毅律师团队",
            "name": "澳门家属处理内地遗产，先从哪里开始",
            "description": "澳门家属处理内地房产、存款或股权继承，先分清死亡与亲属文件、遗嘱或继承安排，以及内地资产所在地，再按实际卡点阅读。",
            "h1": "澳门家属处理内地遗产，先从哪里开始",
            "lead": "家人在澳门、遗产在内地时，先把死亡文件、亲属关系、遗嘱或继承安排，以及房产、存款或股权所在城市分开整理。",
            "pills": ["死亡与亲属文件", "内地资产", "当前卡点"],
            "guide_title": "先别急着把全部文件做一遍",
            "guide": ["列清内地房产、存款或股权线索。", "核对死亡文件和每位家属的身份关系。", "有遗嘱时先确认原件、保管人和涉及资产。", "最后按资产城市确认签署和接收要求。"],
            "checks": [("遗产在哪里", "写清城市、地址、银行或公司名称"), ("谁已经去世", "核对姓名、日期和死亡文件"), ("谁需要参与", "列出配偶、子女、父母及遗嘱情况"), ("卡在哪一步", "文件不齐、家人不配合或资产不清")],
            "section_title": "澳门家属继承内地遗产专题文章",
            "section_lead": "每篇只回答一个实际问题，从文件核对、继承人范围到房产和其他资产逐步整理。",
            "upcoming": ["澳门亲属关系文件怎样连接到内地继承人", "有遗嘱时先核对哪些人和资产", "不能回内地时授权范围怎样写", "只知道旧地址时怎样找房产或存款线索"],
            "facts": ["逝者姓名、死亡时间和死亡地点", "内地房产、账户或公司所在城市", "现有澳门身份、亲属和遗嘱文件"],
            "obstacles": ["亲属关系文件对不上", "遗嘱或继承人范围有争议", "资产线索不完整或无法到场"],
            "bottom_title": "先把逝者、家属和资产分开整理",
            "bottom_text": "不用先判断结果，先让三组资料能够互相对应。",
            "cards": [("房产继承", "澳门家属继承内地房产，先分清两套材料", "把证明家属身份的澳门文件，和内地房产过户材料分开整理。", "/articles/am/macau-family-mainland-property-inheritance_cn.html"), ("死亡文件", "澳门死亡记录用于内地房产继承，先核对哪五项", "先认清文件种类，再把死亡、家属关系和房产材料分开整理。", "/articles/am/macau-death-record-for-mainland-inheritance_cn.html")],
        },
        "en": {
            "path": "articles/macau/index_en.html",
            "title": "Macau families handling an estate in Mainland China | Liu Yi Lawyer Team",
            "name": "Macau families handling an estate in Mainland China",
            "description": "Practical articles for Macau families connecting death and family records to property, bank accounts or company interests in Mainland China.",
            "h1": "Macau families handling an estate in Mainland China",
            "lead": "Start by separating the Macau death and family records from the Mainland property, account or company file. Then choose the article that matches the point where the family is stuck.",
            "pills": ["Death and family records", "Mainland assets", "Current obstacle"],
            "guide_title": "Do not prepare every document at once",
            "guide": ["List the Mainland property, account or company clues.", "Connect the death record to each family member's identity.", "Record whether a will exists and where the original is kept.", "Confirm signing and document requirements in the asset's city."],
            "checks": [("Where is the estate?", "Record the city, address, bank or company name"), ("Who died?", "Check names, dates and the death record"), ("Who may be involved?", "List spouse, children, parents and any will"), ("What is blocking progress?", "Missing records, disagreement, travel or asset tracing")],
            "section_title": "Macau families and Mainland estate matters",
            "section_lead": "Each article answers one practical question, from document checks and family relationships to property and other assets.",
            "upcoming": ["Connecting Macau family records to the heirship file", "What to check first when a will is found", "Defining authority when no one can travel", "Tracing property or accounts from an old address"],
            "facts": ["The deceased's name, date and place of death", "The Mainland city of each property, account or company", "Existing Macau identity, family and will records"],
            "obstacles": ["Family records do not match", "The will or heirs are disputed", "The asset trail is incomplete or no one can travel"],
            "bottom_title": "Separate the person, family and asset files first",
            "bottom_text": "You do not need to predict the outcome before making the records understandable.",
            "cards": [("Property inheritance", "Inheriting Mainland property from Macau: keep the two document files separate", "Separate the Macau family and estate papers from the Mainland property registration file.", "/articles/am/macau-family-mainland-property-inheritance_en.html"), ("Death records", "Using a Macau death record for a Mainland property inheritance", "Identify the document, then separate the death, family and property files.", "/articles/am/macau-death-record-for-mainland-inheritance_en.html")],
        },
    },
    "singapore": {
        "tc": {
            "path": "articles/singapore/index.html",
            "title": "新加坡家屬處理內地遺產，先從哪裏開始 | 劉毅律師團隊",
            "name": "新加坡家屬處理內地遺產，先從哪裏開始",
            "description": "新加坡家屬處理內地房產、存款或股權繼承，先分清遺囑、法院遺產文件、家屬關係和內地資產資料。",
            "eyebrow": "首頁&nbsp;&gt;&nbsp;文章&nbsp;&gt;&nbsp;新加坡繼承專題",
            "h1": "新加坡家屬處理內地遺產<br>先從哪裏開始",
            "lead": "家人在新加坡、遺產在內地時，先確認有沒有有效遺囑、誰能代表遺產，以及房產、存款或股權在哪個內地城市。法院文件和內地資產資料要分開整理。",
            "trust": ["新加坡家屬", "法院遺產文件", "內地房產", "遠程辦理"],
            "guide": [("先看有沒有遺囑", "原件、執行人和家屬意見先記清楚。"), ("再確認誰代表遺產", "遺囑認證和遺產管理文件起點不同。"), ("另做內地資產表", "房產、存款和股權不能只看法院清單。"), ("最後確認跨境使用", "版本、翻譯、附加證明和接收用途逐項問。")],
            "checks": [("遺囑情況", "有沒有有效原件，指定誰做執行人？"), ("法院文件", "已取得哪一種 grant，資產清單是否完整？"), ("內地資產", "涉及哪個城市、登記人和持有方式？"), ("家屬意見", "是否有人反對、失聯或不願提供文件？")],
            "section_title": "新加坡家屬處理內地遺產<br>專題文章",
            "section_lead": "先看最接近目前情況的一篇，分清新加坡遺產程序和內地資產辦理各自回答甚麼。",
            "upcoming": ["Schedule of Assets 沒列內地房產怎樣補", "新加坡死亡文件交內地前先問甚麼", "家人不能回內地時誰來簽署和收件", "有人反對遺囑或申請人時先保存哪些資料"],
            "other_title": "其他地區的內地遺產專題",
            "other": [("/articles/", "香港居民繼承內地房產", "香港"), ("/articles/macau/", "澳門家屬處理內地遺產", "澳門"), ("/articles/united-states/", "美國家屬處理內地遺產", "美國")],
            "bottom_title": "先分清新加坡程序和內地資產",
            "bottom_text": "說明遺囑、法院文件、家屬範圍和內地資產城市，再判斷下一步。",
            "cards": [("房產繼承", "新加坡遺產文件，可以直接辦內地房產過戶嗎", "先分清遺產管理人身份、房屋歸屬和內地登記三層問題。", "/articles/singapore/mainland-property-inheritance.html"), ("法院文件", "新加坡繼承有遺囑和無遺囑，法院文件有甚麼不同", "先看有沒有有效遺囑，再分清誰能代表遺產和內地房產還缺甚麼。", "/articles/singapore/probate-or-letters-of-administration.html")],
        },
        "cn": {
            "path": "articles/singapore/index_cn.html",
            "title": "新加坡家属处理内地遗产，先从哪里开始 | 刘毅律师团队",
            "name": "新加坡家属处理内地遗产，先从哪里开始",
            "description": "新加坡家属处理内地房产、存款或股权继承，先分清遗嘱、法院遗产文件、家属关系和内地资产资料。",
            "h1": "新加坡家属处理内地遗产，先从哪里开始",
            "lead": "家人在新加坡、遗产在内地时，先确认有没有有效遗嘱、谁能代表遗产，以及房产、存款或股权在哪个内地城市。",
            "pills": ["遗嘱与法院文件", "内地资产", "家属意见"],
            "guide_title": "先分清新加坡程序和内地资产",
            "guide": ["有遗嘱先找原件和指定执行人。", "无有效遗嘱先确认谁可以申请管理遗产。", "另做一份内地房产、账户和股权清单。", "最后确认文件版本、翻译和接收要求。"],
            "checks": [("遗嘱情况", "有没有有效原件和指定执行人"), ("法院文件", "已经取得哪一种 grant"), ("内地资产", "城市、登记人和持有方式是什么"), ("家属意见", "是否有人反对、失联或不配合")],
            "section_title": "新加坡家属处理内地遗产专题文章",
            "section_lead": "分清新加坡遗产程序和内地资产办理各自回答什么，再按当前卡点阅读。",
            "upcoming": ["资产清单没有列内地房产怎样补", "新加坡死亡文件交内地前先问什么", "家人不能回内地时谁来签署和收件", "有人反对遗嘱或申请人时先保存哪些资料"],
            "facts": ["是否有有效遗嘱和指定执行人", "现有法院文件与资产清单", "内地房产、账户或公司所在城市"],
            "obstacles": ["遗嘱原件或资产清单不完整", "家属对申请人或分配有争议", "文件跨境使用或签署安排不清楚"],
            "bottom_title": "法院文件不是内地房产过户批文",
            "bottom_text": "先确认谁能代表遗产，再单独核对继承人和内地资产。",
            "cards": [("房产继承", "新加坡遗产文件，可以直接办理内地房产过户吗", "先分清遗产管理人身份、房屋归属和内地登记三层问题。", "/articles/singapore/mainland-property-inheritance_cn.html"), ("法院文件", "新加坡继承有遗嘱和无遗嘱，法院文件有什么不同", "先看有没有有效遗嘱，再分清谁能代表遗产和内地房产还缺什么。", "/articles/singapore/probate-or-letters-of-administration_cn.html")],
        },
        "en": {
            "path": "articles/singapore/index_en.html",
            "title": "Singapore families handling an estate in Mainland China | Liu Yi Lawyer Team",
            "name": "Singapore families handling an estate in Mainland China",
            "description": "Practical articles connecting Singapore probate documents and family records to property, accounts or company interests in Mainland China.",
            "h1": "Singapore families handling an estate in Mainland China",
            "lead": "Start with the will, the person authorised to represent the estate, and the Mainland city where each property, account or company interest is located. Keep the Singapore court file separate from the asset file.",
            "pills": ["Will and court grants", "Mainland assets", "Family positions"],
            "guide_title": "Separate the Singapore process from the asset file",
            "guide": ["With a will, locate the original and named executor.", "Without a valid will, identify who may apply to administer the estate.", "Make a separate list of Mainland property, accounts and shares.", "Confirm document format, translation and overseas-use requirements."],
            "checks": [("Will", "Is there a valid original and a named executor?"), ("Court grant", "Which grant and asset schedule already exist?"), ("Mainland assets", "Which city, registered owner and ownership form?"), ("Family positions", "Does anyone object, refuse records or remain uncontactable?")],
            "section_title": "Singapore families and Mainland estate matters",
            "section_lead": "Understand what the Singapore estate process establishes, then review the Mainland asset and heirship questions separately.",
            "upcoming": ["Adding a Mainland property missing from the asset schedule", "Preparing a Singapore death record for Mainland use", "Signing and receiving documents when no one can travel", "Preserving evidence when the will or applicant is challenged"],
            "facts": ["The will and named executor, if any", "The current grant and Schedule of Assets", "The Mainland city of each property, account or company"],
            "obstacles": ["The original will or asset schedule is incomplete", "The family disputes the applicant or distribution", "Overseas document use or signing remains unclear"],
            "bottom_title": "A Singapore grant is not a Mainland transfer order",
            "bottom_text": "Identify the estate representative first, then review heirship and the Mainland asset separately.",
            "cards": [("Property inheritance", "Can a Singapore probate grant transfer property in Mainland China?", "Separate the personal representative's authority from entitlement and Mainland registration.", "/articles/singapore/mainland-property-inheritance_en.html"), ("Court grants", "Singapore probate with or without a will: which grant applies?", "Start with the will, then separate authority to act from the Mainland property file.", "/articles/singapore/probate-or-letters-of-administration_en.html")],
        },
    },
    "united-states": {
        "tc": {
            "path": "articles/united-states/index.html",
            "title": "美國家屬處理內地遺產，先從哪裏開始 | 劉毅律師團隊",
            "name": "美國家屬處理內地遺產，先從哪裏開始",
            "description": "美國家屬處理內地房產、存款或股權繼承，先核對文件簽發州、正式版本、姓名銜接、家屬範圍和內地資產城市。",
            "eyebrow": "首頁&nbsp;&gt;&nbsp;文章&nbsp;&gt;&nbsp;美國繼承專題",
            "h1": "美國家屬處理內地遺產<br>先從哪裏開始",
            "lead": "家人在美國、遺產在內地時，先核對死亡證明或遺囑由哪一州簽發、姓名是否能和內地舊資料對上，再把房產、存款或公司權益按城市列清。",
            "trust": ["美國家屬", "州簽發文件", "內地遺產", "遠程辦理"],
            "guide": [("先看文件簽發州", "死亡證明、法院文件和公證文件來源不同。"), ("再連接同一身份", "中英文姓名、舊證件和地址逐項對照。"), ("另做內地資產表", "房產、賬戶和公司權益按城市整理。"), ("最後安排跨境使用", "正式副本、附加證明、翻譯和簽署按用途做。")],
            "checks": [("文件從哪州來", "先記簽發機關、日期和正式副本情況。"), ("姓名能否對上", "中英文寫法、舊證件和內地登記要能銜接。"), ("遺產在哪", "列出內地城市、地址、賬戶或公司名稱。"), ("家屬怎樣參與", "誰能簽署、誰有爭議、誰暫時聯絡不到。")],
            "section_title": "美國家屬處理內地遺產<br>專題文章",
            "section_lead": "文章按美國文件、家屬關係、內地房產與其他資產、遠程簽署逐步增加。",
            "upcoming": ["死亡證明由不同州簽發，附加證明找誰辦", "美國法院遺產文件能證明甚麼", "中英文姓名對不上內地房產登記怎樣整理", "只剩舊地址和銀行信件時怎樣做資產線索表"],
            "other_title": "其他地區的內地遺產專題",
            "other": [("/articles/", "香港居民繼承內地房產", "香港"), ("/articles/macau/", "澳門家屬處理內地遺產", "澳門"), ("/articles/singapore/", "新加坡家屬處理內地遺產", "新加坡")],
            "bottom_title": "先核對文件來源，再安排遠程辦理",
            "bottom_text": "說明所在州、文件簽發州、內地資產城市和家屬情況，不用先判斷結果。",
            "cards": [("房產繼承", "美國死亡證明和遺囑，用於內地房產繼承前先核對甚麼", "先看簽發州、正式版本、姓名對照和內地接收用途。", "/articles/us/us-documents-mainland-property-inheritance.html")],
        },
        "cn": {
            "path": "articles/united-states/index_cn.html",
            "title": "美国家属处理内地遗产，先从哪里开始 | 刘毅律师团队",
            "name": "美国家属处理内地遗产，先从哪里开始",
            "description": "美国家属处理内地房产、存款或股权继承，先核对文件签发州、正式版本、姓名衔接、家属范围和内地资产城市。",
            "h1": "美国家属处理内地遗产，先从哪里开始",
            "lead": "家人在美国、遗产在内地时，先核对死亡证明或遗嘱由哪一州签发、姓名能否和内地旧资料对应，再把房产、存款或公司权益按城市列清。",
            "pills": ["州签发文件", "姓名与身份", "内地资产"],
            "guide_title": "先核对文件来源，再谈远程办理",
            "guide": ["记录死亡证明或法院文件的签发州。", "对照中英文姓名、旧证件和内地登记。", "另做内地房产、账户和股权清单。", "按接收用途准备正式副本、翻译和附加证明。"],
            "checks": [("文件来自哪一州", "记录签发机关、日期和正式副本"), ("姓名能否对应", "中英文写法、旧证件和地址逐项连接"), ("内地遗产在哪里", "列出城市、地址、账户或公司名称"), ("家属怎样参与", "谁能签署、谁有争议、谁联系不到")],
            "section_title": "美国家属处理内地遗产专题文章",
            "section_lead": "文章按美国文件、家属关系、内地房产和其他资产、远程签署逐步增加。",
            "upcoming": ["死亡证明由不同州签发，附加证明找谁办理", "美国法院遗产文件能证明什么", "中英文姓名对不上内地房产登记怎样整理", "只剩旧地址和银行信件时怎样做资产线索表"],
            "facts": ["文件签发州、签发机关和正式版本", "逝者中英文姓名与旧身份资料", "内地房产、账户或公司所在城市"],
            "obstacles": ["姓名或证件资料无法衔接", "不知道哪一种文件需要附加证明", "家属分散、资产线索旧或不能到场"],
            "bottom_title": "不要先把所有美国文件都做一遍",
            "bottom_text": "先确认接收城市和具体用途，再安排正式副本、翻译和附加证明。",
            "cards": [("房产继承", "美国死亡证明和遗嘱，用于内地房产继承前先核对什么", "先看签发州、正式版本、姓名对照和内地接收用途。", "/articles/us/us-documents-mainland-property-inheritance_cn.html")],
        },
        "en": {
            "path": "articles/united-states/index_en.html",
            "title": "U.S. families handling an estate in Mainland China | Liu Yi Lawyer Team",
            "name": "U.S. families handling an estate in Mainland China",
            "description": "Practical articles for U.S. families connecting state-issued records, names and family evidence to property, accounts or company interests in Mainland China.",
            "h1": "U.S. families handling an estate in Mainland China",
            "lead": "Begin with the state that issued each death, court or notarised record. Then connect English and Chinese names to the old Mainland records and list each property, account or company interest by city.",
            "pills": ["Issuing state", "Names and identity", "Mainland assets"],
            "guide_title": "Check the source before planning remote work",
            "guide": ["Record the issuing state and authority for each document.", "Connect English and Chinese names, old IDs and addresses.", "Create a separate list of Mainland property, accounts and shares.", "Prepare official copies, apostilles and translations for a defined use."],
            "checks": [("Which state issued it?", "Record the authority, date and official-copy status"), ("Do the names connect?", "Match English, Chinese, old IDs and addresses"), ("Where are the assets?", "List the city, address, account or company"), ("How will the family act?", "Identify signers, disagreements and missing relatives")],
            "section_title": "U.S. families and Mainland estate matters",
            "section_lead": "Articles will progress from U.S. records and family evidence to Mainland property, other assets and remote signing.",
            "upcoming": ["Which authority apostilles a state-issued death certificate?", "What a U.S. probate order does and does not establish", "Connecting English names to a Mainland property record", "Tracing assets from an old address or bank letter"],
            "facts": ["The issuing state, authority and official document version", "The deceased's English and Chinese names and old identity records", "The Mainland city of each property, account or company"],
            "obstacles": ["Names or identity records do not connect", "The correct apostille route is unclear", "Relatives are dispersed, assets are old or no one can travel"],
            "bottom_title": "Do not authenticate every U.S. document first",
            "bottom_text": "Confirm the Mainland recipient and purpose before ordering copies, apostilles and translations.",
            "cards": [("Property inheritance", "Using a U.S. death certificate or will for a Mainland China property inheritance", "Start with the issuing state, official copy, identity match and Mainland purpose.", "/articles/us/us-documents-mainland-property-inheritance_en.html")],
        },
    },
}


def _render_cards(cards: list[tuple[str, str, str, str]], style: str, read_label: str) -> str:
    if style == "v24":
        return "".join(
            f'<a href="{href}"><span class="v24-tag">{label}</span><strong>{title}</strong><p>{summary}</p></a>'
            for label, title, summary, href in cards
        )
    return "".join(
        f'<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">{label}</span><h3>{title}</h3><p>{summary}</p></div><a class="v25-pill-action" href="{href}">{read_label}</a></article>'
        for label, title, summary, href in cards
    )


def _render_v24_hub(copy: dict, topic: str) -> str:
    guide = "".join(f'<li><span>0{i}</span><strong>{title}</strong><p>{body}</p></li>' for i, (title, body) in enumerate(copy["guide"], 1))
    checks = "".join(f'<article><span>0{i}</span><h3>{title}</h3><p>{body}</p></article>' for i, (title, body) in enumerate(copy["checks"], 1))
    trust = "".join(f'<span><b></b>{item}</span>' for item in copy["trust"])
    upcoming = "".join(f'<span>{item}</span>' for item in copy["upcoming"])
    other = "".join(f'<a href="{href}"><strong>{title}</strong><span>{label}</span></a>' for href, title, label in copy["other"])
    cards = _render_cards(copy["cards"], "v24", "")
    return f'''
    <section class="v24-hero" aria-labelledby="hero-title"><article class="v24-hero-card"><p class="v24-breadcrumb">{copy["eyebrow"]}</p><h1 id="hero-title">{copy["h1"]}</h1><p class="v24-hero-lead">{copy["lead"]}</p><div class="v24-actions"><a class="v24-primary" href="#published">查看已發布文章</a><a class="v24-secondary" href="/ask/gpt/?topic={topic}&amp;source=article-topic-hero">說明你的情況</a></div><div class="v24-trust-row" aria-label="專題範圍">{trust}</div></article><aside class="v24-guide" aria-labelledby="guide-title"><div class="v24-guide-head"><h2 id="guide-title">專題導讀</h2><span>衡</span></div><ol>{guide}</ol><a href="/ask/gpt/?topic={topic}&amp;source=article-topic-guide">諮詢 AI 法律助手</a></aside></section>
    <section class="v24-checks" aria-labelledby="checks-title"><div class="v24-checks-title"><h2 id="checks-title">先確認四件事</h2><p>先把事實分開，不用先懂法律術語。</p></div>{checks}</section>
    <section class="v24-article-board" id="published" aria-labelledby="article-index-title"><div class="v24-article-intro"><h2 id="article-index-title">{copy["section_title"]}</h2><p>{copy["section_lead"]}</p><a href="/ask/gpt/?topic={topic}&amp;source=article-topic-board">不知道先看哪篇</a></div><div class="v24-table" aria-label="專題文章"><div class="v24-table-head"><span>分類</span><span>文章標題</span><span>摘要</span></div>{cards}<details class="v24-article-more" open><summary>接下來會整理的問題 <span>{len(copy["upcoming"])} 個方向</span></summary><div class="topic-upcoming-grid">{upcoming}</div></details></div><aside class="v24-other" aria-labelledby="other-title"><h2 id="other-title">{copy["other_title"]}</h2>{other}<a class="v24-more" href="/ask/gpt/?topic={topic}&amp;source=article-topic-more">說明逝者、家屬和資產</a></aside></section>
    <section class="v24-bottom-cta" aria-label="諮詢入口"><div><span>衡</span><h2>{copy["bottom_title"]}</h2><p>{copy["bottom_text"]}</p></div><a href="/ask/gpt/?topic={topic}&amp;source=article-topic-footer">諮詢 AI 法律助手</a></section>
  '''


def _render_v25_hub(copy: dict, topic: str, lang: str) -> str:
    is_en = lang == "en"
    read_label = "Read Article" if is_en else "阅读文章"
    guide = "".join(f"<li>{item}</li>" for item in copy["guide"])
    pills = "".join(f"<span>{item}</span>" for item in copy["pills"])
    checks = "".join(f'<article><span>0{i}</span><strong>{title}</strong><p>{body}</p></article>' for i, (title, body) in enumerate(copy["checks"], 1))
    cards = _render_cards(copy["cards"], "v25", read_label)
    upcoming = "".join(f"<span>{item}</span>" for item in copy["upcoming"])
    facts = "".join(f"<li>{item}</li>" for item in copy["facts"])
    obstacles = "".join(f"<li>{item}</li>" for item in copy["obstacles"])
    if is_en:
        view_label, explain_label = "View Published Articles", "Tell Us About the Estate"
        check_title, check_text = "Which part looks most like your situation?", "Choose the issue that is blocking the family now."
        article_more = "Questions being prepared next"
        other_title, other_text = "Other regional estate topics", "Continue with the family's location."
        fact_title, obstacle_title = "Basic facts", "The immediate obstacle"
        side_title, side_text = "Write down these facts first", "A complete file is not required before the situation can be understood."
        other_links = [("/articles/index_en.html", "Hong Kong families inheriting Mainland property"), ("/articles/macau/index_en.html", "Macau families handling a Mainland estate"), ("/articles/singapore/index_en.html", "Singapore families handling a Mainland estate"), ("/articles/united-states/index_en.html", "U.S. families handling a Mainland estate")]
        ask_label = "Ask AI Legal Assistant"
        eyebrow = f'{copy["name"].split(" handling")[0]} / Article hub'
        direction_label = f'{len(copy["upcoming"])} directions'
    else:
        view_label, explain_label = "查看已发布文章", "说明遗产情况"
        check_title, check_text = "看看哪一步最像你现在的情况", "先选出目前真正卡住家属的一步。"
        article_more = "接下来会整理的问题"
        other_title, other_text = "其他地区的内地遗产专题", "按家属所在地继续阅读。"
        fact_title, obstacle_title = "基本事实", "当前最难的一步"
        side_title, side_text = "咨询前先写下这些信息", "不用先把全部材料准备好，先让逝者、家属和资产能够被理解。"
        suffix = "_cn.html"
        other_links = [("/articles/index_cn.html", "香港居民继承内地房产"), (f"/articles/macau/index{suffix}", "澳门家属处理内地遗产"), (f"/articles/singapore/index{suffix}", "新加坡家属处理内地遗产"), (f"/articles/united-states/index{suffix}", "美国家属处理内地遗产")]
        ask_label = "咨询 AI 法律助手"
        eyebrow = f'{copy["name"].split("，")[0]}专题 / 文章入口'
        direction_label = f'{len(copy["upcoming"])} 个方向'
    current = copy["path"]
    other = "".join(f'<a class="v25-other-card" href="{href}"><strong>{title}</strong></a>' for href, title in other_links if href.lstrip("/") != current)
    return f'''
    <section class="v25-hero" aria-labelledby="hero-title"><article class="v25-hero-main"><p class="v25-eyebrow">{eyebrow}</p><h1 id="hero-title">{copy["h1"]}</h1><p class="v25-lead">{copy["lead"]}</p><div class="v25-pills">{pills}</div></article><aside class="v25-hero-side"><h2>{copy["guide_title"]}</h2><ol>{guide}</ol><div class="v25-hero-actions"><a class="v25-primary" href="#published">{view_label}</a><a class="v25-secondary" href="/ask/gpt/?topic={topic}&amp;source=article-topic-hero">{explain_label}</a></div></aside></section>
    <section class="v25-checkbar"><div class="v25-checkbar-intro"><h2>{check_title}</h2><p>{check_text}</p></div><div class="v25-check-items">{checks}</div></section>
    <section class="v25-content" id="published"><div class="v25-main"><div class="v25-section-copy"><h2>{copy["section_title"]}</h2><p>{copy["section_lead"]}</p></div>{cards}<details class="v25-article-more" open><summary>{article_more} <span>{direction_label}</span></summary><div class="topic-upcoming-grid">{upcoming}</div></details><section class="v25-other-topics"><div class="v25-section-copy"><h2>{other_title}</h2><p>{other_text}</p></div><div class="v25-other-grid">{other}</div></section></div><aside class="v25-side"><section class="v25-side-card"><h2>{side_title}</h2><p>{side_text}</p><h3>{fact_title}</h3><ul>{facts}</ul><h3>{obstacle_title}</h3><ul>{obstacles}</ul></section><section class="v25-side-card v25-side-actions"><h2>{'Not sure what to read first?' if is_en else '还不知道先看哪篇'}</h2><div class="v25-side-buttons"><a class="v25-primary" href="/ask/gpt/?topic={topic}&amp;source=article-topic-side">{ask_label}</a></div></section></aside></section>
    <section class="v25-bottom-cta"><h2>{copy["bottom_title"]}</h2><p>{copy["bottom_text"]}</p></section>
  '''


def update_hub_positioning() -> None:
    for topic, languages in HUB_INHERITANCE_COPY.items():
        for lang, copy in languages.items():
            path = ROOT / copy["path"]
            text = path.read_text(encoding="utf-8")
            text = text.replace("/articles/style.css?v=20260724-topic-v28", "/articles/style.css?v=20260724-topic-v29")
            text, title_count = re.subn(r"<title>.*?</title>", f'<title>{copy["title"]}</title>', text, count=1)
            text, desc_count = re.subn(r'<meta name="description" content=".*?">', f'<meta name="description" content="{copy["description"]}">', text, count=1)
            json_pattern = r'<script type="application/ld\+json">(.*?)</script>'
            match = re.search(json_pattern, text, flags=re.S)
            if not match:
                raise RuntimeError(f"CollectionPage JSON-LD missing: {copy['path']}")
            data = json.loads(match.group(1))
            data["name"] = copy["name"]
            data["description"] = copy["description"]
            data["dateModified"] = TODAY
            json_ld = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            text = text[: match.start(1)] + json_ld + text[match.end(1) :]
            body = _render_v24_hub(copy, topic) if lang == "tc" else _render_v25_hub(copy, topic, lang)
            text, body_count = re.subn(r"(?<=</header>).*?(?=</main>)", body, text, count=1, flags=re.S)
            if title_count != 1 or desc_count != 1 or body_count != 1:
                raise RuntimeError(f"Hub positioning update failed: {copy['path']}")
            path.write_text(text, encoding="utf-8")


def update_hubs() -> None:
    for relative_path, card in HUB_CARDS.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if card in text:
            continue
        marker = '<details class="v24-article-more">' if "index.html" in relative_path and "index_" not in relative_path else '<details class="v25-article-more"'
        if marker not in text:
            raise RuntimeError(f"Hub insertion marker missing: {relative_path}")
        text = text.replace(marker, card + marker, 1)
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
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hub_positioning()
    update_sitemap()
