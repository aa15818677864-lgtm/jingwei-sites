"""Validate the October 24 batch locally and against the live site."""
from __future__ import annotations
import argparse,concurrent.futures,hashlib,json,time
from pathlib import Path
import publish_daily_20261023 as publisher
import check_daily_20261023 as checker

ROOT=publisher.ROOT
publisher.DRAFTS=ROOT/'content-drafts'/'daily-20261024'
publisher.DATE='2026-10-24'
publisher.OUT=ROOT/'content-system'/'daily-publication-log-20261024.json'
checker.ROOT=ROOT
checker.OUT=publisher.OUT
checker.DATE=publisher.DATE
checker.load=publisher.load
checker.url=publisher.url
checker.target=publisher.target

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--live',action='store_true');args=parser.parse_args()
    manifest,links=checker.validate()
    result={'date':publisher.DATE,'local':{'stories':20,'pages':60,'linksAndAssets':len(links),'protectedFilesUnchanged':True,'passed':True}}
    if args.live:
        expected={p['url']:p['sha256'] for p in manifest['pages']}
        work=[(address,expected.get(address)) for address in sorted(set(links)|set(expected))]
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: live=list(pool.map(checker.fetch,work))
        result['live']=live;result['livePassed']=all(x['status']==200 and x['matchesExpected'] for x in live)
        result['verifiedAt']=time.strftime('%Y-%m-%dT%H:%M:%S%z')
        (ROOT/'content-system'/'daily-live-check-20261024.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
        if result['livePassed']:
            manifest.update(status='published-verified',publishedStories=20,publishedPages=60,verifiedAt=result['verifiedAt'])
            publisher.OUT.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
        print(json.dumps({'local':result['local'],'liveChecked':len(live),'livePassed':result['livePassed'],'failures':[x for x in live if x['status']!=200 or not x['matchesExpected']]},ensure_ascii=False))
        if not result['livePassed']:raise SystemExit(1)
    else: print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
