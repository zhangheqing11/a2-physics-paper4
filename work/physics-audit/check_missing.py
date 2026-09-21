from pathlib import Path
import re,json
p=Path('work/physics-audit');rows=[]
for f in sorted(p.glob('*_qp_*_original.txt')):
 base=f.name.replace('_original','');orig=f.read_text().split('\f');merged=(p/base).read_text();normalized=re.sub(r'[^a-z0-9]','',merged.lower())
 findings=[]
 for i,t in enumerate(orig):
  if not t.strip():continue
  if 'BLANK PAGE' in t: findings.append(f'{i+1}:blank');continue
  sentences=[]
  for line in t.splitlines():
   s=re.sub(r'[^a-z0-9]','',line.lower())
   if len(s)>32 and not re.search(r'cambridge|ucles|writ|barcode|candidate|copyright',s):sentences.append(s)
  missing=[s for s in sentences if s not in normalized]
  if len(missing)>len(sentences)*.6 and len(missing)>=2: findings.append(f'{i+1}:text differs '+str(missing[:2]))
 rows.append({'paper':base[:-4],'page_review':findings})
print(json.dumps(rows,ensure_ascii=False,indent=2));(p/'missing_review.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
