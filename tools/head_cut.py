#!/usr/bin/env python3
"""Cut a head and a moving lower jaw out of a photo, for a paper cut-out puppet.

  uv run --python 3.11 --with mediapipe==0.10.14 --with pillow --with numpy --with scipy \
      python tools/head_cut.py <photo.jpg> <matte.png> <out_dir> <id>

Reads the photo (for face landmarks) and its background-removed matte (same size, RGBA).
Writes, all in one shared crop:
  head_<id>_full.png   the head, cut under the chin, nothing else touched: shown when he is silent
  head_<id>.png        the same head with the jaw area painted as a dark mouth: shown under the moving jaw
  jaw_<id>.png         the lower jaw from the lip line down; slide it down to open the mouth
  head_<id>_dark.png / jaw_<id>_dark.png   the same pieces at 12% brightness, for a silhouette
  <id>.json            sizes and anchor points in crop pixels
No pixel of the face is changed except the cut itself and the outline. A white cut edge is baked in."""
import json
import sys

import mediapipe as mp
import numpy as np
from scipy import ndimage
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter

photo_path, matte_path, out_dir, pid = sys.argv[1:5]
photo = Image.open(photo_path).convert("RGB")
matte = Image.open(matte_path).convert("RGBA")
W, H = photo.size
if matte.size != photo.size:
    matte = matte.resize(photo.size, Image.LANCZOS)

with mp.solutions.face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True,
                                     min_detection_confidence=0.4) as fm:
    res = fm.process(np.asarray(photo))
if not res.multi_face_landmarks:
    sys.exit("no face found")
lm = [(p.x * W, p.y * H) for p in res.multi_face_landmarks[0].landmark]

OVAL = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176,
        149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]
UP_IN = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308]
LO_IN = [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308]
oval = [lm[i] for i in OVAL]
xs, ys = [p[0] for p in oval], [p[1] for p in oval]
face_w, face_h = max(xs) - min(xs), max(ys) - min(ys)
chin = lm[152]
cx = (min(xs) + max(xs)) / 2

# 1. the head: everything of the matte above the lips; below them only what lies inside the face outline,
#    so collars, shoulders and a raised arm stay behind. Then the largest connected piece only.
mid = [((lm[a][0] + lm[b][0]) / 2, (lm[a][1] + lm[b][1]) / 2) for a, b in zip(UP_IN, LO_IN)]
left_c, right_c = mid[0], mid[-1]
lip_top = min(p[1] for p in mid)
cut_y = chin[1] + 0.05 * face_h
x_lo, x_hi = min(xs) - 0.42 * face_w, max(xs) + 0.42 * face_w
keep = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(keep)
d.rectangle([x_lo, 0, x_hi, lip_top - 0.06 * face_h], fill=255)
cy = sum(ys) / len(ys)
d.polygon([(cx + (x - cx) * 1.07, cy + (y - cy) * 1.06) for x, y in oval], fill=255)
alpha = ImageChops.multiply(matte.split()[3], keep)
lab, n = ndimage.label(np.asarray(alpha) > 40)
if n > 1:
    sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
    big = 1 + int(np.argmax(sizes))
    alpha = ImageChops.multiply(alpha, Image.fromarray(((lab == big) * 255).astype("uint8")))

# 2. the jaw is a slot, like a marionette's: from the line between the lips straight down past the chin,
#    a little wider than the mouth. The cheeks stay on the head.
pad = 0.10 * face_w
sx0, sx1 = min(left_c[0], right_c[0]) - pad, max(left_c[0], right_c[0]) + pad
bottom = cut_y + 0.04 * face_h
poly = [(sx0, left_c[1])] + mid + [(sx1, right_c[1]), (sx1, bottom), (sx0, bottom)]
jaw_mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(jaw_mask).polygon(poly, fill=255)
jaw_mask = jaw_mask.filter(ImageFilter.GaussianBlur(0.8))
jaw_alpha = ImageChops.multiply(jaw_mask, alpha)
max_drop = 0.09 * (chin[1] - alpha.getbbox()[1])
band = Image.new("L", (W, H), 0)   # the part of the head that shows when the jaw is down: the inside of the mouth
ImageDraw.Draw(band).polygon([(sx0 + 3, left_c[1] + 2)] + [(x, y + 2) for x, y in mid] + [(sx1 - 3, right_c[1] + 2)]
                             + [(sx1 - 3, right_c[1] + max_drop + 6)]
                             + [(x, y + max_drop + 6) for x, y in reversed(mid)] + [(sx0 + 3, left_c[1] + max_drop + 6)],
                             fill=255)
band = ImageChops.multiply(band, alpha)

