// ═══════════════════════════════════════════════════════════════
//  SHBA — Competition Registration · Google Apps Script
//  งาน: SHBA Amigo Championship: Together Through Friendship
//
//  วิธีใช้:
//  1. เปิด Google Sheet → Extensions → Apps Script
//  2. วาง code นี้ทับ Code.gs ทั้งหมด → Save
//  3. Deploy → New Deployment → Web App
//       Execute as: Me  |  Who has access: Anyone
//  4. Copy URL → วางใน main.js (APPS_SCRIPT_URL)
//
//  ⚠️ แก้ code แล้วต้อง Deploy ใหม่ (New Deployment) ทุกครั้ง
// ═══════════════════════════════════════════════════════════════

const SLIP_FOLDER_ID = '1IgX0oS1VoYAGdXRJ9LsoOoM4V8rJFqlo'; // Google Drive folder สำหรับเก็บสลิป

// ── ชื่อ sheets ──────────────────────────────────────────────
const SHEET = {
  REG : 'Registrations',
  NG  : 'New Gen Syrian',
  DW  : 'Special Dwarf',
  PW  : 'Special Poly White',
  FS  : 'Fun Show',
};

// ── map show name → sheet key ─────────────────────────────────
function _showKey(showName) {
  const n = (showName || '').toLowerCase();
  if (n.includes('new gen'))  return 'NG';
  if (n.includes('dwarf'))    return 'DW';
  if (n.includes('poly'))     return 'PW';
  if (n.includes('fun'))      return 'FS';
  return null;
}

// ─── Headers ──────────────────────────────────────────────────
const REG_HEADERS = [
  'หมายเลขใบสมัคร',   // A
  'วันเวลาที่สมัคร',   // B
  'ชื่อ-นามสกุล',      // C
  'ฟาร์ม / เพจ',       // D
  'เบอร์โทร',          // E
  'อีเมล',             // F
  'Member ID',         // G
  'User ID',           // H
  'NG', 'NG จำนวน', 'NG ราคา',   // I J K
  'DW', 'DW จำนวน', 'DW ราคา',   // L M N
  'PW', 'PW จำนวน', 'PW ราคา',   // O P Q
  'FS', 'FS จำนวน', 'FS ราคา',   // R S T
  'รวมแฮม (ตัว)',      // U
  'รวมค่าสมัคร (฿)',   // V
  'ลิงก์สลิป',         // W
  'หมายเหตุ',          // X
  'สถานะ',             // Y
];

// header เดียวกันทุก show sheet
const SHOW_HEADERS = [
  'หมายเลขใบสมัคร',   // A
  'ชื่อ-นามสกุล',      // B
  'ฟาร์ม / เพจ',       // C
  'Member ID',         // D
  'กลุ่ม',             // E  Long Hair / Winter White / Campbell / ...
  'Class',             // F  Self Solid / Agouti Pattern / Normal / ...
  'เพศ',               // G  Male / Female
  'จำนวน',             // H
  'สถานะ',             // I  pending / approved / rejected
];

