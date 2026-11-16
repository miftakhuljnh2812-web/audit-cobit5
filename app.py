
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Audit COBIT 5",
    page_icon="📊",
    layout="wide"
)

# Judul aplikasi
st.title("📊 Sistem Audit COBIT 5")
st.subheader("Aplikasi Audit Persediaan dan Penjualan")

st.divider()

# Informasi perusahaan
st.header("Profil Objek Audit")

st.write("""
**Nama Perusahaan:** PT Muria Bangun Mandiri

**Objek Audit:** Aplikasi Audit Persediaan dan Penjualan

**Framework:** COBIT 5

Aplikasi ini digunakan untuk melakukan evaluasi tata kelola
teknologi informasi pada sistem persediaan dan penjualan.
""")

st.divider()

# Dashboard sederhana
st.header("Dashboard Audit")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Domain COBIT 5", "5")

with col2:
    st.metric("Jumlah Pertanyaan", "30")

with col3:
    st.metric("Status Audit", "Belum Dimulai")

st.info("Silakan lanjutkan ke menu audit untuk memulai evaluasi.")
