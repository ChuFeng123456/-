# -*- coding: utf-8 -*-
import os, shutil, glob, sys
import pdfplumber

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
RENDER = os.path.join(ROOT, "_render")
summary = []

doc_dirs = [d for d in os.listdir(ROOT)
            if os.path.isdir(os.path.join(ROOT, d)) and d[:3] in ("01_", "02_", "03_", "05_", "07_", "08_")]

for d in sorted(doc_dirs):
    docx = glob.glob(os.path.join(ROOT, d, "*.docx"))
    if not docx:
        summary.append(f"[MISSING DOCX] {d}")
        continue
    base = os.path.splitext(os.path.basename(docx[0]))[0]
    pdf = os.path.join(RENDER, base, base + ".pdf")
    if not os.path.exists(pdf):
        summary.append(f"[MISSING PDF] {base}")
        continue
    with pdfplumber.open(pdf) as p:
        pages = len(p.pages)
        first = (p.pages[0].extract_text() or "").replace("\n", " ")[:120]
    dst = os.path.join(ROOT, d, base + ".pdf")
    shutil.copyfile(pdf, dst)
    summary.append(f"[OK {pages}p] {d}\n   {first}")

report = "\n".join(summary)
with open(os.path.join(RENDER, "_finalize_report.txt"), "w", encoding="utf-8") as f:
    f.write(report)
print("finalize done")
