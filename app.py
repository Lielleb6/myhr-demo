import streamlit as st

# הגדרת העמוד - ממורכז כדי שהטלפון יישב באמצע המסך
st.set_page_config(page_title="MyHR+ Elbit Demo", layout="centered")

# הזרקת עיצוב מותאם אישית (CSS) 
css = """
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { max-width: 450px !important; padding-top: 1rem !important; }
    
    .mobile-wrapper {
        width: 100%;
        max-width: 380px;
        height: 750px;
        margin: 0 auto;
        background-color: #f0f2f5;
        border-radius: 40px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        overflow: hidden;
        position: relative;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        border: 8px solid #333;
    }

    .app-header {
        background: linear-gradient(135deg, #003366 0%, #004080 100%);
        color: white;
        padding: 35px 20px 60px 20px;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .header-text h1 { font-size: 20px; margin: 0; padding: 0; color: white; font-weight: bold; line-height: 1.2;}
    .header-text h1 span { font-size: 16px; font-weight: normal; margin-right: 5px;}
    .header-text p { font-size: 12px; margin: 8px 0 0 0; color: #b3d4ff; line-height: 1.4;}
    
    .face-id { width: 30px; height: 30px; opacity: 0.9; margin-top: 5px; }

    .main-content {
        background: white;
        border-radius: 20px 20px 0 0;
        margin-top: -30px;
        height: calc(100% - 150px);
        display: flex;
        flex-direction: column;
    }
    
    .dashboard-title {
        text-align: center; font-size: 18px; font-weight: bold; color: #222;
        padding: 15px 0; border-bottom: 1px solid #eee;
    }

    .cards-container { padding: 15px; background-color: #f4f5f8; flex-grow: 1; overflow-y: auto; padding-bottom: 80px;}

    .card {
        background: white; border-radius: 12px; padding: 15px; margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.04); border: 1px solid #eaeaea;
        display: flex; align-items: center;
    }
    
    .card-icon-area { width: 70px; display: flex; justify-content: center; align-items: center; margin-left: 15px; }
    .card-text-area { flex-grow: 1; text-align: right; }
    
    .card-title { font-size: 14px; font-weight: bold; color: #333; margin-bottom: 4px; }
    .card-value { font-size: 22px; font-weight: 800; color: #000; margin-bottom: 2px; }
    .card-subtitle { font-size: 11px; color: #777; }

    .circle-chart {
        width: 60px; height: 60px; border-radius: 50%;
        border: 5px solid #e0e0e0; border-right-color: #10b981; border-top-color: #10b981;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
    }
    .circle-val { font-size: 20px; font-weight: bold; line-height: 1; }
    .circle-label { font-size: 10px; color: #666; }

    .cibus-icon { width: 50px; height: 50px; background: #e0f2fe; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 24px; }

    .btn-outline {
        width: 100%; padding: 10px; border: 1px solid #004080; border-radius: 6px;
        background: transparent; color: #004080; font-weight: bold; font-size: 13px;
        margin-top: 15px; cursor: pointer;
    }

    .bottom-nav {
        position: absolute; bottom: 0; width: 100%; background: white;
        display: flex; justify-content: space-around; padding: 12px 0 20px 0;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05); border-top: 1px solid #eee;
    }
    .nav-item { display: flex; flex-direction: column; align-items: center; font-size: 11px; color: #888; }
    .nav-item.active { color: #004080; font-weight: bold; }
    .nav-icon { font-size: 20px; margin-bottom: 3px; }

    .alert-overlay {
        position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0,0,0,0.6); backdrop-filter: blur(3px);
        display: flex; justify-content: center; align-items: center; z-index: 100;
    }
    .alert-box {
        background: white; width: 85%; border-radius: 12px;
        box-shadow: 0 0 0 3px #00a3ff, 0 0 30px rgba(0, 163, 255, 0.6);
        overflow: hidden;
    }
    .alert-header {
        background: #003366; color: white; padding: 12px 15px;
        font-weight: bold; font-size: 15px; display: flex; align-items: center;
    }
    .alert-body { padding: 20px; text-align: right; }
    .alert-text { font-size: 14px; color: #222; line-height: 1.5; margin-bottom: 20px; }
    .alert-btn {
        width: 100%; background: #005bb5; color: white; padding: 12px;
        border: none; border-radius: 8px; font-weight: bold; font-size: 15px; cursor: pointer;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.write("⚙️ **פאנל שליטה לדמו (לא ייראה על ידי המשתמש):**")
col1, col2 = st.columns(2)
with col1:
    btn_dashboard = st.button("📱 הצג דשבורד (דניאל)", use_container_width=True)
with col2:
    btn_alert = st.button("⚠️ הצג התראה (מיכל)", use_container_width=True)

if 'current_view' not in st.session_state:
    st.session_state.current_view = 'dashboard'

if btn_dashboard: st.session_state.current_view = 'dashboard'
if btn_alert: st.session_state.current_view = 'alert'

# התיקון: בלוק ה-HTML ללא הזחות כדי ש-Streamlit לא יהפוך אותו לטקסט
if st.session_state.current_view == 'dashboard':
    html = """
