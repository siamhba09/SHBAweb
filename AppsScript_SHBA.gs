// ============================================================
//  SHBA — Competition Entry to Google Sheet
//  วิธีใช้:
//  1. เปิด https://script.google.com → New Project
//  2. วาง code นี้ทั้งหมด
//  3. แก้ SHEET_ID ด้านล่างให้ตรงกับ Google Sheet ของคุณ
//  4. Deploy → New Deployment → Web App
//     - Execute as: Me
//     - Who has access: Anyone
//  5. Copy "Web App URL" → วางใน main.js บรรทัด APPS_SCRIPT_URL
// ============================================================

const SHEET_ID   = '1Cn87CucmIW21JwkfJ9JsNmRe7PnWLt3O7WE1wJsiE7U';
const SHEET_NAME = 'competitions';               // ← ชื่อ sheet tab

// หัวตาราง (สร้างอัตโนมัติถ้ายังไม่มี)
const HEADERS = [
  'หมายเลขประกวด',
  'วันที่-เวลาสมัคร',
  'ชื่อ-นามสกุลเจ้าของ',
  'หมายเลขสมาชิก',
  'ชื่อแฮมสเตอร์',
  'สายพันธุ์',
  'สี',
  'แพตเทิร์น',
  'ประเภทขน',
  'เพศ',
  'อายุ (สัปดาห์)',
  'น้ำหนัก (กรัม)',
  'ประเภทการแข่งขัน',
];

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss    = SpreadsheetApp.openById(SHEET_ID);
    let sheet   = ss.getSheetByName(SHEET_NAME);

    // สร้าง sheet ใหม่ถ้ายังไม่มี
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(HEADERS);
      sheet.getRange(1, 1, 1, HEADERS.length)
        .setBackground('#C9A227')
        .setFontColor('#000000')
        .setFontWeight('bold');
      sheet.setFrozenRows(1);
    }

    // เพิ่มแถวข้อมูล
    sheet.appendRow([
      data.entryNo      || '',
      data.submittedAt  || '',
      data.owner        || '',
      data.memberId     || '',
      data.hamsterName  || '',
      data.breed        || '',
      data.color        || '',
      data.pattern      || '',
      data.coat         || '',
      data.sex          || '',
      data.age          || '',
      data.weight       || '',
      data.compClass    || '',
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok', entry: data.entryNo }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// ทดสอบด้วย GET (ดูว่า script ทำงานได้)
function doGet() {
  return ContentService
    .createTextOutput('SHBA Competition Entry Script is running ✅')
    .setMimeType(ContentService.MimeType.TEXT);
}
