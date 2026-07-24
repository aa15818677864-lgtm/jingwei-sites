from __future__ import annotations

import re

from publish_regional_inheritance_foundations import (
    LANG_SUFFIX,
    ROOT,
    SITE,
    TODAY,
    article_path,
    render_article,
)


REJECTED_SLUG = "co-owned-mainland-property"

ARTICLE = {
    "slug": "us-trust-and-mainland-property",
    "directory": "articles/us",
    "topic": "united-states",
    "copy": {
        "tc": {
            "lang": "zh-Hant",
            "locale": "zh_HK",
            "brand": "劉毅律師團隊",
            "brand_sub": "跨境中國法律事務",
            "eyebrow": "文章 / 美國 living trust（生前信託）與內地房產",
            "title": "美國 living trust 寫了內地房產，家屬還要先查甚麼",
            "description": "美國 living trust 列有內地房產時，家屬先核對信託文件、實際入信託證據和內地登記，再決定由受託人或遺產代表處理。",
            "lead": "信託文件寫到一套房，不等於內地登記已經轉到信託名下。",
            "key_title": "先把三個答案寫在一頁",
            "keys": [
                "最新信託版本有沒有寫這套房",
                "內地房產現在登記給誰",
                "手上是受託人文件還是遺產代表文件",
            ],
            "answer_title": "先查房產有沒有真正放進信託",
            "answer": [
                "加州的公開指引把兩件事分得很清楚：文件已簽署是一回事，資產有沒有實際放進信託是另一回事。只有信託真正持有的資產，才可按信託路徑判斷；附件或資產清單只寫了一個內地地址，不能單獨證明房產登記已完成轉移。",
                "內地房產仍要從目前登記出發。美國信託文件可以幫助說明安排、受託人和受益人，但不會自行改掉內地登記，也不能替房產所在地決定申請人和所需材料。先核對事實，再判斷走信託、繼承或爭議處理。",
            ],
            "sections": [
                (
                    "一、不要只看一頁資產清單",
                    [
                        "先找完整信託文件、所有修改頁、資產附件、受託人接受文件和相關遺囑。記下設立人、原受託人、後任受託人、受益人，以及親人去世後由誰接任。只有摘要或 certificate of trust 時，先確認它能證明哪些事項。",
                        "同一套房在不同版本中出現或被刪除時，把版本日期排成時間線。不要只截出寫有房產的一頁，也不要把含有其他家庭資產和身份資料的整份信託轉發給不相關的人。",
                    ],
                ),
                (
                    "二、查清內地房產有沒有實際入信託",
                    [
                        "核對最新房產登記、原購房合同、付款、歷次轉名文件，以及有沒有專門處理這套房的書面轉移文件。若房產一直登記在逝者個人名下，不能只因信託附件列了地址，便對外說房產已由信託持有。",
                        "反過來，如果家屬找到與信託安排相配的轉移文件或內地登記變更，也不要只靠文件標題下結論。不要倒簽文件，也不要把信託資產清單當成已完成的轉名證明。把原件、簽署日期、登記日期和目前權利人放在同一頁，再向房產所在地確認文件可以回答甚麼。",
                    ],
                ),
                (
                    "三、把受託人、遺產代表和受益人分開",
                    [
                        "後任受託人負責信託內的資產；遺產代表處理屬於逝者遺產的事項；受益人是可能取得利益的人。三者可能是同一人，也可能完全不同。被寫成受益人，不代表可以直接要求內地房產轉到自己名下。",
                        "先確認手上的是受託人接任文件、法院簽發的遺產代表文件，還是只有遺囑中的提名。每份文件回答的權限不同。家屬也不應在身份未核清時，以受託人或遺產代表名義簽署內地文件。",
                    ],
                ),
                (
                    "四、用兩條路徑表決定下一步",
                    [
                        "第一條寫信託路徑：完整文件、入信託證據、現任受託人和受益安排。第二條寫內地房產路徑：目前登記、取得經過、限制、繼承人和當地接收要求。兩條都清楚後，才判斷由誰申請和要補哪一組文件。",
                        "若房產仍在逝者個人名下，可能仍要處理死亡、親屬、遺囑或繼承查驗；若家屬主張房產已屬信託但登記沒有反映，則可能先要處理權屬證據和爭議。不同州和不同內地城市的做法都可能不同，不能只套用加州信託文件。",
                    ],
                ),
            ],
            "related_title": "同一專題繼續閱讀",
            "related": [
                ("/articles/united-states/", "美國家屬處理內地遺產專題"),
                ("/articles/us/us-will-mainland-property.html", "美國遺囑寫到內地房產為何不能直接轉名"),
                ("/articles/us/mainland-asset-omitted-from-probate.html", "內地資產沒有寫進美國遺產文件怎樣辦"),
                ("/articles/us/letters-testamentary-or-administration.html", "常見美國遺產代表文件怎樣分"),
            ],
            "cta": "把信託首頁、修改頁、資產附件、受託人文件和內地房產登記列在一頁，我們先分清信託內資產、逝者遺產和仍待核對的權屬。",
        },
        "cn": {
            "lang": "zh-Hans",
            "locale": "zh_CN",
            "brand": "刘毅律师团队",
            "brand_sub": "跨境中国法律事务",
            "eyebrow": "文章 / 美国 living trust（生前信托）与内地房产",
            "title": "美国 living trust 写了内地房产，家属还要先查什么",
            "description": "美国 living trust 列有内地房产时，家属先核对信托文件、实际入信托证据和内地登记，再决定由受托人或遗产代表处理。",
            "lead": "信托文件写到一套房，不等于内地登记已经转到信托名下。",
            "key_title": "先把三个答案写在一页",
            "keys": [
                "最新信托版本有没有写这套房",
                "内地房产现在登记给谁",
                "手上是受托人文件还是遗产代表文件",
            ],
            "answer_title": "先查房产有没有真正放进信托",
            "answer": [
                "加州的公开指引把两件事分得很清楚：文件已经签署是一回事，资产有没有实际放进信托是另一回事。只有信托真正持有的资产，才可以按照信托路径判断；附件或资产清单只写了一个内地地址，不能单独证明房产登记已经完成转移。",
                "内地房产仍要从目前登记出发。美国信托文件可以帮助说明安排、受托人和受益人，但不会自行更改内地登记，也不能替房产所在地决定申请人和所需材料。先核对事实，再判断走信托、继承或争议处理。",
            ],
            "sections": [
                (
                    "一、不要只看一页资产清单",
                    [
                        "先找完整信托文件、所有修改页、资产附件、受托人接受文件和相关遗嘱。记下设立人、原受托人、后任受托人、受益人，以及亲人去世后由谁接任。只有摘要或 certificate of trust 时，先确认它能证明哪些事项。",
                        "同一套房在不同版本中出现或被删除时，把版本日期排成时间线。不要只截出写有房产的一页，也不要把含有其他家庭资产和身份资料的整份信托转发给不相关的人。",
                    ],
                ),
                (
                    "二、查清内地房产有没有实际入信托",
                    [
                        "核对最新房产登记、原购房合同、付款、历次转名文件，以及有没有专门处理这套房的书面转移文件。如果房产一直登记在逝者个人名下，不能只因为信托附件列了地址，就对外说房产已经由信托持有。",
                        "反过来，如果家属找到与信托安排相配的转移文件或内地登记变更，也不要只靠文件标题下结论。不要倒签文件，也不要把信托资产清单当成已经完成的转名证明。把原件、签署日期、登记日期和目前权利人放在同一页，再向房产所在地确认文件可以回答什么。",
                    ],
                ),
                (
                    "三、把受托人、遗产代表和受益人分开",
                    [
                        "后任受托人负责信托内的资产；遗产代表处理属于逝者遗产的事项；受益人是可能取得利益的人。三者可能是同一人，也可能完全不同。被写成受益人，不代表可以直接要求内地房产转到自己名下。",
                        "先确认手上的是受托人接任文件、法院签发的遗产代表文件，还是只有遗嘱中的提名。每份文件回答的权限不同。家属也不应在身份没有核清时，以受托人或遗产代表名义签署内地文件。",
                    ],
                ),
                (
                    "四、用两条路径表决定下一步",
                    [
                        "第一条写信托路径：完整文件、入信托证据、现任受托人和受益安排。第二条写内地房产路径：目前登记、取得经过、限制、继承人和当地接收要求。两条都清楚后，才判断由谁申请和要补哪一组文件。",
                        "如果房产仍在逝者个人名下，可能仍要处理死亡、亲属、遗嘱或继承查验；如果家属主张房产已经属于信托但登记没有反映，则可能先要处理权属证据和争议。不同州和不同内地城市的做法都可能不同，不能只套用加州信托文件。",
                    ],
                ),
            ],
            "related_title": "同一专题继续阅读",
            "related": [
                ("/articles/united-states/index_cn.html", "美国家属处理内地遗产专题"),
                ("/articles/us/us-will-mainland-property_cn.html", "美国遗嘱写到内地房产为何不能直接转名"),
                ("/articles/us/mainland-asset-omitted-from-probate_cn.html", "内地资产没有写进美国遗产文件怎么办"),
                ("/articles/us/letters-testamentary-or-administration_cn.html", "常见美国遗产代表文件怎样区分"),
            ],
            "cta": "把信托首页、修改页、资产附件、受托人文件和内地房产登记列在一页，我们先分清信托内资产、逝者遗产和仍待核对的权属。",
        },
        "en": {
            "lang": "en",
            "locale": "en_US",
            "brand": "Liu Yi Lawyer Team",
            "brand_sub": "Cross-border Mainland China legal matters",
            "eyebrow": "Article / A U.S. living trust and a Mainland home",
            "title": "A U.S. Living Trust Names a Mainland Home: What the Family Must Check",
            "description": "A practical guide for families checking whether a Mainland home named in a U.S. living trust was actually placed in the trust and who can act next.",
            "lead": "Naming a home in the trust papers does not mean the Mainland property record changed.",
            "key_title": "Put three answers on one page",
            "keys": [
                "Whether the latest trust version names the home",
                "Who appears on the current Mainland record",
                "Whether the family holds trustee or estate papers",
            ],
            "answer_title": "First check whether the home was actually placed in the trust",
            "answer": [
                "California court guidance separates signing a trust from funding it. The trust route applies to assets the trust actually holds. A Mainland address appearing on a schedule or asset list, without more, does not prove that the property record was transferred to the trust.",
                "Start with the current Mainland property record. The U.S. trust papers may identify the plan, trustee and beneficiaries, but they do not change that record by themselves or decide who may apply locally. Confirm the facts before choosing a trust, inheritance or dispute route.",
            ],
            "sections": [
                (
                    "1. Do not rely on one asset schedule",
                    [
                        "Find the complete trust, every amendment, asset schedule, trustee-acceptance paper and related will. Record the settlor, original trustee, successor trustee, beneficiaries and who takes office after the death. If the family has only a certificate of trust, identify exactly what it proves.",
                        "If the same home appears in one version and disappears from another, build a dated version list. Do not keep only the page naming the property, and do not circulate unrelated family assets and identity details with the entire trust file.",
                    ],
                ),
                (
                    "2. Check whether the Mainland home was funded into the trust",
                    [
                        "Compare the latest property record with the purchase contract, payment history, later title papers and any written instrument specifically addressing the home. If the deceased remained the registered owner, a schedule naming the address is not enough to tell others that the trust held title.",
                        "If the family finds a transfer paper or registration change that appears consistent with the trust, do not rely on its heading alone. Do not backdate a document or treat an asset schedule as a completed title transfer. Put the original, signature date, registration date and current owner on one sheet, then ask the registration city what the document establishes there.",
                    ],
                ),
                (
                    "3. Separate the trustee, personal representative and beneficiary",
                    [
                        "A successor trustee administers trust property. A personal representative handles matters belonging to the estate. A beneficiary may receive a benefit. The same person can hold all three roles, but often does not. Being named as a beneficiary is not authority to retitle the Mainland home directly.",
                        "Identify whether the family has a trustee-succession paper, a court-issued personal representative document or only a nomination in a will. Each answers a different authority question. No one should sign a Mainland application as trustee or personal representative before that role is established.",
                    ],
                ),
                (
                    "4. Use two tracks to choose the next step",
                    [
                        "On the trust track, list the complete instrument, funding evidence, current trustee and beneficiary terms. On the Mainland track, list the current record, acquisition history, restrictions, heirs and receiving requirements. Only then decide who should apply and which documents are missing.",
                        "If the home remained in the deceased's name, death, family, will or inheritance-review material may still be needed. If the family says the trust owned it but the record does not, ownership evidence and a dispute may come first. State law and local Mainland practice vary, so do not apply a California trust document as a universal answer.",
                    ],
                ),
            ],
            "related_title": "Continue with the U.S. topic",
            "related": [
                ("/articles/united-states/index_en.html", "U.S. families handling a Mainland estate"),
                ("/articles/us/us-will-mainland-property_en.html", "A U.S. will names Mainland property: what comes next"),
                ("/articles/us/mainland-asset-omitted-from-probate_en.html", "A Mainland asset is missing from U.S. probate papers"),
                ("/articles/us/letters-testamentary-or-administration_en.html", "Letters Testamentary and Letters of Administration"),
            ],
            "cta": "Put the trust cover, amendments, asset schedule, trustee papers and current Mainland property record on one page. We can separate trust property, estate property and disputed ownership.",
        },
    },
}


