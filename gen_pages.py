import os

# ── Shared login modal ──────────────────────────────────────────────────
LOGIN_MODAL = '''<!-- MODALS -->
<div class="modal-overlay" id="login-modal">
  <div class="modal">
    <button class="modal-close" onclick="closeModal(\'login-modal\')"><i class="fa-solid fa-xmark"></i></button>
    <div style="text-align:center;margin-bottom:24px">
      <div style="font-size:2.2rem;margin-bottom:6px">🐹</div>
      <h3 style="margin-bottom:4px"><i class="fa-solid fa-lock text-gold"></i> เข้าสู่ระบบ / สมัครสมาชิก</h3>
      <p style="font-size:.82rem;color:var(--text-muted)">Siam Hamster Breeder Association</p>
    </div>
    <div class="auth-tabs">
      <button class="auth-tab active" id="tab-login"  onclick="switchAuthTab(\'login\')">เข้าสู่ระบบ</button>
      <button class="auth-tab"        id="tab-signup" onclick="switchAuthTab(\'signup\')">สมัครสมาชิกใหม่</button>
    </div>
    <div id="auth-panel-login">
      <button class="btn-google-signin" onclick="signInWithGoogle()" style="margin-bottom:16px">
        <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" alt="Google" width="20" height="20"/>
        เข้าสู่ระบบด้วย Google
      </button>
      <div class="auth-divider"><span>หรือใช้อีเมล</span></div>
      <div class="form-group"><label>อีเมล</label><input type="email" id="li-email" class="form-control" placeholder="your@email.com" /></div>
      <div class="form-group"><label>รหัสผ่าน</label><input type="password" id="li-password" class="form-control" placeholder="••••••••" /></div>
      <button class="btn btn-gold" style="width:100%;justify-content:center;margin-top:4px" onclick="handleEmailLogin()">
        <i class="fa-solid fa-arrow-right-to-bracket"></i> เข้าสู่ระบบ
      </button>
      <p style="text-align:center;margin-top:12px;font-size:.82rem">
        <a href="#" style="color:var(--text-muted)" onclick="handleForgotPassword(event)">ลืมรหัสผ่าน?</a>
      </p>
    </div>
    <div id="auth-panel-signup" style="display:none">
      <button class="btn-google-signin" onclick="signInWithGoogle()" style="margin-bottom:16px">
        <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" alt="Google" width="20" height="20"/>
        สมัครด้วย Google (แนะนำ)
      </button>
      <div class="auth-divider"><span>หรือสมัครด้วยอีเมล</span></div>
      <div class="form-row">
        <div class="form-group"><label>ชื่อ <span class="req">*</span></label><input type="text" id="su-firstname" class="form-control" placeholder="ชื่อจริง" /></div>
        <div class="form-group"><label>นามสกุล <span class="req">*</span></label><input type="text" id="su-lastname" class="form-control" placeholder="นามสกุล" /></div>
      </div>
      <div class="form-group"><label>อีเมล <span class="req">*</span></label><input type="email" id="su-email" class="form-control" placeholder="your@email.com" /></div>
      <div class="form-group"><label>รหัสผ่าน <span class="req">*</span></label><input type="password" id="su-password" class="form-control" placeholder="อย่างน้อย 6 ตัวอักษร" /></div>
      <div class="form-group"><label>ยืนยันรหัสผ่าน <span class="req">*</span></label><input type="password" id="su-password2" class="form-control" placeholder="••••••••" /></div>
      <button class="btn btn-gold" style="width:100%;justify-content:center;margin-top:4px" onclick="handleQuickSignup()">
        <i class="fa-solid fa-user-plus"></i> สร้างบัญชี (สมาชิกสามัญฟรี)
      </button>
    </div>
  </div>
</div>'''

# ── Shared scripts footer ────────────────────────────────────────────────
SCRIPTS = '''<button id="scroll-top"><i class="fa-solid fa-arrow-up"></i></button>
<div class="toast-container" id="toast-container"></div>
<script type="module" src="firebase.js"></script>
<script src="main.js"></script>'''

