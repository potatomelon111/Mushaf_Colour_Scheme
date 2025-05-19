#!/usr/bin/env python3
"""
booklet_rtl.py

Creates an RTL-style booklet from any input PDF page size:
 - Places two pages side by side (right page on right, left page on left)
 - Scales pages down to fit half-width and full height of output page
 - Output page width = 2 × original page width, height = original page height
 - Adds a blank page at the end if original page count is odd

Usage:
    pip install pypdf
    python booklet_rtl.py "C:/path/to/input.pdf"
"""

import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter, Transformation, PageObject

def create_booklet(input_pdf: Path, output_pdf: Path) -> None:
    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()

    first = reader.pages[0]
    w_in = float(first.mediabox.width)
    h_in = float(first.mediabox.height)

    original_pages = list(reader.pages)
    total_pages = len(original_pages)

    pages = original_pages[:]

    # Add blank page at end if odd number of pages to make even
    if total_pages % 2 != 0:
        blank = PageObject.create_blank_page(width=w_in, height=h_in)
        pages.append(blank)
        total_pages += 1

    # Output page dimensions: double width, same height as original page
    sheet_w = w_in * 2
    sheet_h = h_in

    half_w = sheet_w / 2

    # Calculate scale to fit each page inside half sheet width and full height
    scale = min(half_w / w_in, sheet_h / h_in)

    scaled_w = w_in * scale
    scaled_h = h_in * scale

    # Vertically center pages on output sheet
    y_off = (sheet_h - scaled_h) / 2

    # Left page flush at x=0, right page flush at x=scaled width of left page
    x_off_left = 0
    x_off_right = scaled_w

    for i in range(0, total_pages, 2):
        sheet = PageObject.create_blank_page(width=sheet_w, height=sheet_h)

        # RIGHT side gets first page (j=0), LEFT side gets second page (j=1)
        for j in range(2):
            page = pages[i + j]
            tx = x_off_right if j == 0 else x_off_left
            ctm = Transformation().scale(sx=scale, sy=scale).translate(tx=tx, ty=y_off)
            sheet.merge_transformed_page(page, ctm, expand=False)

        writer.add_page(sheet)

    writer.write(str(output_pdf))

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} \"C:/path/to/input.pdf\"")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists() or input_path.suffix.lower() != '.pdf':
        print("Error: input must be a valid PDF file path.")
        sys.exit(1)

    output_path = input_path.with_name(input_path.stem + '_booklet.pdf')
    create_booklet(input_path, output_path)
    print(f"Booklet PDF saved to: {output_path}")

if __name__ == '__main__':
    main()
