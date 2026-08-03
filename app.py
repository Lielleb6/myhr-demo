import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MyHR+ App", layout="wide", initial_sidebar_state="collapsed")

# --- Remove Streamlit's default chrome (header, padding, footer) so the app
# looks like a real full-screen mobile app instead of a page with margins. ---
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
        iframe {border: none !important;}
        body {overflow: hidden;}
    </style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
    :root {
        --navy-deep:   #082a4d;
        --navy:        #0d3f6e;
        --navy-light:  #1a5691;
        --ink:         #101a2b;
        --ink-soft:    #56657a;
        --ink-faint:   #8b98a8;
        --paper:       #eef1f6;
        --card:        #ffffff;
        --emerald:     #1f9d6b;
        --emerald-tint:#e7f6ee;
        --amber:       #c98a2c;
        --amber-tint:  #fbf1e0;
        --blue-tint:   #e8f1fc;
        --line:        #e7ebf1;
    }
    * { box-sizing: border-box; }
    html, body {
        margin: 0; padding: 0; background: var(--paper);
        font-family: 'Assistant', sans-serif; overflow-x: hidden; color: var(--ink);
        -webkit-tap-highlight-color: transparent;
    }

    @keyframes pulse {
        0% { transform: scale(0.96); opacity: 0.75; }
        50% { transform: scale(1.03); opacity: 1; }
        100% { transform: scale(0.96); opacity: 0.75; }
    }
    .pulse-text { animation: pulse 1.6s infinite ease-in-out; }
    .pulse-sub  { animation: pulse 1.6s infinite ease-in-out; animation-delay: 0.2s; }

    #splash {
        position: fixed; inset: 0; z-index: 999;
        background: radial-gradient(120% 90% at 50% 0%, var(--navy-light) 0%, var(--navy) 45%, var(--navy-deep) 100%);
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        transition: opacity 0.5s ease-out;
    }
    #splash.hidden { opacity: 0; pointer-events: none; }

    #app { opacity: 0; transition: opacity 0.5s ease-in; }
    #app.visible { opacity: 1; }

    .shell { width: 100%; max-width: 480px; margin: 0 auto; min-height: 100vh; padding-bottom: 118px; }

    /* ---------- Header ---------- */
    .header {
        position: relative; overflow: hidden;
        background: linear-gradient(160deg, var(--navy-light) 0%, var(--navy) 55%, var(--navy-deep) 100%);
        color: #fff; padding: 34px 22px 40px 22px;
        border-bottom-right-radius: 28px; border-bottom-left-radius: 28px;
        box-shadow: 0 12px 24px -8px rgba(6, 30, 58, 0.45);
    }
    .header-arcs { position: absolute; top: -40px; left: -60px; opacity: 0.16; pointer-events: none; }
    .header-row { display: flex; justify-content: space-between; align-items: flex-start; position: relative; z-index: 2; }
    .avatar-badge {
        width: 46px; height: 46px; border-radius: 14px; flex-shrink: 0;
        background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.22);
        display: flex; align-items: center; justify-content: center;
    }
    .greeting-name { font-size: 21px; font-weight: 800; letter-spacing: 0.2px; margin-bottom: 3px; }
    .greeting-org  { font-size: 14px; font-weight: 600; opacity: 0.92; }
    .greeting-unit { font-size: 12.5px; opacity: 0.68; margin-top: 1px; font-weight: 500; }
    .brand-mark { font-size: 20px; font-weight: 800; letter-spacing: 0.5px; opacity: 0.96; }
    .brand-mark span { color: #6fd9b5; }

    /* ---------- Section label ---------- */
    .eyebrow {
        font-size: 12.5px; font-weight: 700; color: var(--ink-faint);
        letter-spacing: 0.3px; margin: 22px 4px 8px 4px;
    }
    .section-title {
        color: var(--navy-deep); font-size: 20px; font-weight: 800; margin: 0 4px 14px 4px;
    }

    /* ---------- Cards ---------- */
    .content { padding: 0 16px; position: relative; z-index: 10; margin-top: -22px; }
    .card {
        background: var(--card); border-radius: 18px; padding: 18px 20px;
        margin-bottom: 14px; border: 1px solid var(--line);
        box-shadow: 0 1px 2px rgba(16,26,43,0.04), 0 10px 24px -14px rgba(16,26,43,0.16);
        display: flex; align-items: center; justify-content: space-between;
    }
    .card-label { font-size: 13.5px; font-weight: 700; color: var(--ink-soft); margin-bottom: 3px; }
    .card-value { font-size: 26px; font-weight: 900; color: var(--ink); line-height: 1.15; }
    .card-sub   { font-size: 12.5px; color: var(--ink-faint); margin-top: 2px; font-weight: 500; }
    .icon-badge {
        width: 52px; height: 52px; border-radius: 15px; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center;
    }

    .ring-wrap { position: relative; width: 68px; height: 68px; border-radius: 50%; flex-shrink: 0; }
    .ring-center {
        position: absolute; inset: 6px; background: var(--card); border-radius: 50%;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
    }
    .ring-num { font-size: 20px; font-weight: 900; color: var(--ink); line-height: 1; }
    .ring-unit { font-size: 11px; color: var(--ink-faint); font-weight: 600; }

    .salary-card { flex-direction: column; align-items: stretch; padding: 18px 20px 16px 20px; }
    .salary-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; }
    .bars { display: flex; align-items: flex-end; gap: 5px; height: 44px; }
    .bar { width: 9px; border-radius: 3px; background: #dbe3ee; }
    .bar.up { background: var(--emerald); position: relative; }
    .bar.up::after {
        content: "↑"; position: absolute; top: -17px; left: 50%; transform: translateX(-50%);
        color: var(--emerald); font-size: 13px; font-weight: 800;
    }
    .cta-outline {
        width: 100%; text-align: center; border: 1.5px solid var(--navy); color: var(--navy);
        padding: 11px; border-radius: 12px; font-weight: 700; font-size: 14.5px;
        cursor: pointer; transition: background 0.15s ease, transform 0.1s ease;
    }
    .cta-outline:active { background: var(--blue-tint); transform: scale(0.985); }

    /* ---------- Bottom nav ---------- */
    .bottom-nav {
        position: fixed; bottom: 0; left: 0; right: 0; max-width: 480px; margin: 0 auto;
        background: rgba(255,255,255,0.92); backdrop-filter: blur(10px);
        padding: 10px 8px calc(18px + env(safe-area-inset-bottom, 8px)) 8px;
        display: flex; justify-content: space-around; align-items: center;
        border-top: 1px solid var(--line); box-shadow: 0 -8px 24px -12px rgba(16,26,43,0.18);
        z-index: 100;
    }
    .nav-item {
        display: flex; flex-direction: column; align-items: center; gap: 3px;
        font-size: 11.5px; font-weight: 600; color: var(--ink-faint);
        cursor: pointer; padding: 6px 16px; border-radius: 12px;
        transition: background 0.15s ease, color 0.15s ease;
        -webkit-user-select: none; user-select: none;
    }
    .nav-item:active { background: var(--line); }
    .nav-item.active { color: var(--navy); font-weight: 800; background: var(--blue-tint); }

    /* ---------- Modal ---------- */
    #modal-overlay {
        position: fixed; inset: 0; z-index: 1000;
        background: rgba(8, 42, 77, 0.5); backdrop-filter: blur(2px);
        display: none; justify-content: center; align-items: center;
        opacity: 0; transition: opacity 0.25s ease;
    }
    #modal-overlay.visible { display: flex; opacity: 1; }
    .modal-box {
        background: var(--card); border-radius: 20px; padding: 32px 26px 26px 26px;
        width: 82%; max-width: 320px; text-align: center;
        box-shadow: 0 24px 48px -12px rgba(8,42,77,0.35);
        transform: scale(0.92); transition: transform 0.25s ease;
    }
    #modal-overlay.visible .modal-box { transform: scale(1); }
    .modal-icon {
        width: 56px; height: 56px; border-radius: 16px; background: var(--blue-tint);
        display: flex; align-items: center; justify-content: center; margin: 0 auto 14px auto;
    }
    .modal-title { font-size: 18px; font-weight: 800; color: var(--navy-deep); }
    .modal-sub   { font-size: 14.5px; color: var(--ink-soft); margin-top: 6px; line-height: 1.5; }
    .modal-close-btn {
        margin-top: 20px; background: var(--navy); color: white; border: none;
        padding: 11px 26px; border-radius: 12px; font-weight: 700; font-size: 14px;
        font-family: 'Assistant', sans-serif; cursor: pointer; width: 100%;
        transition: background 0.15s ease;
    }
    .modal-close-btn:active { background: var(--navy-deep); }
