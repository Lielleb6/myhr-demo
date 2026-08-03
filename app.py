import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MyHR+ App", layout="wide", initial_sidebar_state="collapsed")

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
        --paper:       #f4f6f9;
        --card:        #ffffff;
        --emerald:     #1f9d6b;
        --emerald-tint:#e7f6ee;
        --blue-tint:   #e8f1fc;
        --line:        #e7ebf1;
    }
    * { box-sizing: border-box; }
    html, body {
        margin: 0; padding: 0; background: var(--paper);
        font-family: 'Assistant', sans-serif; overflow: hidden; color: var(--ink);
        -webkit-tap-highlight-color: transparent;
        height: 100vh;
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
        transition: opacity 0.4s ease-out, visibility 0.4s;
    }
    #splash.hidden { opacity: 0; visibility: hidden; pointer-events: none; }

    #app { opacity: 0; transition: opacity 0.4s ease-in; height: 100vh; display: flex; flex-direction: column; }
    #app.visible { opacity: 1; }

    .shell { width: 100%; max-width: 480px; margin: 0 auto; height: 100vh; display: flex; flex-direction: column; position: relative; }

    /* ---------- Header ---------- */
    .header {
        position: relative; overflow: hidden; flex-shrink: 0;
        background: linear-gradient(160deg, var(--navy-light) 0%, var(--navy) 55%, var(--navy-deep) 100%);
        color: #fff; padding: 24px 20px 30px 20px;
        border-bottom-right-radius: 26px; border-bottom-left-radius: 26px;
        box-shadow: 0 8px 20px -6px rgba(6, 30, 58, 0.35);
    }
    .header-arcs { position: absolute; top: -40px; left: -60px; opacity: 0.14; pointer-events: none; }
    .header-row { display: flex; justify-content: space-between; align-items: flex-start; position: relative; z-index: 2; }
    .avatar-badge {
        width: 42px; height: 42px; border-radius: 12px; flex-shrink: 0;
        background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.24);
        display: flex; align-items: center; justify-content: center;
    }
    .greeting-name { font-size: 20px; font-weight: 800; letter-spacing: 0.2px; margin-bottom: 2px; }
    .greeting-org  { font-size: 13.5px; font-weight: 600; opacity: 0.92; }
    .greeting-unit { font-size: 12px; opacity: 0.7; font-weight: 500; }
    .brand-mark { font-size: 19px; font-weight: 800; letter-spacing: 0.5px; opacity: 0.96; }
    .brand-mark span { color: #6fd9b5; }

    /* ---------- Views / Content ---------- */
    .view-container {
        flex: 1; overflow-y: auto; padding: 16px 16px 90px 16px; display: none;
    }
    .view-container.active-view { display: block; }

    .eyebrow {
        font-size: 12px; font-weight: 700; color: var(--ink-faint);
        letter-spacing: 0.3px; margin: 4px 4px 4px 4px;
    }
    .section-title {
        color: var(--navy-deep); font-size: 19px; font-weight: 800; margin: 0 4px 12px 4px;
    }

    /* ---------- Cards ---------- */
    .card {
        background: var(--card); border-radius: 18px; padding: 16px 18px;
        margin-bottom: 12px; border: 1px solid var(--line);
        box-shadow: 0 2px 4px rgba(16,26,43,0.02), 0 10px 24px -12px rgba(16,26,43,0.1);
        display: flex; align-items: center; justify-content: space-between;
    }
    .card-label { font-size: 13px; font-weight: 700; color: var(--ink-soft); margin-bottom: 2px; }
    .card-value { font-size: 24px; font-weight: 900; color: var(--ink); line-height: 1.1; }
    .card-sub   { font-size: 12px; color: var(--ink-faint); margin-top: 2px; font-weight: 500; }
    
    .icon-badge {
        width: 48px; height: 48px; border-radius: 14px; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center;
    }

    .ring-wrap { position: relative; width: 62px; height: 62px; border-radius: 50%; flex-shrink: 0; }
    .ring-center {
        position: absolute; inset: 5px; background: var(--card); border-radius: 50%;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
    }
    .ring-num { font-size: 18px; font-weight: 900; color: var(--ink); line-height: 1; }
    .ring-unit { font-size: 10.5px; color: var(--ink-faint); font-weight: 600; }

    .salary-card { flex-direction: column; align-items: stretch; padding: 16px 18px 14px 18px; }
    .salary-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }
    .bars { display: flex; align-items: flex-end; gap: 5px; height: 38px; }
    .bar { width: 8px; border-radius: 3px; background: #dbe3ee; }
    .bar.up { background: var(--emerald); position: relative; }
    .bar.up::after {
        content: "↑"; position: absolute; top: -15px; left: 50%; transform: translateX(-50%);
        color: var(--emerald); font-size: 12px; font-weight: 800;
    }
    .cta-outline {
        width: 100%; text-align: center; border: 1.5px solid var(--navy); color: var(--navy);
        padding: 10px; border-radius: 12px; font-weight: 700; font-size: 14px;
        cursor: pointer; transition: background 0.15s ease;
    }
    .cta-outline:active { background: var(--blue-tint); }

    /* ---------- Bottom nav ---------- */
    .bottom-nav {
        position: absolute; bottom: 0; left: 0; right: 0; max-width: 480px; margin: 0 auto;
        background: rgba(255, 255, 255, 0.96); backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 10px 8px calc(14px + env(safe-area-inset-bottom, 6px)) 8px;
        display: flex; justify-content: space-around; align-items: center;
        border-top: 1px solid var(--line); box-shadow: 0 -8px 24px -10px rgba(16,26,43,0.12);
        z-index: 100;
    }
    .nav-item {
        display: flex; flex-direction: column; align-items: center; gap: 2px;
        font-size: 11px; font-weight: 600; color: var(--ink-faint);
        cursor: pointer; padding: 6px 16px; border-radius: 12px;
        transition: all 0.15s ease;
        -webkit-user-select: none; user-select: none;
    }
    .nav-item.active { color: var(--navy); font-weight: 800; background: var(--blue-tint); }
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
        <svg class="header-arcs" width="200" height="200" viewBox="0 0 220 220" fill="none">
            <circle cx="20" cy="20" r="40" stroke="white" stroke-width="1.4"/>
            <circle cx="20" cy="20" r="75" stroke="white" stroke-width="1.4"/>
            <circle cx="20" cy="20" r="110" stroke="white" stroke-width="1.4"/>
        </svg>
        <div class="header-row">
            <div style="display: flex; align-items: flex-start; gap: 12px;">
                <div class="avatar-badge">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.7"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
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

    <!-- VIEW 1: HOME (בית) -->
    <div id="view-home" class="view-container active-view">
        <div class="eyebrow">סקירה כללית</div>
        <div class="section-title">הדשבורד האישי שלי</div>

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

        <div class="card">
            <div style="text-align: right;">
                <div class="card-label">יתרת סיבוס (Cibus)</div>
                <div class="card-value" dir="rtl">₪450</div>
                <div class="card-sub" style="max-width: 180px;">היתרה לספטמבר. כל יום זכאי ל-90 ש\"ח</div>
            </div>
            <div class="icon-badge" style="background: var(--blue-tint);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/></svg>
            </div>
        </div>

        <div class="card salary-card">
            <div class="salary-top">
                <div style="text-align: right;">
                    <div class="card-label">עדכון שכר</div>
                    <div class="card-sub">עדכון שכר מהתלוש האחרון</div>
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
            <div class="cta-outline" onclick="switchView('documents')">צפייה בתלוש האחרון</div>
        </div>
    </div>

    <!-- VIEW 2: BENEFITS (הטבות) -->
    <div id="view-benefits" class="view-container">
        <div class="eyebrow">רווחה והטבות</div>
        <div class="section-title">ההטבות שלך באלביט</div>

        <div class="card">
            <div style="text-align: right;">
                <div class="card-label">קרן השתלמות</div>
                <div class="card-value" dir="rtl">₪42,100</div>
                <div class="card-sub">תחנת פירעון קרובה: אפריל 2027</div>
            </div>
            <div class="icon-badge" style="background: #e7f6ee;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="1.6"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
        </div>

        <div class="card">
            <div style="text-align: right;">
                <div class="card-label">מועדון קונטקט</div>
                <div class="card-value" style="font-size: 20px; color: var(--emerald);">פעיל ומעודכן</div>
                <div class="card-sub">הנחות בלעדיות לנושאי משרה בחטיבה</div>
            </div>
            <div class="icon-badge" style="background: var(--blue-tint);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
        </div>
    </div>

    <!-- VIEW 3: DOCUMENTS (מסמכים) -->
    <div id="view-documents" class="view-container">
        <div class="eyebrow">ארכיון דיגיטלי</div>
        <div class="section-title">תלושי שכר ואישורים</div>

        <div class="card">
            <div style="text-align: right;">
                <div class="card-label">תלוש שכר - יולי 2026</div>
                <div class="card-value" style="font-size: 18px;">חתום דיגיטלית</div>
                <div class="card-sub">הופק ב-01/08/2026</div>
            </div>
            <div class="icon-badge" style="background: var(--blue-tint);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            </div>
        </div>

        <div class="card">
            <div style="text-align: right;">
                <div class="card-label">אישור העסקה ושכר</div>
                <div class="card-value" style="font-size: 18px;">מוכן להורדה</div>
                <div class="card-sub">עבור בנק / משכנתא</div>
            </div>
            <div class="icon-badge" style="background: var(--blue-tint);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            </div>
        </div>
    </div>

    <!-- VIEW 4: PROFILE (פרופיל) -->
    <div id="view-profile" class="view-container">
        <div class="eyebrow">פרטים אישיים</div>
        <div class="section-title">כרטיס עובד - אלביט מערכות</div>

        <div class="card" style="flex-direction: column; align-items: flex-start; gap: 8px;">
            <div style="display: flex; justify-content: space-between; width: 100%;">
                <span style="color: var(--ink-faint); font-weight: 600;">שם מלא:</span>
                <span style="font-weight: 800;">דניאל (אלביט)</span>
            </div>
            <div style="display: flex; justify-content: space-between; width: 100%;">
                <span style="color: var(--ink-faint); font-weight: 600;">חטיבה:</span>
                <span style="font-weight: 800;">חטיבה אווירית</span>
            </div>
            <div style="display: flex; justify-content: space-between; width: 100%;">
                <span style="color: var(--ink-faint); font-weight: 600;">מספר עובד:</span>
                <span style="font-weight: 800;" dir="ltr">EL-88492</span>
            </div>
            <div style="display: flex; justify-content: space-between; width: 100%;">
                <span style="color: var(--ink-faint); font-weight: 600;">סטטוס העסקה:</span>
                <span style="font-weight: 800; color: var(--emerald);">עובד קבוע</span>
            </div>
        </div>
    </div>

    <!-- Bottom Nav -->
    <div class="bottom-nav">
        <div class="nav-item" id="nav-profile" onclick="switchView('profile')">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            פרופיל
        </div>
        <div class="nav-item" id="nav-documents" onclick="switchView('documents')">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            מסמכים
        </div>
        <div class="nav-item" id="nav-benefits" onclick="switchView('benefits')">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="8" width="18" height="14" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="22"></line><path d="M12 8V4h-3a3 3 0 0 0 0 6h6a3 3 0 0 0 0-6h-3v4"></path></svg>
            הטבות
        </div>
        <div class="nav-item active" id="nav-home" onclick="switchView('home')">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            בית
        </div>
    </div>

</div>
</div>

<script>
    function switchView(viewName) {
        // הסתרת כל המסכים
        var views = document.querySelectorAll('.view-container');
        for (var i = 0; i < views.length; i++) {
            views[i].classList.remove('active-view');
        }
        // הצגת המסך הנבחר
        document.getElementById('view-' + viewName).classList.add('active-view');

        // עדכון כפתורי הניווט
        var navItems = document.querySelectorAll('.nav-item');
        for (var j = 0; j < navItems.length; j++) {
            navItems[j].classList.remove('active');
        }
        document.getElementById('nav-' + viewName).classList.add('active');
    }

    // מעבר חלק מספלאש לאפליקציה
    setTimeout(function () {
        var splash = document.getElementById('splash');
        var app = document.getElementById('app');
        splash.classList.add('hidden');
        app.classList.add('visible');
        setTimeout(function () {
            splash.style.display = 'none';
        }, 400);
    }, 1500);
</script>

</body>
</html>
""", height=840, scrolling=False)
