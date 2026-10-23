"""Add the Oct 24 article batch and its honest research status to the SEO database."""
from __future__ import annotations
import csv,json,re,sqlite3
from pathlib import Path
from urllib.parse import urlsplit
import publish_daily_20261024 as batch

ROOT=batch.ROOT
DB_DIR=ROOT/'content-system'/'keyword-database'
DB_PATH=DB_DIR/'seo_keyword_research.sqlite'
PUBLICATION_DATE='2026-10-24'
RESEARCH_DATE='2026-10-23'
CATEGORY_BY_PREFIX={'D24-P':'property-inheritance','D24-F':'funds-and-personal-estate','D24-R':'inheritance-procedure'}
REGION='HK'

def normalize(value):
    return ' '.join(value.strip().lower().split())

def infer_intent(text):
    for label,words in [
      ('document_checklist',['文件','資料','证明','證明','证件','證件','checklist','document']),
      ('procedural',['手续','手續','怎么办','怎樣','如何','流程','process','how']),
      ('remote_authorisation',['委托','委託','授权','授權','远程','遠程','power of attorney','appoint']),
      ('asset_lookup',['查找','查','账户','賬戶','银行','銀行','房产','房產','asset','bank']),
      ('dispute_response',['争议','爭議','纠纷','糾紛','不配合','失联','失聯','dispute','court']),
      ('cost_timing',['费用','費用','时间','時間','周期','週期','cost','timeline']),
      ('identity_language',['姓名','名字','身份','身分','翻译','翻譯','name mismatch'])]:
        if any(word.lower() in text.lower() for word in words): return label
    return 'general_information'

def infer_funnel(text):
    if any(word in text.lower() for word in ['律师','律師','委托','委託','费用','費用','咨询','諮詢','lawyer','appoint']): return 'decision'
    if any(word in text.lower() for word in ['怎么办','怎樣','如何','需要','手续','手續','資料','文件','how','process']): return 'evaluation'
    return 'awareness'

def infer_query_shape(text):
    words=re.findall(r'[A-Za-z0-9]+',text)
    chinese=len(re.findall(r'[\u4e00-\u9fff]',text))
    size=len(words)+chinese/2
    return 'head_or_mid' if size<=8 else 'mid_tail' if size<=16 else 'long_tail'

def export(conn,table,filename=None):
    cur=conn.execute(f'SELECT * FROM {table}')
    with (DB_DIR/(filename or table.replace('_','-')+'.csv')).open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f);writer.writerow([x[0] for x in cur.description]);writer.writerows(cur)

def group_file(story_id):
    return 'property-seven.json' if story_id.startswith('D24-P') else 'funds-seven.json' if story_id.startswith('D24-F') else 'procedure-six.json'