HUB_UPDATES = {
    "articles/united-states/index.html": (
        "/articles/us/us-trust-and-mainland-property.html",
        '<a href="/articles/us/us-trust-and-mainland-property.html"><span class="v24-tag">美國信託</span><strong>living trust 寫了內地房產，還要先查甚麼</strong><p>分清信託清單、實際入信託和內地登記。</p></a>',
    ),
    "articles/united-states/index_cn.html": (
        "/articles/us/us-trust-and-mainland-property_cn.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">美国信托</span><h3>living trust 写了内地房产，还要先查什么</h3><p>分清信托清单、实际入信托和内地登记。</p></div><a class="v25-pill-action" href="/articles/us/us-trust-and-mainland-property_cn.html">阅读文章</a></article>',
    ),
    "articles/united-states/index_en.html": (
        "/articles/us/us-trust-and-mainland-property_en.html",
        '<article class="v25-pillar-card"><div class="v25-pillar-copy"><span class="v25-card-label">U.S. living trust</span><h3>A living trust names a Mainland home</h3><p>Separate the asset schedule, trust funding and property record.</p></div><a class="v25-pill-action" href="/articles/us/us-trust-and-mainland-property_en.html">Read Article</a></article>',
    ),
}


def remove_hub_card(text: str, href: str, traditional: bool) -> str:
    at = text.find(href)
    if at < 0:
        return text
    if traditional:
        start = text.rfind('<a href="', 0, at)
        end = text.find("</a>", at) + len("</a>")
    else:
        start = text.rfind('<article class="v25-pillar-card">', 0, at)
        end = text.find("</article>", at) + len("</article>")
    if start < 0 or end <= at:
        raise RuntimeError(f"Hub card not found for cleanup: {href}")
    return text[:start] + text[end:]


