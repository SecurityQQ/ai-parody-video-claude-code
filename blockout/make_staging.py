#!/usr/bin/env python3
"""Write staging.json for the blockout: the whole film blocked once in world time, each shot a camera on it.
Metres; x right, y into the picture, z up. Times are the film's clock and come from ../sound/beats.json.
Three sets sit apart on x so no shot sees another: atrium at x=0, dark corridor at x=40, daylight corridor at x=80.
Run: python3 make_staging.py   (then check_staging.py and stage_three.ts from the code-to-video-previz skill)"""
import json

ev = {e["id"]: e["time_on_grid"] for e in json.load(open("../sound/beats.json"))["events"]}
END = ev["cut_end"]

boxes = [
    # atrium (S1): a bridge across a tall hall, seen straight on
    {"name": "atrium_floor", "center": [0, 20, -0.1], "size": [30, 60, 0.2], "grey": 0.30},
    {"name": "atrium_wall_l", "center": [-12, 20, 9], "size": [0.5, 60, 18], "grey": 0.42},
    {"name": "atrium_wall_r", "center": [12, 20, 9], "size": [0.5, 60, 18], "grey": 0.42},
    {"name": "atrium_end", "center": [0, 44, 9], "size": [24, 0.5, 18], "grey": 0.55},
    {"name": "bridge", "center": [0, 20, 5.9], "size": [24, 2.2, 0.2], "grey": 0.22},
    {"name": "bridge_rail", "center": [0, 18.95, 6.5], "size": [24, 0.06, 0.08], "grey": 0.7, "no_block": True},
    {"name": "garden", "center": [0, 24, 0.6], "size": [14, 8, 1.2], "grey": 0.18, "no_block": True},
    # glass passage (S2): floor-height tracking shot
    {"name": "p_floor", "center": [-40, 3, -0.05], "size": [20, 10, 0.1], "grey": 0.34},
    {"name": "p_glass", "center": [-40, 3.4, 1.6], "size": [20, 0.1, 3.2], "grey": 0.62},
    {"name": "p_mullion_1", "center": [-41.5, 3.3, 1.6], "size": [0.08, 0.1, 3.2], "grey": 0.2, "no_block": True},
    {"name": "p_mullion_2", "center": [-38.5, 3.3, 1.6], "size": [0.08, 0.1, 3.2], "grey": 0.2, "no_block": True},
    {"name": "p_mullion_3", "center": [-35.5, 3.3, 1.6], "size": [0.08, 0.1, 3.2], "grey": 0.2, "no_block": True},
    # dark corridor (S3) with a lounge behind glass
    {"name": "c_floor", "center": [40, 4, -0.05], "size": [14, 24, 0.1], "grey": 0.20},
    {"name": "c_wall_l", "center": [38.2, -0.5, 1.6], "size": [0.3, 9, 3.2], "grey": 0.10},
    {"name": "c_wall_r", "center": [41.8, -0.5, 1.6], "size": [0.3, 9, 3.2], "grey": 0.10},
    {"name": "c_ceiling", "center": [40, -0.5, 3.25], "size": [3.9, 9, 0.1], "grey": 0.08, "no_block": True},
    {"name": "lounge_back", "center": [40, 13, 1.8], "size": [14, 0.3, 3.6], "grey": 0.60},
    {"name": "sofa_l", "center": [38.0, 9.0, 0.35], "size": [2.4, 0.9, 0.7], "grey": 0.30, "no_block": True},
    {"name": "sofa_r", "center": [42.2, 9.0, 0.35], "size": [2.4, 0.9, 0.7], "grey": 0.30, "no_block": True},
    {"name": "table", "center": [40.1, 9.2, 0.2], "size": [1.4, 0.7, 0.4], "grey": 0.36, "no_block": True},
    # daylight corridor (S4, S5): glass on the left, plain wall on the right
    {"name": "d_floor", "center": [80, 4, -0.05], "size": [16, 30, 0.1], "grey": 0.62},
    {"name": "d_wall_r", "center": [84.5, 4, 1.8], "size": [0.3, 30, 3.6], "grey": 0.80},
    {"name": "d_ceiling", "center": [80, 4, 3.65], "size": [16, 30, 0.1], "grey": 0.85, "no_block": True},
    {"name": "d_hill", "center": [68, 14, 1.0], "size": [10, 30, 2.0], "grey": 0.50, "no_block": True},
    # the jacket: a flat box that leaves Jensen and lands on Tim
    {"name": "jacket", "center": [40, -2.9, 1.25], "size": [0.6, 0.12, 0.7], "grey": 0.02, "no_block": True, "keys": [
        {"t": 0, "center": [40, -2.9, -3]},
        {"t": ev["jacket_off"] - 0.04, "center": [40, -2.9, -3]},
        {"t": ev["jacket_off"], "center": [40, -2.75, 1.25]},
        {"t": ev["jacket_off"] + 0.55, "center": [40.6, 2.5, 2.4]},
        {"t": ev["catch"], "center": [40.9, 6.85, 1.3]},
        {"t": ev["cut_s4"] - 0.001, "center": [40.9, 6.85, 1.3]},
        {"t": ev["cut_s4"], "center": [40, -2.9, -3]}]},
    # the card he holds up in S5
    {"name": "card", "center": [81.95, -2.0, -3], "size": [0.30, 0.05, 0.13], "grey": 0.05, "no_block": True, "keys": [
        {"t": 0, "center": [81.95, -2.05, -3]},
        {"t": ev["cut_s5"] - 0.001, "center": [81.95, -2.05, -3]},
        {"t": ev["cut_s5"], "center": [81.95, -2.05, 0.9]},
        {"t": ev["cut_s5"] + 0.5, "center": [81.95, -2.05, 1.45]},
        {"t": END, "center": [81.95, -2.05, 1.45]}]},
]

