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
BANNERS_DIR = f"{ROOT}/banners/v7"
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
    """Real LLA logo asset used at large scale — same lockup as the homepage hero."""
    # The real lla_logo.png is ~1290x600 including 'by eTeacher Group' tag; keep aspect + scale big.
    logo_h = int(150 * s * scale_mult)
    justify = "flex-start" if align == "left" else "center"
    return f"""
<div class="brandlock" style="display:flex; align-items:center; justify-content:{justify};">
  <img src="{ASSETS}/lla_logo.png" style="height:{logo_h}px; display:block; filter:drop-shadow(0 2px 10px rgba(0,0,0,.35));">
</div>"""

def julie_credential(s, size_mult=1.0, align="left", color_line1=WHITE):
    justify = "flex-start" if align=="left" else "center"
    text_align = "left" if align=="left" else "center"
    name_size = max(15, int(23 * s * size_mult))
    tag_size  = max(12, int(16 * s * size_mult))
    return f"""
<div style="display:flex; flex-direction:column; align-items:{justify}; text-align:{text_align}; gap:{max(2,int(4*s))}px;">
  <div style="font-weight:800; font-size:{name_size}px; color:{color_line1};">Julie Gibson Clark</div>
  <div style="font-weight:600; font-size:{tag_size}px; color:{BLUE_LT}; letter-spacing:.01em; line-height:1.35;">2nd Slowest-Aging Person on Earth</div>
  <div style="font-weight:600; font-size:{tag_size}px; color:{BLUE_LT}; letter-spacing:.01em; line-height:1.35;">Longevity Life Academy Instructor</div>
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
    star_h = max(14, int(22*s*size_mult))
    fs = max(13, int(18*s*size_mult))
    # Just 5 green stars + "4.6/5" — transparent background, sits next to CTA button
    return f"""<div class="trust" style="font-size:{fs}px; gap:{max(6,int(9*s))}px;"><img class="tps" src="{ASSETS}/tp_stars-5.svg" style="height:{star_h}px;"><span style="font-weight:800;">4.6/5</span></div>"""


# ============================================================
# CORE LAYOUT — "Signature" — used for the 6 required banners
# Photo right/full-bleed, brand lockup top-left large, bold headline mid,
# Julie credential + CTA bar bottom. No eyebrow tag, no dash bullets.
# ============================================================
def render_signature(b, size_key, w, h):
    """V7 signature layout: photo FULL-BLEED (edge to edge). Copy stacks over a bottom gradient scrim.
    Logo top-left, big headline center-bottom, credential + cta_row all in the bottom third.
    No navy dead zones — feed-native composition."""
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4
    is_portrait  = ratio < 0.66

    edge = int(48 * s)
    photo = b["photo"]
    focus = b["focus"]

    # Size headlines to actually FILL the width — dominant, bold, clear.
    # For headlines with manual <br> breaks, size by the longest line.
    longest_line = max((len(part) for part in b["headline"].replace("<br>", "\n").split("\n")), default=1)
    if is_landscape:
        # 1200x628 — wide, single or two-line headline needs less height per line
        hl_size = int((88 if longest_line <= 14 else 72 if longest_line <= 18 else 60) * s)
    elif is_portrait:
        # 1080x1920 — tall, headline can stack 3 lines
        # Portrait content_box width ≈ 984px – keep headline safe from wrap
        hl_size = int((156 if longest_line <= 10 else 112 if longest_line <= 12 else 96 if longest_line <= 14 else 88) * s)
    else:  # square-ish (1x1, 4x5)
        hl_size = int((128 if longest_line <= 10 else 100 if longest_line <= 14 else 84) * s)

    # Scrim gradient over the bottom half so text is readable but photo is fully visible.
    if is_landscape:
        # For 1200x628 the copy sits on left half, so use a horizontal gradient
        scrim_style = f"background:linear-gradient(90deg, rgba(3,10,28,.92) 0%, rgba(3,10,28,.85) 38%, rgba(3,10,28,.55) 55%, rgba(3,10,28,.15) 75%, rgba(3,10,28,0) 100%);"
    else:
        scrim_style = f"background:linear-gradient(180deg, rgba(3,10,28,0) 0%, rgba(3,10,28,.15) 30%, rgba(3,10,28,.65) 55%, rgba(3,10,28,.92) 80%, rgba(3,10,28,.98) 100%);"

    if is_landscape:
        # Copy occupies LEFT half; brand top, headline center-left, cta_row bottom-left
        content_box = f"left:{edge}px; width:{int(w*0.56)}px; top:{edge}px; bottom:{edge}px; display:flex; flex-direction:column;"
        brand_scale = 0.9
        # for landscape, credential + cta on same footprint (compact)
    else:
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
    <div class="brandwrap">{brand_lockup(s, align="left", scale_mult=brand_scale)}</div>
    <div class="midspace"></div>
    <div class="display headline">{b['headline']}</div>
    <div class="credential-block">{julie_credential(s, size_mult=(0.95 if is_landscape else 1.05))}</div>
    <div class="cta-row">
      {trust_row(s, size_mult=1.0)}
      {cta_button(s, b.get('cta','Enroll Now'))}
    </div>
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
    top_h = int(300 * s) if not stacked else int(330*s)
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
.iconrow {{ margin-top:{int(14*s)}px; display:flex; flex-direction:column; gap:{int(10*s)}px; }}
.iconstat {{ display:flex; align-items:center; gap:{int(12*s)}px; font-size:{max(13,int(16*s))}px; color:#fff; font-weight:700; }}
.iconstat .ic {{ width:{max(28,int(36*s))}px; height:{max(28,int(36*s))}px; border-radius:8px; background:rgba(126,200,255,.16); border:1px solid rgba(126,200,255,.35); display:flex; align-items:center; justify-content:center; color:{BLUE_LT}; flex-shrink:0; }}
.iconstat .ic svg {{ width:{max(16,int(20*s))}px; height:{max(16,int(20*s))}px; }}
.side.bryan .iconstat {{ color:rgba(255,255,255,.85); }}
.side.bryan .iconstat .ic {{ background:rgba(255,255,255,.08); border-color:rgba(255,255,255,.2); color:rgba(255,255,255,.7); }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:{NAVY_BAR}; border-top:1px solid rgba(126,200,255,.28); display:flex; align-items:center; justify-content:space-between; padding:0 {int(40*s)}px; z-index:20; gap:{int(16*s)}px; }}
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
        <div class="bigstat">#2 <span>slowest aging person on Earth</span></div>
        <div class="statlabel">Rejuvenation Olympics leaderboard</div>
        <div class="iconrow">
          <div class="iconstat"><div class="ic">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12a8 8 0 1 1-16 0 8 8 0 0 1 16 0Z"/><path d="M8 12l3 3 5-6"/></svg>
          </div><span>Personalized longevity protocol</span></div>
          <div class="iconstat"><div class="ic">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4M12 18v4M4.9 4.9l2.8 2.8M16.3 16.3l2.8 2.8M2 12h4M18 12h4M4.9 19.1l2.8-2.8M16.3 7.7l2.8-2.8"/></svg>
          </div><span>Sleep, nutrition &amp; movement plan</span></div>
          <div class="iconstat"><div class="ic">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l3-8 4 16 3-8h4"/></svg>
          </div><span>Live biomarker tracking</span></div>
        </div>
      </div>
    </div>
    <div class="side bryan">
      <img src="{ASSETS}/bryan_johnson.jpg">
      <div class="tag bryan">BRYAN JOHNSON</div>
      <div class="statpanel">
        <div class="bigstat">$2M <span>spent per year</span></div>
        <div class="statlabel">Ranked below Julie on the same board</div>
        <div class="iconrow">
          <div class="iconstat"><div class="ic">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 16 0 8 8 0 0 1-16 0Z"/><path d="M8 8l8 8"/></svg>
          </div><span>100+ supplements a day</span></div>
          <div class="iconstat"><div class="ic">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M2 20c0-3 3-5 7-5s7 2 7 5"/><path d="M15 20c0-2 2-3.5 4.5-3.5S24 18 24 20"/></svg>
          </div><span>30-person medical team</span></div>
          <div class="iconstat"><div class="ic">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="14" rx="2"/><path d="M4 10h16M9 4v4M15 4v4"/></svg>
          </div><span>A full-time job</span></div>
        </div>
      </div>
    </div>
  </div>
  <div class="bar">
    <div style="color:#fff; font-weight:700; font-size:{max(13,int(17*s))}px;">Tuition from <span style="color:{BLUE_LT}; font-weight:800;">$289/mo</span></div>
    {cta_button(s, "Enroll Now", size_mult=0.95)}
  </div>
</div></body></html>"""