<div class="mobile-wrapper">
    <div class="app-header">
        <div class="header-text">
            <h1>שלום, דניאל <span>MyHR+</span></h1>
            <p>אלביט<br>אלביט מערכות - חטיבה אווירית</p>
        </div>
        <div class="face-id">
            <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></svg>
        </div>
    </div>
    
    <div class="main-content">
        <div class="dashboard-title">הדשבורד האישי שלי</div>
        
        <div class="cards-container">
            <div class="card">
                <div class="card-icon-area">
                    <div class="circle-chart">
                        <span class="circle-val">12</span>
                        <span class="circle-label">ימים</span>
                    </div>
                </div>
                <div class="card-text-area">
                    <div class="card-title">יתרת חופשה</div>
                    <div class="card-value">12 ימים</div>
                    <div class="card-subtitle">מתוך 20 ימים שנתיים</div>
                </div>
            </div>
            
            <div class="card">
                <div class="card-icon-area">
                    <div class="cibus-icon">🍽️</div>
                </div>
                <div class="card-text-area">
                    <div class="card-title">יתרת סיבוס (Cibus)</div>
                    <div class="card-value">₪450</div>
                    <div class="card-subtitle">היתרה לספטמבר</div>
                </div>
            </div>
            
            <div class="card" style="display: block;">
                <div style="display: flex; justify-content: space-between;">
                    <div class="card-text-area">
                        <div class="card-title">עדכון שכר</div>
                        <div class="card-subtitle">עדכון שכר בהפצה<br>האחרון</div>
                    </div>
                    <div style="width: 100px; height: 50px; display: flex; align-items: flex-end; justify-content: space-between;">
                        <div style="width: 10px; height: 20%; background: #ccc; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 40%; background: #ccc; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 30%; background: #ccc; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 50%; background: #ccc; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 60%; background: #ccc; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 85%; background: #10b981; border-radius: 2px; position: relative;">
                            <span style="position: absolute; top: -18px; right: -2px; color: #10b981; font-weight: bold;">↑</span>
                        </div>
                    </div>
                </div>
                <button class="btn-outline">צפייה בתלוש האחרון</button>
            </div>
        </div>
    </div>
    
    <div class="bottom-nav">
        <div class="nav-item active"><div class="nav-icon">🏠</div>בית</div>
        <div class="nav-item"><div class="nav-icon">🎁</div>הטבות</div>
        <div class="nav-item"><div class="nav-icon">📄</div>מסמכים</div>
        <div class="nav-item"><div class="nav-icon">👤</div>פרופיל</div>
    </div>
</div>
"""

elif st.session_state.current_view == 'alert':
    html = """
<div class="mobile-wrapper">
    <div class="app-header">
        <div class="header-text">
            <h1>בוקר טוב, מיכל <span>MyHR+</span></h1>
            <p>אלביט<br>אלביט מערכות - חטיבה אווירית</p>
        </div>
        <div class="face-id">
            <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></svg>
        </div>
    </div>
    
    <div class="main-content" style="opacity: 0.6; pointer-events: none;">
        <div class="cards-container">
            <div class="card"><div style="height: 60px;"></div></div>
            <div class="card"><div style="height: 60px;"></div></div>
        </div>
    </div>
    
    <div class="alert-overlay">
        <div class="alert-box">
            <div class="alert-header">
                <span style="margin-left: 8px; color: #ffd700;">⚠️</span> התראה חשובה מ- MyHR+ AI
            </div>
            <div class="alert-body">
                <div class="alert-text">
                    <strong>מיכל</strong>, שמנו לב שעדיין לא ניצלת את סבסוד הלימודים השנתי שלך (עד ₪3,000)!<br><br>
                    תוקף הזכאות פג בעוד 3 ימים (30.09.24).
                </div>
                <button class="alert-btn">למימוש הזכות עכשיו בלחיצה</button>
            </div>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item active"><div class="nav-icon">🏠</div>בית</div>
        <div class="nav-item"><div class="nav-icon">🎁</div>הטבות</div>
        <div class="nav-item"><div class="nav-icon">📄</div>מסמכים</div>
        <div class="nav-item"><div class="nav-icon">👤</div>פרופיל</div>
    </div>
</div>
"""

st.markdown(html, unsafe_allow_html=True)
