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
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

NAVY_DEEP  = "#060b20"
NAVY_BAR   = "#03102a"
BLUE       = "#006EFF"
ICE        = "#9cc3ef"   # approved eyebrow / italic accent
GLOW       = "#8ff2ff"   # approved glowing facts color

FACT_CRED   = "2nd slowest-aging person on Earth."
FACT_COURSE = "The Longevity Blueprint. 18 live sessions. 100% online."

GLOW_SHADOW = ("text-shadow:0 0 6px rgba(127,231,255,.9),0 0 14px rgba(127,231,255,.7),"
               "0 0 28px rgba(90,190,255,.55),0 0 52px rgba(60,150,235,.35),0 2px 8px rgba(2,6,20,.55);")

def html_head(w, h, bg=None):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
{FONT_LINK}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ width:{w}px; height:{h}px; overflow:hidden; background:{bg or NAVY_DEEP}; -webkit-font-smoothing:antialiased; }}
.canvas {{ position:relative; width:{w}px; height:{h}px; background:{bg or NAVY_DEEP}; font-family:'Inter',sans-serif; overflow:hidden; }}
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
    if two_line:
        text = '<span style="white-space:nowrap;">2nd Slowest-Aging</span><br><span style="white-space:nowrap;">Person on Earth</span>'
    else:
        text = '2nd Slowest-Aging Person on Earth'
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



CODEC_FACE = """
@font-face { font-family:'Codec Pro'; src:url('../../assets/CodecPro-Regular.woff') format('woff'); font-weight:400; font-style:normal; }
@font-face { font-family:'Codec Pro'; src:url('../../assets/CodecPro-Bold.ttf') format('truetype'); font-weight:700; font-style:normal; }
@font-face { font-family:'Codec Pro'; src:url('../../assets/CodecPro-ExtraBold.ttf') format('truetype'); font-weight:800; font-style:normal; }
@font-face { font-family:'Codec Pro'; src:url('../../assets/CodecPro-Heavy.ttf') format('truetype'); font-weight:900; font-style:normal; }
"""

def styled_headline(headline, italic_last=True):
    parts = headline.split("<br>")
    if len(parts) < 2 or not italic_last:
        return headline
    last = f'<span style="font-style:italic; font-weight:500; color:#b9d4f2;">{parts[-1]}</span>'
    return "<br>".join(parts[:-1] + [last])

def site_lockup(inner, logo_h):
    """Website lockup: 'Longevity Life Academy' one line + 'by eTeacher Group' second line,
    same fonts/colors as longevitylifeacademy.com."""
    fs = min(int(logo_h * 0.40), int(inner / (22 * 0.47)))
    sub = max(16, int(fs * 0.52))
    return (f'<div style="display:flex; flex-direction:column; gap:{int(fs*0.22)}px;">'
            f'<div style="font-family:\'EB Garamond\',serif; font-weight:500; font-size:{fs}px; '
            f'color:#c9d6ea; letter-spacing:.01em; line-height:1.05; white-space:nowrap;">Longevity Life Academy</div>'
            f'<div style="font-family:\'EB Garamond\',serif; font-style:italic; font-size:{sub}px; color:#93a7c4;">'
            f'by <span style="font-family:\'Inter\',sans-serif; font-style:normal; font-weight:700; color:#338BFF; letter-spacing:.01em;">eTeacher</span> '
            f'<span style="font-size:{int(sub*0.82)}px;">Group</span></div></div>')



NEON_WHITE = ("text-shadow:0 0 5px rgba(255,255,255,.7),0 0 14px rgba(190,225,255,.5),"
              "0 0 30px rgba(130,185,255,.35),0 2px 8px rgba(2,6,20,.45);")
SERIF = "'Instrument Serif','Times New Roman',serif"

def trust_bottom(fs):
    return (f'<div style="display:inline-flex; align-items:center; gap:{int(fs*0.6)}px; white-space:nowrap;">'
            f'<img src="{ASSETS}/tp_stars-5.svg" style="height:{int(fs*1.1)}px; display:block;">'
            f'<img src="{ASSETS}/tp_logo-white.svg" style="height:{int(fs*1.15)}px; display:block; margin-top:{int(fs*0.06)}px;">'
            f'<span style="font-family:\'Inter\',sans-serif; font-weight:600; font-size:{fs}px; color:rgba(255,255,255,.92);">4.6/5&ensp;&middot;&ensp;600+ reviews</span></div>')

