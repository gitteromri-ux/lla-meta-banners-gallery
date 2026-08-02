#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIXED REBUILD — client corrections (banners-fixes.docx):
1. EVERY banner uses the approved reference layout (V7 signature full-bleed):
   big LLA lockup, big serif headline, Julie's name, credential, course info,
   Trustpilot proof, CTA — all present on ALL banners.
2. Trustpilot now shows the official Trustpilot WORDMARK LOGO (not stars only).
3. "2nd Slowest-Aging Person on Earth" enlarged — now a prominent line.
Applies to v1, v2, v3, v4, v6, v7 and chosen. Versus banners keep the
comparison layout but get the full trust/course-info bar.
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
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">"""

NAVY_DEEP  = "#050E22"
NAVY_BAR   = "#03102A"
BLUE       = "#006EFF"
BLUE_LT    = "#7EC8FF"
WHITE      = "#FFFFFF"

COURSE_INFO = "The Longevity Masterclass &middot; 18 Live Sessions &middot; 100% Online"

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
    return s, w / h

def brand_lockup(s, align="left", scale_mult=1.0):
    logo_h = int(150 * s * scale_mult)
    justify = "flex-start" if align == "left" else "center"
    return f"""
<div class="brandlock" style="display:flex; align-items:center; justify-content:{justify};">
  <img src="{ASSETS}/lla_logo.png" style="height:{logo_h}px; display:block; filter:drop-shadow(0 2px 10px rgba(0,0,0,.35));">
</div>"""

def julie_credential(s, size_mult=1.0):
    """FIX: name + credential enlarged. '2nd Slowest-Aging Person on Earth'
    is now a prominent, bold, clearly visible line."""
    name_size = max(18, int(30 * s * size_mult))
    cred_size = max(16, int(27 * s * size_mult))   # was 16*s — now ~1.7x
    tag_size  = max(13, int(18 * s * size_mult))
    return f"""
<div style="display:flex; flex-direction:column; align-items:flex-start; text-align:left; gap:{max(3,int(5*s))}px;">
  <div style="font-weight:800; font-size:{name_size}px; color:{WHITE}; text-shadow:0 2px 14px rgba(0,0,0,.6);">Julie Gibson Clark</div>
  <div style="font-weight:800; font-size:{cred_size}px; color:{BLUE_LT}; letter-spacing:.005em; line-height:1.2; text-shadow:0 2px 14px rgba(0,0,0,.6);">2nd Slowest-Aging Person on Earth</div>
  <div style="font-weight:600; font-size:{tag_size}px; color:rgba(191,224,255,.95); letter-spacing:.01em; line-height:1.3;">Longevity Life Academy Instructor</div>
</div>"""

def course_info(s, size_mult=1.0):
    fs = max(14, int(19 * s * size_mult))
    return f"""<div style="font-weight:700; font-size:{fs}px; color:rgba(255,255,255,.94); letter-spacing:.01em; line-height:1.35; text-shadow:0 2px 12px rgba(0,0,0,.6);">{COURSE_INFO}</div>"""

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

def trust_row(s, size_mult=1.0):
    """FIX: official Trustpilot wordmark logo + 5 green stars + rating."""
    logo_h = max(18, int(28*s*size_mult))
    star_h = max(16, int(24*s*size_mult))
    fs = max(14, int(20*s*size_mult))
    gap = max(8, int(12*s*size_mult))
    return f"""<div class="trust" style="font-size:{fs}px; gap:{gap}px;"><img src="{ASSETS}/tp_logo-white.svg" style="height:{logo_h}px;"><img src="{ASSETS}/tp_stars-5.svg" style="height:{star_h}px;"><span style="font-weight:800;">4.6/5</span></div>"""


