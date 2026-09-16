# Fusion Pixel Font, Vector Screen Holder subset

A 717 glyph subset of [Fusion Pixel Font](https://github.com/TakWolf/fusion-pixel-font)
by [TakWolf](https://takwolf.com), cut for
[Vector Screen Holder](https://github.com/akilluminati47/vector-screen-holder),
a Windhawk mod that fills a display with generative line art. The mod draws one
short status line, and this is the font it draws it in.

## What is in it

The 12px monospaced Latin build, reduced to the alphabetic scripts a status
line can plausibly be written in:

| Range | Block |
| --- | --- |
| U+0020 to U+007E | ASCII |
| U+00A0 to U+00FF | Latin-1 Supplement |
| U+0100 to U+017F | Latin Extended-A |
| U+0180 to U+024F | Latin Extended-B |
| U+02B0 to U+02FF | Spacing Modifier Letters |
| U+0300 to U+036F | Combining Diacritical Marks |
| U+0370 to U+03FF | Greek and Coptic |
| U+0400 to U+04FF | Cyrillic |
| U+0500 to U+052F | Cyrillic Supplement |
| U+2000 to U+206F | General Punctuation |
| U+20A0 to U+20BF | Currency Symbols |

That covers every language written in a Latin, Greek or Cyrillic alphabet. CJK,
Arabic, Hebrew, Thai and the Indic scripts are **not** in the subset; the mod
sends those to the system interface font instead, matched for size.

## Why

Size. The full family is about seven megabytes per language build. A Windhawk
mod is a single C++ source file, so the font has to travel inside it as text.
At 717 glyphs it is 62 KB as TrueType and 8 KB as WOFF2, and 8 KB of base64
fits in a source file without dominating it. The mod hands the WOFF2 to
DirectWrite, which unpacks it into a private font collection at startup.

| Build | Glyphs | Size |
| --- | --- | --- |
| Upstream 12px monospaced Latin | 36539 | 6.98 MB |
| This subset, TrueType | 717 | 62 KB |
| This subset, WOFF2 | 717 | 8 KB |

## Building it

```
pip install fonttools brotli
python subset.py path/to/fusion-pixel-12px-monospaced-latin.ttf
```

The input is the `fusion-pixel-font-12px-monospaced-ttf` archive from the
[upstream releases](https://github.com/TakWolf/fusion-pixel-font/releases).
Nothing is redrawn or added: every glyph here is TakWolf's, unchanged, and the
family name is unchanged with it.

## License

The font is licensed under the [SIL Open Font License 1.1](https://openfontlicense.org),
the same as upstream, and the copyright notice and license text travel inside
the font's own name table. Copyright (c) 2022, TakWolf.

The build script in this directory is MIT, matching the mod it was written for.
