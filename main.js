/* ================================================================
   THAILAND HAMSTER ASSOCIATION — main.js
   Shared: data, utilities, render functions, navbar, toast, scroll
   ================================================================ */
'use strict';

/* ─── DATA ──────────────────────────────────────────────────────── */
const SYRIAN_AGOUTI = [
  { name:'Golden',   genotype:'aa',        emoji:'🟡', desc:'สีทองธรรมชาติ ท้องสีครีม', eye:'ดำ', ear:'สีเนื้อ', bg:'#C8A020' },
  { name:'Yellow',   genotype:'aa To/+',   emoji:'🟠', desc:'สีเหลืองสด พบได้ยาก', eye:'ดำ', ear:'สีเนื้อ', bg:'#E8A030' },
  { name:'Cinnamon', genotype:'aa pp',     emoji:'🟤', desc:'สีน้ำตาลอบเชย สีตาแดง', eye:'แดง', ear:'ชมพู', bg:'#A0522D' },
  { name:'Grey',     genotype:'aa dg/dg',  emoji:'🩶', desc:'สีเทาเข้ม สีทองบนหน้า', eye:'ดำ', ear:'สีเนื้อ', bg:'#708090' },
  { name:'Honey',    genotype:'aa Ru/+',   emoji:'🍯', desc:'สีน้ำผึ้ง ท้องสีขาว', eye:'ดำ', ear:'สีเนื้อ', bg:'#D4A020' },
  { name:'Rust',     genotype:'aa ru/ru',  emoji:'🦊', desc:'สีสนิมเหล็ก น้ำตาลแดง', eye:'ดำ', ear:'สีเนื้อ', bg:'#8B3A15' },
];
const SYRIAN_SELF = [
  { name:'Black',         genotype:'A/A',      emoji:'⬛', desc:'สีดำสนิท เงางาม', eye:'ดำ', ear:'ดำ', bg:'#111' },
  { name:'Cream (BE)',    genotype:'ee',        emoji:'🍦', desc:'ครีมสีตาดำ', eye:'ดำ', ear:'สีเนื้อ', bg:'#FFFACD' },
  { name:'Cream (RE)',    genotype:'ee pp',     emoji:'🤍', desc:'ครีมสีตาแดง', eye:'แดง', ear:'ชมพู', bg:'#FFF5E1' },
  { name:'Mink',          genotype:'pp',        emoji:'🤎', desc:'น้ำตาลมิงค์ สีตาแดง', eye:'แดง', ear:'ชมพู', bg:'#6B3A2A' },
  { name:'Sable',         genotype:'e/e',       emoji:'🫚', desc:'น้ำตาลเข้มอมดำ ท้องครีม', eye:'ดำ', ear:'สีเนื้อ', bg:'#2C1A0E' },
  { name:'Chocolate',     genotype:'bb',        emoji:'🍫', desc:'สีช็อคโกแลต อุ่น', eye:'แดง', ear:'ชมพู', bg:'#4A1C10' },
  { name:'Dove',          genotype:'pp dg/dg',  emoji:'🕊️', desc:'เทาอ่อน สีตาแดง', eye:'แดง', ear:'ชมพู', bg:'#B0A0A8' },
  { name:'Lilac',         genotype:'pp bb',     emoji:'💜', desc:'ม่วงอ่อน สีตาแดง', eye:'แดง', ear:'ชมพู', bg:'#9B8FA8' },
  { name:'Copper',        genotype:'aa Ru/ru',  emoji:'🟥', desc:'น้ำตาลทองแดง', eye:'ดำ', ear:'สีเนื้อ', bg:'#B87333' },
];
const DWARF_WW = [
  { name:'Normal',        genotype:'s+/s+',     emoji:'🐹', desc:'เทาเข้ม ท้องขาว', bg:'#888' },
  { name:'Sapphire',      genotype:'s/s+',      emoji:'💎', desc:'เทาอ่อนอมฟ้า', bg:'#6A8FAF' },
  { name:'Pearl',         genotype:'Pe/+',      emoji:'🤍', desc:'ขาวแซมเทา เหมือนไข่มุก', bg:'#E8E8E0' },
  { name:'Sapphire Pearl',genotype:'s/s Pe/+',  emoji:'🩵', desc:'ผสมเทา-ฟ้า-ขาว', bg:'#9AB8D0' },
];
const DWARF_CAMP = [
  { name:'Normal',  genotype:'+/+',   emoji:'🐹', desc:'น้ำตาลเทา สายหลัง', bg:'#9B8060' },
  { name:'Argente', genotype:'Arg',   emoji:'🟡', desc:'ทองอ่อน สีตาแดง', bg:'#D4A050' },
  { name:'Albino',  genotype:'cc',    emoji:'⬜', desc:'ขาวสนิท สีตาแดง', bg:'#F5F5F5' },
  { name:'Opal',    genotype:'opal',  emoji:'🔵', desc:'เทาอมฟ้า สีตาแดง', bg:'#708090' },
  { name:'Black',   genotype:'mink mink', emoji:'⬛', desc:'ดำหรือเข้มมาก', bg:'#1A1A1A' },
];
const DWARF_ROBO = [
  { name:'Normal',    genotype:'+/+',   emoji:'🐹', desc:'ทรายน้ำตาล ท้องขาว', bg:'#C8A878' },
  { name:'White Face',genotype:'WF/+',  emoji:'😊', desc:'หน้าขาว บนสีปกติ', bg:'#D4B890' },
  { name:'Husky',     genotype:'WF/WF', emoji:'🤍', desc:'ขาวผสมทราย', bg:'#E8E0D0' },
];
const PATTERNS = [
  { name:'Dominant Spot', gene:'To/+ (ยีนเด่น)', emoji:'⚪', dominant:true,
    desc:'ขาวมีจุดสีกระจาย โฮโมไซกัส (To/To) ไม่มีชีวิต ต้องใช้เป็น To/+ เท่านั้น' },
  { name:'Banded',        gene:'Dh/+ (ยีนเด่น)', emoji:'⬜', dominant:true,
    desc:'แถบสีขาวรอบเอว ยีนเด่น Dh โฮโมไซกัสมีปัญหาสุขภาพ' },
  { name:'Tortoiseshell', gene:'To/+ เฉพาะตัวเมีย', emoji:'🟡', dominant:false,
    desc:'แต้มสีเหลือง/ส้มบนพื้นสีหลัก เกิดเฉพาะในแฮมสเตอร์ตัวเมีย' },
  { name:'Roan',          gene:'Ro/+ (ยีนเด่น)', emoji:'🌫️', dominant:true,
    desc:'ขนสีผสมขาวกระจายทั่วตัว โฮโมไซกัสไม่มีชีวิต' },
];
const COAT_TYPES = [
  { name:'Short Hair',  gene:'L/L (ยีนเด่น)', emoji:'🐹',
    desc:'ขนสั้นมาตรฐาน เนื้อขนแน่น เงางาม รูปแบบพื้นฐาน' },
  { name:'Long Hair (Teddy / Angora)', gene:'l/l (ยีนด้อย)', emoji:'🧸',
    desc:'ขนยาวฟู ต้องได้รับยีน l จากทั้งพ่อและแม่ ต้องแปรงสม่ำเสมอ' },
  { name:'Rex',   gene:'Re/+ (ยีนเด่น)', emoji:'🌀',
    desc:'ขนหยิกเป็นคลื่น หนวดหยิก ยีนเด่น ลูกครึ่ง Rex ก็แสดงออก' },
  { name:'Satin', gene:'Sa/+ (ยีนเด่น)', emoji:'✨',
    desc:'ขนเงาวาวมาก บางกว่าปกติ สีดูเข้มกว่า โฮโมไซกัสขนบาง' },
];
const EVENTS = [
  { id:1, name:'SHBA Summer Championship 2026', day:'14–15', month:'JUN',
    location:'ศูนย์การประชุมแห่งชาติสิริกิติ์, กทม.',
    classes:['Best in Show','Best Syrian','Best Dwarf','Pet & Fun'],
    fee:300, deadline:'31 พ.ค. 2026', judges:['ผศ.ดร. วิภาวรรณ ชัยนคร','นายสมพร ทองคำ'],
    status:'open', emoji:'🏆' },
  { id:2, name:'SHBA Regional Show — เชียงใหม่', day:'20', month:'JUL',
    location:'เชียงใหม่ฮอลล์, เชียงใหม่',
    classes:['Best Syrian','Best Dwarf'],
    fee:200, deadline:'10 ก.ค. 2026', judges:['นางสาวรัตนา สมบูรณ์'],
    status:'upcoming', emoji:'🌸' },
  { id:3, name:'SHBA Winter Classic 2025', day:'13–14', month:'DEC',
    location:'ไบเทค บางนา, กทม.',
    classes:['Best in Show','Best Syrian','Best Dwarf','Best Coat','Pet & Fun'],
    fee:300, deadline:'ปิดรับสมัครแล้ว',
    judges:['ผศ.ดร. วิภาวรรณ ชัยนคร','Mr. John Smith (UK)'],
    status:'past', emoji:'❄️' },
  { id:4, name:'SHBA Specialty — Dwarf Only', day:'9', month:'AUG',
    location:'คริสตัล ดีไซน์ เซ็นเตอร์, กทม.',
    classes:['Best Dwarf','Best Winter White','Best Campbell','Best Robo'],
    fee:200, deadline:'31 ก.ค. 2026', judges:['นายประสิทธิ์ มาศวงศ์'],
    status:'upcoming', emoji:'⭐' },
];
const KNOWLEDGE_ARTICLES = [
  { title:'คู่มือมือใหม่: สิ่งที่ต้องเตรียมก่อนเลี้ยงแฮมสเตอร์', emoji:'📖', tag:'beginner', cat:'มือใหม่',
    desc:'ทุกสิ่งที่ต้องรู้ก่อนรับแฮมสเตอร์มาเลี้ยง ตั้งแต่กรง อุปกรณ์ ไปจนถึงการเตรียมบ้าน', date:'8 เม.ย. 2026', readTime:'10 นาที' },
  { title:'อาหารที่ดีที่สุดสำหรับแฮมสเตอร์ Syrian', emoji:'🥦', tag:'food', cat:'อาหาร',
    desc:'อาหารหลัก อาหารเสริม ผักผลไม้ที่กินได้ และที่ควรหลีกเลี่ยงเด็ดขาด', date:'5 เม.ย. 2026', readTime:'8 นาที' },
  { title:'ทำความเข้าใจ Dwarf Hamster ทั้ง 3 สายพันธุ์', emoji:'🐾', tag:'beginner', cat:'สายพันธุ์',
    desc:'ความแตกต่างระหว่าง Winter White, Campbell\'s และ Roborovski พร้อมข้อดีข้อเสีย', date:'1 เม.ย. 2026', readTime:'12 นาที' },
  { title:'การผสมพันธุ์อย่างมีความรับผิดชอบ', emoji:'🧬', tag:'breeding', cat:'การเพาะพันธุ์',
    desc:'หลักการเพาะพันธุ์ที่ดี การเลือกคู่ผสม การดูแลแม่และลูก', date:'28 มี.ค. 2026', readTime:'15 นาที' },
  { title:'เตรียมแฮมสเตอร์สำหรับการประกวด', emoji:'🏆', tag:'show', cat:'การประกวด',
    desc:'เทคนิคการดูแลขน โภชนาการ และการสร้างความคุ้นเคยกับการจัดการ', date:'22 มี.ค. 2026', readTime:'10 นาที' },
  { title:'พื้นฐาน Genetics: ยีนสีของ Syrian Hamster', emoji:'🔬', tag:'genetics', cat:'พันธุกรรม',
    desc:'อธิบาย Genotype, Phenotype และการถ่ายทอดยีนแบบเข้าใจง่าย', date:'15 มี.ค. 2026', readTime:'20 นาที' },
];
const SPECIES_DATA = [
  { name:'Syrian Hamster', sci:'Mesocricetus auratus', emoji:'🐹',
    size:'13–18 ซม.', weight:'85–150 ก.', lifespan:'2–3 ปี', origin:'ซีเรีย', social:'เดี่ยว', notes:'สายพันธุ์ใหญ่ที่สุด เลี้ยงคนเดียวเท่านั้น' },
  { name:'Winter White Dwarf', sci:'Phodopus sungorus', emoji:'⬜',
    size:'7–10 ซม.', weight:'20–45 ก.', lifespan:'1.5–2.5 ปี', origin:'รัสเซีย', social:'คู่/กลุ่มเล็ก', notes:'ขนเปลี่ยนเป็นขาวในฤดูหนาว' },
  { name:"Campbell's Dwarf", sci:'Phodopus campbelli', emoji:'🤎',
    size:'7–10 ซม.', weight:'20–45 ก.', lifespan:'1.5–2.5 ปี', origin:'มองโกเลีย', social:'คู่/กลุ่มเล็ก', notes:'ใกล้ชิด Winter White มาก อาจผสมข้ามสายพันธุ์' },
  { name:'Roborovski Dwarf', sci:'Phodopus roborovskii', emoji:'🌰',
    size:'4.5–5 ซม.', weight:'15–25 ก.', lifespan:'3–3.5 ปี', origin:'มองโกเลีย', social:'กลุ่ม', notes:'เล็กที่สุด วิ่งเร็วที่สุด มีชีวิตยืนยาวที่สุด' },
  { name:'Chinese Hamster', sci:'Cricetulus griseus', emoji:'🐭',
    size:'10–12 ซม.', weight:'30–45 ก.', lifespan:'2–3 ปี', origin:'จีน', social:'เดี่ยว', notes:'หางยาวกว่าสายพันธุ์อื่น คล่องแคล่ว' },
];
const HOF_DATA = [
  { rank:'🥇', name:'"Golden Sunrise"', owner:'ฟาร์มรุ่งอรุณ', breed:'Syrian · Cinnamon Satin', year:'2025' },
  { rank:'🥇', name:'"Pearl Princess"', owner:'สมหญิง ชัยชนะ',  breed:'Winter White · Pearl',  year:'2024' },
  { rank:'🥇', name:'"Midnight Shadow"',owner:'ฟาร์มดาวค้ำ',    breed:'Syrian · Black Long Hair',year:'2023' },
  { rank:'🥇', name:'"Honey Dream"',    owner:'วีรวุฒิ สุขสวัสดิ์',breed:'Syrian · Honey Banded', year:'2022' },
  { rank:'🥇', name:'"Blue Moon"',      owner:'ฟาร์มสายรุ้ง',   breed:'W.White · Sapphire',    year:'2021' },
  { rank:'🥇', name:'"Ruby Fire"',      owner:'ปทุมวดี แสนสุข',  breed:'Syrian · Cinnamon Rex', year:'2020' },
];
const NEWS_DATA = [
  { title:'ประกาศผล SHBA Spring Show 2026 อย่างเป็นทางการ', emoji:'📢', cat:'ข่าวสาร', date:'16 มี.ค. 2026',
    excerpt:'เปิดเผยผู้ชนะ Best in Show และผลรางวัลทั้งหมดจากงาน SHBA Spring Show 2026', featured:true },
  { title:'เปิดรับสมัคร SHBA Summer Championship 2026', emoji:'🏆', cat:'การประกวด', date:'1 เม.ย. 2026',
    excerpt:'พร้อมรายละเอียดคลาสการแข่งขันและรายชื่อกรรมการ', featured:false },
  { title:'อัปเดตมาตรฐาน NHC ปี 2026', emoji:'📋', cat:'มาตรฐาน', date:'20 มี.ค. 2026',
    excerpt:'สมาคมฯ รับรองมาตรฐาน NHC ฉบับปรับปรุง 2026 สำหรับใช้ในงานประกวดทุกรายการ', featured:false },
];
const RESULTS_DATA = [
  { award:'🥇 Best in Show', name:'"Golden Sunrise"',  breed:'Syrian Cinnamon Satin LH', owner:'ฟาร์มรุ่งอรุณ',   score:'99.2', show:'SHBA Spring Show 2026' },
  { award:'🥇 Best Syrian',  name:'"Midnight Prince"', breed:'Syrian Black Banded',       owner:'ดารณี สมบูรณ์',   score:'97.8', show:'SHBA Spring Show 2026' },
  { award:'🥇 Best Dwarf',   name:'"Blue Sky"',         breed:'W.White Sapphire',          owner:'ฟาร์มดาวน้อย',   score:'96.5', show:'SHBA Spring Show 2026' },
  { award:'🥈 Best in Show', name:'"Pearl Queen"',      breed:'Winter White Pearl',         owner:'สมหญิง ชัยชนะ',  score:'98.8', show:'SHBA Winter Show 2025' },
  { award:'🥈 Best Syrian',  name:'"Copper Dream"',     breed:'Syrian Copper Rex',          owner:'วีรวุฒิ สุขสวัสดิ์',score:'95.5', show:'SHBA Winter Show 2025' },
];