# ============================================================
# THE APPROVED REFERENCE LAYOUT — full-bleed signature
# ============================================================
def render_signature(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4
    is_portrait  = ratio < 0.66

    edge = int(48 * s)
    photo = b["photo"]
    focus = b["focus"]

    longest_line = max((len(part) for part in b["headline"].replace("<br>", "\n").split("\n")), default=1)
    if is_landscape:
        hl_size = int((72 if longest_line <= 14 else 60 if longest_line <= 18 else 50) * s)
    elif is_portrait:
        hl_size = int((140 if longest_line <= 10 else 102 if longest_line <= 12 else 88 if longest_line <= 14 else 80) * s)
    else:
        hl_size = int((112 if longest_line <= 10 else 88 if longest_line <= 14 else 74) * s)

    if is_landscape:
        scrim_style = "background:linear-gradient(90deg, rgba(3,10,28,.94) 0%, rgba(3,10,28,.88) 40%, rgba(3,10,28,.55) 58%, rgba(3,10,28,.15) 78%, rgba(3,10,28,0) 100%);"
        content_box = f"left:{edge}px; width:{int(w*0.60)}px; top:{int(34*s)}px; bottom:{int(34*s)}px; display:flex; flex-direction:column;"
        brand_scale = 0.72
        stack_mult = 0.82
    else:
        scrim_style = "background:linear-gradient(180deg, rgba(3,10,28,0) 0%, rgba(3,10,28,.15) 28%, rgba(3,10,28,.68) 52%, rgba(3,10,28,.94) 78%, rgba(3,10,28,.98) 100%);"
        content_box = f"left:{edge}px; right:{edge}px; top:{edge}px; bottom:{edge}px; display:flex; flex-direction:column;"
        brand_scale = 1.1 if is_portrait else 0.95
        stack_mult = 1.0

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
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.02; text-shadow:0 6px 40px rgba(0,0,0,.75); margin:0 0 {int(20*s)}px 0; letter-spacing:-.015em; }}
.credential-block {{ margin-bottom:{int(14*s)}px; }}
.courseinfo {{ margin-bottom:{int(22*s)}px; }}
.cta-row {{ display:flex; align-items:center; justify-content:space-between; gap:{int(20*s)}px; flex-wrap:wrap; }}
.trust {{ background:transparent; padding:0; border:none; box-shadow:none; }}
</style>
<div class="canvas">
  <div class="photobox"><img src="{ASSETS}/{photo}"></div>
  <div class="scrim"></div>
  <div class="topscrim"></div>
  <div class="content">
    <div class="brandwrap">{brand_lockup(s, align="left", scale_mult=brand_scale)}</div>
    <div class="midspace"></div>
    <div class="display headline">{b['headline']}</div>
    <div class="credential-block">{julie_credential(s, size_mult=stack_mult)}</div>
    <div class="courseinfo">{course_info(s, size_mult=stack_mult)}</div>
    <div class="cta-row">
      {trust_row(s, size_mult=stack_mult)}
      {cta_button(s, b.get('cta','Enroll Now'), size_mult=(0.9 if is_landscape else 1.0))}
    </div>
  </div>
</div></body></html>"""


# ============================================================
# VERSUS — Julie vs Bryan Johnson (kept, with fixed proof bar)
# ============================================================
def render_versus(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    stacked = ratio < 1.05
    edge = int(44 * s)
    bar_h = int(170 * s)
    top_h = int(300 * s) if not stacked else int(330*s)
    hl_size = int(48 * s)
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

    return f"""{html_head(w,h)}