</style>
</head>
<body>

<!-- Splash screen -->
<div id="splash">
    <div class="pulse-text" dir="ltr" style="color: white; font-size: 52px; font-weight: 900; letter-spacing: 1px;">MyHR<span style="color:#6fd9b5;">+</span></div>
    <div class="pulse-sub" style="color: #b9d3ec; font-size: 16px; margin-top: 10px; font-weight: 600;">מתחבר למערכות...</div>
</div>

<!-- Main app -->
<div id="app">
<div class="shell">

    <!-- Header -->
    <div class="header">
        <svg class="header-arcs" width="220" height="220" viewBox="0 0 220 220" fill="none">
            <circle cx="20" cy="20" r="40" stroke="white" stroke-width="1.4"/>
            <circle cx="20" cy="20" r="75" stroke="white" stroke-width="1.4"/>
            <circle cx="20" cy="20" r="110" stroke="white" stroke-width="1.4"/>
        </svg>
        <div class="header-row">
            <div style="display: flex; align-items: flex-start; gap: 13px;">
                <div class="avatar-badge">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.7"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                </div>
                <div style="text-align: right;">
                    <div class="greeting-name">שלום, דניאל</div>
                    <div class="greeting-org">אלביט מערכות</div>
                    <div class="greeting-unit">חטיבה אווירית</div>
                </div>
            </div>
            <div dir="ltr" class="brand-mark">MyHR<span>+</span></div>
        </div>
    </div>

    <!-- Content -->
    <div class="content">
        <div class="eyebrow">סקירה כללית</div>
        <div class="section-title">הדשבורד האישי שלי</div>

        <!-- Vacation Card -->
        <div class="card">
            <div style="text-align: right;">
                <div class="card-label">יתרת חופשה</div>
                <div class="card-value">12 ימים</div>
                <div class="card-sub">מתוך 20 ימים שנתיים</div>
            </div>
            <div class="ring-wrap" style="background: conic-gradient(var(--emerald) 0% 60%, #e9edf3 60% 100%);">
                <div class="ring-center">
                    <span class="ring-num">12</span>
                    <span class="ring-unit">ימים</span>
                </div>
            </div>
        </div>

        <!-- Cibus Card -->
        <div class="card">
            <div style="text-align: right;">
                <div class="card-label">יתרת סיבוס (Cibus)</div>
                <div class="card-value" dir="rtl">₪450</div>
                <div class="card-sub" style="max-width: 190px;">היתרה לספטמבר. כל יום זכאי ל-90 ש"ח</div>
            </div>
            <div class="icon-badge" style="background: var(--blue-tint);">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/></svg>
            </div>
        </div>

        <!-- Salary Card -->
        <div class="card salary-card">
            <div class="salary-top">
                <div style="text-align: right;">
                    <div class="card-label">עדכון שכר</div>
                    <div class="card-sub" style="margin-top: 3px;">עדכון שכר מהתלוש האחרון</div>
                </div>
                <div class="bars">
                    <div class="bar" style="height: 38%;"></div>
                    <div class="bar" style="height: 55%;"></div>
                    <div class="bar" style="height: 46%;"></div>
                    <div class="bar" style="height: 66%;"></div>
                    <div class="bar" style="height: 50%;"></div>
                    <div class="bar up" style="height: 100%;"></div>
                </div>
            </div>
            <div class="cta-outline">צפייה בתלוש האחרון</div>
        </div>
    </div>

    <!-- Bottom Nav -->
    <div class="bottom-nav">
        <div class="nav-item nav-construction">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            פרופיל
        </div>
        <div class="nav-item nav-construction">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            מסמכים
        </div>
        <div class="nav-item nav-construction">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="8" width="18" height="14" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="22"></line><path d="M12 8V4h-3a3 3 0 0 0 0 6h6a3 3 0 0 0 0-6h-3v4"></path></svg>
            הטבות
        </div>
        <div class="nav-item active">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            בית
        </div>
    </div>

