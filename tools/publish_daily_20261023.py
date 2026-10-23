"""Render the reviewed 20-story batch; publication is verified separately."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / 'content-drafts' / 'daily-20261023'
DATE = '2026-10-23'
BASE = 'https://www.jingwei-law.com'
LANGS = {'zh-Hant': '', 'zh-Hans': '_cn', 'en': '_en'}
FILES = ['property-seven.json', 'funds-seven.json', 'procedure-six.json']
OUT = ROOT / 'content-system' / 'daily-publication-log-20261023.json'
TOPICS = {
 'hk-mainland-property-inheritance': ('香港居民與內地房產繼承', '香港居民与内地房产继承', 'Mainland property inheritance for Hong Kong families'),
 'hong-kong-other-estate': ('香港家屬與內地遺產', '香港家属与内地遗产', 'Mainland estates for Hong Kong families'),
 'am': ('澳門家屬與內地遺產', '澳门家属与内地遗产', 'Mainland estates for Macau families'),
 'singapore': ('新加坡家屬與內地遺產', '新加坡家属与内地遗产', 'Mainland estates for Singapore families'),
 'us': ('美國家屬與內地遺產', '美国家属与内地遗产', 'Mainland estates for U.S. families'),
 'overseas-chinese': ('海外家屬與內地遺產', '海外家属与内地遗产', 'Mainland estates for families abroad'),
}

def esc(v: str) -> str:
    return html.escape(str(v), quote=True)

def url(story: dict, lang: str) -> str:
    return f'{BASE}/articles/{story["folder"]}/{story["slug"]}{LANGS[lang]}.html'

def target(value: str) -> Path:
    path = urlsplit(value).path
    return ROOT / path.lstrip('/') / ('index.html' if path.endswith('/') else '')

def brand(lang: str) -> str:
    return {'zh-Hant': '靜為律師', 'zh-Hans': '静为律师', 'en': 'Jingwei Law'}[lang]

def render(story: dict, lang: str) -> str:
    d = story['languages'][lang]
    title, lead = d['title'], d['lead']
    desc = d.get('description') or lead[:155]
    page_url = url(story, lang)
    topic = TOPICS[story['folder']][list(LANGS).index(lang)]
    topic_key = story['folder']
    if story['folder'] in {'am', 'us'}:
        topic_key = {'am': 'macau', 'us': 'united-states'}[story['folder']]
    topic_path = '/articles/' if story['folder'] == 'overseas-chinese' else f'/articles/{topic_key}/'
    topic_path = topic_path if lang == 'zh-Hant' else topic_path + f'index{LANGS[lang]}.html'
    ui = {
      'zh-Hant': {'library':'文章庫','date':'發布日期','read':'相關閱讀','scope':'深圳執業的中國內地律師團隊，處理涉及中國內地法律的事務。','label':'靜為律師 · 站內服務','ad':'先把內地資產、文件和家人情況整理清楚','adbody':'使用 AI 法律助手整理問題，再按具體材料判斷辦理安排。','action':'整理案情 →','note':'本文為一般資訊，不構成個案法律意見；具體材料要求以實際接收機構及適用程序為準。'},
      'zh-Hans': {'library':'文章库','date':'发布日期','read':'相关阅读','scope':'深圳执业的中国内地律师团队，处理涉及中国内地法律的事务。','label':'静为律师 · 站内服务','ad':'先把内地资产、文件和家人情况整理清楚','adbody':'使用 AI 法律助手整理问题，再按具体材料判断办理安排。','action':'整理案情 →','note':'本文为一般信息，不构成个案法律意见；具体材料要求以实际接收机构及适用程序为准。'},
      'en': {'library':'Articles','date':'Published','read':'Related reading','scope':'A Shenzhen-based PRC lawyer team handling Mainland China legal matters.','label':'Jingwei Law · Site service','ad':'Organise the Mainland assets, documents and family facts','adbody':'Use the AI legal assistant to prepare questions for a document-specific review.','action':'Organise your facts →','note':'General information only, not advice on an individual matter. Requirements depend on the receiving institution and applicable procedure.'},
    }[lang]
    sections = []
    for section in d['sections']:
        paragraphs = ''.join(f'<p>{esc(p)}</p>' for p in section.get('paragraphs', []))
        bullets = '<ul>' + ''.join(f'<li>{esc(p)}</li>' for p in section.get('bullets', [])) + '</ul>' if section.get('bullets') else ''
        sections.append(f'<section class="hk-section-card article-prose-section"><h2>{esc(section["heading"])}</h2>{paragraphs}{bullets}</section>')
    checklist = '<ul>' + ''.join(f'<li>{esc(x)}</li>' for x in d['checklist']) + '</ul>'
    related = ''.join(f'<p><a href="{esc(x["url"])}">{esc(x["label"][lang])}</a></p>' for x in story['related'])
    alternates = ''.join(f'<link rel="alternate" hreflang="{k}" href="{url(story,k)}">' for k in LANGS)
    language_nav = ''.join(f'<a href="{url(story,k)}" lang="{k}">{label}</a>' for k,label in [('zh-Hant','繁'),('zh-Hans','简'),('en','EN')])
    author = {'@type':'Organization','name':brand(lang),'url':BASE+'/'}
    schema = [
      {'@context':'https://schema.org','@type':'Article','headline':title,'description':desc,'datePublished':DATE,'dateModified':DATE,'inLanguage':lang,'mainEntityOfPage':page_url,'author':author,'publisher':author,'articleSection':topic,'image':[BASE+'/articles/article-library-desk-v26.jpg']},
      {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':ui['library'],'item':BASE+'/articles/'},{'@type':'ListItem','position':2,'name':title,'item':page_url}]},
    ]
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | {brand(lang)}</title><meta name="description" content="{esc(desc)}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{page_url}">{alternates}<link rel="alternate" hreflang="x-default" href="{url(story,'zh-Hant')}">
<meta property="og:type" content="article"><meta property="og:site_name" content="{brand(lang)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{page_url}"><meta property="og:image" content="{BASE}/articles/article-library-desk-v26.jpg"><meta property="article:published_time" content="{DATE}"><meta property="article:modified_time" content="{DATE}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{BASE}/articles/article-library-desk-v26.jpg">
<link rel="stylesheet" href="/articles/style.css?v=20261023"><script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@graph':schema},ensure_ascii=False)}</script>
<style>.article-detail.generated-article .brand::before{{content:"{'J' if lang=='en' else '静' if lang=='zh-Hans' else '靜'}"}}.article-detail .article-hero-inner,.article-detail .article-shell{{grid-template-columns:minmax(0,1fr);max-width:960px}}.article-detail .article-shell{{padding-top:36px}}.article-detail .article-prose-section:first-child h2{{margin-top:18px}}.daily-article-scope{{color:#64748b;font-size:14px}}.daily-article-checklist{{margin-top:24px}}.article-last-updated{{font-size:14px}}@media(max-width:600px){{.article-detail .nav{{flex-wrap:wrap;gap:10px}}.article-detail h1{{overflow-wrap:anywhere}}}}</style></head>
<body class="article-detail generated-article article-regional-inheritance"><header class="site-header"><nav class="nav" aria-label="Article navigation"><a class="brand" href="/articles/"><strong>{brand(lang)}</strong><span>{esc(ui['scope'])}</span></a><a href="{topic_path}">{esc(ui['library'])}</a><div class="article-lang-switch" aria-label="Language switch">{language_nav}</div></nav></header>
<main><section class="article-hero"><div class="article-hero-inner"><div class="article-hero-copy"><p class="eyebrow">{esc(topic)}</p><h1>{esc(title)}</h1><p class="article-lead">{esc(lead)}</p><p class="article-last-updated">{ui['date']}: <time datetime="{DATE}">{DATE}</time></p></div></div></section>
<div class="article-shell"><article class="article-main">{''.join(sections)}
<section class="hk-section-card daily-article-checklist"><h2>{esc(d['checklistTitle'])}</h2>{checklist}</section>
<a class="article-native-ad" href="/ask/gpt/?topic={topic_key}&amp;source=article-inline-ad-{story['slug']}"><span class="article-native-ad__media" aria-hidden="true"><img src="/articles/assets/ai-legal-assistant-native-ad-v2.webp" alt="" width="1536" height="1024" loading="lazy" decoding="async"></span><span class="article-native-ad__copy"><span class="article-native-ad__label">{ui['label']}</span><strong>{ui['ad']}</strong><span class="article-native-ad__description">{ui['adbody']}</span></span><span class="article-native-ad__action">{ui['action']}</span></a>
<section class="topic-article-directory compact-directory"><h2>{ui['read']}</h2>{related}</section><p class="article-source-note">{esc(ui['note'])}</p></article></div></main><footer class="site-footer"><div class="footer-inner">{esc(ui['scope'])}</div></footer><script src="/articles/script.js" defer></script></body></html>'''

def load() -> list[dict]:
    stories = []
    for filename in FILES:
        payload = json.loads((DRAFTS/filename).read_text(encoding='utf-8-sig'))
        stories.extend(payload if isinstance(payload,list) else payload['stories'])
    assert len(stories) == 20, f'Need 20 independent stories; found {len(stories)}'
    assert len({s['id'] for s in stories}) == 20
    assert len({(s['folder'],s['slug']) for s in stories}) == 20
    for s in stories:
        assert s['folder'] in TOPICS
        assert re.fullmatch('[a-z0-9-]+',s['slug'])
        assert '内地' in s['research']['query'] or '內地' in s['research']['query']
        if s['research']['method'] == 'in-app browser':
            assert {1,2}.issubset(set(s['research']['viewedPages'])), s['id']
        else:
            assert s['research']['viewedPages'] == [] and '未把 Google 第1、2页' in s['research']['notes'], s['id']
        assert any(x['type'] in {'competitor','industry','court_case'} for x in s['sources']), s['id']
        assert any(x['type']=='official' for x in s['sources']), s['id']
        assert len(s['related']) >= 2
        for link in s['related']:
            assert target(link['url']).is_file(), (s['id'],link['url'])
        for lang in LANGS:
            d=s['languages'][lang]
            assert len(d['sections']) >= 3 and len(d['checklist']) >= 4, (s['id'],lang)
            text = json.dumps(d,ensure_ascii=False)
            for bad in ['商标','商標','专利','專利','这是草稿','待补','同行文章','本团队曾','本團隊曾']:
                assert bad not in text,(s['id'],bad)
    return stories

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--render',action='store_true')
    args=parser.parse_args()
    stories=load()
    outputs=[]
    for s in stories:
        for lang in LANGS:
            public=url(s,lang)
            path=target(public)
            page=render(s,lang)
            if args.render:
                if path.exists() and 'source=article-inline-ad-'+s['slug'] not in path.read_text(encoding='utf-8'):
                    raise RuntimeError(f'Refusing to overwrite existing article: {path}')
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(page,encoding='utf-8')
            outputs.append({'storyId':s['id'],'lang':lang,'url':public,'path':path.relative_to(ROOT).as_posix(),'title':s['languages'][lang]['title'],'sha256':hashlib.sha256(page.encode()).hexdigest()})
    if args.render:
        by_topic={}
        for s in stories:
            folder={'am':'macau','us':'united-states'}.get(s['folder'],s['folder'])
            for lang in LANGS:
                by_topic.setdefault(('all',lang),[]).append(s)
                if folder!='overseas-chinese': by_topic.setdefault((folder,lang),[]).append(s)
        for (folder,lang),items in by_topic.items():
            path=ROOT/'articles'/('' if folder=='all' else folder)/f'index{LANGS[lang]}.html'
            if not path.exists(): raise RuntimeError(f'Missing topic index {path}')
            text=path.read_text(encoding='utf-8')
            batch_date=datetime.strptime(DATE,'%Y-%m-%d')
            heading=batch_date.strftime('Mainland inheritance · %d %B %Y').replace(' 0',' ') if lang=='en' else f'內地繼承 · {batch_date.year}年{batch_date.month}月{batch_date.day}日' if lang=='zh-Hant' else f'内地继承 · {batch_date.year}年{batch_date.month}月{batch_date.day}日'
            cards=''.join(f'<a href="{url(s,lang).replace(BASE,"")}"><strong>{esc(s["languages"][lang]["title"])}</strong><p>{esc(s["languages"][lang]["lead"][:100])}</p></a>' for s in items)
            batch_marker=DATE.replace('-','')
            start=f'<!-- DAILY_{batch_marker}_START -->'; end=f'<!-- DAILY_{batch_marker}_END -->'
            section=f'{start}<section class="topic-article-directory compact-directory"><h2>{heading}</h2><div class="topic-directory-grid">{cards}</div></section>{end}\n'
            if start in text:
                text=re.sub(re.escape(start)+'.*?'+re.escape(end),lambda _:section.rstrip(),text,flags=re.S)
            else:
                # Put today's links before older daily batches where possible.
                marker='<!-- DAILY_20261010_START -->' if '<!-- DAILY_20261010_START -->' in text else '</main>'
                assert marker in text,str(path)
                text=text.replace(marker,section+marker,1)
            path.write_text(text,encoding='utf-8')
        sitemap=ROOT/'sitemap.xml'
        text=sitemap.read_text(encoding='utf-8')
        have=set(re.findall('<loc>([^<]+)</loc>',text))
        extra=''.join(f'  <url><loc>{x["url"]}</loc><lastmod>{DATE}</lastmod><changefreq>monthly</changefreq><priority>0.60</priority></url>\n' for x in outputs if x['url'] not in have)
        sitemap.write_text(text.replace('</urlset>',extra+'</urlset>'),encoding='utf-8')
        OUT.write_text(json.dumps({'date':DATE,'targetStories':20,'preparedStories':20,'publishedStories':0,'status':'prepared-awaiting-deployment','indexing':'unknown','pages':outputs,'research':[{ 'storyId':s['id'],**s['research'],'sources':s['sources']} for s in stories]},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'stories':len(stories),'pages':len(outputs),'rendered':args.render},ensure_ascii=False))

if __name__=='__main__': main()
