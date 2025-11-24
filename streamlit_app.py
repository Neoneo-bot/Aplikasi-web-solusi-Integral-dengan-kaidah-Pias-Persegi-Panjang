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
        color: #333333;
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
        color: #444444;
        margin-top: 10px;
    }
    </style>

    <div class="judul">Aplikasi Web Solusi Integral Dengan Kaidah Pias Persegi Panjang</div>
    <hr class="garis">
    <div class="deskripsi">Masukkan fungsi dan parameter integral untuk menghitung estimasi integral menggunakan Rectangle Rule.</div>
""", unsafe_allow_html=True)