/* ─── SHARED NAVBAR INIT ─────────────────────────────────────────── */
function initNavbar(activePage) {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  });
  // Highlight active nav link
  document.querySelectorAll('.nav-link[data-page]').forEach(l => {
    l.classList.toggle('active', l.dataset.page === activePage);
  });
  // Hamburger
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobile-nav');
  const mobileClose = document.getElementById('mobile-nav-close');
  if (hamburger) hamburger.addEventListener('click', () => mobileNav.classList.toggle('open'));
  if (mobileClose) mobileClose.addEventListener('click', () => mobileNav.classList.remove('open'));
}

/* ─── COUNTDOWN ─────────────────────────────────────────────────── */
function initCountdown() {
  const target = new Date('2026-06-14T09:00:00');
  function tick() {
    const diff = target - new Date();
    if (diff <= 0) return;
    const d = Math.floor(diff / 86400000);
    const h = Math.floor((diff % 86400000) / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = String(v).padStart(2,'0'); };
    set('cd-days', d); set('cd-hours', h); set('cd-mins', m); set('cd-secs', s);
  }
  tick(); setInterval(tick, 1000);
}

/* ─── COUNTER ANIMATION ─────────────────────────────────────────── */
function animateCounter(el, target, duration = 1800) {
  let val = 0;
  const step = target / (duration / 16);
  const t = setInterval(() => {
    val = Math.min(val + step, target);
    el.textContent = Math.floor(val).toLocaleString();
    if (val >= target) clearInterval(t);
  }, 16);
}