# ── Shared navbar ────────────────────────────────────────────────────────
def navbar(active):
    pages = ['home','about','membership','competitions','directory','knowledge','news','community','contact']
    active_classes = {p: ' active' if p == active else '' for p in pages}
    return f'''<!-- NAV -->
<nav id="navbar">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo">
      <div class="nav-logo-icon">🐹</div>
      <div class="nav-logo-text">SHBA<span>Siam Hamster Breeder Association</span></div>
    </a>
    <ul class="nav-links">
      <li class="nav-item"><a href="index.html" class="nav-link{active_classes['home']}" data-page="home">หน้าหลัก</a></li>
      <li class="nav-item has-dropdown">
        <a href="about.html" class="nav-link{active_classes['about']}" data-page="about">เกี่ยวกับ <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="about.html#history"   class="nav-dd-link"><i class="fa-solid fa-landmark"></i> ประวัติสมาคม SHBA</a>
          <a href="about.html#vision"    class="nav-dd-link"><i class="fa-solid fa-eye"></i> วิสัยทัศน์ &amp; พันธกิจ</a>
          <a href="about.html#committee" class="nav-dd-link"><i class="fa-solid fa-users"></i> คณะกรรมการ</a>
          <a href="about.html#ethics"    class="nav-dd-link"><i class="fa-solid fa-scale-balanced"></i> จรรยาบรรณผู้เพาะพันธุ์</a>
          <a href="about.html#rules"     class="nav-dd-link"><i class="fa-solid fa-file-lines"></i> ข้อบังคับสมาคม</a>
        </div>
      </li>
      <li class="nav-item has-dropdown">
        <a href="membership.html" class="nav-link{active_classes['membership']}" data-page="membership">สมาชิก <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="membership.html#membership"     class="nav-dd-link"><i class="fa-solid fa-id-card"></i> ประเภทสมาชิก &amp; สิทธิประโยชน์</a>
          <a href="membership.html#register"        class="nav-dd-link"><i class="fa-solid fa-user-plus"></i> สมัครสมาชิกออนไลน์</a>
          <a href="membership.html#upgrade-section" class="nav-dd-link"><i class="fa-solid fa-rotate"></i> ต่ออายุสมาชิก</a>
          <a href="membership.html#dashboard"       class="nav-dd-link"><i class="fa-solid fa-gauge"></i> สมาชิก Dashboard</a>
          <a href="membership.html#digital-card"    class="nav-dd-link"><i class="fa-solid fa-credit-card"></i> บัตรสมาชิกดิจิทัล</a>
        </div>
      </li>
      <li class="nav-item has-dropdown">
        <a href="competitions.html" class="nav-link{active_classes['competitions']}" data-page="competitions">การประกวด <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="competitions.html#calendar"  class="nav-dd-link"><i class="fa-solid fa-calendar-days"></i> ปฏิทินการประกวด</a>
          <a href="competitions.html#register"  class="nav-dd-link"><i class="fa-solid fa-pen-to-square"></i> สมัครประกวดออนไลน์</a>
          <a href="competitions.html#standards" class="nav-dd-link"><i class="fa-solid fa-star"></i> มาตรฐานการประกวด</a>
          <a href="competitions.html#rules"     class="nav-dd-link"><i class="fa-solid fa-gavel"></i> กฎกติกาการประกวด</a>
          <a href="competitions.html#results"   class="nav-dd-link"><i class="fa-solid fa-trophy"></i> ผลการประกวด</a>
          <a href="competitions.html#gallery"   class="nav-dd-link"><i class="fa-solid fa-images"></i> แกลเลอรีภาพงานประกวด</a>
          <a href="competitions.html#judges"    class="nav-dd-link"><i class="fa-solid fa-user-tie"></i> ข้อมูลกรรมการตัดสิน</a>
        </div>
      </li>
      <li class="nav-item has-dropdown">
        <a href="directory.html" class="nav-link{active_classes['directory']}" data-page="directory">ร้านค้า &amp; ฟาร์ม <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="directory.html#breeders" class="nav-dd-link"><i class="fa-solid fa-house"></i> ไดเรกทอรีฟาร์ม/ผู้เพาะพันธุ์</a>
          <a href="directory.html#shops"    class="nav-dd-link"><i class="fa-solid fa-store"></i> ไดเรกทอรีร้านค้า</a>
          <a href="directory.html#map"      class="nav-dd-link"><i class="fa-solid fa-map-location-dot"></i> แผนที่ร้านค้า/ฟาร์ม</a>
          <a href="directory.html#reviews"  class="nav-dd-link"><i class="fa-solid fa-star-half-stroke"></i> รีวิว &amp; เรตติ้ง</a>
        </div>
      </li>
      <li class="nav-item has-dropdown">
        <a href="knowledge.html" class="nav-link{active_classes['knowledge']}" data-page="knowledge">คลังความรู้ <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="genetics.html"           class="nav-dd-link"><i class="fa-solid fa-dna"></i> Genetics &amp; สีสัน</a>
          <a href="knowledge.html#care"     class="nav-dd-link"><i class="fa-solid fa-heart"></i> การดูแลทั่วไป</a>
          <a href="knowledge.html#species"  class="nav-dd-link"><i class="fa-solid fa-paw"></i> สายพันธุ์แฮมสเตอร์</a>
          <a href="knowledge.html#articles" class="nav-dd-link"><i class="fa-solid fa-book-open"></i> บทความ &amp; วิจัย</a>
        </div>
      </li>
      <li class="nav-item"><a href="news.html"      class="nav-link{active_classes['news']}"      data-page="news">ข่าวสาร</a></li>
      <li class="nav-item"><a href="community.html" class="nav-link{active_classes['community']}" data-page="community">ชุมชน</a></li>
      <li class="nav-item"><a href="contact.html"   class="nav-link{active_classes['contact']}"   data-page="contact">ติดต่อเรา</a></li>
    </ul>
    <div class="nav-cta">
      <button class="btn btn-outline-gold btn-sm btn-login-trigger" onclick="openModal('login-modal')"><i class="fa-regular fa-user"></i> เข้าสู่ระบบ</button>
      <a href="#" onclick="openModal('login-modal'); switchAuthTab('signup'); return false;" class="btn btn-gold btn-sm btn-register-trigger"><i class="fa-solid fa-plus"></i> สมัครสมาชิก</a>
    </div>
    <button id="theme-toggle" onclick="toggleTheme()" title="เปลี่ยนธีม"><i class="fa-solid fa-sun"></i></button>
    <button class="hamburger" id="hamburger"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mobile-nav" id="mobile-nav">
  <button class="mobile-nav-close" id="mobile-nav-close"><i class="fa-solid fa-xmark"></i></button>
  <div class="mobile-nav-scroll">
    <a href="index.html" class="mobile-nav-link">หน้าหลัก</a>
    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">เกี่ยวกับสมาคม <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="about.html#history"   class="mobile-nav-sub-link"><i class="fa-solid fa-landmark"></i> ประวัติสมาคม</a>
        <a href="about.html#vision"    class="mobile-nav-sub-link"><i class="fa-solid fa-eye"></i> วิสัยทัศน์</a>
        <a href="about.html#committee" class="mobile-nav-sub-link"><i class="fa-solid fa-users"></i> คณะกรรมการ</a>
        <a href="about.html#ethics"    class="mobile-nav-sub-link"><i class="fa-solid fa-scale-balanced"></i> จรรยาบรรณ</a>
      </div>
    </div>
    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">สมาชิก <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="membership.html#membership"  class="mobile-nav-sub-link"><i class="fa-solid fa-id-card"></i> ประเภทสมาชิก</a>
        <a href="membership.html#dashboard"   class="mobile-nav-sub-link"><i class="fa-solid fa-gauge"></i> Dashboard</a>
        <a href="membership.html#digital-card"class="mobile-nav-sub-link"><i class="fa-solid fa-credit-card"></i> บัตรสมาชิก</a>
      </div>
    </div>
    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">การประกวด <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="competitions.html#calendar" class="mobile-nav-sub-link"><i class="fa-solid fa-calendar-days"></i> ปฏิทิน</a>
        <a href="competitions.html#results"  class="mobile-nav-sub-link"><i class="fa-solid fa-trophy"></i> ผลการประกวด</a>
        <a href="competitions.html#judges"   class="mobile-nav-sub-link"><i class="fa-solid fa-user-tie"></i> กรรมการ</a>
      </div>
    </div>
    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">ร้านค้า &amp; ฟาร์ม <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="directory.html#breeders" class="mobile-nav-sub-link"><i class="fa-solid fa-house"></i> ไดเรกทอรีฟาร์ม</a>
        <a href="directory.html#shops"    class="mobile-nav-sub-link"><i class="fa-solid fa-store"></i> ร้านค้า</a>
        <a href="directory.html#map"      class="mobile-nav-sub-link"><i class="fa-solid fa-map-location-dot"></i> แผนที่</a>
      </div>
    </div>
    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">คลังความรู้ <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="genetics.html"           class="mobile-nav-sub-link"><i class="fa-solid fa-dna"></i> Genetics</a>
        <a href="knowledge.html#care"     class="mobile-nav-sub-link"><i class="fa-solid fa-heart"></i> การดูแล</a>
        <a href="knowledge.html#species"  class="mobile-nav-sub-link"><i class="fa-solid fa-paw"></i> สายพันธุ์</a>
      </div>
    </div>
    <a href="news.html"      class="mobile-nav-link">ข่าวสาร</a>
    <a href="community.html" class="mobile-nav-link">ชุมชน</a>
    <a href="contact.html"   class="mobile-nav-link">ติดต่อเรา</a>
    <div class="mobile-nav-divider"></div>
    <div class="mobile-nav-btns">
      <button class="btn btn-outline-gold btn-login-trigger" onclick="closeMobileNav(); openModal('login-modal')"><i class="fa-regular fa-user"></i> เข้าสู่ระบบ</button>
      <a href="#" class="btn btn-gold btn-register-trigger" onclick="closeMobileNav(); openModal('login-modal'); switchAuthTab('signup')"><i class="fa-solid fa-plus"></i> สมัครสมาชิก</a>
    </div>
  </div>
</div>'''

