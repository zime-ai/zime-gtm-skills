#!/usr/bin/env python3
"""
GitHub Social Preview Generator for zime-ai/zime-gtm-skills
Generates a 1280x640 OpenGraph preview image in the style of pqt-graveyard/social-preview.
"""

import argparse
import math
import os
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def create_social_preview(
    output_path=".github/images/social-preview-light.png",
    theme="light",
    owner="zime-ai",
    repo="zime-gtm-skills",
    tagline="Agent Skills for Sales Call Audits & CRM Deal Inspection",
    badges_list=None,
    dot_style="circle",
    seed=42
):
    random.seed(seed)

    if badges_list is None:
        badges_list = [
            "Evidence-Cited Audits",
            "GTM Rubric Engine",
            "Zero Telemetry",
            "MIT Open Source",
        ]

    # 1. Canvas Settings (GitHub standard 1280x640, 2:1 ratio)
    width = 1280
    height = 640

    if theme == "dark":
        bg_color = (13, 17, 23)        # #0D1117 GitHub dark background
        card_bg = (22, 27, 34)         # #161B22 GitHub dark card
        card_border = (48, 54, 61)     # #30363D
        text_muted = (139, 148, 158)   # #8B949E
        text_main = (240, 246, 252)    # #F0F6FC
        text_sub = (175, 184, 193)     # #AFB8C1
        card_shadow = (0, 0, 0, 140)
    else:
        bg_color = (246, 248, 250)      # #F6F8FA GitHub light background
        card_bg = (255, 255, 255)       # #FFFFFF GitHub light card
        card_border = (208, 215, 222)   # #D0D7DE
        text_muted = (101, 109, 118)    # #656D76
        text_main = (31, 35, 40)        # #1F2328
        text_sub = (87, 96, 106)       # #57606A
        card_shadow = (140, 149, 159, 35)

    # Palette of colors for dots & badges
    colors = [
        (243, 108, 33),   # Zime Orange #F36C21
        (0, 168, 150),    # Zime Teal #00A896
        (137, 224, 81),   # Shell Green #89E051
        (49, 120, 198),   # TypeScript Blue #3178C6
        (53, 114, 165),   # Python Blue #3572A5
        (203, 23, 30),    # YAML Red #CB171E
        (168, 85, 247),   # Purple #A855F7
        (236, 72, 153),   # Pink #EC4899
        (245, 158, 11),   # Amber #F59E0B
    ]

    # Create base canvas
    img = Image.new("RGBA", (width, height), bg_color + (255,))

    # 2. Grid & Protected Area Setup
    grid_size = 20
    cols = width // grid_size   # 64
    rows = height // grid_size  # 32

    # Card dimensions & position (Centered box: 920x310)
    card_w = 920
    card_h = 310
    card_x = (width - card_w) // 2  # 180
    card_y = (height - card_h) // 2 # 165

    p_min_x = card_x - 12
    p_max_x = card_x + card_w + 12
    p_min_y = card_y - 12
    p_max_y = card_y + card_h + 12

    def is_protected(x, y):
        return p_min_x <= x <= p_max_x and p_min_y <= y <= p_max_y

    def get_distance_to_protected(x, y):
        dx = max(p_min_x - x, 0, x - p_max_x)
        dy = max(p_min_y - y, 0, y - p_max_y)
        return math.sqrt(dx*dx + dy*dy)

    # Draw Dot Matrix Grid
    dot_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    dot_draw = ImageDraw.Draw(dot_layer)

    for r in range(rows):
        for c in range(cols):
            cx = c * grid_size + 10
            cy = r * grid_size + 10

            if is_protected(cx, cy):
                continue

            if random.random() > 0.25:
                continue

            dist = get_distance_to_protected(cx, cy)
            max_dist = 220.0
            factor = min(1.0, dist / max_dist)
            alpha = int((0.15 + 0.85 * factor * random.uniform(0.6, 1.0)) * 255)

            color = random.choice(colors)
            color_rgba = color + (alpha,)

            radius = 4
            if dot_style == "circle":
                dot_draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=color_rgba)
            else:
                dot_draw.rectangle([cx - radius, cy - radius, cx + radius, cy + radius], fill=color_rgba)

    img = Image.alpha_composite(img, dot_layer)
    draw = ImageDraw.Draw(img)

    # 3. Card Shadow & Background
    card_shape = [card_x, card_y, card_x + card_w, card_y + card_h]
    radius = 16

    shadow_img = Image.new("RGBA", (width, height), (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow_img)
    shadow_offset = 10
    shadow_shape = [card_x + 2, card_y + shadow_offset, card_x + card_w - 2, card_y + card_h + shadow_offset]
    shadow_draw.rounded_rectangle(shadow_shape, radius=radius, fill=card_shadow)
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius=16))

    img = Image.alpha_composite(img, shadow_img)
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle(card_shape, radius=radius, fill=card_bg, outline=card_border, width=2)

    # 4. Fonts Setup
    font_bold_large = None
    font_medium = None
    font_small = None

    font_paths = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf"
    ]

    for fp in font_paths:
        if os.path.exists(fp):
            try:
                font_bold_large = ImageFont.truetype(fp, 42)
                font_medium = ImageFont.truetype(fp, 21)
                font_small = ImageFont.truetype(fp, 14)
                break
            except Exception:
                pass

    if not font_bold_large:
        font_bold_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # 5. Draw Card Content
    content_x = card_x + 44
    content_y = card_y + 44

    # High-precision Official Zime Logo Icon
    icon_size = 48
    icon_x = content_x
    icon_y = content_y - 2
    
    # Outer orange ring
    draw.ellipse([icon_x, icon_y, icon_x + icon_size, icon_y + icon_size], outline=(243, 108, 33), width=5)
    # Middle ring
    draw.ellipse([icon_x + 10, icon_y + 10, icon_x + icon_size - 10, icon_y + icon_size - 10], outline=(243, 108, 33), width=3)
    # Center filled dot
    draw.ellipse([icon_x + 20, icon_y + 20, icon_x + icon_size - 20, icon_y + icon_size - 20], fill=(243, 108, 33))
    # Teal arrow notch pointing top-right
    draw.line([icon_x + 32, icon_y + 16, icon_x + 44, icon_y + 4], fill=(0, 168, 150), width=4)
    draw.polygon([(icon_x + 44, icon_y + 4), (icon_x + 36, icon_y + 3), (icon_x + 44, icon_y + 11)], fill=(0, 168, 150))

    # Title: "zime-ai / zime-gtm-skills" perfectly aligned with logo
    text_start_x = content_x + icon_size + 18
    text_y = content_y

    draw.text((text_start_x, text_y), owner, fill=text_muted, font=font_bold_large)
    owner_bbox = font_bold_large.getbbox(owner) if hasattr(font_bold_large, 'getbbox') else (0,0,130,38)
    owner_w = owner_bbox[2] - owner_bbox[0]

    draw.text((text_start_x + owner_w + 10, text_y), "/", fill=text_muted, font=font_bold_large)
    slash_bbox = font_bold_large.getbbox("/") if hasattr(font_bold_large, 'getbbox') else (0,0,18,38)
    slash_w = slash_bbox[2] - slash_bbox[0]

    draw.text((text_start_x + owner_w + 10 + slash_w + 10, text_y), repo, fill=text_main, font=font_bold_large)

    # Subtitle / Description
    desc_y = content_y + 60
    draw.text((content_x, desc_y), tagline, fill=text_sub, font=font_medium)

    # Badges Row (4 pills neatly spaced on one line)
    badge_y = desc_y + 62

    badge_styles = [
        ((0, 168, 150), (230, 247, 244) if theme=="light" else (10, 40, 36)),
        ((49, 120, 198), (235, 243, 255) if theme=="light" else (15, 30, 50)),
        ((137, 224, 81), (238, 250, 230) if theme=="light" else (25, 45, 20)),
        ((243, 108, 33), (255, 242, 235) if theme=="light" else (45, 25, 15)),
    ]

    bx = content_x
    for idx, label in enumerate(badges_list[:4]):
        border_c, bg_c = badge_styles[idx % len(badge_styles)]
        bbox = font_small.getbbox(label) if hasattr(font_small, 'getbbox') else (0,0,80,18)
        bw = bbox[2] - bbox[0] + 24
        bh = 32
        
        draw.rounded_rectangle([bx, badge_y, bx + bw, badge_y + bh], radius=16, fill=bg_c, outline=border_c, width=1)
        draw.text((bx + 12, badge_y + 7), label, fill=text_main, font=font_small)
        bx += bw + 12

    # GitHub-style language distribution bar at card bottom edge
    lang_bar_y = card_y + card_h - 6
    bar_w = card_w - 32
    bar_x = card_x + 16

    languages = [
        (0.45, (137, 224, 81)),  # Shell / Markdown Green
        (0.30, (49, 120, 198)),  # Prompt Blue
        (0.15, (243, 108, 33)),  # Zime Orange
        (0.10, (203, 23, 30)),   # YAML Red
    ]

    curr_x = bar_x
    for ratio, color in languages:
        seg_w = int(bar_w * ratio)
        draw.rectangle([curr_x, lang_bar_y, curr_x + seg_w, lang_bar_y + 4], fill=color)
        curr_x += seg_w

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"✅ Generated social preview image: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate GitHub Social Preview image")
    parser.add_argument("--output", default=".github/images/social-preview-light.png", help="Output path")
    parser.add_argument("--theme", choices=["dark", "light"], default="light", help="Color theme")
    parser.add_argument("--dots", choices=["circle", "square"], default="circle", help="Grid dot style")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--badges", nargs="+", help="Custom 4 badges")
    args = parser.parse_args()

    badges = args.badges if args.badges else [
        "Evidence-Cited Audits",
        "GTM Rubric Engine",
        "Zero Telemetry",
        "MIT Open Source"
    ]

    create_social_preview(
        output_path=args.output,
        theme=args.theme,
        badges_list=badges,
        dot_style=args.dots,
        seed=args.seed
    )

if __name__ == "__main__":
    main()
