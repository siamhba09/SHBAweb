// ══════════════════════════════════════════════════════════
//  SHBA — Firebase Auth Integration
//  Siam Hamster Breeder Association
// ══════════════════════════════════════════════════════════

import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js';
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
  signOut,
  onAuthStateChanged,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  updateProfile,
  sendPasswordResetEmail,
  sendEmailVerification
} from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js';
import {
  getFirestore,
  doc,
  getDoc,
  setDoc,
  runTransaction,
  serverTimestamp
} from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';

// ── Config ─────────────────────────────────────────────────
const firebaseConfig = {
  apiKey:            "AIzaSyA3isqrom-IqFGvbYtkWzfhTXMgXaBvY1U",
  authDomain:        "shba-1d90f.firebaseapp.com",
  projectId:         "shba-1d90f",
  storageBucket:     "shba-1d90f.firebasestorage.app",
  messagingSenderId: "1066120158359",
  appId:             "1:1066120158359:web:d77ce90aadadba40d05dd2",
  measurementId:     "G-SY96BJNT5B"
};

// ── Init ───────────────────────────────────────────────────
const app      = initializeApp(firebaseConfig);
const auth     = getAuth(app);
const db       = getFirestore(app);
const provider = new GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account' });

// Expose auth & db globally so other module scripts can use them
window._firebaseAuth = auth;
window._firebaseDb   = db;

// ── Auth State ─────────────────────────────────────────────
let currentUser = null;

onAuthStateChanged(auth, async (user) => {
  currentUser = user;
  if (user) {
    await _ensureUserProfile(user);
    await _renderLoggedIn(user);
  } else {
    _renderLoggedOut();
  }
});

// ── Sign In with Google ────────────────────────────────────
window.signInWithGoogle = async function () {
  try {
    const result = await signInWithPopup(auth, provider);
    closeModal('login-modal');
    if (typeof showToast === 'function') {
      showToast('success', `ยินดีต้อนรับ ${result.user.displayName} 👋`);
    }
  } catch (err) {
    console.error('Google Sign-In error:', err);
    if (err.code !== 'auth/popup-closed-by-user') {
      if (typeof showToast === 'function') {
        showToast('error', 'เข้าสู่ระบบไม่สำเร็จ กรุณาลองใหม่อีกครั้ง');
      }
    }
  }
};

// ── Sign Up with Email/Password ────────────────────────
window.signUpWithEmail = async function(firstname, lastname, email, password) {
  const displayName = [firstname, lastname].filter(Boolean).join(' ');
  try {
    const result = await createUserWithEmailAndPassword(auth, email, password);
    // 1) Set displayName in Firebase Auth
    await updateProfile(result.user, { displayName });
    // 2) Generate memberID
    const memberID = await _generateMemberID();
    // 3) Read existing doc first (to preserve createdAt/memberID if race with _ensureUserProfile)
    const ref      = doc(db, 'users', result.user.uid);
    const existing = (await getDoc(ref)).data() || {};
    // 4) Write ALL required fields in one shot
    await setDoc(ref, {
      uid:        result.user.uid,
      memberID:   existing.memberID   || memberID,
      displayName,
      firstname,
      lastname,
      email,
      memberType: existing.memberType || 'standard',
      photoURL:   result.user.photoURL || '',
      provider:   'password',
      createdAt:  existing.createdAt  || serverTimestamp(),
      updatedAt:  serverTimestamp(),
    });
    // 5) Send verification email
    await sendEmailVerification(result.user);
    closeModal('login-modal');
    if (typeof showToast === 'function') {
      showToast('success', `ยินดีต้อนรับ ${displayName}! ส่งอีเมลยืนยันตัวตนแล้ว 📧`);
    }
    return result.user;
  } catch (err) {
    console.error('SignUp error:', err);
    const msgs = {
      'auth/email-already-in-use': 'อีเมลนี้มีบัญชีอยู่แล้ว กรุณาเข้าสู่ระบบ',
      'auth/weak-password':        'รหัสผ่านต้องมีอย่างน้อย 6 ตัวอักษร',
      'auth/invalid-email':        'รูปแบบอีเมลไม่ถูกต้อง',
    };
    if (typeof showToast === 'function') showToast('error', msgs[err.code] || err.message);
    throw err;
  }
};

// ── Sign In with Email/Password ────────────────────────
window.signInWithEmail = async function(email, password) {
  try {
    const result = await signInWithEmailAndPassword(auth, email, password);
    closeModal('login-modal');
    if (typeof showToast === 'function') {
      showToast('success', `ยินดีต้อนรับกลับมา ${result.user.displayName || ''} 👋`);
    }
  } catch (err) {
    console.error('SignIn error:', err);
    const msgs = {
      'auth/user-not-found':   'ไม่พบบัญชีนี้ในระบบ',
      'auth/wrong-password':   'รหัสผ่านไม่ถูกต้อง',
      'auth/invalid-email':    'รูปแบบอีเมลไม่ถูกต้อง',
      'auth/too-many-requests':'พยายามเข้าสู่ระบบหลายครั้งเกินไป กรุณารอสักครู่',
      'auth/invalid-credential': 'อีเมลหรือรหัสผ่านไม่ถูกต้อง',
    };
    if (typeof showToast === 'function') showToast('error', msgs[err.code] || err.message);
    throw err;
  }
};