def page_shell(title, page_key, content, init_fn=''):
    nav = navbar(page_key)
    return f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Siam Hamster Breeder Association</title>
  <link rel="stylesheet" href="styles.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>

{nav}

{content}

{LOGIN_MODAL}

{SCRIPTS}
<script>
  document.addEventListener('DOMContentLoaded', () => {{
    SHBA.initNavbar('{page_key}');
    SHBA.initTheme();
    SHBA.initScrollAnimations();
    SHBA.initScrollTop();
    {init_fn}
  }});
</script>
</body>
</html>'''

# ════════════════════════════════════════════════════════════════
#  ABOUT.HTML
# ════════════════════════════════════════════════════════════════
ABOUT_CONTENT = '''<!-- HERO -->
<div style="background:var(--gradient-hero);padding:120px 0 60px;position:relative;overflow:hidden">
  <div class="hero-bg"></div><div class="hero-grid"></div>
  <div class="container" style="position:relative;z-index:1;text-align:center">
    <div class="tag" style="display:inline-block;margin-bottom:16px">ABOUT SHBA</div>
    <h1 style="margin-bottom:12px">เกี่ยวกับ<span class="text-gradient-gold">สมาคม</span></h1>
    <p style="max-width:560px;margin:0 auto;color:var(--text-muted)">Siam Hamster Breeder Association — ศูนย์กลางความเป็นเลิศด้านแฮมสเตอร์แห่งประเทศไทย</p>
  </div>
</div>

<!-- HISTORY -->
<section id="history" class="section" style="background:var(--black)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">ประวัติสมาคม</div>
      <h2>ประวัติ<span class="text-gradient-gold">SHBA</span></h2>
      <div class="divider"></div>
    </div>
    <div class="fade-in-up" style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;max-width:960px;margin:0 auto">
      <div>
        <p style="color:var(--text-muted);line-height:1.9;margin-bottom:16px">สมาคมสยามแฮมสเตอร์บรีดเดอร์ (SHBA) ก่อตั้งขึ้นในปี พ.ศ. 2563 โดยกลุ่มผู้เพาะพันธุ์แฮมสเตอร์ที่มีความหลงใหลในการพัฒนาสายพันธุ์และยกระดับมาตรฐานการเพาะพันธุ์ในประเทศไทย</p>
        <p style="color:var(--text-muted);line-height:1.9">ปัจจุบัน SHBA มีสมาชิกกว่า 500 คนทั่วประเทศ พร้อมจัดงานประกวดระดับชาติมาแล้วกว่า 20 ครั้ง ภายใต้มาตรฐานสากล</p>
      </div>
      <div class="card" style="padding:32px;text-align:center">
        <div style="font-size:4rem;margin-bottom:12px">🐹</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:16px">
          <div><div style="font-size:2rem;font-weight:900;color:var(--gold);font-family:\'Playfair Display\',serif">500+</div><div style="font-size:.8rem;color:var(--text-muted)">สมาชิก</div></div>
          <div><div style="font-size:2rem;font-weight:900;color:var(--orange);font-family:\'Playfair Display\',serif">20+</div><div style="font-size:.8rem;color:var(--text-muted)">งานประกวด</div></div>
          <div><div style="font-size:2rem;font-weight:900;color:var(--gold);font-family:\'Playfair Display\',serif">5</div><div style="font-size:.8rem;color:var(--text-muted)">ปีแห่งความเป็นเลิศ</div></div>
          <div><div style="font-size:2rem;font-weight:900;color:var(--orange);font-family:\'Playfair Display\',serif">77</div><div style="font-size:.8rem;color:var(--text-muted)">จังหวัด</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- VISION -->
<section id="vision" class="section" style="background:var(--black-light)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">วิสัยทัศน์ & พันธกิจ</div>
      <h2>วิสัยทัศน์<span class="text-gradient-gold"> & พันธกิจ</span></h2>
      <div class="divider"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;max-width:960px;margin:0 auto">
      <div class="card fade-in-up" style="padding:32px;border-top:3px solid var(--gold)">
        <div style="font-size:2.5rem;margin-bottom:16px">🎯</div>
        <h3 style="color:var(--gold);margin-bottom:12px">วิสัยทัศน์</h3>
        <p style="color:var(--text-muted);line-height:1.8">เป็นองค์กรมาตรฐานสากลด้านแฮมสเตอร์แห่งประเทศไทย ที่ได้รับการยอมรับในระดับเอเชีย</p>
      </div>
      <div class="card fade-in-up" style="padding:32px;border-top:3px solid var(--orange)">
        <div style="font-size:2.5rem;margin-bottom:16px">🌟</div>
        <h3 style="color:var(--orange);margin-bottom:12px">พันธกิจ</h3>
        <ul style="color:var(--text-muted);line-height:2;padding-left:16px">
          <li>ส่งเสริมมาตรฐานการเพาะพันธุ์</li>
          <li>จัดงานประกวดระดับชาติ</li>
          <li>เผยแพร่ความรู้ด้านพันธุกรรม</li>
          <li>สร้างชุมชนผู้รักแฮมสเตอร์</li>
        </ul>
      </div>
      <div class="card fade-in-up" style="padding:32px;border-top:3px solid var(--gold)">
        <div style="font-size:2.5rem;margin-bottom:16px">💎</div>
        <h3 style="color:var(--gold);margin-bottom:12px">ค่านิยม</h3>
        <ul style="color:var(--text-muted);line-height:2;padding-left:16px">
          <li>ความโปร่งใส & ซื่อสัตย์</li>
          <li>มาตรฐานระดับสากล</li>
          <li>ความรับผิดชอบต่อสัตว์</li>
          <li>การพัฒนาอย่างยั่งยืน</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- COMMITTEE -->
