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
        "slug": "co-owned-mainland-property",
        "directory": "articles/singapore",
        "topic": "singapore",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 新加坡家屬與共有房產",
                "title": "內地房產多人共有，新加坡家屬怎樣先分出遺產範圍",
                "description": "新加坡家屬處理多人共有的內地房產時，先查登記、共有方式和逝者份額，再填資產清單和安排繼承。",
                "lead": "房產證上有三個名字，不能把整套房直接當成逝者的遺產再分一次。",
                "key_title": "先分清三件事",
                "keys": [
                    "整套房的範圍和價值",
                    "逝者生前真正擁有的份額",
                    "該份額再由哪些人繼承",
                ],
                "answer_title": "先分出逝者的份額，再談繼承",
                "answer": [
                    "多人共有的房產，只有逝者生前實際擁有的部分可能進入遺產。房屋整體、逝者份額和繼承人最後取得的份額，是三個不同問題，不能放在同一個比例裏計算。",
                    "新加坡的資產清單需要準確列出構成遺產的財產，但不會替內地房產判定共有份額。先查房產所在地的登記資料、合同和共有安排；份額仍不清楚時，應標為待核實，而不是先填一個平均數。",
                ],
                "sections": [
                    (
                        "先抄登記資料，不要只問房產證在誰手上",
                        [
                            "逐項記下房屋城市、完整地址、所有登記人、共有方式、是否列明份額、取得日期，以及有沒有抵押、查封或異議。紙面房產證只是資料來源之一，必要時還要看最新登記結果。",
                            "再找購房合同、出資和還款紀錄、共有人之間的書面安排，以及後來有沒有贈與、買賣或份額變更。若證書只寫多人姓名而沒有清楚比例，不要自行除以人數。",
                        ],
                    ),
                    (
                        "把三件事分開寫在一張紙上",
                        [
                            "第一格寫整套房的基本資料和估值用途；第二格只寫逝者可能擁有的份額和證據來源；第三格才寫該份額可能涉及哪些繼承人。每一格旁邊標明已確認、家人說法或待機構核實。",
                            "這樣整理可以避免兩種錯誤：把其他共有人的部分放進遺產，或把逝者的份額直接當成某一名繼承人的份額。即使家屬對最後分配沒有爭議，前兩格仍要先對準登記。",
                        ],
                    ),
                    (
                        "新加坡資產清單只填逝者的遺產",
                        [
                            "申請新加坡遺產文件時，資產清單用來列出構成逝者遺產的財產，並要求提供足夠資料。房產為共有時，應把共有狀態和目前已知份額說清楚，不要把整套房屋價值當成逝者個人財產。",
                            "如果現階段資料不齊，可以先向相關機構補取資料，再按案件要求提交或補充資產清單。逝者去世時的住所不在新加坡時，境外房產是否及怎樣列入申請，還要按實際案件和現行表格確認。法院簽發的代表文件回答誰能處理遺產，不會自動改變內地房屋的登記份額。",
                        ],
                    ),
                    (
                        "共有人不配合時，先查資料再決定路徑",
                        [
                            "證書由其他共有人保管、有人拒絕提供合同，或各人對出資說法不同時，先保存現有影像、付款和聯絡紀錄。繼承人可按房產所在地的查詢要求，準備死亡、親屬、遺囑或其他能說明繼承關係的資料，詢問能查到哪一層登記內容。",
                            "若登記比例、實際出資或房屋處分已有爭議，不要把問題縮成缺一張新加坡文件。先確認爭議的是逝者份額、繼承人分配，還是共有房屋日後出售；三者需要的證據和參與人並不相同。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/singapore/", "新加坡家屬處理內地遺產專題"),
                    ("/articles/singapore/mainland-property-inheritance.html", "新加坡遺產文件能否直接辦內地房產"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets.html", "內地房產怎樣列入新加坡資產清單"),
                    ("/articles/singapore/probate-or-letters-of-administration.html", "先分清兩類新加坡遺產文件"),
                ],
                "cta": "把房產城市、所有登記人、共有方式和現有份額證據列在一頁，我們先找出真正可能進入遺產的部分。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 新加坡家属与共有房产",
                "title": "内地房产多人共有，新加坡家属怎样先分出遗产范围",
                "description": "新加坡家属处理多人共有的内地房产时，先查登记、共有方式和逝者份额，再填资产清单和安排继承。",
                "lead": "房产证上有三个人的名字，不能把整套房直接当成逝者的遗产再分一次。",
                "key_title": "先分清三件事",
                "keys": [
                    "整套房的范围和价值",
                    "逝者生前真正拥有的份额",
                    "该份额再由哪些人继承",
                ],
                "answer_title": "先分出逝者的份额，再谈继承",
                "answer": [
                    "多人共有的房产，只有逝者生前实际拥有的部分可能进入遗产。房屋整体、逝者份额和继承人最后取得的份额，是三个不同问题，不能放在同一个比例里计算。",
                    "新加坡的资产清单需要准确列出构成遗产的财产，但不会替内地房产判断共有份额。先查房产所在地的登记材料、合同和共有安排；份额还不清楚时，应标为待核实，不要先填写一个平均数。",
                ],
                "sections": [
                    (
                        "先抄登记材料，不要只问房产证在谁手上",
                        [
                            "逐项记下房屋城市、完整地址、所有登记人、共有方式、是否列明份额、取得日期，以及有没有抵押、查封或异议。纸面房产证只是材料来源之一，必要时还要查看最新登记结果。",
                            "再找购房合同、出资和还款记录、共有人之间的书面安排，以及后来有没有赠与、买卖或份额变更。如果证书只写多人姓名而没有清楚比例，不要自行除以人数。",
                        ],
                    ),
                    (
                        "把三件事分开写在一张纸上",
                        [
                            "第一格写整套房的基本材料和估值用途；第二格只写逝者可能拥有的份额和证据来源；第三格才写该份额可能涉及哪些继承人。每一格旁边标明已经确认、家人说法或待机构核实。",
                            "这样可以避免两种错误：把其他共有人的部分放进遗产，或把逝者的份额直接当成某一名继承人的份额。即使家属对最后分配没有争议，前两格仍要先对准登记。",
                        ],
                    ),
                    (
                        "新加坡资产清单只填写逝者的遗产",
                        [
                            "申请新加坡遗产文件时，资产清单用来列出构成逝者遗产的财产，并要求提供足够信息。房产属于共有时，应把共有状态和目前已知份额说清楚，不要把整套房屋价值当成逝者个人财产。",
                            "如果现阶段材料不完整，可以先向相关机构补取材料，再按照案件要求提交或补充资产清单。逝者去世时的住所不在新加坡时，境外房产是否以及怎样列入申请，还要按照实际案件和现行表格确认。法院签发的代表文件回答谁能处理遗产，不会自动改变内地房屋的登记份额。",
                        ],
                    ),
                    (
                        "共有人不配合时，先查材料再决定路径",
                        [
                            "证书由其他共有人保管、有人拒绝提供合同，或各人对出资说法不同，先保存现有影像、付款和联系记录。继承人可以按照房产所在地的查询要求，准备死亡、亲属、遗嘱或其他能够说明继承关系的材料，询问可以查到哪一层登记内容。",
                            "如果登记比例、实际出资或房屋处置已经有争议，不要把问题缩成缺一份新加坡文件。先确认争议的是逝者份额、继承人分配，还是共有房屋以后出售；三者需要的证据和参与人并不相同。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/singapore/index_cn.html", "新加坡家属处理内地遗产专题"),
                    ("/articles/singapore/mainland-property-inheritance_cn.html", "新加坡遗产文件能否直接办理内地房产"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_cn.html", "内地房产怎样列入新加坡资产清单"),
                    ("/articles/singapore/probate-or-letters-of-administration_cn.html", "先分清两类新加坡遗产文件"),
                ],
                "cta": "把房产城市、所有登记人、共有方式和现有份额证据列在一页，我们先找出真正可能进入遗产的部分。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / Singapore families and co-owned property",
                "title": "Co-owned Mainland Property: Find the Estate Share First",
                "description": "A practical guide for Singapore families separating a deceased owner's share from the whole Mainland property before probate and inheritance work.",
                "lead": "When three names appear on a Mainland title, the whole home does not become the deceased owner's estate.",
                "key_title": "Keep three things separate",
                "keys": [
                    "The whole property and its value",
                    "The interest the deceased actually owned",
                    "The heirs who may receive that interest",
                ],
                "answer_title": "Identify the deceased's interest before distributing it",
                "answer": [
                    "Only the interest the deceased actually owned may form part of the estate. The whole property, the deceased's ownership share and the share eventually received by an heir are three separate questions.",
                    "A Singapore Schedule of Assets must accurately describe property forming part of the estate, but it does not decide a Mainland co-ownership issue. Check the local title record, contract and ownership arrangements. If the share is still uncertain, mark it for verification instead of dividing by the number of names.",
                ],
                "sections": [
                    (
                        "Read the current title record, not only the paper certificate",
                        [
                            "Record the city, full address, every registered owner, form of co-ownership, any stated share, acquisition date, mortgage and registration restriction. A paper certificate is one source; the latest registration result may be needed as well.",
                            "Then find the purchase contract, funding and mortgage trail, written arrangements between the owners, and any later gift, sale or share change. Several names without a stated ratio do not justify simply dividing the property equally.",
                        ],
                    ),
                    (
                        "Put the three questions in separate boxes",
                        [
                            "Box one describes the entire property and why a value is needed. Box two records only the deceased's possible interest and the evidence for it. Box three lists the people who may inherit that interest. Label every fact as confirmed, family account or awaiting institutional verification.",
                            "This prevents two common errors: putting another co-owner's property into the estate, and treating the deceased's share as if it already belonged to one beneficiary. Agreement about distribution does not remove the need to identify the property interest first.",
                        ],
                    ),
                    (
                        "The Singapore asset schedule should state the estate interest",
                        [
                            "The Schedule of Assets is used to declare property comprising the deceased's estate and requires sufficient details. For a co-owned home, describe the co-ownership and the share currently supported by the records rather than treating the full property value as the deceased's personal asset.",
                            "If information is missing, the relevant institutions can be approached and the schedule may be filed or supplemented as the case permits. Where the deceased was not domiciled in Singapore at death, whether and how the overseas property enters the application must be checked against the actual case and current form. A Singapore grant identifies the personal representative; it does not change the ownership share recorded in Mainland China.",
                        ],
                    ),
                    (
                        "If another owner will not cooperate, verify before choosing a route",
                        [
                            "If another owner holds the certificate, withholds the contract or disputes the funding, preserve the images, payments and messages already available. Ask the property city what a person claiming through the estate must provide to obtain the permitted registration information.",
                            "Do not describe every disagreement as a missing Singapore document. Identify whether the dispute concerns the deceased's existing share, distribution among heirs or a future sale of the co-owned property. Each issue involves different evidence and participants.",
                        ],
                    ),
                ],
                "related_title": "Continue with the Singapore topic",
                "related": [
                    ("/articles/singapore/index_en.html", "Singapore families handling a Mainland estate"),
                    ("/articles/singapore/mainland-property-inheritance_en.html", "Can a Singapore grant transfer Mainland property?"),
                    ("/articles/singapore/mainland-property-in-schedule-of-assets_en.html", "Recording Mainland property in the Schedule of Assets"),
                    ("/articles/singapore/probate-or-letters-of-administration_en.html", "Grant of Probate or Letters of Administration"),
                ],
                "cta": "List the property city, every registered owner, the co-ownership form and the current share evidence. We can then identify the interest that may enter the estate.",
            },
        },
    },
    {
        "slug": "missing-mainland-title",
        "directory": "articles/us",
        "topic": "united-states",
        "copy": {
            "tc": {
                "lang": "zh-Hant",
                "locale": "zh_HK",
                "brand": "劉毅律師團隊",
                "brand_sub": "跨境中國法律事務",
                "eyebrow": "文章 / 美國家屬與內地房產線索",
                "title": "美國家屬找不到內地房產證，可以先從哪些資料補線索",
                "description": "美國家屬找不到內地房產證時，先整理城市、地址、登記姓名和交易線索，再按所在地要求查登記或處理遺失。",
                "lead": "抽屜裏沒有房產證，不代表房子不存在，也不代表第一步一定是補辦新證。",
                "key_title": "先找三類線索",
                "keys": [
                    "城市、地址和小區名稱",
                    "登記姓名和舊證件號碼",
                    "合同、付款和物業紀錄",
                ],
                "answer_title": "先查登記，再問是否需要補證",
                "answer": [
                    "房產證是重要文件，但家屬先要找出房屋在哪個城市、可能登記在誰名下，以及有哪些合同或付款線索。內地登記資料才用來核對現時權利人、共有、抵押和限制狀態。",
                    "不要一律先申請補證。部分地區在產權人已去世、繼承人取得當地要求的繼承權憑證資料後，可能接受遺失聲明並直接辦理轉移；其他地方的資料和程序可能不同。先問房產所在地，才不會辦錯一步。",
                ],
                "sections": [
                    (
                        "從家裏找可以指向一套房的舊紀錄",
                        [
                            "依次查看購房合同、按揭或匯款紀錄、契稅和維修基金票據、物業費、水電通知、租約、裝修單、開發商信件、舊照片和家族訊息。記下文件原本在甚麼位置、由誰找到和日期。",
                            "只保留看得見的線索，不要嘗試使用逝者密碼、驗證碼或人臉登入賬戶。截圖要保留完整畫面和來源，不要只剪下一個地址或金額。",
                        ],
                    ),
                    (
                        "做一張地址和身份對照表",
                        [
                            "一行寫一個可能地址：城市、區、街道、小區、樓棟房號、開發商或物業名稱，以及線索出現在哪份資料。另一欄列逝者的中文姓名、拼音、曾用名、內地舊證件和美國證件。",
                            "地址只有舊小區名、房號曾變，或姓名在美國文件和內地資料中不同時，先把版本全部保留，並在每條線索旁標明是原件、影像還是家人記憶。不要為了方便查詢而自行把它們改成同一個寫法。",
                        ],
                    ),
                    (
                        "繼承人可以先問登記資料怎樣查",
                        [
                            "現行查詢規則容許符合條件的繼承人按要求查詢相關不動產登記資料，但通常要提交身份、死亡、親屬、遺囑或其他能說明繼承事項的資料。具體能否網上查、能查哪些內容和是否可委託，由房產所在地確認。",
                            "向窗口說清楚目前只有哪些線索，並問需要哪一個查詢索引：姓名和舊證件、具體坐落、舊證書號或不動產單元號。先取得可核對的登記結果，再決定後面的繼承文件。",
                        ],
                    ),
                    (
                        "補證、遺失聲明和直接轉移不要混成一步",
                        [
                            "一般的補證程序可能以現有權利人提出申請為起點；產權人已去世後，家屬不應照搬本人補證流程。有些地方允許已取得當地要求之繼承權憑證資料的繼承人共同作遺失不補證聲明，直接申請轉移並處理舊證作廢。",
                            "這不是所有城市的統一捷徑。把登記結果、證書遺失經過、全部可能繼承人和現有美國文件交給實際接收方，確認是先查檔、先完成繼承關係，還是需要另一步公告或聲明。",
                        ],
                    ),
                    (
                        "美國遺產清單先寫線索，不要假裝已確認",
                        [
                            "美國各州的遺產程序不同，但資產清單通常要描述逝者的房地產和實際擁有部分。只知道“在內地有一套房”時，先把城市、地址線索、可能登記姓名和資料缺口交給案件所在州的處理人核對。",
                            "之後查到完整地址、共有份額或抵押資料，可能需要按當地程序補充或更正清單。美國清單可以記錄和管理線索，但不能代替內地登記結果。",
                        ],
                    ),
                ],
                "related_title": "同一專題繼續閱讀",
                "related": [
                    ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                    ("/articles/us/sole-registered-mainland-property.html", "只登記逝者姓名時先查哪六件事"),
                    ("/articles/us/mainland-asset-omitted-from-probate.html", "內地資產沒有寫進美國遺產文件怎樣處理"),
                    ("/articles/us/spousal-share-before-inheritance.html", "房產只寫一人姓名時先查配偶份額"),
                ],
                "cta": "把可能城市、地址、登記姓名、舊證件和付款線索列在一頁，我們先判斷向哪個地方查甚麼。",
            },
            "cn": {
                "lang": "zh-Hans",
                "locale": "zh_CN",
                "brand": "刘毅律师团队",
                "brand_sub": "跨境中国法律事务",
                "eyebrow": "文章 / 美国家属与内地房产线索",
                "title": "美国家属找不到内地房产证，可以先从哪些材料补线索",
                "description": "美国家属找不到内地房产证时，先整理城市、地址、登记姓名和交易线索，再按所在地要求查询登记或处理遗失。",
                "lead": "抽屉里没有房产证，不等于房子不存在，也不等于第一步一定是补办新证。",
                "key_title": "先找三类线索",
                "keys": [
                    "城市、地址和小区名称",
                    "登记姓名和旧证件号码",
                    "合同、付款和物业记录",
                ],
                "answer_title": "先查登记，再问是否需要补证",
                "answer": [
                    "房产证是重要文件，但家属先要找出房屋在哪个城市、可能登记在谁名下，以及有哪些合同或付款线索。内地登记材料才用于核对当前权利人、共有、抵押和限制状态。",
                    "不要一律先申请补证。部分地区在产权人已经去世、继承人取得当地要求的继承权凭证材料后，可能接受遗失声明并直接办理转移；其他地方的材料和程序可能不同。先问房产所在地，才不会办错一步。",
                ],
                "sections": [
                    (
                        "从家里找可以指向一套房的旧记录",
                        [
                            "依次查看购房合同、按揭或汇款记录、契税和维修基金票据、物业费、水电通知、租约、装修单、开发商信件、旧照片和家庭消息。记下文件原来在哪个位置、由谁找到和日期。",
                            "只保留可以看见的线索，不要尝试使用逝者密码、验证码或人脸登录账户。截图保留完整画面和来源，不要只剪下一个地址或金额。",
                        ],
                    ),
                    (
                        "做一张地址和身份对照表",
                        [
                            "一行写一个可能地址：城市、区、街道、小区、楼栋房号、开发商或物业名称，以及线索出现在哪份材料。另一栏列逝者的中文姓名、拼音、曾用名、内地旧证件和美国证件。",
                            "地址只有旧小区名、房号发生过变化，或姓名在美国文件和内地材料中不同时，先把所有版本保留，并在每条线索旁标明是原件、影像还是家人记忆。不要为了方便查询自行改成同一个写法。",
                        ],
                    ),
                    (
                        "继承人可以先问登记材料怎样查",
                        [
                            "现行查询规则允许符合条件的继承人按照要求查询相关不动产登记材料，但通常要提交身份、死亡、亲属、遗嘱或其他可以说明继承事项的材料。能否网上查询、可以查看哪些内容以及是否能委托，由房产所在地确认。",
                            "向窗口说明目前只有哪些线索，并询问需要哪一个查询索引：姓名和旧证件、具体坐落、旧证书号或不动产单元号。先取得可以核对的登记结果，再决定后面的继承材料。",
                        ],
                    ),
                    (
                        "补证、遗失声明和直接转移不要混成一步",
                        [
                            "一般补证程序可能以现有权利人提出申请为起点；产权人去世后，家属不能照搬本人补证流程。有些地方允许已经取得当地要求之继承权凭证材料的继承人共同填写遗失不补证声明，直接申请转移并处理旧证作废。",
                            "这不是所有城市的统一捷径。把登记结果、证书遗失经过、全部可能继承人和现有美国文件交给实际接收方，确认是先查档、先完成继承关系，还是需要另一步公告或声明。",
                        ],
                    ),
                    (
                        "美国遗产清单先写线索，不要假装已经确认",
                        [
                            "美国各州的遗产程序不同，但资产清单通常要描述逝者的房地产和实际拥有部分。只知道“在内地有一套房”时，先把城市、地址线索、可能登记姓名和材料缺口交给案件所在州的处理人核对。",
                            "以后查到完整地址、共有份额或抵押材料，可能要按照当地程序补充或更正清单。美国清单可以记录和管理线索，但不能代替内地登记结果。",
                        ],
                    ),
                ],
                "related_title": "同一专题继续阅读",
                "related": [
                    ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                    ("/articles/us/sole-registered-mainland-property_cn.html", "只登记逝者姓名时先查哪六件事"),
                    ("/articles/us/mainland-asset-omitted-from-probate_cn.html", "内地资产没有写进美国遗产文件怎样处理"),
                    ("/articles/us/spousal-share-before-inheritance_cn.html", "房产只写一人姓名时先查配偶份额"),
                ],
                "cta": "把可能城市、地址、登记姓名、旧证件和付款线索列在一页，我们先判断应该向哪个地方查询什么。",
            },
            "en": {
                "lang": "en",
                "locale": "en_US",
                "brand": "Liu Yi Lawyer Team",
                "brand_sub": "Cross-border Mainland China legal matters",
                "eyebrow": "Article / U.S. families tracing Mainland property",
                "title": "Missing Mainland Property Certificate: Rebuild the Clues First",
                "description": "How a U.S. family can trace a Mainland property from addresses, names and transaction records before asking about title records or a lost certificate.",
                "lead": "An empty drawer does not prove that the Mainland home is gone, and replacing the paper certificate is not always the first step.",
                "key_title": "Start with three clue groups",
                "keys": [
                    "City, address and development name",
                    "Registered name and old identity number",
                    "Contract, payment and management records",
                ],
                "answer_title": "Check the register before asking for a replacement certificate",
                "answer": [
                    "A property certificate is useful, but the family first needs the likely city, registered name and transaction trail. The Mainland registration record is used to check the current owner, co-ownership, mortgage and other restrictions.",
                    "Do not assume that every case begins with a replacement certificate. In some cities, once the heirs hold the inheritance evidence required locally, they may use a loss declaration and apply for the transfer without replacing the old certificate. The receiving city must confirm its route.",
                ],
                "sections": [
                    (
                        "Search the household records for a traceable property",
                        [
                            "Review purchase contracts, mortgage or remittance records, tax and maintenance receipts, management fees, utility notices, leases, renovation invoices, developer letters, old photographs and family messages. Record where each item was found, by whom and on what date.",
                            "Preserve only information the family can legitimately see. Do not use the deceased's password, verification code or face login. Keep the full screenshot and source rather than cropping out one address or amount.",
                        ],
                    ),
                    (
                        "Build one address and identity comparison sheet",
                        [
                            "Give each possible address a row: city, district, street, development, building, unit, developer or property manager, and the record where the clue appears. In a second block list every Chinese name, romanised name, former name, old Mainland identity record and U.S. identity document.",
                            "Preserve every version where the development has been renamed, the unit format changed or the U.S. and Mainland names differ. Mark each clue as an original, an image or a family recollection; do not silently rewrite the records into one convenient spelling.",
                        ],
                    ),
                    (
                        "Ask how a person claiming through the estate may search",
                        [
                            "Current registration-query rules allow a qualifying heir to seek relevant property information, subject to identity, death, family, will or other inheritance evidence. Online access, the information available and the use of an agent depend on the property city.",
                            "Tell the registry what clues exist and ask which search key is needed: the name and former identity number, exact location, old certificate number or property unit number. Obtain a verifiable result before deciding which inheritance papers to prepare.",
                        ],
                    ),
                    (
                        "Keep replacement, loss declaration and transfer separate",
                        [
                            "An ordinary replacement process may begin with the current owner applying. After the owner has died, the family should not simply copy that route. Some local offices permit heirs who hold the locally required inheritance evidence to make a joint declaration that the lost certificate will not be replaced and proceed with the inheritance transfer.",
                            "That is not a universal shortcut. Give the receiving office the search result, circumstances of the loss, possible heirs and available U.S. papers. Ask whether the next step is an archive search, confirmation of the inheritance or a separate notice or declaration.",
                        ],
                    ),
                    (
                        "Record the clue honestly in the U.S. probate file",
                        [
                            "U.S. probate procedure varies by state, but an inventory commonly describes real property and the interest the deceased owned. If the family knows only that a Mainland home existed, give the case professional the city, address clues, possible registered name and missing information.",
                            "A fuller address, co-ownership share or mortgage may later require a supplemental or corrected inventory under the relevant state procedure. The U.S. inventory can manage the clue, but it cannot replace the Mainland title record.",
                        ],
                    ),
                ],
                "related_title": "Continue with the U.S. topic",
                "related": [
                    ("/articles/united-states/index_en.html", "U.S. families handling a Mainland estate"),
                    ("/articles/us/sole-registered-mainland-property_en.html", "Six checks for a home registered only to the deceased"),
                    ("/articles/us/mainland-asset-omitted-from-probate_en.html", "A Mainland asset is missing from the U.S. probate papers"),
                    ("/articles/us/spousal-share-before-inheritance_en.html", "Checking the spouse's interest before inheritance"),
                ],
                "cta": "Put the likely city, address, registered name, former identity record and payment clues on one page. We can then identify where and how to search.",
            },
        },
    },
]


