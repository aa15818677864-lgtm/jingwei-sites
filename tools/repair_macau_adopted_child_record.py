"""Render a reviewed repair for the Macau adopted-child high-value estate guide."""
from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "content-system/macau-adopted-child-record-repair.json").read_text(encoding="utf-8"))
RELATED = ["macau-heir-qualification-deed", "macau-company-share-certificate", "macau-client-mainland-lawyer"]


def set_meta(soup, selector, value):
    tag = soup.select_one(selector)
    if tag:
        tag["content"] = value


def render():
    for lang, item in DATA.items():
        suffix = "" if lang == "tc" else "_" + lang
        path = ROOT / f"articles/am/macau-adopted-child-record{suffix}.html"
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        title = item["title"] + " | 静为律师"
        soup.title.string = title
        set_meta(soup, "meta[name='description']", item["description"])
        set_meta(soup, "meta[property='og:description']", item["description"])
        set_meta(soup, "meta[name='twitter:description']", item["description"])
        set_meta(soup, "meta[property='og:title']", title)
        set_meta(soup, "meta[name='twitter:title']", title)
        schema = soup.select_one("script[type='application/ld+json']")
        if schema and schema.string:
            obj = json.loads(schema.string)
            obj.update(headline=item["title"], description=item["description"], dateModified="2026-09-14")
            schema.string = json.dumps(obj, ensure_ascii=False)
        soup.h1.string = item["title"]
        soup.select_one(".article-lead").string = item["lead"]
        date = soup.select_one("time")
        date["datetime"] = "2026-09-14"
        date.string = "2026-09-14"

        article = soup.select_one("article.article-main")
        ad = article.select_one(".article-native-ad").extract()
        ad["href"] = "/ask/gpt/?topic=macau&source=article-inline-ad-macau-adopted-child-record"
        ad["aria-label"] = "Open AI legal assistant" if lang == "en" else "打开 AI 法律助手"
        ad.select_one("strong").string = item["ad"][0]
        ad.select_one(".article-native-ad__description").string = item["ad"][1]
        article.clear()
        for index, section in enumerate(item["sections"]):
            css = "answer-card" if index == 0 else "hk-section-card article-prose-section"
            block = soup.new_tag("section", attrs={"class": css})
            heading = soup.new_tag("h2")
            heading.string = section[0]
            block.append(heading)
            for paragraph in section[1:]:
                p = soup.new_tag("p")
                p.string = paragraph
                block.append(p)
            article.append(block)
            if index == 1:
                article.append(ad)

        related = soup.new_tag("section", attrs={"class": "topic-article-directory compact-directory"})
        heading = soup.new_tag("h2")
        heading.string = "Related reading" if lang == "en" else ("相關文章" if lang == "tc" else "相关文章")
        related.append(heading)
        for slug in RELATED:
            target = ROOT / f"articles/am/{slug}{suffix}.html"
            target_soup = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
            p = soup.new_tag("p")
            link = soup.new_tag("a", href="/" + target.relative_to(ROOT).as_posix())
            link.string = target_soup.h1.get_text(" ", strip=True)
            p.append(link)
            related.append(p)
        article.append(related)
        rendered = str(soup)
        # Keep the native-ad class first so the repository's exact markup audit
        # recognises this single, otherwise unchanged ad slot.
        rendered = re.sub(
            r'<a aria-label="([^"]*)" class="article-native-ad" href="([^"]*)">',
            r'<a class="article-native-ad" href="\2" aria-label="\1">',
            rendered,
            count=1,
        )
        path.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    render()