<section id="committee" class="section" style="background:var(--black)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">คณะกรรมการ</div>
      <h2>คณะ<span class="text-gradient-gold">กรรมการ</span></h2>
      <p>ผู้บริหารและผู้เชี่ยวชาญที่ขับเคลื่อน SHBA</p>
      <div class="divider"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px;max-width:900px;margin:0 auto">
      <div class="card fade-in-up" style="padding:32px;text-align:center">
        <div style="width:80px;height:80px;border-radius:50%;background:var(--gradient-gold);display:flex;align-items:center;justify-content:center;font-size:2rem;margin:0 auto 16px;border:3px solid var(--gold)">👨</div>
        <h4>นายสมชาย มีทอง</h4>
        <p style="color:var(--gold);font-size:.82rem;margin-top:4px">นายกสมาคม</p>
        <p style="color:var(--text-muted);font-size:.8rem;margin-top:8px">ผู้เพาะพันธุ์แฮมสเตอร์มากกว่า 15 ปี</p>
      </div>
      <div class="card fade-in-up" style="padding:32px;text-align:center">
        <div style="width:80px;height:80px;border-radius:50%;background:var(--gradient-orange);display:flex;align-items:center;justify-content:center;font-size:2rem;margin:0 auto 16px;border:3px solid var(--orange)">👩</div>
        <h4>นางสาวรัตนา สุขใจ</h4>
        <p style="color:var(--orange);font-size:.82rem;margin-top:4px">อุปนายก</p>
        <p style="color:var(--text-muted);font-size:.8rem;margin-top:8px">ผู้เชี่ยวชาญด้านพันธุกรรม</p>
      </div>
      <div class="card fade-in-up" style="padding:32px;text-align:center">
        <div style="width:80px;height:80px;border-radius:50%;background:var(--gradient-gold);display:flex;align-items:center;justify-content:center;font-size:2rem;margin:0 auto 16px;border:3px solid var(--gold)">👨</div>
        <h4>นายวิชัย ใจดี</h4>
        <p style="color:var(--gold);font-size:.82rem;margin-top:4px">เลขาธิการ</p>
        <p style="color:var(--text-muted);font-size:.8rem;margin-top:8px">ผู้จัดการฝ่ายประกวด</p>
      </div>
      <div class="card fade-in-up" style="padding:32px;text-align:center">
        <div style="width:80px;height:80px;border-radius:50%;background:var(--gradient-orange);display:flex;align-items:center;justify-content:center;font-size:2rem;margin:0 auto 16px;border:3px solid var(--orange)">👩</div>
        <h4>นางสาวปริยา ฟาร์มสวย</h4>
        <p style="color:var(--orange);font-size:.82rem;margin-top:4px">เหรัญญิก</p>
        <p style="color:var(--text-muted);font-size:.8rem;margin-top:8px">ผู้ดูแลฟาร์มมาตรฐาน SHBA</p>
      </div>
    </div>
  </div>
</section>

<!-- ETHICS -->
<section id="ethics" class="section" style="background:var(--black-light)">
  <div class="container" style="max-width:800px">
    <div class="section-header fade-in-up">
      <div class="tag">จรรยาบรรณ</div>
      <h2>จรรยาบรรณ<span class="text-gradient-gold">ผู้เพาะพันธุ์</span></h2>
      <p>Breeder's Code of Ethics — มาตรฐานที่สมาชิก SHBA ยึดถือ</p>
      <div class="divider"></div>
    </div>
    <div class="card fade-in-up" style="padding:40px">
      <div style="display:flex;flex-direction:column;gap:20px">
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--gradient-gold);display:flex;align-items:center;justify-content:center;font-weight:800;color:#000;flex-shrink:0">1</div>
          <div><h4 style="color:var(--gold);margin-bottom:4px">สวัสดิภาพสัตว์มาก่อน</h4><p style="color:var(--text-muted)">ให้ความสำคัญกับสุขภาพ ความปลอดภัย และคุณภาพชีวิตของแฮมสเตอร์เป็นอันดับแรก</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--gradient-gold);display:flex;align-items:center;justify-content:center;font-weight:800;color:#000;flex-shrink:0">2</div>
          <div><h4 style="color:var(--gold);margin-bottom:4px">ความซื่อสัตย์ในการซื้อขาย</h4><p style="color:var(--text-muted)">ให้ข้อมูลสายพันธุ์และประวัติที่ถูกต้อง ไม่บิดเบือน ไม่ทุจริต</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--gradient-gold);display:flex;align-items:center;justify-content:center;font-weight:800;color:#000;flex-shrink:0">3</div>
          <div><h4 style="color:var(--gold);margin-bottom:4px">มาตรฐานการเพาะพันธุ์</h4><p style="color:var(--text-muted)">เพาะพันธุ์ตามหลักพันธุศาสตร์ที่ดี ไม่เพาะพันธุ์สัตว์ที่มีโรคทางพันธุกรรม</p></div>
        </div>
        <div style="display:flex;gap:16px;align-items:flex-start">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--gradient-gold);display:flex;align-items:center;justify-content:center;font-weight:800;color:#000;flex-shrink:0">4</div>
          <div><h4 style="color:var(--gold);margin-bottom:4px">การสนับสนุนผู้ซื้อ</h4><p style="color:var(--text-muted)">ให้คำแนะนำการดูแลแก่ผู้ซื้อ และรับผิดชอบหลังการขาย</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- RULES -->
<section id="rules" class="section" style="background:var(--black)">
  <div class="container" style="max-width:760px">
    <div class="section-header fade-in-up">
      <div class="tag">ข้อบังคับ</div>
      <h2>ข้อบังคับ<span class="text-gradient-gold">สมาคม</span></h2>
      <div class="divider"></div>
    </div>
    <div class="card fade-in-up" style="padding:40px">
      <p style="color:var(--text-muted);margin-bottom:20px">ข้อบังคับของสมาคมสยามแฮมสเตอร์บรีดเดอร์ ฉบับปรับปรุง พ.ศ. 2566 ครอบคลุมหลักเกณฑ์การสมัครสมาชิก สิทธิหน้าที่ การประชุม และการปกครองสมาคม</p>
      <button class="btn btn-gold" onclick="openModal('login-modal')"><i class="fa-solid fa-file-pdf"></i> ดาวน์โหลดข้อบังคับ (PDF)</button>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer id="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo"><div class="nav-logo-icon">🐹</div><div class="nav-logo-text">Siam Hamster Breeder Association<span>สมาคมสยามแฮมสเตอร์บรีดเดอร์</span></div></div>
        <p>ศูนย์กลางความเป็นเลิศด้านแฮมสเตอร์แห่งประเทศไทย</p>
      </div>
      <div class="footer-col"><h4>สมาคม</h4><div class="footer-links">
        <a href="about.html#history"   class="footer-link">ประวัติสมาคม</a>
        <a href="about.html#committee" class="footer-link">คณะกรรมการ</a>
        <a href="about.html#ethics"    class="footer-link">จรรยาบรรณ</a>
      </div></div>
      <div class="footer-col"><h4>สมาชิก</h4><div class="footer-links">
        <a href="membership.html"          class="footer-link">ประเภทสมาชิก</a>
        <a href="membership.html#dashboard"class="footer-link">Dashboard</a>
      </div></div>
      <div class="footer-col"><h4>ติดต่อ</h4><div class="footer-links">
        <a href="contact.html"   class="footer-link">ติดต่อเรา</a>
        <a href="community.html" class="footer-link">ชุมชน</a>
      </div></div>
    </div>
    <div class="footer-bottom"><span>© 2026 Siam Hamster Breeder Association. All rights reserved.</span></div>
  </div>
