import re, os

# ── New navbar template (data-page placeholder = PAGE) ───────────────────
NAV_TEMPLATE = '''<!-- NAV -->
<nav id="navbar">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo">
      <div class="nav-logo-icon">🐹</div>
      <div class="nav-logo-text">SHBA<span>Siam Hamster Breeder Association</span></div>
    </a>
    <ul class="nav-links">
      <li class="nav-item"><a href="index.html" class="nav-link{home_active}" data-page="home">หน้าหลัก</a></li>

      <li class="nav-item has-dropdown">
        <a href="about.html" class="nav-link{about_active}" data-page="about">เกี่ยวกับ <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="about.html#history"   class="nav-dd-link"><i class="fa-solid fa-landmark"></i> ประวัติสมาคม SHBA</a>
          <a href="about.html#vision"    class="nav-dd-link"><i class="fa-solid fa-eye"></i> วิสัยทัศน์ &amp; พันธกิจ</a>
          <a href="about.html#committee" class="nav-dd-link"><i class="fa-solid fa-users"></i> คณะกรรมการ</a>
          <a href="about.html#ethics"    class="nav-dd-link"><i class="fa-solid fa-scale-balanced"></i> จรรยาบรรณผู้เพาะพันธุ์</a>
          <a href="about.html#rules"     class="nav-dd-link"><i class="fa-solid fa-file-lines"></i> ข้อบังคับสมาคม</a>
        </div>
      </li>

      <li class="nav-item has-dropdown">
        <a href="membership.html" class="nav-link{membership_active}" data-page="membership">สมาชิก <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="membership.html#membership"     class="nav-dd-link"><i class="fa-solid fa-id-card"></i> ประเภทสมาชิก &amp; สิทธิประโยชน์</a>
          <a href="membership.html#register"        class="nav-dd-link"><i class="fa-solid fa-user-plus"></i> สมัครสมาชิกออนไลน์</a>
          <a href="membership.html#upgrade-section" class="nav-dd-link"><i class="fa-solid fa-rotate"></i> ต่ออายุสมาชิก</a>
          <a href="membership.html#dashboard"       class="nav-dd-link"><i class="fa-solid fa-gauge"></i> สมาชิก Dashboard</a>
          <a href="membership.html#digital-card"    class="nav-dd-link"><i class="fa-solid fa-credit-card"></i> บัตรสมาชิกดิจิทัล</a>
        </div>
      </li>

      <li class="nav-item has-dropdown">
        <a href="competitions.html" class="nav-link{competitions_active}" data-page="competitions">การประกวด <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
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
        <a href="directory.html" class="nav-link{directory_active}" data-page="directory">ร้านค้า &amp; ฟาร์ม <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="directory.html#breeders" class="nav-dd-link"><i class="fa-solid fa-house"></i> ไดเรกทอรีฟาร์ม/ผู้เพาะพันธุ์</a>
          <a href="directory.html#shops"    class="nav-dd-link"><i class="fa-solid fa-store"></i> ไดเรกทอรีร้านค้า</a>
          <a href="directory.html#map"      class="nav-dd-link"><i class="fa-solid fa-map-location-dot"></i> แผนที่ร้านค้า/ฟาร์ม</a>
          <a href="directory.html#reviews"  class="nav-dd-link"><i class="fa-solid fa-star-half-stroke"></i> รีวิว &amp; เรตติ้ง</a>
        </div>
      </li>

      <li class="nav-item has-dropdown">
        <a href="knowledge.html" class="nav-link{knowledge_active}" data-page="knowledge">คลังความรู้ <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        <div class="nav-dropdown">
          <a href="genetics.html"          class="nav-dd-link"><i class="fa-solid fa-dna"></i> Genetics &amp; สีสัน</a>
          <a href="knowledge.html#care"    class="nav-dd-link"><i class="fa-solid fa-heart"></i> การดูแลทั่วไป</a>
          <a href="knowledge.html#species" class="nav-dd-link"><i class="fa-solid fa-paw"></i> สายพันธุ์แฮมสเตอร์</a>
          <a href="knowledge.html#articles"class="nav-dd-link"><i class="fa-solid fa-book-open"></i> บทความ &amp; วิจัย</a>
        </div>
      </li>

      <li class="nav-item"><a href="news.html" class="nav-link{news_active}" data-page="news">ข่าวสาร</a></li>
      <li class="nav-item"><a href="community.html" class="nav-link{community_active}" data-page="community">ชุมชน</a></li>
      <li class="nav-item"><a href="contact.html" class="nav-link{contact_active}" data-page="contact">ติดต่อเรา</a></li>
    </ul>
    <div class="nav-cta">
      <button class="btn btn-outline-gold btn-sm btn-login-trigger" onclick="openModal(\'login-modal\')"><i class="fa-regular fa-user"></i> เข้าสู่ระบบ</button>
      <a href="#" onclick="openModal(\'login-modal\'); switchAuthTab(\'signup\'); return false;" class="btn btn-gold btn-sm btn-register-trigger"><i class="fa-solid fa-plus"></i> สมัครสมาชิก</a>
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
        <a href="about.html#history"   class="mobile-nav-sub-link"><i class="fa-solid fa-landmark"></i> ประวัติสมาคม SHBA</a>
        <a href="about.html#vision"    class="mobile-nav-sub-link"><i class="fa-solid fa-eye"></i> วิสัยทัศน์ &amp; พันธกิจ</a>
        <a href="about.html#committee" class="mobile-nav-sub-link"><i class="fa-solid fa-users"></i> คณะกรรมการ</a>
        <a href="about.html#ethics"    class="mobile-nav-sub-link"><i class="fa-solid fa-scale-balanced"></i> จรรยาบรรณผู้เพาะพันธุ์</a>
        <a href="about.html#rules"     class="mobile-nav-sub-link"><i class="fa-solid fa-file-lines"></i> ข้อบังคับสมาคม</a>
      </div>
    </div>

    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">สมาชิก <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="membership.html#membership"     class="mobile-nav-sub-link"><i class="fa-solid fa-id-card"></i> ประเภทสมาชิก</a>
        <a href="membership.html#register"        class="mobile-nav-sub-link"><i class="fa-solid fa-user-plus"></i> สมัครสมาชิก</a>
        <a href="membership.html#dashboard"       class="mobile-nav-sub-link"><i class="fa-solid fa-gauge"></i> Dashboard</a>
        <a href="membership.html#digital-card"    class="mobile-nav-sub-link"><i class="fa-solid fa-credit-card"></i> บัตรสมาชิก</a>
      </div>
    </div>

    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">การประกวด <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="competitions.html#calendar"  class="mobile-nav-sub-link"><i class="fa-solid fa-calendar-days"></i> ปฏิทินการประกวด</a>
        <a href="competitions.html#results"   class="mobile-nav-sub-link"><i class="fa-solid fa-trophy"></i> ผลการประกวด</a>
        <a href="competitions.html#standards" class="mobile-nav-sub-link"><i class="fa-solid fa-star"></i> มาตรฐานการประกวด</a>
        <a href="competitions.html#judges"    class="mobile-nav-sub-link"><i class="fa-solid fa-user-tie"></i> กรรมการตัดสิน</a>
      </div>
    </div>

    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">ร้านค้า &amp; ฟาร์ม <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="directory.html#breeders" class="mobile-nav-sub-link"><i class="fa-solid fa-house"></i> ไดเรกทอรีฟาร์ม</a>
        <a href="directory.html#shops"    class="mobile-nav-sub-link"><i class="fa-solid fa-store"></i> ไดเรกทอรีร้านค้า</a>
        <a href="directory.html#map"      class="mobile-nav-sub-link"><i class="fa-solid fa-map-location-dot"></i> แผนที่</a>
        <a href="directory.html#reviews"  class="mobile-nav-sub-link"><i class="fa-solid fa-star-half-stroke"></i> รีวิว</a>
      </div>
    </div>

    <div class="mobile-nav-group">
      <button class="mobile-nav-group-btn" onclick="toggleMobileGroup(this)">คลังความรู้ <i class="fa-solid fa-chevron-down mnav-arrow"></i></button>
      <div class="mobile-nav-sub">
        <a href="genetics.html"           class="mobile-nav-sub-link"><i class="fa-solid fa-dna"></i> Genetics &amp; สีสัน</a>
        <a href="knowledge.html#care"     class="mobile-nav-sub-link"><i class="fa-solid fa-heart"></i> การดูแลทั่วไป</a>
        <a href="knowledge.html#species"  class="mobile-nav-sub-link"><i class="fa-solid fa-paw"></i> สายพันธุ์แฮมสเตอร์</a>
        <a href="knowledge.html#articles" class="mobile-nav-sub-link"><i class="fa-solid fa-book-open"></i> บทความ &amp; วิจัย</a>
      </div>
    </div>

    <a href="news.html"      class="mobile-nav-link">ข่าวสาร</a>
    <a href="community.html" class="mobile-nav-link">ชุมชน</a>
    <a href="contact.html"   class="mobile-nav-link">ติดต่อเรา</a>

    <div class="mobile-nav-divider"></div>
    <div class="mobile-nav-btns">
      <button class="btn btn-outline-gold btn-login-trigger" onclick="closeMobileNav(); openModal(\'login-modal\')"><i class="fa-regular fa-user"></i> เข้าสู่ระบบ</button>
      <a href="#" class="btn btn-gold btn-register-trigger" onclick="closeMobileNav(); openModal(\'login-modal\'); switchAuthTab(\'signup\')"><i class="fa-solid fa-plus"></i> สมัครสมาชิก</a>
    </div>
  </div>
</div>'''

