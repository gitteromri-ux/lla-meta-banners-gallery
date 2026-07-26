#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4 — brand-first luxury rebuild.
Fixes: LLA lockup screams above the fold, bold premium serif headlines (Playfair Display,
not italic-script-everywhere), zero tiny all-caps AI eyebrow tags, Julie's real credential
stated in full, action-first CTA copy, only Script 2 (Make It Automatic) and Script 5
(Start With Your Why) hooks used.
"""
import os, json

ROOT = "/home/user/workspace/repo"
BANNERS_DIR = f"{ROOT}/banners/v5"
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

# Brand palette — matched to longevitylifeacademy.com
NAVY_DEEP  = "#050E22"
NAVY       = "#0A1B3D"
NAVY_BAR   = "#03102A"
BLUE       = "#006EFF"
BLUE_LT    = "#7EC8FF"
BLUE_PALE  = "#BFE0FF"
WHITE      = "#FFFFFF"
GOLD       = "#E8A75A"  # used sparingly, only as a rule/accent, never as primary text

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

# ---------------- BRAND LOCKUP (the fix: screams LLA above everything) ----------------
def brand_lockup(s, align="left", scale_mult=1.0):
    """Real logo mark + 'LONGEVITY LIFE ACADEMY' wordmark, large, matching site treatment."""
    mark_h = int(58 * s * scale_mult)
    word_size = int(40 * s * scale_mult)
    sub_size = max(11, int(14 * s * scale_mult))
    justify = "flex-start" if align == "left" else "center"
    return f"""
<div class="brandlock" style="display:flex; align-items:center; justify-content:{justify}; gap:{int(16*s)}px;">
  <img src="{ASSETS}/lla_logo_mark.png" style="height:{mark_h}px; display:block; flex-shrink:0;">
  <div style="display:flex; flex-direction:column; line-height:1;">
    <div style="font-family:'Playfair Display',serif; font-weight:800; font-size:{word_size}px; color:{WHITE}; letter-spacing:.005em;">
      <span style="color:{BLUE_LT};">Longevity</span> Life Academy
    </div>
    <div style="font-size:{sub_size}px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:rgba(255,255,255,.62); margin-top:{max(3,int(6*s))}px;">by eTeacher Group</div>
  </div>
</div>"""

def julie_credential(s, size_mult=1.0, align="left", color_line1=WHITE):
    justify = "flex-start" if align=="left" else "center"
    text_align = "left" if align=="left" else "center"
    name_size = max(15, int(23 * s * size_mult))
    tag_size  = max(12, int(16 * s * size_mult))
    return f"""
<div style="display:flex; flex-direction:column; align-items:{justify}; text-align:{text_align}; gap:{max(2,int(4*s))}px;">
  <div style="font-weight:800; font-size:{name_size}px; color:{color_line1};">Julie Gibson Clark</div>
  <div style="font-weight:600; font-size:{tag_size}px; color:{BLUE_LT}; letter-spacing:.01em;">2nd Slowest-Aging Person on Earth · Longevity Life Academy Instructor</div>
