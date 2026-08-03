import streamlit as st

# הגדרות תצוגה
st.set_page_config(page_title="MyHR+ Mobile", layout="centered", initial_sidebar_state="collapsed")

# שמירת מצב הלחיצה (בשביל החלונית הקופצת)
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = False

# ==========================================
# 1. עיצוב CSS - מיושר שמאלה למניעת שגיאות
# ==========================================
css = """
<style>
.stApp { direction: rtl; background-color: #f4f6f9; font-family: 'Segoe UI', Tahoma, sans-serif; }
#MainMenu, header, footer {visibility: hidden;}
.block-container { padding-top: 0rem; max-width: 480px; margin: auto; }

/* עיצוב הכרטיסיות הלבנות */
div[data-testid="stHorizontalBlock"] {
    background-color: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    border: 1px solid #eaeaea;
    margin-bottom: 15px;
    align-items: center;
}

/* מיקוד ויישור הטקסט והאייקונים בעמודות */
div[data-testid="column"]:nth-child(1) { display: flex; flex-direction: column; justify-content: center; }
div[data-testid="column"]:nth-child(2) { display: flex; align-items: center; justify-content: center; }

/* ========================================= */
/* העיצוב שהופך כפתור רגיל לאייקון עגול ויפה */
/* ========================================= */
div[data-testid="column"]:nth-child(2) button {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: white;
    border: 2px solid #e0e0e0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.06);
    color: #003366;
    font-weight: 900;
    font-size: 16px;
    line-height: 1.2;
    transition: transform 0.2s, box-shadow 0.2s;
}
div[data-testid="column"]:nth-child(2) button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}

/* אייקון 1: חופשה (פס התקדמות ירוק) */
div[data-testid="stHorizontalBlock"]:nth-of-type(1) div[data-testid="column"]:nth-child(2) button {
    border-right-color: #10b981;
    border-top-color: #10b981;
    border-width: 4px;
    color: #000;
    font-size: 17px;
}

/* אייקון 2: סיבוס (רקע תכלת) */
div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="column"]:nth-child(2) button {
    background-color: #e0f2fe;
    border: none;
    font-size: 26px;
}

/* אייקון 3: שכר (רקע אפור בהיר) */
div[data-testid="stHorizontalBlock"]:nth-of-type(3) div[data-testid="column"]:nth-child(2) button {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    font-size: 26px;
}

/* כפתור "צפייה בתלוש" מתחת לטקסט */
div[data-testid="stHorizontalBlock"]:nth-of-type(3) div[data-testid="column"]:nth-child(1) button {
    background-color: transparent;
    border: 1.5px solid #004080;
    color: #004080;
    font-weight: bold;
    border-radius: 8px;
    margin-top: 15px;
    transition: 0.3s;
}
div[data-testid="stHorizontalBlock"]:nth-of-type(3) div[data-testid="column"]:nth-child(1) button:hover {
    background-color: #004080;
    color: white;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ==========================================
# 2. חלונית הפופ-אפ (מוצגת רק אם לחצו על אייקון)
# ==========================================
if st.session_state.show_modal:
    st.markdown("""
    <div style="background-color: #fff3cd; border: 1px solid #ffeeba; border-radius: 12px; padding: 25px; margin-top: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 8px 20px rgba(0,0,0,0.15);">
        <h3 style="color: #856404; margin-top: 0; font-size: 22px;">🚧 בשלבי בנייה - דמו</h3>
        <p style="color: #856404; font-size: 15px; margin-bottom: 20px;">חלונית זו תפתח ותציג את הנתונים המלאים במערכת האמיתית.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✖️ סגור חלונית", use_container_width=True, type="primary"):
        st.session_state.show_modal = False
        st.rerun()
    st.markdown("<hr style='margin: 10px 0 30px 0;'>", unsafe_allow_html=True)

# ==========================================
# 3. הכותרת העליונה (אלביט)
# ==========================================
html_header = """
<div style="background: linear-gradient(135deg, #003366 0%, #004080 100%); padding: 40px 20px 50px 20px; border-radius: 0 0 30px 30px; margin-top: -60px; margin-bottom: 25px; color: white; text-align: right; direction: rtl; box-shadow: 0 10px 20px rgba(0,51,102,0.15);">
    <h2 style="margin:0; font-size: 24px; font-weight: bold; color: white;">שלום, דניאל <span style="font-weight: normal; font-size: 16px; opacity: 0.8; margin-right: 5px;">MyHR+</span></h2>
    <p style="margin: 8px 0 0 0; font-size: 14px; color: #b3d4ff; line-height: 1.4;">אלביט<br>אלביט מערכות - חטיבה אווירית</p>
</div>
<div style="text-align: center; font-size: 18px; font-weight: bold; color: #003366; margin: -50px auto 25px auto; background: white; padding: 15px 30px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); width: 85%;">
    הדשבורד האישי שלי
</div>
"""
st.markdown(html_header, unsafe_allow_html=True)

# ==========================================
# 4. יצירת הכרטיסיות
# ==========================================

# כרטיסייה 1: חופשה
c1_txt, c1_icn = st.columns([3, 1])
with c1_txt:
    st.markdown("""<div style="text-align: right; line-height: 1.3;">
        <div style="font-size: 14px; font-weight: bold; color: #333;">יתרת חופשה</div>
        <div style="font-size: 24px; font-weight: 900; color: #000; margin: 5px 0;">12 ימים</div>
        <div style="font-size: 12px; color: #666;">מתוך 20 ימים שנתיים</div>
    </div>""", unsafe_allow_html=True)
with c1_icn:
    # האייקון הוא בעצם כפתור! הפעלת הפופ-אפ בלחיצה.
    if st.button("12\nימים", key="btn_vac"):
        st.session_state.show_modal = True
        st.rerun()

# כרטיסייה 2: סיבוס
c2_txt, c2_icn = st.columns([3, 1])
with c2_txt:
    st.markdown("""<div style="text-align: right; line-height: 1.3;">
        <div style="font-size: 14px; font-weight: bold; color: #333;">יתרת סיבוס (Cibus)</div>
        <div style="font-size: 24px; font-weight: 900; color: #000; margin: 5px 0;">₪450</div>
        <div style="font-size: 12px; color: #666;">היתרה לספטמבר</div>
    </div>""", unsafe_allow_html=True)
with c2_icn:
    if st.button("🍽️", key="btn_cib"):
        st.session_state.show_modal = True
        st.rerun()

# כרטיסייה 3: עדכון שכר
c3_txt, c3_icn = st.columns([3, 1])
with c3_txt:
    st.markdown("""<div style="text-align: right; line-height: 1.3;">
        <div style="font-size: 14px; font-weight: bold; color: #333;">עדכון שכר</div>
        <div style="font-size: 12px; color: #666; margin-top: 5px;">עדכון שכר בהפצת<br>האחרון</div>
    </div>""", unsafe_allow_html=True)
    # כפתור התלוש באותו צד של הטקסט
    if st.button("צפייה בתלוש האחרון", use_container_width=True, key="btn_pay"):
        st.session_state.show_modal = True
        st.rerun()
with c3_icn:
    if st.button("📊", key="btn_sal"):
        st.session_state.show_modal = True
        st.rerun()
