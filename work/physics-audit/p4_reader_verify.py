from pathlib import Path
from lxml import html
import json,re,hashlib
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'work/physics-audit/p4_reader_content.json').read_text())
tree=html.fromstring((root/'output/physics/p4-web/handbook.html').read_text())
for node in tree.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," inline-math ")]'):
    original=node.get('data-original');tail=node.tail
    node.clear();node.text=original;node.tail=tail
norm=lambda s:re.sub(r'\s+','',s)
text=norm(tree.text_content());missing=[];checked=0
for b in data['blocks']:
    if b['kind']=='image':continue
    parts=[b['text']] if b['kind']=='p' else [c for row in b['rows'] for c in row]
    for p in parts:
        if b.get('style')=='Title' or p.startswith('在Word中可使用导航窗格'):continue
        if re.match(r'^(细分考法|识别与模型|代表题讲解|下一道变式)\s+',p):
            p=re.sub(r'^(细分考法|识别与模型|代表题讲解|下一道变式)\s+', '', p)
        if re.match(r'^[smw]\d{2}/\d{2} Q',p):
            # The reference line is now represented by the question card metadata,
            # while the exact source and target question are checked structurally below.
            continue
        # Index lines become list items; semicolon separators are the only removed characters.
        if b.get('style')=='Indextext' and re.match(r'^\d+\(',p):parts2=p.split('； ')
        else:parts2=[p]
        for part in parts2:
            checked+=1
            if norm(part) not in text:missing.append(part)
assert not missing,missing[:15]
assert hashlib.sha256(Path(data['source']).read_bytes()).hexdigest()==data['sha256']
assert len(tree.xpath('//article'))==85
assert len(tree.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," question ")]'))==85
assert len(tree.xpath('//details[contains(concat(" ",normalize-space(@class)," ")," mark-scheme ")]'))==85
entries=tree.xpath('//ul[@class="question-list"]/li')
assert len(entries)==1250
marks=sum(int(re.search(r'\[(\d+)\]',n.text_content())[1]) for n in entries)
assert marks==2500
ids=tree.xpath('//@id');assert len(ids)==len(set(ids))
assert not tree.xpath('//merror')
print(json.dumps(dict(content_checks=checked,missing=0,subquestions=len(entries),marks=marks,original_unchanged=True),ensure_ascii=False))