# ── Pages to update ───────────────────────────────────────────────────────
PAGES = {
    'index.html':        'home',
    'membership.html':   'membership',
    'competitions.html': 'competitions',
    'genetics.html':     'knowledge',
    'knowledge.html':    'knowledge',
    'news.html':         'news',
}

pages_keys = ['home','about','membership','competitions','directory','knowledge','news','community','contact']

def make_nav(active_page):
    kwargs = {f'{p}_active': ' active' if p == active_page else '' for p in pages_keys}
    return NAV_TEMPLATE.format(**kwargs)

# ── Replace nav block in each file ────────────────────────────────────────
# Pattern: from <!-- NAV --> to closing </div> of mobile-nav
NAV_RE = re.compile(
    r'<!-- NAV -->\s*<nav id="navbar">.*?</nav>\s*<div class="mobile-nav"[^>]*>.*?</div>',
    re.DOTALL
)

os.chdir('/sessions/zen-charming-gauss/mnt/SHBA')

for fn, page in PAGES.items():
    if not os.path.exists(fn):
        print(f'SKIP (not found): {fn}')
        continue
    txt = open(fn, encoding='utf-8').read()
    new_nav = make_nav(page)
    new_txt, n = NAV_RE.subn(new_nav, txt)
    if n > 0:
        open(fn, 'w', encoding='utf-8').write(new_txt)
        print(f'OK ({n} replacement): {fn}')
    else:
        print(f'NO MATCH: {fn}')

print('Done.')