def tp_pill(fs):
    return (f'<div style="display:inline-flex; align-items:center; gap:{int(fs*0.62)}px; '
            f'background:rgba(12,24,52,.62); border:1px solid rgba(255,255,255,.16); border-radius:9999px; '
            f'padding:{int(fs*0.52)}px {int(fs*0.95)}px; white-space:nowrap; font-family:\'Inter\',sans-serif; font-size:{fs}px; color:rgba(255,255,255,.88);">'
            f'<img src="{ASSETS}/tp_stars-5.svg" style="height:{int(fs*1.05)}px; display:block;">'
            f'<span style="font-weight:700; color:#fff;">4.6 / 5</span>'
            f'<span style="opacity:.55;">&middot;</span><span style="font-weight:600;">Trustpilot</span>'
            f'<span style="opacity:.55;">&middot;</span><span>600+ reviews</span></div>')

def logo_img(w):
    return (f'<img src="{ASSETS}/lla_logo.png" style="width:{w}px; height:auto; display:block;">')

def site_lockup2(lock_fs):
    """Exact site hero lockup, wordmark on ONE line: Longevity (#B8D4E8) Life Academy (#FFF),
    Instrument Serif 400, byline: italic 'by' + official eTeacher logotype + italic 'Group'."""
    by_fs = max(17, int(lock_fs * 0.46))
    img_h = max(22, int(lock_fs * 0.46))
    return (f'<div>'
            f'<div style="font-family:{SERIF}; font-weight:400; font-size:{lock_fs}px; line-height:0.95; '
            f'letter-spacing:-.015em; white-space:nowrap;">'
            f'<span style="color:#B8D4E8;">Longevity</span> <span style="color:#FFFFFF;">Life Academy</span></div>'
            f'<div style="display:flex; align-items:center; gap:{int(by_fs*0.42)}px; margin-top:{int(lock_fs*0.28)}px;">'
            f'<span style="font-family:{SERIF}; font-style:italic; font-size:{by_fs}px; color:#FFFFFF;">by</span>'
            f'<img src="{ASSETS}/eteacher_word.png" style="height:{img_h}px; display:block; margin-top:{int(img_h*0.14)}px;">'
            f'<span style="font-family:{SERIF}; font-style:italic; font-size:{by_fs}px; color:#FFFFFF;">Group</span>'
            f'</div></div>')

def headline_site(headline, hl_size, inner, budget=1.32):
    """Site hero title: Codec Pro 700 white, tight; last line Instrument Serif italic, blue gradient."""
    parts = headline.split("<br>")
    if len(parts) >= 2:
        last = (f'<span style="font-family:{SERIF}; font-style:italic; font-weight:400; letter-spacing:-.02em; '
                f'background:linear-gradient(180deg,#BFE2FF 0%,#6FB6FF 100%); -webkit-background-clip:text; '
                f'background-clip:text; -webkit-text-fill-color:transparent;">{parts[-1]}</span>')
        body = "<br>".join(parts[:-1] + [last])
    else:
        body = headline
    return (f'<div style="font-family:{SERIF}; font-weight:400; font-size:{hl_size}px; '
            f'color:#ffffff; line-height:0.99; letter-spacing:-.012em; width:{int(inner*budget)}px; position:relative; z-index:9; '
            f'text-shadow:0 4px 32px rgba(0,0,0,.45);">{body}</div>')

def credential_site(fs):
    return (f'<div style="font-family:{SERIF}; font-style:italic; font-weight:400; '
            f'font-size:{fs}px; color:{GOLD}; line-height:1.15; white-space:nowrap;">'
            f'<span style="font-style:normal;">&#9733;</span>&nbsp;2nd Slowest-Aging Person on Earth</div>')

