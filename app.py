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
        --navy-deep:   #061a33;
        --navy:        #0a2e5c;
        --navy-light:  #144a8a;
        --ink:         #0f172a;
        --ink-soft:    #475569;
        --ink-faint:   #94a3b8;
        --paper:       #f8fafc;
        --card:        #ffffff;
        --emerald:     #0d9488;
        --emerald-tint:#ccfbf1;
        --line:        #e2e8f0;
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
            background: radial-gradient(120% 90% at 50% 0%, #144a8a 0%, #0a2e5c 50%, #061a33 100%);
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

    /* ---------- אשף התאמה אישית פרימיום (Onboarding) ---------- */
    #onboarding {
        position: absolute; inset: 0; z-index: 990; background: #ffffff;
        display: none; flex-direction: column; padding: 24px 20px; overflow-y: auto;
    }
    #onboarding.active { display: flex; }
    
    .onboarding-header { margin-bottom: 20px; text-align: right; }
    .onboarding-badge {
        display: inline-block; background: #e0f2fe; color: #0369a1; font-size: 11px;
        font-weight: 800; padding: 4px 10px; border-radius: 20px; margin-bottom: 8px; letter-spacing: 0.5px;
    }
    .onboarding-title { font-size: 24px; font-weight: 900; color: var(--navy-deep); letter-spacing: -0.5px; }
    .onboarding-sub { font-size: 13.5px; color: var(--ink-soft); margin-top: 4px; line-height: 1.5; }
    
    .pref-list { display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px; }
    .pref-item {
        background: #f8fafc; border: 1.5px solid var(--line); padding: 14px 16px;
        border-radius: 16px; display: flex; align-items: center; justify-content: space-between;
        cursor: pointer; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .pref-item:active { transform: scale(0.98); }
    .pref-item.selected { 
        border-color: var(--emerald); 
        background: var(--emerald-tint); 
        box-shadow: 0 4px 12px rgba(13, 148, 136, 0.1);
    }
    .pref-content { display: flex; align-items: center; gap: 12px; }
    .pref-icon {
        width: 36px; height: 36px; border-radius: 10px; background: #ffffff;
        display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .pref-label { font-weight: 800; font-size: 14px; color: var(--ink); }
    
    .pref-check {
        width: 22px; height: 22px; border-radius: 50%; border: 2px solid var(--ink-faint);
        display: flex; align-items: center; justify-content: center; transition: all 0.2s;
        font-size: 11px; color: transparent;
    }
    .pref-item.selected .pref-check { background: var(--emerald); border-color: var(--emerald); color: white; }

    .btn-primary {
        background: linear-gradient(135deg, var(--navy) 0%, var(--navy-deep) 100%);
        color: white; border: none; width: 100%; padding: 16px;
        border-radius: 16px; font-weight: 800; font-size: 15px; cursor: pointer; text-align: center;
        box-shadow: 0 10px 25px -5px rgba(10, 46, 92, 0.4); transition: transform 0.15s ease;
    }
    .btn-primary:active { transform: scale(0.98); }

    #app { height: 100%; display: flex; flex-direction: column; }

    /* ---------- Header ---------- */
    .header {
        position: relative; overflow: hidden; flex-shrink: 0;
        background: linear-gradient(160deg, var(--navy-light) 0%, var(--navy) 55%, var(--navy-deep) 100%);
        color: #fff; padding: 22px 18px 24px 18px;
        border-bottom-right-radius: 28px; border-bottom-left-radius: 28px;
        box-shadow: 0 10px 25px -5px rgba(6, 26, 51, 0.4);
    }
    .header-arcs { position: absolute; top: -40px; left: -60px; opacity: 0.12; pointer-events: none; }
    .header-row { display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 2; }
    
    .user-greeting { display: flex; align-items: flex-start; gap: 10px; }
    .avatar-badge {
        width: 42px; height: 42px; border-radius: 14px; flex-shrink: 0;
        background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3);
        display: flex; align-items: center; justify-content: center;
    }
    .greeting-name { font-size: 19px; font-weight: 800; letter-spacing: 0.2px; margin-bottom: 1px; }
    .greeting-org  { font-size: 13px; font-weight: 600; opacity: 0.92; }
    .greeting-unit { font-size: 11.5px; opacity: 0.7; font-weight: 500; }

    .brand-logo-badge {
        display: flex; align-items: center; gap: 12px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.22);
        padding: 10px 14px; border-radius: 18px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }
    .logo-graphic {
        width: 40px; height: 40px; background: linear-gradient(135deg, #0d9488 0%, #144a8a 100%);
        border-radius: 12px; display: flex; align-items: center; justify-content: center;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 4px 10px rgba(0,0,0,0.3);
        position: relative; flex-shrink: 0;
    }
    .logo-text-col { display: flex; flex-direction: column; text-align: left; }
    .brand-main-text {
        font-size: 26px; font-weight: 900; letter-spacing: 0.8px; line-height: 1; color: #ffffff;
    }
    .brand-main-text span { color: #5eead4; }
    .brand-tagline {
        font-size: 8.5px; font-weight: 700; color: #cbd5e1; letter-spacing: 0.8px; margin-top: 3px;
        text-transform: uppercase;
    }

    /* ---------- Views / Content ---------- */
    .view-container {
        flex: 1; overflow-y: auto; padding: 16px 16px 95px 16px; display: none;
        -webkit-overflow-scrolling: touch;
        overscroll-behavior-y: contain;
    }
    .view-container.active-view { display: block; }

    .eyebrow {
        font-size: 11.5px; font-weight: 700; color: var(--ink-faint);
        letter-spacing: 0.5px; margin: 4px 4px 4px 4px; text-transform: uppercase;
    }
    .section-title {
        color: var(--navy-deep); font-size: 19px; font-weight: 800; margin: 0 4px 14px 4px;
        display: flex; justify-content: space-between; align-items: center;
    }

    /* ---------- Cards & Widgets ---------- */
    .card {
        background: var(--card); border-radius: 20px; padding: 16px 18px;
        margin-bottom: 12px; border: 1px solid var(--line);
        box-shadow: 0 4px 20px -4px rgba(15, 23, 42, 0.05);
        display: flex; align-items: center; justify-content: space-between;
    }

    .card-label { font-size: 13.5px; font-weight: 700; color: var(--ink-soft); margin-bottom: 2px; }
    .card-value { font-size: 22px; font-weight: 900; color: var(--ink); line-height: 1.1; }
    .card-sub   { font-size: 12px; color: var(--ink-faint); margin-top: 3px; font-weight: 500; line-height: 1.4; }
    
    .icon-badge {
        width: 48px; height: 48px; border-radius: 14px; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center;
    }

    .pulse-alert-card {
        background: linear-gradient(135deg, #fef3c7 0%, #fffbeb 100%);
        border: 1px solid #fde68a; border-radius: 20px; padding: 14px 16px;
        margin-bottom: 12px; display: flex; align-items: center; gap: 12px;
        box-shadow: 0 4px 15px rgba(217, 119, 6, 0.08);
    }

    .simulator-card {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white; border-radius: 20px; padding: 18px; margin-bottom: 12px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.3);
    }
    .slider-container { margin-top: 12px; }
    .slider-container input { width: 100%; accent-color: #5eead4; cursor: pointer; }

    .ring-wrap { position: relative; width: 58px; height: 58px; border-radius: 50%; flex-shrink: 0; }
    .ring-center {
        position: absolute; inset: 5px; background: var(--card); border-radius: 50%;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
    }
    .ring-num { font-size: 16px; font-weight: 900; color: var(--ink); line-height: 1; }
    .ring-unit { font-size: 10px; color: var(--ink-faint); font-weight: 600; }

    .salary-card { flex-direction: column; align-items: stretch; padding: 16px 18px; }
    .salary-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }
    .bars { display: flex; align-items: flex-end; gap: 5px; height: 36px; }
    .bar { width: 7px; border-radius: 3px; background: #e2e8f0; }
    .bar.up { background: var(--emerald); position: relative; }
    .bar.up::after {
        content: "↑"; position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
        color: var(--emerald); font-size: 11px; font-weight: 800;
    }
    .cta-outline {
        width: 100%; text-align: center; border: 1.5px solid var(--navy); color: var(--navy);
        padding: 10px; border-radius: 12px; font-weight: 700; font-size: 13.5px;
        cursor: pointer; transition: background 0.15s ease;
    }
    .cta-outline:active { background: #f0f4f8; }

    /* ---------- כפתור צף לעוזרת חכמה (Mira AI) ---------- */
    .mira-fab {
        position: absolute; bottom: 85px; left: 16px; background: linear-gradient(135deg, #0d9488 0%, #144a8a 100%);
        color: white; width: 52px; height: 52px; border-radius: 50%;
        display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer;
        box-shadow: 0 6px 20px rgba(13, 148, 136, 0.4); z-index: 90; border: 2px solid rgba(255,255,255,0.4);
    }
    .mira-fab-text { font-size: 13px; font-weight: 900; letter-spacing: 0.5px; line-height: 1; }
    .mira-fab-sub { font-size: 8px; font-weight: 700; opacity: 0.9; text-transform: uppercase; margin-top: 1px; }

    /* מודאל צ'אט חי עם AI */
    .mira-modal {
        position: absolute; inset: 0; background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px);
        z-index: 200; display: none; align-items: flex-end;
    }
    .mira-modal.active { display: flex; }
    .mira-sheet {
        background: white; width: 100%; border-top-left-radius: 24px; border-top-right-radius: 24px;
        padding: 20px; max-height: 75vh; height: 75vh; display: flex; flex-direction: column;
    }
    .chat-history {
        flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; margin-bottom: 12px; padding-right: 4px;
    }
    .chat-bubble {
        padding: 12px 14px; border-radius: 14px; font-size: 13.5px; line-height: 1.4; max-width: 85%; word-break: break-word;
    }
    .chat-bubble.ai { background: #f1f5f9; color: var(--ink); align-self: flex-start; border-bottom-left-radius: 4px; }
    .chat-bubble.user { background: var(--navy); color: white; align-self: flex-end; border-bottom-right-radius: 4px; }

    .chat-input-row { display: flex; gap: 8px; align-items: center; border-top: 1px solid var(--line); padding-top: 12px; }
    .chat-input {
        flex: 1; background: #f8fafc; border: 1.5px solid var(--line); padding: 12px 14px;
        border-radius: 14px; font-size: 14px; outline: none; font-family: 'Assistant', sans-serif;
    }
    .chat-input:focus { border-color: var(--navy-light); background: white; }
    .chat-send-btn {
        background: var(--navy); color: white; border: none; width: 44px; height: 44px;
        border-radius: 14px; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }

    /* פרופיל עריכה */
    .profile-input-group { display: flex; flex-direction: column; gap: 4px; width: 100%; margin-bottom: 12px; }
    .profile-label { font-size: 12px; font-weight: 700; color: var(--ink-faint); }
    .profile-input {
        background: #f8fafc; border: 1.5px solid var(--line); padding: 10px 14px;
        border-radius: 12px; font-size: 14px; font-weight: 700; color: var(--ink); outline: none;
        font-family: 'Assistant', sans-serif; width: 100%; transition: border-color 0.2s;
    }
    .profile-input:focus { border-color: var(--navy-light); background: #ffffff; }

    /* ---------- Bottom Navigation ---------- */
    .bottom-nav {
        position: absolute; bottom: 0; left: 0; right: 0; max-width: 480px; margin: 0 auto;
        background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 10px 8px calc(14px + env(safe-area-inset-bottom, 6px)) 8px;
        display: flex; justify-content: space-around; align-items: center;
        border-top: 1px solid var(--line); box-shadow: 0 -10px 30px -10px rgba(15, 23, 42, 0.08);
        z-index: 100;
    }
    .nav-item {
        display: flex; flex-direction: column; align-items: center; gap: 2px;
        font-size: 11px; font-weight: 600; color: var(--ink-faint);
        cursor: pointer; padding: 6px 14px; border-radius: 12px;
        transition: all 0.15s ease;
    }
    .nav-item.active { color: var(--navy); font-weight: 800; background: #e0f2fe; }
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

    <!-- Onboarding: אשף בחירה אישי פרימיום -->
    <div id="onboarding">
        <div class="onboarding-header">
            <span class="onboarding-badge">Executive Workspace</span>
            <div class="onboarding-title">התאמת דשבורד אישי</div>
            <div class="onboarding-sub">בחר את המדדים וההטבות שתרצה לראות במוקד מסך הבית שלך לחוויית ניהול ממוקדת:</div>
        </div>
        
        <div class="pref-list">
            <div class="pref-item selected" onclick="togglePref(this, 'pulse')">
                <div class="pref-content">
                    <div class="pref-icon">⚡</div>
                    <span class="pref-label">פיד עדכונים חכמים (Pulse)</span>
                </div>
                <div class="pref-check">✓</div>
            </div>
            <div class="pref-item selected" onclick="togglePref(this, 'simulator')">
                <div class="pref-content">
                    <div class="pref-icon">🔮</div>
                    <span class="pref-label">סימולטור צמיחה עתידית</span>
                </div>
                <div class="pref-check">✓</div>
            </div>
            <div class="pref-item selected" onclick="togglePref(this, 'vacation')">
                <div class="pref-content">
                    <div class="pref-icon">🌴</div>
                    <span class="pref-label">יתרת חופשה שנתית</span>
                </div>
                <div class="pref-check">✓</div>
            </div>
            <div class="pref-item selected" onclick="togglePref(this, 'cibus')">
                <div class="pref-content">
                    <div class="pref-icon">🍽️</div>
                    <span class="pref-label">תקציב אוכל (סיבוס)</span>
                </div>
                <div class="pref-check">✓</div>
            </div>
            <div class="pref-item selected" onclick="togglePref(this, 'salary')">
                <div class="pref-content">
                    <div class="pref-icon">📈</div>
                    <span class="pref-label">עדכון שכר ותלושים</span>
                </div>
                <div class="pref-check">✓</div>
            </div>
        </div>

        <button class="btn-primary" onclick="savePreferences()">כניסה לדשבורד האישי</button>
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
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    </div>
                    <div style="text-align: right;">
                        <div class="greeting-name" id="header-name">שלום, דניאל</div>
                        <div class="greeting-org" id="header-org">אלביט מערכות</div>
                        <div class="greeting-unit" id="header-unit">חטיבה אווירית</div>
                    </div>
                </div>
                
                <div class="brand-logo-badge" dir="ltr">
                    <div class="logo-graphic">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#5eead4" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
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

        <!-- VIEW 1: HOME -->
        <div id="view-home" class="view-container active-view">
            <div class="eyebrow">סקירה כללית</div>
            <div class="section-title">
                <span>הדשבורד האישי שלי</span>
                <span style="font-size: 11.5px; color: var(--navy-light); cursor: pointer; font-weight: 700;" onclick="resetOnboarding()">שינוי העדפות ⚙️</span>
            </div>

            <div id="home-cards-container"></div>
        </div>

        <!-- VIEW 2: BENEFITS -->
        <div id="view-benefits" class="view-container">
            <div class="eyebrow">רווחה ותנאים</div>
            <div class="section-title"><span>ההטבות והתנאים שלך</span></div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">מניות ואופציות</div>
                    <div class="card-value" style="font-size: 20px; color: var(--emerald);">1,500 יחידות</div>
                    <div class="card-sub">חלק מהרווחים ושותפות עתידית בחברה</div>
                </div>
                <div class="icon-badge" style="background: var(--emerald-tint);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--emerald)" stroke-width="1.8"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>
                </div>
            </div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">קרן השתלמות</div>
                    <div class="card-value" dir="rtl">₪42,100</div>
                    <div class="card-sub">הפקדות מעסיק מוגדלות מהיום הראשון</div>
                </div>
                <div class="icon-badge" style="background: #e0f2fe;">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.8"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
            </div>
        </div>

        <!-- VIEW 3: DOCUMENTS -->
        <div id="view-documents" class="view-container">
            <div class="eyebrow">ארכיון דיגיטלי</div>
            <div class="section-title"><span>חוזים, תלושים ואישורים</span></div>

            <div class="card">
                <div style="text-align: right;">
                    <div class="card-label">חוזה עבודה אישי</div>
                    <div class="card-value" style="font-size: 17px; color: var(--emerald);">חתום ומאושר</div>
                    <div class="card-sub">גרסה מעודכנת</div>
                </div>
                <div class="icon-badge" style="background: #e0f2fe;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.8"><path d="M12 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                </div>
            </div>
        </div>

        <!-- VIEW 4: PROFILE -->
        <div id="view-profile" class="view-container">
            <div class="eyebrow">פרטים אישיים והגדרות</div>
            <div class="section-title"><span>כרטיס עובד וניהול פרופיל</span></div>

            <div class="card" style="flex-direction: column; align-items: flex-start; gap: 12px; padding: 20px;">
                <div class="profile-input-group">
                    <span class="profile-label">שם מלא:</span>
                    <input type="text" id="input-name" class="profile-input" value="דניאל" oninput="saveProfileData()">
                </div>
                <div class="profile-input-group">
                    <span class="profile-label">חברה מעסיקה:</span>
                    <input type="text" id="input-org" class="profile-input" value="אלביט מערכות" oninput="saveProfileData()">
                </div>
                <div class="profile-input-group">
                    <span class="profile-label">חטיבה / מחלקה:</span>
                    <input type="text" id="input-unit" class="profile-input" value="חטיבה אווירית" oninput="saveProfileData()">
                </div>
                <div class="profile-input-group">
                    <span class="profile-label">מספר עובד:</span>
                    <input type="text" id="input-id" class="profile-input" value="EL-88492" oninput="saveProfileData()">
                </div>
                <div style="width: 100%; display: flex; justify-content: space-between; align-items: center; margin-top: 4px; padding-top: 10px; border-top: 1px solid var(--line);">
                    <span style="color: var(--ink-faint); font-weight: 600; font-size: 13px;">סטטוס העסקה:</span>
                    <span style="font-weight: 800; color: var(--emerald); font-size: 13.5px;">עובד קבוע (תקף)</span>
                </div>
            </div>
        </div>

        <!-- כפתור צף לעוזרת חכמה (Mira AI) -->
        <div class="mira-fab" onclick="toggleMira(true)" title="Mira AI">
            <div class="mira-fab-text">AI</div>
            <div class="mira-fab-sub">Mira</div>
        </div>

        <!-- מודאל צ'אט חי עם AI -->
        <div class="mira-modal" id="mira-modal">
            <div class="mira-sheet">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <div style="font-weight: 900; font-size: 18px; color: var(--navy-deep);">Mira AI • עוזרת HR חכמה</div>
                    <div style="cursor: pointer; font-weight: 700; color: var(--ink-faint); font-size: 18px;" onclick="toggleMira(false)">✕</div>
                </div>
                
                <div class="chat-history" id="chat-history">
                    <div class="chat-bubble ai">היי! אני מירה, העוזרת החכמה שלך. אפשר לשאול אותי כל שעה על ימי חופשה, שכר, תנאים או נהלי חברה ואענה לך מיד!</div>
                </div>

                <div class="chat-input-row">
                    <input type="text" id="chat-input-field" class="chat-input" placeholder="הקלד שאלה למירה..." onkeypress="handleChatKey(event)">
                    <button class="chat-send-btn" onclick="sendChatMessage()">שלח</button>
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

    function saveProfileData() {
        var name = document.getElementById('input-name').value;
        var org = document.getElementById('input-org').value;
        var unit = document.getElementById('input-unit').value;
        var id = document.getElementById('input-id').value;

        var profile = { name: name, org: org, unit: unit, id: id };
        localStorage.setItem('myhr_profile', JSON.stringify(profile));
        updateHeaderDisplay();
    }

    function loadProfileData() {
        var saved = localStorage.getItem('myhr_profile');
        if (saved) {
            var profile = JSON.parse(saved);
            if (document.getElementById('input-name')) document.getElementById('input-name').value = profile.name || 'דניאל';
            if (document.getElementById('input-org')) document.getElementById('input-org').value = profile.org || 'אלביט מערכות';
            if (document.getElementById('input-unit')) document.getElementById('input-unit').value = profile.unit || 'חטיבה אווירית';
            if (document.getElementById('input-id')) document.getElementById('input-id').value = profile.id || 'EL-88492';
        }
        updateHeaderDisplay();
    }

    function updateHeaderDisplay() {
        var saved = localStorage.getItem('myhr_profile');
        var name = 'דניאל', org = 'אלביט מערכות', unit = 'חטיבה אווירית';
        if (saved) {
            var profile = JSON.parse(saved);
            name = profile.name || name;
            org = profile.org || org;
            unit = profile.unit || unit;
        }
        var nameEl = document.getElementById('header-name');
        var orgEl = document.getElementById('header-org');
        var unitEl = document.getElementById('header-unit');
        if (nameEl) nameEl.innerText = 'שלום, ' + name;
        if (orgEl) orgEl.innerText = org;
        if (unitEl) unitEl.innerText = unit;
    }

    function toggleMira(show) {
        var modal = document.getElementById('mira-modal');
        if (show) {
            modal.classList.add('active');
        } else {
            modal.classList.remove('active');
        }
    }

    function handleChatKey(e) {
        if (e.key === 'Enter') {
            sendChatMessage();
        }
    }

    function sendChatMessage() {
        var inputField = document.getElementById('chat-input-field');
        var text = inputField.value.trim();
        if (!text) return;

        var history = document.getElementById('chat-history');
        history.innerHTML += '<div class="chat-bubble user">' + text + '</div>';
        inputField.value = '';
        history.scrollTop = history.scrollHeight;

        setTimeout(function() {
            var reply = "בדקתי עבורך במערכות החברה. בהתאם לנתוני הפרופיל והזכויות שלך, הנושא מטופל מול מחלקת משאבי אנוש ומופיע באזור האישי.";
            
            var lower = text.toLowerCase();
            if (lower.includes('חופש') || lower.includes('ימים')) {
                reply = "יש לך כרגע 12 ימי חופשה צבורים פנויים לניצול עד סוף השנה האזרחית הנוכחית.";
            } else if (lower.includes('שכר') || lower.includes('תלוש')) {
                reply = "תלוש השכר האחרון שלך הופק והועבר לארכיון הדיגיטלי תחת לשונית 'מסמכים'.";
            } else if (lower.includes('קרן') || lower.includes('השתלמות')) {
                reply = "קרן ההשתלמות שלך פעילה ומופקדות אליה ההפרשות המקסימליות מדי חודש (היתרה הנוכחית עומדת על כ-₪42,100).";
            } else if (lower.includes('סיבוס') || lower.includes('אוכל')) {
                reply = "תקציב הסיבוס שלך מעודכן בסך 90 ש\"ח ליום עבודה. היתרה החודשית זמינה בדשבורד הבית.";
            }

            history.innerHTML += '<div class="chat-bubble ai">' + reply + '</div>';
            history.scrollTop = history.scrollHeight;
        }, 600);
    }

    function updateSimulator(val) {
        var baseStocks = 1500;
        var baseEdu = 42100;
        var multiplier = parseInt(val);
        
        var calculatedStocks = baseStocks + (multiplier * 350);
        var calculatedEdu = baseEdu + (multiplier * 12500);

        var sEl = document.getElementById('sim-stocks');
        var eEl = document.getElementById('sim-edu');
        if (sEl) sEl.innerText = calculatedStocks + ' יחידות';
        if (eEl) eEl.innerText = '₪' + calculatedEdu.toLocaleString();
    }

    function buildDynamicDashboard() {
        var container = document.getElementById('home-cards-container');
        if (!container) return;
        container.innerHTML = '';
        
        var saved = localStorage.getItem('myhr_prefs');
        var prefs = saved ? JSON.parse(saved) : ['pulse', 'simulator', 'vacation', 'cibus', 'salary'];

        var cardsHtml = {
            pulse: `
                <div class="pulse-alert-card">
                    <div style="font-size: 26px;">⚡</div>
                    <div style="text-align: right; flex: 1;">
                        <div style="font-size: 13px; font-weight: 800; color: #b45309;">עדכון חכם להיום</div>
                        <div style="font-size: 12px; color: var(--ink-soft); margin-top: 1px;">נותרו לך עוד 3 ימים לנצל את תקציב הסיבוס החודשי. נופש החטיבה באילת עוד 14 יום!</div>
                    </div>
                </div>
            `,
            simulator: `
                <div class="simulator-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 14px; font-weight: 800; color: #5eead4;">🔮 סימולטור צמיחה עתידית</span>
                        <span style="font-size: 11px; opacity: 0.7;" id="sim-years">הזז לשנים קדימה</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-top: 12px;">
                        <div style="text-align: right;">
                            <div style="font-size: 11px; opacity: 0.7;">מניות צפויות:</div>
                            <div style="font-size: 16px; font-weight: 900;" id="sim-stocks">1,500 יחידות</div>
                        </div>
                        <div style="text-align: right;">
                            <div style="font-size: 11px; opacity: 0.7;">קרן השתלמות:</div>
                            <div style="font-size: 16px; font-weight: 900;" id="sim-edu">₪42,100</div>
                        </div>
                    </div>
                    <div class="slider-container">
                        <input type="range" min="1" max="5" value="1" oninput="updateSimulator(this.value)">
                    </div>
                </div>
            `,
            vacation: `
                <div class="card">
                    <div style="text-align: right;">
                        <div class="card-label">יתרת חופשה</div>
                        <div class="card-value">12 ימים</div>
                        <div class="card-sub">מתוך 20 ימים שנתיים</div>
                    </div>
                    <div class="ring-wrap" style="background: conic-gradient(var(--emerald) 0% 60%, #e2e8f0 60% 100%);">
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
                        <div class="card-sub" style="max-width: 170px;">היתרה לספטמבר. כל יום זכאי ל-90 ש"ח</div>
                    </div>
                    <div class="icon-badge" style="background: #e0f2fe;">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="1.8"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/></svg>
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
        var target = document.getElementById('view-' + viewName);
        if (target) target.classList.add('active-view');

        var navItems = document.querySelectorAll('.nav-item');
        for (var j = 0; j < navItems.length; j++) {
            navItems[j].classList.remove('active');
        }
        var navTarget = document.getElementById('nav-' + viewName);
        if (navTarget) navTarget.classList.add('active');
    }

    // הפעלה מיידית של אתחול המערכת בלי לחכות ל-window.onload
    loadProfileData();
    if (!localStorage.getItem('myhr_prefs')) {
        var onboardingEl = document.getElementById('onboarding');
        if (onboardingEl) onboardingEl.classList.add('active');
    } else {
        buildDynamicDashboard();
    }
</script>

</body>
</html>
""", height=880, scrolling=False)
