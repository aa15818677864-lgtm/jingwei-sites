const SHEET_NAME = 'Leads';
const HEADERS = [
  'submitted_at',
  'site',
  'language',
  'page_title',
  'page_url',
  'name',
  'area_code',
  'phone',
  'wechat',
  'inquiry_type',
  'message',
  'source',
  'user_agent'
];

function setupSheet() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = spreadsheet.insertSheet(SHEET_NAME);
  }

  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.setFrozenRows(1);
  }
}

function doGet() {
  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  setupSheet();

  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
  const row = HEADERS.map(function (header) {
    return getParam_(e, header);
  });

  if (!row[0]) {
    row[0] = new Date().toISOString();
  }

  sheet.appendRow(row);

  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

function getParam_(e, key) {
  if (!e || !e.parameter) {
    return '';
  }

  return e.parameter[key] || '';
}