</div>"""

def cta_button(s, text="Enroll Now", size_mult=1.0):
    font = max(15, int(25 * s * size_mult))
    pad_v = max(12, int(20 * s * size_mult))
    pad_h = max(24, int(42 * s * size_mult))
    return f"""<span class="cta" style="font-size:{font}px; padding:{pad_v}px {pad_h}px;">{text} <span>&rarr;</span></span>"""

CTA_CSS = f"""
.cta {{ display:inline-flex; align-items:center; gap:10px; background:linear-gradient(135deg,#3A8DFF 0%,{BLUE} 100%); color:#fff; font-weight:800; border-radius:999px; border:1.5px solid rgba(255,255,255,.55); box-shadow:0 8px 28px rgba(0,110,255,.55), inset 0 1px 0 rgba(255,255,255,.35); white-space:nowrap; font-family:'Inter',sans-serif; }}
"""

TRUST_CSS = f"""
.trust {{ display:flex; align-items:center; gap:10px; color:rgba(255,255,255,.85); font-weight:600; }}
.trust img.tpl {{ display:block; }} .trust img.tps {{ display:block; }}
"""

def trust_row(s, size_mult=1.0):
    tp_h = max(12, int(18*s*size_mult))
    star_h = max(10, int(15*s*size_mult))
    fs = max(10, int(14*s*size_mult))
    return f"""<div class="trust" style="font-size:{fs}px;"><img class="tpl" src="{ASSETS}/tp_logo-white.svg" style="height:{tp_h}px;"><img class="tps" src="{ASSETS}/tp_stars-5.svg" style="height:{star_h}px;"><span>4.6/5 &middot; 600+ verified reviews</span></div>"""


# ============================================================
# CORE LAYOUT — "Signature" — used for the 6 required banners
# Photo right/full-bleed, brand lockup top-left large, bold headline mid,
# Julie credential + CTA bar bottom. No eyebrow tag, no dash bullets.
# ============================================================
def render_signature(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4
    is_portrait  = ratio < 0.66

    edge = int(52 * s)
    top_pad = int(46 * s)
    bar_h = int((92 if is_landscape else 158) * s)
    hl_size = int((84 if not is_landscape else 66) * s)
    if is_portrait:
        hl_size = int(92 * s)
        # long headlines need a smaller size in the narrow portrait content box
        # to avoid each manual <br> line wrapping again into extra lines.
        longest_line = max((len(part) for part in b["headline"].replace("<br>", "\n").split("\n")), default=0)
        if longest_line >= 20:
            hl_size = int(74 * s)

    photo = b["photo"]
    focus = b["focus"]

    if is_landscape:
        # photo right half, text left half
        img_box = f"left:{int(w*0.44)}px; right:0; top:0; bottom:0;"
        scrim = f"background:linear-gradient(90deg, {NAVY_DEEP} 0%, {NAVY_DEEP} 38%, rgba(5,14,34,.85) 46%, rgba(5,14,34,.15) 62%, transparent 78%);"
        content_box = f"left:{edge}px; width:{int(w*0.46)}px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center;"
    elif is_portrait:
        img_box = f"left:0; right:0; top:0; height:{int(h*0.56)}px;"
        scrim = f"background:linear-gradient(180deg, rgba(5,14,34,.15) 0%, rgba(5,14,34,.05) 40%, {NAVY_DEEP} 92%);"
        content_box = f"left:{edge}px; right:{edge}px; top:{int(h*0.50)}px; bottom:{bar_h+int(30*s)}px; display:flex; flex-direction:column; justify-content:flex-start;"
    else:  # square
        img_box = f"left:0; right:0; top:0; height:{int(h*0.50)}px;"
        scrim = f"background:linear-gradient(180deg, rgba(5,14,34,.1) 0%, rgba(5,14,34,.05) 45%, {NAVY_DEEP} 90%);"
        content_box = f"left:{edge}px; right:{edge}px; top:{int(h*0.44)}px; bottom:{bar_h+int(28*s)}px; display:flex; flex-direction:column; justify-content:flex-start;"

    return f"""{html_head(w,h)}
<style>
{CTA_CSS}{TRUST_CSS}
.photobox {{ position:absolute; {img_box} overflow:hidden; z-index:1; }}
.photobox img {{ width:100%; height:100%; object-fit:cover; object-position:{focus}; }}
.scrimbox {{ position:absolute; {img_box} {scrim} z-index:2; }}
.content {{ position:absolute; {content_box} z-index:5; }}
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.06; text-shadow:0 6px 30px rgba(0,0,0,.5); margin:{int(28*s)}px 0 {int(22*s)}px 0; }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:{NAVY_BAR}; border-top:1px solid rgba(126,200,255,.28); display:flex; align-items:center; justify-content:space-between; padding:0 {int(40*s)}px; z-index:20; gap:{int(18*s)}px; }}
</style>
<div class="canvas">
  <div class="photobox"><img src="{ASSETS}/{photo}"></div>
  <div class="scrimbox"></div>
  <div class="content">
    {brand_lockup(s, align="left", scale_mult=1.05)}
    <div class="display headline">{b['headline']}</div>
    {julie_credential(s, size_mult=1.0)}
  </div>
  <div class="bar">
    {trust_row(s, size_mult=0.9)}
    {cta_button(s, b.get('cta','Enroll Now'))}
  </div>
</div></body></html>"""


# ============================================================
# ALT LAYOUT 1 — "Masthead" — brand lockup as a full-width top masthead band
# (very explicit brand scream), photo below, headline overlays bottom of photo.
# ============================================================
def render_masthead(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4
    edge = int(50 * s)
    mast_h = int((118 if not is_landscape else 96) * s)
    bar_h = int((92 if is_landscape else 150) * s)
    hl_size = int((78 if not is_landscape else 62) * s)

    return f"""{html_head(w,h)}
