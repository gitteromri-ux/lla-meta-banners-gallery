#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PREMIUM REBUILD — mirrors the client-approved Courtney luxury editorial system:
- EB Garamond (premium serif) display, Inter for functional text. NO Playfair.
- Fonts significantly larger throughout.
- Course info NEVER a dash/dot-delimited text list — glowing benefit lines
  in the approved Courtney "facts" treatment.
- Correct course name: The Longevity Blueprint (not "Masterclass").
- "2nd slowest-aging person on Earth." = first glowing fact line, large.
- Trustpilot wordmark logo + 5 stars + 4.6/5, placed BELOW the CTA.
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = "../../assets"

SIZES = {
    "1x1":   {"w":1080, "h":1080, "label":"1:1 Feed",     "note":"Instagram Post / FB Feed Square"},
    "4x5":   {"w":1080, "h":1350, "label":"4:5 Vertical", "note":"Instagram / FB Feed Vertical"},
    "9x16":  {"w":1080, "h":1920, "label":"9:16 Story",   "note":"IG Stories, Reels, FB Stories"},
    "191x1": {"w":1200, "h":628,  "label":"1.91:1 Link",  "note":"FB Link Ad / Marketplace"},
}

FONT_LINK = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

NAVY_DEEP  = "#060b20"
NAVY_BAR   = "#03102a"
BLUE       = "#006EFF"
ICE        = "#9cc3ef"   # approved eyebrow / italic accent
GLOW       = "#8ff2ff"   # approved glowing facts color

FACT_CRED   = "2nd slowest-aging person on Earth."
FACT_COURSE = "The Longevity Blueprint. 18 live sessions. 100% online."

GLOW_SHADOW = ("text-shadow:0 0 6px rgba(127,231,255,.9),0 0 14px rgba(127,231,255,.7),"
               "0 0 28px rgba(90,190,255,.55),0 0 52px rgba(60,150,235,.35),0 2px 8px rgba(2,6,20,.55);")

def html_head(w, h):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
{FONT_LINK}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ width:{w}px; height:{h}px; overflow:hidden; background:{NAVY_DEEP}; -webkit-font-smoothing:antialiased; }}
.canvas {{ position:relative; width:{w}px; height:{h}px; background:{NAVY_DEEP}; font-family:'Inter',sans-serif; overflow:hidden; }}
.display {{ font-family:'EB Garamond',serif; font-weight:600; letter-spacing:-.012em; }}
</style></head><body>"""

def scale_for(w, h):
    area = w * h
    s = (area / (1080*1080)) ** 0.5
    return s, w / h

def brand_lockup(s, align="left", scale_mult=None):
    justify = "flex-start" if align == "left" else "center"
    style = f"height:{int(160*s*scale_mult)}px; display:block;" if scale_mult else "display:block;"
    return f"""
<div class="brandlock" style="display:flex; align-items:center; justify-content:{justify};">
  <img src="{ASSETS}/lla_logo.png" style="{style} filter:drop-shadow(0 2px 10px rgba(0,0,0,.35));">
</div>"""

def styled_headline(headline, italic_last=True):
    """Approved treatment: last headline line in italic ice-blue Garamond."""
    parts = headline.split("<br>")
    if len(parts) < 2 or not italic_last:
        return headline
    last = f'<span style="font-style:italic; font-weight:500; color:#b9d4f2;">{parts[-1]}</span>'
    return "<br>".join(parts[:-1] + [last])

GOLD = "#dcbf85"

def cred_line(s, mult=1.0, fs=None):
    fs = fs or max(24, int(38 * s * mult))
    return (f'<div style="font-family:\'EB Garamond\',serif; font-style:italic; font-weight:500; '
            f'font-size:{fs}px; color:rgba(232,241,252,.92); line-height:1.3;">'
            f'<span style="font-weight:700; font-style:normal; color:#ffffff;">Julie Gibson Clark</span>, '
            f'Longevity Life Academy Instructor</div>')

def credential_gold(fs, two_line=False):
    """Julie's authority credential — distinct gold serif treatment (NOT course info)."""
    text = '2nd Slowest-Aging<br>Person on Earth' if two_line else '2nd Slowest-Aging Person on Earth'
    return (f'<div style="font-family:\'EB Garamond\',serif; font-style:italic; font-weight:600; '
            f'font-size:{fs}px; color:{GOLD}; line-height:1.18; letter-spacing:.005em;">'
            f'<span style="font-style:normal;">&#9733;</span>&nbsp; {text}</div>')

