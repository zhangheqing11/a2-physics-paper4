from pathlib import Path
import io, re, time
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import pypdf
import pypdfium2 as pdfium
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parents[2]
SRC=Path('/Users/zhangheqing/Desktop/a2 physics/a2physics.pdf')
OUT=ROOT/'output/physics/p4-web/a2physics_中文版_原图对照译本.pdf'
FONT='/System/Library/Fonts/STHeiti Medium.ttc'
pdfmetrics.registerFont(TTFont('Chinese',FONT,subfontIndex=0))

def translate(text):
    text=re.sub(r'\s+',' ',text).strip()
    if not text:return '（本页无可提取正文；请参考上一页保留的原图。）'
    chunks=[]; cur=''
    for sent in re.split(r'(?<=[.!?])\s+',text):
        if len(cur)+len(sent)>3600:
            if cur: chunks.append(cur); cur=''
        cur+=((' ' if cur else '')+sent)
    if cur:chunks.append(cur)
    out=[]
    for chunk in chunks:
        query=urlencode({'client':'gtx','sl':'en','tl':'zh-CN','dt':'t','q':chunk})
        last=None
        for attempt in range(5):
            try:
                req=Request('https://translate.google.com/translate_a/single?'+query,
                            headers={'User-Agent':'Mozilla/5.0'})
                with urlopen(req,timeout=45) as response:
                    out.append(''.join(x[0] for x in json.loads(response.read().decode('utf-8'))[0]))
                last=None
                break
            except Exception as exc:
                last=exc
                time.sleep(1.5*(attempt+1))
        if last is not None:
            raise last
        time.sleep(.35)
    return '\n'.join(out)

def wrap(c,text,x,y,width,font=9,leading=14):
    c.setFont('Chinese',font); maxchars=max(18,int(width/(font*.95)))
    for para in text.splitlines():
        words=list(para) if any('\u4e00'<=ch<='\u9fff' for ch in para) else para.split(' '); line=''
        for word in words:
            sep='' if any('\u4e00'<=ch<='\u9fff' for ch in para) else (' ' if line else '')
            if len(line)+len(sep)+len(word)>maxchars:
                c.drawString(x,y,line); y-=leading; line=word
            else: line+=sep+word
        if line:c.drawString(x,y,line); y-=leading
        y-=3
        if y<18*mm:c.showPage(); c.setFont('Chinese',font); y=277*mm
    return y

reader=pypdf.PdfReader(str(SRC)); doc=pdfium.PdfDocument(str(SRC)); c=canvas.Canvas(str(OUT),pagesize=A4)
for i,page in enumerate(reader.pages):
    rendered=doc[i].render(scale=1.8); pil=rendered.to_pil().convert('RGB'); bio=io.BytesIO(); pil.save(bio,format='JPEG',quality=88); bio.seek(0)
    iw,ih=pil.size; scale=min(190*mm/iw,277*mm/ih); c.setFillColorRGB(1,1,1); c.rect(0,0,210*mm,297*mm,fill=1,stroke=0)
    c.drawImage(ImageReader(bio),(210*mm-iw*scale)/2,15*mm,width=iw*scale,height=ih*scale,preserveAspectRatio=True,anchor='c'); c.setFont('Chinese',7); c.setFillColorRGB(.3,.38,.4); c.drawString(17*mm,8*mm,f'原文第 {i+1} 页 / Original page {i+1}'); c.showPage()
    c.setFillColorRGB(.08,.18,.22); c.setFont('Chinese',15); c.drawString(17*mm,280*mm,f'中文译文 · 第 {i+1} 页'); c.setStrokeColorRGB(.75,.82,.82); c.line(17*mm,276*mm,193*mm,276*mm)
    try: tr=translate(page.extract_text() or '')
    except Exception as e: tr='（本页自动翻译失败，请参考原图；错误：'+str(e)[:120]+'）'
    wrap(c,tr,17*mm,268*mm,176*mm,font=8.5,leading=12); c.setFont('Chinese',7); c.setFillColorRGB(.3,.38,.4); c.drawString(17*mm,8*mm,f'对应原文第 {i+1} 页 · 保留原图在前一页'); c.showPage()
    if (i+1)%10==0: print(f'{i+1}/{len(reader.pages)}',flush=True)
c.save(); print(OUT)