def stat_chip(fs, label):
    dot = (f'<span style="width:{max(7,int(fs*0.42))}px; height:{max(7,int(fs*0.42))}px; border-radius:50%; '
           f'background:#2BE080; box-shadow:0 0 8px rgba(43,224,128,.9),0 0 18px rgba(43,224,128,.5); '
           f'display:inline-block; flex-shrink:0;"></span>')
    return (f'<span style="display:inline-flex; align-items:center; gap:{int(fs*0.55)}px; white-space:nowrap; '
            f'background:linear-gradient(180deg, rgba(46,84,150,.34) 0%, rgba(14,30,64,.42) 100%); border:1px solid rgba(140,180,255,.22); box-shadow:inset 0 1px 0 rgba(255,255,255,.10); border-radius:{int(fs*0.62)}px; '
            f'padding:{int(fs*0.55)}px {int(fs*0.85)}px; font-family:\'Inter\',sans-serif; font-weight:600; '
            f'font-size:{fs}px; letter-spacing:.09em; color:#f2f7ff;">{dot}{label}</span>')

def blueprint_site(bp_fs, sub_fs):
    return (f'<div>'
            f'<div style="font-family:\'Codec Pro\',\'Inter\',sans-serif; font-weight:700; font-size:{bp_fs}px; '
            f'color:#ffffff; letter-spacing:-.01em; line-height:1.12; white-space:nowrap; {NEON_WHITE}">The Longevity Blueprint</div>'
            f'<div style="display:flex; gap:{int(sub_fs*0.7)}px; margin-top:{int(sub_fs*0.75)}px;">'
            f'{stat_chip(sub_fs, "18 LIVE SESSIONS")}{stat_chip(sub_fs, "100% ONLINE")}</div></div>')

def cta_site(fs, text):
    if not text.endswith("&#8594;"):
        text = text + " &#8594;"
    return (f'<span style="display:inline-flex; align-items:center; white-space:nowrap; '
            f'background:linear-gradient(180deg,#338BFF 0%,#006EFF 100%); color:#fff; '
            f"font-family:'Inter',sans-serif; font-weight:600; font-size:{fs}px; letter-spacing:.01em; "
            f'padding:{int(fs*0.55)}px {int(fs*1.15)}px; border-radius:9999px; '
            f'box-shadow:0 12px 28px rgba(0,110,255,.38),0 2px 6px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.25);">{text}</span>')



def gold_credential(fs, align="left"):
    """Champagne-gradient serif credential: hairline rules + diamond accent, gradient-clipped text."""
    rule = (f'<span style="flex:1; height:1px; min-width:{int(fs*0.8)}px; '
            f'background:linear-gradient(90deg, rgba(219,183,120,0) 0%, rgba(219,183,120,.85) 50%, rgba(219,183,120,0) 100%);"></span>')
    return (f'<div style="filter:drop-shadow(0 2px {int(fs*0.55)}px rgba(206,168,96,.32)); text-align:{align};">'
            f'<div style="display:flex; align-items:center; gap:{int(fs*0.34)}px; margin-bottom:{int(fs*0.32)}px;">'
            f'{rule}<span style="color:#EBD3A2; font-size:{int(fs*0.46)}px; line-height:1;">&#10022;</span>{rule}</div>'
            f'<div style="font-family:{SERIF}; font-style:italic; font-weight:400; font-size:{fs}px; line-height:1.12; '
            f'letter-spacing:.005em; white-space:nowrap; '
            f'background:linear-gradient(180deg,#FAF0DA 0%,#EDD2A0 42%,#C99F5C 100%); '
            f'-webkit-background-clip:text; background-clip:text; color:transparent;">'
            f'2nd Slowest-Aging<br>Person on Earth</div></div>')


