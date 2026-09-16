#!/usr/bin/env python3
"""Build the Vector Screen Holder subset of Fusion Pixel Font.

Takes the 12px monospaced Latin build and keeps the alphabetic scripts a short
status line can plausibly be written in: ASCII, Latin-1, Latin Extended-A and
B, spacing and combining diacritics, Greek, Cyrillic and Cyrillic Supplement,
and general punctuation. That is 717 glyphs, which is every language written in
a Latin, Greek or Cyrillic alphabet.

The point of the subset is size. The full family is about seven megabytes per
language build, which is not something a single file Windhawk mod can carry.
At 717 glyphs it is 62 KB as TrueType and 8 KB as WOFF2, small enough to sit
inside the mod's source as base64 and be unpacked by DirectWrite at startup.

Usage:
    python subset.py path/to/fusion-pixel-12px-monospaced-latin.ttf

Requires fonttools and brotli:
    pip install fonttools brotli
"""
import sys
import os
from fontTools import subset
from fontTools.ttLib import TTFont

RANGES = [
    (0x0020, 0x007E),   # ASCII
    (0x00A0, 0x00FF),   # Latin-1 Supplement
    (0x0100, 0x017F),   # Latin Extended-A
    (0x0180, 0x024F),   # Latin Extended-B
    (0x02B0, 0x02FF),   # Spacing Modifier Letters
    (0x0300, 0x036F),   # Combining Diacritical Marks
    (0x0370, 0x03FF),   # Greek and Coptic
    (0x0400, 0x04FF),   # Cyrillic
    (0x0500, 0x052F),   # Cyrillic Supplement
    (0x2000, 0x206F),   # General Punctuation
    (0x20A0, 0x20BF),   # Currency Symbols
]

DROP = ['DSIG', 'GPOS', 'GSUB', 'FFTM', 'gasp', 'prep', 'fpgm', 'cvt ',
        'hdmx', 'VDMX', 'LTSH', 'PCLT', 'vhea', 'vmtx', 'VORG']

OUT = "fusion-pixel-12px-mono-latin-vsh"


def build(src, flavor, ext):
    font = TTFont(src)
    opts = subset.Options()
    opts.layout_features = []
    # 0 copyright, 13 license description and 14 license URL travel with it
    opts.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]
    opts.name_legacy = True
    opts.notdef_outline = True
    opts.glyph_names = False
    opts.drop_tables += DROP

    have = set(TTFont(src, lazy=True).getBestCmap().keys())
    cps = sorted({c for lo, hi in RANGES for c in range(lo, hi + 1) if c in have})

    sub = subset.Subsetter(options=opts)
    sub.populate(unicodes=cps)
    sub.subset(font)
    if flavor:
        font.flavor = flavor
    path = "%s.%s" % (OUT, ext)
    font.save(path)
    return path, len(cps), os.path.getsize(path)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    src = sys.argv[1]
    for flavor, ext in ((None, "ttf"), ("woff2", "woff2")):
        path, n, size = build(src, flavor, ext)
        print("%-38s %6d glyphs  %7d bytes" % (path, n, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
