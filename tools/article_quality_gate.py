"""Fail closed on stub/duplicate article bodies. A 200 response is not a quality pass.

Run: python tools/article_quality_gate.py [--json report.json]
Requires beautifulsoup4. This check deliberately reports existing debt too.
"""
from collections import defaultdict
from pathlib import Path
import argparse
import hashlib
import json
import re
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]

def audit(root=ROOT):
    pages = []
    for path in sorted((root / 'articles').rglob('*.html')):
        raw = path.read_text(encoding='utf-8')
        soup = BeautifulSoup(raw, 'html.parser')
        if not soup.h1 or not re.search(r'"@type"\s*:\s*"(?:Article|BlogPosting)"', raw):
            continue
        body = soup.select_one('article.article-main') or soup.find('article') or soup.find('main')
        if not body:
            continue
        has_ai = any('/ask/' in a.get('href','') for a in soup.find_all('a'))
        for tag in body.select('.article-native-ad,.topic-article-directory,.compact-directory,.cta-panel,script,style,nav,header,footer'):
            tag.decompose()
        paragraphs = list(dict.fromkeys(p.get_text(' ', strip=True) for p in body.select('p,li') if p.get_text(' ', strip=True)))
        text = '\n'.join(paragraphs)
        rel = path.relative_to(root).as_posix()
        pages.append({'path':rel, 'story':re.sub(r'_(?:tc|cn|en)$','',rel[:-5]), 'hash':hashlib.sha256(text.encode()).hexdigest(), 'paragraphs':len(paragraphs), 'missing_ai':not has_ai, 'title':soup.h1.get_text(' ',strip=True)})
    groups = defaultdict(list)
    for p in pages: groups[p['hash']].append(p)
    for p in pages:
        p['duplicate_stories'] = len({x['story'] for x in groups[p['hash']]})
        p['fail'] = p['paragraphs'] <= 2 or p['duplicate_stories'] >= 3 or p['missing_ai']
    bad = [p for p in pages if p['fail']]
    return {'total_pages':len(pages), 'failed_pages':len(bad), 'failed_stories':len({p['story'] for p in bad}), 'failures':bad}

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--json');args=parser.parse_args()
    result=audit()
    if args.json: Path(args.json).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='failures'},ensure_ascii=False))
    raise SystemExit(1 if result['failed_pages'] else 0)
