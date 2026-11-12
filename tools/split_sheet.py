#!/usr/bin/env python3
"""Split the paper-doll sheet into one PNG per piece, by connected regions of the alpha channel.
Usage: python3 tools/split_sheet.py cast/sheets/paper_doll_sheet_v1.png cast/cutouts name1 name2 ...
Pieces are ordered left to right by their centre. Each is cropped to its own region (pixels of other pieces
removed), upscaled 2x (Lanczos) and written with 8 px of clear margin. Python 3 + Pillow only."""
import sys
from PIL import Image

src, out, names = sys.argv[1], sys.argv[2], sys.argv[3:]
im = Image.open(src).convert("RGBA")
w, h = im.size
alpha = im.split()[3].load()
label = [[0] * w for _ in range(h)]
regions = []
for y0 in range(h):
    for x0 in range(w):
        if alpha[x0, y0] > 24 and not label[y0][x0]:
            n = len(regions) + 1
            stack, pix = [(x0, y0)], []
            label[y0][x0] = n
            while stack:
                x, y = stack.pop()
                pix.append((x, y))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    u, v = x + dx, y + dy
                    if 0 <= u < w and 0 <= v < h and not label[v][u] and alpha[u, v] > 24:
                        label[v][u] = n
                        stack.append((u, v))
            regions.append(pix)
regions = [r for r in regions if len(r) > 1500]
regions.sort(key=lambda r: sum(p[0] for p in r) / len(r))
if len(regions) != len(names):
    sys.exit(f"found {len(regions)} pieces, expected {len(names)}")
src_px = im.load()
for pix, name in zip(regions, names):
    xs, ys = [p[0] for p in pix], [p[1] for p in pix]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs) + 1, max(ys) + 1
    piece = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    pp = piece.load()
    for x, y in pix:
        pp[x - x0, y - y0] = src_px[x, y]
    piece = piece.resize((piece.width * 2, piece.height * 2), Image.LANCZOS)
    canvas = Image.new("RGBA", (piece.width + 16, piece.height + 16), (0, 0, 0, 0))
    canvas.paste(piece, (8, 8), piece)
    canvas.save(f"{out}/{name}.png")
    print(name, canvas.size)
