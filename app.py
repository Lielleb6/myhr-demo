import streamlit as st
import pandas as pd
import numpy as np

# הגדרות עמוד - פריסה רחבה ואייקון (חייב להיות בשורה הראשונה)
st.set_page_config(page_title="MyHR+", layout="wide", page_icon="💼")

# עיצוב כותרת עליונה
st.markdown("<h1 style='text-align: center; color: #0c4a6e;'>MyHR+</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-top: -15px;'>מערכת חכמה לניהול משאבי אנוש ונוכחות</p>", unsafe_allow_html=True)
st.markdown("---")

# חלוקה ל-3 לשוניות
tab1, tab2, tab3 = st.tabs(["👤 אזור אישי (דניאל)", "🤖 התראות AI (מיכל)", "📊 ניהול נוכחות מחוזי"])

# ==========================================
# לשונית 1: אזור אישי לעובד (דניאל)
# ==========================================
with tab1:
    st.markdown("### 👋 שלום, דניאל")
    
    # תצוגת נתונים בשלוש עמודות
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="🌴 יתרת חופשה", value="12 ימים", delta="מתוך 20 בשנה", delta_color="off")
    with col2:
        st.metric(label="🤒 יתרת מחלה", value="8 ימים", delta="נוצלו 2 החודש", delta_color="inverse")
    with col3:
        st.metric(label="₪ תקציב רווחה", value="₪450", delta="לספטמבר", delta_color="off")
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**📈 עדכוני שכר והטבות (באלפי שקלים)**")
    
    # גרף אזור (Area Chart) יפה יותר מגרף עמודות פשוט
    chart_data = pd.DataFrame(
        np.array([[20, 25, 30, 28, 45, 60]]), 
        columns=['אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר']
    )
    st.area_chart(chart_data.T)
    
    # אזור נפתח לתלוש שכר
    with st.expander("📄 צפייה בתלוש האחרון"):
        st.info("תלוש ספטמבר מוכן לצפייה. המערכת מזהה אותך אוטומטית ולכן אין צורך בסיסמה נוספת.")

# ==========================================
# לשונית 2: התראות AI מותאמות אישית (מיכל)
# ==========================================
with tab2:
    st.markdown("### 🤖 בוקר טוב, מיכל")
    
    # הודעת אזהרה בולטת
    st.warning("⚠️ **התראת MyHR+ AI חשובה!**\n\nמיכל, שמנו לב שעדיין לא ניצלת את סבסוד הלימודים השנתי שלך (עד 3,000₪). תוקף הזכאות פג בעוד 3 ימים. אל תפספסי!")
    
    # כפתור פעולה אינטראקטיבי
    if st.button("⚡ למימוש הזכות עכשיו בלחיצה"):
        st.balloons() # אנימציה של בלונים
        st.success("הבקשה למימוש סבסוד הלימודים נפתחה והועברה לטיפול. חסכת לעצמך ולמחלקת כוח האדם התעסקות מיותרת בניירת!")

# ==========================================
# לשונית 3: לוח בקרה למנהלי משאבי אנוש / נוכחות
# ==========================================
with tab3:
    st.markdown("### 🏢 לוח בקרה - מחוז חיפה והצפון")
    st.caption("מבט כולל על נתוני נוכחות, דירוגים ודוחות (תצוגת מנהל מערכת)")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric(label="👥 סה״כ עובדים פעילים במחוז", value="524")
    with col_b:
        st.metric(label="⏳ דוחות נוכחות חסרים", value="18", delta="-5 משבוע שעבר", delta_color="normal")
    with col_c:
        st.metric(label="✅ דירוגים שאושרו", value="96%")

    st.markdown("---")
    st.write("**סטטוס הגשת דוחות נוכחות לפי אגפים (באחוזים):**")
    
    # גרף עמודות להצגת נתוני מחלקות
    progress_data = pd.DataFrame({
        'אגף': ['לשכת רווחה', 'מנהלה ותפעול', 'פיקוח שטח', 'כספים'],
        'אחוז הגשה': [98, 85, 92, 100]
    }).set_index('אגף')
    
    st.bar_chart(progress_data, color="#0c4a6e")
