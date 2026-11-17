import { Workbook, SpreadsheetFile, FileBlob } from "file:///C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";
console.log("keys:", Object.keys({ Workbook, SpreadsheetFile, FileBlob }));
const wb = Workbook.create();
const s = wb.worksheets.add("Sheet1");
s.getRange("A1").values = [["hello"]];
console.log("sheet ok:", wb.worksheets.getItem("Sheet1").name);
