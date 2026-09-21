from pathlib import Path
from pypdf import PdfReader
import re,json,csv,hashlib
root=Path.cwd(); out=root/'work/physics-audit'; rows=[]
for kind,name in [('qp','（已压缩）9702_ALL_QuestionPapers_merged.pdf'),('ms','9702_all_ms_merged.pdf')]:
    pages=(out/(kind+'.txt')).read_text().split('\f'); groups=[]; current=None
    if not pages[-1].strip():pages.pop()
    for idx,t in enumerate(pages):
        if ('PHYSICS' in t and ('Cambridge International' in t or 'Cambridge Assessment' in t) and (('READ THESE' in t or 'INSTRUCTIONS' in t) if kind=='qp' else 'MARK SCHEME' in t)):
            comp=re.search(r'9702/([45]\d)',t)
            year=re.search(r'(?:May/June|October/November|February/March)\s+(20\d\d)',t)
            if comp and year:
                season='s' if 'May/June' in year[0] else 'w' if 'October' in year[0] else 'm'
                current={'id':f'9702_{season}{year[1][2:]}_{kind}_{comp[1]}','kind':kind,'year':year[1],'season':season,'component':comp[1],'start':idx+1,'pages':[]}
                groups.append(current)
        if current: current['pages'].append((idx+1,t))
    for g in groups:
        text='\n'.join(f'\n=== MERGED PAGE {n} ===\n{t}' for n,t in g.pop('pages'))
        (out/(g['id']+'.txt')).write_text(text)
        g['end']=int(re.findall(r'=== MERGED PAGE (\d+)',text)[-1]);g['file']=name
        rows.append(g)
    print(kind,'pages',len(pages),'papers',len(groups))
with (out/'inventory.json').open('w') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
with (root/'output/physics/试卷总账.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for r in rows: print(r['id'],r['start'],r['end'])
