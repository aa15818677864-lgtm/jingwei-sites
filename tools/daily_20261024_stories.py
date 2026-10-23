"""Build the Oct 24 researched story batch in the existing publication format."""
from __future__ import annotations
import json
from pathlib import Path
from urllib.parse import quote
from opencc import OpenCC

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'content-drafts' / 'daily-20261024'
S2HK = OpenCC('s2hk')
S2T = OpenCC('s2t')
T2S = OpenCC('t2s')

# Each story is a fresh practical outline based on the cited issue sources and
# Mainland authorities. Search volumes remain unmeasured.
DATA = [
{
 'id':'D24-P01','slug':'mainland-housing-reform-property-inheritance-check','folder':'hk-mainland-property-inheritance','category':'property-inheritance','query':'内地房改房继承登记',
 'comp':('https://www.zwjkey.com/jingdiananli/minshianli/2026-08-20/13493.html','房改房继承引纠纷：家庭内部产权协议与登记外观'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/233181.html','中华人民共和国民法典'),
 'title':'内地房改房继承登记：先核产权比例、补款记录和夫妻共有','titleEn':'Inheriting a Mainland housing-reform home: check title, payments and marital ownership first',
 'lead':'父母留下的房改房，旧房本、购房协议和单位档案可能各写一套信息。香港家属办理前，先查清被继承人实际取得的是全部产权还是有限产权、是否尚有价款或土地收益事项，再判断哪些权利进入遗产。',
 'leadEn':'A housing-reform home may have an old certificate, a purchase agreement and employer records that do not say the same thing. Before a Hong Kong family applies, establish what title the deceased actually acquired, whether any payment or land-related condition remains, and which rights form part of the estate.',
 'sections':[
  ('先分清“房改房”不等于同一种产权','房改房可能按成本价、标准价或其他政策安排购买。登记证书、房改售房合同、缴款凭证和产权备注要放在一起看；仅凭“当年单位分房”或子女出过钱，不能直接推定房屋全部属于某一人。','Identify the actual title','Housing-reform homes arose under different purchase arrangements. Read the register, sale agreement, payment records and any title restriction together. An old workplace allocation or a child’s contribution does not by itself establish sole ownership.'),
  ('先析出配偶份额，再计算遗产','房屋如在婚姻关系存续期间取得，要先核对购房时间、资金来源和夫妻财产约定。属于夫妻共同财产的，应先区分配偶自己的份额；只有被继承人依法享有的部分才进入继承范围。','Separate a spouse’s share before calculating the estate','If the home was acquired during marriage, check the acquisition date, source of funds and any marital property agreement. A spouse’s own share must be separated before the deceased’s interest is treated as estate property.'),
  ('向售房单位和登记机构分别核实','把房改合同、房款收据、补差或补缴记录、旧证及最新登记信息列成一张时间表，向原售房单位确认档案是否仍保存，再向房屋所在地登记机构核对办理所需材料。不同城市、不同房改政策的补件要求可能不同。','Verify with the former employer and registry','Create a timeline from the reform-sale contract, receipts, adjustment payments, old certificate and current register. Ask the former employer whether its file survives, then confirm the local registry’s list. Requirements can vary by city and reform scheme.')],
 'checkTitle':'香港家属先整理','check':['房改售房合同及购房时采用的价格类型。','缴款、补差、维修基金或土地收益记录。','旧房本、最新登记信息和共有情况。','婚姻证明及夫妻财产约定。','原单位档案联系人和房屋所在地登记机构答复。'],
 'checkEn':['The reform-sale contract and purchase-price category.','Payment, adjustment, maintenance-fund or land-income records.','Old certificate, current register and co-ownership entries.','Marriage records and any marital property agreement.','The employer archive contact and local registry’s response.']
},
{
 'id':'D24-P02','slug':'mainland-nominee-property-estate-evidence','folder':'hk-mainland-property-inheritance','category':'property-inheritance','query':'内地房产代持继承争议',
 'comp':('https://www.icourt.cc/prac-document/159233.html','代持人死亡后，继承人能否就代持的财产进行继承？'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/233181.html','中华人民共和国民法典'),
 'title':'内地房产代持人先去世，出资家属怎样整理继承争议证据','titleEn':'The registered nominee dies first: evidence for a Mainland property inheritance dispute',
 'lead':'房屋登记在亲属名下，实际出资人却是另一位家人；登记人先离世后，继承人面对的往往不只是分遗产，还包括代持关系是否存在、房屋权利归谁。先保存完整证据，别急着把“出资”写成“产权”。',
 'leadEn':'A home may be registered to one relative while another family member supplied the money. If the registered owner dies first, heirs may have to resolve both the estate and whether a nominee arrangement existed. Preserve the evidence; payment alone does not automatically prove title.',
 'sections':[
  ('登记、出资和实际使用要分开证明','收集登记簿、购房合同、付款流水、贷款还款、税费凭证、装修支出及长期占有使用记录。每份材料说明的是不同事实：谁登记、谁付款、谁管理，不能互相替代。','Prove registration, payment and use separately','Collect the register, purchase contract, payment and mortgage records, tax receipts, renovation expenses and evidence of long-term use. Each proves a different fact: registration, funding or management are not interchangeable.'),
  ('代持约定最好找同期材料印证','书面代持协议、聊天记录、催款或分红记录、房屋交付和物业沟通，均要保留原始载体与完整上下文。单方回忆或事后补写的说明，证明力可能有限；更不能改动转账备注或补造签名。','Look for contemporaneous evidence of the arrangement','Keep the original nominee agreement, messages, repayment or income records, handover material and property-management correspondence with their full context. A later statement or one person’s recollection may be insufficient. Never alter a transfer note or create a signature.'),
  ('先判断是否需要诉讼和财产保全','如其他继承人主张登记人个人所有，或房屋将被出售、抵押、查封，应及时评估确认权属、继承分割或执行异议等不同请求及证据保全需要。香港家属应先取得不动产所在地登记和诉讼材料，再确定内地程序。','Assess litigation and preservation early','If heirs say the registered owner alone owned the home, or a sale, mortgage or enforcement is imminent, assess the proper claim and whether evidence or property preservation is needed. Obtain registry and case materials from the property’s Mainland location before selecting a procedure.')],
 'checkTitle':'证据整理清单','check':['产权登记、购房合同及历次变更资料。','原始付款流水、贷款及税费记录。','代持协议、聊天记录和完整电子数据。','交房、居住、出租、物业沟通与维修材料。','其他继承人的主张、诉讼或处分风险。'],
 'checkEn':['Title register, purchase contract and change history.','Original payment, mortgage and tax records.','The nominee agreement and complete electronic messages.','Handover, occupation, rental, management and repair records.','Other heirs’ claims and any litigation or disposal risk.']
},
{
 'id':'D24-P03','slug':'mainland-multi-city-property-inheritance-registration','folder':'hk-mainland-property-inheritance','category':'property-inheritance','query':'内地多套房产登记路径',
 'comp':('https://www.hankunlaw.com/upload/portal/20250612/f44ce3dcb89fa63aeb1a95cd6efa1d68.pdf','境外继承人继承中国内地遗产的程序与财产调查'),
 'official':('https://www.shantou.gov.cn/stszrzyj/zwgk/gzdt/content/post_2529754.html','汕头市不动产登记交易中心继承登记业务便民解答'),
 'title':'内地多套房产分布不同城市，香港继承人怎样排登记次序','titleEn':'Mainland properties in several cities: a practical registration sequence for Hong Kong heirs',
 'lead':'遗产房分别在深圳、广州或其他城市，家属常想一次交齐材料、一次过户。实际办理通常要按每处不动产所在地的登记要求逐项核实；一套亲属关系文件可以作为共同底稿，但不代表各地受理材料完全相同。',
 'leadEn':'When estate homes sit in Shenzhen, Guangzhou and other cities, families often hope to file everything at once. Each property’s local registry requirements should be checked separately. A shared family-evidence file helps, but does not make every city’s filing list identical.',
 'sections':[
  ('先做一张“房屋—城市—权利人”表','逐套记录坐落、登记权利人、共有份额、抵押或查封、房屋用途及目前是否出租。把旧证、合同和登记查询放在同一目录，避免把同名小区或旧门牌误当成同一物业。','Make a property-by-city inventory','For each home, record its location, registered owner, co-ownership, mortgage or seizure, use and tenancy. Keep old certificates, contracts and registry searches together so that similar addresses are not confused.'),
  ('每处房产分别确认受理机构和方式','向各地不动产登记中心确认能否继承登记、是否需要公证或生效法律文书、所有继承人是否到场，以及香港形成的声明或授权如何使用。部分地区提供线上申请或本市通办，不能直接推定跨市也可通办。','Confirm the receiving office and route for each property','Ask each local registry about inheritance registration, whether notarisation or a final court document is required, who must attend, and how Hong Kong declarations or powers of attorney are accepted. A city-level online or one-stop service does not necessarily cover another city.'),
  ('共享证明材料，分别留受理回执','死亡、亲属关系、婚姻和遗嘱材料可建立一套清晰底档，再按当地要求准备原件、复印件或核验件。分别保存申请表、补件通知和回执，登记完成后核对权利人、份额及限制信息。','Reuse core evidence, but keep separate filing records','Build one clear file of death, family, marriage and will evidence, then prepare originals or certified copies as each registry requires. Keep each application, deficiency notice and receipt. After registration, verify the names, shares and restrictions on every new certificate.')],
 'checkTitle':'多地办理工作表','check':['每套物业的城市、地址和不动产单元号。','当地登记中心联系方式及书面材料清单。','各继承人的身份、关系及授权文件状态。','每地申请、补件和回执编号。','登记后证书、份额和抵押状态的复核记录。'],
 'checkEn':['City, address and unit identifier for each property.','Each registry’s contact and written document list.','Identity, relationship and authority documents for every heir.','Application, deficiency and receipt references for each city.','Post-registration checks of title shares and encumbrances.']
},
{
 'id':'D24-P04','slug':'mainland-public-housing-tenancy-after-death','folder':'hk-mainland-property-inheritance','category':'property-inheritance','query':'内地公房承租权变更继承',
 'comp':('https://www.middlapartners.com/family/yanjiu/public-housing-tenant-death-shanghai.html','老公房承租人去世：承租权变更与共同居住人认定'),
 'official':('https://www.moj.gov.cn/pub/sfbgw/fzgz/fzgzggflfwx/fzgzggflfw/202402/t20240208_494638.html','司法部：自管公房变更承租人问题释疑'),
 'title':'内地公房承租人去世，家属先核同住资格与单位规则','titleEn':'A Mainland public-housing tenant dies: check occupancy eligibility and local rules',
 'lead':'公房租约上的承租人离世，不等于房屋产权自动由继承人取得。香港家属要先分清这是公有住房租赁关系、已购房改房，还是其他住房安排，再查看租约、同住记录和当地变更承租人规则。',
 'leadEn':'The death of a named public-housing tenant does not automatically transfer ownership to heirs. First determine whether the home remains publicly owned, was purchased under a reform scheme, or is subject to another arrangement. Then review the lease, occupancy evidence and local succession rules for tenancy.',
 'sections':[
  ('先看手上的文件写的是所有权还是租赁权','房屋所有权证、不动产登记簿与公房租赁凭证反映的权利不同。若只有承租凭证，家属不能只凭亲属身份把房屋列作可分割的产权遗产。','Identify whether the document records ownership or tenancy','A title certificate and registry entry differ from a public-housing lease certificate. If the deceased held only a tenancy, kinship alone does not make the building divisible estate property.'),
  ('新承租人资格因城市和房屋类型而异','各地可能考虑共同居住、户籍、家庭住房条件、租约约定和管理单位规则；直管公房、自管公房及保障性住房也可能采用不同程序。不要照搬上海、北京或某一单位的顺序到其他城市。','Eligibility depends on location and housing type','Local rules may consider co-residence, household registration, housing conditions, lease terms and the owner’s policy. Direct-managed, employer-managed and subsidised housing can follow different routes. Do not apply one city’s order to another.'),
  ('尽早书面联系产权单位或房管机构','整理原租约、租金凭证、共同居住人资料、死亡证明和家属意见，向管理单位确认申请期限、资格审查和争议处理办法。家属之间有分歧时，先保留租金及房屋使用记录，避免一方擅自更换锁具或转租。','Contact the housing owner or authority in writing','Prepare the lease, rent records, co-resident evidence, death certificate and family positions. Ask the owner or housing authority about deadlines, eligibility review and dispute handling. If relatives disagree, preserve rent and use records and avoid unilateral lock changes or subletting.')],
 'checkTitle':'联系房管单位前','check':['公房租赁合同、租赁凭证及产权人资料。','承租人生前共同居住和户籍材料。','租金支付记录及管理单位往来。','当地承租人变更办法和申请期限。','家属协商记录及尚未解决的争议。'],
 'checkEn':['Public-housing lease, tenancy certificate and owner details.','Evidence of co-residence and household registration.','Rent payments and correspondence with the housing manager.','Local tenant-change rules and application deadline.','Family discussions and unresolved disagreements.']
},
{
 'id':'D24-P05','slug':'mainland-residence-right-and-property-inheritance','folder':'hk-mainland-property-inheritance','category':'property-inheritance','query':'内地居住权继承影响',
 'comp':('https://www.customslawyer.cn/upload/default/20220209/a55bee8759e47b9b12dba520c164cce1.pdf','民法典新增居住权制度的实务讨论'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/233181.html','中华人民共和国民法典第三百六十六至三百七十一条'),
 'title':'内地房屋设有居住权，产权继承后还要核对什么','titleEn':'A Mainland home has a registered right of residence: what heirs should check',
 'lead':'房屋产权人去世后，继承人可能取得所有权，但房屋上已登记的居住权仍会影响实际使用。相反，居住权人去世时，该人身性权利通常依法消灭。先查登记簿和合同，再区分产权继承与居住权处理。',
 'leadEn':'Heirs may acquire ownership of a home while a registered right of residence continues to affect its use. When the residence-right holder dies, that personal right generally ends under Mainland law. Check the register and contract, then address ownership and residence separately.',
 'sections':[
  ('把产权人和居住权人分别列清','核对不动产登记簿是否记载居住权、权利人、期限及相关合同。房屋所有权人死亡，与居住权人死亡是两件事；不能仅因产权变更，就认定居住安排自动失效。','List the owner and residence-right holder separately','Check whether the register records a residence right, its holder, term and supporting contract. The owner’s death and the residence-right holder’s death are different events. A change of owner alone does not establish that the right has ended.'),
  ('留意居住权期限及注销材料','《民法典》规定居住权不得转让、继承，期限届满或居住权人死亡时消灭；注销登记仍应按登记机构程序办理。家属需要出售或办理后续登记时，先向房屋所在地机构确认死亡证明、登记申请及是否要权利人配合。','Check the term and cancellation documents','The Civil Code says a residence right cannot be transferred or inherited and ends when its term expires or its holder dies. Cancellation still follows registry procedure. Before a sale or later registration, confirm what death evidence and application the local office requires.'),
  ('遗嘱安排要避免把所有权和居住安排混写','遗嘱可以处分立遗嘱人自己的房屋权益，但新增居住权或保留他人居住安排，涉及权利人、期限、登记及其他共有人的权利。把“房子给谁”与“谁继续居住、住多久”分开表达并核实可登记性。','Keep ownership and occupation clauses distinct','A will can dispose of the testator’s own property interest, but creating or preserving residence arrangements raises separate questions about the holder, term, registration and co-owners. State who receives ownership separately from who may live there and for how long.')],
 'checkTitle':'需要核对的权利信息','check':['最新不动产登记簿及居住权登记内容。','居住权合同或设立居住权的遗嘱条款。','居住权人、所有权人及共有人的身份情况。','居住期限、死亡或届满证明材料。','登记机构对注销或后续过户的答复。'],
 'checkEn':['Current real estate register and residence-right entry.','The residence-right agreement or will clause creating it.','Identity of the holder, owner and any co-owners.','The term and evidence of death or expiry.','The registry’s instructions for cancellation or later transfer.']
},
{
 'id':'D24-P06','slug':'mainland-small-property-rights-inheritance-evidence','folder':'hk-mainland-property-inheritance','category':'property-inheritance','query':'内地小产权房继承风险',
 'comp':('https://www.daohualaw.com/2026/hyjsl_0414/696.html','小产权房继承诉讼中的权属与证据问题'),
 'official':('https://www.shantou.gov.cn/stszrzyj/zwgk/gzdt/content/post_2529754.html','汕头市不动产登记交易中心继承登记业务便民解答'),
 'title':'内地小产权房继承风险：先查可继承的权益是什么','titleEn':'Inheritance risks for a Mainland small-property home: identify the actual right first',
 'lead':'“小产权房”不是统一的法定产权类别。香港家属看到村证、合作建房合同或长期居住事实时，应先查土地和建设背景，判断死者拥有的是登记所有权、合同请求权，还是占有使用等利益；不要把材料直接等同商品房产权。',
 'leadEn':'“Small-property home” is not a single legal title category. If a Hong Kong family finds a village certificate, co-building agreement or long occupation, investigate the land and construction history. The deceased may have held registered title, contractual claims or use interests, which are not interchangeable with ordinary commercial-home title.',
 'sections':[
  ('先把土地、建设和交易背景查明','收集集体土地或宅基地资料、建房审批、村集体文件、购买合同、付款记录、入住及后续处分情况。确认房屋是否登记、登记在谁名下，以及购买人是否具备相关集体成员资格。','Investigate land, construction and transaction history','Collect collective-land or homestead records, construction approvals, village documents, contracts, payment records, occupation and later transactions. Confirm whether the home is registered, to whom, and whether the buyer met any collective-membership condition.'),
  ('把“能否作为遗产”与“能否过户”分开','个案中可能存在可继承的合同或使用利益，但这不等于可以办理商品房式的不动产权转移登记。不同土地性质、建房手续和地区政策会影响法院能处理的请求及登记部门能办理的事项。','Separate inheritable interests from registrable ownership','A case may involve inheritable contractual or use interests without allowing a commercial-style title transfer. Land status, construction approvals and local policy affect both the claim a court can decide and what a registry can record.'),
  ('用原始证据说明权益如何形成','保存原合同、付款凭证、村集体收款或盖章文件、建房材料、租住管理记录以及与出卖方的通信。若继承人之间争议的是实际权益或补偿款，不要只提出“过户房屋”一个请求，应先让内地律师按证据和当地规则区分诉求。','Show how the interest arose with original evidence','Preserve the original contract, payment trail, village receipts or seals, construction material, occupancy records and communications with the seller. If heirs dispute an actual interest or compensation, do not assume a request to transfer title will address every issue; assess claims under local rules.')],
 'checkTitle':'先收集這些材料','check':['土地性质、村集体及建房审批资料。','买卖或合作建房合同与原始付款凭证。','房屋交付、居住、出租和维修记录。','房屋目前登记、查封或征收状态。','继承人各自的权利主张及能支持的证据。'],
 'checkEn':['Land status, collective records and construction approvals.','Purchase or co-building agreement and original payment proof.','Handover, occupation, rental and repair records.','Current registration, enforcement or expropriation status.','Each heir’s claim and the evidence supporting it.']
},
{
 'id':'D24-P07','slug':'mainland-parking-space-estate-registration','folder':'hk-mainland-property-inheritance','category':'property-inheritance','query':'内地房屋附车位继承登记',
 'comp':('https://www.tmlslaw.com/wenhua/qikan/943.html','小区车位的权属与使用安排'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/233181.html','中华人民共和国民法典第二百七十五条'),
 'title':'内地房屋附带车位继承，先分清产权车位和使用权','titleEn':'A parking space linked to a Mainland home: distinguish ownership from use rights',
 'lead':'房屋和车位一起写在家人口中，不代表两者一定是同一项产权。香港家属应核对车位有没有独立登记、购买或赠与文件，还是只有租赁、人防或长期使用合同，再确定遗产清单和办理路径。',
 'leadEn':'A family may refer to a home and its parking space as one package, but they may represent different rights. Check for separate registration and purchase documents, or whether the arrangement is a lease, civil-defence space or long-term use contract, before listing it as estate property.',
 'sections':[
  ('先找车位编号和独立权属资料','核对车位是否有独立不动产登记、买卖或赠与合同、付款凭证及发票。只写有“固定车位”的物业协议、停车卡或交费记录，未必能证明车位所有权。','Locate the space number and separate title records','Check for separate real estate registration, a sale or gift contract, payment records and invoices. A property agreement listing an allocated space, parking card or fee receipt may not prove ownership.'),
  ('合同性质决定能否登记转移','《民法典》允许规划车位通过出售、附赠或出租等方式约定归属；人防车位、公共车位或仅有使用权的安排，法律性质和可转移方式可能不同。剩余期限、物业管理条件和当地登记规则都要单独确认。','The contract determines whether a title transfer is available','The Civil Code allows planned parking spaces to be allocated by sale, gift or lease. A civil-defence or common space, or a use-only arrangement, may follow different transfer rules. Check the term, management conditions and local registration procedure.'),
  ('房屋和车位分项列入遗产清单','按“房屋”“产权车位”“使用合同权益”“未结费用”分栏登记。若车位已登记在死者名下，按当地不动产继承程序核实；若只是合同权益，联系开发商、管理方或出租方确认死亡后的变更、退费和剩余期限。','List the home and parking interest separately','Use separate entries for the home, owned space, contractual use interest and unpaid fees. If the space is registered to the deceased, check the local inheritance process. For a contractual right, ask the developer or manager about succession, refunds and the remaining term.')],
 'checkTitle':'車位資料核對表','check':['車位編號、位置及是否有獨立登記。','車位買賣、贈與、租賃或人防合同。','付款、管理費及剩餘期限記錄。','是否與房屋共有或限制轉讓。','登記機構、物業或合同相對方的答覆。'],
 'checkEn':['Space number, location and separate title entry.','Sale, gift, lease or civil-defence-space agreement.','Payments, management fees and remaining term.','Any co-ownership or transfer restriction.','Responses from the registry, manager or contract counterparty.']
},
{
 'id':'D24-F01','slug':'mainland-enterprise-annuity-inheritance-claim','folder':'hong-kong-other-estate','category':'funds-and-personal-estate','query':'内地企业年金遗属领取',
 'comp':('https://www.dehenglaw.com/CN/tansuocontent/0008/025433/7.aspx?MID=0902','企业年金案件特点及应对思路——企业年金法律系列'),
 'official':('https://www.mohrss.gov.cn/SYrlzyhshbzb/shehuibaozhang/zcwj/201712/t20171222_284833.html','企业年金办法'),
 'title':'内地企业年金遗属领取：向原单位核对账户和受益人','titleEn':'Claiming a Mainland enterprise-annuity balance after death',
 'lead':'长辈在企业工作多年，遗属未必知道是否参加企业年金。先联系原单位人事或年金经办机构，查询个人账户、已归属权益和指定受益人；企业年金与基本养老保险的遗属待遇不是同一笔款。',
 'leadEn':'A Hong Kong family may not know whether a deceased relative had an enterprise annuity. Ask the former employer or plan administrator for the account, vested balance and beneficiary designation. This is separate from survivor benefits under basic pension insurance.',
 'sections':[
  ('从原单位和计划管理人查账户','准备死亡证明、亲属关系和申请人身份资料，要求确认是否参加企业年金、账户管理机构、余额及单位计划约定。只查银行流水可能看不到尚未领取或由受托机构管理的年金权益。','Start with the former employer and plan administrator','Provide death, relationship and claimant identity records and ask whether the deceased joined a plan, who administers it, what balance remains and what the plan says. A bank statement may not reveal an annuity managed separately.'),
  ('核对余额归属与受益安排','企业年金办法对符合条件的个人账户资金领取有规定，但具体权益还要看计划、归属规则和领取状态。把已指定受益人、法定继承人、退休后已购买的保险产品分别核实，不要把所有年金金额按一个规则处理。','Check vesting and beneficiary arrangements','The enterprise-annuity rules address payment of eligible individual-account funds, but the plan, vesting status and payment stage matter. Verify a designated beneficiary, statutory heirs and any annuity insurance purchased at retirement separately.'),
  ('让经办方一次性列明申请材料','请管理机构说明申请表、死亡和关系证明、受益人资料、账户去向及是否需要继承公证或生效法律文书。若家属在香港，先问文件格式与授权要求，并保留提交清单、回执和结算明细。','Ask the administrator for a complete document list','Request the application form, death and relationship evidence, beneficiary information, payment destination and whether a notarised inheritance certificate or final court document is needed. Hong Kong applicants should confirm document format and authority requirements, keeping receipts and the final account statement.')],
 'checkTitle':'向年金经办方查询','check':['原单位名称、工作时间和可能的年金计划。','个人账户或权益记录单。','受益人指定及年金领取状态。','死亡、亲属关系和申请人身份证明。','经办方的材料清单、授权要求与结算回执。'],
 'checkEn':['Former employer and possible plan membership.','Individual account or benefit statement.','Beneficiary designation and payment status.','Death, relationship and claimant identity records.','The administrator’s document list, authority rules and settlement receipt.']
},
{
 'id':'D24-F02','slug':'mainland-occupational-annuity-deceased-account','folder':'hong-kong-other-estate','category':'funds-and-personal-estate','query':'内地职业年金遗产申领',
 'comp':('https://www.icbc.com.cn/page/721854096264167430.html','个人领取职业年金需要哪些条件'),
 'official':('https://www.jss.gov.cn/jss/zfxxgk/jczwgklyxxgk/SHBX/art/2022/art_ac0f7a7e07f4412c9a6c70b5d7dca906.html','机关事业单位养老保险政策问答'),
 'title':'内地职业年金遗产申领，香港家属先找参保单位和账户记录','titleEn':'Claiming a Mainland occupational-annuity balance after death',
 'lead':'职业年金常见于机关事业单位工作人员，但家属未必清楚它和基本养老金、企业年金的区别。先确认死者是否属于参保范围、个人账户余额及待遇领取阶段，再按参保单位和经办地办理。',
 'leadEn':'Occupational annuities are common for public-institution and government employees, but families may confuse them with basic pension benefits or enterprise annuities. Confirm plan membership, the individual balance and payment stage, then follow the employer’s and administering region’s process.',
 'sections':[
  ('先确认计划类型和参保经办地','从退休材料、工资单、权益记录单和原单位人事部门核实职业年金账户。异地调动或退休人员可能涉及不同经办地，香港家属应先找最后参保单位，避免把请求寄到不负责的窗口。','Confirm the plan and administering region','Check retirement records, pay slips, benefit statements and the former employer’s HR office. Transfers between regions or retirement can involve different administrators. Start with the last participating employer to identify the correct office.'),
  ('在职死亡和退休后死亡都要看账户阶段','官方政策问答说明，工作人员在职死亡以及退休后死亡，职业年金账户余额可以继承；但如何核算、是否已有按月领取或购买商业养老保险，要以账户和合同记录为准。不要把未来未发生的月待遇直接当成现存现金。','Check whether the account was in service or already paying benefits','Official guidance states that an occupational-annuity account balance may be inherited after death in service or after retirement. The calculation still depends on account and contract records, including monthly payments or an annuity-insurance purchase. Future payments are not automatically a cash balance.'),
  ('用书面申请确认收款路径','向经办机构索取账户权益核定、继承申请表及可接受的死亡、身份、关系和授权材料清单。涉及多个继承人时，应先确认款项支付给指定受益人还是依法确定的继承人，避免家属自行分款造成重复申请。','Confirm the payment route in writing','Ask the administrator for the account calculation, claim form and accepted death, identity, relationship and authority records. Where there are several heirs, confirm whether payment goes to a designated beneficiary or legally established heirs before anyone divides funds privately.')],
 'checkTitle':'核查職業年金前','check':['原工作单位、参保地及退休状态。','职业年金个人账户权益记录。','是否已领取待遇或购买年金保险。','指定受益人、继承人及关系证明。','经办机构书面确认的支付方式和材料。'],
 'checkEn':['Former employer, plan region and retirement status.','Occupational-annuity account statement.','Any benefits already paid or annuity insurance purchased.','Beneficiary, heir and relationship evidence.','Written payment route and document list from the administrator.']
},
{
 'id':'D24-F03','slug':'mainland-bond-inheritance-transfer-process','folder':'hong-kong-other-estate','category':'funds-and-personal-estate','query':'内地债券遗产查询办理',
 'comp':('https://www.icbc.com.cn/page/721852688718659625.html','柜台记账式债券非交易过户业务问答'),
 'official':('https://www.moj.gov.cn/pub/sfbgw/flfggz/flfggzbmgz/200907/t20090728_144726.html','债券登记托管结算管理办法'),
 'title':'内地债券遗产怎样查和过户：先找托管机构，再核非交易手续','titleEn':'Mainland bond inheritance: locate the custodian and confirm a non-trade transfer',
 'lead':'逝者账户里可能有储蓄国债、柜台债券或其他托管产品。香港家属先查清债券由哪家银行或登记托管机构记录，再问继承能否办理非交易过户，还是需要到期兑付或按规则赎回。',
 'leadEn':'A deceased person may have held savings bonds, bank-counter bonds or other custody products. A Hong Kong family should identify the bank or registry holding the position, then ask whether inheritance can be processed as a non-trade transfer or requires maturity or redemption under the product rules.',
 'sections':[
  ('先识别债券类型和托管渠道','查找银行流水、交易确认、债券账户卡、电子对账单和投资者代码。记下产品名称、托管机构、账户号码及付息日；银行代销的债券与银行存款不是同一产品，不能直接套用存款提取流程。','Identify the bond and custody channel','Look for bank statements, trade confirmations, custody cards, electronic statements and investor codes. Record the product, custodian, account number and payment dates. A bank-distributed bond is not a bank deposit and does not automatically follow deposit-withdrawal rules.'),
  ('询问继承是否属于非交易过户','部分柜台债券规则允许因继承办理非交易过户，通常需有效继承文件和受让方账户；不同债券及托管机构的材料、柜台和交易限制可能不同。先取得书面清单，不要为办过户而提前出售或分享密码。','Ask whether inheritance uses a non-trade transfer','Some counter-bond rules allow a non-trade transfer after inheritance, generally requiring valid succession documents and a receiving account. Documents, counters and trading restrictions vary by bond and custodian. Obtain a written list before selling or sharing account credentials.'),
  ('同步确认利息、到期和税费记录','要求机构核对持仓数量、应付利息、是否质押冻结、兑付或转入后的账户要求。继承人分散在香港和内地时，先确定由谁申请、谁开户和如何授权，并将结算单留作遗产账目。','Reconcile interest, maturity and restrictions','Ask the custodian to confirm quantity, accrued interest, pledges or freezes, maturity and the receiving-account requirements. If heirs are split between Hong Kong and the Mainland, decide who applies, opens the account and grants authority. Keep the settlement record in the estate accounts.')],
 'checkTitle':'债券查询与申请资料','check':['债券名称、账户号和托管机构线索。','交易确认、对账单及银行流水。','继承权证明、死亡证明和身份资料。','受让人债券托管账户要求。','付息、到期、冻结及费用核对记录。'],
 'checkEn':['Bond name, account number and custodian clues.','Trade confirmations, statements and bank records.','Succession, death and identity documents.','Requirements for the recipient custody account.','Interest, maturity, freeze and fee reconciliation.']
},
{
 'id':'D24-F04','slug':'mainland-payment-wallet-balance-after-death','folder':'hong-kong-other-estate','category':'funds-and-personal-estate','query':'内地电子支付账户继承',
 'comp':('https://www.vlaws.cn/show.aspx?cid=36&id=27285','数字遗产（微信/支付宝账号）怎么处理？'),
 'official':('https://sfj.gz.gov.cn/gzssfj/flfw/pf/yasf/content/post_10760952.html','广州市司法局：亲人去世后微信与支付宝余额能否继承'),
 'title':'内地电子支付账户有余额，香港家属怎样查资产和申请','titleEn':'A Mainland payment wallet has a balance: how heirs can identify and claim assets',
 'lead':'电子支付账号、钱包余额、平台内理财和聊天资料不是同一类权益。香港家属不要尝试冒用逝者密码登录；应通过平台官方渠道核实账户资产、欠款及可申请的项目，并把隐私信息与财产余额分开处理。',
 'leadEn':'A payment account, wallet balance, in-app investment and private messages are different kinds of interests. A Hong Kong family should not log in using the deceased’s credentials. Contact the platform through official channels to identify assets, debts and claimable items, separating financial value from private content.',
 'sections':[
  ('先分清余额、产品和账号使用权','钱包里可结算的余额或购买的金融产品，与账号本身、聊天记录或个人资料的访问权限不同。平台协议和核验规则可能限制账号转让；亲属身份不等于取得密码或读取所有信息的权利。','Separate money, financial products and account access','A withdrawable wallet balance or investment product differs from the account itself, messages or personal-data access. Platform terms may restrict account transfer. Kinship alone does not grant a password or access to all private information.'),
  ('通过客服渠道申请资产核查','准备死亡证明、关系证明、申请人身份证明及平台要求的其他材料，使用官方客服、遗产处理入口或依法取得的法院文书。要求平台说明余额、理财产品、未结交易、自动扣款和贷款欠款分别如何处理。','Request an asset review through official support','Prepare death, relationship and claimant identity records and any platform-specific documents. Use official customer support, estate procedures or a valid court document. Ask how the balance, investments, unsettled transactions, automatic charges and loan debts are handled separately.'),
  ('保护数据和其他用户隐私','账号内容可能涉及逝者和第三人的隐私，申请时说明只查询与遗产有关的资金和产品，不要求无关聊天内容。保存客服编号、提交材料、处理结果和实际到账凭证，避免把平台的账号回收规则误当成余额归零。','Protect data and third-party privacy','Account content may include the deceased’s and others’ private information. Limit a request to estate-related balances and products rather than unrelated messages. Keep support references, documents, decisions and payment records; account closure does not by itself establish that the balance is zero.')],
 'checkTitle':'联系平台前的资料','check':['可能使用的平台名称、手机号或实名线索。','死亡证明、亲属关系和申请人身份文件。','钱包余额、理财及扣款的现有记录。','官方客服工单号和书面处理要求。','需要查询的财产范围及隐私保护说明。'],
 'checkEn':['Platform name, phone number or identity clues.','Death, family relationship and claimant identity documents.','Available wallet, investment and payment records.','Official support ticket and written requirements.','The requested financial scope and privacy safeguards.']
},
{
 'id':'D24-F05','slug':'mainland-housing-allowance-estate-inquiry','folder':'hong-kong-other-estate','category':'funds-and-personal-estate','query':'内地住房补贴遗产申领',
 'comp':('https://www.sdcourt.gov.cn/jnanszqfy/389687/389688/6487277/index.html','继承纠纷中住房补贴的分割'),
 'official':('https://www.ggj.gov.cn/zcfg/zcjd/202201/t20220126_34981.htm','国家机关事务管理局：住房补贴发放问题解读'),
 'title':'内地住房补贴能否继承，先查发放依据和夫妻共有','titleEn':'Can a Mainland housing allowance be inherited? Check the entitlement and ownership history',
 'lead':'住房补贴可能仍在单位审核、尚未发放，或已经进入个人账户。香港家属应先向原单位查询政策依据、核定金额和发放时间，再判断它是死者个人已取得的财产、夫妻共同财产，还是尚未满足条件的待遇请求。',
 'leadEn':'A housing allowance may still be under employer review, unpaid or already credited to an account. Ask the former employer for the policy basis, approved amount and payment date, then determine whether it was the deceased’s acquired property, marital property or an entitlement that had not yet vested.',
 'sections':[
  ('核实补贴属于哪项政策','向单位索取住房补贴办法、资格审核、计算表和审批记录。不同单位和时期的发放条件并不相同；不要仅凭工资条上的简称或同事领取过，就推定逝者已取得相同金额。','Identify the governing allowance scheme','Request the employer’s scheme, eligibility review, calculation and approval records. Conditions differ by employer and period. A shorthand on a payslip or a colleague’s payment does not establish that the deceased had acquired the same amount.'),
  ('确认何时形成可主张的财产权利','核对补贴在死亡前是否已经核定、支付或划入账户，以及是否仍需住房状况、工龄或其他条件。若处于婚姻存续期间，还要分析取得时间与夫妻财产关系，先区分配偶的份额。','Determine whether a property right had accrued','Check whether the allowance was approved, paid or credited before death and whether housing status, service years or other conditions remained. If the entitlement arose during marriage, assess the acquisition date and marital-property position before calculating the estate.'),
  ('由单位书面说明申请路径','请经办单位列出申请人、材料、收款账户和期限，并区分住房补贴余额与公积金、养老金等项目。遇到继承人意见不同，要求单位暂缓有争议部分的处理并保留核定文件、通知和账目。','Ask the employer to confirm the claim route in writing','Request the claimant, documents, receiving account and deadline, distinguishing the allowance from housing-fund or pension balances. If heirs disagree, ask how disputed amounts are held and retain every calculation, notice and accounting record.')],
 'checkTitle':'查住房补贴時','check':['住房补贴政策及适用版本。','单位资格审核、核定金额和审批日期。','实际发放、账户入账或尚未支付状态。','婚姻及家庭住房情况材料。','经办单位对申请人、材料和期限的答复。'],
 'checkEn':['The housing-allowance scheme and applicable version.','Employer eligibility review, approved amount and date.','Payment, account credit or unpaid status.','Marriage and household-housing records.','The employer’s written claimant, document and deadline instructions.']
},
{
 'id':'D24-F06','slug':'mainland-bank-wealth-management-inheritance','folder':'hong-kong-other-estate','category':'funds-and-personal-estate','query':'内地理财产品遗产核查',
 'comp':('https://hankunlaw.com/upload/portal/20250612/f44ce3dcb89fa63aeb1a95cd6efa1d68.pdf','境外继承人继承内地遗产的财产调查问题'),
 'official':('https://www.gsjn.gov.cn/zfxxgk/xzxxgk/yaz/fdzdgknr/shbx/art/2024/art_c34de45c4111475b88c6f208f7ef419a.html','金融监管总局与人民银行关于已故存款人提取要求的通知'),
 'title':'内地银行理财产品列入遗产前，先核管理人和赎回条件','titleEn':'Before listing a Mainland wealth product as estate cash, check its manager and redemption terms',
 'lead':'银行账户里显示的理财不一定是现金存款。产品可能仍在封闭期、持有期或由独立理财管理人登记。香港家属先查产品名称、持有份额、净值日期和赎回规则，再申请赎回或非交易过户。',
 'leadEn':'A wealth product shown in a bank account is not necessarily a cash deposit. It may be locked, subject to a holding period or registered with a separate manager. Identify the product, units, valuation date and redemption rules before seeking redemption or a non-trade transfer.',
 'sections':[
  ('向银行和产品管理人分别核实','索取产品合同、风险揭示书、持仓或份额证明、最近净值及交易状态。银行可能只是销售机构，实际赎回或过户由产品管理人办理；两边所需材料应提前确认。','Check with both the bank and product manager','Obtain the product terms, risk disclosure, holding statement, latest valuation and transaction status. The bank may only distribute the product; redemption or transfer may be handled by the manager. Confirm both parties’ requirements first.'),
  ('分辨到期赎回和继承过户','监管通知提到，银行业机构可协助申请人向理财产品管理人申请赎回或非交易过户；产品合同、开放日和投资者适当性仍会影响具体处理。不能把小额存款简化提取规则理解为所有理财都能直接支取。','Distinguish redemption from inheritance transfer','A regulatory notice says banks should guide applicants to seek redemption or non-trade transfer from the product manager. The contract, dealing window and investor-suitability rules still matter. Simplified small-deposit procedures do not mean every investment can be withdrawn directly.'),
  ('以产品结算单更新遗产清单','记录申请日期、单位净值、赎回金额、费用、到账账户和未结收益。若家属还没确定分配比例，可先把产品状态和估值日记入清单，不要用旧买入金额代替当前价值。','Update the estate inventory from the settlement statement','Record the application date, unit value, redemption amount, fees, receiving account and unsettled returns. If heirs have not agreed on shares, list the product and valuation date without treating its original purchase price as its current value.')],
 'checkTitle':'向银行或管理人查询','check':['产品名称、管理人和销售渠道。','持仓份额、估值日期及是否封闭或冻结。','赎回、非交易过户和投资者资格要求。','继承证明、死亡和申请人身份材料。','结算金额、费用及到账凭证。'],
 'checkEn':['Product name, manager and sales channel.','Units, valuation date and any lock or freeze.','Redemption, non-trade transfer and investor eligibility rules.','Succession, death and claimant identity documents.','Settlement amount, fees and payment evidence.']
},
{
 'id':'D24-F07','slug':'mainland-mutual-fund-inheritance-transfer','folder':'hong-kong-other-estate','category':'funds-and-personal-estate','query':'内地基金份额继承登记',
 'comp':('https://www.gffunds.com.cn/xswd/bgxz/9/202308/t20230816_386644.shtml','办理继承过户流程及申请表'),
 'official':('https://www.chinaclear.cn/zdjs/editor_file/20200522161535403.pdf','中国结算投资者业务指南'),
 'title':'内地基金份额继承登记：确认账户、过户材料和小额程序','titleEn':'Registering inherited Mainland fund units: accounts, documents and simplified procedures',
 'lead':'逝者持有的基金份额不一定要先卖出再分款。基金管理人或登记机构可能办理继承类非交易过户；香港家属先确认基金在哪个销售渠道、登记机构是谁，以及受让人是否需要开立对应账户。',
 'leadEn':'Inherited fund units may not need to be sold before they are divided. A fund manager or registration agency may offer an inheritance-related non-trade transfer. First identify the sales channel and registrar and whether each recipient needs an account.',
 'sections':[
  ('先定位基金账户与登记机构','查看基金账户卡、交易确认、电子对账单和销售平台资料，确认基金代码、份额、销售机构及登记机构。不同基金和登记系统的业务表格、账户要求并不完全一致。','Locate the fund account and registrar','Review account cards, confirmations, statements and sales-platform records to identify each fund code, unit balance, distributor and registrar. Forms and account requirements differ across funds and registration systems.'),
  ('询问继承类非交易过户材料','常见材料会涉及继承权证明、死亡证明、继承人身份证明、业务申请表及受让账户；具体以基金管理人和登记机构现行要求为准。多名继承人应先写清份额分配，避免过户申请内容与协议、公证书或裁判文书不一致。','Ask for the inheritance transfer document list','Common requirements may include succession evidence, proof of death, heir identification, an application and recipient accounts. Confirm current requirements with the manager and registrar. Multiple heirs should agree on unit allocations before filing so the application matches the agreement or legal document.'),
  ('核实小额遗产简化安排是否适用','部分机构已公布小额已故投资者遗产的简化程序，但门槛、产品范围和申请主体有限定；基金不能赎回时，规则还可能要求改办非交易过户。先逐项核对適用条件，不要据此承诺一定可快速到账。','Check whether a simplified small-estate process applies','Some institutions publish simplified procedures for small investor estates, with limits on value, products and eligible applicants. If units cannot be redeemed, a non-trade transfer may be needed. Check each condition; do not assume quick payment is guaranteed.')],
 'checkTitle':'基金份额过户材料','check':['基金代码、份额和登记机构信息。','继承证明、死亡证明及继承人身份证明。','基金账户或受让账户开户要求。','多名继承人的份额分配文件。','小额遗产程序的额度和产品范围核对。'],
 'checkEn':['Fund codes, unit balances and registrar information.','Succession, death and heir identity documents.','Fund-account or recipient-account opening rules.','Allocation documents for multiple heirs.','Value and product limits for any simplified process.']
},
{
 'id':'D24-R01','slug':'mainland-hong-kong-inheritance-documents-transfer','folder':'hong-kong-other-estate','category':'inheritance-procedure','query':'内地港澳继承文书转递',
 'comp':('https://www.middlapartners.com/inbound/yanjiu/hk-macau-inheritance.html','港澳居民继承内地遗产：委托公证人制度全流程'),
 'official':('https://www.caao.org.hk/zh-CN/handling-notarization/notarized-documents','中国委托公证人协会：公证文书种类'),
 'title':'香港继承文件送内地使用，先核文书类型和转递要求','titleEn':'Using Hong Kong inheritance documents in Mainland China: verify the document and transfer route',
 'lead':'香港家属办理内地遗产时，身份声明、放弃继承、授权委托和香港法院文件用途不同，办理与转递路径也不一样。先问清内地接收机构要证明什么，再联系委托公证人准备对应文书。',
 'leadEn':'For a Mainland estate, a family-status declaration, renunciation, power of attorney and Hong Kong court document serve different purposes and follow different routes. Ask the Mainland receiving institution what must be proved, then prepare the matching document through the appropriate Hong Kong notarial process.',
 'sections':[
  ('先问内地接收机构需要证明的事实','把办理事项、资产所在地、继承人身份、是否有遗嘱及是否有人放弃继承说明清楚。接收方可能需要亲属关系及遗嘱状况声明、放弃声明、授权委托或法院文件，不能只说“做一份继承公证”。','Ask the Mainland recipient what fact must be proved','Explain the task, asset location, heirs, whether a will exists and whether anyone renounces. The recipient may need a family-and-will declaration, renunciation, authority or court document; a generic request for an inheritance notarisation is not specific enough.'),
  ('核对委托公证与审核转递环节','香港委托公证人协会公布的文书类型说明列明，继承或放弃内地遗产可使用相应声明；办理后还要核实是否需由中国法律服务（香港）有限公司审核、加章转递。先确认最新线上或纸本流程及文书格式。','Confirm the notary and transfer steps','The Hong Kong Association of China-Appointed Attesting Officers lists declarations for inheriting or renouncing Mainland estates. Confirm whether review, sealing and transfer by China Legal Services (Hong Kong) is required, and whether the current process is paper or electronic.'),
  ('把文书内容与实际申请逐项对应','核对姓名、证件号码、亲属关系、死者资料、资产所在地、授权事项与有效期限。香港文书完成后，把编号和接收方回执交给内地公证处、登记机构或银行，发现差异要先更正，避免反复补件。','Match each document to the actual application','Check names, identity numbers, family links, deceased details, asset location, authority and expiry. After completion in Hong Kong, keep the reference and Mainland receipt. Correct any mismatch before the file reaches the notary, registry or bank.')],
 'checkTitle':'委托公证前核对','check':['内地资产所在地及接收机构名称。','该机构要求证明的具体事实和文书格式。','死亡、身份、亲属关系及遗嘱材料。','是否办理放弃声明或授权委托。','审核转递流程、编号和接收回执。'],
 'checkEn':['Mainland asset location and receiving institution.','The specific fact and document format required.','Death, identity, family and will records.','Whether a renunciation or power of attorney is needed.','Review, transfer, reference number and receipt.']
},
{
 'id':'D24-R02','slug':'mainland-estate-inventory-overseas-heirs','folder':'hong-kong-other-estate','category':'inheritance-procedure','query':'内地遗产清单申报程序',
 'comp':('https://www.hankunlaw.com/upload/portal/20250612/f44ce3dcb89fa63aeb1a95cd6efa1d68.pdf','境外继承人继承内地遗产的资产调查难点'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/500681.html','最高人民法院：遗产管理人制度典型案例答记者问'),
 'title':'香港家属整理内地遗产清单，按权属、负债和证据分栏','titleEn':'An estate inventory for Mainland assets: separate ownership, debts and evidence',
 'lead':'跨境继承最容易漏掉的，往往不是一套房，而是资产线索散在不同银行、登记机构、单位和平台。先建立清单，区分死者个人财产、夫妻或家庭共有财产、债权债务和待核实权益，再决定查询或申报次序。',
 'leadEn':'In a cross-border inheritance, asset clues may be scattered across banks, registries, employers and platforms. Build an inventory that separates the deceased’s property, marital or family co-ownership, debts and unresolved interests before deciding what to investigate or report.',
 'sections':[
  ('清单记录资产线索，不先下归属结论','每项写明资产类别、机构、账号或地址、登记人、估值日期、原始凭证、共同权利人和目前状态。标注“已确认”“待查询”或“有争议”，不要把家人口述金额直接当成最终遗产数。','Record clues without deciding ownership too early','For each item, note its type, institution, account or address, registered holder, valuation date, source document, co-owners and status. Mark it confirmed, pending or disputed; do not treat a family estimate as the final estate value.'),
  ('先析产，再统计死者可继承部分','房屋、存款、证券和补贴可能有夫妻共同、共有或他人代持部分。先找出登记及资金来源，再把配偶或共同权利人的份额剥离；对尚未确认的房屋或平台资产保留争议栏。','Separate co-owned property before calculating the estate','Homes, deposits, securities and allowances may include a spouse’s or another person’s share. Check title and funding, separate proven co-ownership first, and retain a disputed category for unresolved property or platform balances.'),
  ('按机构分批查询并保存结果','房屋向所在地登记机构查询，年金向单位或管理人查询，账户资产向银行、证券或平台走正式渠道。需要法院调查收集的，先整理具体线索、持有人和查询理由。每次申请记录提交日、回函、补件和新发现。','Query institutions in batches and preserve results','Ask the local property registry, employer or annuity manager, bank, securities firm or platform through formal channels. For a court-assisted inquiry, prepare the target holder, specific lead and reason. Log dates, replies, missing items and new findings.')],
 'checkTitle':'遗产清单字段','check':['资产类别、机构和账号或地址线索。','登记权利人、共同权利人及来源凭证。','估值日期、负债、收入和限制状态。','查询机构、申请时间和书面答复。','已确认、待查及有争议事项的区分。'],
 'checkEn':['Asset type, institution and account or address clues.','Registered and co-owners with source documents.','Valuation date, debts, income and restrictions.','Inquiry destination, application date and written response.','Separate confirmed, pending and disputed entries.']
},
{
 'id':'D24-R03','slug':'mainland-multiple-wills-conflict-review','folder':'hong-kong-other-estate','category':'inheritance-procedure','query':'内地多份遗嘱效力判断',
 'comp':('https://www.jingyinlaw.com/news-info.php?classID=4&id=3701','多份遗嘱的效力认定：内容抵触时，以最后一份有效遗嘱为准'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/386521.html','最高人民法院贯彻实施民法典典型案例'),
 'title':'多份遗嘱涉及内地财产，香港家属先核时间、形式和冲突部分','titleEn':'Several wills cover Mainland assets: compare dates, formalities and conflicting clauses',
 'lead':'家属找到几份遗嘱时，不宜只看哪份更新或是否公证。先逐份核对订立日期、形式、签署和见证、立遗嘱能力及处分财产范围；存在冲突的条款，再按适用法律判断。',
 'leadEn':'When a family finds several wills, the newest or notarised document should not be selected without review. Compare each date, form, signature, witnesses, capacity and property scope, then assess conflicting clauses under the applicable law.',
 'sections':[
  ('把每份遗嘱的原件和形成过程固定下来','保存原件、封套、草稿、修改痕迹、见证人资料、录像和保管记录，扫描件不替代原件。记录家属何时、从何处找到文件，不要在原件上写注或自行订在一起。','Preserve each original and its creation history','Keep originals, envelopes, drafts, edits, witness details, recordings and custody records. A scan is not a substitute for an original. Record when and where each document was found; do not annotate or staple originals.'),
  ('逐份检查形式与真实意思','自书、代书、打印、录音录像等形式有不同要求。对打印或代书文件，重点核实见证人资格、是否全程在场、签名和日期；同时看订立时的认知情况、胁迫或欺诈争议及是否处分本人财产。','Test formal validity and genuine intent','Handwritten, witnessed, printed, audio and video wills have different formal requirements. For printed or dictated documents, verify witness eligibility, presence throughout, signatures and date. Also consider capacity, coercion allegations and whether the will covers the testator’s own property.'),
  ('冲突只按实际冲突范围处理','内地《民法典》规定，立有数份遗嘱且内容相抵触的，以最后的遗嘱为准，但每份遗嘱是否有效、是否覆盖同一财产仍要先审查。涉及香港制作的文件及跨境继承时，另核遗嘱形式与准据法，不宜只凭日期作决定。','Resolve only the portions that actually conflict','The Mainland Civil Code provides that where several wills conflict, the later will prevails. First establish that each is valid and covers the same property. For a Hong Kong document or cross-border succession, separately assess form and governing law rather than relying on date alone.')],
 'checkTitle':'多份遗嘱核对表','check':['每份文件原件、日期和保管来源。','遗嘱形式、签名、见证人及录像资料。','立遗嘱时的能力及争议线索。','每份遗嘱处分的具体财产和条款冲突。','遗嘱制作地、资产所在地及适用法律问题。'],
 'checkEn':['Originals, dates and custody history for every will.','Form, signatures, witnesses and recordings.','Capacity and any evidence of a dispute.','Property covered and clauses that conflict.','Place of execution, asset location and governing-law questions.']
},
{
 'id':'D24-R04','slug':'mainland-inheritance-evidence-preservation-application','folder':'hong-kong-other-estate','category':'inheritance-procedure','query':'内地遗产诉讼证据保全',
 'comp':('https://hankunlaw.com/upload/portal/20250612/f44ce3dcb89fa63aeb1a95cd6efa1d68.pdf','境外继承人继承内地遗产的诉讼和财产风险'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/212721.html','最高人民法院关于民事诉讼证据的若干规定'),
 'title':'内地继承诉讼证据可能灭失，香港家属怎样申请证据保全','titleEn':'Evidence in a Mainland inheritance case may disappear: when to seek preservation',
 'lead':'遗产争议中的监控、手机记录、原始票据或账户资料可能被删除、覆盖或难以再次取得。香港家属要先写清证据在哪里、证明什么、为何可能灭失，再尽快咨询受理法院是否需要证据保全或法院调查。',
 'leadEn':'Surveillance footage, phone records, original receipts or account data in an estate dispute may be deleted, overwritten or become difficult to obtain. Identify where the evidence is, what it proves and why it may disappear, then promptly ask the court about preservation or judicial collection.',
 'sections':[
  ('列明证据内容和保管人','不要只写“申请保全全部遗产资料”。列出具体设备、文件、账号、时间范围和控制人，说明它与遗嘱真伪、财产流向、居住或代持争议的关联。先自行合法保存现有副本，并记录来源和取得日期。','Identify the evidence and its custodian','Avoid a general request to preserve all estate material. Specify the device, file, account, date range and person controlling it, and explain its link to a will, asset transfer, occupation or nominee dispute. Preserve lawful copies and record their source and date.'),
  ('说明紧迫性并选对程序','根据《民事诉讼证据的若干规定》，诉讼中的证据保全应在举证期限届满前提出；紧急情况下，法律允许符合条件的诉前保全申请。是否需要担保、法院采取什么措施，要由法院结合证据和影响判断。','Explain urgency and choose the correct procedure','Under the Supreme People’s Court evidence rules, a trial-stage preservation request should be made before the evidence period expires. In urgent cases, pre-action preservation may be available where legal conditions are met. The court decides whether security or a particular measure is required.'),
  ('把申请、法院答复和替代副本留档','申请书写明证据名称、位置、待证明事实、灭失风险及无法自行取得的原因。同步保存合法截屏、原始设备、邮件回执和证据交接记录；申请错误可能造成损失，范围应与争点相称。','Keep the application, court response and backup copies','State the evidence, location, fact to be proved, risk of loss and why it cannot be collected independently. Preserve lawful screenshots, original devices, delivery records and chain-of-custody notes. A mistaken request may cause loss, so tailor its scope to the dispute.')],
 'checkTitle':'准备证据保全申请','check':['证据名称、载体、所在位置和保管人。','需要证明的继承争议事实。','证据可能灭失或难以取得的具体原因。','举证期限、紧急程度和法院联系信息。','已有副本、来源说明及保管记录。'],
 'checkEn':['Evidence description, format, location and custodian.','The inheritance issue the evidence would prove.','Specific risk of loss or difficulty obtaining it later.','Evidence deadline, urgency and court details.','Existing copies, source notes and custody records.']
},
{
 'id':'D24-R05','slug':'mainland-estate-administrator-court-appointment','folder':'hong-kong-other-estate','category':'inheritance-procedure','query':'内地遗产管理人指定程序',
 'comp':('https://www.jtn.com/CN/booksdetail.aspx?Lan=CN&PageUrl=majorbook&keyid=00000000000000007723&type=06001','遗产管理人制度在实践中的应用探析'),
 'official':('https://www.court.gov.cn/zixun/xiangqing/500681.html','最高人民法院遗产管理人制度典型案例答记者问'),
 'title':'内地遗产管理人确定有争议，香港利害关系人怎样申请指定','titleEn':'A dispute over a Mainland estate administrator: how an interested person can seek appointment',
 'lead':'多名继承人互不信任、遗产无人管理或遗嘱执行人资格有争议时，先确认现有管理人是否已依法确定。若确定本身存在争议，利害关系人可以按内地程序向法院申请指定；并非每宗继承案都要另走这一程序。',
 'leadEn':'If heirs distrust one another, no one manages the assets or the executor’s role is disputed, first establish whether an administrator has already been determined by law. An interested person may apply to a Mainland court where the appointment itself is disputed; a separate application is not required in every inheritance case.',
 'sections':[
  ('先按民法典确定现有管理人','核对遗嘱是否指定执行人、继承人是否已推选管理人，以及是否存在依法担任的主体。若身份和权限均无争议，可先确认其管理范围；管理人不等于可以自行改变遗嘱或分配遗产。','Identify the existing administrator under the Civil Code','Check whether a will appoints an executor, heirs have chosen a person, or another statutory role applies. If identity and authority are undisputed, confirm the management scope. An administrator cannot rewrite a will or distribute property at will.'),
  ('确定管理人有争议时准备申请材料','最高人民法院说明，对确定有争议的，利害关系人可向法院申请指定遗产管理人，并按特别程序处理。香港申请人要整理身份、利害关系、死者住所或经常居所、继承人情况、遗产线索及争议原因。','Prepare an application if the appointment is disputed','The Supreme People’s Court explains that an interested person may ask the court to appoint an administrator where the determination is disputed, using a special procedure. A Hong Kong applicant should organise identity, interest, the deceased’s residence, heirs, asset clues and the reason for disagreement.'),
  ('申请中说明管理需要和拟任人条件','列明需要保管、查询、收租、偿债或处理的事项，以及现有冲突和风险。若提名某位人选，提供其与死者及继承人的关系、管理能力和利益冲突信息。获指定后仍须依法保存账目、报告处理情况并保护遗产权利。','Explain the need and suitability of a proposed person','Describe the tasks—preservation, inquiries, rent, debts or administration—and the existing conflict or risk. If proposing a person, provide their relationship, ability and potential conflicts. Once appointed, the administrator must keep accounts, report actions and protect estate interests.')],
 'checkTitle':'法院申请前整理','check':['遗嘱执行人、推选管理人及现有管理安排。','申请人身份和与遗产的利害关系。','其他继承人、住所线索和争议事实。','需要保管或处理的资产及紧迫风险。','拟任人选的能力、关系和利益冲突说明。'],
 'checkEn':['Executor, any heir-selected administrator and current arrangements.','Applicant identity and legal interest in the estate.','Other heirs, residence clues and facts in dispute.','Assets needing protection or administration and urgency.','A proposed candidate’s ability, relationship and conflicts.']
},
{
 'id':'D24-R06','slug':'mainland-minor-inherits-property-guardian-registration','folder':'hong-kong-other-estate','category':'inheritance-procedure','query':'内地未成年人继承房产监护人签字',
 'comp':('https://www.dehenglaw.com/cn/newscontent/0006/036540/2.aspx?MID=0876','指定监护案与跨境遗产处置'),
 'official':('https://www.shantou.gov.cn/stszrzyj/zwgk/gzdt/content/post_2529754.html','汕头市不动产登记交易中心继承登记业务便民解答'),
 'title':'未成年人继承内地房产，监护人代办要注意什么','titleEn':'A minor inherits Mainland property: what the guardian should know',
 'lead':'未成年人可以继承内地房产，登记申请通常由法定监护人代办。香港家属还要处理监护关系证明、可能存在的利益冲突，以及之后出售或处分房屋时“为了未成年人利益”的审查要求。',
 'leadEn':'A minor can inherit Mainland property, with a legal guardian generally applying on the child’s behalf. Hong Kong families should also prepare proof of guardianship, address any conflict of interest and understand the child-benefit review that may apply to a later sale or disposition.',
 'sections':[
  ('先准备能证明监护关系的文件','出生医学证明、户口资料、收养登记或法院指定监护人的文书，均可能用于证明监护关系；具体接受哪些材料要问房屋所在地登记机构。监护人和未成年人在香港时，还要核对身份文件与授权方式。','Prepare evidence of guardianship','A birth record, household record, adoption document or court guardianship order may establish the relationship. Ask the local registry what it accepts. If both guardian and child are in Hong Kong, also confirm identity documents and authority requirements.'),
  ('登记继承与之后处分房屋是两步','继承登记让未成年人取得其依法享有的产权份额。日后出售、抵押或放弃权益时，监护人须保护未成年人利益；不宜为了方便成年继承人分房而让孩子签署放弃或无偿转让文件。','Treat inheritance registration and later disposal as separate steps','Inheritance registration records the minor’s lawful share. A later sale, mortgage or waiver must protect the child’s interests. Do not ask the child to renounce or transfer property without payment merely to simplify the adults’ arrangement.'),
  ('监护人自身有利益冲突时先处理代表问题','若监护人同时是其他继承人、交易受让人或与孩子利益相反的一方，先向公证、登记或法院机构说明，确认是否需要另一监护人共同签署或依法确定独立代表。保留估价、交易理由和价款流向，证明决定服务于未成年人。','Address conflicts before the guardian signs','If the guardian is also another heir, purchaser or a person whose interests conflict with the child’s, disclose this and ask whether another guardian or independent representative is required. Keep valuations, reasons and payment records to show the decision protects the minor.')],
 'checkTitle':'监护人办理资料','check':['未成年人身份及出生、收养或户籍证明。','法定监护关系证明及监护人身份证明。','继承登记所需死亡、亲属和产权材料。','是否存在监护人与其他继承人的利益冲突。','日后出售或处分时证明符合未成年人利益的材料。'],
 'checkEn':['The minor’s identity, birth, adoption or household records.','Guardianship evidence and the guardian’s identification.','Death, family and title documents for registration.','Any conflict between the guardian and other heirs.','For a later disposal, records showing the child’s interests are protected.']
},
]

def convert(value):
    if isinstance(value, str): return S2T.convert(S2HK.convert(value))
    if isinstance(value, list): return [convert(x) for x in value]
    if isinstance(value, dict): return {k:convert(v) for k,v in value.items()}
    return value

def simplify(value):
    if isinstance(value, str): return T2S.convert(value)
    if isinstance(value, list): return [simplify(x) for x in value]
    if isinstance(value, dict): return {k:simplify(v) for k,v in value.items()}
    return value

SOURCE_TYPES = {'D24-F02':'industry','D24-F03':'industry','D24-F05':'court_case','D24-F07':'industry'}

def make(story):
    source_type = SOURCE_TYPES.get(story['id'], 'competitor')
    source_note = ('基金管理人/金融机构的业务材料，仅用于核对产品办理线索；不代表法律意见。' if source_type == 'industry' else '法院公布的相关案件，仅用于观察争议焦点；未据此推定全国统一裁判结果。' if source_type == 'court_case' else '同行法律文章，仅用于识别读者问题和内容切入点；未沿用其品牌、案例叙述或段落结构。')
    source_comp = {'url':story['comp'][0],'title':story['comp'][1],'type':source_type,'notes':source_note+' Google 前两页因验证未完成，未记录排名。'}
    source_official = {'url':story['official'][0],'title':story['official'][1],'type':'official','notes':'用于核对内地法律、主管机构或地方办理信息；当地指南仅作该地区示例，不外推为全国统一材料清单。'}
    qurl = 'https://www.google.com.hk/search?q=' + quote(story['query'])
    base = {
      'id':story['id'],'slug':story['slug'],'folder':story['folder'],'category':story['category'],
      'research':{'query':story['query'],'searchUrl':qurl,'viewedPages':[],'observedAt':'2026-10-23','method':'web search fallback; Google via Playwright encountered a new CAPTCHA after one verified query','notes':'已用公开网页搜索核对相关同行法律文章或行业办理资料及官方材料，并按内地法律范围原创改写。Google 后续关键词请求再次触发验证，因此未把 Google 第1、2页或排名记为已查。搜索量未测。'},
      'sources':[source_comp,source_official],
      'related':story.get('related') or [
        {'url':'https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/asset-clue-list.html','label':{'zh-Hant':'整理內地遺產線索','zh-Hans':'整理内地遗产线索','en':'Organising clues to Mainland assets'}},
        {'url':'https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/documents.html','label':{'zh-Hant':'香港家屬辦理內地繼承文件','zh-Hans':'香港家属办理内地继承文件','en':'Documents for Hong Kong families handling Mainland inheritance'}}
      ],
      'languages':{
       'zh-Hans':simplify({'title':story['title'],'lead':story['lead'],'sections':[{'heading':h,'paragraphs':[p]} for h,p,_,_ in story['sections']],'checklistTitle':story['checkTitle'],'checklist':story['check']}),
       'en':{'title':story['titleEn'],'lead':story['leadEn'],'sections':[{'heading':he,'paragraphs':[pe]} for _,_,he,pe in story['sections']],'checklistTitle':'Documents and points to check','checklist':story['checkEn']}
      }
    }
    base['languages']['zh-Hant'] = convert(base['languages']['zh-Hans'])
    return base

def main():
    assert len(DATA) == 20 and len({x['query'] for x in DATA}) == 20
    prop=[make(x) for x in DATA if x['id'].startswith('D24-P')]
    funds=[make(x) for x in DATA if x['id'].startswith('D24-F')]
    procedure=[make(x) for x in DATA if x['id'].startswith('D24-R')]
    OUT.mkdir(parents=True,exist_ok=True)
    for name,items in [('property-seven.json',prop),('funds-seven.json',funds),('procedure-six.json',procedure)]:
        (OUT/name).write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'stories':len(DATA),'groups':[len(prop),len(funds),len(procedure)],'draftDir':str(OUT)},ensure_ascii=False))

if __name__ == '__main__': main()
