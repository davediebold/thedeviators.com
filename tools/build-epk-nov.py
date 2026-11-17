from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import mm
from pathlib import Path

OUT = Path("docs/downloads/The_Deviators_EPK_2026-11.pdf")
styles = getSampleStyleSheet()
brand = colors.HexColor("#111111")
accent = colors.HexColor("#c5362e")
muted = colors.HexColor("#666666")

title = ParagraphStyle("title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=27, leading=30, alignment=TA_CENTER, textColor=brand, spaceAfter=8)
sub = ParagraphStyle("sub", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=14, alignment=TA_CENTER, textColor=accent, spaceAfter=15)
h = ParagraphStyle("h", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=brand, spaceBefore=10, spaceAfter=6)
body = ParagraphStyle("body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10, leading=14, textColor=brand, spaceAfter=8)
small = ParagraphStyle("small", parent=body, fontSize=8.5, leading=12, textColor=muted)
quote = ParagraphStyle("quote", parent=body, fontName="Helvetica-BoldOblique", fontSize=11, leading=15, leftIndent=8, rightIndent=8, textColor=brand, spaceBefore=5, spaceAfter=9)
link = ParagraphStyle("link", parent=body, textColor=accent)

story = [
    Spacer(1, 6*mm),
    Paragraph("THE DEVIATORS", title),
    Paragraph("ELECTRONIC PRESS KIT - NOVEMBER 2026", sub),
    Paragraph("Dublin three-piece. Original high-energy punk, pop and rock n roll.", h),
    Paragraph("The Deviators are Bitzy (guitar/vocals), Bren (bass/vocals) and Andy (drums/vocals): three Dublin musicians with decades of stage time behind them, now making new original material together. The songs are short, melodic and high-energy, with punk and guitar-pop roots and a live show built for a room.", body),
    Paragraph("<b>Debut album:</b> <i>More Volume, Less Reverb</i><br/><b>Produced by:</b> Stano<br/><b>Recorded at:</b> Hellfire Studios, County Dublin<br/><b>Engineered by:</b> Joe McGrath<br/><b>Mastered by:</b> Ivan Jackman", body),
    Paragraph("<b>Tokyo - out now</b>", h),
    Paragraph("The first single, <i>Tokyo</i>, was released on 1 November 2026 and launched live at The Grand Social, Dublin. The album is finished, vinyl pressing is underway, and a Dublin album launch is being planned for late February / early March 2027.", body),
    Paragraph('<link href="https://thedeviators1.bandcamp.com/track/tokyo" color="#c5362e"><u>Listen to Tokyo on Bandcamp</u></link><br/><link href="https://open.spotify.com/artist/3D9eaEDot52WmVWm9zcRU2" color="#c5362e"><u>The Deviators on Spotify</u></link><br/><link href="https://thedeviators.com/" color="#c5362e"><u>thedeviators.com</u></link>', link),
    Paragraph("Live", h),
    Paragraph("Recent shows include The Grand Social, Annesley House, Farewell to Bohs at Dalymount and a special-guest slot at Rocky De Valera & the Gravediggers' sold-out Grand Social reunion. Their 1 November show at The Grand Social launched <i>Tokyo</i> with Amadan as special guests.", body),
    Paragraph('"The songs were riotous and the crowd ate up every second of it." - The Goo', quote),
    Paragraph('"Terrific gig by both the Devs and the DeValeras." - Colm O\'Hare, music journalist', quote),
    Paragraph('"They have the look. They have the songs. They have the pedigrees. Most importantly, they have the Rock n Roll." - Karl Tsigdinos, Shakin\' Street', quote),
    PageBreak(),
    Paragraph("WHERE THEY'VE COME FROM", title)
]

for name, text_body in [
    ("BITZY", "Started in 1976 with The Slum and was fronting The Strougers by 1978. Baby Goes Boom followed, then a long break from music. He returned in 2009 with The Lee Harveys and spent 15 years with the band until their 2024 break. He is also the author of the punk memoir <i>Past the Point of Rescue</i>. A brief spell with The Last Pop Stars came before The Deviators."),
    ("BREN", "Started playing bass with The End in 1979 and later played alongside Andy in The Cathedral. In 2014 he teamed up with former The End drummer Johnny Bonnie in Trouble Pilgrims, the band that rose from the ashes of The Radiators From Space."),
    ("ANDY", "Started his first band, Slit Possex, at 14. The Cathedral followed in the early 1980s, then Cabra bands Purdah, Primatevo and Lure through the 90s. Clash Jam Wallop followed, then Complete Control and three years with The Modfathers before The Deviators.")
]:
    story += [Paragraph(name, h), Paragraph(text_body, body)]

story += [
    Paragraph("Press / booking assets", h),
    Paragraph('<link href="https://thedeviators.com/press/" color="#c5362e"><u>Live EPK / press page</u></link><br/><link href="https://thedeviators.com/media/" color="#c5362e"><u>Press photos and logo files</u></link><br/><link href="https://thedeviators.com/live/" color="#c5362e"><u>Live dates and video</u></link>', link),
    Spacer(1, 8*mm),
    Paragraph("BOOKINGS / MANAGEMENT", h),
    Paragraph("<b>Dave Diebold</b><br/>dave.diebold@gmail.com<br/>087 997 3953", body),
    Paragraph("The Deviators - Dublin, Ireland", small)
]

OUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=16*mm, title="The Deviators EPK - November 2026", author="The Deviators")
doc.build(story)
print(f"Built {OUT}")