def course_block(title_fs, chip_fs, gap):
    """Course info — clearly separated: course name + pill chips. Never a text list."""
    pad_v = int(chip_fs * 0.50); pad_h = int(chip_fs * 0.95)
    chips = "".join(
        f'<span style="display:inline-flex; align-items:center; padding:{pad_v}px {pad_h}px; '
        f'border-radius:9999px; background:rgba(0,110,255,.16); border:1.5px solid rgba(156,195,239,.55); '
        f'color:#eaf2fc; font-weight:700; font-size:{chip_fs}px; letter-spacing:.01em; white-space:nowrap;">{c}</span>'
        for c in ["18 Live Sessions", "100% Online"])
    return (f'<div style="display:flex; flex-direction:column; gap:{int(gap*0.7)}px;">'
            f'<div style="font-family:\'Inter\',sans-serif; font-weight:800; font-size:{title_fs}px; '
            f'color:#ffffff; letter-spacing:-.01em; line-height:1.08; white-space:nowrap;">The Longevity Blueprint</div>'
            f'<div style="display:flex; flex-wrap:nowrap; gap:{int(gap*0.75)}px;">{chips}</div></div>')

def cta_button(s, text="Enroll Now", mult=1.0, fs=None):
    fs = fs or max(24, int(36 * s * mult))
    pad_v = max(14, int(fs * 0.68))
    pad_h = max(30, int(fs * 1.6))
    return (f'<span style="display:inline-flex; align-items:center; justify-content:center; white-space:nowrap; '
            f'background:{BLUE}; color:#ffffff; '
            f"font-family:'Inter',sans-serif; font-weight:700; font-size:{fs}px; letter-spacing:.12em; "
            f'text-transform:uppercase; padding:{pad_v}px {pad_h}px; border-radius:9999px; '
            f'box-shadow:0 12px 34px rgba(0,60,160,.45);">{text}</span>')

def trust_row(s, mult=1.0, fs=None):
    base = fs or int(30*s*mult)
    logo_h = max(24, int(base*1.4))
    star_h = max(22, int(base*1.2))
    f2 = max(18, base)
    gap = max(10, int(base*0.55))
    return (f'<div style="display:flex; align-items:center; gap:{gap}px; font-size:{f2}px; color:rgba(240,246,253,.94); font-weight:600; white-space:nowrap;">'
            f'<img src="{ASSETS}/tp_logo-white.svg" style="height:{logo_h}px; display:block;">'
            f'<img src="{ASSETS}/tp_stars-5.svg" style="height:{star_h}px; display:block;">'
            f'<span style="font-weight:700;">4.6/5</span></div>')


