import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
     @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
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
        animation: fadeInUp 4s ease-out;
        font-size: 20px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 5px;
        color: #ffffff;
    }
    .contoh-fungsi {
        animation: fadeInUp 4s ease-out;
        font-size: 14px;
        color: #cccccc;
        margin-bottom: 10px;
    }
    .stTextInput > div > input {
        height: 45px;
        font-size: 16px;
        border-radius: 8px;
        padding-left: 10px;
        animation: fadeInUp 5s ease-out;
    }
     .nb-fungsi {
        animation: fadeInUp 4s ease-out;
        font-size: 14px;
        color: #cccccc;
        margin-bottom: 10px;
    }
    .label-param {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 5px;
        animation: fadeInUp 5s ease-out;
    }
    .nb-param {
        animation: fadeInUp 4s ease-out;
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
        animation: fadeInUp 6s ease-out;
    }
    .stButton > button {
        display: inline-block;
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
        animation: fadeInUp 2.6s ease-out;
    }

    .stButton > button:hover {
        background-color: #218838;
        transform: scale(1.05);
        animation: pulse 1s infinite;
    }
    </style>

    <div class="judul">Aplikasi Web Solusi Integral Dengan Kaidah Pias Persegi Panjang</div>
    <hr class="garis">
    <div class="deskripsi">Masukkan fungsi dan parameter integral untuk menghitung estimasi integral menggunakan Rectangle Rule.</div>
""", unsafe_allow_html=True)

# Input fungsi
st.markdown("<div class='label-fungsi'>FUNGSI f(x)</div>", unsafe_allow_html=True)
st.markdown("<div class='contoh-fungsi'>contoh: x^2 + 3*x + 1</div>", unsafe_allow_html=True)
fungsi_input = st.text_input("", placeholder="Masukkan fungsi di sini...")
st.markdown("<div class='nb-fungsi'>NB : * = kali atau x, ^ = pangkat</div>", unsafe_allow_html=True)

# Input parameter integral
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='label-param'>Batas Bawah (a)</div>", unsafe_allow_html=True)
    a = st.number_input("", key="bawah", format="%.2f", value=0.0)
with col2:
    st.markdown("<div class='label-param'>Batas Atas (b)</div>", unsafe_allow_html=True)
    b = st.number_input("", key="atas", format="%.2f", value=1.0)
with col3:
    st.markdown("<div class='label-param'>Jumlah Pias (n)</div>", unsafe_allow_html=True)
    n = st.number_input("", min_value=1, step=1, key="pias", value=10)
    st.markdown("<div class='nb-fungsi'>NB : 1 = 1,00</div>", unsafe_allow_html=True)
    
# Pilihan tipe pias
st.markdown("<div class='label-pias'>Pilih Tipe Pias:</div>", unsafe_allow_html=True)
tipe_pias = st.radio(
    "",
    options=["Left Rectangle", "Right Rectangle", "Midpoint"],
    horizontal=True
)

# Tombol hitung
if st.button("Hitung Intrgral"):
    try:
        #buat falidasi kode
        if a > b:
            a, b = b, a

        #parsing fungsi
        x = sp.symbols('x')
        f = sp.sympify(fungsi_input)
        f_num = sp.lambdify(x, f, "numpy")

        #lebar pias
        h = (b - a) / n

        #meentukan titik evaluasi
        if tipe_pias == "Left Rectangle":
            xs = np.linspace(a, b - h, n)
        elif tipe_pias == "Right Rectangle":
            xs = np.linspace(a + h, b, n)
        else:  #midpoin
            xs = np.linspace(a + h/2, b - h/2, n)
            
        # Hitung integral aproksimasi
        integral_est = np.sum(f_num(xs) * h)
        st.success(f"Hasil estimasi integral: {integral_est:.2f}")

        # Bandingkan dengan integral eksak
        integral_exact = sp.integrate(f, (x, a, b))
        st.info(f"Nilai integral eksak: {float(integral_exact):.2f}")
        
        # Visualisasi pias
        fig, ax = plt.subplots()
        X = np.linspace(a, b, 200)
        ax.plot(X, f_num(X), 'b', label='f(x)')
        for xi in xs:
            ax.bar(xi, f_num(xi), width=h, alpha=0.3, align='edge')
        ax.legend()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
