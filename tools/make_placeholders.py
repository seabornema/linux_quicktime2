#!/usr/bin/env python3
"""Generate placeholder sprites. Needs Pillow (pip install pillow).
Run from the repo root:  python3 tools/make_placeholders.py [--force]
Existing files are NOT overwritten unless you pass --force."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("src/usr/share/qte-popups/sprites")
FORCE = "--force" in sys.argv
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
S = 256

def font(size):
    try:
        return ImageFont.truetype(BOLD, size)
    except OSError:
        return ImageFont.load_default()

def save(img, name):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    if path.exists() and not FORCE:
        print("skip (exists)", path); return
    img.save(path); print("wrote", path)

def flash(pressed):
    """Two frames: spacebar up / spacebar down."""
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    col = (255, 140, 0, 255) if pressed else (245, 197, 66, 255)
    d.rounded_rectangle((4, 4, S - 4, S - 4), 28, fill=(30, 30, 38, 255), outline=col, width=8)
    d.text((S / 2, 80), "MASH!", font=font(54), fill=col, anchor="mm")
    top = 150 if pressed else 136
    d.rounded_rectangle((28, top, S - 28, top + 56), 12, fill=col)
    d.text((S / 2, top + 28), "SPACE", font=font(30), fill=(30, 30, 38, 255), anchor="mm")
    return img

def badge(text, color, size):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.ellipse((6, 6, S - 6, S - 6), fill=(30, 30, 38, 255), outline=color, width=10)
    d.text((S / 2, S / 2), text, font=font(size), fill=color, anchor="mm")
    return img

save(flash(False), "flash_a.png")
save(flash(True),  "flash_b.png")
save(badge("NICE!", (61, 220, 132, 255), 58), "success.png")
save(badge("FAIL",  (255, 77, 77, 255), 66),  "fail.png")