def lower_third_wide(s, size_key, w, edge):
    bot = int(150*s) if size_key == "9x16" else int(44*s)
    avail = w - 2*edge
    name_fs = min(int(44*s), int(avail*0.42 / (18*0.58)))
    role_fs = int(name_fs*0.60)
    cred_fs = min(int(60*s), int(avail*0.50 / (19.5*0.42)))
    return (f'<div style="position:absolute; left:0; right:0; bottom:0; z-index:9; '
            f'padding:{int(90*s)}px {edge}px {bot}px {edge}px; '
            f'background:linear-gradient(180deg, rgba(4,9,26,0) 0%, rgba(4,9,26,.60) 52%, rgba(4,9,26,.94) 100%);">'
            f'<div style="display:flex; justify-content:space-between; align-items:flex-end; width:100%;">'
            f'<div style="border-left:{max(4,int(6*s))}px solid {BLUE}; padding-left:{int(20*s)}px;">'
            f'<div style="font-family:\'Inter\',sans-serif; font-weight:800; font-size:{name_fs}px; color:#ffffff; '
            f'letter-spacing:.01em; line-height:1.12; white-space:nowrap;">Julie Gibson Clark</div>'
            f'<div style="font-family:{SERIF}; font-style:italic; font-weight:400; font-size:{role_fs}px; '
            f'color:{ICE}; line-height:1.25; margin-top:{int(6*s)}px; white-space:nowrap;">Longevity Life Academy Instructor</div></div>'
            f'{gold_credential(cred_fs, "right")}'
            f'</div></div>')


def lower_third(s, size_key, name_fs, role_fs, cred_fs):
    bot = int(170*s) if size_key == "9x16" else int(40*s)
    return (f'<div style="position:absolute; left:0; right:0; bottom:0; z-index:6; '
            f'padding:{int(90*s)}px {int(30*s)}px {bot}px {int(30*s)}px; '
            f'background:linear-gradient(180deg, rgba(4,9,26,0) 0%, rgba(4,9,26,.78) 62%, rgba(4,9,26,.92) 100%);">'
            f'<div style="border-left:{max(4,int(6*s))}px solid {BLUE}; padding-left:{int(18*s)}px;">'
            f'<div style="font-family:\'Inter\',sans-serif; font-weight:800; font-size:{name_fs}px; color:#ffffff; '
            f'letter-spacing:.01em; line-height:1.15; white-space:nowrap;">Julie Gibson Clark</div>'
            f'<div style="font-family:{SERIF}; font-style:italic; font-weight:400; font-size:{role_fs}px; '
            f'color:{ICE}; line-height:1.25; margin-top:{int(5*s)}px;">Longevity Life Academy Instructor</div>'
            f'<div style="margin-top:{int(14*s)}px;">{gold_credential(cred_fs, "left")}</div>'
            f'</div></div>')


