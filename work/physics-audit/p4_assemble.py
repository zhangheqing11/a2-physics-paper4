from pathlib import Path
import json,re,collections,csv
P=Path('work/physics-audit');O=Path('output/physics/p4-complete')
rows=json.loads((P/'p4_allrows.json').read_text()); groups=collections.defaultdict(list)
for r in rows:groups[(r['paper'][5:],r['q'].split('(')[0])].append(r)
for line in (P/'p4_mapping.txt').read_text().splitlines():
 a=line.split()
 if '_' in a[0]:paper=a[0];continue
 target=groups[(paper,a[0])];assert len(target)==len(a)-1,(paper,a[0],len(target),len(a)-1)
 for r,c in zip(target,a[1:]):r['types']=c.split('+')
for r in rows:
 if r['paper'].endswith('43'):
  src=next(x for x in rows if x['paper']==r['paper'][:-2]+'41' and x['q']==r['q'])
  assert re.sub(r'\s+','',src['answer'])==re.sub(r'\s+','',r['answer'])
  r['types']=src['types'];r['equivalent_ms']=src['paper']+':'+src['q']
 else:r['equivalent_ms']=''
 assert r.get('types') and r['marks']>0
assert len(rows)==1250 and sum(r['marks'] for r in rows)==2500
(P/'p4_mapped.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
inv={r['id']:r for r in json.loads((P/'inventory.json').read_text())}
qpblocks={}
for paper in sorted({r['paper'] for r in rows}):
 text=(P/(paper.replace('_4','_qp_4')+'.txt')).read_text()
 blocks={};cur=None;pg=None
 for line in text.splitlines():
  m=re.match(r'=== MERGED PAGE (\d+)',line)
  if m:pg=int(m[1])
  m=re.match(r'^ {0,40}(10|[1-9])\s+(?=[A-Z(])',line)
  if m and (int(m[1])==1 if cur is None else int(m[1])==int(cur)+1):
   cur=m[1];blocks[cur]={'page':pg,'text':[]}
  if cur:blocks[cur]['text'].append(line)
 assert set(blocks)==set(map(str,range(1,11))),(paper,blocks.keys())
 for q,b in blocks.items():
  b['text']='\n'.join(b['text'])
  b['marks']=sum(map(int,re.findall(r'\[(\d+)\]',b['text'])))
  expected=sum(r['marks'] for r in rows if r['paper']==paper and r['q'].split('(')[0]==q)
  assert b['marks']==expected,(paper,q,b['marks'],expected)
 qpblocks[paper]=blocks
 for r in [r for r in rows if r['paper']==paper]:r['qp_page']=blocks[r['q'].split('(')[0]]['page']
(P/'p4_qpblocks.json').write_text(json.dumps(qpblocks,ensure_ascii=False,indent=2))
(P/'p4_mapped.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
bytype=collections.defaultdict(list)
for r in rows:
 for t in r['types']:bytype[t].append(r)
if __name__=='__main__':
 for t,rs in sorted(bytype.items()):
  r=rs[0];print(t,len(rs),r['paper'][5:],r['q'],re.sub(r'\s+',' ',r['answer'])[:190])
