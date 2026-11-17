# -*- coding: utf-8 -*-
import glob, os
import pdfplumber

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
checks = {
    "01_讯飞_产品需求文档": ["资料来源", "华经"],
    "02_讯飞_竞品分析": ["资料来源", "钉钉闪记"],
    "03_讯飞_功能模块PRD与功能说明": ["验收标准"],
    "04_讯飞_产品数据周报": ["02-23", "模板使用说明"],
    "05_光云_需求文档": ["资料来源", "光云科技"],
    "07_光云_复盘分析报告": ["个人沉淀"],
    "08_车队项目_需求文档": ["里程碑"],
}
out = []
for folder, keys in checks.items():
    pdfs = glob.glob(os.path.join(ROOT, folder, "*.pdf"))
    if not pdfs:
        out.append(folder + ": NO PDF")
        continue
    with pdfplumber.open(pdfs[0]) as pdf:
        text = "".join((p.extract_text() or "") for p in pdf.pages)
    missing = [k for k in keys if k not in text]
    out.append(folder + (": OK" if not missing else ": MISSING " + str(missing)))

with open(os.path.join(ROOT, "_build", "_qa_report.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("qa done")