WALK = 1.4  # metres a second
figures = [
    {"name": "jensen", "height": 1.70, "color": 0.12, "keys": [
        # S1: crosses the bridge, left to right
        {"t": 0.0, "pos": [-7.5, 20, 6.0], "heading": 90},
        {"t": ev["cut_s2"] - 0.001, "pos": [-7.5 + WALK * ev["cut_s2"], 20, 6.0], "heading": 90},
        # S2: passes the floor camera (the passage is on the bridge level, further along)
        {"t": ev["cut_s2"], "pos": [-42.0, 2.0, 0], "heading": 90},
        {"t": ev["cut_s3"] - 0.001, "pos": [-42.0 + WALK * (ev["cut_s3"] - ev["cut_s2"]), 2.0, 0], "heading": 90},
        # S3: walks up the dark corridor to the lens and stops
        {"t": ev["cut_s3"], "pos": [40, 2.6, 0], "heading": 180},
        {"t": ev["strip_on_eyes"] + 0.2, "pos": [40, -2.9, 0], "heading": 180},
        {"t": ev["rack_focus"], "pos": [40, -2.9, 0], "heading": 180},
        {"t": ev["catch"] + 0.6, "pos": [39.5, -2.9, 0], "heading": 180},   # he edges to the left of frame
        {"t": ev["cut_s4"] - 0.001, "pos": [39.5, -2.9, 0], "heading": 180},
        # S5: leans in from the left
        {"t": ev["cut_s4"], "pos": [77.4, -1.9, 0], "heading": 90},
        {"t": ev["jensen_in"], "pos": [77.4, -1.9, 0], "heading": 90},
        {"t": ev["jensen_in"] + 0.3, "pos": [80.55, -1.9, 0], "heading": 100},
        {"t": END, "pos": [80.55, -1.9, 0], "heading": 100}]},
    {"name": "tim", "height": 1.83, "color": 0.72, "keys": [
        {"t": 0.0, "pos": [47.0, 7.0, 0], "heading": 270},                     # out of sight behind the right wall
        {"t": ev["rack_focus"] - 0.301, "pos": [47.0, 7.0, 0], "heading": 270},
        {"t": ev["rack_focus"] - 0.3, "pos": [43.3, 7.0, 0], "heading": 270},
        {"t": ev["catch"], "pos": [40.9, 7.0, 0], "heading": 270},      # walks in from the right behind the glass, catches the jacket, stops
        {"t": ev["cut_s4"] - 0.001, "pos": [40.9, 7.0, 0], "heading": 200},
        {"t": ev["cut_s4"], "pos": [82.4, 3.2, 0], "heading": 190},
        {"t": ev["wave"] + 0.45, "pos": [81.6, -2.0, 0], "heading": 185},   # walks up to his mark and stops
        {"t": END, "pos": [81.6, -2.0, 0], "heading": 185}]},
]