// ═══════════════════════════════════════════════════════════════
//  Main handler
// ═══════════════════════════════════════════════════════════════
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss   = SpreadsheetApp.getActiveSpreadsheet();

    // ── เตรียม sheets ──────────────────────────────────────────
    const regSheet = _getSheet(ss, SHEET.REG, REG_HEADERS,  _styleReg);
    const ngSheet  = _getSheet(ss, SHEET.NG,  SHOW_HEADERS, _styleShow);
    const dwSheet  = _getSheet(ss, SHEET.DW,  SHOW_HEADERS, _styleShow);
    const pwSheet  = _getSheet(ss, SHEET.PW,  SHOW_HEADERS, _styleShow);
    const fsSheet  = _getSheet(ss, SHEET.FS,  SHOW_HEADERS, _styleShow);
    const showSheets = { NG: ngSheet, DW: dwSheet, PW: pwSheet, FS: fsSheet };

    // ── บันทึกสลิปลง Google Drive ──────────────────────────────
    let slipUrl = '';
    if (data.slipBase64) {
      try {
        const folder   = _getSlipFolder();
        const ext      = (data.slipFileName || 'slip.jpg').split('.').pop() || 'jpg';
        const fileName = `${data.entryNo || 'slip'}.${ext}`;
        const blob     = Utilities.newBlob(
          Utilities.base64Decode(data.slipBase64),
          data.slipMime || 'image/jpeg',
          fileName
        );
        const file = folder.createFile(blob);
        slipUrl = `https://drive.google.com/file/d/${file.getId()}/view`;
        try {
          file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
        } catch(shareErr) {
          Logger.log('Sharing error (link still saved): ' + shareErr.toString());
        }
        Logger.log('slipUrl: ' + slipUrl);
      } catch(slipErr) {
        Logger.log('Drive slip error: ' + slipErr.toString());
      }
    }

    // ── Parse shows ────────────────────────────────────────────
    const shows = JSON.parse(data.shows || '[]');
    const sMap  = {};
    shows.forEach(s => {
      const k = _showKey(s.show);
      if (k) sMap[k] = s;
    });

    const g = k => {
      const s = sMap[k];
      return s ? { sel:'Y', cnt: s.count||0, cost: s.cost||0 }
               : { sel:'N', cnt: 0,          cost: 0          };
    };
    const ng=g('NG'), dw=g('DW'), pw=g('PW'), fs=g('FS');

    // ── Sheet: Registrations (1 row ต่อใบสมัคร) ───────────────
    regSheet.appendRow([
      data.entryNo     || '',
      data.submittedAt || '',
      data.owner       || '',
      data.farm        || '',
      data.phone       || '',
      data.userEmail   || '',
      data.memberId    || '',
      data.userId      || '',
      ng.sel, ng.cnt, ng.cost,
      dw.sel, dw.cnt, dw.cost,
      pw.sel, pw.cnt, pw.cost,
      fs.sel, fs.cnt, fs.cost,
      Number(data.totalHamsters) || 0,
      Number(data.totalFee)      || 0,
      slipUrl,
      data.note || '',
      'pending',
    ]);

    // ── Show sheets (1 row ต่อ 1 class entry) ──────────────────
    shows.forEach(s => {
      const key   = _showKey(s.show);
      const sheet = key ? showSheets[key] : null;
      if (!sheet) return;

      (s.classes || []).forEach(c => {
        if (!c.count || c.count <= 0) return;

        // parse "Long Hair · Self Solid ♂" → group / class / gender
        const label  = c.class || '';
        const dotIdx = label.indexOf(' · ');
        let group = '', classGender = '';
        if (dotIdx >= 0) {
          group       = label.substring(0, dotIdx).trim();
          classGender = label.substring(dotIdx + 3).trim();
        } else {
          group       = s.show || '';
          classGender = label;
        }

        let gender    = '';
        let className = classGender;
        if (classGender.endsWith('♂')) {
          gender = 'Male';  className = classGender.slice(0, -1).trim();
        } else if (classGender.endsWith('♀')) {
          gender = 'Female'; className = classGender.slice(0, -1).trim();
        }

        sheet.appendRow([
          data.entryNo  || '',
          data.owner    || '',
          data.farm     || '',
          data.memberId || '',
          group,
          className,
          gender,
          c.count,
          'pending',
        ]);
      });
    });

    return _ok({ entryNo: data.entryNo, slipUrl });

  } catch (err) {
    Logger.log('SHBA doPost error: ' + err.toString());
    return _err(err.toString());
  }
}

// ─── Allow CORS preflight ──────────────────────────────────────
function doOptions(e) {
  return ContentService.createTextOutput('').setMimeType(ContentService.MimeType.TEXT);
}

// ─── Google Drive ──────────────────────────────────────────────
function _getSlipFolder() {
  return DriveApp.getFolderById(SLIP_FOLDER_ID);
}

// ── ทดสอบ Drive access (รันใน Apps Script editor เพื่อ authorize) ──
function testDriveAccess() {
  try {
    const folder = DriveApp.getFolderById(SLIP_FOLDER_ID);
    Logger.log('✅ Drive access OK — folder: ' + folder.getName());
  } catch(e) {
    Logger.log('❌ Drive error: ' + e.toString());
  }
}

// ─── Sheet helpers ─────────────────────────────────────────────
function _getSheet(ss, name, headers, styleFn) {
  let sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    sheet.appendRow(headers);
    styleFn(sheet, headers.length);
  } else if (sheet.getLastRow() === 0) {
    sheet.appendRow(headers);
    styleFn(sheet, headers.length);
  }
  return sheet;
}

function _styleReg(sheet, len) {
  sheet.getRange(1,1,1,len)
    .setBackground('#1B1B2F').setFontColor('#FFD700').setFontWeight('bold').setFontSize(10);
  sheet.setFrozenRows(1);
  sheet.setColumnWidth(1,160); sheet.setColumnWidth(2,170);
  sheet.setColumnWidth(3,160); sheet.setColumnWidth(6,200);
  sheet.setColumnWidth(23,300);
}

function _styleShow(sheet, len) {
  const bg = {
    'New Gen Syrian'     : { bg:'#1B2B1B', fg:'#90EE90' },
    'Special Dwarf'      : { bg:'#1B1B2B', fg:'#ADD8E6' },
    'Special Poly White' : { bg:'#2B2B2B', fg:'#E0E0E0' },
    'Fun Show'           : { bg:'#2B1B0F', fg:'#FFD700' },
  };
  const name   = sheet.getName();
  const colors = bg[name] || { bg:'#1B1B2F', fg:'#FFD700' };
  sheet.getRange(1,1,1,len)
    .setBackground(colors.bg).setFontColor(colors.fg).setFontWeight('bold').setFontSize(10);
  sheet.setFrozenRows(1);
  sheet.setColumnWidth(1,160); sheet.setColumnWidth(2,160);
  sheet.setColumnWidth(3,140); sheet.setColumnWidth(4,140);
  sheet.setColumnWidth(5,160); sheet.setColumnWidth(6,80);
  sheet.setColumnWidth(7,70);
}

// ─── Response helpers ──────────────────────────────────────────
function _ok(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(Object.assign({ status:'ok' }, obj)))
    .setMimeType(ContentService.MimeType.JSON);
}
function _err(msg) {
  return ContentService
    .createTextOutput(JSON.stringify({ status:'error', message: msg }))
    .setMimeType(ContentService.MimeType.JSON);
}
