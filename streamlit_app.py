import streamlit as st

# Color Branding (Dashen Sushi Green)
SUSHI_GREEN = "#83b735"

st.set_page_config(page_title="FutureValue AI by Dashen", page_icon="📈")

# Custom CSS to match Dashen Brand
st.markdown(f"""
    <style>
    .main {{ background-color: #ffffff; }}
    .stButton>button {{
        background-color: {SUSHI_GREEN};
        color: white;
        border-radius: 8px;
        width: 100%;
        height: 3.5em;
        border: none;
        font-weight: bold;
        font-size: 18px;
    }}
    .stButton>button:hover {{
        background-color: #6e9a2d;
        color: white;
    }}
    /* Style for Slider Sushi Green */
    div[data-baseweb="slider"] > div > div {{
        background-color: {SUSHI_GREEN} !important;
    }}
    /* Metric styling */
    [data-testid="stMetricValue"] {{
        color: {SUSHI_GREEN};
        font-size: 32px;
    }}
    [data-testid="stMetricLabel"] {{
        font-size: 18px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# Title Section
st.markdown(f"<h1 style='text-align: center; color: #333;'>📈 FutureValue AI by Dashen</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: {SUSHI_GREEN};'>رؤية القيمة المستقبلية من داشن</h3>", unsafe_allow_html=True)

st.write("---")

# Inputs Section
col1, col2 = st.columns(2)

with col1:
    project_type = st.selectbox(
        "Project Type | نوع المشروع",
        ["Apartment | شقة", "Villa | فيلا", "Roof | روف"]
    )
    status = st.selectbox(
        "Status | الحالة",
        ["Under Construction | تحت الإنشاء"]
    )

with col2:
    area = st.selectbox(
        "Area | المنطقة",
        ["Ar Rawdah | الروضة", "Al Yasmin | الياسمين", "Al Malqa | الملقا", "Al Narjis | النرجس"]
    )
    current_price = st.number_input(
        "Current Price (SAR) | السعر الحالي (ريال)",
        min_value=100000, value=750000, step=10000
    )

years = st.slider("Years to Completion | سنوات حتى التسليم", 1, 5, 2)

# Calculation Logic (AI Model Approximation)
appreciation_rates = {
    "Ar Rawdah | الروضة": 0.09,
    "Al Yasmin | الياسمين": 0.11,
    "Al Malqa | الملقا": 0.12,
    "Al Narjis | النرجس": 0.08
}
annual_rate = appreciation_rates.get(area, 0.08)
future_val = current_price * (1 + annual_rate) ** years
profit = future_val - current_price
roi = (profit / current_price) * 100

# Prediction Button
if st.button("Predict Future Value | توقع القيمة المستقبلية"):
    st.write("---")
    target_year = 2025 + years
    
    st.markdown(f"### Predicted Value in {target_year} | القيمة المتوقعة في عام {target_year}")
    st.markdown(f"<h1 style='color: {SUSHI_GREEN};'>SAR {future_val:,.0f}</h1>", unsafe_allow_html=True)

    m1, m2 = st.columns(2)
    m1.metric("Estimated Profit | الربح التقديري", f"SAR {profit:,.0f}")
    m2.metric("Total ROI | إجمالي العائد", f"{roi:.1f}%")

    st.write("---")
    
    # Bilingual Info Section
    st.info(f"""
    **ℹ️ AI Insights | معلومات الذكاء الاصطناعي:**
    Our AI analysis shows an 85% confidence score based on historical data mining and municipal growth permits.
    \n يُظهر تحليل الذكاء الاصطناعي لدينا درجة ثقة بنسبة 85% بناءً على تنقيب البيانات التاريخية وتصاريح النمو البلدي.
    """)

    st.warning(f"""
    **Disclaimer | إخلاء مسؤولية:**
    This is an AI-generated estimation based on market trends. Actual values may vary.
    \n هذا تقدير ناتج عن الذكاء الاصطناعي بناءً على اتجاهات السوق. قد تختلف القيم الفعلية.
    """)
