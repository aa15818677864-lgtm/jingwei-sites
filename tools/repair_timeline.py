"""Render the reviewed, language-specific timeline copy without changing site wiring."""
from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content-system/timeline-repair.json').read_text(encoding='utf-8'))
RELATED = ['different-institutions-different-files', 'hong-kong-and-mainland-workstreams', 'preserve-evidence-before-dispute']

def render():
    for lang, item in DATA.items():
        suffix = '' if lang == 'tc' else '_' + lang
        path = ROOT / f'articles/hong-kong-other-estate/timeline-milestones{suffix}.html'
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        for old in soup.find_all('style'):
            if '.article-detail .nav{flex-wrap:wrap' in old.get_text(): old.decompose()
        layout = soup.new_tag('style')
        layout.string = '.article-detail .nav{flex-wrap:wrap;gap:12px}.article-detail .nav>a{white-space:nowrap}.article-detail .nav .brand{flex:1 0 100%}.article-detail .nav .brand span{white-space:normal}.site-footer{padding:24px;line-height:1.7}'
        soup.head.append(layout)
        for selector in ['meta[name="description"]', 'meta[property="og:description"]', 'meta[name="twitter:description"]']:
            soup.select_one(selector)['content'] = item['description']
        schema = soup.select_one('script[type="application/ld+json"]')
        obj = json.loads(schema.string)
        obj.update(description=item['description'], dateModified='2026-09-11')
        schema.string = json.dumps(obj, ensure_ascii=False)
        soup.select_one('.article-lead').string = item['lead']
        date = soup.select_one('time')
        date['datetime'] = '2026-09-11'
        date.string = '2026-09-11'
        article = soup.select_one('article.article-main')
        ad = article.select_one('.article-native-ad').extract()
        ad['aria-label'] = 'Open AI legal assistant' if lang == 'en' else '打开 AI 法律助手'
        ad.select_one('strong').string = 'Ask the AI legal assistant' if lang == 'en' else ('向 AI 法律助手說明情況' if lang == 'tc' else '向 AI 法律助手说明情况')
        ad.select_one('.article-native-ad__description').string = 'Describe the asset, current stage and missing documents. Avoid sharing identity numbers.' if lang == 'en' else ('先說資產、辦理階段和缺件，不必提供證件號碼。' if lang == 'tc' else '先说资产、办理阶段和缺件，不必提供证件号码。')
        article.clear()
        for index, section in enumerate(item['sections']):
            tag = soup.new_tag('section', attrs={'class':'hk-section-card article-prose-section'})
            h = soup.new_tag('h2'); h.string = section[0]; tag.append(h)
            for text in section[1:]:
                p = soup.new_tag('p'); p.string = text; tag.append(p)
            article.append(tag)
            if index == 1:
                article.append(ad)
        related = soup.new_tag('section', attrs={'class':'topic-article-directory compact-directory'})
        h = soup.new_tag('h2'); h.string = 'Related reading' if lang == 'en' else ('相關文章' if lang == 'tc' else '相关文章'); related.append(h)
        for slug in RELATED:
            target = ROOT / f'articles/hong-kong-other-estate/{slug}{suffix}.html'
            target_soup = BeautifulSoup(target.read_text(encoding='utf-8'), 'html.parser')
            p = soup.new_tag('p'); a = soup.new_tag('a', href='/' + target.relative_to(ROOT).as_posix())
            a.string = target_soup.h1.get_text(' ',strip=True); p.append(a); related.append(p)
        article.append(related)
        # Add visible language navigation; keep the existing reciprocal hreflang metadata.
        nav = soup.select_one('header nav')
        for a in nav.find_all('a'):
            if '/timeline-milestones' in a.get('href',''): a.decompose()
        for code, label in [('tc','繁體'),('cn','简体'),('en','English')]:
            other = '' if code == 'tc' else '_' + code
            a = soup.new_tag('a', href=f'/articles/hong-kong-other-estate/timeline-milestones{other}.html')
            a.string = label; nav.append(a)
        path.write_text(str(soup), encoding='utf-8')

if __name__ == '__main__':
    render()
