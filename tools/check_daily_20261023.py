"""Validate only this batch, and optionally verify the deployed bytes."""
from __future__ import annotations
import argparse,concurrent.futures,hashlib,json,re,time,urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
from publish_daily_20261023 import ROOT,OUT,BASE,DATE,LANGS,load,url,target

class Tags(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]
    def handle_starttag(self,tag,attrs): self.tags.append((tag,dict(attrs)))

def validate():
    stories=load(); manifest=json.loads(OUT.read_text(encoding='utf-8'))
    assert len(manifest['pages'])==60
    sitemap={e.text for e in ET.parse(ROOT/'sitemap.xml').iter() if e.tag.endswith('}loc')}
    titles=set(); descriptions=set(); links=set()
    for item in manifest['pages']:
        path=ROOT/item['path']; text=path.read_text(encoding='utf-8'); p=Tags();p.feed(text)
        assert hashlib.sha256(text.encode()).hexdigest()==item['sha256'],item['path']
        title=re.search(r'<title>(.*?)</title>',text,re.S).group(1);assert title not in titles; titles.add(title)
        metas={a.get('name',a.get('property')):a.get('content') for t,a in p.tags if t=='meta'}
        desc=metas['description']; assert desc and desc not in descriptions; descriptions.add(desc)
        assert metas['og:url']==item['url'] and metas['og:type']=='article'
        assert metas['twitter:card']=='summary_large_image'
        assert 'noindex' not in metas['robots']
        assert [(a.get('href')) for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[item['url']]
        hreflang={a.get('hreflang'):a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='alternate'}
        story=next(s for s in stories if s['id']==item['storyId'])
        for lang in LANGS: assert hreflang[lang]==url(story,lang)
        assert hreflang['x-default']==url(story,'zh-Hant')
        blocks=re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S)
        graph=json.loads(blocks[0])['@graph'];article=next(s for s in graph if s['@type']=='Article')
        assert article['headline']==item['title'] and article['datePublished']==DATE
        assert text.count('class="article-native-ad"')==1
        assert len([1 for t,a in p.tags if t=='h1'])==1
        assert len([1 for t,a in p.tags if t=='h2'])>=5
        assert item['url'] in sitemap
        for t,a in p.tags:
            for key in ('href','src'):
                v=a.get(key,''); parts=urlsplit(v)
                if not v or v.startswith('#') or parts.scheme in ('tel','mailto','data'):continue
                if parts.netloc and parts.netloc!='www.jingwei-law.com':continue
                if not parts.path:continue
                resolved=target(v) if parts.path.startswith('/') else path.parent/unquote(parts.path)
                if resolved.is_dir(): resolved=resolved/'index.html'
                assert resolved.is_file(),(item['path'],v)
                links.add(BASE+parts.path)
    baseline=json.loads((ROOT/'content-system/daily-baseline-20261023.json').read_text())
    for rel,digest in baseline['protected'].items(): assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,rel
    return manifest,sorted(links)

def fetch(v):
    address,expected=v
    try:
        req=urllib.request.Request(address,headers={'User-Agent':'Jingwei-Publication-Verification/1.0','Cache-Control':'no-cache'})
        with urllib.request.urlopen(req,timeout=35) as r:
            body=r.read(); status=r.status; final=r.url
        digest=hashlib.sha256(body).hexdigest()
        return {'url':address,'status':status,'finalUrl':final,'sha256':digest,'matchesExpected':digest==expected if expected else True,'bytes':len(body)}
    except Exception as e:return {'url':address,'status':None,'matchesExpected':False,'error':str(e)}

def main():
    args=argparse.ArgumentParser(); args.add_argument('--live',action='store_true'); opts=args.parse_args()
    m,links=validate(); result={'date':DATE,'local':{'stories':20,'pages':60,'linksAndAssets':len(links),'protectedFilesUnchanged':True,'passed':True}}
    if opts.live:
        expected={p['url']:p['sha256'] for p in m['pages']}
        work=[(address,expected.get(address)) for address in sorted(set(links)|set(expected))]
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: live=list(pool.map(fetch,work))
        result['live']=live; result['livePassed']=all(x['status']==200 and x['matchesExpected'] for x in live)
        result['verifiedAt']=time.strftime('%Y-%m-%dT%H:%M:%S%z')
        output=ROOT/'content-system'/'daily-live-check-20261023.json';output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
        if result['livePassed']:
            m.update(status='published-verified',publishedStories=20,publishedPages=60,verifiedAt=result['verifiedAt'])
            OUT.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
        print(json.dumps({'local':result['local'],'liveChecked':len(live),'livePassed':result['livePassed'],'failures':[x for x in live if x['status']!=200 or not x['matchesExpected']]},ensure_ascii=True))
        if not result['livePassed']:raise SystemExit(1)
    else: print(json.dumps(result,ensure_ascii=True))

if __name__=='__main__':main()