# ============================================================
# SIGNATURE — SPLIT PANEL: text on one side, Julie fully visible on the other
# ============================================================
def render_signature(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4
    is_portrait  = ratio < 0.66

    text_frac = 0.55 if is_landscape else 0.58
    tw = int(w * text_frac)
    edge = int(56 * s) if not is_landscape else int(48 * s)
    top_pad = int(120 * s) if size_key == "9x16" else edge
    bot_pad = int(150 * s) if size_key == "9x16" else edge
    inner = tw - 2 * edge

    # ---- headline: as large as fits the panel width
    import html as _h
    plain = b["headline"].replace("<br>", "\n")
    for ent, ch in [("&rsquo;","'"),("&ldquo;",'"'),("&rdquo;",'"'),("&amp;","&")]:
        plain = plain.replace(ent, ch)
    longest = max((len(l) for l in plain.split("\n")), default=1)
    hl_cap = (96 if is_landscape else 150) * s
    hl_size = int(min(hl_cap, inner / (longest * 0.44)))

    # ---- per-format stack sizing (everything fits, no overflow)
    if is_landscape:
        logo_h   = int(100 * s)
        eyebrow_fs = 0                      # dropped on landscape (approved pattern)
        name_fs  = min(int(26*s), int(inner / (54*0.52)))
        gold_fs  = min(int(30*s), int(inner / (36*0.44)))
        title_fs = int(30*s)
        chip_fs  = min(int(26*s), int((inner-16) / 19.7))
        cta_fs   = int(26*s)
        trust_fs = int(22*s)
        gap      = int(14*s)
        cta_row  = True
    elif is_portrait:
        logo_h   = int(190 * s)
        eyebrow_fs = min(int(38*s), int(inner / (28*0.5)))
        name_fs  = min(int(38*s), int(inner / (28*0.52)))
        gold_fs  = min(int(52*s), int(inner / (20*0.46)))
        title_fs = min(int(50*s), int(inner / (23*0.52)))
        chip_fs  = min(int(34*s), int((inner-16) / 19.7))
        cta_fs   = int(34*s)
        trust_fs = int(26*s)
        gap      = int(26*s)
        cta_row  = False
    else:
        logo_h   = int(140 * s)
        eyebrow_fs = min(int(34*s), int(inner / (28*0.5)))
        name_fs  = int(32*s)
        gold_fs  = min(int(44*s), int(inner / (20*0.46)))
        title_fs = min(int(42*s), int(inner / (23*0.52)))
        chip_fs  = min(int(30*s), int((inner-16) / 19.7))
        cta_fs   = int(32*s)
        trust_fs = int(24*s)
        gap      = int(20*s)
        cta_row  = False

    gold_two_line = (36 * 0.44 * gold_fs) > inner
    eyebrow = "" if not eyebrow_fs else (
        f'<div style="font-family:\'EB Garamond\',serif; font-style:italic; font-weight:500; '
        f'font-size:{eyebrow_fs}px; color:{ICE}; margin-top:{int(18*s)}px; white-space:nowrap;">Live Online Longevity Course</div>')

    if cta_row:
        ctablock = (f'<div class="ctablock" style="display:flex; flex-direction:row; align-items:center; gap:{int(24*s)}px;">'
                    f'{cta_button(s, b.get("cta","Enroll Now"), fs=cta_fs)}{trust_row(s, fs=trust_fs)}</div>')
    else:
        ctablock = (f'<div class="ctablock" style="display:flex; flex-direction:column; align-items:flex-start; gap:{int(18*s)}px;">'
                    f'{cta_button(s, b.get("cta","Enroll Now"), fs=cta_fs)}{trust_row(s, fs=trust_fs)}</div>')

    photo = b["photo"]; focus = b["focus"]

    return f"""{html_head(w,h)}
<style>
.canvas {{ display:flex; flex-direction:row; }}
.textpanel {{ width:{tw}px; height:{h}px; flex-shrink:0; position:relative; z-index:5;
  background:linear-gradient(160deg, #0a1430 0%, {NAVY_DEEP} 55%, #04081a 100%);
  padding:{top_pad}px {edge}px {bot_pad}px {edge}px; display:flex; flex-direction:column; }}
.photopanel {{ position:relative; flex:1; height:{h}px; overflow:hidden; background:{NAVY_DEEP}; }}
.photopanel img {{ width:100%; height:100%; object-fit:cover; object-position:{focus}; display:block; }}
.photopanel .blend {{ position:absolute; inset:0; background:linear-gradient(90deg, {NAVY_DEEP} 0%, rgba(6,11,32,.35) 10%, rgba(6,11,32,0) 26%); pointer-events:none; }}
.brandlock img {{ height:{logo_h}px; max-width:{inner}px; object-fit:contain; object-position:left center; display:block; }}
.headline {{ font-size:{hl_size}px; color:#f5f8fc; line-height:1.02; margin:0; }}
.stack {{ display:flex; flex-direction:column; gap:{gap}px; }}
</style>
<div class="canvas">
  <div class="textpanel">
    <div style="flex-shrink:0;">
      {brand_lockup(s, align="left")}
      {eyebrow}
    </div>
    <div style="flex:1; min-height:{int(24*s)}px;"></div>
    <div class="stack">
      <div class="display headline">{styled_headline(b['headline'])}</div>
      <div>{cred_line(s, fs=name_fs)}</div>
      <div>{credential_gold(gold_fs, two_line=gold_two_line)}</div>
      <div>{course_block(title_fs, chip_fs, gap)}</div>
      {ctablock}
    </div>
  </div>
  <div class="photopanel"><img src="{ASSETS}/{photo}"><div class="blend"></div></div>
</div></body></html>"""


# ============================================================
# VERSUS — Julie vs Bryan Johnson (premium serif + approved bar)
# ============================================================
def render_versus(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    stacked = ratio < 1.05
    edge = int(44 * s)
    bar_h = int(190 * s) if not ratio > 1.4 else int(150 * s)
    top_h = int(310 * s) if not stacked else int(340*s)
    hl_size = int(56 * s)
    side_h = (h - top_h - bar_h) / (2 if stacked else 1)
    side_w = w if stacked else w / 2
    container_ratio = side_w / side_h
    if container_ratio >= 2.6:
        bryan_pos = "50% 38%"
    elif container_ratio >= 1.6:
        bryan_pos = "50% 45%"
    else:
        bryan_pos = "50% 55%"

    split_style = "flex-direction:column;" if stacked else "flex-direction:row;"
    bar_landscape = ratio > 1.4
    fact_fs = max(18, int(26*s*(0.9 if bar_landscape else 1.0)))

    if bar_landscape:
        bar_inner = (f'<div style="display:flex; flex-direction:column; gap:{int(10*s)}px;">'
                     f'<div style="font-weight:700; font-size:{fact_fs}px; color:{GLOW}; {GLOW_SHADOW}">{FACT_COURSE}</div>'
                     f'{trust_row(s, mult=0.82)}</div>'
                     f'{cta_button(s, b.get("cta","Enroll Now"), mult=0.78)}')
        bar_flex = "flex-direction:row; align-items:center; justify-content:space-between;"
    else:
        bar_inner = (f'<div style="font-weight:700; font-size:{fact_fs}px; color:{GLOW}; {GLOW_SHADOW}">{FACT_COURSE}</div>'
                     f'<div style="display:flex; align-items:center; justify-content:space-between; width:100%; gap:{int(16*s)}px;">'
                     f'{trust_row(s, mult=0.9)}{cta_button(s, b.get("cta","Enroll Now"), mult=0.85)}</div>')
        bar_flex = "flex-direction:column; align-items:flex-start; justify-content:center;"

    return f"""{html_head(w,h)}
<style>
.top {{ position:absolute; left:{edge}px; right:{edge}px; top:{int(38*s)}px; z-index:10; }}
.headline {{ font-size:{hl_size}px; color:#f5f8fc; line-height:1.04; text-align:center; margin-top:{int(20*s)}px; text-shadow:0 5px 34px rgba(2,6,20,.65); }}
.split {{ position:absolute; left:0; right:0; top:{top_h}px; bottom:{bar_h}px; display:flex; {split_style} }}
.side {{ position:relative; flex:1; overflow:hidden; }}
.side img {{ width:100%; height:100%; object-fit:cover; }}
.side.julie img {{ object-position:52% 20%; }}
.side.bryan img {{ object-position:{bryan_pos}; filter:grayscale(0.45) brightness(0.85); }}
.tag {{ position:absolute; left:{int(24*s)}px; top:{int(24*s)}px; padding:{int(9*s)}px {int(18*s)}px; border-radius:999px; font-weight:700; font-size:{max(14,int(19*s))}px; letter-spacing:.02em; z-index:5; }}
.tag.julie {{ background:{BLUE}; color:#fff; }}
.tag.bryan {{ background:rgba(255,255,255,.18); color:#fff; border:1px solid rgba(255,255,255,.4); }}
.statpanel {{ position:absolute; left:0; right:0; bottom:0; padding:{int(22*s)}px {int(24*s)}px; z-index:5; }}
.side.julie .statpanel {{ background:linear-gradient(180deg, transparent, rgba(3,14,40,.96) 55%); }}
.side.bryan .statpanel {{ background:linear-gradient(180deg, transparent, rgba(10,10,12,.96) 55%); }}
.bigstat {{ font-family:'EB Garamond',serif; font-weight:600; font-size:{int(52*s)}px; color:#fff; line-height:1; }}
.bigstat span {{ font-family:'Inter',sans-serif; font-size:{max(15,int(20*s))}px; font-weight:700; color:rgba(255,255,255,.88); margin-left:{int(8*s)}px; }}
.statlabel {{ font-size:{max(13,int(16*s))}px; color:{ICE}; font-weight:600; margin-top:{int(5*s)}px; }}
.side.bryan .statlabel {{ color:rgba(255,255,255,.55); }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:{NAVY_BAR}; border-top:1px solid rgba(156,195,239,.3); display:flex; {bar_flex} padding:{int(16*s)}px {int(40*s)}px; z-index:20; gap:{int(12*s)}px; }}
</style>
<div class="canvas">
  <div class="top">
    {brand_lockup(s, align="center", scale_mult=0.9)}
    <div class="display headline">She Beats Bryan Johnson.<br><span style="font-style:italic; font-weight:500; color:#b9d4f2;">For $289/mo.</span></div>
  </div>
  <div class="split">
    <div class="side julie">
      <img src="{ASSETS}/real_julie-standing-hd.jpg">
      <div class="tag julie">JULIE GIBSON CLARK</div>
      <div class="statpanel">
        <div class="bigstat">#2 <span>slowest-aging person on Earth</span></div>
        <div class="statlabel">Rejuvenation Olympics leaderboard</div>
      </div>
    </div>
    <div class="side bryan">
      <img src="{ASSETS}/bryan_johnson.jpg">
      <div class="tag bryan">BRYAN JOHNSON</div>
      <div class="statpanel">
        <div class="bigstat">$2M <span>spent per year</span></div>
        <div class="statlabel">Ranked below Julie on the same board</div>
      </div>
    </div>
  </div>
  <div class="bar">
    {bar_inner}
  </div>
</div></body></html>"""


# ---------------- ALL BANNERS, ALL VERSIONS ----------------
exec(open(os.path.join(ROOT, "banner_defs.py")).read())

total = 0
for version, banners in VERSIONS.items():
    out_dir = os.path.join(ROOT, "banners", version)
    os.makedirs(out_dir, exist_ok=True)
    for b in banners:
        renderer = render_versus if b.get("layout") == "versus" else render_signature
        for size_key, size in SIZES.items():
            fn = f"{b['id']}_{size_key}.html"
            html = renderer(b, size_key, size["w"], size["h"])
            with open(os.path.join(out_dir, fn), "w") as f:
                f.write(html)
            total += 1
print(f"Wrote {total} HTML files.")
