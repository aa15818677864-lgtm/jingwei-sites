"""Render a reviewed, non-divorce repair for the Macau company-share article."""
from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "content-system/macau-company-share-certificate-repair.json").read_text(encoding="utf-8"))
RELATED = ["macau-heir-qualification-deed", "macau-client-mainland-lawyer", "signing-in-macau"]


def render():
    for lang, item in DATA.items():
        suffix = "" if lang == "tc" else "_" + lang
        path = ROOT / f"articles/am/macau-company-share-certificate{suffix}.html"
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

        for selector in ["meta[name='description']", "meta[property='og:description']", "meta[name='twitter:description']"]:
            tag = soup.select_one(selector)
            if tag:
                tag["content"] = item["description"]
        schema = soup.select_one("script[type='application/ld+json']")
        if schema:
            obj = json.loads(schema.string)
            obj.update(description=item["description"], dateModified="2026-09-13")
            schema.string = json.dumps(obj, ensure_ascii=False)
        soup.select_one(".article-lead").string = item["lead"]
        date = soup.select_one("time")
        date["datetime"] = "2026-09-13"
        date.string = "2026-09-13"

        article = soup.select_one("article.article-main")
        ad = article.select_one(".article-native-ad").extract()
        ad["aria-label"] = "Open AI legal assistant" if lang == "en" else "打开 AI 法律助手"
        ad.select_one("strong").string = item["ad"][0]
        ad.select_one(".article-native-ad__description").string = item["ad"][1]
        article.clear()
        for index, section in enumerate(item["sections"]):
            block = soup.new_tag("section", attrs={"class": "hk-section-card article-prose-section"})
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

        nav = soup.select_one("header nav")
        for link in nav.find_all("a"):
            if "/macau-company-share-certificate" in link.get("href", ""):
                link.decompose()
        for code, label in [("tc", "繁體"), ("cn", "简体"), ("en", "English")]:
            other = "" if code == "tc" else "_" + code
            link = soup.new_tag("a", href=f"/articles/am/macau-company-share-certificate{other}.html")
            link.string = label
            nav.append(link)
        path.write_text(str(soup), encoding="utf-8")


if __name__ == "__main__":
    render()
