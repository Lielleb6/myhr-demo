import streamlit as st
import time

# הגדרות תצוגה עליונות
st.set_page_config(page_title="MyHR+ App", layout="centered", initial_sidebar_state="collapsed")

# ניהול מצב (טעינה וחלוניות)
if 'app_loaded' not in st.session_state:
    st.session_state.app_loaded = False
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = False

# ==========================================
# 1. עיצוב CSS - מראה מקצועי ותאגידי
# ==========================================
css = """
<style>
/* איפוס הגדרות לתחושת אפליקציה מוחלטת */
.stApp { direction: rtl; background-color: #f4f5f8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; overscroll-behavior-y: none; user-select: none; }
::-webkit-scrollbar { display: none; }
#MainMenu, header, footer { display: none !important; }
.block-container { padding: 0 !important; max-width: 480px; margin: auto; padding-bottom: 90px !important; }

/* מסך הטעינה */
.splash-container {
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: linear-gradient(135deg, #003366 0%, #004080 100%);
    display: flex; flex-direction: column; justify-content: center; align-items: center; z-index: 999999;
}
.pulse-title { color: white; font-size: 45px; font-weight: 800; animation: pulse 1.5s infinite ease-in-out; }
.pulse-subtitle { color: #b3d4ff; font-size: 14px; margin-top: 8px; animation: pulse 1.5s infinite ease-in-out; animation-delay: 0.2s; }
@keyframes pulse { 0% { transform: scale(0.95); opacity: 0.8; } 50% { transform: scale(1.02); opacity: 1; } 100% { transform: scale(0.95); opacity: 0.8; } }

/* חלונית קופצת (Modal) */
.modal-overlay { background-color: #fff3cd; border: 1px solid #ffeeba; border-radius: 12px; padding: 20px; margin: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }

/* עיצוב כרטיסיות מקצועי */
div[data-testid="stHorizontalBlock"] {
    background-color: white; border-radius: 12px; padding: 18px 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03); border: 1px solid #eaeaea; margin: 0 15px 12px 15px;
    align-items: center; gap: 0 !important;
}
div[data-testid="column"]:nth-child(1) { flex: 1; }
div[data-testid="column"]:nth-child(2) { width: 70px !important; flex: none !important; display: flex; justify-content: flex-end; }

/* עיצוב הכפתורים כאייקונים חלקים */
div[data-testid="column"]:nth-child(2) button {
    width: 54px; height: 54px; border-radius: 50%; background-color: transparent; border: none;
    display: flex; align-items: center; justify-content: center; transition: 0.2s;
}
div[data-testid="column"]:nth-child(2) button:active { transform: scale(0.95); }

/* הסתרת טקסט ברירת המחדל של כפתורי האייקונים (כדי להכניס SVG במקום) */
div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="column"]:nth-child(2) button p,
div[data-testid="stHorizontalBlock"]:nth-of-type(3) div[data-testid="column"]:nth-child(2) button p { display: none; }

/* 1. גרף חופשה עגול */
div[data-testid="stHorizontalBlock"]:nth-of-type(1) div[data-testid="column"]:nth-child(2) button {
    border: 4px solid #f0f0f0; border-top-color: #10b981; border-right-color: #10b981;
    color: #111; font-weight: 800; font-size: 15px; background: white;
}

/* 2. אייקון סיבוס וקטורי מותאם אישית */
div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="column"]:nth-child(2) button {
    background-color: #f0f9ff;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230284c7' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2'%3E%3C/path%3E%3Cpath d='M7 2v20'%3E%3C/path%3E%3Cpath d='M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7'%3E%3C/path%3E%3C/svg%3E");
    background-size: 22px; background-repeat: no-repeat; background-position: center;
}

/* 3. אייקון שכר וקטורי */
div[data-testid="stHorizontalBlock"]:nth-of-type(3) div[data-testid="column"]:nth-child(2) button {
    background-color: #f8fafc; border: 1px solid #e2e8f0;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23475569' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'%3E%3C/line%3E%3Cline x1='12' y1='20' x2='12' y2='4'%3E%3C/line%3E%3Cline x1='6' y1='20' x2='6' y2='14'%3E%3C/line%3E%3C/svg%3E");
    background-size: 22px; background-repeat: no-repeat; background-position: center;
}

/* כפתור תלוש שכר אלגנטי */
div[data-testid="stHorizontalBlock"]:nth-of-type(3) div[data-testid="column"]:nth-child(1) button {
    background-color: transparent; border: 1px solid #004080; color: #004080; font-weight: 600; font-size: 13px;
    border-radius: 6px; margin-top: 12px; padding: 6px 0; min-height: 0; width: 85%;
}
div[data-testid="stHorizontalBlock"]:nth-of-type(3) div[data-testid="column"]:nth-child(1) button:active { background-color: #004080; color: white; }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ==========================================
# 2. לוגיקת טעינה (Splash Screen)
# ==========================================
if not st.session_state.app_loaded:
    st.markdown("""
<div class="splash-container">
    <div class="pulse-title">MyHR+</div>
    <div class="pulse-subtitle">מתחבר למערכות...</div>
