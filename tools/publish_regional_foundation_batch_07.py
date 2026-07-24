from __future__ import annotations

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
        "slug": "singapore-family-first-fact-sheet",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_SG",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡與內地遺產",
                "title": "新加坡家屬第一次整理內地遺產，一頁事實表要寫甚麼",
                "description": "新加坡家屬第一次處理內地房產、存款或公司權益時，用一頁事實表分清逝者、代表人、家屬和資產線索。",
                "lead": "不用先把所有證明辦好。先用一頁紙回答四件事：誰離世、誰在處理、家裏有哪些人、內地有哪些資產線索。",
                "key_title": "這一頁先回答四件事",
                "keys": [
                    "逝者近年的生活中心和現有新加坡文件",
                    "誰是遺囑執行人或正在申請管理遺產",
                    "家屬關係、聯絡情況和目前意見",
                    "每項內地資產的城市、姓名和證明線索",
                ],
                "visuals": [
                    ("先分人物和資產", "逝者、處理人和家屬", "每項內地資產", "先分成兩類，再在一頁內各自寫清。"),
                    ("先整理，再選程序", "確認人和文件", "逐項列資產", "圈出目前卡點", "這張表用來問對問題，不是法院表格。"),
                    ("每條資料標記來源", "已見原件", "只有影像", "家人記憶", "待機構核對", "不把聽說的內容寫成已確認事實。"),
                ],
                "answer_title": "先說最實用的答案",
                "answer": [
                    "這張一頁事實表不是新加坡法院的 Schedule of Assets，也不是用來決定誰一定繼承。它是家屬第一次溝通時的工作紙，目的是把逝者、遺產處理人、家屬關係和每項內地資產放在同一頁，讓律師或接收機構看得懂目前缺甚麼。",
                    "新加坡的遺產程序會確認誰可作為遺囑執行人或遺產管理人，正式申請也會涉及法院資產清單（Schedule of Assets）；但內地房產、賬戶或公司仍要按資產所在地逐項處理。先把兩邊資料連起來，比一開始大量翻譯文件更有用。",
                ],
                "sections": [
                    (
                        "第一格寫逝者，不要只抄死亡證明",
                        [
                            "先寫中英文姓名、曾用姓名、出生和離世日期、近年實際生活中心，以及是否留下遺囑。死亡證明上的地址只是其中一條資料；如果逝者長期在新加坡和內地兩地生活，把每段時間和原因一併記下。",
                            "再列現有新加坡文件：死亡記錄、遺囑原件、法院申請編號、Grant 或正在準備的 Schedule of Assets。只寫文件名稱、日期、簽發或提交方和保管人，不要把整份文件內容塞進這一頁。",
                        ],
                    ),
                    (
                        "第二格寫誰在處理，第三格畫家屬關係",
                        [
                            "有遺囑時，寫明遺囑指定的執行人和目前是否已取得法院簽發的代表文件（Grant）；沒有遺囑時，寫明誰正在申請管理遺產。正在申請不等於已獲任命，未取得相應文件前，不要把申請人寫成已獲任的管理人。",
                            "家屬關係用一行一人：姓名、與逝者關係、所在國家或城市、是否能聯絡、是否已看過遺囑或資產資料。家屬有不同說法時，分別記錄，不要先由一名聯絡人代替所有人作結論。",
                        ],
                    ),
                    (
                        "第四格每項內地資產只佔一行",
                        [
                            "房產寫城市、地址或小區、登記姓名、共有情況和證書或合同線索；存款寫銀行和分行線索，不在家族群組公開完整賬號；公司權益寫公司名稱、登記城市和已知股東資料。暫時不知道價值，可以留空，不要猜一個數字。",
                            "新加坡正式資產清單和這張家屬工作紙用途不同。正式清單由申請人按法院要求準確申報；法院樣表中的境外財產欄，明確以逝者去世時以新加坡為住所地的情況為前提。個案是否填寫及怎樣填，仍要按實際案件和現行表格確認。",
                        ],
                    ),
                    (
                        "最後只圈出一個目前卡點",
                        [
                            "卡點可能是找不到遺囑原件、尚未確定誰代表遺產、家屬失聯、內地房產城市不清楚，或姓名對不上。一次只圈最先要解決的一項，旁邊寫負責人和下一個核對對象。",
                            "把原件、影像、家人記憶和待機構確認分開標記。如果有人反對遺囑、否認某項資產、拒絕交文件，或代表人身份已有爭議，這張表仍可保留事實，但不應用它代替正式法律意見。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "有遺囑和無遺囑時法院文件有甚麼不同"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "內地房產有沒有列入 Schedule of Assets"),
                    ("/articles/singapore/domicile-and-mainland-asset-location.html", "住所和內地資產所在地分別影響甚麼"),
                ],
                "cta": "先把四個區塊寫滿到目前知道的程度，再判斷下一步應找文件、問家人，還是向資產所在地核對。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡与内地遗产",
                "title": "新加坡家属第一次整理内地遗产，一页事实表要写什么",
                "description": "新加坡家属第一次处理内地房产、存款或公司权益时，用一页事实表分清逝者、代表人、家属和资产线索。",
                "lead": "不用先把所有证明办好。先用一页纸回答四件事：谁去世、谁在处理、家里有哪些人、内地有哪些资产线索。",
                "key_title": "这一页先回答四件事",
                "keys": [
                    "逝者近年的生活中心和现有新加坡文件",
                    "谁是遗嘱执行人或正在申请管理遗产",
                    "家属关系、联系情况和目前意见",
                    "每项内地资产的城市、姓名和证明线索",
                ],
                "visuals": [
                    ("先分人物和资产", "逝者、处理人和家属", "每项内地资产", "先分成两类，再在一页内分别写清。"),
                    ("先整理，再选程序", "确认人和文件", "逐项列资产", "圈出当前卡点", "这张表用于问对问题，不是法院表格。"),
                    ("每条资料标记来源", "已见原件", "只有影像", "家人记忆", "待机构核对", "不把听说的内容写成已确认事实。"),
                ],
                "answer_title": "先说最实用的答案",
                "answer": [
                    "这张一页事实表不是新加坡法院的 Schedule of Assets，也不是用来决定谁一定继承。它是家属第一次沟通时的工作纸，目的是把逝者、遗产处理人、家属关系和每项内地资产放在同一页，让律师或接收机构看懂目前缺什么。",
                    "新加坡的遗产程序会确认谁可以作为遗嘱执行人或遗产管理人，正式申请也会涉及法院资产清单（Schedule of Assets）；但内地房产、账户或公司仍要按资产所在地逐项处理。先把两边资料连起来，比一开始大量翻译文件更有用。",
                ],
                "sections": [
                    (
                        "第一格写逝者，不要只抄死亡证明",
                        [
                            "先写中英文姓名、曾用姓名、出生和去世日期、近年实际生活中心，以及是否留下遗嘱。死亡证明上的地址只是其中一条资料；如果逝者长期在新加坡和内地两地生活，把每段时间和原因一起记下。",
                            "再列现有新加坡文件：死亡记录、遗嘱原件、法院申请编号、Grant 或正在准备的 Schedule of Assets。只写文件名称、日期、签发或提交方和保管人，不要把整份文件内容塞进这一页。",
                        ],
                    ),
                    (
                        "第二格写谁在处理，第三格画家属关系",
                        [
                            "有遗嘱时，写明遗嘱指定的执行人和目前是否已经取得法院签发的代表文件（Grant）；没有遗嘱时，写明谁正在申请管理遗产。正在申请不等于已经获任，未取得相应文件前，不要把申请人写成已经获任的管理人。",
                            "家属关系一行一人：姓名、与逝者关系、所在国家或城市、是否能联系、是否看过遗嘱或资产资料。家属有不同说法时分别记录，不要先由一名联系人替所有人下结论。",
                        ],
                    ),
                    (
                        "第四格每项内地资产只占一行",
                        [
                            "房产写城市、地址或小区、登记姓名、共有情况和证书或合同线索；存款写银行和分行线索，不在家族群里公开完整账号；公司权益写公司名称、登记城市和已知股东资料。暂时不知道价值可以留空，不要猜一个数字。",
                            "新加坡正式资产清单和这张家属工作纸用途不同。正式清单由申请人按法院要求准确申报；法院样表中的境外财产栏，明确以逝者去世时以新加坡为住所地的情况为前提。个案是否填写以及怎样填，仍要按实际案件和现行表格确认。",
                        ],
                    ),
                    (
                        "最后只圈出一个当前卡点",
                        [
                            "卡点可能是找不到遗嘱原件、还没确定谁代表遗产、家属失联、内地房产城市不清楚，或姓名对不上。一次只圈最先要解决的一项，旁边写负责人和下一个核对对象。",
                            "把原件、影像、家人记忆和待机构确认分开标记。如果有人反对遗嘱、否认某项资产、拒绝交文件，或代表人身份已有争议，这张表仍可以保留事实，但不能代替正式法律意见。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "有遗嘱和无遗嘱时法院文件有什么不同"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "内地房产有没有列入 Schedule of Assets"),
                    ("/articles/singapore/domicile-and-mainland-asset-location_cn.html", "住所和内地资产所在地分别影响什么"),
                ],
                "cta": "先把四个区块写到目前知道的程度，再判断下一步应该找文件、问家人，还是向资产所在地核对。",
            },
            "en": {
                "lang": "en",
                "locale": "en_SG",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore and Mainland estates",
                "title": "A One-Page Estate Fact Sheet for a Singapore Family with Mainland Assets",
                "description": "A practical one-page fact sheet for Singapore families organising a Mainland property, bank account or company interest after a death.",
                "lead": "A complete legal file is not the first requirement. Start with one page that identifies the deceased, the person handling the estate, the family and each Mainland asset clue.",
                "key_title": "Put four things on one page",
                "keys": [
                    "The deceased's recent home base and current Singapore papers",
                    "The executor, administrator or current applicant",
                    "The family members, contact status and different accounts",
                    "One row for every known or possible Mainland asset",
                ],
                "visuals": [
                    ("Separate people from assets", "Deceased, representative, family", "Each Mainland asset", "Use two clear groups, then complete both on one page."),
                    ("Organise before choosing a route", "Identify people and papers", "List each asset", "Circle one obstacle", "This is a working sheet, not a court form."),
                    ("Label the source of every fact", "Original seen", "Image only", "Family memory", "Institution to confirm", "Do not present recollection as verified evidence."),
                ],
                "answer_title": "The practical answer",
                "answer": [
                    "This one-page fact sheet is not the Singapore court's Schedule of Assets and it does not decide who inherits. It is a family working document. Its job is to show the deceased, the estate representative, the family structure and each Mainland asset in a form that a lawyer or receiving institution can understand quickly.",
                    "A Singapore grant identifies the executor or administrator who may manage the estate, and the court process also uses a Schedule of Assets. Mainland property, accounts and company interests still have to be addressed asset by asset where they are held. The first page should connect the two files without pretending they are one procedure.",
                ],
                "sections": [
                    (
                        "Block one: describe the deceased, not only the death certificate",
                        [
                            "Record every known English and Chinese name, former names, birth and death dates, the recent stable home base and whether a will has been found. An address on a death record is one clue, not a complete answer. If the deceased spent substantial time in both Singapore and Mainland China, note the periods and reasons.",
                            "List the Singapore papers already held: death record, original will, court case number, grant, or a Schedule of Assets being prepared. On this page, record only the document name, date, issuing or filing party and current holder. Keep the underlying documents in a separate indexed folder.",
                        ],
                    ),
                    (
                        "Block two: identify the representative; block three: map the family",
                        [
                            "If there is a will, name the executor and state whether a grant has been issued. If there is no will, record who is applying to administer the estate. An applicant is not yet an appointed administrator. Until the relevant grant is issued, the sheet must not describe that person as already appointed.",
                            "Give each family member one line: name, relationship, country or city, contact status, and whether that person has seen the will or asset records. Preserve different accounts where relatives disagree. The family coordinator should not silently turn one person's memory into the family's agreed position.",
                        ],
                    ),
                    (
                        "Block four: give every Mainland asset one row",
                        [
                            "For property, record the city, estate or address, registered name, possible co-owner and title or contract clue. For a bank account, record the bank and branch clue without circulating a full account number in a family chat. For a company interest, record the company name, registration city and known shareholder evidence. Leave an unknown value blank rather than inventing one.",
                            "The formal Singapore asset schedule and the family fact sheet do different jobs. In the court's sample form, the section for property outside Singapore is framed for a deceased person domiciled in Singapore at death. Whether and how that section applies must be checked against the actual case and current form; the working sheet may still keep clearly labelled leads.",
                        ],
                    ),
                    (
                        "Finish by circling one immediate obstacle",
                        [
                            "The obstacle may be a missing original will, an unresolved representative, an unreachable relative, an uncertain Mainland city or a name mismatch. Circle only the first issue that prevents progress, then write the person responsible and the institution or record to check next.",
                            "Use separate labels for an original seen, an image, family memory and information awaiting institutional confirmation. If someone challenges the will, denies an asset, withholds documents or disputes the representative, the sheet remains useful as a factual record but cannot replace advice on the contested matter.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore estate topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling Mainland estate matters"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Probate and administration when there is or is not a will"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Checking a Mainland property in the Schedule of Assets"),
                    ("/articles/singapore/domicile-and-mainland-asset-location_en.html", "Domicile and the location of a Mainland asset"),
                ],
                "cta": "Complete the four blocks with what is genuinely known, then decide whether the next step is finding a record, asking a relative or checking with the asset holder.",
            },
        },
    },
    {
        "slug": "mainland-asset-omitted-from-probate",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國與內地遺產",
                "title": "美國遺產文件沒有寫內地資產，家屬先怎樣核對",
                "description": "美國遺產文件沒有列出內地房產、存款或公司權益時，先分清文件種類、州程序、資產權屬和內地辦理位置。",
                "lead": "手上明明有美國法院文件，家人卻知道內地還有房產或賬戶。先不要把「文件沒寫」理解成「資產不存在」或「已經處理完」。",
                "key_title": "先核對四件事",
                "keys": [
                    "這是遺囑、申請、資產清單、Grant 還是結案文件",
                    "案件在哪個州和縣，現在是否已結束",
                    "內地資產登記在誰名下，有沒有共有或指定安排",
                    "是否要補充美國文件，或先向內地接收方問用途",
                ],
                "visuals": [
                    ("先分文件和資產", "美國案件文件", "內地資產記錄", "兩邊資料要連接，但不能互相代替。"),
                    ("兩條工作線要並行", "核對美國案件", "核對內地資產", "再決定如何銜接", "美國文件不會自動替內地資產完成登記。"),
                    ("一項資產寫一行", "城市與地址", "登記姓名", "權屬證明", "美國文件位置", "先把事實連上，再判斷是否補充程序。"),
                ],
                "answer_title": "先說結論",
                "answer": [
                    "美國遺產（probate）材料沒有寫內地資產，不足以單獨證明那項資產不存在、不是遺產，或已經分配完。遺囑、最初申請、資產清單、任命執行人或管理人的文件和結案材料，各自回答不同問題；要先確認你看的文件種類和案件階段。",
                    "美國各州程序不同。有些法院資料明確要求受任人申報資產，也有州或縣提供發現新增資產後補充文件或重新取得證明的安排。是否需要修改、補交或重開，要由案件所在州的程序和這項內地資產的用途決定，不能套用一個全美答案。",
                ],
                "sections": [
                    (
                        "第一步：找出是哪一頁沒有寫",
                        [
                            "遺囑可能只用『其餘財產』等概括文字；最初申請可能只填估算；資產清單才較集中列出遺產資料；Grant 或任命文件主要確認誰有權管理；結案或分配材料則反映當時向法院提交的處理結果。不要只看文件封面。",
                            "在一張表上寫文件名稱、州、縣、案號、提交日期、簽署人和資產出現的頁碼。若沒有完整卷宗，先向原承辦律師、執行人或法院查清有哪些文件，不要從一張掃描件推斷整個案件。",
                        ],
                    ),
                    (
                        "第二步：另做一行內地資產事實",
                        [
                            "寫清資產城市、地址或機構、登記姓名、共有情況、取得時間、現有證書或賬戶線索，以及家屬何時發現。房產只登記逝者一人、多人共有、設有按揭或已被他人使用，後續問題都不同。",
                            "同時查明它為甚麼沒出現在美國材料：當時家屬不知道、只列美國境內資產、文件使用概括描述、資產被誤認為非 probate 資產，或案件結束後才找到。這些是待核對原因，不要先把責任歸給某一個家屬。",
                        ],
                    ),
                    (
                        "第三步：向案件所在州問是否需要補充",
                        [
                            "美國 probate 由州和當地法院程序管理。官方法院資料顯示，資產清單、補充申報和案件結束後發現新增資產的處理方式會因州甚至縣的表格而不同。有些情況可以由原受任人補交資料或取得額外證明，有些則要先處理受任人的權限或重新開啟程序。",
                            "帶着一頁問題去問：案件是否仍在進行、原執行人或管理人是否仍有權限、哪份文件需要更新、新增資產是否影響通知、分配或稅務申報。這一步由熟悉案件所在州的人判斷，不能只向內地機構問美國法院應怎樣改。",
                        ],
                    ),
                    (
                        "第四步：再問內地資產所在地需要甚麼",
                        [
                            "內地房產登記、銀行或公司不會因美國卷宗補了一行就自動辦完。應先向實際接收機構說明：逝者姓名、資產城市、現有美國代表文件、遺囑和家屬關係，並問清那份美國文件要證明的是代表權、遺囑內容，還是其他事實。",
                            "如果美國案件已結束、原執行人不能再處理、家屬對資產歸屬有爭議，或內地登記姓名與美國文件無法連接，應把美國程序和內地辦理分成兩張任務表。先解決會卡住下一步的問題，不要把所有文件一次做翻譯和證明。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/remote-china-lawyer.html", "人在美國處理內地繼承哪些可遠程做"),
                    ("/articles/us/domicile-and-mainland-asset-location.html", "住所州和內地資產所在地分別影響甚麼"),
                    ("/articles/us/us-documents-mainland-property-inheritance.html", "美國死亡證明和遺囑用於內地房產前先核對甚麼"),
                ],
                "cta": "先找出文件種類、州縣和案件階段，再把內地資產單獨寫一行，才知道應先補美國卷宗還是先問內地用途。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国与内地遗产",
                "title": "美国遗产文件没有写内地资产，家属先怎样核对",
                "description": "美国遗产文件没有列出内地房产、存款或公司权益时，先分清文件种类、州程序、资产权属和内地办理地点。",
                "lead": "手上明明有美国法院文件，家人却知道内地还有房产或账户。先不要把‘文件没写’理解成‘资产不存在’或‘已经处理完’。",
                "key_title": "先核对四件事",
                "keys": [
                    "这是遗嘱、申请、资产清单、Grant 还是结案文件",
                    "案件在哪个州和县，现在是否已经结束",
                    "内地资产登记在谁名下，有没有共有或指定安排",
                    "是否要补充美国文件，或先向内地接收方问用途",
                ],
                "visuals": [
                    ("先分文件和资产", "美国案件文件", "内地资产记录", "两边资料要连接，但不能相互代替。"),
                    ("两条工作线并行", "核对美国案件", "核对内地资产", "再决定如何衔接", "美国文件不会自动替内地资产完成登记。"),
                    ("一项资产写一行", "城市和地址", "登记姓名", "权属证明", "美国文件位置", "先把事实连上，再判断是否补充程序。"),
                ],
                "answer_title": "先说结论",
                "answer": [
                    "美国遗产（probate）材料没有写内地资产，不足以单独证明那项资产不存在、不是遗产，或已经分配完。遗嘱、最初申请、资产清单、任命执行人或管理人的文件和结案材料，各自回答不同问题；先确认文件种类和案件阶段。",
                    "美国各州程序不同。有些法院资料要求受任人申报资产，也有州或县提供发现新增资产后补充文件或重新取得证明的安排。是否需要修改、补交或重开，要由案件所在州的程序和这项内地资产的用途决定，不能套用一个全美答案。",
                ],
                "sections": [
                    (
                        "第一步：找出是哪一页没有写",
                        [
                            "遗嘱可能只用‘其余财产’等概括文字；最初申请可能只填估算；资产清单才更集中列出遗产资料；Grant 或任命文件主要确认谁有权管理；结案或分配材料反映当时向法院提交的处理结果。不要只看文件封面。",
                            "在一张表上写文件名称、州、县、案号、提交日期、签字人和资产出现的页码。如果没有完整卷宗，先向原承办律师、执行人或法院查清有哪些文件，不要从一张扫描件推断整个案件。",
                        ],
                    ),
                    (
                        "第二步：另做一行内地资产事实",
                        [
                            "写清资产城市、地址或机构、登记姓名、共有情况、取得时间、现有证书或账户线索，以及家属何时发现。房产只登记逝者一人、多人共有、设有按揭或已经被他人使用，后续问题都不同。",
                            "同时查明它为什么没出现在美国材料：当时家属不知道、只列美国境内资产、文件使用概括描述、资产被误认为非 probate 资产，或案件结束后才找到。这些是待核对原因，不要先把责任归给某一个家属。",
                        ],
                    ),
                    (
                        "第三步：向案件所在州问是否需要补充",
                        [
                            "美国 probate 由州和当地法院程序管理。官方法院资料显示，资产清单、补充申报和案件结束后发现新增资产的处理方式会因州甚至县的表格而不同。有些情况可以由原受任人补交资料或取得额外证明，有些要先处理受任人的权限或重新开启程序。",
                            "带一页问题去问：案件是否仍在进行、原执行人或管理人是否仍有权限、哪份文件需要更新、新增资产是否影响通知、分配或税务申报。这一步由熟悉案件所在州的人判断，不能只向内地机构问美国法院应该怎样改。",
                        ],
                    ),
                    (
                        "第四步：再问内地资产所在地需要什么",
                        [
                            "内地房产登记、银行或公司不会因为美国卷宗补了一行就自动办完。先向实际接收机构说明逝者姓名、资产城市、现有美国代表文件、遗嘱和家属关系，并问清那份美国文件要证明的是代表权、遗嘱内容，还是其他事实。",
                            "如果美国案件已经结束、原执行人不能再处理、家属对资产归属有争议，或内地登记姓名与美国文件无法连接，应把美国程序和内地办理分成两张任务表。先解决会卡住下一步的问题，不要把所有文件一次做翻译和证明。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/remote-china-lawyer_cn.html", "人在美国处理内地继承哪些可以远程做"),
                    ("/articles/us/domicile-and-mainland-asset-location_cn.html", "住所州和内地资产所在地分别影响什么"),
                    ("/articles/us/us-documents-mainland-property-inheritance_cn.html", "美国死亡证明和遗嘱用于内地房产前先核对什么"),
                ],
                "cta": "先找出文件种类、州县和案件阶段，再把内地资产单独写一行，才知道应该先补美国卷宗还是先问内地用途。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. and Mainland estates",
                "title": "A Mainland Asset Is Missing from the U.S. Probate Papers: What Should the Family Check?",
                "description": "How to review a U.S. probate file when it does not mention a Mainland property, account or company interest, without assuming the asset disappeared.",
                "lead": "Missing from one probate document does not mean missing from the estate. First identify the document, the state and county, and the stage of the case.",
                "key_title": "Check four things before drawing a conclusion",
                "keys": [
                    "Is this the will, petition, inventory, letters, order or closing paper?",
                    "Which state and county has the case, and is it still open?",
                    "How is the Mainland asset titled and is anyone else named?",
                    "Does the U.S. file need attention, or does the Mainland recipient need a different fact?",
                ],
                "visuals": [
                    ("Separate the file from the asset", "U.S. probate file", "Mainland asset record", "The records must connect, but neither replaces the other."),
                    ("Run two workstreams", "Review the U.S. file", "Verify the Mainland asset", "Connect only what is needed", "A U.S. filing does not automatically change a Mainland record."),
                    ("Give each asset one row", "City and address", "Registered name", "Ownership record", "Location in U.S. file", "Connect the facts before choosing a corrective step."),
                ],
                "answer_title": "The short answer",
                "answer": [
                    "The absence of a Mainland asset from a U.S. probate paper does not, by itself, establish that the asset does not exist, falls outside the estate or has already been distributed. A will, initial petition, inventory, appointment paper and closing account serve different purposes. Identify the document and case stage before interpreting the omission.",
                    "Probate procedure is state-specific. Official court materials in different states show inventory duties and procedures for assets found after an estate was thought to be complete, but the forms and consequences are not uniform. The court file must be reviewed under the state and county handling the case, while the Mainland asset must be checked where it is registered or held.",
                ],
                "sections": [
                    (
                        "Step one: find the exact page where the asset is missing",
                        [
                            "A will may use a broad residuary clause without naming every account or property. An initial petition may contain only an estimate. An inventory is more directly concerned with estate assets. Letters or an appointment order mainly evidence authority, while a closing paper records what was reported and administered at that stage. The cover page is not enough.",
                            "Create a file index with the document name, state, county, case number, filing date, signatory and the pages where assets are described. If the family holds only a scan, ask the former attorney, executor or court record office what else is in the file before treating the scan as the whole proceeding.",
                        ],
                    ),
                    (
                        "Step two: create a separate record for the Mainland asset",
                        [
                            "Record the city, address or institution, registered name, co-ownership, acquisition date, title or account clue and when the family discovered it. A property registered solely to the deceased raises different questions from a co-owned home, mortgaged property or home already occupied by someone else.",
                            "Then list possible explanations for the omission: the family did not know about it; the working list focused on U.S. assets; the document used broad wording; someone treated it as a non-probate asset; or it was found only after the case closed. These are questions to investigate, not accusations against a relative or fiduciary.",
                        ],
                    ),
                    (
                        "Step three: ask the state handling the probate file what must be updated",
                        [
                            "The state and local court control the probate procedure. Official court guidance shows that inventory reporting and later-discovered assets can require different affidavits, certificates, notices or reopening steps depending on the jurisdiction and the status of the fiduciary. There is no reliable nationwide form for every estate.",
                            "Ask whether the case remains open, whether the original executor or administrator still has authority, which filing would change, and whether the new asset affects notice, distribution, accounting or tax work. Those questions belong with counsel or the court process in the state handling the estate, not with the Mainland property office.",
                        ],
                    ),
                    (
                        "Step four: ask what the Mainland asset holder actually needs",
                        [
                            "A corrected U.S. inventory will not automatically transfer a Mainland property or release an account. Tell the actual receiving institution the deceased's names, the asset city, the existing U.S. appointment papers, the will and the family structure. Ask whether the U.S. document is expected to prove authority, the terms of the will or another specific fact.",
                            "If the U.S. case is closed, the former fiduciary lacks current authority, the family disputes the asset, or the names do not connect to the Mainland record, use two separate task lists. Resolve the issue that blocks the next real step before apostilling and translating an entire file.",
                        ],
                    ),
                ],
                "related_title": "Continue with the United States estate topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling Mainland estate matters"),
                    ("/articles/us/remote-china-lawyer_en.html", "What can be handled remotely from the United States"),
                    ("/articles/us/domicile-and-mainland-asset-location_en.html", "Domicile and the location of a Mainland asset"),
                    ("/articles/us/us-documents-mainland-property-inheritance_en.html", "Using U.S. death, will and probate papers for Mainland property"),
                ],
                "cta": "Identify the document, state, county and case stage, then give the Mainland asset one separate row. That shows which side needs the next answer.",
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
            page = render_article(article, lang).replace(
                "</head>",
                "  <style>\n"
                "    .article-regional-inheritance .article-image-grid{grid-template-columns:repeat(2,minmax(0,1fr))}\n"
                "    .article-regional-inheritance .article-image-grid figure:last-child{grid-column:1/-1;width:calc(50% - 8px);justify-self:center}\n"
                "    @media(max-width:700px){.article-regional-inheritance .article-image-grid{grid-template-columns:1fr}.article-regional-inheritance .article-image-grid figure:last-child{grid-column:auto;width:auto}}\n"
                "  </style>\n</head>",
            )
            (target_dir / f"{article['slug']}{suffix}.html").write_text(
                page, encoding="utf-8"
            )
            for index, name in enumerate(("context", "path", "checklist"), start=1):
                svg = visual_svg(article["copy"][lang]["visuals"][index - 1], index)
                svg = (
                    svg.replace(".item{font-size:29px", ".item{font-size:42px")
                    .replace(".compact{font-size:24px", ".compact{font-size:38px")
                    .replace(".small{font-size:23px", ".small{font-size:36px")
                    .replace(".caption{font-size:24px", ".caption{font-size:32px")
                )
                (image_dir / f"{index:02d}-{name}{suffix}.svg").write_text(
                    svg, encoding="utf-8"
                )


HUB_UPDATES = {
    "articles/singapore/index.html": {
        "href": "/articles/singapore/singapore-family-first-fact-sheet.html",
        "card": '<a href="/articles/singapore/singapore-family-first-fact-sheet.html"><span class="v24-tag">第一步</span><strong>新加坡家屬第一次整理內地遺產，一頁事實表要寫甚麼</strong><p>把逝者、處理人、家屬和每項內地資產先放在同一頁。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/singapore/index_cn.html": {
        "href": "/articles/singapore/singapore-family-first-fact-sheet_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">第一步</span><h3>新加坡家属第一次整理内地遗产，一页事实表要写什么</h3><p>把逝者、处理人、家属和每项内地资产先放在同一页。</p></div><a class="v25-pill-action" href="/articles/singapore/singapore-family-first-fact-sheet_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/singapore/index_en.html": {
        "href": "/articles/singapore/singapore-family-first-fact-sheet_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">First step</span><h3>A one-page estate fact sheet for a Singapore family</h3><p>Put the deceased, representative, family and each Mainland asset on one page.</p></div><a class="v25-pill-action" href="/articles/singapore/singapore-family-first-fact-sheet_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index.html": {
        "href": "/articles/us/mainland-asset-omitted-from-probate.html",
        "card": '<a href="/articles/us/mainland-asset-omitted-from-probate.html"><span class="v24-tag">遺漏資產</span><strong>美國遺產文件沒有寫內地資產，家屬先怎樣核對</strong><p>先分清文件種類、案件階段和內地資產登記資料。</p></a>',
        "marker": '<details class="v24-article-more"',
    },
    "articles/united-states/index_cn.html": {
        "href": "/articles/us/mainland-asset-omitted-from-probate_cn.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">遗漏资产</span><h3>美国遗产文件没有写内地资产，家属先怎样核对</h3><p>先分清文件种类、案件阶段和内地资产登记资料。</p></div><a class="v25-pill-action" href="/articles/us/mainland-asset-omitted-from-probate_cn.html">阅读文章</a></article>',
        "marker": '<details class="v25-article-more"',
    },
    "articles/united-states/index_en.html": {
        "href": "/articles/us/mainland-asset-omitted-from-probate_en.html",
        "card": '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Omitted asset</span><h3>A Mainland asset is missing from the U.S. probate papers</h3><p>Identify the document, case stage and Mainland ownership record first.</p></div><a class="v25-pill-action" href="/articles/us/mainland-asset-omitted-from-probate_en.html">Read Article</a></article>',
        "marker": '<details class="v25-article-more"',
    },
}


US_UPCOMING = {
    "articles/united-states/index.html": (
        '<span>3 個方向</span></summary><div class="topic-upcoming-grid"><span>美國法院遺產文件能證明甚麼</span><span>中英文姓名對不上內地房產登記怎樣整理</span><span>只剩舊地址和銀行信件時怎樣做資產線索表</span>',
        '<span>2 個方向</span></summary><div class="topic-upcoming-grid"><span>中英文姓名對不上內地房產登記怎樣整理</span><span>只剩舊地址和銀行信件時怎樣做資產線索表</span>',
    ),
    "articles/united-states/index_cn.html": (
        '<span>3 个方向</span></summary><div class="topic-upcoming-grid"><span>美国法院遗产文件能证明什么</span><span>中英文姓名对不上内地房产登记怎样整理</span><span>只剩旧地址和银行信件时怎样做资产线索表</span>',
        '<span>2 个方向</span></summary><div class="topic-upcoming-grid"><span>中英文姓名对不上内地房产登记怎样整理</span><span>只剩旧地址和银行信件时怎样做资产线索表</span>',
    ),
    "articles/united-states/index_en.html": (
        '<span>3 directions</span></summary><div class="topic-upcoming-grid"><span>What a U.S. probate order does and does not establish</span><span>Connecting English names to a Mainland property record</span><span>Tracing assets from an old address or bank letter</span>',
        '<span>2 directions</span></summary><div class="topic-upcoming-grid"><span>Connecting English names to a Mainland property record</span><span>Tracing assets from an old address or bank letter</span>',
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
        text = text.replace(
            "美國 probate 文件沒有寫內地資產，家屬先怎樣核對",
            "美國遺產文件沒有寫內地資產，家屬先怎樣核對",
        ).replace(
            "美国 probate 文件没有写内地资产，家属先怎样核对",
            "美国遗产文件没有写内地资产，家属先怎样核对",
        )
        if relative_path in US_UPCOMING:
            old, new = US_UPCOMING[relative_path]
            if old not in text and new not in text:
                raise RuntimeError(f"US upcoming marker missing: {relative_path}")
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
    for hub in ("singapore", "united-states"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, f"{SITE}/articles/{hub}/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