def main():
    stories=batch.publisher.load()
    log=json.loads(batch.publisher.OUT.read_text(encoding='utf-8'))
    status='published' if log.get('status')=='published-verified' else 'prepared'
    conn=sqlite3.connect(DB_PATH);conn.execute('PRAGMA foreign_keys=ON')
    conn.executescript('''
      CREATE TABLE IF NOT EXISTS daily_story_research(
        story_id TEXT PRIMARY KEY,research_date TEXT NOT NULL,keyword_id INTEGER NOT NULL,
        category TEXT NOT NULL,audience TEXT NOT NULL,method TEXT NOT NULL,
        viewed_pages TEXT NOT NULL,search_url TEXT NOT NULL,sources_json TEXT NOT NULL,
        notes TEXT NOT NULL,article_url TEXT NOT NULL,publication_status TEXT NOT NULL,
        live_verified_at TEXT,source_file TEXT NOT NULL);
      CREATE VIEW IF NOT EXISTS daily_category_volume_summary AS
      SELECT d.research_date,d.category,COUNT(DISTINCT d.keyword_id) AS keyword_count,
        COUNT(DISTINCT CASE WHEN v.status='observed' AND v.is_market_volume=1 THEN d.keyword_id END) AS keywords_with_observed_volume,
        SUM(CASE WHEN v.status='observed' AND v.is_market_volume=1 THEN v.value ELSE NULL END) AS observed_market_volume
      FROM daily_story_research d LEFT JOIN volume_observations v ON d.keyword_id=v.keyword_id
      GROUP BY d.research_date,d.category;
    ''')
    conn.execute('''INSERT OR IGNORE INTO platforms VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',(
      'public_web_search','公开网页搜索（非 Google SERP）','竞品/行业来源发现，不用于排名判断',90,'HK','zh-Hans',0,0,0,1,0,None,
      '用于定位法律文章、行业办理资料与官方来源；不能证明 Google 排名、前两页覆盖或搜索量。'))
    conn.execute('INSERT OR REPLACE INTO database_meta VALUES(?,?)',('last_daily_research_import',RESEARCH_DATE))
    conn.execute('INSERT OR REPLACE INTO database_meta VALUES(?,?)',('last_daily_publication_batch',PUBLICATION_DATE))
    source_counts={}
    for s in stories:
        q=s['research']['query'];category=CATEGORY_BY_PREFIX[s['id'][:5]]
        norm=normalize(q)
        found=conn.execute('SELECT keyword_id FROM keywords WHERE normalized_keyword=?',(norm,)).fetchone()
        keyword_status='source-collected-google-unverified'
        if found:
            kid=found[0]
            conn.execute('UPDATE keywords SET existing_url=?,status=? WHERE keyword_id=?',(batch.publisher.url(s,'zh-Hant'),keyword_status,kid))
        else:
            cur=conn.execute('''INSERT INTO keywords(keyword_text,normalized_keyword,language,market,topic,cluster,intent,funnel_stage,query_shape,seed_source,existing_url,status,created_at)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',(q,norm,'zh-Hans',REGION,'mainland-inheritance',category,infer_intent(q),infer_funnel(q),infer_query_shape(q),'daily-web-search-fallback',batch.publisher.url(s,'zh-Hant'),keyword_status,RESEARCH_DATE))
            kid=cur.lastrowid
        source_file='content-drafts/daily-20261024/'+group_file(s['id'])
        conn.execute('INSERT OR REPLACE INTO keyword_sources VALUES(?,?,?,?)',(kid,'daily-article-source-research',s['id'],source_file))
        conn.execute('INSERT OR IGNORE INTO keyword_categories VALUES(?,?,?,?,?)',(category,'business-content',category,'Mainland China inheritance and estate content for Hong Kong families','Track exact search volume only from a dated, geographic, source-backed measurement; never infer volume from SERP presence.'))
        conn.execute('INSERT OR REPLACE INTO article_index VALUES(?,?,?,?,?,?,?,?,?,?)',(s['id'],REGION,'mainland-inheritance',category,s['slug'],s['languages']['zh-Hant']['title'],status,batch.publisher.url(s,'zh-Hant'),3,source_file))
        conn.execute('''INSERT OR REPLACE INTO daily_story_research VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(
          s['id'],RESEARCH_DATE,kid,category,REGION,s['research']['method'],json.dumps(s['research']['viewedPages']),s['research']['searchUrl'],
          json.dumps(s['sources'],ensure_ascii=False),s['research']['notes'],batch.publisher.url(s,'zh-Hant'),status,log.get('verifiedAt'),source_file))
        source_type=s['sources'][0]['type'];source_counts[source_type]=source_counts.get(source_type,0)+1
        conn.execute("DELETE FROM competitor_observations WHERE keyword_id=? AND observed_at=? AND source_method='public web search fallback; 20261024 batch'",(kid,RESEARCH_DATE))
        if source_type=='competitor':
            source=s['sources'][0]
            conn.execute('''INSERT INTO competitor_observations(keyword_id,platform_id,rank,title,url,domain,content_type,observed_at,search_locale,gap_notes,status,source_method)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',(kid,'public_web_search',None,source['title'],source['url'],urlsplit(source['url']).netloc,'legal-article',RESEARCH_DATE,
              'Google locale and result position not verified',source.get('notes',''),'source-recorded-ranking-unverified','public web search fallback; 20261024 batch'))
        for task_type,platform,task_status,required,notes,depth,completed in [
          ('legal-source-discovery','public_web_search','completed','Find a relevant legal or industry source and an authoritative Mainland reference; record exact URLs and source type.',
           'Source discovery completed outside the Google results page. No SERP position or first-two-page coverage is claimed.',None,RESEARCH_DATE),
          ('google-serp-first-two-pages','google_search','blocked-verification','Inspect the first two organic result pages, record competitor URLs and content gaps; never click ads.',
           'Google CAPTCHA appeared again. Pages 1 and 2 were not verified; retry only through a normal browser session.',2,None)
        ]:
            exists=conn.execute('SELECT task_id FROM daily_search_tasks WHERE search_date=? AND keyword_id=? AND task_type=?',(RESEARCH_DATE,kid,task_type)).fetchone()
            if exists:
                conn.execute('''UPDATE daily_search_tasks SET query=?,platform_id=?,market=?,language=?,result_depth=?,status=?,required_evidence=?,completed_at=?,notes=? WHERE task_id=?''',
                  (q,platform,REGION,'zh-Hans',depth,task_status,required,completed,notes,exists[0]))
            else:
                conn.execute('''INSERT INTO daily_search_tasks(search_date,keyword_id,query,platform_id,task_type,market,language,result_depth,status,required_evidence,completed_at,notes)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',(RESEARCH_DATE,kid,q,platform,task_type,REGION,'zh-Hans',depth,task_status,required,completed,notes))
        if not conn.execute("SELECT 1 FROM volume_observations WHERE keyword_id=? AND platform_id='google_ads_keyword_planner'",(kid,)).fetchone():
            conn.execute('''INSERT INTO volume_observations(keyword_id,platform_id,metric,value,unit,status,period_label,observed_at,geo,language,network,confidence,is_market_volume,notes)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(kid,'google_ads_keyword_planner','avg_monthly_searches',None,'searches/month','pending',None,RESEARCH_DATE,REGION,'zh-Hans','Google','unknown',1,'No Keyword Planner measurement collected; value intentionally left NULL.'))
    conn.execute('UPDATE daily_search_tasks SET status=\'cancelled-outside-service-scope\' WHERE status=\'planned\' AND keyword_id IN (SELECT keyword_id FROM keywords WHERE keyword_text LIKE \'%商标%\' OR keyword_text LIKE \'%商標%\' OR keyword_text LIKE \'%专利%\' OR keyword_text LIKE \'%專利%\')')
    conn.commit()
    tables=['keywords','keyword_variants','platforms','keyword_categories','keyword_sources','daily_search_tasks','article_index','competitor_observations','volume_observations','daily_story_research','daily_category_volume_summary','business_category_volume_summary']
    for table in tables:
        try: export(conn,table,{'daily_search_tasks':'daily-search-tasks.csv','keyword_sources':'keyword-sources.csv','keyword_categories':'keyword-categories.csv','daily_category_volume_summary':'daily-category-volume-summary.csv','business_category_volume_summary':'business-category-volume-summary.csv'}.get(table))
        except sqlite3.OperationalError: pass
    counts={t:conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0] for t in ['keywords','keyword_variants','article_index','competitor_observations','daily_search_tasks','daily_story_research']}
    summary={'publicationDate':PUBLICATION_DATE,'researchDate':RESEARCH_DATE,'dailyStories':len(stories),'dailyPublished':20 if status=='published' else 0,
      'sourceTypeCounts':source_counts,'googleFirstTwoPagesVerified':0,'googleTasksBlockedByVerification':20,'measuredSearchVolumes':0,
      'counts':counts,'monthlySearchVolume':'Not measured; pending values are NULL.','rankings':'Source URLs are recorded as fallback research only; all rank values remain NULL.'}
    (DB_DIR/'daily-import-summary-20261024.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    (DB_DIR/'database-summary.json').write_text(json.dumps({'generated_at':RESEARCH_DATE,'database':str(DB_PATH),**summary},ensure_ascii=False,indent=2),encoding='utf-8')
    conn.close()
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
