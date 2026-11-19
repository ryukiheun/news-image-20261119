#!/usr/bin/env python3
"""Draw the news-image-20261119 entry: a 1024x1024 newspaper-style
infographic, "Six Stories, One Thursday".

Six verified 19 November 2026 stories, each in its own card with a
hand-drawn pictogram, a coloured side bar and a region tag. Rendered
with Pillow only; fully deterministic, no network, no timestamps.
Run:  python3 draw_image.py   (writes entry.png beside this file)
"""

import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"

W, H = 1024, 1024

PAPER = (246, 241, 231)      # warm newsprint
INK = (26, 26, 24)           # near-black text
MUTED = (110, 104, 90)       # grey-brown secondary text
CARD = (255, 255, 255)
CARD_EDGE = (216, 208, 190)
MASTHEAD = (14, 59, 59)      # deep teal
GOLD = (232, 184, 75)
WHITE = (255, 255, 255)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SERIF_B = str(FONT_DIR / "DejaVuSerif-Bold.ttf")
SANS = str(FONT_DIR / "DejaVuSans.ttf")
SANS_B = str(FONT_DIR / "DejaVuSans-Bold.ttf")


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        print(f"WARNING: font not found, using default: {path}",
              file=sys.stderr)
        return ImageFont.load_default()


F_TITLE = font(SERIF_B, 58)
F_KICKER = font(SANS_B, 19)
F_SUB = font(SANS, 19)
F_TAG = font(SANS_B, 13)
F_HEAD = font(SANS_B, 21)
F_BODY = font(SANS, 15)
F_FOOT = font(SANS_B, 12)
F_CREDIT = font(SANS, 12)

STORIES = [
    dict(
        tag="CULTURE · WORLDWIDE",
        color=(108, 63, 181),
        head="GTA VI goes live after 13 years",
        body=("Rockstar's blockbuster unlocks at midnight local time, "
              "first in New Zealand. Sensor Tower puts advance sales "
              "past 15m copies."),
        foot="19 NOV 2026 · AUCKLAND FIRST",
        icon="controller",
    ),
    dict(
        tag="DIPLOMACY · SHENZHEN",
        color=(179, 55, 46),
        head="Trump, Xi and Putin meet in Shenzhen",
        body=("First-ever three-way summit of the US, Chinese and "
              "Russian leaders. Nuclear arms are Trump's top topic; "
              "no deal expected."),
        foot="19 NOV 2026 · ON THE APEC SIDELINES",
        icon="summit",
    ),
    dict(
        tag="JUSTICE · THE HAGUE",
        color=(31, 78, 121),
        head="World court rules on Rohingya genocide",
        body=("The ICJ rules today in Gambia's case against Myanmar, "
              "seven years after The Gambia filed the case. No state "
              "has ever been found responsible for genocide by the ICJ."),
        foot="19 NOV 2026 · PEACE PALACE, 10:00 CET",
        icon="scales",
    ),
    dict(
        tag="TECH · WASHINGTON",
        color=(14, 124, 107),
        head="US AI chip curbs take effect",
        body=("Licences needed for advanced chips to Indonesia, "
              "Malaysia, Singapore, Thailand and Brazil, and for "
              "data centres giving firms in China, Macau and other "
              "restricted states remote access over 12m TPP of "
              "computing power."),
        body_lines=4,
        foot="19 NOV 2026 · FEDERAL REGISTER",
        icon="chip",
    ),
    dict(
        tag="SPORT · WELLINGTON",
        color=(90, 125, 26),
        head="Bumrah strikes as India–NZ Test begins",
        body=("Cricket: India win the toss and bowl first at the Basin "
              "Reserve. Latham falls for 0 off the third ball; New "
              "Zealand 60 runs for 4 wickets at lunch."),
        foot="19 NOV 2026 · BASIN RESERVE",
        icon="cricket",
    ),
    dict(
        tag="SPORT · LAS VEGAS",
        color=(200, 90, 23),
        head="F1 takes over the Strip",
        body=("The Las Vegas Grand Prix weekend opens tonight with two "
              "practice sessions on the Strip circuit. The race "
              "is on Saturday."),
        foot="19 NOV 2026 · PRACTICE FROM 4:30 PM PT",
        icon="flag",
    ),
]


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(draw, kind, box, color):
    """Small pictogram in a 56x56 box (x, y), drawn from primitives."""
    x, y = box
    if kind == "controller":
        draw.rounded_rectangle([x + 4, y + 16, x + 52, y + 40], 10,
                               outline=color, width=4)
        draw.line([x + 14, y + 28, x + 22, y + 28], fill=color, width=3)
        draw.line([x + 18, y + 24, x + 18, y + 32], fill=color, width=3)
        for dx, dy in ((34, 24), (42, 24), (34, 32), (42, 32)):
            draw.ellipse([x + dx, y + dy, x + dx + 4, y + dy + 4],
                         fill=color)
    elif kind == "summit":
        for cx in (14, 28, 42):
            draw.ellipse([x + cx - 7, y + 6, x + cx + 7, y + 20], fill=color)
        draw.line([x + 6, y + 44, x + 50, y + 44], fill=color, width=4)
        draw.line([x + 14, y + 20, x + 14, y + 44], fill=color, width=3)
        draw.line([x + 28, y + 20, x + 28, y + 44], fill=color, width=3)
        draw.line([x + 42, y + 20, x + 42, y + 44], fill=color, width=3)
    elif kind == "scales":
        draw.line([x + 28, y + 6, x + 28, y + 46], fill=color, width=4)
        draw.line([x + 10, y + 12, x + 46, y + 12], fill=color, width=4)
        for cx in (12, 44):
            draw.line([x + cx, y + 12, x + cx - 8, y + 30], fill=color,
                      width=3)
            draw.line([x + cx, y + 12, x + cx + 8, y + 30], fill=color,
                      width=3)
            draw.arc([x + cx - 8, y + 22, x + cx + 8, y + 38], 0, 180,
                     fill=color, width=3)
        draw.line([x + 18, y + 46, x + 38, y + 46], fill=color, width=4)
    elif kind == "chip":
        draw.rectangle([x + 12, y + 12, x + 44, y + 44], outline=color,
                       width=4)
        draw.rectangle([x + 22, y + 22, x + 34, y + 34], fill=color)
        for i in range(3):
            px = x + 18 + i * 10
            draw.line([px, y + 4, px, y + 12], fill=color, width=3)
            draw.line([px, y + 44, px, y + 52], fill=color, width=3)
            draw.line([x + 4, y + 18 + i * 10, x + 12, y + 18 + i * 10],
                      fill=color, width=3)
            draw.line([x + 44, y + 18 + i * 10, x + 52, y + 18 + i * 10],
                      fill=color, width=3)
    elif kind == "cricket":
        draw.ellipse([x + 6, y + 30, x + 24, y + 48], fill=(178, 34, 34))
        draw.arc([x + 6, y + 30, x + 24, y + 48], 200, 340, fill=WHITE,
                 width=2)
        draw.line([x + 34, y + 46, x + 46, y + 16], fill=(122, 82, 44),
                  width=10)
        draw.line([x + 44, y + 20, x + 50, y + 8], fill=(122, 82, 44),
                  width=5)
    elif kind == "flag":
        draw.line([x + 8, y + 6, x + 8, y + 50], fill=color, width=4)
        for r in range(3):
            for c in range(4):
                if (r + c) % 2 == 0:
                    draw.rectangle(
                        [x + 12 + c * 9, y + 8 + r * 9,
                         x + 21 + c * 9, y + 17 + r * 9], fill=INK)
                else:
                    draw.rectangle(
                        [x + 12 + c * 9, y + 8 + r * 9,
                         x + 21 + c * 9, y + 17 + r * 9],
                        outline=INK, width=1)