<style>
{CTA_CSS}{TRUST_CSS}
.top {{ position:absolute; left:{edge}px; right:{edge}px; top:{int(38*s)}px; z-index:10; }}
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.1; text-align:center; margin-top:{int(20*s)}px; }}
.split {{ position:absolute; left:0; right:0; top:{top_h}px; bottom:{bar_h}px; display:flex; {split_style} }}
.side {{ position:relative; flex:1; overflow:hidden; }}
.side img {{ width:100%; height:100%; object-fit:cover; }}
.side.julie img {{ object-position:52% 20%; }}
.side.bryan img {{ object-position:{bryan_pos}; filter:grayscale(0.45) brightness(0.85); }}
.tag {{ position:absolute; left:{int(24*s)}px; top:{int(24*s)}px; padding:{int(8*s)}px {int(16*s)}px; border-radius:999px; font-weight:800; font-size:{max(13,int(17*s))}px; letter-spacing:.02em; z-index:5; }}
.tag.julie {{ background:{BLUE}; color:#fff; }}
.tag.bryan {{ background:rgba(255,255,255,.18); color:#fff; border:1px solid rgba(255,255,255,.4); }}
.statpanel {{ position:absolute; left:0; right:0; bottom:0; padding:{int(22*s)}px {int(24*s)}px; z-index:5; }}
.side.julie .statpanel {{ background:linear-gradient(180deg, transparent, rgba(3,14,40,.96) 55%); }}
.side.bryan .statpanel {{ background:linear-gradient(180deg, transparent, rgba(10,10,12,.96) 55%); }}
.bigstat {{ font-family:'Playfair Display',serif; font-weight:800; font-size:{int(46*s)}px; color:#fff; line-height:1; }}
.bigstat span {{ font-family:'Inter',sans-serif; font-size:{max(13,int(17*s))}px; font-weight:700; color:rgba(255,255,255,.85); margin-left:{int(8*s)}px; }}
.statlabel {{ font-size:{max(12,int(14*s))}px; color:{BLUE_LT}; font-weight:700; margin-top:{int(4*s)}px; }}
.side.bryan .statlabel {{ color:rgba(255,255,255,.55); }}
.bullets {{ margin-top:{int(14*s)}px; display:flex; flex-direction:column; gap:{int(7*s)}px; }}
.bullets div {{ font-size:{max(12,int(15*s))}px; color:rgba(255,255,255,.92); font-weight:600; }}
.side.bryan .bullets div {{ color:rgba(255,255,255,.65); }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:{NAVY_BAR}; border-top:1px solid rgba(126,200,255,.28); display:flex; {'flex-direction:row; align-items:center; justify-content:space-between;' if bar_landscape else 'flex-direction:column; align-items:flex-start; justify-content:center;'} padding:{int(14*s)}px {int(40*s)}px; z-index:20; gap:{int(10*s)}px; }}
.barrow {{ display:flex; align-items:center; justify-content:space-between; width:100%; gap:{int(16*s)}px; }}
.trust {{ background:transparent; padding:0; border:none; box-shadow:none; }}
</style>
<div class="canvas">
  <div class="top">
    {brand_lockup(s, align="center", scale_mult=0.9)}
    <div class="display headline">She Beats Bryan Johnson.<br>For $289/mo.</div>
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
    <div class="barrow">
      <div style="color:#fff; font-weight:700; font-size:{max(14,int(19*s))}px;">{COURSE_INFO} &middot; from <span style="color:{BLUE_LT}; font-weight:800;">$289/mo</span></div>
      {'' if not bar_landscape else ''}
    </div>
    <div class="barrow">
      {trust_row(s, size_mult=0.9)}
      {cta_button(s, b.get('cta','Enroll Now'), size_mult=0.9)}
    </div>
  </div>
</div></body></html>"""


# ---------------- ALL BANNERS, ALL VERSIONS ----------------
def hl(h1, h2):
    return f"{h1}<br>{h2}"

V1 = [
    {"id":"v1_b1", "title":"Make It Automatic",      "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"Make longevity<br>automatic."},
    {"id":"v1_b2", "title":"Willpower Fails",        "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Willpower fails.<br>Habits don&rsquo;t."},
    {"id":"v1_b3", "title":"Sleep. Food. Movement.", "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"Sleep. Food.<br>Movement."},
    {"id":"v1_b4", "title":"It\u2019s Being There",  "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"It&rsquo;s being<br>there."},
    {"id":"v1_b5", "title":"Stay Strong",            "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"Stay strong.<br>For them."},
    {"id":"v1_b6", "title":"He\u2019s My Son",       "photo":"real_julie-hero.jpg",        "focus":"78% 30%", "headline":"He&rsquo;s<br>my son."},
]
V2 = [
    {"id":"v2_b1", "title":"8 Months per Year",   "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"&ldquo;I only age<br>eight months.&rdquo;"},
    {"id":"v2_b2", "title":"Optimise Your Cells", "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"&ldquo;Eat right. Move.<br>Optimise your cells.&rdquo;"},
    {"id":"v2_b3", "title":"Automatic Habits",    "photo":"real_julie-hero.jpg",        "focus":"78% 30%", "headline":"Make longevity<br>automatic."},
    {"id":"v2_b4", "title":"Willpower Fails",     "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"Willpower fails.<br>Habits don&rsquo;t."},
    {"id":"v2_b5", "title":"It\u2019s Being There","photo":"real_julie-standing-hd.jpg","focus":"52% 18%", "headline":"It&rsquo;s not the years.<br>It&rsquo;s being there."},
    {"id":"v2_b6", "title":"65 Days Younger",     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"65 days younger<br>every year."},
]
V3 = [
    {"id":"v3_b1", "title":"Make Longevity Automatic", "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"Make longevity<br>automatic."},
    {"id":"v3_b2", "title":"Outlast Willpower",        "photo":"real_julie-hero.jpg",        "focus":"78% 30%", "headline":"Build habits that<br>outlast willpower."},
    {"id":"v3_b3", "title":"Good Night\u2019s Sleep",  "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"&ldquo;You cannot biohack a<br>good night&rsquo;s sleep.&rdquo;"},
    {"id":"v3_b4", "title":"Age Slower",               "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Age slower.<br>Be there longer."},
    {"id":"v3_b5", "title":"Stay Strong",              "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Stay strong for the<br>people who need you."},
    {"id":"v3_b6", "title":"Eight Months per Year",    "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"&ldquo;For every year<br>that passes, I only<br>age eight months.&rdquo;"},
    {"id":"v3_b7", "title":"Offer Panel",              "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Learn to age<br>a third slower."},
    {"id":"v3_b8", "title":"Editorial Cover",          "photo":"real_julie-purple.jpg",      "focus":"50% 15%", "headline":"Slow your<br>pace of aging."},
    {"id":"v3_b9", "title":"Gallery Arch",             "photo":"julie_real_1.jpg",           "focus":"50% 30%", "headline":"Learn longevity<br>from the world&rsquo;s<br>#2 slowest ager."},
    {"id":"v3_b10","title":"Julie vs Bryan",           "layout":"versus"},
]
V4 = [
    {"id":"v4_b1", "title":"Willpower Fails, Habits Don't", "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Willpower fails.<br>Habits don&rsquo;t.", "cta":"Build My Protocol"},
    {"id":"v4_b2", "title":"Make Longevity Automatic", "photo":"real_julie-purple.jpg", "focus":"50% 15%", "headline":"Make longevity<br>automatic.", "cta":"Start My Blueprint"},
    {"id":"v4_b3", "title":"Small Habits, Kept For Years", "photo":"real_julie-hero.jpg", "focus":"78% 30%", "headline":"Small habits.<br>Kept for years.", "cta":"Join the Next Cohort"},
    {"id":"v4_b4", "title":"It's Not The Years, It's Being There", "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"It&rsquo;s not the years.<br>It&rsquo;s being there.", "cta":"Apply Now"},
    {"id":"v4_b5", "title":"Stay Strong For The People Who Need You", "photo":"real_julie-purple.jpg", "focus":"50% 15%", "headline":"Stay strong for the<br>people who need you.", "cta":"Enroll Now"},
    {"id":"v4_b6", "title":"Live Longer For Your Reason", "photo":"real_julie-hero.jpg", "focus":"78% 30%", "headline":"Find your reason.<br>Then live longer for it.", "cta":"Start Today"},
    {"id":"v4_b7", "title":"Habits That Outlast Willpower", "photo":"real_julie-standing-hd.jpg", "focus":"52% 15%", "headline":"Habits that outlast<br>willpower.", "cta":"Get My Protocol"},
    {"id":"v4_b8", "title":"Be There For Them", "photo":"real_julie-purple.jpg", "focus":"50% 18%", "headline":"Be there for<br>the people who<br>need you.", "cta":"Apply Now"},
    {"id":"v4_b9", "title":"Repeat It Until It's Automatic", "photo":"real_julie-standing-hd.jpg", "focus":"52% 10%", "headline":"Repeat it until it&rsquo;s<br>automatic.", "cta":"Join the Next Cohort"},
    {"id":"v4_b10","title":"Julie vs Bryan Johnson", "layout":"versus"},
]
V6 = [
    {"id":"v6_b1", "title":"Age Slower Starting With Your Habits", "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Age slower.<br>Starting with<br>your habits.", "cta":"Build My Protocol"},
    {"id":"v6_b2", "title":"The Science Of Aging Slower", "photo":"real_julie-purple.jpg", "focus":"50% 15%", "headline":"The science of<br>aging slower.", "cta":"Start My Blueprint"},
    {"id":"v6_b3", "title":"Small Habits Slower Aging", "photo":"real_julie-hero.jpg", "focus":"78% 30%", "headline":"Small habits.<br>Slower aging.", "cta":"Join the Next Cohort"},
    {"id":"v6_b4", "title":"Add Healthy Years To Your Life", "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Add healthy years<br>to your life.", "cta":"Apply Now"},
    {"id":"v6_b5", "title":"Live Long Live Strong Be There", "photo":"real_julie-purple.jpg", "focus":"50% 15%", "headline":"Live long.<br>Live strong.<br>Be there.", "cta":"Enroll Now"},
    {"id":"v6_b6", "title":"Slow Your Biological Age", "photo":"real_julie-hero.jpg", "focus":"78% 30%", "headline":"Slow your<br>biological age.", "cta":"Start Today"},
    {"id":"v6_b7", "title":"The Habits That Slow Aging", "photo":"real_julie-standing-hd.jpg", "focus":"52% 15%", "headline":"The habits that<br>slow aging.", "cta":"Get My Protocol"},
    {"id":"v6_b8", "title":"More Years More Strength More You", "photo":"real_julie-purple.jpg", "focus":"50% 18%", "headline":"More years.<br>More strength.<br>More you.", "cta":"Apply Now"},
    {"id":"v6_b9", "title":"Aging Is A Habit Change It", "photo":"real_julie-standing-hd.jpg", "focus":"52% 10%", "headline":"Aging is a habit.<br>Change it.", "cta":"Join the Next Cohort"},
    {"id":"v6_b10","title":"Julie vs Bryan Johnson", "layout":"versus"},
]
V7 = [dict(b, id=b["id"].replace("v6_","v7_")) for b in V6]
CHOSEN = [
    {"id":"chosen_b1", "title":"Repeat It Until It's Automatic", "photo":"real_julie-standing-hd.jpg", "focus":"52% 10%", "headline":"Repeat it until<br>it&rsquo;s automatic.", "cta":"Join the Next Cohort"},
    {"id":"chosen_b2", "title":"Age Slower, Be There Longer", "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Age slower.<br>Be there longer.", "cta":"Enroll Now"},
    {"id":"chosen_b3", "title":"Eight Months per Year", "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"&ldquo;For every year<br>that passes, I only<br>age eight months.&rdquo;", "cta":"Enroll Now"},
    {"id":"chosen_b4", "title":"Learn to Age a Third Slower", "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%", "headline":"Learn to age<br>a third slower.", "cta":"Enroll Now"},
    {"id":"chosen_b5", "title":"Slow Your Pace of Aging", "photo":"real_julie-purple.jpg", "focus":"50% 24%", "headline":"Slow your<br>pace of aging.", "cta":"Enroll Now"},
    {"id":"chosen_b6", "title":"World's #2 Slowest Ager", "photo":"julie_real_1.jpg", "focus":"50% 30%", "headline":"Learn longevity<br>from the world&rsquo;s<br>#2 slowest ager.", "cta":"Enroll Now"},
]

VERSIONS = {"v1": V1, "v2": V2, "v3": V3, "v4": V4, "v6": V6, "v7": V7, "chosen": CHOSEN}

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
