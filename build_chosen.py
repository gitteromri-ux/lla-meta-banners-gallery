#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHOSEN BANNERS — final corrected set.
The 6 banners Omri selected from V3/V4, rebuilt in the V7 full-bleed feed-native
layout (the approved reference), with corrections:
  1. Every banner shows: brand lockup + headline + Julie's name block +
     Trustpilot + CTA, exactly like the approved reference layout.
  2. Trustpilot now includes the Trustpilot NAME (official wordmark logo),
     not just the stars.
  3. "2nd Slowest-Aging Person on Earth" enlarged — clearly visible.
  4. V7 fonts everywhere: Playfair Display headlines + Inter.
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
BANNERS_DIR = f"{ROOT}/banners/chosen"
ASSETS = "../../assets"
os.makedirs(BANNERS_DIR, exist_ok=True)

SIZES = {
    "1x1":   {"w":1080, "h":1080, "label":"1:1 Feed",     "note":"Instagram Post / FB Feed Square"},
    "4x5":   {"w":1080, "h":1350, "label":"4:5 Vertical", "note":"Instagram / FB Feed Vertical"},
    "9x16":  {"w":1080, "h":1920, "label":"9:16 Story",   "note":"IG Stories, Reels, FB Stories"},
    "191x1": {"w":1200, "h":628,  "label":"1.91:1 Link",  "note":"FB Link Ad / Marketplace"},
}

FONT_LINK = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">"""

NAVY_DEEP  = "#050E22"
NAVY_BAR   = "#03102A"
BLUE       = "#006EFF"
BLUE_LT    = "#7EC8FF"
WHITE      = "#FFFFFF"

def html_head(w, h):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
{FONT_LINK}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ width:{w}px; height:{h}px; overflow:hidden; background:{NAVY_DEEP}; }}
.canvas {{ position:relative; width:{w}px; height:{h}px; background:{NAVY_DEEP}; font-family:'Inter',sans-serif; overflow:hidden; }}
.display {{ font-family:'Playfair Display',serif; font-weight:800; letter-spacing:-.01em; }}
</style></head><body>"""

def scale_for(w, h):
    area = w * h
    s = (area / (1080*1080)) ** 0.5
    ratio = w / h
    return s, ratio

# FIX: clean icon-only mark top-left (no smeared dark logo text on light photos)
def brand_lockup(s, scale_mult=1.0):
    logo_h = int(110 * s * scale_mult)
    return f"""
<div class="brandlock" style="display:flex; align-items:center; justify-content:flex-start;">
  <img src="{ASSETS}/lla_logo_mark_icon.png" style="height:{logo_h}px; display:block; filter:drop-shadow(0 3px 14px rgba(0,0,0,.55));">
</div>"""

# NEW: large text brand lockup above the headline — exactly like the website
# homepage fold, but "Longevity Life Academy" in ONE line.
def brand_text_lockup(s, is_landscape=False):
    lla_size = int((52 if is_landscape else 58) * s)
    by_size  = max(13, int(lla_size * 0.40))
    grp_size = max(11, int(by_size * 0.78))
    gap = max(4, int(8*s))
    return f"""
<div style="display:flex; flex-direction:column; align-items:flex-start; gap:{gap}px; margin-bottom:{int(26*s)}px;">
  <div style="font-family:'Playfair Display',serif; font-weight:600; font-size:{lla_size}px; line-height:1; letter-spacing:.005em; white-space:nowrap; text-shadow:0 4px 24px rgba(0,0,0,.65);"><span style="color:#8FC7F2;">Longevity</span> <span style="color:#FFFFFF;">Life Academy</span></div>
  <div style="font-size:{by_size}px; line-height:1; text-shadow:0 2px 12px rgba(0,0,0,.6);"><span style="font-family:'Playfair Display',serif; font-style:italic; font-weight:600; color:rgba(255,255,255,.9);">by</span> <span style="font-family:'Inter',sans-serif; font-weight:800; color:#4B9BFF; letter-spacing:.01em;">eTeacher</span> <span style="font-family:'Playfair Display',serif; font-style:italic; font-weight:500; font-size:{grp_size}px; color:rgba(255,255,255,.85);">Group</span></div>
</div>"""

# FIX: Julie's block MUCH larger — credential WAY larger, in NEON, it must stick out.
NEON = "#7EC8FF"
NEON_GLOW = "0 2px 16px rgba(0,0,0,.55)"
def julie_credential(s, size_mult=1.0):
    name_size = max(18, int(32 * s * size_mult))
    cred_size = max(20, int(38 * s * size_mult))   # WAY larger than before, neon
    tag_size  = max(15, int(24 * s * size_mult))
    return f"""
