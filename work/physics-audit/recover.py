from pathlib import Path
import re,subprocess,concurrent.futures,json,hashlib
p=Path('work/physics-audit');out=Path('output/physics/补充原卷');out.mkdir(exist_ok=True)
pop='/Users/zhangheqing/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin/pdftotext'
jobs=[]
for f in p.glob('9702_*_qp_*.txt'):
 t=f.read_text();m=re.search(r'This document has (\d+) pages',t)
 if m and t.count('=== MERGED PAGE')!=int(m[1]):jobs.append((f,int(m[1])))
def run(job):
 f,n=job;year='20'+f.stem.split('_')[1][1:];url=f'https://bestexamhelp.com/exam/cambridge-international-a-level/physics-9702/{year}/{f.stem}.pdf';dest=out/(f.stem+'.pdf')
 r=subprocess.run(['curl','-fLsS','--retry','2','--max-time','45',url,'-o',str(dest)],capture_output=True)
 if r.returncode:return {'paper':f.stem,'error':r.stderr.decode()}
 subprocess.run([pop,'-layout',str(dest),str(p/(f.stem+'_original.txt'))],check=True,capture_output=True)
 pages=(p/(f.stem+'_original.txt')).read_text().split('\f');pages=pages[:-1] if not pages[-1].strip() else pages
 merged=f.read_text(); omitted=[]
 for i,page in enumerate(pages):
  # Blank pages and identifying header/footer removed for text matching.
  lines=[re.sub(r'\s+',' ',x).strip() for x in page.splitlines() if len(x.strip())>28 and not re.search(r'©|9702/|\.\.{4}|DO NOT WRITE|Cambridge|\*',x)]
  evidence=[x for x in lines if re.search('[A-Za-z]{4}',x)]
  normalized=re.sub(r'\s+',' ',merged)
  found=sum(x in normalized for x in evidence)
  if evidence and found==0:omitted.append({'printed_page':i+1,'evidence':evidence[:3]})
 return {'paper':f.stem,'declared_pages':n,'original_pages':len(pages),'merged_pages':merged.count('=== MERGED PAGE'),'suspected_missing':omitted,'source':url,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(run,jobs))
(p/'recovery.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print(json.dumps(rows,ensure_ascii=False,indent=2))