</footer>'''

# ════════════════════════════════════════════════════════════════
#  DIRECTORY.HTML
# ════════════════════════════════════════════════════════════════
DIRECTORY_CONTENT = '''<!-- HERO -->
<div style="background:var(--gradient-hero);padding:120px 0 60px;position:relative;overflow:hidden">
  <div class="hero-bg"></div><div class="hero-grid"></div>
  <div class="container" style="position:relative;z-index:1;text-align:center">
    <div class="tag" style="display:inline-block;margin-bottom:16px">DIRECTORY</div>
    <h1 style="margin-bottom:12px">ร้านค้า<span class="text-gradient-gold"> & ฟาร์ม</span></h1>
    <p style="max-width:560px;margin:0 auto;color:var(--text-muted)">ไดเรกทอรีฟาร์มผู้เพาะพันธุ์และร้านค้าแฮมสเตอร์ที่ได้รับการรับรองจาก SHBA</p>
  </div>
</div>

<!-- SEARCH BAR -->
<div style="background:var(--black-light);padding:32px 0;border-bottom:1px solid rgba(201,162,39,0.1)">
  <div class="container" style="display:flex;gap:12px;max-width:700px">
    <input type="text" class="form-control" placeholder="🔍 ค้นหาฟาร์มหรือร้านค้า..." style="flex:1"/>
    <select class="form-control" style="max-width:160px">
      <option>ทุกจังหวัด</option>
      <option>กรุงเทพฯ</option>
      <option>เชียงใหม่</option>
      <option>ขอนแก่น</option>
    </select>
    <button class="btn btn-gold"><i class="fa-solid fa-magnifying-glass"></i> ค้นหา</button>
  </div>
</div>

<!-- BREEDER DIRECTORY -->
<section id="breeders" class="section" style="background:var(--black)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">ไดเรกทอรี</div>
      <h2>ฟาร์มผู้<span class="text-gradient-gold">เพาะพันธุ์</span></h2>
      <p>ฟาร์มที่ได้รับการรับรองจาก SHBA มาตรฐานสูงสุด</p>
      <div class="divider"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px">
      <div class="card fade-in-up" style="padding:28px">
        <div style="display:flex;gap:14px;align-items:center;margin-bottom:16px">
          <div style="width:56px;height:56px;border-radius:12px;background:var(--gradient-gold);display:flex;align-items:center;justify-content:center;font-size:1.6rem;flex-shrink:0">🏠</div>
          <div><h4>Golden Hamster Farm</h4><div style="color:var(--gold);font-size:.78rem;margin-top:2px">🧬 Breeder Member · SHBA-2024-0012</div></div>
        </div>
        <p style="color:var(--text-muted);font-size:.85rem;margin-bottom:12px">เชี่ยวชาญ Syrian สายพันธุ์ Satin และ Longhair มากกว่า 10 ปี</p>
        <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px">
          <span class="tag" style="font-size:.72rem;padding:3px 10px">Syrian</span>
          <span class="tag" style="font-size:.72rem;padding:3px 10px">Satin</span>
          <span class="tag" style="font-size:.72rem;padding:3px 10px">กรุงเทพฯ</span>
        </div>
        <div style="display:flex;gap:8px">
          <button class="btn btn-outline-gold btn-sm" style="flex:1;justify-content:center"><i class="fa-solid fa-eye"></i> ดูโปรไฟล์</button>
          <button class="btn btn-gold btn-sm"><i class="fa-brands fa-line"></i> Line</button>
        </div>
      </div>
      <div class="card fade-in-up" style="padding:28px">
        <div style="display:flex;gap:14px;align-items:center;margin-bottom:16px">
          <div style="width:56px;height:56px;border-radius:12px;background:var(--gradient-orange);display:flex;align-items:center;justify-content:center;font-size:1.6rem;flex-shrink:0">🐾</div>
          <div><h4>Paws & Pearls Farm</h4><div style="color:var(--gold);font-size:.78rem;margin-top:2px">🧬 Breeder Member · SHBA-2024-0089</div></div>
        </div>
        <p style="color:var(--text-muted);font-size:.85rem;margin-bottom:12px">ผู้เชี่ยวชาญ Winter White และ Campbell สีหายาก</p>
        <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px">
          <span class="tag" style="font-size:.72rem;padding:3px 10px">Winter White</span>
          <span class="tag" style="font-size:.72rem;padding:3px 10px">Campbell</span>
          <span class="tag" style="font-size:.72rem;padding:3px 10px">เชียงใหม่</span>
        </div>
        <div style="display:flex;gap:8px">
          <button class="btn btn-outline-gold btn-sm" style="flex:1;justify-content:center"><i class="fa-solid fa-eye"></i> ดูโปรไฟล์</button>
          <button class="btn btn-gold btn-sm"><i class="fa-brands fa-line"></i> Line</button>
        </div>
      </div>
      <div class="card fade-in-up" style="padding:28px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;border:2px dashed rgba(201,162,39,0.2);min-height:200px">
        <div style="font-size:2.5rem;opacity:.4">➕</div>
        <p style="color:var(--text-muted);text-align:center;font-size:.9rem">สนใจลงทะเบียนฟาร์มของคุณ?</p>
        <button class="btn btn-outline-gold btn-sm" onclick="openModal('login-modal')">สมัคร Breeder Member</button>
      </div>
    </div>
  </div>
</section>

