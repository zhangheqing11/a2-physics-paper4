from pathlib import Path
import re
p=Path('work/physics-audit')
for f in sorted(p.glob('9702_*_qp_4*.txt')):
 if f.stem.endswith('43'):continue
 t=f.read_text(); starts=list(re.finditer(r'^\s*(\d{1,2})\s+(?=\([a-z]\)|[A-Z][a-z])',t,re.M))
 for j,m in enumerate(starts):
  block=t[m.start():starts[j+1].start() if j+1<len(starts) else len(t)]
  if not re.search(r'circular|centripetal|angular speed|orbits|in a circle|radius of the orbit',block,re.I):continue
  q=m[1];ms=(p/f.name.replace('_qp_','_ms_')).read_text()
  lines=ms.splitlines(); keep=[];active=False
  for line in lines:
   k=re.match(r'^\s*(\d{1,2})\([a-z]\)',line)
   if k:active=k[1]==q
   if active and line.strip() and not re.search(r'PUBLISHED|©|Mark Scheme',line):keep.append(line.strip())
  print('\n###',f.stem,'Q'+q,'\n'+'\n'.join(keep))