<style>
{CTA_CSS}{TRUST_CSS}
.mast {{ position:absolute; left:0; right:0; top:0; height:{mast_h}px; background:linear-gradient(180deg,#03102A 0%, #04173A 100%); display:flex; align-items:center; padding:0 {edge}px; z-index:20; border-bottom:2px solid {BLUE}; }}
.photobox {{ position:absolute; left:0; right:0; top:{mast_h}px; bottom:{bar_h}px; overflow:hidden; }}
.photobox img {{ width:100%; height:100%; object-fit:cover; object-position:{b['focus']}; }}
.scrimbox {{ position:absolute; left:0; right:0; top:{mast_h}px; bottom:{bar_h}px; background:linear-gradient(180deg, transparent 0%, transparent 45%, rgba(5,14,34,.55) 72%, rgba(5,14,34,.94) 100%); }}
.content {{ position:absolute; left:{edge}px; right:{edge}px; bottom:{bar_h+int(34*s)}px; z-index:5; }}
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.08; text-shadow:0 6px 30px rgba(0,0,0,.55); margin-bottom:{int(20*s)}px; }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:{NAVY_BAR}; border-top:1px solid rgba(126,200,255,.28); display:flex; align-items:center; justify-content:space-between; padding:0 {int(40*s)}px; z-index:20; gap:{int(18*s)}px; }}
</style>
<div class="canvas">
  <div class="mast">{brand_lockup(s, align="left", scale_mult=0.92)}</div>
  <div class="photobox"><img src="{ASSETS}/{b['photo']}"></div>
  <div class="scrimbox"></div>
  <div class="content">
    <div class="display headline">{b['headline']}</div>
    {julie_credential(s, size_mult=1.0)}
  </div>
  <div class="bar">
    {trust_row(s, size_mult=0.9)}
    {cta_button(s, b.get('cta','Enroll Now'))}
  </div>
</div></body></html>"""


# ============================================================
# ALT LAYOUT 2 — "Split Panel" — vertical navy panel with headline+CTA,
# photo fills the other side full-bleed. Editorial, very premium.
# ============================================================
def render_splitpanel(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    stacked = ratio < 0.85  # portrait/story -> stack panel on top of photo
    edge = int(48 * s)
    bar_h = int(118 * s)
    hl_size = int(70 * s) if not stacked else int(80*s)

    if stacked:
        panel_style = f"left:0; right:0; top:0; height:{int(h*0.46)}px;"
        photo_style = f"left:0; right:0; top:{int(h*0.46)}px; bottom:0;"
        hl_size = int(hl_size * 1.1)
    else:
        panel_w = int(w*0.52)
        panel_style = f"left:0; top:0; bottom:0; width:{panel_w}px;"
        photo_style = f"left:{panel_w}px; right:0; top:0; bottom:0;"
        hl_size = int(hl_size * 0.9)

    return f"""{html_head(w,h)}
<style>
{CTA_CSS}{TRUST_CSS}
.panel {{ position:absolute; {panel_style} background:linear-gradient(165deg,#081B40 0%,{NAVY_DEEP} 80%); display:flex; flex-direction:column; justify-content:center; padding:{int(48*s)}px {edge}px; z-index:5; border-right:{'none' if stacked else f'2px solid {BLUE}'}; border-bottom:{f'2px solid {BLUE}' if stacked else 'none'}; }}
.photobox {{ position:absolute; {photo_style} overflow:hidden; }}
.photobox img {{ width:100%; height:100%; object-fit:cover; object-position:{b['focus']}; }}
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.08; text-shadow:0 4px 20px rgba(0,0,0,.4); margin:{int(26*s)}px 0 {int(24*s)}px 0; }}
.footer {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:{NAVY_BAR}; border-top:1px solid rgba(126,200,255,.28); display:flex; align-items:center; justify-content:space-between; padding:0 {int(40*s)}px; z-index:20; gap:{int(18*s)}px; }}
</style>
<div class="canvas">
  <div class="photobox"><img src="{ASSETS}/{b['photo']}"></div>
  <div class="panel">
    {brand_lockup(s, align="left", scale_mult=1.0)}
    <div class="display headline">{b['headline']}</div>
    {julie_credential(s, size_mult=0.95)}
  </div>
  <div class="footer">
    {trust_row(s, size_mult=0.9)}
    {cta_button(s, b.get('cta','Enroll Now'))}
  </div>
