"""Correct only the prematurely published D24 batch; preserve URLs and copy."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timedelta, timezone

ROOT = Path(__file__).resolve().parents[1]
OLD, ACTUAL = '2026-10-24', '2026-10-23'
MANIFEST = ROOT / 'content-system/daily-publication-log-20261024.json'

def apply():
    m = json.loads(MANIFEST.read_text(encoding='utf-8'))
    assert len(m['pages']) == 60 and len({p['storyId'] for p in m['pages']}) == 20
    for p in m['pages']:
        path = ROOT / p['path']
        assert p['path'].startswith(('articles/hk-mainland-property-inheritance/', 'articles/hong-kong-other-estate/'))
        text = path.read_text(encoding='utf-8')
        corrected = text.replace(OLD, ACTUAL)
        assert OLD not in corrected and '"datePublished": "2026-10-23"' in corrected
        path.write_text(corrected, encoding='utf-8')
        p['sha256'] = hashlib.sha256(corrected.encode()).hexdigest()
    # Retain the batch marker so this block stays distinct from the first 20.
    for folder in ['', 'hk-mainland-property-inheritance', 'hong-kong-other-estate']:
        for suffix in ['', '_cn', '_en']:
            path = ROOT / 'articles' / folder / f'index{suffix}.html'
            text = path.read_text(encoding='utf-8')
            pattern = r'<!-- DAILY_20261024_START -->.*?<!-- DAILY_20261024_END -->'
            assert len(re.findall(pattern, text, re.S)) == 1
            text = re.sub(pattern, lambda x: x[0].replace('2026年10月24日', '2026年10月23日').replace('24 October 2026', '23 October 2026'), text, flags=re.S)
            path.write_text(text, encoding='utf-8')
    path = ROOT / 'sitemap.xml'
    sitemap = path.read_text(encoding='utf-8')
    for p in m['pages']:
        pattern = r'(<url>\s*<loc>' + re.escape(p['url']) + r'</loc>\s*<lastmod>)[^<]+(</lastmod>)'
        sitemap, count = re.subn(pattern, lambda x: x[1] + ACTUAL + x[2], sitemap)
        assert count == 1, p['url']
    path.write_text(sitemap, encoding='utf-8')
    m.update(date=ACTUAL, originalBatchDate=OLD, additionalStoriesOnActualDate=20,
             dateCorrection='Retained URLs; corrected future date to actual first publication date.',
             dateCorrectedAt=datetime.now(timezone(timedelta(hours=8))).isoformat(),
             status='date-corrected-awaiting-deployment', publishedStories=20)
    MANIFEST.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding='utf-8')
    path = ROOT / 'content-system/keyword-database/daily-import-summary-20261024.json'
    summary = json.loads(path.read_text(encoding='utf-8'))
    summary.update(publicationDate=ACTUAL, originalBatchDate=OLD,
                   actualDateTotalStories=40, additionalStories=20)
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Corrected 60 pages, 9 indexes, sitemap and batch records; copy and URLs preserved.')

if __name__ == '__main__':
    apply()
