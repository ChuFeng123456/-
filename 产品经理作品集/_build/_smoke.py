# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docbuild import *

doc = new_document()
title(doc, "测试文档标题", "副标题说明")
heading(doc, "一级标题", 1)
para(doc, "正文段落，用于验证中文字体、行距与页边距是否正常。")
heading(doc, "二级标题", 2)
bullets(doc, ["要点一", "要点二", "要点三"])
table(doc, ["项目", "说明", "数值"], [["价格", "公开渠道", "3999 元"], ["电池", "容量", "2600mAh"]], widths_cm=[3, 7, 3])
add_footer_page_numbers(doc)
save(doc, os.path.join(os.path.dirname(__file__), "..", "_render", "smoke.docx"))
print("smoke ok")
