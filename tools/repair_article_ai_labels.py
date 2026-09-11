"""Mechanical label correction only; never claims to repair substantive bodies."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

def repair():
    changed=[]
    for path in sorted((ROOT/'articles').rglob('*.html')):
        raw=path.read_text(encoding='utf-8')
        # Divorce-related content requires separate, current user confirmation.
        title=re.search(r'<title>(.*?)</title>',raw,re.S)
        if re.search(r'divorce|離婚|离婚',path.name+' '+(title.group(1) if title else ''),re.I):
            continue
        if 'article-native-ad' not in raw: continue
        lang=re.search(r'<html[^>]*lang=[\"\x27]([^\"\x27]+)',raw)
        code=lang.group(1).lower() if lang else ''
        label='Ask the AI legal assistant' if code.startswith('en') else ('向 AI 法律助手說明情況' if code in ('zh-hant','zh-tw','zh-hk') else '向 AI 法律助手说明情况')
        def patch(m):
            ad=m.group()
            heading=re.search(r'<strong\b[^>]*>(.*?)</strong>',ad,re.S)
            if not heading or re.search(r'AI|人工智能',heading.group(1),re.I):return ad
            return ad[:heading.start(1)]+label+ad[heading.end(1):]
        new=re.sub(r'<a\b[^>]*class=[\"\x27][^\"\x27]*\barticle-native-ad\b[^\"\x27]*[\"\x27][^>]*>.*?</a>',patch,raw,flags=re.S)
        if new!=raw:path.write_text(new,encoding='utf-8');changed.append(path.relative_to(ROOT).as_posix())
    print(f'AI labels clarified on {len(changed)} pages; body quality unchanged.')

if __name__=='__main__':repair()
