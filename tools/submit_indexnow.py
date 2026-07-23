from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
HOST = "www.jingwei-law.com"
SITE = f"https://{HOST}"
KEY = "57a8db48b2dd474284fe5961dda07ef0"
KEY_LOCATION = f"{SITE}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP = ROOT / "sitemap.xml"


def sitemap_urls(prefix: str | None, lastmod: str | None) -> list[str]:
    tree = ET.parse(SITEMAP)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    rows = []
    for item in tree.findall("sm:url", namespace):
        url = (item.findtext("sm:loc", default="", namespaces=namespace) or "").strip()
        modified = (item.findtext("sm:lastmod", default="", namespaces=namespace) or "").strip()
        path = urlparse(url).path
        if not url.startswith(SITE):
            continue
        if prefix and not path.startswith(prefix):
            continue
        if lastmod and modified != lastmod:
            continue
        rows.append(url)
    return sorted(set(rows))


def submit(urls: list[str]) -> int:
    if not urls:
        print("No URLs matched the submission filters")
        return 0
    payload = json.dumps(
        {"host": HOST, "key": KEY, "keyLocation": KEY_LOCATION, "urlList": urls},
        separators=(",", ":"),
    ).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "LiuYiArticleOps/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            print(f"IndexNow HTTP {response.status}; submitted {len(urls)} URLs")
            return 0 if response.status in {200, 202} else 1
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        print(f"IndexNow HTTP {error.code}; {body or error.reason}")
        return 1
    except urllib.error.URLError as error:
        print(f"IndexNow request failed: {error.reason}")
        return 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Submit verified sitemap URLs to IndexNow")
    parser.add_argument("--prefix", help="Only include URL paths beginning with this value")
    parser.add_argument("--lastmod", help="Only include sitemap entries with this YYYY-MM-DD lastmod")
    parser.add_argument("--dry-run", action="store_true", help="Print the payload without sending it")
    args = parser.parse_args()
    urls = sitemap_urls(args.prefix, args.lastmod)
    if args.dry_run:
        print(json.dumps({"host": HOST, "keyLocation": KEY_LOCATION, "count": len(urls), "urlList": urls}, ensure_ascii=False, indent=2))
        return
    raise SystemExit(submit(urls))


if __name__ == "__main__":
    main()
