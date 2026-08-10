#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Line, Path as DrawPath, String
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MD = ROOT / "output" / "pdf" / "mri_full_course_formula_sheet.md"
DEFAULT_PDF = ROOT / "output" / "pdf" / "mri_full_course_formula_sheet.pdf"
RED = "#B00020"
FONT_PATHS = [
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def find_font() -> str:
    for path in FONT_PATHS:
        if Path(path).exists():
            return path
    raise FileNotFoundError("Could not find Arial/Unicode-compatible TTF font.")


def html_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def markdown_formula_to_reportlab(text: str) -> str:
    text = html_escape(text)
    text = text.replace(f'&lt;font color="{RED}"&gt;', f'<font color="{RED}">')
    text = text.replace("&lt;/font&gt;", "</font>")
    for tag in ("sub", "sup"):
        text = text.replace(f"&lt;{tag}&gt;", f"<{tag}>")
        text = text.replace(f"&lt;/{tag}&gt;", f"</{tag}>")
    text = re.sub(r"\^(-?\d+|[A-Za-z])", r"<sup>\1</sup>", text)
    text = re.sub(r"_([A-Za-z]+|\d+[A-Za-z]?)", r"<sub>\1</sub>", text)
    return text


def sequence_figure(kind: str, width: float) -> Drawing:
    height = 40
    drawing = Drawing(width, height)
    ink = colors.HexColor("#17292E")
    accent = colors.HexColor(RED)
    muted = colors.HexColor("#5B6668")

    def text(x, y, value, size=5.2, color=muted):
        drawing.add(String(x, y, value, fontName="SheetRegular", fontSize=size, fillColor=color))

    def axis(y, label):
        drawing.add(Line(14, y, width - 8, y, strokeColor=ink, strokeWidth=0.55))
        drawing.add(Line(width - 12, y + 2, width - 8, y, strokeColor=ink, strokeWidth=0.55))
        drawing.add(Line(width - 12, y - 2, width - 8, y, strokeColor=ink, strokeWidth=0.55))
        text(1, y - 2, label, 5.0, ink)

    def pulse(x, y, label, tall=18):
        drawing.add(Line(x, y, x, y + tall, strokeColor=accent, strokeWidth=1.2))
        drawing.add(Line(x - 3, y, x + 3, y, strokeColor=accent, strokeWidth=1.2))
        text(x - 5, y + tall + 2, label, 5.0, accent)

    def bracket(x1, x2, y, label):
        drawing.add(Line(x1, y, x2, y, strokeColor=accent, strokeWidth=0.55))
        drawing.add(Line(x1, y - 2, x1, y + 2, strokeColor=accent, strokeWidth=0.55))
        drawing.add(Line(x2, y - 2, x2, y + 2, strokeColor=accent, strokeWidth=0.55))
        text((x1 + x2) / 2 - 5, y + 2.5, label, 5.0, accent)

    if kind == "gre":
        axis(30, "RF")
        pulse(34, 30, "α", 10)
        pulse(width * 0.54, 30, "α", 10)
        bracket(34, width * 0.54, 37, "TR")
        axis(15, "Mz")
        recovery = DrawPath()
        recovery.moveTo(34, 8)
        recovery.curveTo(width * 0.30, 11, width * 0.40, 16, width * 0.54, 20)
        recovery.lineTo(width * 0.54, 8)
        recovery.curveTo(width * 0.70, 11, width * 0.82, 16, width - 18, 20)
        recovery.strokeColor = accent
        recovery.strokeWidth = 1.1
        recovery.fillColor = None
        drawing.add(recovery)
        axis(3, "Mxy")
        drawing.add(Line(34, 12, width * 0.38, 3, strokeColor=accent, strokeWidth=1.1))
        drawing.add(Line(width * 0.54, 12, width * 0.80, 3, strokeColor=accent, strokeWidth=1.1))
    elif kind == "se":
        axis(30, "RF")
        pulse(28, 30, "90°", 9)
        pulse(width * 0.42, 30, "180°", 17)
        bracket(28, width * 0.42, 37, "TE/2")
        bracket(width * 0.42, width * 0.72, 37, "TE/2")
        axis(17, "Mxy")
        drawing.add(Line(28, 26, width * 0.42, 17, strokeColor=accent, strokeWidth=1.1))
        drawing.add(Line(width * 0.42, 17, width * 0.72, 25, strokeColor=accent, strokeWidth=1.1))
        drawing.add(Line(width * 0.72, 25, width - 16, 17, strokeColor=accent, strokeWidth=1.1))
        text(width * 0.70, 27, "echo", 5.0, accent)
        axis(4, "Mz")
        drawing.add(Line(16, 12, 28, 12, strokeColor=accent, strokeWidth=1.1))
        drawing.add(Line(28, 12, width * 0.42, 6, strokeColor=accent, strokeWidth=1.1))
        drawing.add(Line(width * 0.42, 6, width - 16, 12, strokeColor=accent, strokeWidth=1.1))
    elif kind == "ernst":
        axis(30, "RF")
        pulse(24, 30, "α", 8)
        pulse(width * 0.35, 30, "α", 8)
        pulse(width * 0.56, 30, "α", 8)
        pulse(width * 0.77, 30, "α", 8)
        axis(14, "Mz")
        for x in (24, width * 0.35, width * 0.56, width * 0.77):
            drawing.add(Line(x - 16, 21, x, 18, strokeColor=accent, strokeWidth=1.1))
            drawing.add(Line(x, 18, x, 8, strokeColor=accent, strokeWidth=1.1))
            drawing.add(Line(x, 8, x + 26, 17, strokeColor=accent, strokeWidth=1.1))
        text(width * 0.58, 20, "MSS repeats before RF", 5.0, accent)
    return drawing


def parse_markdown(md_path: Path):
    lectures = []
    current_lecture = None
    current_section = None

    for raw_line in md_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            current_lecture = {"title": line[3:].strip(), "sections": []}
            lectures.append(current_lecture)
            current_section = None
        elif line.startswith("### ") and current_lecture is not None:
            current_section = {"title": line[4:].strip(), "rows": []}
            current_lecture["sections"].append(current_section)
        elif line.startswith("- **") and current_section is not None:
            match = re.match(r"- \*\*(.+?):\*\* (.*)$", line)
            if match:
                label, rest = match.groups()
                if " - " in rest:
                    formula, note = rest.rsplit(" - ", 1)
                else:
                    formula, note = rest, ""
                current_section["rows"].append((label, formula, note or ""))

    return lectures


def footer(canvas, doc):
    width, _ = landscape(A4)
    canvas.saveState()
    canvas.setFont("SheetRegular", 13)
    canvas.setFillColor(colors.HexColor("#10272D"))
    canvas.drawCentredString(width / 2, 580, "MRI Full Course Formula Sheet")
    canvas.setFont("SheetRegular", 7)
    canvas.setFillColor(colors.HexColor("#5B6668"))
    canvas.drawCentredString(width / 2, 566, "Compact formulas for exam memorization - two lectures per page")
    canvas.setFont("SheetRegular", 6.5)
    canvas.drawCentredString(width / 2, 7 * mm, f"MRI full-course formula sheet - page {doc.page}")
    canvas.restoreState()


def make_table(rows, styles, col_widths):
    table_rows = []
    for label, formula, note in rows:
        figure_match = re.fullmatch(r"\[\[figure:([a-z0-9_-]+)\]\]", formula)
        formula_cell = (
            sequence_figure(figure_match.group(1), col_widths[1] - 4)
            if figure_match
            else Paragraph(markdown_formula_to_reportlab(formula), styles["Formula"])
        )
        table_rows.append(
            [
                Paragraph(f"<b>{html_escape(label)}</b>", styles["CellLabel"]),
                formula_cell,
                Paragraph(markdown_formula_to_reportlab(note), styles["Note"]),
            ]
        )
    table = Table(table_rows, colWidths=col_widths, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTNAME", (0, 0), (-1, -1), "SheetRegular"),
                ("LEFTPADDING", (0, 0), (-1, -1), 2.2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2.2),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                ("GRID", (0, 0), (-1, -1), 0.2, colors.HexColor("#D4DBDE")),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F5F8F9")),
            ]
        )
    )
    return table


