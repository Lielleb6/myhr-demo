import streamlit as st
import time

st.set_page_config(page_title="MyHR+ App", layout="centered", initial_sidebar_state="collapsed")

if 'app_loaded' not in st.session_state:
    st.session_state.app_loaded = False

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
.stApp { background-color: #f0f2f6 !important; }
.block-container { padding: 0 !important; max-width: 480px !important; }
#MainMenu { visibility: hidden; }
header { display: none !important; }
footer { display: none !important; }

@keyframes pulse {
    0% { transform: scale(0.95); opacity: 0.8; }
    50% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.8; }
}
.pulse-text { animation: pulse 1.5s infinite ease-in-out; }
.pulse-sub { animation: pulse 1.5s infinite ease-in-out; animation-delay: 0.2s; }
</style>
""", unsafe_allow_html=True)

if not st.session_state.app_loaded:
    st.markdown("""
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(180deg, #0a4682 0%, #052c54 100%); display: flex; flex-direction: column; justify-content: center; align-items: center; z-index: 999999; font-family: 'Assistant', sans-serif;">
        <div class="pulse-text" dir="ltr" style="color: white; font-size: 55px; font-weight: 900; letter-spacing: 2px;">MyHR+</div>
        <div class="pulse-sub" style="color: #b3d4ff; font-size: 18px; margin-top: 10px; font-weight: 600;">מתחבר למערכות...</div>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(2.5)
    st.session_state.app_loaded = True
    st.rerun()

else:
    st.markdown("""
    <div style="background-color: #f0f2f6; padding-bottom: 110px; width: 100%; direction: rtl; font-family: 'Assistant', sans-serif;">
        <div style="background: linear-gradient(180deg, #0a4682 0%, #052c54 100%); color: white; padding: 40px 20px 45px 20px; border-bottom-right-radius: 25px; border-bottom-left-radius: 25px; display: flex; justify-content: space-between; align-items: flex-start; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <div style="display: flex; align-items: flex-start; gap: 12px;">
                <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></svg>
                <div style="text-align: right;">
                    <div style="font-size: 22px; font-weight: 800; margin-bottom: 2px;">שלום, דניאל</div>
                    <div style="font-size: 15px; opacity: 0.9; font-weight: 600;">אלביט מערכות</div>
                    <div style="font-size: 14px; opacity: 0.85;">חטיבה אווירית</div>
                </div>
            </div>
            <div dir="ltr" style="font-size: 24px; font-weight: 800; letter-spacing: 0.5px;">MyHR+</div>
        </div>

        <div style="padding: 20px 15px 0 15px; position: relative; z-index: 10;">
            <div style="text-align: right; color: #0a4682; font-size: 22px; font-weight: 900; margin-bottom: 15px;">הדשבורד האישי שלי</div>

            <div style="background: white; border-radius: 16px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; align-items: center; justify-content: space-between;">
                <div style="text-align: right;">
                    <div style="font-size: 16px; font-weight: 700; color: #111;">יתרת חופשה</div>
                    <div style="font-size: 28px; font-weight: 900; color: #000; margin: 2px 0;">12 ימים</div>
                    <div style="font-size: 14px; color: #666;">מתוך 20 ימים שנתיים</div>
                </div>
                <div style="position: relative; width: 75px; height: 75px; border-radius: 50%; background: conic-gradient(#34d399 0% 60%, #e5e7eb 60% 100%); display: flex; justify-content: center; align-items: center;">
                    <div style="width: 55px; height: 55px; background: white; border-radius: 50%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                        <span style="font-size: 22px; font-weight: 900; color: #000; line-height: 1;">12</span>
                        <span style="font-size: 12px; color: #666; font-weight: 600;">ימים</span>
                    </div>
                </div>
            </div>

            <div style="background: white; border-radius: 16px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; align-items: center; justify-content: space-between;">
                <div style="text-align: right;">
                    <div style="font-size: 16px; font-weight: 700; color: #111;">יתרת סיבוס (Cibus)</div>
                    <div dir="rtl" style="font-size: 28px; font-weight: 900; color: #000; margin: 2px 0;">₪450</div>
                    <div style="font-size: 13px; color: #666; max-width: 180px;">היתרה לספטמבר. כל יום זכאי ל-90 ש"ח</div>
                </div>
                <div style="width: 70px; height: 70px; border-radius: 50%; background: #f0f7ff; display: flex; justify-content: center; align-items: center; border: 1px solid #e1effe;">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0a4682" stroke-width="1.5"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/></svg>
                </div>
            </div>

            <div style="background: white; border-radius: 16px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px;">
                    <div style="text-align: right;">
                        <div style="font-size: 16px; font-weight: 700; color: #111;">עדכון שכר</div>
                        <div style="font-size: 14px; color: #666; margin-top: 2px;">עדכון שכר מהתלוש האחרון</div>
                    </div>
                    <div style="display: flex; align-items: flex-end; gap: 4px; height: 45px;">
                        <div style="width: 10px; height: 40%; background: #cbd5e1; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 60%; background: #cbd5e1; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 50%; background: #cbd5e1; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 70%; background: #cbd5e1; border-radius: 2px;"></div>
                        <div style="width: 10px; height: 55%; background: #cbd5e1; border-radius: 2px;"></div>
                        <div style="width: 12px; height: 90%; background: #34d399; border-radius: 2px; position: relative; display: flex; justify-content: center;">
                            <span style="position: absolute; top: -16px; color: #34d399; font-size: 14px; font-weight: bold;">↑</span>
                        </div>
                    </div>
                </div>
                <div style="width: 100%; text-align: center; border: 1.5px solid #0a4682; color: #0a4682; padding: 10px; border-radius: 10px; font-weight: 700; font-size: 15px;">צפייה בתלוש האחרון</div>
            </div>
        </div>

        <div style="position: fixed; bottom: 0; left: 0; right: 0; background: white; padding: 12px 0 25px 0; display: flex; justify-content: space-around; box-shadow: 0 -4px 15px rgba(0,0,0,0.05); border-top: 1px solid #f0f0f0; z-index: 100; max-width: 480px; margin: 0 auto;">
            <div style="text-align: center; color: #94a3b8; font-weight: 600; font-size: 12px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg><br>פרופיל
            </div>
            <div style="text-align: center; color: #94a3b8; font-weight: 600; font-size: 12px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg><br>מסמכים
            </div>
            <div style="text-align: center; color: #94a3b8; font-weight: 600; font-size: 12px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="8" width="18" height="14" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="22"></line><path d="M12 8V4h-3a3 3 0 0 0 0 6h6a3 3 0 0 0 0-6h-3v4"></path></svg><br>הטבות
            </div>
            <div style="text-align: center; color: #0a4682; font-weight: 800; font-size: 12px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg><br>בית
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
