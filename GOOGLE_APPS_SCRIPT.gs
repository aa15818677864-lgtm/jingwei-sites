const SHEET_NAME = 'Leads';
const NOTIFY_EMAIL = '842598522@qq.com';

const FIELD_KEYS = [
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
  'user_agent',
  'client_ip'
];

const DISPLAY_HEADERS = [
  '\u63d0\u4ea4\u65f6\u95f4',
  '\u7ad9\u70b9',
  '\u8bed\u8a00',
  '\u9875\u9762\u6807\u9898',
  '\u9875\u9762\u94fe\u63a5',
  '\u79f0\u547c',
  '\u533a\u53f7',
  '\u8054\u7cfb\u7535\u8bdd',
  '\u5fae\u4fe1',
  '\u54a8\u8be2\u4e8b\u9879',
  '\u7559\u8a00\u5185\u5bb9',
  '\u6765\u6e90',
  '\u6d4f\u89c8\u5668\u4fe1\u606f',
  '\u5ba2\u6237IP'
];

function setupSheet() {
  const sheet = getOrCreateSheet_();
  updateHeaderRow_(sheet);
  sheet.setFrozenRows(1);
  sheet.autoResizeColumns(1, DISPLAY_HEADERS.length);
}

function prepareSheet() {
  const sheet = getOrCreateSheet_();
  updateHeaderRow_(sheet);

  const removed = removeDiagnosticRows_(sheet);
  sheet.setFrozenRows(1);
  sheet.autoResizeColumns(1, DISPLAY_HEADERS.length);

  Logger.log('Removed diagnostic rows: ' + removed);
}

function cleanupDiagnosticRows() {
  const sheet = getOrCreateSheet_();
  const removed = removeDiagnosticRows_(sheet);
  Logger.log('Removed diagnostic rows: ' + removed);
}

function doGet() {
  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  const sheet = getOrCreateSheet_();
  updateHeaderRow_(sheet);

  const row = FIELD_KEYS.map(function (key) {
    return getParam_(e, key);
  });

  if (!row[0]) {
    row[0] = new Date().toISOString();
  }

  sheet.appendRow(row);
  sendNotificationEmail_(row);

  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

function getOrCreateSheet_() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = spreadsheet.insertSheet(SHEET_NAME);
  }

  return sheet;
}

function updateHeaderRow_(sheet) {
  sheet.getRange(1, 1, 1, DISPLAY_HEADERS.length).setValues([DISPLAY_HEADERS]);
}

function removeDiagnosticRows_(sheet) {
  const lastRow = sheet.getLastRow();
  if (lastRow <= 1) {
    return 0;
  }

  const values = sheet.getRange(2, 1, lastRow - 1, FIELD_KEYS.length).getValues();
  let removed = 0;

  for (let index = values.length - 1; index >= 0; index -= 1) {
    const site = String(values[index][1] || '').toLowerCase();
    const source = String(values[index][11] || '').toLowerCase();

    if (site === 'diag' || source === 'diagnostic') {
      sheet.deleteRow(index + 2);
      removed += 1;
    }
  }

  return removed;
}