# ============================================================
# SIGNATURE - site-hero composition on split navy panel
# ============================================================
def render_signature(b, size_key, w, h):
    s, ratio = scale_for(w, h)
    is_landscape = ratio > 1.4
    is_portrait  = ratio < 0.9
    is_story     = ratio < 0.62

    text_frac = 0.55 if is_landscape else (0.65 if is_story else (0.62 if is_portrait else 0.58))
    tw = int(w * text_frac)
    edge = int(42 * s) if is_landscape else (int(40 * s) if is_portrait else int(48 * s))
    inner = tw - 2 * edge
    pw = w - tw

    plain = b["headline"].replace("<br>", "\n")
    for ent, ch in [("&rsquo;","'"),("&ldquo;",'"'),("&rdquo;",'"'),("&amp;","&")]:
        plain = plain.replace(ent, ch)
    longest = max((len(l) for l in plain.split("\n")), default=1)
    hl_cap = (126 if is_landscape else 180) * s
    hl_budget = 1.12 if is_portrait else (1.22 if is_landscape else 1.08)
    hl_size = int(min(hl_cap, (inner * hl_budget) / (longest * 0.36)))
    nlines = b['headline'].count('<br>') + 1
    if nlines >= 3:
        hl_size = int(hl_size * (0.70 if is_landscape else (0.92 if not is_portrait else 1.0)))

    if is_landscape:
        tp_fs, cred_cap, bp_cap, cta_fs = int(16*s), int(28*s), int(36*s), int(20*s)
        g_tp, g_lock, g_hl, g_cred, g_bp = int(16*s), int(20*s), int(22*s), int(12*s), int(24*s)
        lock_cap = int(64*s)
    elif is_portrait:
        tp_fs, cred_cap, bp_cap, cta_fs = int(30*s), int(56*s), int(72*s), int(33*s)
        g_tp, g_lock, g_hl, g_cred, g_bp = int(44*s), int(48*s), int(52*s), int(24*s), int(58*s)
        lock_cap = int(112*s)
    else:
        tp_fs, cred_cap, bp_cap, cta_fs = int(19*s), int(34*s), int(46*s), int(23*s)
        g_tp, g_lock, g_hl, g_cred, g_bp = int(20*s), int(26*s), int(28*s), int(14*s), int(30*s)
        lock_cap = int(84*s)

    wb = 1.30 if is_portrait else 1.0
    logo_w = int(inner * (0.56 if is_landscape else 0.88))
    tp_fs   = min(tp_fs, int(inner / (47*0.52)))
    lock_fs = min(lock_cap, int(inner*1.00 / (22*0.36)))
    cred_fs = min(cred_cap, int(inner*wb / (36*0.43)))
    bp_fs   = min(bp_cap, int(inner*1.00 / (23*0.47)))
    sub_fs  = max(13, int(bp_fs*0.46))
    name_fs = min(int(40*s), int((pw - 80*s) / (18*0.52)))
    lt_cred_fs = min(int(46*s), int((pw - 95*s) / (20*0.44)))
    role_fs = min(int(27*s), int((pw - 80*s) / (33*0.40)))

    photo = b["photo"]; focus = b["focus"]
    cta = b.get("cta", "Enroll Now")

    return f"""{html_head(w,h)}
<style>
{CODEC_FACE}
.canvas {{ display:flex; flex-direction:row; position:relative; }}
.textpanel {{ width:{tw}px; height:{h}px; flex-shrink:0; position:relative; z-index:5;
  background:radial-gradient(120% 90% at 8% 6%, rgba(0,110,255,.16) 0%, rgba(0,110,255,0) 55%),radial-gradient(100% 80% at 90% 100%, rgba(0,60,160,.12) 0%, rgba(0,60,160,0) 60%),linear-gradient(160deg, #0a1430 0%, {NAVY_DEEP} 55%, #04081a 100%);
  padding:0 {edge}px; display:flex; flex-direction:column; justify-content:center; }}
.photopanel {{ position:relative; flex:1; height:{h}px; overflow:hidden; background:{NAVY_DEEP}; }}
.photopanel img {{ width:100%; height:100%; object-fit:cover; object-position:{focus}; display:block; filter:saturate(1.06) contrast(1.04) brightness(.99); }}
.photopanel .blend {{ position:absolute; inset:0; background:linear-gradient(90deg, {NAVY_DEEP} 0%, rgba(6,11,32,.45) 12%, rgba(6,11,32,0) 30%), radial-gradient(140% 60% at 50% 118%, rgba(4,9,26,.55) 0%, rgba(4,9,26,0) 55%); pointer-events:none; }}
</style>
<div class="canvas">
  <div class="textpanel">
    <div style="margin-bottom:{g_lock}px;">{site_lockup2(lock_fs)}</div>
    <div style="margin-bottom:{g_hl}px;">{headline_site(b['headline'], hl_size, inner, 1.12 if is_portrait else (1.22 if is_landscape else 1.08))}</div>
    <div style="margin-top:{int(h*(0.06 if is_portrait else 0.11))}px; margin-bottom:{int(g_bp*1.35)}px;">{blueprint_site(bp_fs, sub_fs)}</div>
    <div>{trust_bottom(tp_fs)}</div>
  </div>
  <div class="photopanel"><img src="{ASSETS}/{photo}"><div class="blend"></div>{"" if is_portrait else lower_third(s, size_key, name_fs, role_fs, lt_cred_fs)}</div>
{lower_third_wide(s, size_key, w, edge) if is_portrait else ""}
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
                     f'{trust_row(s, mult=0.82)}</div>')
        bar_flex = "flex-direction:row; align-items:center; justify-content:space-between;"
    else:
        bar_inner = (f'<div style="font-weight:700; font-size:{fact_fs}px; color:{GLOW}; {GLOW_SHADOW}">{FACT_COURSE}</div>'
                     f'<div style="display:flex; align-items:center; justify-content:space-between; width:100%; gap:{int(16*s)}px;">'
                     f'{trust_row(s, mult=0.9)}</div>')
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
    <div style="display:flex; justify-content:center;">{site_lockup2(int(44*s))}</div>
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