shots = [
    {"id": "s1", "start": 0, "end": ev["cut_s2"], "lens": 24, "ease": "hold", "subjects": ["jensen"],
     "from": {"pos": [0, -4, 7.2], "look": [0, 20, 6.6]}, "to": {"pos": [0, -4, 7.2], "look": [0, 20, 6.6]}},
    {"id": "s2", "start": ev["cut_s2"], "end": ev["cut_s3"], "lens": 35, "ease": "linear", "subjects": [],   # a shot of feet: his head is out of frame on purpose
     "from": {"pos": [-41.6, 0.5, 0.14], "look": [-41.5, 2.0, 0.22]},
     "to": {"pos": [-41.6 + WALK * (ev["cut_s3"] - ev["cut_s2"]) * 0.82, 0.5, 0.14], "look": [-41.5 + WALK * (ev["cut_s3"] - ev["cut_s2"]) * 0.82, 2.0, 0.22]}},
    {"id": "s3a", "start": ev["cut_s3"], "end": ev["lights_up"], "lens": 35, "ease": "out", "subjects": ["jensen"],
     "from": {"pos": [40, -4.4, 1.55], "look": [40, 4, 1.5]}, "to": {"pos": [40, -4.25, 1.55], "look": [40, 4, 1.5]}},
    {"id": "s3b", "start": ev["lights_up"], "end": ev["punch_no"], "lens": 50, "ease": "smooth", "subjects": ["jensen"],
     "from": {"pos": [40, -4.4, 1.55], "look": [40, 4, 1.52]}, "to": {"pos": [40, -4.2, 1.55], "look": [40, 4, 1.52]}},
    {"id": "s3c", "start": ev["punch_no"], "end": ev["wide_jacket"], "lens": 85, "ease": "hold", "subjects": ["jensen"],
     "from": {"pos": [40, -4.4, 1.58], "look": [40, 4, 1.58]}, "to": {"pos": [40, -4.4, 1.58], "look": [40, 4, 1.58]}},
    {"id": "s3d", "start": ev["wide_jacket"], "end": ev["cut_s4"], "lens": 35, "ease": "hold", "subjects": ["jensen", "tim"],
     "visible_from": {"tim": ev["rack_focus"]},
     "from": {"pos": [40, -4.4, 1.55], "look": [40, 4, 1.5]}, "to": {"pos": [40, -4.4, 1.55], "look": [40, 4, 1.5]}},
    {"id": "s4", "start": ev["cut_s4"], "end": ev["cut_s5"], "lens": 28, "ease": "hold", "subjects": ["tim"],
     "from": {"pos": [79.6, -6.2, 1.5], "look": [81.2, 4, 1.35]}, "to": {"pos": [79.6, -6.2, 1.5], "look": [81.2, 4, 1.35]}},
    {"id": "s5", "start": ev["cut_s5"], "end": END, "lens": 40, "ease": "smooth", "subjects": ["tim", "jensen"],
     "visible_from": {"jensen": ev["jensen_in"] + 0.3},
     "from": {"pos": [81.0, -4.7, 1.5], "look": [81.25, -2.0, 1.42]}, "to": {"pos": [81.0, -4.6, 1.5], "look": [81.25, -2.0, 1.42]}},
]

json.dump({"title": "Not you. Blockout", "frame": {"w": 1280, "h": 720, "fps": 24}, "shots": shots, "boxes": boxes,
           "figures": figures, "fill": 0.55}, open("staging.json", "w"), indent=1)
print("shots", [(s["id"], s["start"], s["end"]) for s in shots])