</div>
</div>

<!-- Under-construction modal -->
<div id="modal-overlay">
    <div class="modal-box">
        <div class="modal-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M12 9v4M12 17h.01M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0Z"/></svg>
        </div>
        <div class="modal-title">בקרוב!</div>
        <div class="modal-sub">העמוד הזה נמצא בתהליך בנייה</div>
        <button id="modal-close-btn" class="modal-close-btn">סגור</button>
    </div>
</div>

<script>
    var overlay = document.getElementById('modal-overlay');

    function showUnderConstruction() { overlay.classList.add('visible'); }
    function closeModal() { overlay.classList.remove('visible'); }

    var constructionItems = document.querySelectorAll('.nav-construction');
    for (var i = 0; i < constructionItems.length; i++) {
        constructionItems[i].addEventListener('click', showUnderConstruction);
    }

    document.getElementById('modal-close-btn').addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
        if (e.target === overlay) closeModal();
    });

    // Smooth splash -> app transition, done entirely client-side.
    setTimeout(function () {
        document.getElementById('splash').classList.add('hidden');
        document.getElementById('app').classList.add('visible');
        setTimeout(function () {
            document.getElementById('splash').style.display = 'none';
        }, 500);
    }, 1600);
</script>

</body>
</html>
""", height=926, scrolling=True)
