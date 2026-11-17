# -*- coding: utf-8 -*-
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "10_网吧交友助手_原型", "svg")
os.makedirs(OUT_DIR, exist_ok=True)

NAV = ["登录授权", "选网吧", "随机匹配", "匿名聊天", "个人资料", "管理后台", "语音消息", "吧主入驻", "图片动态"]
W, H = 1440, 900
SIDE = 224
TOP = 64
BG = "#0d0b1a"
PANEL = "#151226"
LINE = "#2a2342"
TEXT = "#e8e6f5"
CYAN = "#00e5ff"
MAGENTA = "#ff2ec4"


def svg_open(name):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Microsoft YaHei, PingFang SC, sans-serif">',
            f'<rect width="{W}" height="{H}" fill="{BG}"/>']


def svg_close():
    return ["</svg>"]


def skeleton(svg, title):
    svg.append(f'<rect width="{SIDE}" height="{H}" fill="#0a0816"/>')
    svg.append(f'<text x="20" y="34" fill="{CYAN}" font-size="19" font-weight="800">开黑搭子</text>')
    for i, n in enumerate(NAV):
        fill = "#ffffff" if n == title else "#cfcae8"
        active = n == title
        svg.append(f'<rect x="12" y="{72+i*42}" width="{SIDE-24}" height="34" rx="8" fill="{"rgba(0,229,255,0.12)" if active else "none"}" stroke="{"rgba(0,229,255,0.4)" if active else "none"}"/>')
        svg.append(f'<text x="28" y="{94+i*42}" fill="{fill}" font-size="14">{n}</text>')
    svg.append(f'<rect x="{SIDE}" y="0" width="{W-SIDE}" height="{TOP}" fill="{PANEL}" stroke="{LINE}"/>')
    svg.append(f'<text x="{SIDE+24}" y="40" fill="{TEXT}" font-size="20" font-weight="800">{title}</text>')
    svg.append(f'<text x="{W-320}" y="40" fill="#8f89ad" font-size="12">开黑搭子 · 原型线框 V1.0</text>')


def panel(svg, x, y, w, h, title, rows=0):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{PANEL}" stroke="{LINE}"/>')
    svg.append(f'<text x="{x+18}" y="{y+28}" fill="{TEXT}" font-size="15" font-weight="700">{title}</text>')
    for r in range(rows):
        ry = y + 44 + r * 36
        svg.append(f'<rect x="{x+12}" y="{ry}" width="{w-24}" height="24" rx="5" fill="#1d1734"/>')


def write(name, svg):
    with open(os.path.join(OUT_DIR, name + ".svg"), "w", encoding="utf-8") as f:
        f.write("\n".join(svg))


# login
s = svg_open("login"); skeleton(s, "登录授权")
panel(s, SIDE + 330, 160, 480, 380, "微信一键登录", rows=1)
write("login", s + svg_close())

# cafe
s = svg_open("cafe"); skeleton(s, "选网吧")
for i in range(3):
    panel(s, SIDE + 30 + i * 390, 120, 360, 220, "网吧卡片", rows=2)
write("cafe", s + svg_close())

# match
s = svg_open("match"); skeleton(s, "随机匹配")
panel(s, SIDE + 330, 140, 480, 300, "匹配中", rows=2)
panel(s, SIDE + 330, 470, 480, 220, "我的会话", rows=2)
write("match", s + svg_close())

# chat
s = svg_open("chat"); skeleton(s, "匿名聊天")
panel(s, SIDE + 330, 120, 480, 520, "匿名搭子 #1024", rows=4)
write("chat", s + svg_close())

# profile
s = svg_open("profile"); skeleton(s, "个人资料")
panel(s, SIDE + 330, 140, 480, 320, "个人资料", rows=3)
write("profile", s + svg_close())

# admin
s = svg_open("admin"); skeleton(s, "管理后台")
panel(s, SIDE + 18, 110, W - SIDE - 36, 650, "举报处理", rows=6)
write("admin", s + svg_close())

# placeholder pages
for key, title in (("voice", "语音消息"), ("merchant", "吧主入驻"), ("moments", "图片动态")):
    s = svg_open(key); skeleton(s, title)
    panel(s, SIDE + 330, 200, 480, 220, title + "（二期占位）", rows=1)
    write(key, s + svg_close())

print("svg done")