// ── Reset Password ─────────────────────────────────────
window.resetPassword = async function(email) {
  if (!email) { if (typeof showToast === 'function') showToast('error', 'กรุณาใส่อีเมลก่อน'); return; }
  try {
    await sendPasswordResetEmail(auth, email);
    if (typeof showToast === 'function') showToast('success', 'ส่งลิงก์รีเซ็ตรหัสผ่านไปยังอีเมลแล้ว 📧');
  } catch (err) {
    if (typeof showToast === 'function') showToast('error', 'ไม่พบอีเมลนี้ในระบบ');
  }
};

// ── Sign Out ───────────────────────────────────────────────
window.signOutUser = async function () {
  try {
    await signOut(auth);
    if (typeof showToast === 'function') {
      showToast('info', 'ออกจากระบบแล้ว 👋');
    }
  } catch (err) {
    console.error('Sign-out error:', err);
  }
};

// ── Get Current User ───────────────────────────────────────
window.getCurrentUser = function () { return currentUser; };


// ── Generate memberID: SHBA-YYYY-NNNNN ────────────────────
async function _generateMemberID() {
  const year = new Date().getFullYear();
  try {
    const counterRef = doc(db, 'meta', 'memberCounter');
    const nextNum    = await runTransaction(db, async (tx) => {
      const snap    = await tx.get(counterRef);
      const current = snap.exists() ? (snap.data().count || 0) : 0;
      const next    = current + 1;
      tx.set(counterRef, { count: next }, { merge: true });
      return next;
    });
    return `SHBA-${year}-${String(nextNum).padStart(5, '0')}`;
  } catch {
    // Fallback: timestamp-based unique number
    const num = Math.floor(Date.now() / 1000) % 100000;
    return `SHBA-${year}-${String(num).padStart(5, '0')}`;
  }
}

// ── Create/Update User Profile in Firestore ────────────────
// Fields stored: uid, memberID, displayName, firstname, lastname,
//                email, memberType, photoURL, provider, createdAt, updatedAt
async function _ensureUserProfile(user) {
  try {
    const ref      = doc(db, 'users', user.uid);
    const snap     = await getDoc(ref);
    const existing = snap.exists() ? snap.data() : null;

    // Parse firstname / lastname from Auth displayName
    const rawName   = (user.displayName || '').trim();
    const parts     = rawName.split(/\s+/);
    const firstName = parts[0] || '';
    const lastName  = parts.slice(1).join(' ') || '';
    const provider  = user.providerData?.[0]?.providerId || 'unknown';

    if (!existing) {
      // ── New user: generate memberID + write all required fields ──
      const memberID = await _generateMemberID();
      await setDoc(ref, {
        uid:         user.uid,
        memberID,
        displayName: rawName,
        firstname:   firstName,
        lastname:    lastName,
        email:       user.email    || '',
        memberType:  'standard',
        photoURL:    user.photoURL || '',
        provider,
        createdAt:   serverTimestamp(),
        updatedAt:   serverTimestamp(),
      });
    } else {
      // ── Existing user: patch only null/missing fields ──
      const patch = { updatedAt: serverTimestamp() };
      if (!existing.memberID)                          patch.memberID    = await _generateMemberID();
      if (!existing.uid)                               patch.uid         = user.uid;
      if (!existing.displayName && rawName)            patch.displayName = rawName;
      if (!existing.firstname   && firstName)          patch.firstname   = firstName;
      if (!existing.lastname    && lastName)            patch.lastname    = lastName;
      if (!existing.email       && user.email)          patch.email       = user.email;
      if (!existing.memberType)                         patch.memberType  = 'standard';
      if (!existing.photoURL    && user.photoURL)       patch.photoURL    = user.photoURL;
      if (!existing.provider)                           patch.provider    = provider;
      await setDoc(ref, patch, { merge: true });
    }
  } catch (err) {
    console.warn('Firestore profile update skipped:', err.message);
  }
}

// ── Membership badge config ────────────────────────────────
const _memberBadges = {
  honorary: { icon: '⭐', label: 'Honorary',  color: '#a855f7' },
  breeder:  { icon: '🧬', label: 'Breeder',   color: '#f97316' },
};
function _normType(memberType) {
  if (!memberType) return 'standard';
  // normalize "Breeder Member" → "breeder", "Honorary Member" → "honorary" etc.
  return memberType.toLowerCase().split(' ')[0];
}
function _getBadge(memberType) {
  return _memberBadges[_normType(memberType)] || { icon: '🐾', label: 'Standard', color: '#d4a843' };
}

