from pathlib import Path
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'work/physics-audit/p4_core.md'
OUT=ROOT/'output/physics/p4-web/P4核心概念与公式_中文优化版.pdf'
FONT='/System/Library/Fonts/STHeiti Medium.ttc'
pdfmetrics.registerFont(TTFont('Chinese',FONT,subfontIndex=0))

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='ZhTitle',parent=styles['Title'],fontName='Chinese',fontSize=21,leading=29,alignment=TA_CENTER,textColor=colors.HexColor('#145f73'),spaceAfter=12))
styles.add(ParagraphStyle(name='ZhH1',parent=styles['Heading1'],fontName='Chinese',fontSize=17,leading=24,textColor=colors.HexColor('#145f73'),spaceBefore=14,spaceAfter=8))
styles.add(ParagraphStyle(name='ZhH2',parent=styles['Heading2'],fontName='Chinese',fontSize=13.5,leading=20,textColor=colors.HexColor('#145f73'),spaceBefore=10,spaceAfter=5))
styles.add(ParagraphStyle(name='ZhBody',parent=styles['BodyText'],fontName='Chinese',fontSize=9.2,leading=15,spaceAfter=5,textColor=colors.HexColor('#19313a')))
styles.add(ParagraphStyle(name='ZhFormula',parent=styles['BodyText'],fontName='Chinese',fontSize=9.4,leading=15,leftIndent=8*mm,rightIndent=4*mm,borderColor=colors.HexColor('#d6e2e4'),borderWidth=.6,borderPadding=6,backColor=colors.HexColor('#f3f8f8'),spaceBefore=5,spaceAfter=5))
styles.add(ParagraphStyle(name='ZhGuide',parent=styles['BodyText'],fontName='Chinese',fontSize=8.7,leading=14,leftIndent=8*mm,rightIndent=4*mm,textColor=colors.HexColor('#145f73'),backColor=colors.HexColor('#edf5f6'),borderColor=colors.HexColor('#145f73'),borderWidth=1,borderPadding=5,spaceAfter=5))

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

story=[]
for raw in SRC.read_text().splitlines():
    line=raw.strip()
    if not line:
        story.append(Spacer(1,2)); continue
    if line.startswith('# '):
        story.append(Paragraph(esc(line[2:]),styles['ZhTitle'] if not story else styles['ZhH1'])); continue
    if line.startswith('## '):
        story.append(Paragraph(esc(line[3:]),styles['ZhH2'])); continue
    if line.startswith('@'):
        a=line.find('|'); b=line.rfind('|'); kind=line[1:a]; formula=line[a+1:b]; note=line[b+1:]
        story.append(Paragraph(f'<b>{esc(kind)}</b>　{esc(formula)}',styles['ZhFormula']))
        guide='推导顺序：基础关系 → 代入定义 → 化简，并检查单位、方向和适用条件。' if kind=='推导' else '阅读顺序：先识别现象 → 选择基础关系 → 检查方向、单位与适用条件。'
        story.append(Paragraph(guide,styles['ZhGuide']))
        story.append(Paragraph(esc(note),styles['ZhBody']))
    else:
        story.append(Paragraph(esc(line),styles['ZhBody']))

def footer(canvas,doc):
    canvas.saveState(); canvas.setFont('Chinese',7.5); canvas.setFillColor(colors.HexColor('#546972'))
    canvas.drawString(18*mm,10*mm,'CIE 9702 Paper 4 · 中文优化版')
    canvas.drawRightString(192*mm,10*mm,f'{doc.page}')
    canvas.restoreState()

OUT.parent.mkdir(parents=True,exist_ok=True)
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=17*mm,leftMargin=17*mm,topMargin=15*mm,bottomMargin=17*mm,title='P4核心概念与公式 中文优化版')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
