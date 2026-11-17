import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "file:///C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const OUT = "C:/Users/L1532/Documents/ChatGPT/项目仓库/产品经理作品集/04_讯飞_产品数据周报/科大讯飞AI录音笔产品数据周报.xlsx";
const FONT = "Microsoft YaHei";

const wb = Workbook.create();

// ---------- Sheet 1 指标口径 ----------
const defs = wb.worksheets.add("指标口径");
defs.getRange("A1:C1").values = [["产品数据周报指标口径", "", ""]];
defs.getRange("A1:C1").merge();
defs.getRange("A1").format.font = { name: FONT, size: 14, bold: true, color: "#1F2937" };
defs.getRange("A3:C3").values = [["指标", "定义", "统计口径"]];
defs.getRange("A4:C10").values = [
  ["销量", "本周新售台数", "电商平台成交口径"],
  ["好评率", "近30天好评占比", "主要电商平台汇总"],
  ["转写使用率", "录音后使用转写功能的占比", "激活设备埋点"],
  ["次周留存", "激活后次周仍活跃的占比", "账号活跃口径"],
  ["转写准确率", "清晰普通话识别正确率", "抽检样本评估"],
  ["同步耗时", "录音停止到云端可读的秒数", "全量设备中位数"],
  ["同类差评占比", "差评中与录音转写相关的占比", "人工分类口径"],
];
defs.getRange("A3:C3").format = { fill: "#1F3864", font: { name: FONT, bold: true, color: "#FFFFFF" }, borders: { preset: "all", style: "thin", color: "#D9D9D9" } };
defs.getRange("A4:C10").format = { font: { name: FONT, size: 11 }, borders: { preset: "all", style: "thin", color: "#D9D9D9" }, verticalAlignment: "center" };
defs.getRange("A4:C10").format.autofitColumns();
defs.getRange("A3:C10").format.autofitRows();

// ---------- Sheet 2 十二周原始数据 ----------
const data = wb.worksheets.add("12周原始数据");
data.getRange("A1:H1").values = [["十二周趋势数据（示例数据）", "", "", "", "", "", "", ""]];
data.getRange("A1:H1").merge();
data.getRange("A1").format.font = { name: FONT, size: 14, bold: true, color: "#1F2937" };
data.getRange("A2:H2").values = [["周次", "销量(台)", "好评率", "转写使用率", "次周留存", "转写准确率", "同步耗时(秒)", "同类差评占比"]];
data.getRange("A3:H14").values = [
  ["12-08", 120, 0.880, 0.52, 0.38, 0.940, 68, 0.180],
  ["12-15", 145, 0.884, 0.53, 0.39, 0.942, 67, 0.178],
  ["12-22", 168, 0.889, 0.54, 0.39, 0.945, 66, 0.175],
  ["12-29", 190, 0.892, 0.55, 0.40, 0.946, 65, 0.172],
  ["01-05", 210, 0.896, 0.56, 0.41, 0.948, 65, 0.170],
  ["01-12", 235, 0.901, 0.58, 0.42, 0.950, 64, 0.168],
  ["01-19", 255, 0.905, 0.59, 0.43, 0.952, 63, 0.165],
  ["01-26", 270, 0.910, 0.61, 0.44, 0.955, 62, 0.162],
  ["02-02", 285, 0.914, 0.62, 0.45, 0.957, 61, 0.160],
  ["02-09", 300, 0.919, 0.64, 0.46, 0.960, 60, 0.158],
  ["02-16", 310, 0.923, 0.66, 0.48, 0.963, 59, 0.156],
  ["02-23", 320, 0.926, 0.68, 0.49, 0.965, 58, 0.153],
];
data.getRange("A2:H2").format = { fill: "#1F3864", font: { name: FONT, bold: true, color: "#FFFFFF" }, borders: { preset: "all", style: "thin", color: "#D9D9D9" }, horizontalAlignment: "center" };
data.getRange("A3:H14").format = { font: { name: FONT, size: 11 }, borders: { preset: "all", style: "thin", color: "#D9D9D9" }, verticalAlignment: "center" };
data.getRange("A3:A14").format.horizontalAlignment = "center";
data.getRange("B3:B14").format.numberFormat = "#,##0";
data.getRange("C3:F14").format.numberFormat = "0.0%";
data.getRange("G3:G14").format.numberFormat = "#,##0";
data.getRange("H3:H14").format.numberFormat = "0.0%";
data.getRange("A15").values = [["本表为示例数据，上线后替换为真实埋点与电商平台数据。"]];
data.getRange("A15").format.font = { name: FONT, size: 9, italic: true, color: "#6B7280" };
data.getRange("A2:H14").format.autofitColumns();