def cleanup_rejected_draft() -> None:
    for lang in ("tc", "cn", "en"):
        rejected = ROOT / "articles/us" / f"{REJECTED_SLUG}{LANG_SUFFIX[lang]}.html"
        if rejected.exists():
            rejected.unlink()
    for relative_path in HUB_UPDATES:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        traditional = relative_path.endswith("index.html")
        suffix = "" if traditional else ("_cn" if relative_path.endswith("index_cn.html") else "_en")
        old_href = f"/articles/us/{REJECTED_SLUG}{suffix}.html"
        path.write_text(remove_hub_card(text, old_href, traditional), encoding="utf-8")
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    pattern = re.compile(
        r"\s*<url>\s*<loc>https://www\.jingwei-law\.com/articles/us/"
        + re.escape(REJECTED_SLUG)
        + r"(?:_cn|_en)?\.html</loc>.*?</url>",
        re.S,
    )
    sitemap.write_text(pattern.sub("", text), encoding="utf-8")


def write_article() -> None:
    target_dir = ROOT / ARTICLE["directory"]
    for lang in ("tc", "cn", "en"):
        target = target_dir / f"{ARTICLE['slug']}{LANG_SUFFIX[lang]}.html"
        target.write_text(render_article(ARTICLE, lang), encoding="utf-8")


def update_hubs() -> None:
    for relative_path, (href, card) in HUB_UPDATES.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        traditional = relative_path.endswith("index.html")
        marker = '<details class="v24-article-more"' if traditional else '<details class="v25-article-more"'
        if marker not in text:
            raise RuntimeError(f"Hub insertion marker missing: {relative_path}")
        text = remove_hub_card(text, href, traditional)
        path.write_text(text.replace(marker, card + marker, 1), encoding="utf-8")


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
    for lang in ("tc", "cn", "en"):
        url = SITE + article_path(ARTICLE, lang)
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
    for suffix in ("", "index_cn.html", "index_en.html"):
        text = update_lastmod(text, SITE + "/articles/united-states/" + suffix)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    cleanup_rejected_draft()
    write_article()
    update_hubs()
    update_sitemap()
