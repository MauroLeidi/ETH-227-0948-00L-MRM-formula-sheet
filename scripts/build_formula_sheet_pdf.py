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
    text = re.sub(r"\^([A-Za-z0-9+\-*/().]+)", r"<sup>\1</sup>", text)
    text = re.sub(r"_([A-Za-z0-9+\-*/().]+)", r"<sub>\1</sub>", text)
    return text


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
    table_rows = [
        [
            Paragraph(f"<b>{html_escape(label)}</b>", styles["CellLabel"]),
            Paragraph(markdown_formula_to_reportlab(formula), styles["Formula"]),
            Paragraph(markdown_formula_to_reportlab(note), styles["Note"]),
        ]
        for label, formula, note in rows
    ]
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
            fontSize=5.9,
            leading=6.9,
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
    col_widths = [col_w * 0.22, col_w * 0.52, col_w * 0.26]

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