// ---------- Sheet 3 周报模板 ----------
const tpl = wb.worksheets.add("周报模板");
tpl.getRange("A1:B1").values = [["科大讯飞AI录音笔产品数据周报", ""]];
tpl.getRange("A1:B1").merge();
tpl.getRange("A1").format.font = { name: FONT, size: 15, bold: true, color: "#1F2937" };
tpl.getRange("A3").values = [["报告周期"]];
tpl.getRange("B3").values = [["2026-02-23 至 2026-03-01"]];
tpl.getRange("A4:B11").values = [
  ["指标", "本周数值（自动取第12周）"],
  ["销量(台)", ""],
  ["好评率", ""],
  ["转写使用率", ""],
  ["次周留存", ""],
  ["转写准确率", ""],
  ["同步耗时(秒)", ""],
  ["同类差评占比", ""],
];
tpl.getRange("B5").formulas = [["='12周原始数据'!B14"]];
tpl.getRange("B6").formulas = [["='12周原始数据'!C14"]];
tpl.getRange("B7").formulas = [["='12周原始数据'!D14"]];
tpl.getRange("B8").formulas = [["='12周原始数据'!E14"]];
tpl.getRange("B9").formulas = [["='12周原始数据'!F14"]];
tpl.getRange("B10").formulas = [["='12周原始数据'!G14"]];
tpl.getRange("B11").formulas = [["='12周原始数据'!H14"]];
tpl.getRange("B5").format.numberFormat = "#,##0";
tpl.getRange("B6:B9").format.numberFormat = "0.0%";
tpl.getRange("B10").format.numberFormat = "#,##0";
tpl.getRange("B11").format.numberFormat = "0.0%";
tpl.getRange("A4:B11").format = { font: { name: FONT, size: 11 }, borders: { preset: "all", style: "thin", color: "#D9D9D9" }, verticalAlignment: "center" };
tpl.getRange("A4:B4").format = { fill: "#1F3864", font: { name: FONT, bold: true, color: "#FFFFFF" } };
tpl.getRange("A13").values = [["异常与归因（填写）"]];
tpl.getRange("A14").values = [["第1-4周同类差评占比较高，差评集中在同步慢与转写整理困难。第5周起上线同步链路优化与一键转写入口后，同步耗时逐步回落，差评占比随之下降。"]];
tpl.getRange("A13").format.font = { name: FONT, bold: true, size: 11 };
tpl.getRange("A14").format.font = { name: FONT, size: 11 };
tpl.getRange("A16").values = [["优化建议（填写）"]];
tpl.getRange("A17").values = [["继续优化多人会议场景的说话人分离准确率；把一键转写设为录音后的默认动作；跟踪方言与专业词汇的转写准确率。"]];
tpl.getRange("A16").format.font = { name: FONT, bold: true, size: 11 };
tpl.getRange("A17").format.font = { name: FONT, size: 11 };
tpl.getRange("A1:B17").format.autofitColumns();

// ---------- Sheet 4 图表 ----------
const charts = wb.worksheets.add("图表");
const catRange = data.getRange("A3:A14");
const salesRange = data.getRange("B3:B14");
const praiseRange = data.getRange("C3:C14");
const usageRange = data.getRange("D3:D14");

const c1 = charts.charts.add("line", [catRange, salesRange]);
c1.title = "周销量趋势";
c1.titleTextStyle.typeface = FONT;
c1.titleTextStyle.fontSize = 12;
c1.legend = { position: "bottom", textStyle: { typeface: FONT } };
c1.xAxis = { axisType: "textAxis", textStyle: { typeface: FONT, fontSize: 10 } };
c1.yAxis = { numberFormatCode: "#,##0", numberFormatSourceLinked: false, textStyle: { typeface: FONT } };
c1.setPosition("A1", "H14");

const c2 = charts.charts.add("line", [catRange, praiseRange, usageRange]);
c2.title = "好评率与转写使用率趋势";
c2.titleTextStyle.typeface = FONT;
c2.titleTextStyle.fontSize = 12;
c2.legend = { position: "bottom", textStyle: { typeface: FONT } };
c2.xAxis = { axisType: "textAxis", textStyle: { typeface: FONT, fontSize: 10 } };
c2.yAxis = { numberFormatCode: "0%", numberFormatSourceLinked: false, textStyle: { typeface: FONT } };
c2.setPosition("A16", "H30");

wb.recalculate();

const errScan = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!", options: { useRegex: true, maxResults: 100 } });
console.log("error scan:", errScan.ndjson || "none");

const xlsx = await SpreadsheetFile.exportXlsx(wb);
await fs.mkdir(path.dirname(OUT), { recursive: true });
await xlsx.save(OUT);
console.log("saved", OUT);
