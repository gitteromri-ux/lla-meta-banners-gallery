#!/usr/bin/env python3
"""
Generate every banner in 4 Meta/IG ad sizes.
Strategy: define each banner as a small config, then render it responsively
into 4 target dimensions with layout adaptations (photo crop, type scale, brand bar position).
"""
import os, json
BANNERS_DIR = "/home/user/workspace/lla-gallery/banners"

# 4 Meta / IG ad sizes
SIZES = {
    "1x1":     {"w":1080, "h":1080, "label":"1:1 Feed",      "note":"Instagram Post / FB Feed Square"},
    "4x5":     {"w":1080, "h":1350, "label":"4:5 Vertical",  "note":"Instagram / FB Feed Vertical"},
    "9x16":    {"w":1080, "h":1920, "label":"9:16 Story",    "note":"IG Stories, Reels, FB Stories"},
    "191x1":   {"w":1200, "h":628,  "label":"1.91:1 Link",   "note":"FB Link Ad / Marketplace"},
}

# ---------------- BANNER CONFIGS ----------------
# Each banner: photo, photo_focus (x%,y% for object-position), headline (2 lines: roman + italic), version, notes
# H1 = big serif roman, H2 = big serif italic accent

BANNERS = {
    # ============= V1 (first delivery, no PR photos, generic layout) =============
    "v1": [
        {"id":"v1_b1", "title":"Make It Automatic",         "photo":None, "h1":"Make longevity",    "h2":"automatic.",          "focus":"50% 30%", "quote":False},
        {"id":"v1_b2", "title":"Willpower Fails",           "photo":None, "h1":"Willpower fails.",  "h2":"Habits don\u2019t.",  "focus":"50% 30%", "quote":False},
        {"id":"v1_b3", "title":"Sleep. Food. Movement.",    "photo":None, "h1":"Sleep. Food.",      "h2":"Movement.",           "focus":"50% 30%", "quote":False},
        {"id":"v1_b4", "title":"It\u2019s Being There",     "photo":None, "h1":"It\u2019s being",    "h2":"there.",              "focus":"50% 30%", "quote":False},
        {"id":"v1_b5", "title":"Stay Strong",               "photo":None, "h1":"Stay strong.",       "h2":"For them.",           "focus":"50% 30%", "quote":False},
        {"id":"v1_b6", "title":"He\u2019s My Son",          "photo":None, "h1":"He\u2019s",          "h2":"my son.",             "focus":"50% 30%", "quote":False},
    ],
    # ============= V2 (real PR Julie, credential lockup, luxury) =============
    "v2": [
        {"id":"v2_b1", "title":"8 Months per Year",         "photo":"real_julie-standing-hd.jpg", "focus":"52% 22%",
         "h1":"\u201cI only age",              "h2":"eight months.\u201d",  "quote":True},
        {"id":"v2_b2", "title":"Optimise Your Cells",       "photo":"real_julie-purple.jpg",      "focus":"50% 24%",
         "h1":"\u201cEat right. Move.",         "h2":"Optimise your cells.\u201d","quote":True},
        {"id":"v2_b3", "title":"Automatic Habits",          "photo":"real_julie-hero.jpg",        "focus":"75% 42%",
         "h1":"Make longevity",                 "h2":"automatic.",           "quote":False},
        {"id":"v2_b4", "title":"Willpower Fails",           "photo":"real_julie-purple.jpg",      "focus":"50% 24%",
         "h1":"Willpower fails.",               "h2":"Habits don\u2019t.",   "quote":False},
        {"id":"v2_b5", "title":"It\u2019s Being There",     "photo":"real_julie-standing-hd.jpg", "focus":"52% 22%",
         "h1":"It\u2019s not the years.",       "h2":"It\u2019s being there.","quote":False},
        {"id":"v2_b6", "title":"65 Days Younger",           "photo":"real_julie-standing-hd.jpg", "focus":"52% 22%",
         "h1":"65 days younger",                "h2":"every year.",          "quote":False},
    ],
    # ============= V3 (latest — brand bar layout, action CTAs) =============
    "v3": [
        {"id":"v3_b1", "title":"Make Longevity Automatic",  "photo":"real_julie-purple.jpg",      "focus":"50% 24%",
         "h1":"Make longevity",                 "h2":"automatic.",           "quote":False},
        {"id":"v3_b2", "title":"Outlast Willpower",         "photo":"real_julie-hero.jpg",        "focus":"75% 42%",
         "h1":"Build habits that",              "h2":"outlast willpower.",   "quote":False},
        {"id":"v3_b3", "title":"Good Night\u2019s Sleep",   "photo":"real_julie-purple.jpg",      "focus":"50% 24%",
         "h1":"\u201cYou cannot biohack a",     "h2":"good night\u2019s sleep.\u201d", "quote":True},
        {"id":"v3_b4", "title":"Age Slower",                "photo":"real_julie-standing-hd.jpg", "focus":"52% 22%",
         "h1":"Age slower.",                    "h2":"Be there longer.",     "quote":False},
        {"id":"v3_b5", "title":"Stay Strong",               "photo":"real_julie-standing-hd.jpg", "focus":"52% 22%",
         "h1":"Stay strong for the",            "h2":"people who need you.", "quote":False},
        {"id":"v3_b6", "title":"Eight Months per Year",     "photo":"real_julie-standing-hd.jpg", "focus":"52% 22%",
         "h1":"\u201cFor every year that passes,","h2":"I only age eight months.\u201d","quote":True},
        {"id":"v3_b7", "title":"Offer Panel",               "photo":"real_julie-standing-hd.jpg", "focus":"52% 22%",
         "h1":"Learn to age",                   "h2":"a third slower.",      "quote":False, "layout":"panel"},
        {"id":"v3_b8", "title":"Editorial Cover",           "photo":"real_julie-purple.jpg",      "focus":"50% 24%",
         "h1":"Slow your",                      "h2":"pace of aging.",       "quote":False, "layout":"cover"},
        {"id":"v3_b9", "title":"Gallery Arch",              "photo":"julie_real_1.jpg",           "focus":"50% 30%",
         "h1":"Learn longevity from",           "h2":"the world\u2019s #2 slowest ager.","quote":False, "layout":"arch"},
        {"id":"v3_b10","title":"Julie vs Bryan",            "photo":"julie_real_1.jpg",           "focus":"50% 30%",
         "h1":"Learn to slow your aging",       "h2":"by up to a third.",    "quote":False, "layout":"vs"},
    ],
}