function sendNotificationEmail_(row) {
  const record = {};

  FIELD_KEYS.forEach(function (key, index) {
    record[key] = row[index] || '';
  });

  const siteLabel = getSiteLabel_(record.site);
  const inquiryLabel = record.inquiry_type || record.page_title || '\u8868\u5355\u63d0\u4ea4';
  const subject = '\u65b0\u5ba2\u6237\u54a8\u8be2 - ' + (record.name || '\u672a\u586b\u5199') + ' - ' + inquiryLabel;
  const phoneDisplay = formatPhone_(record.area_code, record.phone);
  const plainBody = [
    siteLabel,
    '',
    '\u9759\u4e3a\u5f8b\u5e08\u4e8b\u52a1\u6240 - \u65b0\u5ba2\u6237\u54a8\u8be2\u901a\u77e5',
    '',
    '\u63d0\u4ea4\u65f6\u95f4: ' + formatDateTime_(record.submitted_at),
    '',
    '\u6765\u6e90\u9875\u9762: ' + (record.page_title || ''),
    '',
    '\u6765\u6e90\u9875\u9762URL: ' + (record.page_url || ''),
    '',
    '\u5ba2\u6237\u79f0\u547c: ' + (record.name || ''),
    '',
    '\u8054\u7cfb\u7535\u8bdd: ' + phoneDisplay,
    '',
    '\u5fae\u4fe1\u8d26\u53f7: ' + (record.wechat || ''),
    '',
    '\u54a8\u8be2\u4e8b\u9879: ' + (record.inquiry_type || ''),
    '',
    '\u5ba2\u6237\u7559\u8a00: ' + (record.message || ''),
    '',
    '\u5ba2\u6237IP: ' + (record.client_ip || ''),
    '',
    '\u6765\u6e90: ' + (record.source || '')
  ].join('\n');

  const htmlBody = [
    '<div style="font-family:Arial,PingFang SC,Microsoft YaHei,sans-serif;line-height:1.8;color:#222;">',
    '<p style="margin:0 0 18px;font-size:18px;color:#159570;">' + escapeHtml_(siteLabel) + '</p>',
    '<p style="margin:0 0 20px;font-size:24px;font-weight:700;">\u9759\u4e3a\u5f8b\u5e08\u4e8b\u52a1\u6240 - \u65b0\u5ba2\u6237\u54a8\u8be2\u901a\u77e5</p>',
    buildFieldHtml_('\u63d0\u4ea4\u65f6\u95f4', formatDateTime_(record.submitted_at)),
    buildFieldHtml_('\u6765\u6e90\u9875\u9762', record.page_title || ''),
    buildLinkFieldHtml_('\u6765\u6e90\u9875\u9762URL', record.page_url || ''),
    buildFieldHtml_('\u5ba2\u6237\u79f0\u547c', record.name || ''),
    buildFieldHtml_('\u8054\u7cfb\u7535\u8bdd', phoneDisplay),
    buildFieldHtml_('\u5fae\u4fe1\u8d26\u53f7', record.wechat || ''),
    buildFieldHtml_('\u54a8\u8be2\u4e8b\u9879', record.inquiry_type || ''),
    buildFieldHtml_('\u5ba2\u6237\u7559\u8a00', record.message || ''),
    buildFieldHtml_('\u5ba2\u6237IP', record.client_ip || ''),
    '</div>'
  ].join('');

  try {
    MailApp.sendEmail({
      to: NOTIFY_EMAIL,
      subject: subject,
      body: plainBody,
      htmlBody: htmlBody
    });
  } catch (error) {
    Logger.log('Email send failed: ' + error);
  }
}

function getSiteLabel_(site) {
  const siteLabelMap = {
    ml: '\u9759\u4e3a\u5f8b\u5e08\u4e8b\u52a1\u6240\u7f51\u7ad9 - \u9a6c\u6765\u897f\u4e9a\u7ad9',
    xj: '\u9759\u4e3a\u5f8b\u5e08\u4e8b\u52a1\u6240\u7f51\u7ad9 - \u65b0\u52a0\u5761\u7ad9'
  };

  return siteLabelMap[String(site || '').toLowerCase()] || '\u9759\u4e3a\u5f8b\u5e08\u4e8b\u52a1\u6240\u7f51\u7ad9';
}

function formatPhone_(areaCode, phone) {
  if (areaCode && phone) {
    return areaCode + ' ' + phone;
  }

  return areaCode || phone || '';
}

function buildFieldHtml_(label, value) {
  return '<p style="margin:0 0 16px;font-size:16px;"><strong>' + escapeHtml_(label) + ':</strong> ' + escapeHtml_(value || '') + '</p>';
}

function buildLinkFieldHtml_(label, value) {
  const escapedLabel = escapeHtml_(label);
  const escapedValue = escapeHtml_(value || '');

  if (!value) {
    return '<p style="margin:0 0 16px;font-size:16px;"><strong>' + escapedLabel + ':</strong> </p>';
  }

  return '<p style="margin:0 0 16px;font-size:16px;"><strong>' + escapedLabel + ':</strong> <a href="' + escapedValue + '">' + escapedValue + '</a></p>';
}

function formatDateTime_(value) {
  if (!value) {
    return '';
  }

  const date = new Date(value);
  if (isNaN(date.getTime())) {
    return String(value);
  }

  return Utilities.formatDate(
    date,
    Session.getScriptTimeZone() || 'Asia/Shanghai',
    'yyyy-MM-dd HH:mm:ss'
  );
}

function escapeHtml_(value) {
  return String(value || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function getParam_(e, key) {
  if (!e || !e.parameter) {
    return '';
  }

  return e.parameter[key] || '';
}
