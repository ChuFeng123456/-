# -*- coding: utf-8 -*-
"""Shared helpers to build consistent, professional Chinese DOCX files."""

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor, Inches

BODY_FONT = "微软雅黑"
MONO_HINT = "Consolas"
BLACK = RGBColor(0x00, 0x00, 0x00)
GRAY = RGBColor(0x59, 0x59, 0x59)
LIGHT_GRAY = RGBColor(0x80, 0x80, 0x80)
HEADER_FILL = "1F3864"
ALT_FILL = "F2F6FC"
BORDER = "D9D9D9"


def _set_run_font(run, name=BODY_FONT, size=10.5, bold=False, italic=False, color=BLACK):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia"):
        rFonts.set(qn(attr), name)


def new_document(margins_cm=2.0):
    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(margins_cm)
    section.bottom_margin = Cm(margins_cm)
    section.left_margin = Cm(2.2)
    section.right_margin = Cm(2.2)
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(10.5)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    return doc


def _fmt_paragraph(p, align=None, before=0, after=6, line=1.38):
    pf = p.paragraph_format
    if align is not None:
        pf.alignment = align
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    return p


def title(doc, text, subtitle=None):
    p = doc.add_paragraph(style="Title")
    _fmt_paragraph(p, align=WD_ALIGN_PARAGRAPH.LEFT, before=0, after=4, line=1.15)
    r = p.add_run(text)
    _set_run_font(r, size=22, bold=True)
    if subtitle:
        ps = doc.add_paragraph()
        _fmt_paragraph(ps, align=WD_ALIGN_PARAGRAPH.LEFT, before=0, after=12, line=1.3)
        rs = ps.add_run(subtitle)
        _set_run_font(rs, size=11, bold=False, color=GRAY)
    return p


def heading(doc, text, level=1):
    p = doc.add_paragraph(style=f"Heading {level}")
    _fmt_paragraph(p, before=10 if level == 1 else 8, after=4, line=1.2)
    r = p.add_run(text)
    _set_run_font(r, size={1: 15, 2: 12.5, 3: 11.5}[level], bold=True)
    return p


def para(doc, text, size=10.5, bold=False, align=None, after=6, before=0, color=BLACK, italic=False):
    p = doc.add_paragraph()
    _fmt_paragraph(p, align=align, before=before, after=after)
    r = p.add_run(text)
    _set_run_font(r, size=size, bold=bold, italic=italic, color=color)
    return p


def lead_para(doc, label, text, size=10.5):
    p = doc.add_paragraph()
    _fmt_paragraph(p, after=4)
    r1 = p.add_run(label)
    _set_run_font(r1, size=size, bold=True)
    r2 = p.add_run(text)
    _set_run_font(r2, size=size)
    return p


def bullets(doc, items, size=10.5, style="List Bullet"):
    for it in items:
        p = doc.add_paragraph(style=style)
        _fmt_paragraph(p, after=3, line=1.32)
        r = p.add_run(it)
        _set_run_font(r, size=size)
    return doc


def numbered(doc, items, size=10.5):
    for it in items:
        p = doc.add_paragraph(style="List Number")
        _fmt_paragraph(p, after=3, line=1.32)
        r = p.add_run(it)
        _set_run_font(r, size=size)
    return doc


def _shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def _set_table_borders_and_margins(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), BORDER)
        borders.append(el)
    tblPr.append(borders)
    mar = OxmlElement("w:tblCellMar")
    for side, w in (("top", "70"), ("left", "110"), ("bottom", "70"), ("right", "110")):
        m = OxmlElement(f"w:{side}")
        m.set(qn("w:w"), w)
        m.set(qn("w:type"), "dxa")
        mar.append(m)
    tblPr.append(mar)


def _write_cell(cell, text, size=9.5, bold=False, color=BLACK, align=None, valign=WD_CELL_VERTICAL_ALIGNMENT.CENTER):
    cell.vertical_alignment = valign
    p = cell.paragraphs[0]
    _fmt_paragraph(p, align=align, after=0, before=0, line=1.22)
    for i, chunk in enumerate(text.split("\n")):
        if i > 0:
            p.add_run().add_break()
        r = p.add_run(chunk)
        _set_run_font(r, size=size, bold=bold, color=color)


def table(doc, headers, rows, widths_cm=None, size=9.5, header_fill=HEADER_FILL, align_first_left=True):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.autofit = False
    t.alignment = 1  # center table on page
    _set_table_borders_and_margins(t)
    for j, htext in enumerate(headers):
        cell = t.rows[0].cells[j]
        _shade(cell, header_fill)
        _write_cell(cell, htext, size=size, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
                    align=WD_ALIGN_PARAGRAPH.CENTER)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = t.rows[i + 1].cells[j]
            if i % 2 == 1:
                _shade(cell, ALT_FILL)
            is_narrative = len(str(val)) > 18
            a = WD_ALIGN_PARAGRAPH.LEFT if (j == 0 and align_first_left) or is_narrative else WD_ALIGN_PARAGRAPH.LEFT
            _write_cell(cell, str(val), size=size, align=a)
    if widths_cm:
        for j, w in enumerate(widths_cm):
            for row in t.rows:
                row.cells[j].width = Cm(w)
    return t


def _field(run, instr):
    fld1 = OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = instr
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1)
    run._r.append(instr_text)
    run._r.append(fld2)


def add_footer_page_numbers(doc, prefix="第 ", suffix=" 页"):
    footer = doc.sections[0].footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if prefix:
        r0 = p.add_run(prefix)
        _set_run_font(r0, size=8.5, color=LIGHT_GRAY)
    r1 = p.add_run()
    _set_run_font(r1, size=8.5, color=LIGHT_GRAY)
    _field(r1, "PAGE")
    if suffix:
        r2 = p.add_run(suffix)
        _set_run_font(r2, size=8.5, color=LIGHT_GRAY)
    return footer


def source_note(doc, lines):
    for ln in lines:
        p = doc.add_paragraph()
        _fmt_paragraph(p, after=2, line=1.25)
        r = p.add_run(ln)
        _set_run_font(r, size=8.5, color=GRAY)
    return doc


def save(doc, path):
    doc.save(path)
    return path