HUB_UPDATES = {
    "articles/singapore/index.html": (
        "/articles/singapore/co-owned-mainland-property.html",
        '<a href="/articles/singapore/co-owned-mainland-property.html"><span class="v24-tag">共有房產</span><strong>內地房產多人共有，先怎樣分出遺產範圍</strong><p>分開整套房、逝者份額和繼承人最後所得。</p></a>',
    ),
    "articles/singapore/index_cn.html": (
        "/articles/singapore/co-owned-mainland-property_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">共有房产</span><h3>内地房产多人共有，先怎样分出遗产范围</h3><p>分开整套房、逝者份额和继承人最后所得。</p></div><a class="v25-pill-action" href="/articles/singapore/co-owned-mainland-property_cn.html">阅读文章</a></article>',
    ),
    "articles/singapore/index_en.html": (
        "/articles/singapore/co-owned-mainland-property_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Co-owned property</span><h3>Identify the estate share in a co-owned Mainland home</h3><p>Separate the whole property, the deceased\'s interest and the heirs\' eventual shares.</p></div><a class="v25-pill-action" href="/articles/singapore/co-owned-mainland-property_en.html">Read Article</a></article>',
    ),
    "articles/united-states/index.html": (
        "/articles/us/missing-mainland-title.html",
        '<a href="/articles/us/missing-mainland-title.html"><span class="v24-tag">房產線索</span><strong>找不到內地房產證，先從哪些資料補線索</strong><p>先查城市、地址、登記姓名和交易紀錄，再問遺失程序。</p></a>',
    ),
    "articles/united-states/index_cn.html": (
        "/articles/us/missing-mainland-title_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">房产线索</span><h3>找不到内地房产证，先从哪些材料补线索</h3><p>先查城市、地址、登记姓名和交易记录，再问遗失程序。</p></div><a class="v25-pill-action" href="/articles/us/missing-mainland-title_cn.html">阅读文章</a></article>',
    ),
    "articles/united-states/index_en.html": (
        "/articles/us/missing-mainland-title_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">Property clues</span><h3>Missing Mainland property certificate: rebuild the clues first</h3><p>Trace the city, address, registered name and transaction record before asking about loss.</p></div><a class="v25-pill-action" href="/articles/us/missing-mainland-title_en.html">Read Article</a></article>',
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
    for base in ("/articles/singapore/", "/articles/united-states/"):
        for suffix in ("", "index_cn.html", "index_en.html"):
            text = update_lastmod(text, SITE + base + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_articles()
    update_hubs()
    update_sitemap()
