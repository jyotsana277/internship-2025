from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import sys
import io


def create_watermark(text):

    packet = io.BytesIO()

    c = canvas.Canvas(packet)
    c.drawString(100, 10, text)
    c.save()

    packet.seek(0)

    return PdfReader(packet)


def add_watermark(input_pdf, output_pdf, text):

    watermark = create_watermark(text)

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        page.merge_page(watermark.pages[0])
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)


if __name__ == "__main__":

    add_watermark(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )