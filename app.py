import streamlit as st

# 1. Cài đặt tiêu đề trang web
st.set_page_config(page_title="App Tính Tổng", layout="centered")

# 2. Đưa đoạn CSS font Montserrat & màu XANH DƯƠNG vào
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

* {
    font-family: 'Montserrat', sans-serif !important;
}

.stApp {
    background-image: url("https://wptutbyserahwang.wordpress.com/wp-content/uploads/2020/04/201.jpg?w=560"); 
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* KHUNG DUONG-VIEN THEO CÁCH CỦA BẠN */
.block-container {
    background-color: rgba(255, 255, 255, 0.95); /* Làm nền trắng hơn xíu để che nét đứt cho rõ */
    border-radius: 15px; /* Giảm bo tròn lại cho giống thẻ bài */
    padding: 3rem;
    
    /* 🟢 Bóng đổ 30 độ về bên trái giữ nguyên */
    box-shadow: -15px 26px 50px rgba(30, 58, 138, 0.3) !important; 
    
    /* 🟢 Thêm đường viền nét đứt theo code bạn học */
    border: 3px dotted #3b82f6 !important; 
    
    max-width: 750px !important; 
    margin: auto !important; 
    margin-top: 10vh !important; /* Đẩy khung xuống một chút cho đẹp */
}

div[data-testid="stMain"] {
    justify-content: center !important;
}

button[aria-label="Step Up"], button[aria-label="Step Down"] {
    display: none !important;
}

div[data-baseweb="input"] > div, 
div[data-baseweb="number-input"] > div {
    border-radius: 15px !important; 
    border: 2px solid #93c5fd !important; 
    background-color: #eff6ff !important; 
}

input {
    color: #1e3a8a !important; 
    -webkit-text-fill-color: #1e3a8a !important;
    font-weight: bold !important;
    font-size: 1.2rem !important;
    text-align: center !important; 
}

button[data-testid="baseButton-primary"] {
    background-color: #3b82f6 !important; 
    border: none !important;
    border-radius: 25px !important; 
    padding: 0.75rem 2rem !important;
    box-shadow: 0 4px 10px rgba(59, 130, 246, 0.4); 
    width: 100%; 
    margin-top: 20px !important; 
    transition: all 0.3s ease;
}

button[data-testid="baseButton-primary"] * {
    color: #ffffff !important; 
    font-weight: bold !important;
    font-size: 1.2rem !important;
}

button[data-testid="baseButton-primary"]:hover {
    background-color: #1d4ed8 !important; 
    transform: translateY(-2px); 
}

h1, h2, h3, h4, p {
    color: #1e3a8a !important;
}

.math-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-height: 45px;
    font-size: 2rem;
    font-weight: bold;
    color: #1e3a8a;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 3. GIAO DIỆN BÀI TOÁN TÍNH TỔNG
# ==========================================

# 🟢 ÁP DỤNG MÃ TIEU-DE CỦA BẠN (Dùng margin âm để kéo đè lên viền đứt)
tieu_de_html = """
<div style="text-align: center; margin-top: -65px; margin-bottom: 30px;">
    <span style="display: inline-block; background: white; padding: 5px 25px; font-size: 24px; font-weight: bold; color: #1e3a8a; border-radius: 10px; border: 2px solid #3b82f6;">
        🧩 BÀI TOÁN TÍNH TỔNG
    </span>
</div>
"""
st.markdown(tieu_de_html, unsafe_allow_html=True)

# Phần nội dung bên trong giữ nguyên
col1, col2, col3, col4, col5 = st.columns([2, 1, 2, 1, 2])

with col1:
    x1 = st.number_input("x1", value=0.0, step=1.0, label_visibility="collapsed")

with col2:
    st.markdown("<div class='math-icon'>+</div>", unsafe_allow_html=True)

with col3:
    x2 = st.number_input("x2", value=0.0, step=1.0, label_visibility="collapsed")

with col4:
    st.markdown("<div class='math-icon'>=</div>", unsafe_allow_html=True)

with col5:
    result_placeholder = st.empty()
    result_placeholder.markdown("<div class='math-icon'>?</div>", unsafe_allow_html=True)

st.write("") 

# ==========================================
# 4. XỬ LÝ NÚT BẤM
# ==========================================
if st.button("TÍNH TOÁN", type="primary"):
    ket_qua = x1 + x2
    result_placeholder.markdown(f"<div class='math-icon'>{ket_qua}</div>", unsafe_allow_html=True)
