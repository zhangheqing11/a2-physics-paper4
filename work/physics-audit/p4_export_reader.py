"""Read-only extraction of the final handbook; retain exact paragraph/table order."""
from pathlib import Path
import json, base64, hashlib
from docx import Document
from docx.oxml.ns import qn

root = Path(__file__).resolve().parents[2]
source = root / 'output/physics/p4-complete/CIE9702_P4_学习与题型全册_2022至2025.docx'
doc = Document(source)
blocks = []
for child in doc.element.body:
    if child.tag == qn('w:p'):
        text = ''.join(n.text or '' for n in child.iter(qn('w:t')))
        style = child.find('w:pPr/w:pStyle', child.nsmap)
        if text:
            blocks.append(dict(kind='p', text=text, style=style.get(qn('w:val')) if style is not None else 'Normal'))
        for pic in child.iter(qn('a:blip')):
            part = doc.part.related_parts[pic.get(qn('r:embed'))]
            blocks.append(dict(kind='image', data='data:'+part.content_type+';base64,'+base64.b64encode(part.blob).decode()))
    elif child.tag == qn('w:tbl'):
        rows = []
        for row in child.findall(qn('w:tr')):
            rows.append([''.join(n.text or '' for n in cell.iter(qn('w:t'))) for cell in row.findall(qn('w:tc'))])
        blocks.append(dict(kind='table', rows=rows))
data = dict(source=str(source), sha256=hashlib.sha256(source.read_bytes()).hexdigest(), blocks=blocks)
(root/'work/physics-audit/p4_reader_content.json').write_text(json.dumps(data, ensure_ascii=False))
print(json.dumps(dict(blocks=len(blocks), images=sum(b['kind']=='image' for b in blocks), sha256=data['sha256'])))