<!-- SHOP DIRECTORY -->
<section id="shops" class="section" style="background:var(--black-light)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">ร้านค้า</div>
      <h2>ไดเรกทอรี<span class="text-gradient-gold">ร้านค้า</span></h2>
      <p>ร้านค้าอุปกรณ์และแฮมสเตอร์ที่แนะนำโดย SHBA</p>
      <div class="divider"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px">
      <div class="card fade-in-up" style="padding:24px">
        <div style="display:flex;gap:12px;align-items:center;margin-bottom:12px">
          <div style="width:48px;height:48px;border-radius:10px;background:rgba(201,162,39,0.15);display:flex;align-items:center;justify-content:center;font-size:1.4rem">🏪</div>
          <div><h4 style="font-size:1rem">HamsterHub Thailand</h4><div style="color:var(--text-muted);font-size:.78rem">กรุงเทพฯ · ออนไลน์</div></div>
        </div>
        <p style="color:var(--text-muted);font-size:.82rem;margin-bottom:12px">อุปกรณ์เลี้ยงแฮมสเตอร์ครบครัน นำเข้าจากยุโรปและญี่ปุ่น</p>
        <div style="display:flex;gap:6px">
          <button class="btn btn-outline-gold btn-sm" style="font-size:.78rem"><i class="fa-solid fa-globe"></i> เว็บไซต์</button>
          <button class="btn btn-gold btn-sm" style="font-size:.78rem"><i class="fa-brands fa-line"></i> Line</button>
        </div>
      </div>
      <div class="card fade-in-up" style="padding:24px">
        <div style="display:flex;gap:12px;align-items:center;margin-bottom:12px">
          <div style="width:48px;height:48px;border-radius:10px;background:rgba(232,114,42,0.15);display:flex;align-items:center;justify-content:center;font-size:1.4rem">🛒</div>
          <div><h4 style="font-size:1rem">Hammy World</h4><div style="color:var(--text-muted);font-size:.78rem">เชียงใหม่ · หน้าร้าน</div></div>
        </div>
        <p style="color:var(--text-muted);font-size:.82rem;margin-bottom:12px">กรงคุณภาพสูง อาหาร และวัสดุรองกรงออร์แกนิค</p>
        <div style="display:flex;gap:6px">
          <button class="btn btn-outline-gold btn-sm" style="font-size:.78rem"><i class="fa-solid fa-map-pin"></i> แผนที่</button>
          <button class="btn btn-gold btn-sm" style="font-size:.78rem"><i class="fa-brands fa-line"></i> Line</button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MAP -->
<section id="map" class="section" style="background:var(--black)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">แผนที่</div>
      <h2>แผนที่<span class="text-gradient-gold">ร้านค้า/ฟาร์ม</span></h2>
      <div class="divider"></div>
    </div>
    <div class="fade-in-up" style="background:var(--black-card);border:var(--border-gold);border-radius:var(--radius-xl);height:400px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:16px">
      <div style="font-size:3rem">🗺️</div>
      <h3 style="color:var(--text-muted)">แผนที่อินเตอร์แอคทีฟ (เร็วๆ นี้)</h3>
      <p style="color:var(--gray-500);font-size:.88rem">ระบบแผนที่กำลังพัฒนา จะเปิดใช้งานเร็วๆ นี้</p>
    </div>
  </div>
</section>

<!-- REVIEWS -->
<section id="reviews" class="section" style="background:var(--black-light)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">รีวิว</div>
      <h2>รีวิว <span class="text-gradient-gold">&amp; เรตติ้ง</span></h2>
      <div class="divider"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px">
      <div class="card fade-in-up" style="padding:24px">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px">
          <div><h4 style="font-size:.95rem">Golden Hamster Farm</h4><div style="color:var(--gold);font-size:.9rem;margin-top:4px">⭐⭐⭐⭐⭐ <span style="color:var(--text-muted);font-size:.8rem">(47 รีวิว)</span></div></div>
          <span style="font-size:.72rem;color:var(--text-muted)">15 มี.ค. 2026</span>
        </div>
        <p style="color:var(--text-muted);font-size:.85rem;line-height:1.7">"แฮมสเตอร์สุขภาพดีมาก เพาะพันธุ์อย่างมืออาชีพ แนะนำเป็นอย่างยิ่ง!"</p>
        <div style="color:var(--gray-500);font-size:.78rem;margin-top:8px">— สมาชิก SHBA</div>
      </div>
      <div class="card fade-in-up" style="padding:24px">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px">
          <div><h4 style="font-size:.95rem">Paws & Pearls Farm</h4><div style="color:var(--gold);font-size:.9rem;margin-top:4px">⭐⭐⭐⭐⭐ <span style="color:var(--text-muted);font-size:.8rem">(32 รีวิว)</span></div></div>
          <span style="font-size:.72rem;color:var(--text-muted)">10 มี.ค. 2026</span>
        </div>
        <p style="color:var(--text-muted);font-size:.85rem;line-height:1.7">"Winter White สีสวยมาก ตรงตามสายพันธุ์ที่ระบุ บริการดีเยี่ยม"</p>
        <div style="color:var(--gray-500);font-size:.78rem;margin-top:8px">— สมาชิก SHBA</div>
      </div>
    </div>
  </div>
</section>

<footer id="footer">
  <div class="container">
    <div class="footer-bottom"><span>© 2026 Siam Hamster Breeder Association. All rights reserved.</span></div>
  </div>
</footer>'''

# ════════════════════════════════════════════════════════════════
#  COMMUNITY.HTML
# ════════════════════════════════════════════════════════════════
COMMUNITY_CONTENT = '''<!-- HERO -->
<div style="background:var(--gradient-hero);padding:120px 0 60px;position:relative;overflow:hidden">
  <div class="hero-bg"></div><div class="hero-grid"></div>
  <div class="container" style="position:relative;z-index:1;text-align:center">
    <div class="tag" style="display:inline-block;margin-bottom:16px">COMMUNITY</div>
    <h1 style="margin-bottom:12px">ชุมชน<span class="text-gradient-gold">SHBA</span></h1>
    <p style="max-width:560px;margin:0 auto;color:var(--text-muted)">พบปะแลกเปลี่ยนความรู้กับผู้รักแฮมสเตอร์ทั่วประเทศ</p>
    <div style="margin-top:28px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a href="#" class="btn btn-gold"><i class="fa-brands fa-facebook-f"></i> Facebook Group</a>
      <a href="#" class="btn btn-outline-gold"><i class="fa-brands fa-line"></i> Line OA</a>
      <a href="#" class="btn btn-outline-gold"><i class="fa-brands fa-discord"></i> Discord</a>
    </div>
  </div>
</div>