/* ─── SCROLL ANIMATIONS ─────────────────────────────────────────── */
function initScrollAnimations() {
  const obs = new IntersectionObserver(entries =>
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
    { threshold: 0.1 });
  document.querySelectorAll('.fade-in-up').forEach(el => obs.observe(el));
}

/* ─── SCROLL TO TOP ─────────────────────────────────────────────── */
function initScrollTop() {
  const btn = document.getElementById('scroll-top');
  if (!btn) return;
  window.addEventListener('scroll', () => btn.classList.toggle('show', window.scrollY > 400));
  btn.addEventListener('click', () => window.scrollTo({ top:0, behavior:'smooth' }));
}

/* ─── TOAST ─────────────────────────────────────────────────────── */
window.showToast = (type, msg) => {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  const icon = type === 'success' ? 'fa-circle-check' : type === 'error' ? 'fa-circle-xmark' : 'fa-circle-info';
  const color = type === 'success' ? '#48C758' : type === 'error' ? '#E84242' : 'var(--orange)';
  toast.innerHTML = `<i class="fa-solid ${icon}" style="color:${color}"></i><span>${msg}</span>`;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
};

/* ─── MODALS ────────────────────────────────────────────────────── */
window.openModal = (id) => { const m = document.getElementById(id); if (m) m.classList.add('open'); };
window.closeModal = (id) => { const m = document.getElementById(id); if (m) m.classList.remove('open'); };
document.addEventListener('click', e => { if (e.target.classList.contains('modal-overlay')) e.target.classList.remove('open'); });