<div style="display:flex; flex-direction:column; align-items:flex-start; text-align:left; gap:{max(4,int(7*s))}px;">
  <div style="font-weight:800; font-size:{name_size}px; color:{WHITE}; text-shadow:0 3px 16px rgba(0,0,0,.6);">Julie Gibson Clark</div>
  <div style="font-weight:900; font-size:{cred_size}px; color:{NEON}; letter-spacing:.01em; line-height:1.15; white-space:nowrap; text-shadow:{NEON_GLOW};">2nd Slowest-Aging Person on Earth</div>
  <div style="font-weight:700; font-size:{tag_size}px; color:{BLUE_LT}; letter-spacing:.01em; line-height:1.3; text-shadow:0 2px 12px rgba(0,0,0,.55);">Longevity Life Academy Instructor</div>
</div>"""

def cta_button(s, text="Enroll Now", size_mult=1.0):
    font = max(15, int(25 * s * size_mult))
    pad_v = max(12, int(20 * s * size_mult))
    pad_h = max(24, int(42 * s * size_mult))
    return f"""<span class="cta" style="font-size:{font}px; padding:{pad_v}px {pad_h}px;">{text} <span>&rarr;</span></span>"""

CTA_CSS = f"""
.cta {{ display:inline-flex; align-items:center; gap:10px; background:linear-gradient(135deg,#3A8DFF 0%,{BLUE} 100%); color:#fff; font-weight:800; border-radius:999px; border:1.5px solid rgba(255,255,255,.55); box-shadow:0 8px 28px rgba(0,110,255,.55), inset 0 1px 0 rgba(255,255,255,.35); white-space:nowrap; font-family:'Inter',sans-serif; }}
"""

TRUST_CSS = """
.trust { display:flex; align-items:center; color:rgba(255,255,255,.9); font-weight:600; }
.trust img { display:block; }
"""

# FIX: Trustpilot wordmark (official logo incl. name) + 5 stars + 4.6/5
def trust_row(s, size_mult=1.0):
    logo_h = max(16, int(24*s*size_mult))   # "Trustpilot" wordmark height
    star_h = max(14, int(22*s*size_mult))
    fs = max(13, int(18*s*size_mult))
    gap = max(8, int(12*s))
    return f"""<div class="trust" style="font-size:{fs}px; gap:{gap}px;"><img src="{ASSETS}/tp_logo-white.svg" style="height:{logo_h}px;"><img src="{ASSETS}/tp_stars-5.svg" style="height:{star_h}px;"><span style="font-weight:800;">4.6/5</span></div>"""

def render_signature(b, w, h):
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4
    is_portrait  = ratio < 0.66
    edge = int(48 * s)
    photo = b["photo"]
    focus = b["focus"]

    longest_line = max((len(part) for part in b["headline"].replace("<br>", "\n").split("\n")), default=1)
    if is_landscape:
        hl_size = int((88 if longest_line <= 14 else 72 if longest_line <= 18 else 60) * s)
    elif is_portrait:
        hl_size = int((156 if longest_line <= 10 else 112 if longest_line <= 12 else 96 if longest_line <= 14 else 88) * s)
    else:
        hl_size = int((128 if longest_line <= 10 else 100 if longest_line <= 14 else 84) * s)

    if is_landscape:
        scrim_style = "background:linear-gradient(90deg, rgba(3,10,28,.92) 0%, rgba(3,10,28,.85) 38%, rgba(3,10,28,.55) 55%, rgba(3,10,28,.15) 75%, rgba(3,10,28,0) 100%);"
        content_box = f"left:{edge}px; width:{int(w*0.56)}px; top:{edge}px; bottom:{edge}px; display:flex; flex-direction:column;"
        brand_scale = 0.9
    else:
        scrim_style = "background:linear-gradient(180deg, rgba(3,10,28,0) 0%, rgba(3,10,28,.15) 30%, rgba(3,10,28,.65) 55%, rgba(3,10,28,.92) 80%, rgba(3,10,28,.98) 100%);"
        content_box = f"left:{edge}px; right:{edge}px; top:{edge}px; bottom:{edge}px; display:flex; flex-direction:column;"
        brand_scale = 1.1 if is_portrait else 1.0

    return f"""{html_head(w,h)}
<style>
{CTA_CSS}{TRUST_CSS}
.photobox {{ position:absolute; inset:0; overflow:hidden; z-index:1; background:{NAVY_DEEP}; }}
.photobox img {{ width:100%; height:100%; object-fit:cover; object-position:{focus}; }}
.scrim {{ position:absolute; inset:0; {scrim_style} z-index:2; }}
.topscrim {{ position:absolute; left:0; right:0; top:0; height:{int(240*s)}px; background:linear-gradient(180deg, rgba(3,10,28,.78) 0%, rgba(3,10,28,.5) 40%, rgba(3,10,28,.15) 75%, rgba(3,10,28,0) 100%); z-index:3; pointer-events:none; }}
.content {{ position:absolute; {content_box} z-index:5; }}
.brandwrap {{ flex-shrink:0; }}
.midspace {{ flex:1; }}
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.02; text-shadow:0 6px 40px rgba(0,0,0,.75); margin:0 0 {int(24*s)}px 0; letter-spacing:-.015em; }}
.credential-block {{ margin-bottom:{int(24*s)}px; }}
.cta-row {{ display:flex; align-items:center; justify-content:space-between; gap:{int(20*s)}px; flex-wrap:wrap; }}
.trust {{ background:transparent; padding:0; border:none; box-shadow:none; }}
</style>
<div class="canvas">
  <div class="photobox"><img src="{ASSETS}/{photo}"></div>
  <div class="scrim"></div>
  <div class="topscrim"></div>
  <div class="content">
    <div class="brandwrap">{brand_lockup(s, scale_mult=brand_scale)}</div>
    <div class="midspace"></div>
    {brand_text_lockup(s, is_landscape=is_landscape)}
    <div class="display headline">{b['headline']}</div>
    <div class="credential-block">{julie_credential(s, size_mult=(0.95 if is_landscape else 1.0))}</div>
    <div class="cta-row">
      {trust_row(s, size_mult=1.0)}
      {cta_button(s, b.get('cta','Enroll Now'))}
    </div>
  </div>
</div></body></html>"""


# The 6 chosen banners — order matches Omri's screenshots.
BANNERS = [
    {"id":"chosen_b1", "title":"Repeat It Until It's Automatic", "from":"V4 #9",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 10%",
     "headline":"Repeat it until<br>it&rsquo;s automatic.", "cta":"Join the Next Cohort"},
    {"id":"chosen_b2", "title":"Age Slower, Be There Longer", "from":"V3 #4",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%",
     "headline":"Age slower.<br>Be there longer.", "cta":"Enroll Now"},
    {"id":"chosen_b3", "title":"Eight Months per Year", "from":"V3 #6",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%",
     "headline":"&ldquo;For every year<br>that passes, I only<br>age eight months.&rdquo;", "cta":"Enroll Now"},
    {"id":"chosen_b4", "title":"Learn to Age a Third Slower", "from":"V3 #7",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%",
     "headline":"Learn to age<br>a third slower.", "cta":"Enroll Now"},
    {"id":"chosen_b5", "title":"Slow Your Pace of Aging", "from":"V3 #8",
     "photo":"real_julie-purple.jpg", "focus":"50% 24%",
     "headline":"Slow your<br>pace of aging.", "cta":"Enroll Now"},
    {"id":"chosen_b6", "title":"World's #2 Slowest Ager", "from":"V3 #9",
     "photo":"julie_real_1.jpg", "focus":"50% 30%",
     "headline":"Learn longevity<br>from the world&rsquo;s<br>#2 slowest ager.", "cta":"Enroll Now"},
]

manifest = {"chosen": []}
for b in BANNERS:
    item = {"id": b["id"], "title": b["title"], "layout": "signature", "sizes": {}}
    for size_key, size in SIZES.items():
        fn = f"{b['id']}_{size_key}.html"
        with open(f"{BANNERS_DIR}/{fn}", "w") as f:
            f.write(render_signature(b, size["w"], size["h"]))
        item["sizes"][size_key] = {
            "html": fn, "png": fn.replace(".html", ".png"),
            "w": size["w"], "h": size["h"], "label": size["label"], "note": size["note"],
        }
    manifest["chosen"].append(item)

with open(f"{BANNERS_DIR}/chosen_manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Wrote {len(BANNERS)*len(SIZES)} HTML files across {len(BANNERS)} banners x {len(SIZES)} sizes.")
