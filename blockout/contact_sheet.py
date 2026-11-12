#!/usr/bin/env python3
"""First, middle and last frame of each shot as one sheet: rows are shots in film order, columns first / middle / last.
Usage: python3 contact_sheet.py renders/blockout_v001.mp4 stills/contact_v001.jpg"""
import json, subprocess, sys
from PIL import Image

video, out = sys.argv[1], sys.argv[2]
S = json.load(open("staging.json"))
fps = S["frame"]["fps"]
W, H = 400, 225
sheet = Image.new("RGB", (W * 3, H * len(S["shots"])), (20, 20, 20))
for r, s in enumerate(S["shots"]):
    n0, n1 = round(s["start"] * fps), round(s["end"] * fps) - 1
    for c, n in enumerate((n0, (n0 + n1) // 2, n1)):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-vf", f"select=eq(n\\,{n}),scale={W}:{H}",
                              "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
        import io
        sheet.paste(Image.open(io.BytesIO(raw)).convert("RGB"), (c * W, r * H))
sheet.save(out, quality=88)
print(out, sheet.size, "rows:", [s["id"] for s in S["shots"]])
