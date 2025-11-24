import streamlit as st

st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .judul {
        animation: fadeIn 1.5s ease-out;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: ;
        margin-top: 30px;
    }
    .garis {
        border: none;
        height: 2px;
        background: linear-gradient(to right, #888, #ccc, #888);
        margin: 20px auto;
        width: 60%;
    }
    .deskripsi {
        animation: fadeIn 3s ease-out;
        text-align: center;
        font-size: 18px;
        color: ;
        margin-top: 10px;
    }
        .label-fungsi {
        font-size: 20px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 5px;
        color: #ffffff;
    }

    .contoh-fungsi {
        font-size: 14px;
        color: #cccccc;
        margin-bottom: 10px;
    }

    .stTextInput > div > input {
        height: 45px;
        font-size: 16px;
        border-radius: 8px;
        padding-left: 10px;
    }
        .label-param {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 5px;
    }
     .nb-fungsi {
        font-size: 14px;
        color: #cccccc;
        margin-bottom: 10px;
    }
    .label-pias {
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .btn-hitung {
        display: inline-block;
        text-align: right;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        color: white;
        background-color: #28a745;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin-top: 30px;
    }

    .btn-hitung:hover {
        background-color: #218838;
    }
    </style>

    <div class="judul">Aplikasi Web Solusi Integral Dengan Kaidah Pias Persegi Panjang</div>
    <hr class="garis">
    <div class="deskripsi">Masukkan fungsi dan parameter integral untuk menghitung estimasi integral menggunakan Rectangle Rule.</div>
""", unsafe_allow_html=True)

# Input fungsi
st.markdown("<div class='label-fungsi'>FUNGSI f(x)</div>", unsafe_allow_html=True)
st.markdown("<div class='contoh-fungsi'>contoh: x^2 + 3x + 1</div>", unsafe_allow_html=True)
fungsi_input = st.text_input("", placeholder="Masukkan fungsi di sini...")

# Input parameter integral
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='label-param'>Batas Bawah (a)</div>", unsafe_allow_html=True)
    a = st.number_input("", key="bawah")
with col2:
    st.markdown("<div class='label-param'>Batas Atas (b)</div>", unsafe_allow_html=True)
    b = st.number_input("", key="atas")
with col3:
    st.markdown("<div class='label-param'>Jumlah Pias (n)</div>", unsafe_allow_html=True)
    n = st.number_input("", min_value=1, step=1, key="pias")
   
    st.markdown("<div class='nb-fungsi'>NB: 1,00 = 1</div>", unsafe_allow_html=True)
    
# Pilihan tipe pias
st.markdown("<div class='label-pias'>Pilih Tipe Pias:</div>", unsafe_allow_html=True)
tipe_pias = st.radio(
    "",
    options=["Left Rectangle", "Right Rectangle", "Midpoint"],
    horizontal=True
)

# Tombol dengan HTML
hitung = st.markdown(
    "<button class='btn-hitung'>Hitung Integral</button>",
    unsafe_allow_html=True
)
