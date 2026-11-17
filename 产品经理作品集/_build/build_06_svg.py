# -*- coding: utf-8 -*-
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "06_光云_原型", "svg")
os.makedirs(OUT_DIR, exist_ok=True)

NAV = ["登录页", "工作台", "订单列表", "订单详情", "批量打单", "库存列表", "库存同步 / 对账", "库存盘点", "缺货与异常预警", "预警设置", "消息中心", "数据看板", "帮助中心"]
W, H = 1440, 900
SIDE = 216
TOP = 64


def svg_open(name):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Microsoft YaHei, PingFang SC, sans-serif">',
            f'<rect width="{W}" height="{H}" fill="#f4f6fa"/>']


def svg_close():
    return ["</svg>"]


def skeleton(svg, title):
    svg.append(f'<rect width="{SIDE}" height="{H}" fill="#101a2e"/>')
    svg.append(f'<text x="20" y="34" fill="#ffffff" font-size="18" font-weight="700">光云 · 订单与库存</text>')
    for i, n in enumerate(NAV):
        fill = "#1f5feb" if n == title else "#cbd5e1"
        svg.append(f'<rect x="12" y="{70+i*44}" width="{SIDE-24}" height="36" rx="8" fill="{"#1f5feb" if n==title else "none"}"/>')
        svg.append(f'<text x="26" y="{93+i*44}" fill="{fill}" font-size="14">{n}</text>')
    svg.append(f'<rect x="{SIDE}" y="0" width="{W-SIDE}" height="{TOP}" fill="#ffffff" stroke="#e4e8f0"/>')
    svg.append(f'<text x="{SIDE+24}" y="40" fill="#1f2937" font-size="20" font-weight="700">{title}</text>')
    svg.append(f'<text x="{W-320}" y="40" fill="#6b7280" font-size="12">光云科技 · 订单与库存模块 · 线框 V1.0</text>')


def panel(svg, x, y, w, h, title, rows=0):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#ffffff" stroke="#e4e8f0"/>')
    svg.append(f'<text x="{x+18}" y="{y+28}" fill="#1f2937" font-size="15" font-weight="700">{title}</text>')
    if rows:
        for r in range(rows):
            ry = y + 46 + r * 34
            svg.append(f'<rect x="{x+12}" y="{ry}" width="{w-24}" height="24" rx="4" fill="#f2f5fa"/>')
            svg.append(f'<line x1="{x+12}" y1="{ry+24+6}" x2="{x+w-12}" y2="{ry+24+6}" stroke="#e4e8f0"/>')


def kpis(svg, y=100):
    cw = (W - SIDE - 36 - 30) // 4
    for i in range(4):
        x = SIDE + 18 + i * (cw + 10)
        svg.append(f'<rect x="{x}" y="{y}" width="{cw}" height="96" rx="10" fill="#ffffff" stroke="#e4e8f0"/>')
        svg.append(f'<rect x="{x+14}" y="{y+16}" width="72" height="10" rx="5" fill="#dbe4f5"/>')
        svg.append(f'<rect x="{x+14}" y="{y+46}" width="96" height="22" rx="5" fill="#1f5feb"/>')


def write(name, svg):
    path = os.path.join(OUT_DIR, name + ".svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("saved", path)


# 1 dashboard
s = svg_open("dashboard")
skeleton(s, "工作台")
kpis(s)
panel(s, SIDE + 18, 220, 700, 340, "待办提醒", rows=4)
panel(s, SIDE + 738, 220, 670, 340, "快捷入口", rows=0)
s.extend([f'<rect x="{SIDE+756}" y="{470}" width="110" height="34" rx="8" fill="#1f5feb"/>',
          f'<text x="{SIDE+776}" y="{492}" fill="#ffffff" font-size="13">去处理订单</text>'])
write("dashboard", s + svg_close())

# 2 orders
s = svg_open("orders")
skeleton(s, "订单列表")
panel(s, SIDE + 18, 100, W - SIDE - 36, 700, "筛选与工具栏", rows=0)
panel(s, SIDE + 18, 160, W - SIDE - 36, 620, "订单列表", rows=9)
write("orders", s + svg_close())

# 3 order-detail
s = svg_open("order-detail")
skeleton(s, "订单详情")
panel(s, SIDE + 18, 100, 680, 380, "订单信息", rows=5)
panel(s, SIDE + 718, 100, 670, 380, "状态时间线", rows=3)
panel(s, SIDE + 18, 500, W - SIDE - 36, 280, "商品明细", rows=3)
write("order-detail", s + svg_close())

# 4 inventory
s = svg_open("inventory")
skeleton(s, "库存列表")
panel(s, SIDE + 18, 100, W - SIDE - 36, 700, "库存列表", rows=10)
write("inventory", s + svg_close())

# 5 reconcile
s = svg_open("reconcile")
skeleton(s, "库存同步 / 对账")
panel(s, SIDE + 18, 100, 680, 500, "最近同步记录", rows=5)
panel(s, SIDE + 718, 100, 670, 500, "对账差异", rows=4)
write("reconcile", s + svg_close())

# 6 alerts
s = svg_open("alerts")
skeleton(s, "缺货与异常预警")
panel(s, SIDE + 18, 100, W - SIDE - 36, 700, "预警列表", rows=10)
write("alerts", s + svg_close())

# 7 analytics
s = svg_open("analytics")
skeleton(s, "数据看板")
kpis(s)
panel(s, SIDE + 18, 220, W - SIDE - 36, 480, "近7日订单量", rows=0)
s.extend([f'<rect x="{SIDE+60}" y="520" width="80" height="160" rx="6" fill="#1f5feb"/>',
          f'<rect x="{SIDE+190}" y="470" width="80" height="210" rx="6" fill="#1f5feb"/>',
          f'<rect x="{SIDE+320}" y="540" width="80" height="140" rx="6" fill="#1f5feb"/>'])
write("analytics", s + svg_close())

# 8 login
s = svg_open("login")
skeleton(s, "登录页")
panel(s, SIDE + 330, 150, 480, 420, "登录工作台", rows=2)
write("login", s + svg_close())

# 9 batch-ship
s = svg_open("batch-ship")
skeleton(s, "批量打单")
panel(s, SIDE + 18, 100, W - SIDE - 36, 700, "批量打单", rows=9)
write("batch-ship", s + svg_close())

# 10 stocktake
s = svg_open("stocktake")
skeleton(s, "库存盘点")
panel(s, SIDE + 18, 100, W - SIDE - 36, 700, "库存盘点", rows=9)
write("stocktake", s + svg_close())

# 11 alert-settings
s = svg_open("alert-settings")
skeleton(s, "预警设置")
panel(s, SIDE + 18, 100, 680, 500, "预警规则", rows=4)
panel(s, SIDE + 718, 100, 670, 500, "通知方式", rows=4)
write("alert-settings", s + svg_close())

# 12 messages
s = svg_open("messages")
skeleton(s, "消息中心")
panel(s, SIDE + 18, 100, W - SIDE - 36, 700, "消息列表", rows=9)
write("messages", s + svg_close())

# 13 help
s = svg_open("help")
skeleton(s, "帮助中心")
panel(s, SIDE + 18, 100, 680, 500, "常见问题", rows=4)
panel(s, SIDE + 718, 100, 670, 500, "联系支持", rows=2)
write("help", s + svg_close())

print("svg done")
