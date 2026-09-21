from pathlib import Path
import re
import tempfile

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[2]
CURRENT = ROOT / 'output/physics/p4-web/a2physics_中文版_原图对照译本.pdf'
SOURCE = Path('/Users/zhangheqing/Desktop/a2 physics/a2physics.pdf')
OUT = ROOT / 'output/physics/p4-web/a2physics_中文版_易读排版版.pdf'

BODY_FONT = '/System/Library/Fonts/STHeiti Light.ttc'
HEAD_FONT = '/System/Library/Fonts/STHeiti Medium.ttc'
pdfmetrics.registerFont(TTFont('A2Body', BODY_FONT, subfontIndex=0))
pdfmetrics.registerFont(TTFont('A2Head', HEAD_FONT, subfontIndex=0))

PAGE_W, PAGE_H = A4
LEFT = 18 * mm
RIGHT = 18 * mm
TOP = 29 * mm
BOTTOM = 17 * mm
TEXT_W = PAGE_W - LEFT - RIGHT


def is_cjk(ch):
    return '\u2e80' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf'


def clean_translation(text, page_no):
    lines = []
    for raw in (text or '').splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('中文译文'):
            continue
        if line.startswith('对应原文第'):
            continue
        # The original extraction sometimes leaves the source page number alone.
        if re.fullmatch(r'\d{1,4}', line):
            continue
        lines.append(line)
    if not lines:
        return '本页没有可提取的正文；请结合前一页保留的原图阅读。'
    text = ' '.join(lines)
    # The supplied PDF uses an embedded symbol font whose extracted text maps
    # several mathematical glyphs to private/incorrect characters. Normalize
    # those glyphs for the readable text layer; the facing source page remains
    # untouched and preserves the original typeset equations.
    text = text.translate(str.maketrans({
        'Æ': '=',
        '¡': '−',
        'Å': '+',
        '£': '×',
        '\x00': 'ε',
        'µ': '(',
        '¶': ')',
    }))
    # Remove artificial spaces inserted between adjacent Chinese characters while
    # retaining spaces that separate Latin text, variables, and equations.
    text = re.sub(r'(?<=[\u2e80-\u9fff\u3400-\u4dbf])\s+(?=[\u2e80-\u9fff\u3400-\u4dbf])', '', text)
    return text


def tokens(text):
    out = []
    buf = ''
    for ch in text:
        if is_cjk(ch):
            if buf:
                out.append(buf)
                buf = ''
            out.append(ch)
        elif ch.isspace():
            if buf:
                out.append(buf)
                buf = ''
            out.append(' ')
        else:
            buf += ch
    if buf:
        out.append(buf)
    return out


def wrap_lines(text, font_name, font_size, width):
    result = []
    line = ''
    for token in tokens(text):
        candidate = line + token
        if line and pdfmetrics.stringWidth(candidate, font_name, font_size) > width:
            result.append(line.rstrip())
            line = token.lstrip()
        else:
            line = candidate
    if line.strip():
        result.append(line.rstrip())
    return result


def old_syllabus_topic(page_no):
    if 199 <= page_no <= 219:
        return 'Chapter 15 Electronics'
    if 220 <= page_no <= 237:
        return 'Chapter 16 Telecommunication'
    return None


def draw_header(c, page_no, continuation=False):
    c.setFillColorRGB(0.08, 0.18, 0.22)
    c.setFont('A2Head', 15)
    suffix = '（续）' if continuation else ''
    c.drawString(LEFT, PAGE_H - 16 * mm, f'中文译文 · 第 {page_no} 页{suffix}')
    c.setStrokeColorRGB(0.76, 0.82, 0.82)
    c.setLineWidth(0.7)
    c.line(LEFT, PAGE_H - 21 * mm, PAGE_W - RIGHT, PAGE_H - 21 * mm)
    topic = old_syllabus_topic(page_no)
    if topic:
        c.setFillColorRGB(1.0, 0.95, 0.84)
        c.roundRect(LEFT, PAGE_H - 34 * mm, TEXT_W, 9 * mm, 2.2 * mm, fill=1, stroke=0)
        c.setFillColorRGB(0.48, 0.25, 0.04)
        c.setFont('A2Head', 8.2)
        c.drawString(
            LEFT + 3 * mm,
            PAGE_H - 28.5 * mm,
            f'考纲提示 · {topic}：旧版拓展内容；2022 起不再属于 9702 A Level，当前 Paper 4 不考。',
        )
        return PAGE_H - 40 * mm
    return PAGE_H - TOP


def draw_footer(c, page_no):
    c.setFillColorRGB(0.30, 0.38, 0.40)
    c.setFont('A2Body', 7.5)
    c.drawString(LEFT, 9 * mm, f'对应原文第 {page_no} 页 · 原图页在前')


def make_translation_pages(source_reader, current_reader, temp_path):
    c = canvas.Canvas(str(temp_path), pagesize=A4, pageCompression=1)
    c.setTitle('A2 Physics 中文版·易读排版对照译本')
    generated = 0
    for i in range(len(source_reader.pages)):
        page_no = i + 1
        text = clean_translation(current_reader.pages[2 * i + 1].extract_text() or '', page_no)
        remaining = text
        first = True
        while remaining:
            y = draw_header(c, page_no, continuation=not first)
            c.setFillColorRGB(0.10, 0.17, 0.20)
            c.setFont('A2Body', 10.5)
            lines = wrap_lines(remaining, 'A2Body', 10.5, TEXT_W)
            usable = max(1, int((y - BOTTOM - 5 * mm) / (17 * 1)))
            part = lines[:usable]
            for line in part:
                c.drawString(LEFT, y, line)
                y -= 17
            remaining = ''.join(lines[usable:]).lstrip()
            draw_footer(c, page_no)
            c.showPage()
            generated += 1
            first = False
            if not part:
                break
    c.save()
    return generated


def main():
    source_reader = PdfReader(str(SOURCE))
    current_reader = PdfReader(str(CURRENT))
    if len(current_reader.pages) < 2 * len(source_reader.pages):
        raise RuntimeError('当前译本页数不足，无法安全重排。')
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
        temp_path = Path(tmp.name)
    try:
        translation_count = make_translation_pages(source_reader, current_reader, temp_path)
        translation_reader = PdfReader(str(temp_path))
        writer = PdfWriter()
        if translation_count != len(source_reader.pages):
            raise RuntimeError(f'本次排版产生了 {translation_count} 个译页，预期为 {len(source_reader.pages)} 个。')
        for i, source_page in enumerate(source_reader.pages):
            # Keep the source PDF page as vector content, scaled to A4 without
            # rasterizing diagrams or labels.
            source_page.scale_to(PAGE_W, PAGE_H)
            writer.add_page(source_page)
            # The current corpus fits one readable translation page per source
            # page; keep the pairing deterministic and auditable.
            writer.add_page(translation_reader.pages[i])
        writer.add_metadata({
            '/Title': 'A2 Physics 中文版·易读排版对照译本',
            '/Subject': '原图与中文译文对照阅读版',
            '/Creator': 'Codex',
        })
        with OUT.open('wb') as f:
            writer.write(f)
        print(f'{OUT}\nsource_pages={len(source_reader.pages)} translation_pages={translation_count} final_pages={len(writer.pages)}')
    finally:
        temp_path.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