def build_pdf(lectures, output_pdf: Path):
    pdfmetrics.registerFont(TTFont("SheetRegular", find_font()))

    width, height = landscape(A4)
    margin_x = 8 * mm
    margin_top = 24 * mm
    margin_bottom = 12 * mm
    gutter = 6 * mm
    col_w = (width - 2 * margin_x - gutter) / 2

    frames = [
        Frame(
            margin_x + i * (col_w + gutter),
            margin_bottom,
            col_w,
            height - margin_top - margin_bottom,
            leftPadding=0,
            bottomPadding=0,
            rightPadding=0,
            topPadding=0,
            id=f"col{i}",
        )
        for i in range(2)
    ]

    base = getSampleStyleSheet()
    styles = {
        "LectureTitle": ParagraphStyle(
            "LectureTitle",
            parent=base["Heading1"],
            fontName="SheetRegular",
            fontSize=9.2,
            leading=10.4,
            textColor=colors.HexColor("#10272D"),
            spaceAfter=0,
        ),
        "Section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="SheetRegular",
            fontSize=7.8,
            leading=9.0,
            textColor=colors.white,
            backColor=colors.HexColor("#1F4B55"),
            borderPadding=(1.4, 3, 1.4, 3),
            spaceAfter=0,
        ),
        "CellLabel": ParagraphStyle(
            "CellLabel",
            parent=base["Normal"],
            fontName="SheetRegular",
            fontSize=5.8,
            leading=6.7,
            textColor=colors.HexColor("#17292E"),
        ),
        "Formula": ParagraphStyle(
            "Formula",
            parent=base["Normal"],
            fontName="SheetRegular",
            fontSize=5.75,
            leading=6.8,
            textColor=colors.HexColor("#0E1719"),
        ),
        "Note": ParagraphStyle(
            "Note",
            parent=base["Normal"],
            fontName="SheetRegular",
            fontSize=5.35,
            leading=6.4,
            textColor=colors.HexColor("#475254"),
        ),
    }

    story = []
    col_widths = [col_w * 0.20, col_w * 0.58, col_w * 0.22]

    for idx, lecture in enumerate(lectures):
        if idx > 0:
            story.append(FrameBreak() if idx % 2 == 1 else PageBreak())
        story.append(Paragraph(html_escape(lecture["title"]), styles["LectureTitle"]))
        story.append(Spacer(1, 0.6 * mm))
        for section in lecture["sections"]:
            story.append(
                KeepTogether(
                    [
                        Paragraph(html_escape(section["title"]), styles["Section"]),
                        make_table(section["rows"], styles, col_widths),
                        Spacer(1, 1.4 * mm),
                    ]
                )
            )

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(output_pdf), pagesize=landscape(A4))
    doc.addPageTemplates([PageTemplate(id="TwoLectures", frames=frames, onPage=footer)])
    doc.build(story)


def main():
    md_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MD
    output_pdf = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PDF
    lectures = parse_markdown(md_path)
    if not lectures:
        raise SystemExit(f"No lecture sections found in {md_path}")
    build_pdf(lectures, output_pdf)
    print(output_pdf)


if __name__ == "__main__":
    main()