def html_head(w, h):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ width:{w}px; height:{h}px; overflow:hidden; background:#020B1C; }}
.canvas {{ position:relative; width:{w}px; height:{h}px; background:#020B1C; font-family:'Inter',sans-serif; overflow:hidden; }}
.serif {{ font-family:'Instrument Serif',serif; font-weight:400; letter-spacing:-.01em; line-height:1.02; text-shadow:0 4px 24px rgba(0,0,0,.6); }}
.serif i {{ font-style:italic; color:#A9CFFF; }}
</style></head><body>"""


def scale_for(w, h, layout="standard"):
    """Return scale factors for this canvas so type/spacing feel right."""
    area = w * h
    base_area = 1080 * 1080
    # square root scale of area
    s = (area / base_area) ** 0.5
    # aspect for layout choices
    ratio = w / h
    return s, ratio


# ============================================================
# STANDARD LAYOUT (photo + bottom brand bar + headline + eyebrow + credential)
# used for v1, v2, v3 first-6 banners
# ============================================================

def render_standard(banner, size_key, w, h, version):
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4    # 1.91:1
    is_portrait  = ratio < 0.7    # 9:16
    is_v1_flat   = (banner.get("photo") is None)

    # sizes
    if is_landscape:
        bar_h = int(90 * s * 1.15)
    else:
        bar_h = int(148 * s)
    hl_size1 = int(88 * s * (0.85 if is_landscape else 1.0))
    hl_size2 = int(94 * s * (0.85 if is_landscape else 1.0))
    if banner.get("quote"):
        hl_size1 = int(hl_size1 * 0.78)
        hl_size2 = int(hl_size2 * 0.85)
    eyebrow_size = max(12, int(19 * s))
    cred_size    = max(12, int(16 * s))
    logo_h       = int(bar_h * 0.55)
    cta_font     = max(14, int(24 * s))
    cta_pad_v    = max(10, int(18 * s))
    cta_pad_h    = max(20, int(38 * s))
    edge_pad     = int(56 * s)

    # photo block
    if banner["photo"] and not is_v1_flat:
        # cover photo area = full canvas minus bar
        photo_area = f"""
<div class="photo">
  <img src="../../assets/{banner['photo']}" style="object-position:{banner['focus']};">
</div>"""
    else:
        # abstract gradient for v1
        photo_area = f"""
<div class="photo bg">
  <div class="orbit"></div>
</div>"""

    # scrim placement: for landscape put text on left, photo shifted right; for others bottom-left
    if is_landscape:
        text_style = f"left:{edge_pad}px; top:50%; transform:translateY(-50%); text-align:left; max-width:60%;"
        scrim_style = "background:linear-gradient(90deg, rgba(2,11,28,.94) 0%, rgba(2,11,28,.62) 40%, rgba(2,11,28,.08) 70%, rgba(2,11,28,0) 100%);"
    elif is_portrait:
        text_style = f"left:{edge_pad}px; right:{edge_pad}px; bottom:{bar_h + int(80*s)}px; text-align:left;"
        scrim_style = "background:linear-gradient(180deg, rgba(2,11,28,.25) 0%, rgba(2,11,28,0) 30%, rgba(2,11,28,0) 45%, rgba(2,11,28,.65) 70%, rgba(2,11,28,.95) 100%);"
    else:
        text_style = f"left:{edge_pad}px; right:{edge_pad}px; bottom:{bar_h + int(52*s)}px; text-align:left;"
        scrim_style = "background:linear-gradient(90deg, rgba(2,11,28,.88) 0%, rgba(2,11,28,.55) 42%, rgba(2,11,28,.12) 72%, rgba(2,11,28,0) 100%), linear-gradient(180deg, rgba(2,11,28,0) 60%, rgba(2,11,28,.5) 100%);"

    # credential (skip for v1)
    if version == "v1":
        credential_block = ""
    else:
        credential_block = f"""
<div class="cred" style="font-size:{cred_size}px; margin-top:{int(20*s)}px;">
  <span class="rule"></span>With <b>Julie Gibson Clark</b> \u2014 2nd Slowest-Aging Woman on Earth<br>
  <span class="f">Founding Faculty \u00b7 Longevity Life Academy</span>
</div>"""

    # trust in bar (skip for v1)
    if version == "v1":
        trust_block = ""
    else:
        tp_h = int(bar_h * 0.20)
        star_h = int(bar_h * 0.16)
        trust_block = f"""
<div class="r1">
  <img class="tpl" src="../../assets/tp_logo-white.svg" style="height:{tp_h}px;">
  <img class="tps" src="../../assets/tp_stars-5.svg" style="height:{star_h}px;">
  <span style="font-size:{max(10,int(bar_h*0.10))}px;">4.6 / 5 \u00b7 600+ verified reviews</span>
</div>"""

    r2_size = max(10, int(bar_h * 0.10))

    return f"""{html_head(w,h)}
<style>
.photo {{ position:absolute; left:0; right:0; top:0; bottom:{bar_h}px; overflow:hidden; }}
.photo img {{ width:100%; height:100%; object-fit:cover; }}
.photo.bg {{ background:radial-gradient(1200px 800px at 30% 40%, #0A2450 0%, #020B1C 65%); }}
.photo.bg .orbit {{ position:absolute; inset:0; background:radial-gradient(circle at 50% 45%, rgba(0,110,255,.12) 0%, transparent 50%); }}
.scrim {{ position:absolute; left:0; right:0; top:0; bottom:{bar_h}px; {scrim_style} }}
.content {{ position:absolute; z-index:5; {text_style} color:#fff; }}
.eyebrow {{ display:flex; align-items:center; gap:{max(6,int(10*s))}px; margin-bottom:{int(18*s)}px; }}
.eyebrow .dot {{ width:{max(6,int(9*s))}px; height:{max(6,int(9*s))}px; border-radius:50%; background:#E8A75A; box-shadow:0 0 12px rgba(232,167,90,.9); }}
.eyebrow .txt {{ font-size:{eyebrow_size}px; font-weight:700; letter-spacing:.22em; text-transform:uppercase; text-shadow:0 1px 8px rgba(0,0,0,.7); }}
.eyebrow .txt b {{ color:#7EC8FF; font-weight:700; }}
.cred {{ color:#fff; font-weight:700; text-transform:uppercase; letter-spacing:.13em; line-height:1.7; text-shadow:0 1px 8px rgba(0,0,0,.8); }}
.cred .rule {{ display:inline-block; width:{int(28*s)}px; height:{max(2,int(3*s))}px; background:#E8A75A; vertical-align:middle; margin-right:{int(12*s)}px; border-radius:2px; }}
.cred b {{ color:#E8A75A; }}
.cred .f {{ color:#A9CFFF; font-weight:600; letter-spacing:.11em; }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:linear-gradient(180deg,#03132E 0%,#010B1E 100%); border-top:1px solid rgba(232,167,90,.55); display:flex; align-items:center; padding:0 {int(36*s)}px; z-index:20; gap:{int(20*s)}px; }}
.bar .logo img {{ height:{logo_h}px; display:block; }}
.bar .mid {{ margin:0 auto; display:flex; flex-direction:column; align-items:center; gap:{max(4,int(6*s))}px; color:#fff; text-align:center; }}
.bar .mid .r1 {{ display:flex; align-items:center; gap:{max(4,int(8*s))}px; color:rgba(255,255,255,.85); font-weight:600; }}
.bar .mid .r2 {{ font-size:{r2_size}px; font-weight:500; color:rgba(255,255,255,.6); letter-spacing:.04em; }}
.cta {{ display:inline-flex; align-items:center; gap:{max(6,int(10*s))}px; background:linear-gradient(135deg,#3A8DFF 0%,#006EFF 100%); color:#fff; font-weight:800; font-size:{cta_font}px; padding:{cta_pad_v}px {cta_pad_h}px; border-radius:999px; border:1px solid rgba(255,255,255,.5); box-shadow:0 6px 24px rgba(0,110,255,.5), inset 0 1px 0 rgba(255,255,255,.3); white-space:nowrap; font-family:'Inter',sans-serif; }}
</style>
<div class="canvas">
  {photo_area}
  <div class="scrim"></div>
  <div class="content">
    <div class="eyebrow"><span class="dot"></span><span class="txt">The Longevity Masterclass <b>\u00b7 100% Online</b></span></div>
    <div class="serif" style="font-size:{hl_size1}px; color:#fff;">{banner['h1']}</div>
    <div class="serif" style="font-size:{hl_size2}px;"><i>{banner['h2']}</i></div>
    {credential_block}
  </div>
  <div class="bar">
    <div class="logo"><img src="../../assets/lla_logo.png"></div>
    <div class="mid">
      {trust_block}
      <div class="r2">18 Live Sessions \u00b7 longevitylifeacademy.com</div>
    </div>
    <span class="cta">Enroll Now <span>\u2192</span></span>
  </div>
</div></body></html>"""


# ============================================================
# ALT LAYOUTS FOR V3 (panel, cover, arch, vs)
# For simplicity in gallery: render standard layout for these too, but with layout tag suffix.
# For the vs one, keep a compact panel style.
# ============================================================

def render_vs(banner, size_key, w, h):
    """Julie vs Bryan comparison — adapts side-by-side to landscape and stacked to portrait."""
    s, ratio = scale_for(w, h)
    stacked = (ratio < 1.0)  # portrait or square → stacked
    is_landscape = ratio > 1.4

    edge = int(40 * s)
    bar_h = int(90 * s * 1.15) if is_landscape else int(148 * s)
    logo_h = int(bar_h * 0.55)

    title_h1 = int(64 * s * (0.85 if is_landscape else 1.0))
    title_h2 = int(70 * s * (0.85 if is_landscape else 1.0))

    if stacked:
        cards_style = f"flex-direction:column; gap:{int(18*s)}px;"
    else:
        cards_style = f"flex-direction:row; gap:{int(20*s)}px;"

    return f"""{html_head(w,h)}
<style>
.canvas {{ background:radial-gradient(1100px 600px at 50% -10%, #0A2450 0%, #020B1C 55%); }}
.frame {{ position:absolute; inset:{int(20*s)}px; border:1px solid rgba(232,167,90,.4); z-index:1; pointer-events:none; }}
.top {{ position:absolute; left:{edge}px; right:{edge}px; top:{int(38*s)}px; text-align:center; color:#fff; z-index:3; }}
.top .eyebrow {{ display:flex; align-items:center; justify-content:center; gap:{int(10*s)}px; margin-bottom:{int(14*s)}px; }}
.top .eyebrow .dot {{ width:{max(6,int(9*s))}px; height:{max(6,int(9*s))}px; border-radius:50%; background:#E8A75A; box-shadow:0 0 12px rgba(232,167,90,.9); }}
.top .eyebrow span.txt {{ font-size:{max(11,int(17*s))}px; font-weight:700; letter-spacing:.22em; text-transform:uppercase; }}
.top .eyebrow span.txt b {{ color:#7EC8FF; }}
.cards {{ position:absolute; left:{edge}px; right:{edge}px; top:{int(230*s)}px; bottom:{bar_h + int(40*s)}px; display:flex; {cards_style} }}
.card {{ flex:1; border-radius:{int(14*s)}px; padding:{int(24*s)}px; position:relative; color:#fff; overflow:hidden; }}
.card.julie {{ background:linear-gradient(165deg,#06234E 0%,#031534 70%); border:1.5px solid rgba(126,200,255,.6); box-shadow:0 12px 40px rgba(0,110,255,.28); }}
.card.bryan {{ background:linear-gradient(165deg,#101722 0%,#0A0F16 70%); border:1px solid rgba(255,255,255,.14); color:rgba(255,255,255,.7); }}
.card .rank {{ font-size:{max(10,int(13*s))}px; font-weight:800; letter-spacing:.14em; text-transform:uppercase; }}
.card.julie .rank {{ color:#E8A75A; }} .card.bryan .rank {{ color:rgba(255,255,255,.4); }}
.stat {{ margin-top:{int(14*s)}px; padding:{int(12*s)}px {int(16*s)}px; border-radius:{int(10*s)}px; }}
.card.julie .stat {{ background:rgba(0,110,255,.16); border:1px solid rgba(126,200,255,.35); }}
.card.bryan .stat {{ background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); }}
.stat .v {{ font-family:'Instrument Serif',serif; font-size:{int(36*s)}px; line-height:1; }}
.stat .k {{ font-size:{max(10,int(12*s))}px; font-weight:700; letter-spacing:.09em; text-transform:uppercase; margin-top:{int(6*s)}px; }}
.card.julie .stat .k {{ color:#A9CFFF; }} .card.bryan .stat .k {{ color:rgba(255,255,255,.4); }}
.lst {{ margin-top:{int(14*s)}px; display:flex; flex-direction:column; gap:{int(9*s)}px; }}
.lst .i {{ font-size:{max(12,int(16*s))}px; font-weight:600; }}
.card.julie .lst .i .m {{ color:#E8A75A; font-weight:800; margin-right:{int(8*s)}px; }}
.card.bryan .lst .i .m {{ color:rgba(255,255,255,.35); font-weight:800; margin-right:{int(8*s)}px; }}
.cost {{ margin-top:{int(12*s)}px; display:inline-block; padding:{int(7*s)}px {int(13*s)}px; border-radius:999px; font-size:{max(11,int(14*s))}px; font-weight:800; background:rgba(232,167,90,.14); border:1px solid rgba(232,167,90,.55); color:#E8A75A; }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:linear-gradient(180deg,#03132E 0%,#010B1E 100%); border-top:1px solid rgba(232,167,90,.55); display:flex; align-items:center; padding:0 {int(36*s)}px; z-index:20; gap:{int(20*s)}px; }}
.bar .logo img {{ height:{logo_h}px; display:block; }}
.bar .mid {{ margin:0 auto; display:flex; flex-direction:column; align-items:center; gap:{max(4,int(6*s))}px; color:#fff; text-align:center; font-size:{max(10,int(bar_h*0.10))}px; }}
.bar .mid .r1 {{ display:flex; align-items:center; gap:{max(4,int(8*s))}px; color:rgba(255,255,255,.85); font-weight:600; }}
.bar .mid .r1 img {{ height:{int(bar_h*0.18)}px; }}
.cta {{ display:inline-flex; align-items:center; gap:{max(6,int(10*s))}px; background:linear-gradient(135deg,#3A8DFF 0%,#006EFF 100%); color:#fff; font-weight:800; font-size:{max(14,int(22*s))}px; padding:{max(10,int(16*s))}px {max(22,int(34*s))}px; border-radius:999px; border:1px solid rgba(255,255,255,.5); box-shadow:0 6px 24px rgba(0,110,255,.5); white-space:nowrap; }}
</style>
<div class="canvas">
  <div class="frame"></div>
  <div class="top">
    <div class="eyebrow"><span class="dot"></span><span class="txt">The Longevity Masterclass <b>\u00b7 100% Online</b></span></div>
    <div class="serif" style="font-size:{title_h1}px; color:#fff;">Learn to slow your aging</div>
    <div class="serif" style="font-size:{title_h2}px;"><i>by up to a third.</i></div>
    <div style="margin-top:{int(10*s)}px; font-size:{max(11,int(14*s))}px; color:rgba(255,255,255,.85); letter-spacing:.11em; text-transform:uppercase;">Taught by <b style="color:#E8A75A;">Julie Gibson Clark</b> \u2014 her real, measured result</div>
  </div>
  <div class="cards">
    <div class="card julie">
      <div class="rank">\u2605 Ranked #2 in the World \u00b7 Rejuvenation Olympics</div>
      <div class="stat"><div class="v">0.665 <span style="font-size:{int(19*s)}px;">pace of aging</span></div><div class="k">\u2248 8 months of aging per year \u00b7 DunedinPACE</div></div>
      <div class="lst">
        <div class="i"><span class="m">\u2014</span>Your full personalized protocol</div>
        <div class="i"><span class="m">\u2014</span>Sleep \u2014 the true non-negotiable</div>
        <div class="i"><span class="m">\u2014</span>Nutrition &amp; daily eating rhythm</div>
        <div class="i"><span class="m">\u2014</span>VO\u2082 max cardio &amp; strength training</div>
      </div>
      <div class="cost">Tuition from $360/mo \u2014 not $2M a year</div>
    </div>
    <div class="card bryan">
      <div class="rank">Ranked Below Julie \u00b7 2023 Leaderboard</div>
      <div class="stat"><div class="v">~$2M <span style="font-size:{int(19*s)}px;">a year</span></div><div class="k">The cost of chasing the same goal</div></div>
      <div class="lst">
        <div class="i"><span class="m">\u2014</span>100+ supplements a day</div>
        <div class="i"><span class="m">\u2014</span>A team of 30+ doctors</div>
        <div class="i"><span class="m">\u2014</span>A full-time longevity operation</div>
        <div class="i"><span class="m">\u2014</span>Results she beat \u2014 on fundamentals</div>
      </div>
    </div>
  </div>
  <div class="bar">
    <div class="logo"><img src="../../assets/lla_logo.png"></div>
    <div class="mid">
      <div class="r1"><img src="../../assets/tp_logo-white.svg"><img src="../../assets/tp_stars-5.svg"><span>4.6 / 5 \u00b7 600+ reviews</span></div>
      <div style="font-size:{max(10,int(bar_h*0.10))}px; color:rgba(255,255,255,.6);">longevitylifeacademy.com</div>
    </div>
    <span class="cta">Enroll Now \u2192</span>
  </div>
</div></body></html>"""


# ---------------- WRITE ALL HTML FILES ----------------
manifest = {}
for version, banners in BANNERS.items():
    manifest[version] = []
    for b in banners:
        item = {"id": b["id"], "title": b["title"], "sizes": {}}
        for size_key, size in SIZES.items():
            fn = f"{b['id']}_{size_key}.html"
            path = f"{BANNERS_DIR}/{version}/{fn}"
            if b.get("layout") == "vs":
                html = render_vs(b, size_key, size["w"], size["h"])
            else:
                html = render_standard(b, size_key, size["w"], size["h"], version)
            with open(path, "w") as f:
                f.write(html)
            item["sizes"][size_key] = {
                "html": fn,
                "png": fn.replace(".html", ".png"),
                "w": size["w"], "h": size["h"],
                "label": size["label"],
                "note": size["note"],
            }
        manifest[version].append(item)

with open(f"{BANNERS_DIR}/../manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

total = sum(len(v)*len(SIZES) for v in BANNERS.values())
print(f"Wrote {total} banner HTML files across {sum(len(v) for v in BANNERS.values())} banners × {len(SIZES)} sizes.")