# 3. crop both to one box
box = alpha.getbbox()
m = int(0.06 * face_w)
drop_room = int(0.20 * face_h)
box = (max(0, box[0] - m), max(0, box[1] - m), min(W, box[2] + m), min(H, box[3] + m + drop_room))
ox, oy = box[0], box[1]
rgb = photo.crop(box)
a_head, a_jaw, a_band = alpha.crop(box), jaw_alpha.crop(box), band.crop(box)

MOUTH = (38, 10, 14)
head = Image.new("RGBA", rgb.size, (0, 0, 0, 0))
head.paste(rgb, (0, 0), a_head)
inside = Image.new("RGBA", rgb.size, MOUTH + (255,))
teeth = ImageDraw.Draw(inside)  # a row of lower teeth that shows as the jaw goes down
for (x0, y0), (x1, y1) in zip(mid[2:-3], mid[3:-2]):
    teeth.polygon([(x0 - ox, y0 - oy + 0.035 * face_h), (x1 - ox, y1 - oy + 0.035 * face_h),
                   (x1 - ox, y1 - oy + 0.07 * face_h), (x0 - ox, y0 - oy + 0.07 * face_h)], fill=(232, 226, 214, 255))
plain = head.copy()          # the head before the mouth is cut: shown whenever he is not speaking
head.paste(inside, (0, 0), a_band)
jaw = Image.new("RGBA", rgb.size, (0, 0, 0, 0))
jaw.paste(rgb, (0, 0), a_jaw)

# 4. the white cut edge, outside the silhouette only (never along the lip cut)
stroke = max(3, int(0.022 * face_w))


def edge_of(a, forbid=None):
    grown = a.filter(ImageFilter.MaxFilter(stroke * 2 + 1)).filter(ImageFilter.GaussianBlur(0.7))
    if forbid is not None:
        grown = ImageChops.multiply(grown, forbid)
    return grown


def with_edge(piece, a, forbid=None):
    out = Image.new("RGBA", piece.size, (0, 0, 0, 0))
    white = Image.new("RGBA", piece.size, (250, 248, 242, 255))
    out.paste(white, (0, 0), edge_of(a, forbid))
    out.alpha_composite(piece)
    return out


below_lips = Image.new("L", rgb.size, 0)
lip_y = max(p[1] for p in mid) - oy
ImageDraw.Draw(below_lips).rectangle([0, chin[1] - oy - 0.02 * face_h, rgb.size[0], rgb.size[1]], fill=255)
head_o = with_edge(head, a_head)
# the jaw carries only the piece of the head's own outline that lies under it, so no white line crosses the face
slot = jaw_mask.crop(box).filter(ImageFilter.MaxFilter(stroke * 2 + 1))
jaw_edge = ImageChops.multiply(ImageChops.multiply(edge_of(a_head), slot), below_lips)
jaw_o = Image.new("RGBA", jaw.size, (0, 0, 0, 0))
jaw_o.paste(Image.new("RGBA", jaw.size, (250, 248, 242, 255)), (0, 0), jaw_edge)
jaw_o.alpha_composite(jaw)


def dark(piece, k=0.12):
    r, g, b, a = piece.split()
    return Image.merge("RGBA", (*ImageEnhance.Brightness(Image.merge("RGB", (r, g, b))).enhance(k).split(), a))


plain_o = with_edge(plain, a_head)
plain_o.save(f"{out_dir}/head_{pid}_full.png")
dark(plain_o).save(f"{out_dir}/head_{pid}_full_dark.png")
head_o.save(f"{out_dir}/head_{pid}.png")
jaw_o.save(f"{out_dir}/jaw_{pid}.png")
dark(head_o).save(f"{out_dir}/head_{pid}_dark.png")
dark(jaw_o).save(f"{out_dir}/jaw_{pid}_dark.png")

hair_top = a_head.getbbox()[1]
eye_y = (lm[159][1] + lm[386][1]) / 2 - oy
meta = {
    "id": pid, "source": photo_path, "crop_in_photo": box, "size": list(rgb.size),
    "head_height": round(chin[1] - oy - hair_top, 1), "face_width": round(face_w, 1),
    "neck": [round(cx - ox, 1), round(cut_y - oy, 1)],
    "mouth": [round((left_c[0] + right_c[0]) / 2 - ox, 1), round(lip_y, 1)],
    "eyes_y": round(eye_y, 1), "hair_top": hair_top, "chin_y": round(chin[1] - oy, 1),
    "jaw_max_drop": round(max_drop, 1), "stroke_px": stroke,
}
json.dump(meta, open(f"{out_dir}/{pid}.json", "w"), indent=1)
print(json.dumps(meta))
