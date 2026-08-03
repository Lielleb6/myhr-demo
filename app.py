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
        body {overflow: hidden; background-color: #082a4d;}
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
    * { 
        box-sizing: border-box; 
        -webkit-user-select: none;
        user-select: none;
        -webkit-touch-callout: none;
    }
    
    body {
        margin: 0; padding: 0; background: var(--paper);
        font-family: 'Assistant', sans-serif; overflow: hidden; color: var(--ink);
        -webkit-tap-highlight-color: transparent;
        overscroll-behavior-y: none;
    }

    #desktop-view-warning { display: none; }

    @media (min-width: 768px) {
        #app-wrapper { display: none !important; }
        #desktop-view-warning {
            display: flex !important;
            position: fixed; inset: 0;
            background: radial-gradient(120% 90% at 50% 0%, #1a5691 0%, #0d3f6e 50%, #082a4d 100%);
            color: white; flex-direction: column; justify-content: center; align-items: center;
            text-align: center; padding: 30px; font-family: 'Assistant', sans-serif;
            z-index: 999999;
        }
    }

    .shell {
        width: 100vw; height: 100vh; max-width: 480px; margin: 0 auto;
        background: var(--paper); display: flex; flex-direction: column; position: relative;
        overflow: hidden;
        overscroll-behavior: none;
    }

    @keyframes pulse {
        0% { transform: scale(0.96); opacity: 0.75; }
        50% { transform: scale(1.03); opacity: 1; }
        100% { transform: scale(0.96); opacity: 0.75; }
    }
    .pulse-text { animation: pulse 1.6s infinite ease-in-out; }
    .pulse-sub  { animation: pulse 1.6s infinite ease-in-out; animation-delay: 0.2s; }

    #splash {
        position: absolute; inset: 0; z-index: 999;
        background: radial-gradient(120% 90% at 50% 0%, var(--navy-light) 0%, var(--navy) 45%, var(--navy-deep) 100%);
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        transition: opacity 0.4s ease-out, visibility 0.4s;
    }
    #splash.hidden { opacity: 0; visibility: hidden; pointer-events: none; }

    /* ---------- אשף התאמה אישית (Onboarding) ---------- */
    #onboarding {
        position: absolute; inset: 0; z-index: 990; background: var(--paper);
        display: none; flex-direction: column; padding: 20px; overflow-y: auto;
    }
    #onboarding.active { display: flex; }
    
    .onboarding-title { font-size: 22px; font-weight: 900; color: var(--navy-deep); margin-bottom: 6px; }
    .onboarding-sub { font-size: 13.5px; color: var(--ink-soft); margin-bottom: 16px; line-height: 1.4; }
    
    .pref-item {
        background: var(--card); border: 2px solid var(--line); padding: 12px 14px;
        border-radius: 14px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;
        cursor: pointer; transition: all 0.2s;
    }
    .pref-item.selected { border-color: var(--emerald); background: var(--emerald-tint); }
    .pref-label { font-weight: 700; font-size: 14px; color: var(--ink); }
    .pref-check { width: 20px; height: 20px; border-radius: 6px; border: 2px solid var(--ink-faint); display: flex; align-items: center; justify-content: center; }
    .pref-item.selected .pref-check { background: var(--emerald); border-color: var(--emerald); color: white; }

    .btn-primary {
        background: var(--navy); color: white; border: none; width: 100%; padding: 14px;
        border-radius: 14px; font-weight: 800; font-size: 16px; cursor: pointer; text-align: center;
        margin-top: 10px; box-shadow: 0 4px 12px rgba(13,63,110,0.3);
    }
    .btn-primary:active { transform: scale(0.98); }

    #app { opacity: 0; transition: opacity 0.4s ease-in; height: 100%; display: flex; flex-direction: column; }
    #app.visible { opacity: 1; }

    .header {
        position: relative; overflow: hidden; flex-shrink: 0;
        background: linear-gradient(160deg, var(--navy-light) 0%, var(--navy) 55%, var(--navy-deep) 100%);
        color: #fff; padding: 22px 18px 24px 18px;
        border-bottom-right-radius: 28px; border-bottom-left-radius: 28px;
        box-shadow: 0 8px 20px -6px rgba(6, 30, 58, 0.35);
    }
    .header-arcs { position: absolute; top: -40px; left: -60px; opacity: 0.14; pointer-events: none; }
    .header-row { display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 2; }
    
    .user-greeting { display: flex; align-items: flex-start; gap: 10px; }
    .avatar-badge {
        width: 40px; height: 40px; border-radius: 12px; flex-shrink: 0;
        background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.24);
        display: flex; align-items: center; justify-content: center;
    }
    .greeting-name { font-size: 19px; font-weight: 800; letter-spacing: 0.2px; margin-bottom: 1px; }
    .greeting-org  { font-size: 13px; font-weight: 600; opacity: 0.92; }
    .greeting-unit { font-size: 11.5px; opacity: 0.7; font-weight: 500; }

    .brand-logo-badge {
        display: flex; align-items: center; gap: 12px;
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 10px 14px; border-radius: 18px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .logo-graphic {
        width: 42px; height: 42px; background: linear-gradient(135deg, #2ecc71 0%, #1a5691 100%);
        border-radius: 12px; display: flex; align-items: center; justify-content: center;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 4px 10px rgba(0,0,0,0.3);
        position: relative; flex-shrink: 0;
    }
    .logo-text-col { display: flex; flex-direction: column; text-align: left; }
    .brand-main-text {
        font-size: 28px; font-weight: 900; letter-spacing: 0.8px; line-height: 1; color: #ffffff;
    }
    .brand-main-text span { color: #6fd9b5; }
    .brand-tagline {
        font-size: 9.5px; font-weight: 700; color: #b9d3ec; letter-spacing: 0.6px; margin-top: 3px;
        text-transform: uppercase;
    }

    .view-container {
        flex: 1; overflow-y: auto; padding: 16px 16px 95px 16px; display: none;
        -webkit-overflow-scrolling: touch;
        overscroll-behavior-y: contain;
    }
    .view-container.active-view { display: block; }

    .eyebrow {
        font-size: 12px; font-weight: 700; color: var(--ink-faint);
        letter-spacing: 0.3px; margin: 4px 4px 4px 4px;
    }
    .section-title {
        color: var(--navy-deep); font-size: 20px; font-weight: 800; margin: 0 4px 14px 4px;
        display: flex; justify-content: space-between; align-items: center;
    }

    .card {
        background: var(--card); border-radius: 18px; padding: 16px 18px;
        margin-bottom: 12px; border: 1px solid var(--line);
        box-shadow: 0 2px 4px rgba(16,26,43,0.02), 0 10px 24px -12px rgba(16,26,43,0.1);
        display: flex; align-items: center; justify-content: space-between;
    }

    .card-label { font-size: 14px; font-weight: 700; color: var(--ink-soft); margin-bottom: 2px; }
    .card-value { font-size: 24px; font-weight: 900; color: var(--ink); line-height: 1.1; }
    .card-sub   { font-size: 12.5px; color: var(--ink-faint); margin-top: 2px; font-weight: 500; line-height: 1.4; }
    
    .icon-badge {
        width: 50px; height: 50px; border-radius: 14px; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center;
    }

    .ring-wrap { position: relative; width: 62px; height: 62px; border-radius: 50%; flex-shrink: 0; }
    .ring-center {
        position: absolute; inset: 5px; background: var(--card); border-radius: 50%;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
    }
    .ring-num { font-size: 18px; font-weight: 900; color: var(--ink); line-height: 1; }
    .ring-unit { font-size: 10.5px; color: var(--ink-faint); font-weight: 600; }

    .salary-card { flex-direction: column; align-items: stretch; padding: 16px 18px; }
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
        font-size: 11.5px; font-weight: 600; color: var(--ink-faint);
        cursor: pointer; padding: 6px 16px; border-radius: 12px;
        transition: all 0.15s ease;
    }
    .nav-item.active { color: var(--navy); font-weight: 800; background: var(--blue-tint); }
</style>
</head>
<body>

<div id="desktop-view-warning">
    <div style="font-size: 64px; margin-bottom: 20px;">📱</div>
    <div style="font-size: 28px; font-weight: 900; margin-bottom: 12px;">האפליקציה מיועדת למובייל בלבד</div>
    <div style="font-size: 16px; opacity: 0.85; max-width: 380px; line-height: 1.6;">
        מערכת MyHR+ מותאמת באופן בלעדי למכשירים סלולריים לחוויית עובד מושלמת. אנא פתח את הקישור מהטלפון הנייד שלך.
    </div>
</div>

<div id="app-wrapper" style="width: 100%; height: 100%; display: flex; justify-content: center;">
<div class="shell">

    <!-- Splash Screen -->
    <div id="splash">
        <div class="pulse-text" dir="ltr" style="color: white; font-size: 52px; font-weight: 900; letter-spacing: 1px;">MyHR<span style="color:#6fd9b5;">+</span></div>
        <div class="pulse-sub" style="color: #b9d3ec; font-size: 16px; margin-top: 10px; font-weight: 600;">מתחבר למערכות...</div>
    </div>

    <!-- Onboarding: בחירת מדדים לדשבורד האישי -->
    <div id="onboarding">
        <div style="margin-top: 10px;">
            <div class="onboarding-title">התאם אישית את הדשבורד שלך 🎯</div>
            <div class="onboarding-sub">בחר אילו נתונים והטבות תרצה שיוצגו מיד בדף הבית שלך:</div>
        </div>
        
        <div class="pref-item selected" onclick="togglePref(this, 'vacation')">
            <span class="pref-label">🌴 יתרת חופשה</span>
            <div class="pref-check">✓</div>
        </div>
        <div class="pref-item selected" onclick="togglePref(this, 'cibus')">
            <span class="pref-label">🍽️ תקציב אוכל (סיבוס)</span>
            <div class="pref-check">✓</div>
        </div>
        <div class="pref-item selected" onclick="togglePref(this, 'salary')">
            <span class="pref-label">📈 עדכון שכר ותלושים</span>
            <div class="pref-check">✓</div>
        </div>
        <div class="pref-item" onclick="togglePref(this, 'stocks')">
            <span class="pref-label">📈 מניות ואופציות</span>
            <div class="pref-check">✓</div>
        </div>
        <div class="pref-item" onclick="togglePref(this, 'education')">
            <span class="pref-label">💰 קרן השתלמות</span>
            <div class="pref-check">✓</div>
        </div>
        <div class="pref-item" onclick="togglePref(this, 'bonus')">
            <span class="pref-label">🎁 בונוס שנתי מובטח</span>
            <div class="pref-check">✓</div>
        </div>
        <div class="pref-item" onclick="togglePref(this, 'hybrid')">
            <span class="pref-label">🌿 עבודה היברידית</span>
            <div class="pref-check">✓</div>
        </div>

        <button class="btn-primary" onclick="savePreferences()">שמור והתחל לעבוד</button>
    </div>

    <!-- Main App -->
    <div id="app">

        <!-- Header -->
        <div class="header">
            <svg class="header-arcs" width="200" height="200" viewBox="0 0 220 220" fill="none">
                <circle cx="20" cy="20" r="40" stroke="white" stroke-width="1.4"/>
                <circle cx="20" cy="20" r="75" stroke="white" stroke-width="1.4"/>
                <circle cx="20" cy="20" r="110" stroke="white" stroke-width="1.4"/>
            </svg>
            <div class="header-row">
                <div class="user-greeting">
                    <div class="avatar-badge">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.7"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    </div>
                    <div style="text-align: right;">
                        <div class="greeting-name">שלום, דניאל</div>
                        <div class="greeting-org">אלביט מערכות</div>
                        <div class="greeting-unit">חטיבה אווירית</div>
                    </div>
                </div>
                
                <div class="brand-logo-badge" dir="ltr">
                    <div class="logo-graphic">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6fd9b5" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                            <rect x="9" y="8" width="6" height="10" rx="1"/>
                            <line x1="12" y1="15" x2="12" y2="15.01"/>
                        </svg>
                    </div>
                    <div class="logo-text-col">
                        <div class="brand-main-text">MyHR<span>+</span></div>
                        <div class="brand-tagline">Accessible • Precise • Comprehensive</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- VIEW 1: HOME (בית - דינמי לפי בחירת המשתמש) -->
        <div id="view-home" class="view-container active-view">
            <div class="eyebrow">סקירה כללית</div>
            <div class="section-title">
                <span>הדשבורד האישי שלי</span>
                <span style="font-size: 12px; color: var(--navy-light); cursor: pointer; text-decoration: underline;" onclick="resetOnboarding()">שינוי העדפות ⚙️</span>
            </div>

            <div id="home-cards-container">
                <!-- הכרטיסים יטענו דינמית לפי ההגדרות -->
            </div>
        </div>

        <!-- VIEW 2: BENEFITS (הטבות) -->
        <div id="view-benefits" class="view-container">
            <div class="eyebrow">רווחה ותנאים</div>
            <div class="section-title"><span>ההטבות והתנאים שלך</span></div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">מניות ואופציות</div>
                    <div class="card-value" style="font-size: 20px; color: var(--emerald);">1,500 יחידות</div>
                    <div class="card-sub">חלק מהרווחים ושותפות עתידית בחברה</div>
                </div>
                <div class="icon-badge" style="background: #e7f6ee;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="1.6"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">קרן השתלמות</div>
                    <div class="card-value" dir="rtl">₪42,100</div>
                    <div class="card-sub">הפקדות מעסיק מוגדלות מהיום הראשון</div>
                </div>
                <div class="icon-badge" style="background: var(--blue-tint);">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">בונוס שנתי מובטח</div>
                    <div class="card-value">עד 3 משכורות</div>
                    <div class="card-sub">על בסיס עמידה ביעדי החברה והאינדיבידואל</div>
                </div>
                <div class="icon-badge" style="background: #fbf1e0;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c98a2c" stroke-width="1.6"><path d="M20 12v10H4V12"/><path d="M2 7h20v5H2z"/><path d="M12 22V7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">תקציב אוכל (סיבוס)</div>
                    <div class="card-value" dir="rtl">₪1,980 / חודש</div>
                    <div class="card-sub">סבסוד יומי מלא לארוחות צהריים וחדר אוכל</div>
                </div>
                <div class="icon-badge" style="background: var(--blue-tint);">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">תווי קנייה ומתנות חג</div>
                    <div class="card-value" dir="rtl">₪3,500 / שנה</div>
                    <div class="card-sub">תווי קנייה בסכומים גבוהים בראש השנה ופסח</div>
                </div>
                <div class="icon-badge" style="background: #e7f6ee;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="1.6"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">נופש ואירועי חברה</div>
                    <div class="card-value" style="font-size: 19px; color: var(--emerald);">כלול במלואו</div>
                    <div class="card-sub">ימי כיף מרוכזים, הופעות וטיול שנתי חטיבתי</div>
                </div>
                <div class="icon-badge" style="background: var(--blue-tint);">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">עבודה היברידית</div>
                    <div class="card-value" style="font-size: 19px;">3 ימים מהמשרד</div>
                    <div class="card-sub">כולל תקציב חד-פעמי להקמת משרד ביתי נוח</div>
                </div>
                <div class="icon-badge" style="background: #fbf1e0;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c98a2c" stroke-width="1.6"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">ביטוח בריאות מורחב</div>
                    <div class="card-value" style="font-size: 19px; color: var(--emerald);">כיסוי משפחתי מלא</div>
                    <div class="card-sub">כולל רפואה פרטית, ניתוחים ובדיקות סקר</div>
                </div>
                <div class="icon-badge" style="background: var(--blue-tint);">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">ספורט ופנאי</div>
                    <div class="card-value" style="font-size: 19px;">מנוי פרימיום</div>
                    <div class="card-sub">מנוי למכון כושר רשתי והשתתפות בחוגים</div>
                </div>
                <div class="icon-badge" style="background: #e7f6ee;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
                </div>
            </div>

        </div>

        <!-- VIEW 3: DOCUMENTS (מסמכים) -->
        <div id="view-documents" class="view-container">
            <div class="eyebrow">ארכיון דיגיטלי</div>
            <div class="section-title"><span>חוזים, תלושים ואישורים</span></div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">חוזה עבודה אישי</div>
                    <div class="card-value" style="font-size: 17px; color: var(--emerald);">חתום ומאושר</div>
                    <div class="card-sub">גרסה מעודכנת - חטיבה אווירית</div>
                </div>
                <div class="icon-badge" style="background: var(--blue-tint);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M12 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">תלוש שכר - יולי 2026</div>
                    <div class="card-value" style="font-size: 17px;">חתום דיגיטלית</div>
                    <div class="card-sub">הופק ב-01/08/2026</div>
                </div>
                <div class="icon-badge" style="background: var(--blue-tint);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">אישור העסקה ושכר</div>
                    <div class="card-value" style="font-size: 17px;">מוכן להורדה</div>
                    <div class="card-sub">עבור בנק / משכנתא</div>
                </div>
                <div class="icon-badge" style="background: var(--blue-tint);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                </div>
            </div>
        </div>

        <!-- VIEW 4: PROFILE (פרופיל) -->
        <div id="view-profile" class="view-container">
            <div class="eyebrow">פרטים אישיים</div>
            <div class="section-title"><span>כרטיס עובד - אלביט מערכות</span></div>

            <div class="card" style="flex-direction: column; align-items: flex-start; gap: 8px;">
                <div style="display: flex; justify-content: space-between; width: 100%;">
                    <span style="color: var(--ink-faint); font-weight: 600;">שם מלא:</span>
                    <span style="font-weight: 800;">דניאל</span>
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
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                פרופיל
            </div>
            <div class="nav-item" id="nav-documents" onclick="switchView('documents')">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                מסמכים
            </div>
            <div class="nav-item" id="nav-benefits" onclick="switchView('benefits')">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="8" width="18" height="14" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="22"></line><path d="M12 8V4h-3a3 3 0 0 0 0 6h6a3 3 0 0 0 0-6h-3v4"></path></svg>
                הטבות
            </div>
            <div class="nav-item active" id="nav-home" onclick="switchView('home')">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                בית
            </div>
        </div>

    </div>

</div>
</div>

<script>
    function togglePref(el, key) {
        el.classList.toggle('selected');
    }

    function savePreferences() {
        var selectedItems = [];
        var items = document.querySelectorAll('.pref-item');
        items.forEach(function(item) {
            if (item.classList.contains('selected')) {
                // מציאת המפתח מתוך ה-onclick
                var onclickStr = item.getAttribute('onclick');
                var match = onclickStr.match(/'([^']+)'/);
                if (match && match[1]) {
                    selectedItems.push(match[1]);
                }
            }
        });
        localStorage.setItem('myhr_prefs', JSON.stringify(selectedItems));
        document.getElementById('onboarding').classList.remove('active');
        buildDynamicDashboard();
    }

    function resetOnboarding() {
        document.getElementById('onboarding').classList.add('active');
    }

    function buildDynamicDashboard() {
        var container = document.getElementById('home-cards-container');
        container.innerHTML = '';
        
        var saved = localStorage.getItem('myhr_prefs');
        var prefs = saved ? JSON.parse(saved) : ['vacation', 'cibus', 'salary'];

        // הגדרת כל כרטיסי הבית האפשריים
        var cardsHtml = {
            vacation: `
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
            `,
            cibus: `
                <div class="card">
                    <div style="text-align: right;">
                        <div class="card-label">יתרת סיבוס (Cibus)</div>
                        <div class="card-value" dir="rtl">₪450</div>
                        <div class="card-sub" style="max-width: 180px;">היתרה לספטמבר. כל יום זכאי ל-90 ש"ח</div>
                    </div>
                    <div class="icon-badge" style="background: var(--blue-tint);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/></svg>
                    </div>
                </div>
            `,
            salary: `
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
            `,
            stocks: `
                <div class="card">
                    <div style="text-align: right;">
                        <div class="card-label">מניות ואופציות</div>
                        <div class="card-value" style="font-size: 20px; color: var(--emerald);">1,500 יחידות</div>
                        <div class="card-sub">חלק מהרווחים ושותפות עתידית בחברה</div>
                    </div>
                    <div class="icon-badge" style="background: #e7f6ee;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="1.6"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>
                    </div>
                </div>
            `,
            education: `
                <div class="card">
                    <div style="text-align: right;">
                        <div class="card-label">קרן השתלמות</div>
                        <div class="card-value" dir="rtl">₪42,100</div>
                        <div class="card-sub">הפקדות מעסיק מוגדלות מהיום הראשון</div>
                    </div>
                    <div class="icon-badge" style="background: var(--blue-tint);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.6"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                    </div>
                </div>
            `,
            bonus: `
                <div class="card">
                    <div style="text-align: right;">
                        <div class="card-label">בונוס שנתי מובטח</div>
                        <div class="card-value">עד 3 משכורות</div>
                        <div class="card-sub">על בסיס עמידה ביעדי החברה והאינדיבידואל</div>
                    </div>
                    <div class="icon-badge" style="background: #fbf1e0;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c98a2c" stroke-width="1.6"><path d="M20 12v10H4V12"/><path d="M2 7h20v5H2z"/><path d="M12 22V7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>
                    </div>
                </div>
            `,
            hybrid: `
                <div class="card">
                    <div style="text-align: right;">
                        <div class="card-label">עבודה היברידית</div>
                        <div class="card-value" style="font-size: 19px;">3 ימים מהמשרד</div>
                        <div class="card-sub">כולל תקציב חד-פעמי להקמת משרד ביתי נוח</div>
                    </div>
                    <div class="icon-badge" style="background: #fbf1e0;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c98a2c" stroke-width="1.6"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                    </div>
                </div>
            `
        };

        prefs.forEach(function(key) {
            if (cardsHtml[key]) {
                container.innerHTML += cardsHtml[key];
            }
        });

        if (prefs.length === 0) {
            container.innerHTML = '<div style="text-align:center; color:var(--ink-faint); padding: 30px;">לא נבחרו פריטים לתצוגה. לחץ על "שינוי העדפות" למעלה.</div>';
        }
    }

    function switchView(viewName) {
        var views = document.querySelectorAll('.view-container');
        for (var i = 0; i < views.length; i++) {
            views[i].classList.remove('active-view');
        }
        document.getElementById('view-' + viewName).classList.add('active-view');

        var navItems = document.querySelectorAll('.nav-item');
        for (var j = 0; j < navItems.length; j++) {
            navItems[j].classList.remove('active');
        }
        document.getElementById('nav-' + viewName).classList.add('active');
    }

    // תזרים טעינה והצגת אשף אם זו פעם ראשונה
    setTimeout(function () {
        var splash = document.getElementById('splash');
        var app = document.getElementById('app');
        if (splash && app) {
            splash.classList.add('hidden');
            app.classList.add('visible');
            setTimeout(function () {
                splash.style.display = 'none';
                
                // בדיקה האם המשתמש כבר בחר העדפות בעבר
                if (!localStorage.getItem('myhr_prefs')) {
                    document.getElementById('onboarding').classList.add('active');
                } else {
                    buildDynamicDashboard();
                }
            }, 400);
        }
    }, 1500);
</script>

</body>
</html>
""", height=880, scrolling=False)
