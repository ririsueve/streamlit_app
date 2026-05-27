import streamlit as st

# 1. Cài đặt tiêu đề trang web
st.set_page_config(page_title="App Tính Tổng", layout="centered")

# 2. Đưa đoạn CSS màu XANH TEAL & nền mây trời vào
custom_css = """
<style>
/* 1. ĐỔI TOÀN BỘ FONT THÀNH TIMES NEW ROMAN */
* {
    font-family: 'Times New Roman', Times, serif !important;
}

/* Nền mây trời */
.stApp {
    background-image: url("https://images.pexels.com/photos/37060630/pexels-photo-37060630.jpeg"); 
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* 2. CANH GIỮA HOÀN TOÀN CẢ NGANG LẪN DỌC */
.block-container {
    background-color: rgba(255, 255, 255, 0.85); 
    border-radius: 30px; 
    padding: 3rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1); 
    max-width: 750px !important; 
    margin: auto !important; 
}

div[data-testid="stMain"] {
    justify-content: center !important;
}

/* 3. LÀM ĐỀU CÁC Ô NHẬP LIỆU (Ẩn nút cộng trừ) */
button[aria-label="Step Up"], button[aria-label="Step Down"] {
    display: none !important;
}

/* Viền ô nhập số màu XANH NHẠT (#3BC1A8) */
div[data-baseweb="input"] > div, 
div[data-baseweb="number-input"] > div {
    border-radius: 15px !important; 
    border: 2px solid #3BC1A8 !important; 
    background-color: #f0fbf9 !important; /* Nền xanh rất nhạt */
}

/* Chữ người dùng nhập vào màu XANH ĐẬM NHẤT (#005461) */
input {
    color: #005461 !important; 
    -webkit-text-fill-color: #005461 !important;
    font-weight: bold !important;
    font-size: 1.2rem !important;
    text-align: center !important; 
}

/* 4. SỬA NÚT TÍNH TOÁN BẰNG BỘ MÀU XANH TEAL */
button[data-testid="baseButton-primary"] {
    background-color: #249E94 !important; 
    border: none !important;
    border-radius: 25px !important; 
    padding: 0.75rem 2rem !important;
    box-shadow: 0 4px 10px rgba(36, 158, 148, 0.4); 
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
    background-color: #0C7779 !important; 
    transform: translateY(-2px); 
}

/* Đổi màu chữ tiêu đề thành XANH (#0C7779) */
h1, h2, h3, h4, p {
    color: #0C7779 !important;
}

/* 5. CÔNG CỤ CANH GIỮA DẤU CỘNG, BẰNG, HỎI CHẤM */
.math-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-height: 45px;
    font-size: 2rem;
    font-weight: bold;
    color: #0C7779;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 3. GIAO DIỆN BÀI TOÁN TÍNH TỔNG
# ==========================================
st.markdown("### 🧩 BÀI TOÁN TÍNH TỔNG")
st.write("") 

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