</div></body></html>"""


# ============================================================
# ALT LAYOUT 3 — "Statement Card" — full-bleed photo, centered bottom
# card containing brand lockup + headline + CTA in one cohesive block.
# ============================================================
def render_statementcard(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    edge = int(56 * s)
    hl_size = int(66 * s)
    card_pad = int(44 * s)
    is_wide = ratio > 1.4  # e.g. 191x1 — a bottom overlay card would be tall enough to cover the face

    if is_wide:
        # side-by-side: photo left, full-height navy card right — never overlaps the face
        hl_size = int(54 * s)
        return f"""{html_head(w,h)}
<style>
{CTA_CSS}{TRUST_CSS}
.photobox {{ position:absolute; left:0; top:0; bottom:0; width:46%; overflow:hidden; }}
.photobox img {{ width:100%; height:100%; object-fit:cover; object-position:{b['focus']}; }}
.card {{ position:absolute; left:46%; right:0; top:0; bottom:0; background:{NAVY_DEEP}; border-left:1.5px solid rgba(126,200,255,.4); padding:{int(40*s)}px {int(48*s)}px; display:flex; flex-direction:column; justify-content:center; z-index:10; }}
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.08; margin:{int(20*s)}px 0 {int(18*s)}px 0; }}
.footrow {{ display:flex; align-items:center; justify-content:space-between; margin-top:{int(20*s)}px; padding-top:{int(18*s)}px; border-top:1px solid rgba(126,200,255,.2); gap:{int(16*s)}px; flex-wrap:wrap; }}
</style>
<div class="canvas">
  <div class="photobox"><img src="{ASSETS}/{b['photo']}"></div>
  <div class="card">
    {brand_lockup(s, align="left", scale_mult=0.9)}
    <div class="display headline">{b['headline']}</div>
    {julie_credential(s, size_mult=0.9)}
    <div class="footrow">
      {trust_row(s, size_mult=0.8)}
      {cta_button(s, b.get('cta','Enroll Now'), size_mult=0.9)}
    </div>
  </div>
</div></body></html>"""

    return f"""{html_head(w,h)}
<style>
{CTA_CSS}{TRUST_CSS}
.photobox {{ position:absolute; inset:0; overflow:hidden; }}
.photobox img {{ width:100%; height:100%; object-fit:cover; object-position:{b['focus']}; }}
.scrimtop {{ position:absolute; left:0; right:0; top:0; height:40%; background:linear-gradient(180deg, rgba(5,14,34,.55) 0%, transparent 100%); }}
.card {{ position:absolute; left:{edge}px; right:{edge}px; bottom:{int(44*s)}px; background:rgba(5,14,34,.90); border:1.5px solid rgba(126,200,255,.4); border-radius:{int(22*s)}px; padding:{card_pad}px; backdrop-filter:blur(6px); z-index:10; box-shadow:0 20px 60px rgba(0,0,0,.5); }}
.headline {{ font-size:{hl_size}px; color:{WHITE}; line-height:1.08; margin:{int(22*s)}px 0 {int(20*s)}px 0; }}
.footrow {{ display:flex; align-items:center; justify-content:space-between; margin-top:{int(22*s)}px; padding-top:{int(20*s)}px; border-top:1px solid rgba(126,200,255,.2); gap:{int(16*s)}px; flex-wrap:wrap; }}
</style>
<div class="canvas">
  <div class="photobox"><img src="{ASSETS}/{b['photo']}"></div>
  <div class="scrimtop"></div>
  <div class="card">
    {brand_lockup(s, align="left", scale_mult=1.0)}
    <div class="display headline">{b['headline']}</div>
    {julie_credential(s, size_mult=0.95)}
    <div class="footrow">
      {trust_row(s, size_mult=0.85)}
      {cta_button(s, b.get('cta','Enroll Now'), size_mult=0.95)}
    </div>
  </div>