def draw_card(draw, story, x, y, w, h):
    color = story["color"]
    draw.rounded_rectangle([x, y, x + w, y + h], 6, fill=CARD,
                           outline=CARD_EDGE, width=1)
    # left accent bar
    draw.rounded_rectangle([x, y, x + 9, y + h], 6, fill=color)
    draw.rectangle([x + 5, y, x + 9, y + h], fill=color)
    # pictogram, top right
    draw_icon(draw, story["icon"], (x + w - 72, y + 18), color)
    tx = x + 24
    tw = w - 24 - 84  # leave room for the icon
    # tag
    draw.text((tx, y + 18), story["tag"], font=F_TAG, fill=color)
    # headline, up to 2 lines
    head_all = wrap(draw, story["head"], F_HEAD, tw)
    if len(head_all) > 2:
        print(f"WARNING: headline truncated in card "
              f"'{story['head'][:40]}': {len(head_all)} lines > 2",
              file=sys.stderr)
    head_lines = head_all[:2]
    hy = y + 44
    for line in head_lines:
        draw.text((tx, hy), line, font=F_HEAD, fill=INK)
        hy += 26
    # body, up to 3 lines (4 for the chip card, which names the
    # five countries and the rule's threshold)
    body_cap = story.get("body_lines", 3)
    body_all = wrap(draw, story["body"], F_BODY, w - 48)
    if len(body_all) > body_cap:
        print(f"WARNING: body truncated in card "
              f"'{story['head'][:40]}': {len(body_all)} lines "
              f"> {body_cap}", file=sys.stderr)
    body_lines = body_all[:body_cap]
    by = hy + 10
    for line in body_lines:
        draw.text((tx, by), line, font=F_BODY, fill=(64, 60, 52))
        by += 21
    # footer
    draw.text((tx, y + h - 30), story["foot"], font=F_FOOT, fill=MUTED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- masthead ----
    draw.rectangle([0, 0, W, 168], fill=MASTHEAD)
    draw.rectangle([0, 168, W, 172], fill=GOLD)
    kicker = "THURSDAY  ·  19 NOVEMBER 2026"
    draw.text((24, 22), kicker, font=F_KICKER, fill=GOLD)
    draw.text((24, 52), "Six Stories, One Thursday", font=F_TITLE,
              fill=WHITE)
    draw.text((24, 124), "The world on Thursday — six stories, one day.",
              font=F_SUB, fill=(205, 220, 215))

    # ---- grid of cards ----
    margin, gutter = 22, 16
    cw = (W - 2 * margin - gutter) // 2
    top, bottom = 190, 992
    ch = (bottom - top - 2 * gutter) // 3
    for i, story in enumerate(STORIES):
        row, col = divmod(i, 2)
        x = margin + col * (cw + gutter)
        y = top + row * (ch + gutter)
        draw_card(draw, story, x, y, cw, ch)

    # ---- credit line ----
    credit = "Sources: AFP · Reuters · AP · NDTV · US BIS · RACER  —  19 November 2026"
    cw_px = draw.textlength(credit, font=F_CREDIT)
    draw.text(((W - cw_px) / 2, 1002), credit, font=F_CREDIT, fill=MUTED)

    img.save(OUT, "PNG")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
