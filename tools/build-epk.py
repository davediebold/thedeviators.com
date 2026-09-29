"""Rebuild page two of the current Deviators EPK and publish the result."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
import shutil

from PIL import Image, ImageOps
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Deviators_EPK (updated).pdf"
PAGE_ONE_BASE = ROOT / "source-assets" / "documents" / "The_Deviators_EPK_2026-09_page1.pdf"
PUBLIC = ROOT / "docs" / "downloads" / "The_Deviators_EPK_2026-09.pdf"
IMAGE_DIR = ROOT / "docs" / "img"
TMP_DIR = ROOT / "tmp" / "pdfs" / "epk-build"
PAGE_W = 595.2756
PAGE_H = 841.8898


BIOS = [
    (
        "BITZY",
        "bitzy-band-guitar-vox-mono.jpg",
        "Bitzy started in 1976 with The Slum and was fronting The Strougers by 1978. "
        "Baby Goes Boom followed, then a long break from music. He returned in 2009 with "
        "The Lee Harveys and spent 15 years with the band until their 2024 break. He is also "
        "the author of the punk memoir <i>Past the Point of Rescue</i>, now on its third reprint. "
        "A brief spell with The Last Pop Stars came before The Deviators.",
        (0.5, 0.5),
    ),
    (
        "BREN",
        "bren-band-bass-mono.jpg",
        "Bren started playing bass with The End in 1979 and later played alongside Andy in "
        "The Cathedral. In 2014 he teamed up with former The End drummer Johnny Bonnie in "
        "Trouble Pilgrims, the band that rose from the ashes of The Radiators From Space.",
        (0.5, 0.34),
    ),
    (
        "ANDY",
        "andy-band-drums-mono.jpg",
        "Drummer Andy started his first band, Slit Possex, at 14. The Cathedral followed in "
        "the early 1980s, then Cabra bands Purdah, Primatevo and Lure through the '90s. "
        "Inspired by the loss of Joe Strummer, Clash Jam Wallop was born and Andy spent 16 "
        "years with them. Complete Control followed, then three years with The Modfathers, "
        "including festivals and larger stages, before The Deviators.",
        (0.5, 0.5),
    ),
]


def draw_cover_crop(c: canvas.Canvas, path: Path, x: float, y: float, w: float, h: float,
                    centering: tuple[float, float]) -> None:
    with Image.open(path) as source:
        fitted = ImageOps.fit(source.convert("L"), (round(w * 3), round(h * 3)),
                              method=Image.Resampling.LANCZOS, centering=centering)
        buffer = BytesIO()
        fitted.save(buffer, format="JPEG", quality=92, optimize=True)
        buffer.seek(0)
        c.drawImage(ImageReader(buffer), x, y, width=w, height=h, mask="auto")


def draw_paragraph(c: canvas.Canvas, text: str, x: float, y_top: float, w: float,
                   font_size: float = 7.8, leading: float = 9.7,
                   color=black) -> float:
    style = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=font_size,
        leading=leading,
        textColor=color,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(w, PAGE_H)
    paragraph.drawOn(c, x, y_top - height)
    return y_top - height


def draw_label(c: canvas.Canvas, text: str, x: float, y: float, size: float = 8.2) -> None:
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(black)
    c.drawString(x, y, text)


def build_first_page_overlay() -> bytes:
    stream = BytesIO()
    c = canvas.Canvas(stream, pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    x = 34
    y = 82
    w = 310
    h = 101
    c.setFillColor(HexColor("#f1f1f1"))
    c.rect(x, y, w, h, stroke=0, fill=1)
    c.setFillColor(black)
    c.rect(x, y, 4, h, stroke=0, fill=1)
    quote = (
        '"They have the look. They have the songs. They have the pedigrees. Most importantly, '
        "they have the Rock &#8217;n&#8217; Roll. The Deviators have it all...\""
    )
    draw_paragraph(c, f"<b>{quote}</b>", x + 16, y + h - 15, w - 30,
                   font_size=9.7, leading=12)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(x + 16, y + 14, "- KARL TSIGDINOS, SHAKIN' STREET")
    c.showPage()
    c.save()
    return stream.getvalue()


def build_second_page() -> bytes:
    stream = BytesIO()
    c = canvas.Canvas(stream, pagesize=(PAGE_W, PAGE_H), pageCompression=1)

    margin = 34
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 27)
    c.drawString(margin, 792, "WHERE THEY'VE COME FROM")

    logo = IMAGE_DIR / "logo-dark.png"
    with Image.open(logo) as logo_image:
        logo_w = 110
        logo_h = logo_w * logo_image.height / logo_image.width
    c.drawImage(str(logo), PAGE_W - margin - logo_w, 780, width=logo_w, height=logo_h,
                mask="auto", preserveAspectRatio=True)

    c.setLineWidth(2.2)
    c.line(margin, 754, PAGE_W - margin, 754)
    c.setFont("Helvetica", 6.6)
    c.setFillColor(HexColor("#666666"))
    date_text = "DUBLIN / SEPTEMBER 2026"
    c.drawRightString(PAGE_W - margin, 741, date_text)

    gap = 13
    col_w = (PAGE_W - 2 * margin - 2 * gap) / 3
    photo_y = 606
    photo_h = 118
    heading_y = 586
    body_top = 568

    for index, (name, image_name, bio, centering) in enumerate(BIOS):
        x = margin + index * (col_w + gap)
        draw_cover_crop(c, IMAGE_DIR / image_name, x, photo_y, col_w, photo_h, centering)
        c.setFillColor(black)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x, heading_y, name)
        draw_paragraph(c, bio, x, body_top, col_w, font_size=7.55, leading=9.3)

    quote_y = 385
    quote_h = 76
    quote_gap = 12
    quote_w = (PAGE_W - 2 * margin - quote_gap) / 2

    c.setFillColor(black)
    c.rect(margin, quote_y, quote_w, quote_h, stroke=0, fill=1)
    c.setFillColor(white)
    draw_paragraph(c, '<b>"THE SONGS WERE RIOTOUS AND THE CROWD ATE UP EVERY SECOND OF IT."</b>',
                   margin + 14, quote_y + quote_h - 13, quote_w - 28,
                   font_size=8.8, leading=10.8, color=white)
    c.setFont("Helvetica-Bold", 6.8)
    c.drawString(margin + 14, quote_y + 13, "- THE GOO")

    second_x = margin + quote_w + quote_gap
    c.setFillColor(HexColor("#ececec"))
    c.rect(second_x, quote_y, quote_w, quote_h, stroke=0, fill=1)
    c.setFillColor(black)
    c.rect(second_x, quote_y, 4, quote_h, stroke=0, fill=1)
    draw_paragraph(c, '<b>"TERRIFIC GIG BY BOTH THE DEVS AND THE DEVALERAS."</b>',
                   second_x + 16, quote_y + quote_h - 13, quote_w - 30,
                   font_size=8.8, leading=10.8)
    c.setFont("Helvetica-Bold", 6.8)
    c.drawString(second_x + 16, quote_y + 13, "- COLM O'HARE, MUSIC JOURNALIST")

    card_y = 190
    card_h = 154
    c.setFillColor(HexColor("#ececec"))
    c.rect(margin, card_y, PAGE_W - 2 * margin, card_h, stroke=0, fill=1)
    c.setFillColor(black)
    draw_label(c, "BOOKINGS / MANAGEMENT", margin + 14, card_y + card_h - 25)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(margin + 14, card_y + 90, "Dave Diebold")
    c.setFont("Helvetica", 9)
    c.drawString(margin + 14, card_y + 64, "dave.diebold@gmail.com")
    c.drawString(margin + 14, card_y + 44, "087 997 3953")

    link_x = PAGE_W - margin - 14
    links = [
        ("MUSIC - CREATURES", "https://soundcloud.com/deebs1967/creatures_edit"),
        ("LIVE - GRAND SOCIAL", "https://thedeviators.com/live/"),
    ]
    link_ys = [card_y + 91, card_y + 67]
    c.setFont("Helvetica-Bold", 8.2)
    for (label, url), y in zip(links, link_ys):
        width = stringWidth(label, "Helvetica-Bold", 8.2)
        c.drawRightString(link_x, y, label)
        c.linkURL(url, (link_x - width, y - 3, link_x, y + 9), relative=0)
    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor("#666666"))
    c.drawRightString(link_x, card_y + 27, "CLICK THE LINKS IN THIS PDF")

    c.setStrokeColor(HexColor("#999999"))
    c.setLineWidth(0.5)
    c.line(margin, 70, PAGE_W - margin, 70)
    c.setFillColor(HexColor("#555555"))
    c.setFont("Helvetica-Bold", 7)
    c.drawString(margin, 57, "THE DEVIATORS - EPK")
    c.drawRightString(PAGE_W - margin, 57, "MANAGEMENT: DAVE DIEBOLD")

    c.showPage()
    c.save()
    return stream.getvalue()


def main() -> None:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    original_bytes = PAGE_ONE_BASE.read_bytes()
    source_reader = PdfReader(BytesIO(original_bytes))
    overlay_reader = PdfReader(BytesIO(build_first_page_overlay()))
    second_reader = PdfReader(BytesIO(build_second_page()))

    writer = PdfWriter()
    first_page = source_reader.pages[0]
    first_page.merge_page(overlay_reader.pages[0])
    writer.add_page(first_page)
    writer.add_page(second_reader.pages[0])
    if source_reader.metadata:
        metadata = {key: str(value) for key, value in source_reader.metadata.items() if value is not None}
        writer.add_metadata(metadata)

    output = TMP_DIR / "The_Deviators_EPK_2026-09.pdf"
    with output.open("wb") as handle:
        writer.write(handle)

    shutil.copy2(output, SOURCE)
    shutil.copy2(output, PUBLIC)
    print(f"Updated {SOURCE.relative_to(ROOT)}")
    print(f"Updated {PUBLIC.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