</div></body></html>"""


# ============================================================
# BONUS — Julie vs Bryan Johnson split-screen comparison
# ============================================================
def render_versus(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    stacked = ratio < 1.05
    edge = int(44 * s)
    bar_h = int(150 * s)
    top_h = int(200 * s) if not stacked else int(230*s)
    hl_size = int(48 * s)
    # the container's own width:height ratio determines how much of the (square) source photo is visible.
    # wider-than-tall containers crop more vertically, so shift the focal point down to reveal eyes+mouth.
    side_h = (h - top_h - bar_h) / (2 if stacked else 1)
    side_w = w if stacked else w / 2
    container_ratio = side_w / side_h
    if container_ratio >= 2.6:
        bryan_pos = "50% 60%"
    elif container_ratio >= 1.6:
        bryan_pos = "50% 45%"
    else:
        bryan_pos = "50% 55%"

    split_style = "flex-direction:column;" if stacked else "flex-direction:row;"

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
.tag {{ position:absolute; left:{int(24*s)}px; top:{int(24*s)}px; padding:{int(8*s)}px {int(16*s)}px; border-radius:999px; font-weight:800; font-size:{max(12,int(15*s))}px; letter-spacing:.02em; z-index:5; }}
.tag.julie {{ background:{BLUE}; color:#fff; }}
.tag.bryan {{ background:rgba(255,255,255,.18); color:#fff; border:1px solid rgba(255,255,255,.4); }}
.statpanel {{ position:absolute; left:0; right:0; bottom:0; padding:{int(22*s)}px {int(24*s)}px; z-index:5; }}
.side.julie .statpanel {{ background:linear-gradient(180deg, transparent, rgba(3,14,40,.96) 55%); }}
.side.bryan .statpanel {{ background:linear-gradient(180deg, transparent, rgba(10,10,12,.96) 55%); }}
.bigstat {{ font-family:'Playfair Display',serif; font-weight:800; font-size:{int(46*s)}px; color:#fff; line-height:1; }}
.bigstat span {{ font-family:'Inter',sans-serif; font-size:{max(12,int(15*s))}px; font-weight:700; color:rgba(255,255,255,.75); margin-left:{int(8*s)}px; }}
.statlabel {{ font-size:{max(11,int(13*s))}px; color:{BLUE_LT}; font-weight:700; margin-top:{int(4*s)}px; }}
.side.bryan .statlabel {{ color:rgba(255,255,255,.55); }}
.bullets {{ margin-top:{int(14*s)}px; display:flex; flex-direction:column; gap:{int(7*s)}px; }}
.bullets div {{ font-size:{max(12,int(15*s))}px; color:rgba(255,255,255,.92); font-weight:600; }}
.side.bryan .bullets div {{ color:rgba(255,255,255,.65); }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:{NAVY_BAR}; border-top:1px solid rgba(126,200,255,.28); display:flex; align-items:center; justify-content:space-between; padding:0 {int(40*s)}px; z-index:20; gap:{int(16*s)}px; }}
</style>
<div class="canvas">
  <div class="top">
    {brand_lockup(s, align="center", scale_mult=0.9)}
    <div class="display headline">She Ages Slower Than Bryan Johnson. For $289/mo.</div>
  </div>
  <div class="split">
    <div class="side julie">
      <img src="{ASSETS}/real_julie-standing-hd.jpg">
      <div class="tag julie">JULIE GIBSON CLARK</div>
      <div class="statpanel">
        <div class="bigstat">#2 <span>slowest aging person on Earth</span></div>
        <div class="statlabel">Rejuvenation Olympics &middot; DunedinPACE 0.665</div>
        <div class="bullets">
          <div>&#10003; Full personalized longevity protocol</div>
          <div>&#10003; Sleep, nutrition &amp; daily movement blueprint</div>
          <div>&#10003; Continuous glucose &amp; biomarker tracking</div>
          <div>&#10003; Live coaching across 18 sessions</div>
        </div>
      </div>
    </div>
    <div class="side bryan">
      <img src="{ASSETS}/bryan_johnson.jpg">
      <div class="tag bryan">BRYAN JOHNSON</div>
      <div class="statpanel">
        <div class="bigstat">$2M <span>spent per year</span></div>
        <div class="statlabel">Ranked below Julie on the same leaderboard</div>
        <div class="bullets">
          <div>&mdash; 100+ supplements, every single day</div>
          <div>&mdash; A 30-person medical team on payroll</div>
          <div>&mdash; Hundreds of tests &amp; experimental therapies</div>
          <div>&mdash; A full-time job just to keep up</div>
        </div>
      </div>
    </div>
  </div>
  <div class="bar">
    <div style="color:#fff; font-weight:700; font-size:{max(12,int(15*s))}px;">Tuition from <span style="color:{BLUE_LT};">$289/mo</span> &mdash; not $2M/year</div>
    {cta_button(s, "Enroll Now", size_mult=0.95)}
  </div>
</div></body></html>"""