<!-- SOCIAL CHANNELS -->
<section class="section" style="background:var(--black)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">ช่องทาง</div>
      <h2>ช่องทาง<span class="text-gradient-gold">การสื่อสาร</span></h2>
      <div class="divider"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px;max-width:960px;margin:0 auto">
      <div class="card fade-in-up" style="padding:32px;text-align:center;border-top:3px solid #1877f2">
        <div style="font-size:3rem;color:#1877f2;margin-bottom:12px"><i class="fa-brands fa-facebook-f"></i></div>
        <h3 style="margin-bottom:8px">Facebook Group</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin-bottom:16px">กลุ่มหลักสำหรับแลกเปลี่ยนภาพแฮมสเตอร์ ข้อมูล และประกาศต่างๆ</p>
        <div style="font-size:1.4rem;font-weight:800;color:#1877f2;margin-bottom:12px">12,400+ สมาชิก</div>
        <a href="#" class="btn btn-gold w-100" style="justify-content:center">เข้าร่วมกลุ่ม</a>
      </div>
      <div class="card fade-in-up" style="padding:32px;text-align:center;border-top:3px solid #06c755">
        <div style="font-size:3rem;color:#06c755;margin-bottom:12px"><i class="fa-brands fa-line"></i></div>
        <h3 style="margin-bottom:8px">Line Official</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin-bottom:16px">รับข่าวสารประกวด อัปเดตล่าสุด และประกาศอย่างเป็นทางการ</p>
        <div style="font-size:1.4rem;font-weight:800;color:#06c755;margin-bottom:12px">8,200+ ผู้ติดตาม</div>
        <a href="#" class="btn btn-gold w-100" style="justify-content:center">เพิ่มเพื่อน</a>
      </div>
      <div class="card fade-in-up" style="padding:32px;text-align:center;border-top:3px solid #5865f2">
        <div style="font-size:3rem;color:#5865f2;margin-bottom:12px"><i class="fa-brands fa-discord"></i></div>
        <h3 style="margin-bottom:8px">Discord Server</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin-bottom:16px">พื้นที่สนทนาเรียลไทม์ ห้องเฉพาะสายพันธุ์ พันธุกรรม และประกวด</p>
        <div style="font-size:1.4rem;font-weight:800;color:#5865f2;margin-bottom:12px">3,100+ สมาชิก</div>
        <a href="#" class="btn btn-gold w-100" style="justify-content:center">เข้าร่วม Discord</a>
      </div>
      <div class="card fade-in-up" style="padding:32px;text-align:center;border-top:3px solid #ff0050">
        <div style="font-size:3rem;color:#ff0050;margin-bottom:12px"><i class="fa-brands fa-tiktok"></i></div>
        <h3 style="margin-bottom:8px">TikTok</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin-bottom:16px">วิดีโอสั้นแฮมสเตอร์น่ารัก เบื้องหลังงานประกวด และ tips การเลี้ยง</p>
        <div style="font-size:1.4rem;font-weight:800;color:#ff0050;margin-bottom:12px">45,000+ ผู้ติดตาม</div>
        <a href="#" class="btn btn-gold w-100" style="justify-content:center">ติดตาม</a>
      </div>
    </div>
  </div>
</section>

<!-- UPCOMING EVENTS -->
<section class="section" style="background:var(--black-light)">
  <div class="container">
    <div class="section-header fade-in-up">
      <div class="tag">กิจกรรม</div>
      <h2>กิจกรรม<span class="text-gradient-gold">ชุมชน</span></h2>
      <div class="divider"></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:16px;max-width:700px;margin:0 auto">
      <div class="card fade-in-up" style="padding:24px;display:flex;gap:20px;align-items:center">
        <div style="text-align:center;min-width:60px"><div style="font-size:1.6rem;font-weight:900;color:var(--gold);font-family:\'Playfair Display\',serif">20</div><div style="font-size:.72rem;color:var(--text-muted)">เม.ย.</div></div>
        <div style="flex:1"><h4 style="margin-bottom:4px">SHBA Spring Meetup 2026</h4><p style="color:var(--text-muted);font-size:.85rem">งานพบปะสมาชิก แลกเปลี่ยนแฮมสเตอร์ และบรรยายพิเศษด้านพันธุกรรม</p></div>
        <button class="btn btn-gold btn-sm">สมัคร</button>
      </div>
      <div class="card fade-in-up" style="padding:24px;display:flex;gap:20px;align-items:center">
        <div style="text-align:center;min-width:60px"><div style="font-size:1.6rem;font-weight:900;color:var(--orange);font-family:\'Playfair Display\',serif">15</div><div style="font-size:.72rem;color:var(--text-muted)">พ.ค.</div></div>
        <div style="flex:1"><h4 style="margin-bottom:4px">Workshop: Hamster Photography</h4><p style="color:var(--text-muted);font-size:.85rem">เรียนถ่ายภาพแฮมสเตอร์อย่างมืออาชีพ สำหรับการลงประกวดภาพ</p></div>
        <button class="btn btn-outline-gold btn-sm">ดูรายละเอียด</button>
      </div>
    </div>
  </div>
</section>

<footer id="footer">
  <div class="container">
    <div class="footer-bottom"><span>© 2026 Siam Hamster Breeder Association. All rights reserved.</span></div>
  </div>
</footer>'''

# ════════════════════════════════════════════════════════════════
#  CONTACT.HTML
# ════════════════════════════════════════════════════════════════
CONTACT_CONTENT = '''<!-- HERO -->
<div style="background:var(--gradient-hero);padding:120px 0 60px;position:relative;overflow:hidden">
  <div class="hero-bg"></div><div class="hero-grid"></div>
  <div class="container" style="position:relative;z-index:1;text-align:center">
    <div class="tag" style="display:inline-block;margin-bottom:16px">CONTACT US</div>
    <h1 style="margin-bottom:12px">ติดต่อ<span class="text-gradient-gold">เรา</span></h1>
    <p style="max-width:560px;margin:0 auto;color:var(--text-muted)">มีคำถาม ข้อเสนอแนะ หรือต้องการสอบถามข้อมูล ติดต่อเราได้เลย</p>
  </div>
</div>