</div>
""", unsafe_allow_html=True)
    time.sleep(2.2)
    st.session_state.app_loaded = True
    st.rerun()

# ==========================================
# 3. האפליקציה המרכזית (דשבורד)
# ==========================================
else:
    # אזור הכותרת (Header) - מותאם למקור
    st.markdown("""
<div style="background: linear-gradient(135deg, #003366 0%, #004080 100%); padding: 35px 20px 45px 20px; color: white; display: flex; justify-content: space-between; align-items: flex-start; border-radius: 0 0 20px 20px; box-shadow: 0 4px 12px rgba(0,51,102,0.1);">
    <div>
        <div style="font-size: 17px; font-weight: 700; display: flex; align-items: center; gap: 6px;">
            שלום, דניאל <span style="font-size: 13px; font-weight: 400; opacity: 0.85;">MyHR+</span>
        </div>
        <div style="font-size: 13px; color: #b3d4ff; margin-top: 5px; line-height: 1.4;">אלביט<br>אלביט מערכות - חטיבה אווירית</div>
    </div>
    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5" style="opacity:0.9;"><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></svg>
</div>

<div style="text-align: center; font-size: 16px; font-weight: 700; color: #111; margin: 25px 0 15px 0;">הדשבורד האישי שלי</div>
""", unsafe_allow_html=True)

    # חלונית קופצת (אם לחצו על כפתור)
    if st.session_state.show_modal:
        st.markdown("""
<div class="modal-overlay">
    <h3 style="color: #856404; margin: 0 0 10px 0; font-size: 18px;">🚧 בשלבי בנייה - דמו</h3>
    <p style="color: #856404; font-size: 14px; margin-bottom: 15px;">הנתונים יוצגו כאן במערכת המלאה.</p>
</div>
""", unsafe_allow_html=True)
        if st.button("סגור חלונית", use_container_width=True):
            st.session_state.show_modal = False
            st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)

    # --- כרטיסייה 1: חופשה ---
    col_t1, col_i1 = st.columns([3, 1])
    with col_t1:
        st.markdown("""
<div style="line-height: 1.2;">
    <div style="font-size: 13px; font-weight: 600; color: #555;">יתרת חופשה</div>
    <div style="font-size: 20px; font-weight: 800; color: #111; margin: 4px 0;">12 ימים</div>
    <div style="font-size: 11px; color: #888;">מתוך 20 ימים שנתיים</div>
</div>
""", unsafe_allow_html=True)
    with col_i1:
        if st.button("12", key="vac"): st.session_state.show_modal = True; st.rerun()

    # --- כרטיסייה 2: סיבוס ---
    col_t2, col_i2 = st.columns([3, 1])
    with col_t2:
        st.markdown("""
<div style="line-height: 1.2;">
    <div style="font-size: 13px; font-weight: 600; color: #555;">יתרת סיבוס (Cibus)</div>
    <div style="font-size: 20px; font-weight: 800; color: #111; margin: 4px 0;">₪450</div>
    <div style="font-size: 11px; color: #888;">היתרה לספטמבר</div>
</div>
""", unsafe_allow_html=True)
    with col_i2:
        if st.button("cibus", key="cib"): st.session_state.show_modal = True; st.rerun()

    # --- כרטיסייה 3: עדכון שכר ---
    col_t3, col_i3 = st.columns([3, 1])
    with col_t3:
        st.markdown("""
<div style="line-height: 1.2;">
    <div style="font-size: 13px; font-weight: 600; color: #555;">עדכון שכר</div>
    <div style="font-size: 11px; color: #888; margin-top: 4px;">עדכון שכר בהפצה האחרון</div>
</div>
""", unsafe_allow_html=True)
        if st.button("צפייה בתלוש האחרון", key="pay"): st.session_state.show_modal = True; st.rerun()
    with col_i3:
        if st.button("salary", key="sal"): st.session_state.show_modal = True; st.rerun()

    # ==========================================
    # 4. תפריט ניווט תחתון (Bottom Navigation)
    # ==========================================
    st.markdown("""
<div style="position: fixed; bottom: 0; left: 0; right: 0; background: white; display: flex; justify-content: space-around; padding: 12px 0 25px 0; box-shadow: 0 -4px 15px rgba(0,0,0,0.04); border-top: 1px solid #f0f0f0; z-index: 999;">
    <div style="text-align: center; color: #004080; font-weight: 700; font-size: 11px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:3px;"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg><br>בית
    </div>
    <div style="text-align: center; color: #94a3b8; font-weight: 600; font-size: 11px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:3px;"><rect x="3" y="8" width="18" height="14" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="22"></line><path d="M12 8V4h-3a3 3 0 0 0 0 6h6a3 3 0 0 0 0-6h-3v4"></path></svg><br>הטבות
    </div>
    <div style="text-align: center; color: #94a3b8; font-weight: 600; font-size: 11px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:3px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg><br>מסמכים
    </div>
    <div style="text-align: center; color: #94a3b8; font-weight: 600; font-size: 11px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:3px;"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg><br>פרופיל
    </div>
</div>
""", unsafe_allow_html=True)