# ---------------- BANNER CONTENT — Script 2 & Script 5 hooks only ----------------
# Script 2 = "Make It Automatic" (willpower fails / habits / repetition)
# Script 5 = "Start With Your Why" (not living forever / being there / her son)

BANNERS = [
    # ---- 6 CORE SIGNATURE BANNERS ----
    # Cluster A: Habits/Automatic (Script 2)
    {"id":"v5_b1", "layout":"signature", "script":2, "title":"Age Slower Starting With Your Habits",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%",
     "headline":"Age slower.<br>Starting with<br>your habits.", "cta":"Build My Protocol"},
    {"id":"v5_b2", "layout":"signature", "script":2, "title":"The Science Of Aging Slower",
     "photo":"real_julie-purple.jpg", "focus":"50% 15%",
     "headline":"The science of<br>aging slower.", "cta":"Start My Blueprint"},
    {"id":"v5_b3", "layout":"signature", "script":2, "title":"Small Habits Slower Aging",
     "photo":"real_julie-hero.jpg", "focus":"78% 30%",
     "headline":"Small habits.<br>Slower aging.", "cta":"Join the Next Cohort"},
    # Cluster B: Live longer for the people you love (Script 5)
    {"id":"v5_b4", "layout":"signature", "script":5, "title":"Add Healthy Years To Your Life",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%",
     "headline":"Add healthy years<br>to your life.", "cta":"Apply Now"},
    {"id":"v5_b5", "layout":"signature", "script":5, "title":"Live Long Live Strong Be There",
     "photo":"real_julie-purple.jpg", "focus":"50% 15%",
     "headline":"Live long.<br>Live strong.<br>Be there.", "cta":"Enroll Now"},
    {"id":"v5_b6", "layout":"signature", "script":5, "title":"Slow Your Biological Age",
     "photo":"real_julie-hero.jpg", "focus":"78% 30%",
     "headline":"Slow your<br>biological age.", "cta":"Start Today"},

    # ---- 3 ALTERNATE LAYOUTS ----
    {"id":"v5_b7", "layout":"masthead", "script":2, "title":"The Habits That Slow Aging",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 15%",
     "headline":"The habits that<br>slow aging.", "cta":"Get My Protocol"},
    {"id":"v5_b8", "layout":"splitpanel", "script":5, "title":"More Years More Strength More You",
     "photo":"real_julie-purple.jpg", "focus":"50% 18%",
     "headline":"More years.<br>More strength.<br>More you.", "cta":"Apply Now"},
    {"id":"v5_b9", "layout":"statementcard", "script":2, "title":"Aging Is A Habit Change It",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 10%",
     "headline":"Aging is a habit.<br>Change it.", "cta":"Join the Next Cohort"},

    # ---- BONUS: Julie vs Bryan Johnson ----
    {"id":"v5_b10", "layout":"versus", "script":None, "title":"Julie vs Bryan Johnson",
     "photo":None, "focus":None, "headline":None, "cta":"Enroll Now"},
]

RENDERERS = {
    "signature": render_signature,
    "masthead": render_masthead,
    "splitpanel": render_splitpanel,
    "statementcard": render_statementcard,
    "versus": render_versus,
}

manifest = {"v5": []}
for b in BANNERS:
    item = {"id": b["id"], "title": b["title"], "layout": b["layout"], "sizes": {}}
    fn_render = RENDERERS[b["layout"]]
    for size_key, size in SIZES.items():
        fn = f"{b['id']}_{size_key}.html"
        path = f"{BANNERS_DIR}/{fn}"
        html = fn_render(b, size_key, size["w"], size["h"])
        with open(path, "w") as f:
            f.write(html)
        item["sizes"][size_key] = {
            "html": fn, "png": fn.replace(".html", ".png"),
            "w": size["w"], "h": size["h"], "label": size["label"], "note": size["note"],
        }
    manifest["v5"].append(item)

with open(f"{BANNERS_DIR}/v5_manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Wrote {len(BANNERS)*len(SIZES)} HTML files across {len(BANNERS)} banners x {len(SIZES)} sizes.")
