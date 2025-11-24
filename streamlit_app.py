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
        color: white;
        margin-top: 30px;
    }

    .deskripsi {
        animation: fadeIn 3s ease-out;
        text-align: left;
        font-size: 18px;
        color: #dddddd;
        margin-top: 10px;
    }
    </style>

    <div class="judul">Aplikasi Web Solusi Integral Dengan Kaidah Pias Persegi Panjang</div>
    <div class="deskripsi">Masukkan fungsi dan parameter integral untuk menghitung estimasi integral menggunakan Rectangle Rule.</div>
""", unsafe_allow_html=True)

