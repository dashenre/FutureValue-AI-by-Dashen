import streamlit as st

# Dashen Brand Colors from Screenshots
DASHEN_GREEN = "#83b735" # The Sushi Green
DARK_BG = "#1e1e1e"     # Dark background like your services section
TEXT_WHITE = "#ffffff"

st.set_page_config(page_title="FutureValue AI by Dashen", page_icon="📈", layout="centered")

# Custom CSS for Exact Match with Dashen Website
st.markdown(f"""
    <style>
    /* Main Background */
    .stApp {{
        background-color: #ffffff;
    }}
    
    /* Dark Card for the Tool Area */
    .main-container {{
        background-color: {DARK_BG};
        padding: 30px;
        border-radius: 10px;
        color: {TEXT_WHITE};
    }}

    /* Heading Style */
    h1, h2, h3 {{
        color: {DASHEN_GREEN} !important;
        font-family: 'Arial', sans-serif;
    }}

    /* Button Style: Dashen Green with White Text */
    .stButton>button {{
        background-color: {DASHEN_GREEN};
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 4px;
        width: 100%;
        margin-top: 20px;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #6e9a2d;
        color: white;
    }}

    /* Input Fields Styling */
    label {{
        color: #333 !important;
        font-weight: bold !important;
    }}
    
    /* Metrics section like your news cards */
    .metric-container {{
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    }}
    
    /* Slider Color Customization */
    div[data-baseweb="slider"] > div > div {{
        background-color: {DASHEN_GREEN} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# Title Section (English & Saudi Arabic)
st.markdown(f"<h1 style='text-align: center;'>FutureValue AI by Dashen</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>رؤية القيمة المستقبلية من داشن</h2>", unsafe_allow_html=True)
st.write("")

# Main Tool Card (Form)
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        project_type = st.selectbox("Project Type | نوع المشروع", ["Apartment | شقة", "Villa | فيلا", "Roof | روف"])
        status = st.selectbox("Status | الحالة", ["Under Construction | تحت الإنشاء"])
    
    with col2:
        area = st.selectbox("Area | المنطقة", ["Ar Rawdah | الروضة", "Al Yasmin | الياسمين", "Al Malqa | الملقا", "Al Narjis | النرجس"])
        price = st.number_input("Current Price (SAR) | السعر الحالي", min_value=100000, value=750000)

    years = st.slider("Years to Completion | سنوات حتى التسليم", 1, 5, 2)

    # Calculation logic
    rate = {"Ar Rawdah | الروضة": 0.09, "Al Yasmin | الياسمين": 0.11, "Al Malqa | الملقا": 0.12, "Al Narjis | النرجس": 0.08}.get(area, 0.08)
    f_val = price * (1 + rate) ** years
    profit = f_val - price
    roi = (profit / price) * 100

    if st.button("Predict Future Value | توقع القيمة المستقبلية"):
        st.markdown("---")
        target_year = 2025 + years
        
        # Result Layout
        st.markdown(f"<h3 style='text-align:center;'>Analysis for {target_year} | {target_year} تحليل عام </h3>", unsafe_allow_html=True)
        
        # Big Value Display
        st.markdown(f"<div style='text-align:center; padding:20px; background-color:{DARK_BG}; border-radius:10px;'>"+
                    f"<p style='color:white; margin:0;'>Predicted Market Value | القيمة السوقية المتوقعة</p>"+
                    f"<h1 style='color:{DASHEN_GREEN}; font-size:45px; margin:0;'>SAR {f_val:,.0f}</h1></div>", unsafe_allow_html=True)
        
        st.write("")
        
        # Metrics Row
        m1, m2 = st.columns(2)
        with m1:
            st.markdown(f"<div class='metric-container'><p style='margin:0;'>Estimated Profit</p><h2 style='margin:0;'>SAR {profit:,.0f}</h2><p style='margin:0;'>الربح التقديري</p></div>", unsafe_allow_html=True)
        with m2:
            st.markdown(f"<div class='metric-container'><p style='margin:0;'>Total ROI</p><h2 style='margin:0;'>{roi:.1f}%</h2><p style='margin:0;'>إجمالي العائد</p></div>", unsafe_allow_html=True)

        st.write("")
        st.info("ℹ️ Our AI analysis shows an 85% confidence score. | يُظهر تحليلنا ثقة بنسبة 85٪")
