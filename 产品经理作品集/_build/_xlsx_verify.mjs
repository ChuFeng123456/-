import { FileBlob, SpreadsheetFile } from "file:///C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";
const input = await FileBlob.load("C:/Users/L1532/Documents/ChatGPT/项目仓库/产品经理作品集/04_讯飞_产品数据周报/科大讯飞AI录音笔产品数据周报.xlsx");
const wb = await SpreadsheetFile.importXlsx(input);
const tpl = wb.worksheets.getItem("周报模板");
console.log("sheets:", wb.worksheets.items ? wb.worksheets.items.length : "n/a");
console.log("B5:", tpl.getRange("B5").values[0][0]);
console.log("B6:", tpl.getRange("B6").values[0][0]);
console.log("B11:", tpl.getRange("B11").values[0][0]);
