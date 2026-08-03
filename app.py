import streamlit as st

# 1. הגדרות תצוגה
st.set_page_config(page_title="MyHR+ Mobile", layout="centered", initial_sidebar_state="collapsed")

# 2. עיצוב CSS נקי למובייל - ללא מסגרות מזויפות, רק עיצוב מודרני לאפליקציה
st.markdown("""
<style>
    .stApp { direction: rtl; background-color: #f4f6f9; font-family: 'Segoe UI', Tahoma, sans-serif; }
    
    /* הסתרת תפריטי המערכת של Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* עיצוב החלק העליון (הכחול של אלביט) */
    .top-header {
        background: linear-gradient(135deg, #003366 0%, #004080 100%);
        padding: 25px 20px;
        border-radius: 15px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .top-header h2 { margin: 0; color: white; font-size: 24px; font-weight: 700; }
    .top-header p { margin: 5px 0 0 0; color: #b3d4ff; font-size: 14px; }
    
    /* עיצוב הכרטיסיות (הלבנות עם הצללית) */
    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #eaeaea;
        margin-bottom: 10px;
    }
    
    /* התראת ה-AI הקופצת (Pop-up) הזוהרת */
    .ai-alert {
        background-color: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 0 0 3px #00a3ff, 0 10px 25px rgba(0, 163, 255, 0.4);
        border: 1px solid #00a3ff;
        margin: 20px 0;
        text-align: right;
    }
    .ai-alert h4 { color: #003366; margin-top: 0; font-size: 18px; font-weight: bold; }
    .ai-alert p { color: #333; font-size: 16px; line-height: 1.5; }
    
    /* עיצוב כפתורים */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #005bb5;
        color: white;
        padding: 10px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #004080; }
</style>
""", unsafe_allow_html=True)

# 3. פאנל שליטה עליון להחלפה בין המסכים בדמו
col1, col2 = st.columns(2)
with col1:
    if st.button("📱 הצג דשבורד (דניאל)"): st.session_state.current = 'dash'
with col2:
    if st.button("⚠️ הצג התראה (מיכל)"): st.session_state.current = 'alert'

if 'current' not in st.session_state: st.session_state.current = 'dash'

# 4. התוכן עצמו (בנוי מרכיבים מקוריים כדי שזה יעבוד חלק)
if st.session_state.current == 'dash':
    
    st.markdown("""
    <div class="top-header">
        <h2>שלום, דניאל</h2>
        <p>אלביט מערכות - חטיבה אווירית</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### הדשבורד האישי שלי")
    
    # שימוש ב-Metrics של פייתון שמקבלים את העיצוב שיצרנו למעלה
    st.metric(label="🌴 יתרת חופשה", value="12 ימים", delta="מתוך 20 ימים שנתיים", delta_color="off")
    st.metric(label="🍽️ יתרת סיבוס (Cibus)", value="₪450", delta="היתרה לספטמבר", delta_color="off")
    
    with st.container():
        st.metric(label="📈 עדכון שכר", value="בוצע", delta="עדכון שכר בהפצה האחרון", delta_color="normal")
        st.button("צפייה בתלוש האחרון", key="tlush")

elif st.session_state.current == 'alert':
    
    st.markdown("""
    <div class="top-header">
        <h2>בוקר טוב, מיכל</h2>
        <p>אלביט מערכות - חטיבה אווירית</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="ai-alert">
        <h4>⚠️ התראה חשובה מ- MyHR+ AI</h4>
        <p><strong>מיכל</strong>, שמנו לב שעדיין לא ניצלת את סבסוד הלימודים השנתי שלך (עד ₪3,000)!<br><br>
        תוקף הזכאות פג בעוד 3 ימים (30.09.24).</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("למימוש הזכות עכשיו בלחיצה", type="primary", key="claim")
