import streamlit as st
import pandas as pd
import numpy as np

# 1. הגדרות תצוגה בסיסיות (חייב להיות בשורה הראשונה)
st.set_page_config(page_title="MyHR+ Mobile", layout="wide", initial_sidebar_state="collapsed")

# 2. הזרקת עיצוב מתקדם (CSS) להתאמה למובייל ולמראה מודרני (Shadow Cards)
st.markdown("""
<style>
    /* כיווניות לימין והגדרת גופן מודרני */
    .stApp {
        direction: rtl;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        background-color: #f4f6f9;
    }
    
    /* הסתרת התפריטים של Streamlit לתחושת אפליקציה נקייה */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* עיצוב כרטיסיות צפות (Cards) לנתונים */
    div.css-1r6slb0, div.css-12w0qpk, div.stMetric {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 10px;
    }
    
    /* עיצוב כותרות אישיות */
    h1, h2, h3 {
        color: #0f172a;
        font-weight: 700;
    }
    
    /* עיצוב כפתורים */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #0284c7;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 0;
        box-shadow: 0 4px 6px rgba(2, 132, 199, 0.2);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #0369a1;
        box-shadow: 0 6px 8px rgba(2, 132, 199, 0.3);
    }
    
    /* עיצוב לשוניות (Tabs) שיתאימו למגע בטלפון */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        justify-content: center;
        background-color: white;
        padding: 10px;
        border-radius: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 16px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 3. כותרת האפליקציה (Header)
st.markdown("<h2 style='text-align: center; color: #0284c7; margin-bottom: 0;'>📱 MyHR+</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #64748b; margin-top: -10px;'>מערכת חכמה לניהול משאבי אנוש ונוכחות</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; font-size: 12px; color: #475569; background-color: #e0f2fe; padding: 5px; border-radius: 20px; width: fit-content; margin: 0 auto 20px auto;'>משרד הרווחה והביטחון החברתי - מחוז חיפה והצפון</p>", unsafe_allow_html=True)

# 4. יצירת לשוניות ניווט מותאמות
tab_personal, tab_admin, tab_ai = st.tabs(["👤 אזור אישי", "🏢 ניהול נוכחות ודירוגים", "🤖 עוזר חכם"])

# ==========================================
# לשונית 1: אזור אישי לעובד (תצוגת כרטיסיות מובייל)
# ==========================================
with tab_personal:
    st.markdown("### 👋 בוקר טוב, ישראל")
    st.caption("תקציר נתונים אישיים לחודש נוכחי")
    
    # שימוש ב-Container כדי לייצר מראה של כרטיסיה נפרדת
    with st.container():
        st.metric(label="🌴 יתרת חופשה שנתית", value="14.5 ימים", delta="מתוך 22 ימים", delta_color="off")
    
    with st.container():
        st.metric(label="🤒 יתרת מחלה", value="42 ימים", delta="לא נוצלו ימי מחלה החודש", delta_color="normal")
        
    with st.container():
        st.metric(label="⏱️ שעות נוספות החודש", value="12.5 שעות", delta="אושר מראש: 15 שעות", delta_color="inverse")

    st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown("#### 📄 דוחות אחרונים")
    
    # תפריט נפתח (Accordion) מותאם למובייל
    with st.expander("📝 דוח נוכחות - אוקטובר"):
        st.success("הדוח הוגש ואושר על ידי המנהל הישיר.")
        st.button("הורד העתק PDF", key="btn_pdf1")
        
    with st.expander("💰 תלוש שכר - ספטמבר"):
        st.info("התלוש זמין לצפייה מאובטחת.")
        st.button("לצפייה בתלוש", key="btn_salary")

# ==========================================
# לשונית 2: לוח בקרה מחוזי (מיועד לניהול רחב)
# ==========================================
with tab_admin:
    st.markdown("### 📊 תמונת מצב - מנהל משאבי אנוש")
    st.caption("נתוני נוכחות בזמן אמת עבור 524 עובדי המחוז")
    
    # בכוונה משתמשים בעמודות שיהפכו לשורות במובייל
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="👥 סה״כ עובדים פעילים", value="524", delta="2 עובדים חדשים")
    with col2:
        st.metric(label="⏳ דוחות נוכחות חסרים", value="18", delta="חריגה מהיעד", delta_color="inverse")
        
    with st.container():
        st.metric(label="⭐ עדכוני דירוג שאושרו", value="94%", delta="היעד: 100% עד סוף החודש", delta_color="off")

    st.markdown("#### אישור שעות חריגות לפי יחידה")
    
    # גרף עמודות אופקי שייראה טוב גם במסך צר
    chart_data = pd.DataFrame({
        'יחידה': ['לשכות רווחה', 'מנהלה ותפעול', 'פיקוח שטח', 'כספים', 'אגף קהילה'],
        'שעות שאושרו': [120, 85, 210, 45, 90]
    }).set_index('יחידה')
    
    st.bar_chart(chart_data, color="#0ea5e9")
    
    st.markdown("#### טיפול אדמיניסטרטיבי דחוף")
    st.warning("שים לב: יש לאשר 5 בקשות חריגות לעדכון דירוגי שכר לפני סגירת החודש.")
    if st.button("פתח מערכת אישורים", key="btn_admin"):
        st.success("מערכת האישורים נפתחה. הודעה נשלחה למנהלי היחידות.")

# ==========================================
# לשונית 3: התראות AI וסיוע
# ==========================================
with tab_ai:
    st.markdown("### 🤖 העוזר החכם שלך")
    st.caption("התראות המבוססות על למידת מכונה לשיפור מיצוי זכויות ונוכחות")
    
    st.info("💡 **זיהוי חריגות בדיווח:**\n\nהמערכת זיהתה שבימי שלישי יש נטייה לחוסר דיווח שעון יציאה במחלקת פיקוח שטח. האם תרצה להגדיר תזכורת אוטומטית לנייד של עובדי המחלקה בשעה 16:00?")
    if st.button("הפעל תזכורת חכמה", key="btn_ai_1"):
        st.toast('תזכורת אוטומטית הוגדרה בהצלחה!', icon='✅')
        
    st.error("⚠️ **התראת מיצוי זכויות:**\n\nישנם 42 עובדים במחוז שטרם ניצלו את תקציב קצובת הביגוד השנתי. הזכאות פגה בעוד חודשיים.")
    if st.button("שלח קמפיין תזכורת מרוכז", key="btn_ai_2"):
        st.balloons()
        st.success("הודעות פוש (Push) נשלחו לכל 42 העובדים הרלוונטיים.")