// ── Update Navbar UI: Logged In ────────────────────────────
async function _renderLoggedIn(user) {
  // Hide login/register buttons
  document.querySelectorAll('.btn-login-trigger, .btn-register-trigger').forEach(el => {
    el.style.display = 'none';
  });

  // Fetch memberType from Firestore
  let memberType = null;
  try {
    const snap = await getDoc(doc(db, 'users', user.uid));
    if (snap.exists()) memberType = snap.data().memberType || null;
  } catch (_) { /* ignore, show Standard as default */ }

  const badge = _getBadge(memberType);

  // Show user avatar dropdown (create if not exists)
  let userMenu = document.getElementById('user-nav-menu');
  if (!userMenu) {
    userMenu = document.createElement('div');
    userMenu.id = 'user-nav-menu';
    userMenu.className = 'user-nav-menu';
    userMenu.innerHTML = `
      <div class="member-badge-pill" style="--badge-color:${badge.color}" title="ระดับสมาชิก">
        <span class="badge-icon">${badge.icon}</span>
        <span class="badge-label">${badge.label}</span>
      </div>
      <button class="user-nav-btn" onclick="toggleUserDropdown()" title="${user.displayName}">
        <img src="${user.photoURL || ''}" onerror="this.style.display='none'" class="user-avatar" alt="avatar"/>
        <span class="user-name">${user.displayName?.split(' ')[0] || 'สมาชิก'}</span>
        <i class="fa-solid fa-chevron-down" style="font-size:.7rem"></i>
      </button>
      <div class="user-dropdown" id="user-dropdown">
        <div class="user-dropdown-header">
          <img src="${user.photoURL || ''}" onerror="this.style.display='none'" class="user-dropdown-avatar" alt="avatar"/>
          <div>
            <div class="user-dropdown-name">${user.displayName}</div>
            <div class="user-dropdown-email">${user.email}</div>
            <div class="user-dropdown-badge" style="color:${badge.color}">${badge.icon} ${badge.label} Member</div>
          </div>
        </div>
        <div class="user-dropdown-divider"></div>
        <a href="myaccount.html" class="user-dropdown-item"><i class="fa-solid fa-gauge"></i> My Account</a>
        <a href="myaccount.html#membership" class="user-dropdown-item"><i class="fa-solid fa-id-card"></i> บัตรสมาชิก</a>
        <a href="myaccount.html#activity" class="user-dropdown-item"><i class="fa-solid fa-trophy"></i> การประกวดของฉัน</a>
        <div class="user-dropdown-divider"></div>
        <button class="user-dropdown-item text-danger" onclick="signOutUser()">
          <i class="fa-solid fa-arrow-right-from-bracket"></i> ออกจากระบบ
        </button>
      </div>
    `;

    // Insert into nav-cta
    const navCta = document.querySelector('.nav-cta');
    if (navCta) navCta.appendChild(userMenu);
  } else {
    // Update badge
    const badgePill = userMenu.querySelector('.member-badge-pill');
    if (badgePill) {
      badgePill.style.setProperty('--badge-color', badge.color);
      const icon  = badgePill.querySelector('.badge-icon');
      const label = badgePill.querySelector('.badge-label');
      if (icon)  icon.textContent  = badge.icon;
      if (label) label.textContent = badge.label;
    }
    // Update dropdown badge line
    const dropBadge = userMenu.querySelector('.user-dropdown-badge');
    if (dropBadge) {
      dropBadge.style.color = badge.color;
      dropBadge.textContent = `${badge.icon} ${badge.label} Member`;
    }
    // Update avatar/name
    const img  = userMenu.querySelector('.user-avatar');
    const name = userMenu.querySelector('.user-name');
    if (img)  img.src = user.photoURL || '';
    if (name) name.textContent = user.displayName?.split(' ')[0] || 'สมาชิก';
    userMenu.style.display = '';
  }

  // Close dropdown when clicking outside
  document.addEventListener('click', _closeDropdownOnOutside);
}

// ── Update Navbar UI: Logged Out ───────────────────────────
function _renderLoggedOut() {
  document.querySelectorAll('.btn-login-trigger, .btn-register-trigger').forEach(el => {
    el.style.display = '';
  });
  const userMenu = document.getElementById('user-nav-menu');
  if (userMenu) userMenu.style.display = 'none';
  document.removeEventListener('click', _closeDropdownOnOutside);
}

// ── Dropdown Toggle ────────────────────────────────────────
window.toggleUserDropdown = function () {
  const dd = document.getElementById('user-dropdown');
  if (dd) dd.classList.toggle('open');
};

function _closeDropdownOnOutside(e) {
  const menu = document.getElementById('user-nav-menu');
  if (menu && !menu.contains(e.target)) {
    const dd = document.getElementById('user-dropdown');
    if (dd) dd.classList.remove('open');
  }
}

// ── Export for use in other scripts ───────────────────────
window.SHBAAuth = { auth, db, currentUser: () => currentUser };
