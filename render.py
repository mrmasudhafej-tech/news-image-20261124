#!/usr/bin/env python3
"""Draw the 24 November 2026 front page and save it as entry.png.

Original artwork drawn with Pillow for this competition day only.
Run:  python3 render.py   (writes entry.png next to this file, 1024x1024)
The shipped entry program (main.py) only copies entry.png to the output
directory, so grading runs are byte-identical.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 246, 236)
INK = (22, 22, 22)
NAVY = (22, 41, 77)
RED = (176, 30, 36)
GREY = (90, 90, 84)
LIGHT_BLUE = (168, 205, 232)
DARK_SKY = (16, 32, 64)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Split text into lines that fit max_width pixels."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_width, fill, spacing=6):
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def headline_block(draw, x, y, text, fnt, max_width, fill, spacing=2):
    return draw_wrapped(draw, x, y, text, fnt, max_width, fill, spacing)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 34
    right = W - mx
    cw = right - mx

    # ---- Masthead ----
    d.text((W // 2, 30), "ONE DAY  \u2022  ONE PAGE  \u2022  THE WORLD'S NEWS",
           font=font(SANS_BOLD, 19), fill=GREY, anchor="ma")
    d.text((W // 2, 56), "WORLD NEWS",
           font=font(SERIF_BOLD, 88), fill=NAVY, anchor="ma")
    d.text((W // 2, 152), "TUESDAY  24  NOVEMBER  2026",
           font=font(SANS_BOLD, 30), fill=RED, anchor="ma")
    d.line([(mx, 196), (right, 196)], fill=INK, width=4)
    d.line([(mx, 202), (right, 202)], fill=INK, width=1)

    # ---- Lead story: full-width panel ----
    top, bottom = 214, 510
    d.rectangle([mx, top, right, bottom], outline=NAVY, width=3)
    # illustration panel on the right
    art_x0, art_y0 = right - 308, top + 14
    art_x1, art_y1 = right - 14, bottom - 40
    d.rectangle([art_x0, art_y0, art_x1, art_y1], fill=DARK_SKY)
    # stars
    for sx, sy in [(art_x0 + 30, art_y0 + 26), (art_x0 + 120, art_y0 + 18),
                   (art_x0 + 210, art_y0 + 40), (art_x0 + 70, art_y0 + 70),
                   (art_x0 + 250, art_y0 + 90), (art_x0 + 160, art_y0 + 55)]:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
    # Earth arc at the bottom of the panel, kept inside it
    d.ellipse([art_x0 + 16, art_y1 - 58, art_x1 - 16, art_y1 + 2],
              fill=(52, 110, 168))
    d.ellipse([art_x0 + 48, art_y1 - 44, art_x0 + 118, art_y1 - 6],
              fill=(74, 150, 84))
    d.ellipse([art_x0 + 168, art_y1 - 50, art_x0 + 232, art_y1 - 12],
              fill=(74, 150, 84))
    # dashed orbit
    for i in range(0, 360, 18):
        import math
        a = math.radians(i)
        ox = (art_x0 + art_x1) // 2 + int(128 * math.cos(a))
        oy = (art_y0 + art_y1) // 2 + int(78 * math.sin(a))
        d.ellipse([ox - 3, oy - 3, ox + 3, oy + 3], fill=(255, 255, 255))
    # satellite: body + solar panels
    cx, cy = (art_x0 + art_x1) // 2 + 52, (art_y0 + art_y1) // 2 - 52
    d.rectangle([cx - 52, cy - 8, cx - 18, cy + 8], fill=(200, 60, 60))
    d.rectangle([cx + 18, cy - 8, cx + 52, cy + 8], fill=(200, 60, 60))
    d.rectangle([cx - 16, cy - 14, cx + 16, cy + 14], fill=(220, 220, 220),
                outline=NAVY, width=2)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED)
    d.text(((art_x0 + art_x1) // 2, bottom - 32),
           "SATELLITE 'SPUTNIK-S' \u2014 REPORTED",
           font=font(SANS_BOLD, 14), fill=NAVY, anchor="ma")

    tx = mx + 16
    tw = art_x0 - tx - 18
    d.text((tx, top + 14), "SPACE  \u2022  BERLIN",
           font=font(SANS_BOLD, 20), fill=RED)
    y = headline_block(d, tx, top + 46,
                       "NATO vows to defend space as Russia 'may launch nuclear satellite'",
                       font(SERIF_BOLD, 36), tw, INK)
    y += 8
    draw_wrapped(d, tx, y,
                 "Western intelligence reports say Moscow has built "
                 "Sputnik-S, a satellite designed to carry a nuclear "
                 "warhead, and could launch it within weeks. NATO chief "
                 "Mark Rutte vowed to defend allied territory in "
                 "space; the Kremlin denies the reports.",
                 font(SANS, 21), tw, INK, spacing=3)

    # ---- Middle row: two stories ----
    d.line([(mx, 524), (right, 524)], fill=INK, width=2)
    mid_y = 536
    col_w = (cw - 28) // 2
    lx, rx = mx, mx + col_w + 28
    d.line([(mx + col_w + 14, mid_y), (mx + col_w + 14, 700)],
           fill=GREY, width=1)

    # Left: Libya
    d.text((lx, mid_y), "WAR AT SEA  \u2022  LIBYA",
           font=font(SANS_BOLD, 19), fill=RED)
    y = headline_block(d, lx, mid_y + 28,
                       "Ukraine says sea drones sank Russian warship off Libya",
                       font(SERIF_BOLD, 30), col_w, INK)
    draw_wrapped(d, lx, y + 6,
                 "Zelenskyy said sea drones sank the corvette "
                 "Merkury at Benghazi and hit the Angara.",
                 font(SANS, 20), col_w, INK, spacing=4)

    # Right: Estonia
    d.text((rx, mid_y), "EUROPE  \u2022  ESTONIA",
           font=font(SANS_BOLD, 19), fill=RED)
    y = headline_block(d, rx, mid_y + 28,
                       "Russia warns Estonia it is 'on the verge of open war'",
                       font(SERIF_BOLD, 30), col_w, INK)
    draw_wrapped(d, rx, y + 6,
                 "Moscow summoned Estonia's envoy over its "
                 "border-closure plan. Tallinn denies the airspace claim.",
                 font(SANS, 20), col_w, INK, spacing=4)

    # ---- Bottom row: two boxed stories ----
    d.line([(mx, 714), (right, 714)], fill=INK, width=2)
    box_y, box_h = 728, 208
    for bx, header in [(lx, "TECH & LAW  \u2022  UNITED STATES"),
                       (rx, "SPORT  \u2022  GENEVA")]:
        d.rectangle([bx, box_y, bx + col_w, box_y + box_h], outline=INK,
                    width=2)
        d.rectangle([bx, box_y, bx + col_w, box_y + 34], fill=NAVY)
        d.text((bx + 12, box_y + 6), header,
               font=font(SANS_BOLD, 18), fill=(255, 255, 255))
    # Grok story
    y = headline_block(d, lx + 12, box_y + 44,
                       "Two states sue Musk firms over Grok sexualised images",
                       font(SERIF_BOLD, 26), col_w - 24, INK)
    draw_wrapped(d, lx + 12, y + 6,
                 "Virginia and Oregon, the first states to sue, say "
                 "Grok's 'spicy mode' turned photos into sexualised "
                 "images without consent.",
                 font(SANS, 20), col_w - 24, INK, spacing=4)
    # Chess story
    y = headline_block(d, rx + 12, box_y + 44,
                       "Youngest chess title match begins: Gukesh v Sindarov",
                       font(SERIF_BOLD, 26), col_w - 24, INK)
    draw_wrapped(d, rx + 12, y + 6,
                 "Both aged 20, champion Gukesh defends his crown "
                 "against Sindarov in a 14-game match. Game 1 is "
                 "today in Geneva.",
                 font(SANS, 20), col_w - 24, INK, spacing=4)

    # ---- Footer strip ----
    d.line([(mx, 950), (right, 950)], fill=INK, width=1)
    d.text((W // 2, 958),
           "ALSO: UN chief urges a global AI safety framework within a year \u2014 Barbados summit",
           font=font(SANS_BOLD, 19), fill=NAVY, anchor="ma")
    d.text((W // 2, 984),
           "Stories reported on 24 November 2026  \u2022  Sources: Reuters, AP, SCMP, Japan Times, Chess.com",
           font=font(SANS, 15), fill=GREY, anchor="ma")

    out = "entry.png"
    img.save(out, optimize=True)
    print(f"saved {out} {img.size}")


if __name__ == "__main__":
    main()
