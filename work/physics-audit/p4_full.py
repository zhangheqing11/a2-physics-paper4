from pathlib import Path
import re,json,collections
P=Path('work/physics-audit');OUT=Path('output/physics/p4-complete');OUT.mkdir(exist_ok=True)
inv={x['id']:x for x in json.loads((P/'inventory.json').read_text())}
allrows=[]
for f in sorted(P.glob('9702_*_ms_4*.txt')):
 paper=f.stem.replace('_ms',''); rows={};cur=None;page=0
 for line in f.read_text().splitlines():
  pg=re.match(r'=== MERGED PAGE (\d+)',line)
  if pg:page=int(pg[1]);continue
  m=re.match(r'^\s*(\d+\s*\([a-z]\)(?:\s*\([ivx]+\))?)(?:\s+.*)?$',line)
  if m:
   cur=re.sub(r'\s','',m[1]); rows.setdefault(cur,{'paper':paper,'q':cur,'page':page,'lines':[],'markcodes':[]})
  if cur and line.strip() and not re.search(r'©|PUBLISHED|Mark Scheme|^\s*Question\s+Answer',line):
   rows[cur]['lines'].append(line.strip())
   mark=re.search(r'\s([BCMA]\d+)\s*$',line)
   if mark: rows[cur]['markcodes'].append(mark[1])
 for r in rows.values():
  r['marks']=sum(int(x[1:]) for x in r['markcodes']);r['answer']=' '.join(r.pop('lines')); allrows.append(r)
 print(paper,len(rows),sum(r['marks'] for r in rows.values()))
(P/'p4_allrows.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2))
for group in ['s22','w22','s23','w23','m24','s24','w24','s25','w25']:
 selected=[r for r in allrows if group in r['paper'] and not r['paper'].endswith('43')]
 (P/f'read_{group}.txt').write_text('\n'.join(f"{r['paper']} {r['q']} [{r['marks']}] {r['answer']}" for r in selected))
