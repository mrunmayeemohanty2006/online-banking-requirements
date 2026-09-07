#!/usr/bin/env python3
"""
Reusable Markdown -> PDF generator using ReportLab.

Usage:
    python3 tools/generate_pdf.py INPUT.md OUTPUT.pdf [TITLE] [VERSION] [STATUS]

Converts Markdown (headings, paragraphs, lists, tables, horizontal rules,
basic bold/italic/code) into a professional A4 PDF with page numbers.
"""
import os
import re
import sys
import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
    HRFlowable,
    PageBreak,
)
from reportlab.pdfbase.pdfmetrics import stringWidth


def parse_markdown(md_text):
    """Parse simple markdown into ReportLab flowable elements."""
    lines = md_text.split("\n")
    elements = []
    i = 0
    n = len(lines)
    styles = getSampleStyleSheet()

    body = ParagraphStyle(
        "BodyText",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        spaceAfter=6,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        spaceAfter=3,
        leftIndent=12,
        bulletIndent=2,
    )

    def is_table_block(start):
        j = start
        if j >= n or not lines[j].strip().startswith("|"):
            return False
        # ensure there is a separator row
        if j + 1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[j + 1]):
            return True
        return False

    def is_list_block(start):
        j = start
        if j >= n:
            return False
        return bool(lines[j].strip()) and (
            re.match(r"^[-*]\s+", lines[j].strip())
            or re.match(r"^\d+\.\s+", lines[j].strip())
        )

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            size = max(14, 22 - (level - 1) * 2)
            style = ParagraphStyle(
                f"h{level}",
                parent=styles["Heading1"],
                fontSize=size,
                leading=size + 4,
                spaceBefore=14,
                spaceAfter=8,
                textColor=colors.HexColor("#1a1a2e"),
            )
            if level <= 2:
                elements.append(HRFlowable(
                    width="100%", thickness=1, color=colors.HexColor("#999999"),
                    spaceBefore=4, spaceAfter=10,
                ))
            elements.append(Paragraph(escape_and_format(text), style))
            i += 1
            continue

        # horizontal rule
        if re.match(r"^---+$", stripped) or re.match(r"^\*\*\*+$", stripped):
            elements.append(HRFlowable(
                width="100%", thickness=1, color=colors.HexColor("#cccccc"),
                spaceBefore=10, spaceAfter=10,
            ))
            i += 1
            continue

        # tables
        if is_table_block(i):
            rows = []
            while i < n and lines[i].strip().startswith("|") and lines[i].strip() != "|":
                row = lines[i].strip()
                if re.match(r"^\|[\s:|-]+\|$", row) and not any(
                    re.search(r"[^|:\-\s]", cell) for cell in split_md_row(row)
                ):
                    i += 1
                    continue
                cells = split_md_row(row)
                rows.append(cells)
                i += 1
            if rows:
                t = Table(rows, repeatRows=1)
                t.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e8f0")),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ]))
                # wrap cell content in Paragraphs for long text
                styled_data = []
                for ri, row in enumerate(rows):
                    styled_row = []
                    for ci, cell in enumerate(row):
                        cell = cell.replace("<br>", "<br/>")
                        cstyle = ParagraphStyle(
                            f"cell{ri}{ci}",
                            parent=styles["BodyText"],
                            fontSize=8.5,
                            leading=11,
                        )
                        styled_row.append(Paragraph(escape_and_format(cell), cstyle))
                    styled_data.append(styled_row)
                t = Table(styled_data, repeatRows=1, colWidths=None)
                t.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e8f0")),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ]))
                elements.append(t)
                elements.append(Spacer(1, 8))
            continue

        # bullet list
        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < n and lines[i].strip() and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(Paragraph(escape_and_format(lines[i].strip()[2:]), bullet))
                i += 1
            elements.append(ListFlowable(
                items, bulletType="bullet", start="bulletchar",
                leftIndent=14, bulletFontSize=6, spaceAfter=4,
            ))
            elements.append(Spacer(1, 4))
            continue

        # numbered list
        m = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if m:
            items = []
            while i < n and lines[i].strip() and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(ListItem(
                    Paragraph(escape_and_format(re.match(r"^\d+\.\s+(.*)$", lines[i].strip()).group(1)), bullet),
                    value=len(items) + 1,
                ))
                i += 1
            elements.append(ListFlowable(
                items, bulletType="1", leftIndent=14,
                bulletFormat="%s.", spaceAfter=4,
            ))
            elements.append(Spacer(1, 4))
            continue

        # paragraph (possibly multi-line)
        para_lines = []
        while i < n and lines[i].strip():
            para_lines.append(lines[i].strip())
            i += 1
        text = " ".join(para_lines)
        if text:
            elements.append(Paragraph(escape_and_format(text), body))

    return elements


def split_md_row(row):
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|") and not row.endswith("\\|"):
        row = row[:-1]
    cells = []
    current = ""
    esc = False
    for ch in row:
        if ch == "|" and not esc:
            cells.append(current.strip())
            current = ""
        else:
            if ch == "\\" and not esc:
                esc = True
                continue
            esc = False
            current += ch
    cells.append(current.strip())
    return cells


def escape_and_format(text):
    """Escape XML then apply simple markdown: **bold**, *italic*, `code`."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r"<font face='Courier'>\1</font>", text)
    return text


def add_page_number(canvas, doc, title):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(20 * mm, 12 * mm, title)
    canvas.drawRightString(A4[0] - 20 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def generate_pdf(md_path, pdf_path, title, version="1.0", status="RAW"):
    with open(md_path, "r") as f:
        md_text = f.read()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=title,
        author="BRD Agent",
    )

    header = [
        Paragraph(
            f"<b>{escape_and_format_and_title(title)}</b>",
            ParagraphStyle("hdr", parent=getSampleStyleSheet()["Title"], fontSize=16, leading=20),
        ),
    ]

    elements = parse_markdown(md_text)
    doc.build(elements, onFirstPage=lambda c, d: add_page_number(c, d, title),
              onLaterPages=lambda c, d: add_page_number(c, d, title))
    print(f"Wrote {pdf_path}")


def escape_and_format_and_title(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 tools/generate_pdf.py INPUT.md OUTPUT.pdf [TITLE] [VERSION] [STATUS]")
        sys.exit(1)
    md_path = sys.argv[1]
    pdf_path = sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(md_path)
    version = sys.argv[4] if len(sys.argv) > 4 else "1.0"
    status = sys.argv[5] if len(sys.argv) > 5 else "RAW"
    generate_pdf(md_path, pdf_path, title, version, status)