<!-- CONTACT SECTION -->
<section class="section" style="background:var(--black)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;max-width:960px;margin:0 auto">

      <!-- Contact Info -->
      <div class="fade-in-up">
        <h2 style="margin-bottom:8px">ช่องทาง<span class="text-gradient-gold">ติดต่อ</span></h2>
        <p style="color:var(--text-muted);margin-bottom:32px">เราพร้อมตอบทุกคำถามภายใน 24 ชั่วโมง (วันทำการ)</p>

        <div style="display:flex;flex-direction:column;gap:20px">
          <div style="display:flex;gap:16px;align-items:center">
            <div style="width:48px;height:48px;border-radius:12px;background:rgba(201,162,39,0.1);border:var(--border-gold);display:flex;align-items:center;justify-content:center;flex-shrink:0"><i class="fa-brands fa-line" style="color:#06c755;font-size:1.3rem"></i></div>
            <div><div style="font-weight:600">Line Official</div><div style="color:var(--text-muted);font-size:.85rem">@SHBA_Thailand</div></div>
          </div>
          <div style="display:flex;gap:16px;align-items:center">
            <div style="width:48px;height:48px;border-radius:12px;background:rgba(201,162,39,0.1);border:var(--border-gold);display:flex;align-items:center;justify-content:center;flex-shrink:0"><i class="fa-solid fa-envelope" style="color:var(--gold);font-size:1.2rem"></i></div>
            <div><div style="font-weight:600">อีเมล</div><div style="color:var(--text-muted);font-size:.85rem">contact@shba.or.th</div></div>
          </div>
          <div style="display:flex;gap:16px;align-items:center">
            <div style="width:48px;height:48px;border-radius:12px;background:rgba(201,162,39,0.1);border:var(--border-gold);display:flex;align-items:center;justify-content:center;flex-shrink:0"><i class="fa-brands fa-facebook-f" style="color:#1877f2;font-size:1.2rem"></i></div>
            <div><div style="font-weight:600">Facebook</div><div style="color:var(--text-muted);font-size:.85rem">SHBA Thailand</div></div>
          </div>
          <div style="display:flex;gap:16px;align-items:center">
            <div style="width:48px;height:48px;border-radius:12px;background:rgba(201,162,39,0.1);border:var(--border-gold);display:flex;align-items:center;justify-content:center;flex-shrink:0"><i class="fa-solid fa-location-dot" style="color:var(--orange);font-size:1.2rem"></i></div>
            <div><div style="font-weight:600">ที่ตั้งสมาคม</div><div style="color:var(--text-muted);font-size:.85rem">กรุงเทพมหานคร ประเทศไทย</div></div>
          </div>
        </div>

        <div style="margin-top:32px;padding:20px;background:rgba(201,162,39,0.06);border:var(--border-gold);border-radius:var(--radius-md)">
          <h4 style="color:var(--gold);margin-bottom:8px"><i class="fa-solid fa-clock"></i> เวลาทำการ</h4>
          <p style="color:var(--text-muted);font-size:.85rem">จันทร์ – ศุกร์: 9:00 – 18:00 น.<br/>เสาร์ – อาทิตย์: 10:00 – 16:00 น.</p>
        </div>
      </div>

      <!-- Contact Form -->
      <div class="card fade-in-up" style="padding:36px">
        <h3 style="margin-bottom:20px"><i class="fa-solid fa-paper-plane text-gold"></i> ส่งข้อความ</h3>
        <div class="form-row">
          <div class="form-group"><label>ชื่อ <span class="req">*</span></label><input type="text" class="form-control" placeholder="ชื่อของคุณ" /></div>
          <div class="form-group"><label>นามสกุล</label><input type="text" class="form-control" placeholder="นามสกุล" /></div>
        </div>
        <div class="form-group"><label>อีเมล <span class="req">*</span></label><input type="email" class="form-control" placeholder="your@email.com" /></div>
        <div class="form-group">
          <label>หัวข้อ</label>
          <select class="form-control">
            <option>-- เลือกหัวข้อ --</option>
            <option>สมัครสมาชิก</option>
            <option>งานประกวด</option>
            <option>ไดเรกทอรีฟาร์ม/ร้านค้า</option>
            <option>แจ้งปัญหาระบบ</option>
            <option>อื่นๆ</option>
          </select>
        </div>
        <div class="form-group"><label>ข้อความ <span class="req">*</span></label><textarea class="form-control" rows="5" placeholder="รายละเอียดที่ต้องการสอบถาม..."></textarea></div>
        <button class="btn btn-gold" style="width:100%;justify-content:center"><i class="fa-solid fa-paper-plane"></i> ส่งข้อความ</button>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section" style="background:var(--black-light)">
  <div class="container" style="max-width:700px">
    <div class="section-header fade-in-up">
      <div class="tag">FAQ</div>
      <h2>คำถาม<span class="text-gradient-gold">ที่พบบ่อย</span></h2>
      <div class="divider"></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:12px">
      <div class="card fade-in-up" style="padding:20px;cursor:pointer">
        <div style="display:flex;justify-content:space-between;align-items:center"><h4 style="font-size:.95rem">จะสมัครสมาชิก SHBA ได้อย่างไร?</h4><i class="fa-solid fa-chevron-down" style="color:var(--gold);font-size:.8rem"></i></div>
        <p style="color:var(--text-muted);font-size:.85rem;margin-top:12px">สมัครได้โดยคลิก "สมัครสมาชิก" ที่มุมขวาบน เลือกสมัครด้วย Google หรืออีเมล ไม่มีค่าใช้จ่ายสำหรับสมาชิกสามัญ</p>
      </div>
      <div class="card fade-in-up" style="padding:20px;cursor:pointer">
        <div style="display:flex;justify-content:space-between;align-items:center"><h4 style="font-size:.95rem">Breeder Member ต่างจาก Standard อย่างไร?</h4><i class="fa-solid fa-chevron-down" style="color:var(--gold);font-size:.8rem"></i></div>
        <p style="color:var(--text-muted);font-size:.85rem;margin-top:12px">Breeder Member (฿2,000/ปี) ได้รับสิทธิ์เพิ่มเติม เช่น หน้า Public Profile ของฟาร์ม ลงทะเบียนสายพันธุ์ ส่วนลดประกวด 20% และสิทธิ์โหวตในที่ประชุม</p>
      </div>
      <div class="card fade-in-up" style="padding:20px;cursor:pointer">
        <div style="display:flex;justify-content:space-between;align-items:center"><h4 style="font-size:.95rem">จะลงทะเบียนฟาร์มในไดเรกทอรีได้อย่างไร?</h4><i class="fa-solid fa-chevron-down" style="color:var(--gold);font-size:.8rem"></i></div>
        <p style="color:var(--text-muted);font-size:.85rem;margin-top:12px">ต้องเป็น Breeder Member ก่อน จากนั้นสามารถสมัครลงทะเบียนฟาร์มได้ผ่าน Dashboard</p>
      </div>
    </div>
  </div>
</section>

<footer id="footer">
  <div class="container">
    <div class="footer-bottom"><span>© 2026 Siam Hamster Breeder Association. All rights reserved.</span></div>
  </div>
</footer>'''

# ── Write files ───────────────────────────────────────────────────────────
os.chdir('/sessions/zen-charming-gauss/mnt/SHBA')

pages_to_create = [
    ('about.html',     'เกี่ยวกับสมาคม', 'about',     ABOUT_CONTENT),
    ('directory.html', 'ร้านค้า & ฟาร์ม', 'directory', DIRECTORY_CONTENT),
    ('community.html', 'ชุมชน',           'community', COMMUNITY_CONTENT),
    ('contact.html',   'ติดต่อเรา',       'contact',   CONTACT_CONTENT),
]

for fn, title, key, content in pages_to_create:
    html = page_shell(title, key, content)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created: {fn}')

print('All done.')
