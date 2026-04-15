// ============================================================
//  SHBA — Competition Entry to Google Sheet  v2.0
//  (รองรับ multi-show registration จากฟอร์มใหม่)
//
//  วิธี Deploy ใหม่:
//  1. เปิด https://script.google.com → เลือก project เดิม
//  2. แทนที่ code ทั้งหมดด้วยไฟล์นี้
//  3. Deploy → Manage Deployments → แก้ไข deployment เดิม
//     → "New Version" → Deploy
//     (URL เดิมยังใช้ได้ — ไม่ต้องเปลี่ยน main.js)
// ============================================================

const SHEET_ID    = '1Cn87CucmIW21JwkfJ9JsNmRe7PnWLt3O7WE1wJsiE7U';
const SHEET_NAME  = 'competitions';   // ชื่อ tab ใน Google Sheet
const DETAIL_NAME = 'class_detail';   // tab เก็บรายละเอียด class แบบ per-row

// ── หัวตาราง main sheet (1 row = 1 การสมัคร) ──────────────────
const HEADERS = [
  'หมายเลขประกวด',       // A
  'วันที่-เวลาสมัคร',     // B
  'ชื่อ-นามสกุล',         // C
  'ชื่อฟาร์ม/เพจ',        // D
  'เบอร์โทร',             // E
  'หมายเลขสมาชิก',       // F
  'Shows ที่สมัคร',       // G
  'จำนวนแฮมสเตอร์',      // H
  'ค่าสมัครรวม (บาท)',    // I
  'Bundle 4 Shows',       // J
  'สรุป Class',           // K
  'หมายเหตุ',             // L
  'สถานะ',               // M
];

// ── หัวตาราง detail sheet (1 row = 1 show ใน 1 การสมัคร) ──────
const DETAIL_HEADERS = [
  'หมายเลขประกวด',   // A
  'ชื่อ-นามสกุล',    // B
  'ชื่อฟาร์ม/เพจ',   // C
  'เบอร์โทร',        // D
  'Show',            // E
  'ราคา (บาท)',      // F
  'รูปแบบ',         // G  perhead / unlimited
  'จำนวนตัว',       // H
  'รายละเอียด Class', // I
  'วันที่สมัคร',     // J
];

// ─────────────────────────────────────────────────────────────
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss   = SpreadsheetApp.openById(SHEET_ID);

    // ── เตรียม sheet หลัก ──────────────────────────────────
    const sheet = _getOrCreateSheet(ss, SHEET_NAME, HEADERS, '#C9A227');

    // ── parse shows ────────────────────────────────────────
    let showsData = [];
    try { showsData = JSON.parse(data.shows || '[]'); } catch(_) {}

    const showNames = showsData.map(s => _shortName(s.show)).join(', ');

    // สรุป class แบบ readable
    const classSummary = showsData.map(s => {
      const cls = (s.classes || []).map(c => `${c.class}×${c.count}`).join(', ');
      return _shortName(s.show) + ': ' + (cls || '(เหมา)');
    }).join(' | ');

    // ── append row หลัก ────────────────────────────────────
    sheet.appendRow([
      data.entryNo        || '',
      data.submittedAt    || '',
      data.owner          || '',
      data.farm           || '',
      data.phone          || '',
      data.memberId       || '',
      showNames,
      Number(data.totalHamsters) || 0,
      Number(data.totalFee)      || 0,
      data.bundleApplied  ? '✅ Bundle' : '',
      classSummary,
      data.note           || '',
      'รอยืนยัน',
    ]);

    // ── append detail rows (1 row per show) ────────────────
    const detailSheet = _getOrCreateSheet(ss, DETAIL_NAME, DETAIL_HEADERS, '#2c5f8a');
    showsData.forEach(s => {
      const cls = (s.classes || []).map(c => `${c.class}(${c.count})`).join(', ');
      detailSheet.appendRow([
        data.entryNo     || '',
        data.owner       || '',
        data.farm        || '',
        data.phone       || '',
        s.show           || '',
        Number(s.cost)   || 0,
        s.mode === 'unlimited' ? 'เหมา' : 'รายตัว',
        Number(s.count)  || 0,
        cls              || '-',
        data.submittedAt || '',
      ]);
    });

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok', entry: data.entryNo }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// ── ทดสอบด้วย GET ───────────────────────────────────────────
function doGet() {
  return ContentService
    .createTextOutput('SHBA Competition Entry Script v2.0 ✅ — Running OK')
    .setMimeType(ContentService.MimeType.TEXT);
}

// ── Helper: ตัดชื่อ Show ให้สั้นลง ─────────────────────────
function _shortName(name) {
  if (!name) return '';
  return name
    .replace('The Syrian Hamster Showcase (Open League)', 'Open League')
    .replace('The Syrian Hamster Showcase', 'Open League')
    .replace('Extreme Dilute Specialty Show', 'Extreme Dilute')
    .replace('Polywhite Specialty Show', 'Polywhite')
    .replace('New Gen Syrian Hamster Show', 'New Gen');
}

// ── Helper: สร้าง / หา sheet ───────────────────────────────
function _getOrCreateSheet(ss, name, headers, headerColor) {
  let sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    sheet.appendRow(headers);
    const range = sheet.getRange(1, 1, 1, headers.length);
    range.setBackground(headerColor || '#444444')
         .setFontColor('#ffffff')
         .setFontWeight('bold');
    sheet.setFrozenRows(1);
    // auto-resize columns
    for (let i = 1; i <= headers.length; i++) {
      sheet.setColumnWidth(i, 150);
    }
  }
  return sheet;
}