/* ─── RENDER: COLOR CARD ─────────────────────────────────────────── */
function renderColorCard(c) {
  return `<div class="color-card">
    <div class="color-swatch" style="background:${c.bg||'#888'}">${c.emoji}</div>
    <div class="color-card-body">
      <h4>${c.name}</h4>
      <div class="genotype">${c.genotype}</div>
      <p>${c.desc}</p>
      ${c.eye ? `<p style="font-size:.7rem;margin-top:4px;color:var(--gray-500)">ตา: ${c.eye} · หู: ${c.ear}</p>` : ''}
    </div>
  </div>`;
}

/* ─── RENDER: EVENTS ────────────────────────────────────────────── */
window.renderEvents = function(filter = 'all') {
  const grid = document.getElementById('events-grid');
  if (!grid) return;
  const list = filter === 'all' ? EVENTS : EVENTS.filter(e => e.status === filter);
  const sMap  = { open:'badge-green', upcoming:'badge-blue', past:'badge-orange' };
  const sLabel = { open:'เปิดรับสมัคร', upcoming:'กำลังจะมา', past:'ผ่านมาแล้ว' };
  grid.innerHTML = list.map(ev => `
    <div class="event-card">
      <div class="event-card-header">
        <div>
          <span class="badge ${sMap[ev.status]}" style="margin-bottom:8px;display:inline-block">${sLabel[ev.status]}</span>
          <h3 class="event-title">${ev.emoji} ${ev.name}</h3>
        </div>
        <div class="event-date-box"><div class="day">${ev.day}</div><div class="month">${ev.month}</div></div>
      </div>
      <div class="event-card-body">
        <div class="event-meta">
          <div class="event-meta-item"><span class="event-meta-icon">📍</span>${ev.location}</div>
          <div class="event-meta-item"><span class="event-meta-icon">📅</span>ปิดรับสมัคร: ${ev.deadline}</div>
          <div class="event-meta-item"><span class="event-meta-icon">⚖️</span>${ev.judges.join(', ')}</div>
        </div>
        <div class="event-classes">${ev.classes.map(c=>`<span class="badge badge-gold" style="font-size:.72rem">${c}</span>`).join('')}</div>
      </div>
      <div class="event-card-footer">
        <div class="event-fee">ค่าสมัคร <span>฿${ev.fee}</span>/ตัว</div>
        ${ev.status==='open'
          ? `<button class="btn btn-orange btn-sm" onclick="openEntryForm(${ev.id})"><i class="fa-solid fa-plus"></i> สมัคร</button>`
          : ev.status==='past'
          ? `<a href="competitions.html#results" class="btn btn-outline-gold btn-sm"><i class="fa-solid fa-trophy"></i> ดูผล</a>`
          : `<button class="btn btn-outline-gold btn-sm" disabled style="opacity:.5;cursor:not-allowed">เร็วๆ นี้</button>`}
      </div>
    </div>`).join('');
};
window.filterEvents = (f, btn) => {
  document.querySelectorAll('#events-grid').forEach(() => {});
  document.querySelectorAll('.evt-filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderEvents(f);
};
window.openEntryForm = (id) => {
  const form = document.getElementById('comp-register-form');
  if (!form) return;
  form.classList.add('open');
  const num = `SHBA-2026-${String(Math.floor(Math.random()*900)+100).padStart(4,'0')}`;
  const el = document.getElementById('entry-num');
  if (el) el.textContent = num;
  form.scrollIntoView({ behavior:'smooth', block:'start' });
};
window.submitCompEntry = () => {
  showToast('success', '✅ ส่งใบสมัครสำเร็จ! กรุณาชำระเงินภายใน 3 วัน');
  const f = document.getElementById('comp-register-form');
  if (f) f.classList.remove('open');
};

/* ─── RENDER: GENETICS ───────────────────────────────────────────── */
window.renderGeneticsGrids = function() {
  const m = { 'syrian-agouti-grid': SYRIAN_AGOUTI, 'syrian-self-grid': SYRIAN_SELF,
               'dwarf-ww-grid': DWARF_WW, 'dwarf-camp-grid': DWARF_CAMP, 'dwarf-robo-grid': DWARF_ROBO };
  Object.entries(m).forEach(([id, data]) => {
    const el = document.getElementById(id);
    if (el) el.innerHTML = data.map(renderColorCard).join('');
  });
  const pat = document.getElementById('patterns-grid');
  if (pat) pat.innerHTML = PATTERNS.map(p => `
    <div class="pattern-card">
      <div class="pattern-icon">${p.emoji}</div>
      <h3>${p.name}</h3>
      <div class="pattern-gene">${p.gene}</div>
      <p>${p.desc}</p>
      <div style="margin-top:12px">
        <span class="badge ${p.dominant?'badge-orange':'badge-gold'}">${p.dominant?'ยีนเด่น':'เฉพาะเพศเมีย'}</span>
      </div>
    </div>`).join('');
  const coat = document.getElementById('coat-grid');
  if (coat) coat.innerHTML = COAT_TYPES.map(c => `
    <div class="pattern-card">
      <div class="pattern-icon">${c.emoji}</div>
      <h3>${c.name}</h3>
      <div class="pattern-gene">${c.gene}</div>
      <p>${c.desc}</p>
    </div>`).join('');
};
window.switchGenTab = (panel, btn) => {
  document.querySelectorAll('.gen-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.gen-panel').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  const ids = { syrian:'panel-syrian','syrian-self':'panel-syrian-self',dwarf:'panel-dwarf',patterns:'panel-patterns',coat:'panel-coat',calculator:'panel-calculator' };
  const el = document.getElementById(ids[panel]);
  if (el) el.classList.add('active');
};
window.calculateGenetics = () => {
  const g = (id) => { const el = document.getElementById(id); return el ? el.value : ''; };
  const sireColor = g('sire-color') || 'Golden';
  const damColor  = g('dam-color')  || 'Golden';
  const sireCoat  = g('sire-coat')  || 'Short';
  const damCoat   = g('dam-coat')   || 'Short';
  const sirePat   = g('sire-pattern') || 'Self';
  const damPat    = g('dam-pattern')  || 'Self';
  const out = document.getElementById('calc-output');
  if (!out) return;
  const results = [];
  if (sireColor === damColor) {
    results.push({ emoji:'🟡', label:`${sireColor} — 75%`, pct:75 });
    results.push({ emoji:'🤍', label:'Cream/Albino (ยีนด้อย) — 25%', pct:25 });
  } else {
    results.push({ emoji:'🟡', label:`${sireColor} (สีพ่อ) — 50%`, pct:50 });
    results.push({ emoji:'🟤', label:`${damColor} (สีแม่) — 50%`, pct:50 });
  }
  const lp = sireCoat==='Long/Short' && damCoat==='Long/Short' ? 25
           : (sireCoat==='Long'||damCoat==='Long') ? 50 : 0;
  if (lp > 0) {
    results.push({ emoji:'🧸', label:`Long Hair (l/l) — ${lp}%`, pct:lp });
    results.push({ emoji:'🐹', label:`Short / Carrier — ${100-lp}%`, pct:100-lp });
  } else if (sireCoat==='Rex' || damCoat==='Rex') {
    results.push({ emoji:'🌀', label:'Rex (Re/+) — 50%', pct:50 });
    results.push({ emoji:'🐹', label:'Short Hair — 50%', pct:50 });
  } else {
    results.push({ emoji:'🐹', label:'Short Hair (ปกติ) — 100%', pct:100 });
  }
  if (sirePat!=='Self' || damPat!=='Self') {
    const pat = sirePat!=='Self' ? sirePat : damPat;
    results.push({ emoji:'⬜', label:`${pat} — ~50%`, pct:50 });
    results.push({ emoji:'🟫', label:'Self (ไม่มีแพตเทิร์น) — ~50%', pct:50 });
  }
  out.innerHTML = results.slice(0,6).map(r => `
    <div class="result-row"><span>${r.emoji} ${r.label}</span><span class="result-pct">${r.pct}%</span></div>
    <div class="result-bar-wrap"><div class="result-bar" style="width:${r.pct}%"></div></div>`).join('')
    + `<p style="font-size:.78rem;color:var(--gray-500);margin-top:16px">* ผลลัพธ์เป็นการประมาณการทางสถิติ ผลจริงอาจแตกต่างกัน</p>`;
};

/* ─── RENDER: SPECIES ────────────────────────────────────────────── */
window.renderSpecies = function() {
  const grid = document.getElementById('species-grid');
  if (!grid) return;
  grid.innerHTML = SPECIES_DATA.map(s => `
    <div class="species-card">
      <div class="species-header">${s.emoji}</div>
      <div class="species-body">
        <h3>${s.name}</h3>
        <p class="sci-name">${s.sci}</p>
        <div class="species-stats">
          <div class="species-stat"><div class="label">ขนาด</div><div class="val">${s.size}</div></div>
          <div class="species-stat"><div class="label">น้ำหนัก</div><div class="val">${s.weight}</div></div>
          <div class="species-stat"><div class="label">อายุขัย</div><div class="val">${s.lifespan}</div></div>
          <div class="species-stat"><div class="label">ถิ่นกำเนิด</div><div class="val">${s.origin}</div></div>
        </div>
        <p style="font-size:.8rem;color:var(--gray-500);margin-top:4px"><i class="fa-solid fa-users" style="color:var(--orange)"></i> ${s.social}</p>
        <p style="font-size:.8rem;margin-top:6px;line-height:1.5">${s.notes}</p>
      </div>
    </div>`).join('');
};

/* ─── RENDER: KNOWLEDGE ──────────────────────────────────────────── */
let _knowledgeTag = 'all';
window.renderKnowledge = function(filter = 'all', search = '') {
  _knowledgeTag = filter;
  const grid = document.getElementById('knowledge-grid');
  if (!grid) return;
  let arts = KNOWLEDGE_ARTICLES;
  if (filter !== 'all') arts = arts.filter(a => a.tag === filter);
  if (search) arts = arts.filter(a => a.title.toLowerCase().includes(search.toLowerCase()) || a.desc.toLowerCase().includes(search.toLowerCase()));
  if (!arts.length) {
    grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:48px;color:var(--gray-500)">
      <i class="fa-solid fa-search" style="font-size:2rem;display:block;margin-bottom:12px"></i>ไม่พบบทความที่ตรงกับการค้นหา</div>`;
    return;
  }
  grid.innerHTML = arts.map(a => `
    <div class="knowledge-card">
      <div class="knowledge-thumb">${a.emoji}<div class="knowledge-cat"><span class="badge badge-gold">${a.cat}</span></div></div>
      <div class="knowledge-body">
        <h4>${a.title}</h4>
        <p>${a.desc}</p>
        <a href="#" class="news-read-more">อ่านต่อ <i class="fa-solid fa-arrow-right"></i></a>
      </div>
      <div style="padding:12px 20px;border-top:1px solid rgba(255,255,255,.05);display:flex;gap:16px;font-size:.78rem;color:var(--gray-500)">
        <span><i class="fa-regular fa-calendar" style="color:var(--gold)"></i> ${a.date}</span>
        <span><i class="fa-regular fa-clock" style="color:var(--gold)"></i> ${a.readTime}</span>
      </div>
    </div>`).join('');
};
window.filterByTag = (tag, btn) => {
  document.querySelectorAll('.k-tag').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderKnowledge(tag, document.getElementById('k-search')?.value || '');
};
window.filterKnowledge = (val) => renderKnowledge(_knowledgeTag, val);

/* ─── RENDER: HOF ────────────────────────────────────────────────── */
window.renderHOF = function() {
  const grid = document.getElementById('hof-grid');
  if (!grid) return;
  grid.innerHTML = HOF_DATA.map(h => `
    <div class="hof-card">
      <div class="hof-rank">${h.rank}</div>
      <h4>${h.name}</h4>
      <div class="owner">${h.owner}</div>
      <div class="breed">${h.breed}</div>
      <div class="year-badge">Champion ${h.year}</div>
    </div>`).join('');
};

/* ─── RENDER: NEWS ────────────────────────────────────────────────── */
window.renderNews = function() {
  const grid = document.getElementById('news-grid');
  if (!grid) return;
  grid.innerHTML = NEWS_DATA.map(n => `
    <div class="news-card ${n.featured?'featured':''}">
      <div class="news-thumb">${n.emoji}</div>
      <div class="news-body">
        <div class="news-meta">
          <span class="badge badge-orange">${n.cat}</span>
          <span><i class="fa-regular fa-calendar"></i> ${n.date}</span>
        </div>
        <h3>${n.title}</h3>
        <p>${n.excerpt}</p>
        <a href="#" class="news-read-more">อ่านเพิ่มเติม <i class="fa-solid fa-arrow-right"></i></a>
      </div>
    </div>`).join('');
};

/* ─── RENDER: RESULTS TABLE ──────────────────────────────────────── */
window.renderResults = function() {
  const tbody = document.getElementById('results-tbody');
  if (!tbody) return;
  tbody.innerHTML = RESULTS_DATA.map((r,i) => `
    <tr style="border-bottom:1px solid rgba(255,255,255,.05);${i%2?'background:rgba(255,255,255,.02)':''}">
      <td style="padding:14px 16px">${r.award}</td>
      <td style="padding:14px 16px;font-weight:600">${r.name}</td>
      <td style="padding:14px 16px;color:var(--gray-300)">${r.breed}</td>
      <td style="padding:14px 16px;color:var(--gold)">${r.owner}</td>
      <td style="padding:14px 16px;color:var(--orange);font-weight:700">${r.score}</td>
      <td style="padding:14px 16px;font-size:.82rem;color:var(--gray-500)">${r.show}</td>
    </tr>`).join('');
};

/* ─── FORMS ──────────────────────────────────────────────────────── */
window.handleRegister = (e) => {
  e.preventDefault();
  const fn = document.getElementById('reg-firstname')?.value;
  const em = document.getElementById('reg-email')?.value;
  if (!fn || !em) { showToast('error', '❌ กรุณากรอกข้อมูลที่จำเป็นให้ครบ'); return; }
  const btn = e.target.querySelector('[type="submit"]');
  btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> กำลังดำเนินการ...'; btn.disabled = true;
  setTimeout(() => {
    showToast('success', `✅ สมัครสำเร็จ! ส่งอีเมลยืนยันไปที่ ${em} แล้ว`);
    e.target.reset();
    btn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> ส่งใบสมัคร'; btn.disabled = false;
  }, 1800);
};
window.handleLogin = () => { showToast('success', '✅ เข้าสู่ระบบสำเร็จ!'); closeModal('login-modal'); };
window.submitJudgeApp = () => { showToast('info', '📋 ส่งใบสมัครแล้ว เจ้าหน้าที่จะติดต่อกลับภายใน 7 วัน'); closeModal('judge-app-modal'); };
window.selectMemberType = (type) => { const r = document.getElementById(`mt-${type}`); if (r) r.checked = true; };

/* ─── EXPOSE INIT ────────────────────────────────────────────────── */
window.SHBA = { initNavbar, initCountdown, initScrollAnimations, initScrollTop, animateCounter };

/* ─── THEME TOGGLE ───────────────────────────────────────────────── */
function _updateThemeBtn(theme) {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;
  if (theme === 'dark') {
    btn.innerHTML = '<i class="fa-solid fa-sun"></i>';
    btn.title = 'เปลี่ยนเป็น Light Mode';
  } else {
    btn.innerHTML = '<i class="fa-solid fa-moon"></i>';
    btn.title = 'เปลี่ยนเป็น Dark Mode';
  }
}

function initTheme() {
  // Apply saved preference (default: dark) — run BEFORE DOMContentLoaded to prevent flash
  const saved = localStorage.getItem('shba-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  _updateThemeBtn(saved);
}

window.toggleTheme = () => {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('shba-theme', next);
  _updateThemeBtn(next);
  showToast('info', next === 'light' ? '☀️ เปลี่ยนเป็น Light Mode แล้ว' : '🌙 เปลี่ยนเป็น Dark Mode แล้ว');
};

// Expose in THA namespace
if (window.SHBA) window.SHBA.initTheme = initTheme;

// Run immediately so there's no flash of wrong theme
(function() {
  const saved = localStorage.getItem('shba-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
})();