# ---------------- BANNER CONTENT — Script 2 & Script 5 hooks only ----------------
# Script 2 = "Make It Automatic" (willpower fails / habits / repetition)
# Script 5 = "Start With Your Why" (not living forever / being there / her son)

BANNERS = [
    # ---- 6 CORE SIGNATURE BANNERS ----
    # Cluster A: Habits/Automatic (Script 2)
    {"id":"v7_b1", "layout":"signature", "script":2, "title":"Age Slower Starting With Your Habits",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%",
     "headline":"Age slower.<br>Starting with<br>your habits.", "cta":"Build My Protocol"},
    {"id":"v7_b2", "layout":"signature", "script":2, "title":"The Science Of Aging Slower",
     "photo":"real_julie-purple.jpg", "focus":"50% 15%",
     "headline":"The science of<br>aging slower.", "cta":"Start My Blueprint"},
    {"id":"v7_b3", "layout":"signature", "script":2, "title":"Small Habits Slower Aging",
     "photo":"real_julie-hero.jpg", "focus":"78% 30%",
     "headline":"Small habits.<br>Slower aging.", "cta":"Join the Next Cohort"},
    # Cluster B: Live longer for the people you love (Script 5)
    {"id":"v7_b4", "layout":"signature", "script":5, "title":"Add Healthy Years To Your Life",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 18%",
     "headline":"Add healthy years<br>to your life.", "cta":"Apply Now"},
    {"id":"v7_b5", "layout":"signature", "script":5, "title":"Live Long Live Strong Be There",
     "photo":"real_julie-purple.jpg", "focus":"50% 15%",
     "headline":"Live long.<br>Live strong.<br>Be there.", "cta":"Enroll Now"},
    {"id":"v7_b6", "layout":"signature", "script":5, "title":"Slow Your Biological Age",
     "photo":"real_julie-hero.jpg", "focus":"78% 30%",
     "headline":"Slow your<br>biological age.", "cta":"Start Today"},

    # ---- 3 ALTERNATE LAYOUTS ----
    {"id":"v7_b7", "layout":"masthead", "script":2, "title":"The Habits That Slow Aging",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 15%",
     "headline":"The habits that<br>slow aging.", "cta":"Get My Protocol"},
    {"id":"v7_b8", "layout":"splitpanel", "script":5, "title":"More Years More Strength More You",
     "photo":"real_julie-purple.jpg", "focus":"50% 18%",
     "headline":"More years.<br>More strength.<br>More you.", "cta":"Apply Now"},
    {"id":"v7_b9", "layout":"statementcard", "script":2, "title":"Aging Is A Habit Change It",
     "photo":"real_julie-standing-hd.jpg", "focus":"52% 10%",
     "headline":"Aging is a habit.<br>Change it.", "cta":"Join the Next Cohort"},

    # ---- BONUS: Julie vs Bryan Johnson ----
    {"id":"v7_b10", "layout":"versus", "script":None, "title":"Julie vs Bryan Johnson",
     "photo":None, "focus":None, "headline":None, "cta":"Enroll Now"},
]

RENDERERS = {
    "signature": render_signature,
    # V7: b7/b8/b9 all use the same full-bleed treatment as signature —
    # the unified feed-native composition. The versus banner keeps its own layout.
    "masthead": render_signature,
    "splitpanel": render_signature,
    "statementcard": render_signature,
    "versus": render_versus,
}

manifest = {"v7": []}
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
    manifest["v7"].append(item)

with open(f"{BANNERS_DIR}/v7_manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Wrote {len(BANNERS)*len(SIZES)} HTML files across {len(BANNERS)} banners x {len(SIZES)} sizes.")
