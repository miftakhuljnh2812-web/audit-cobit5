import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Audit COBIT 5",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# SESSION STATE
# =====================================
if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

# =====================================
# CSS GRADASI
# =====================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #F4F7FF,
        #E8EEFF,
        #F9F8FF
    );
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #142D5C 0%,
        #2457B8 55%,
        #647DE0 100%
    );
}

[data-testid="stSidebar"] * {
    color: white;
}

/* JUDUL */
.main-title {
    font-size: 32px;
    font-weight: 800;
    color: #183B75;
}

.subtitle {
    color: #64748B;
    font-size: 15px;
}

/* KARTU DASHBOARD */
.info-card {
    background: linear-gradient(
        135deg,
        #FFFFFF,
        #E4ECFF
    );
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #DCE5FF;
    box-shadow: 0 4px 15px rgba(36,87,184,0.10);
    min-height: 125px;
}

.info-label {
    color: #64748B;
    font-size: 14px;
}

.info-value {
    color: #2457B8;
    font-size: 27px;
    font-weight: bold;
}

.section-title {
    color: #183B75;
    font-size: 22px;
    font-weight: bold;
}

/* TOMBOL */
.stButton > button {
    background: linear-gradient(
        90deg,
        #2457B8,
        #647DE0
    );
    color: white;
    border: none;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================
with st.sidebar:

    st.markdown("# 📊 COBIT 5")
    st.markdown("### AUDIT SYSTEM")
    st.divider()

    menu = st.radio(
        "MENU NAVIGASI",
        [
            "Dashboard",
            "Profil Perusahaan",
            "Kuesioner Audit",
            "Hasil Audit",
            "Rekomendasi"
        ],
        key="menu"
    )

    st.divider()

    st.caption("Sistem Audit Tata Kelola TI")
    st.caption("Framework COBIT 5")
    st.caption("© 2026 Audit COBIT 5")

# =====================================
# DASHBOARD
# =====================================
if menu == "Dashboard":

    st.markdown(
        '<p class="main-title">Dashboard Audit COBIT 5</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Sistem Evaluasi Tata Kelola Teknologi Informasi</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.header("Selamat Datang!")

    st.write("""
    Website ini merupakan sistem evaluasi tata kelola
    teknologi informasi menggunakan framework COBIT 5.

    Objek audit adalah Aplikasi Persediaan dan Penjualan
    pada PT Muria Bangun Mandiri.
    """)

    st.divider()

    st.markdown(
        '<p class="section-title">Ringkasan Audit</p>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="info-label">Domain COBIT 5</div>
            <div class="info-value">5</div>
            <div class="info-label">Domain evaluasi</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="info-label">Jumlah Pertanyaan</div>
            <div class="info-value">30</div>
            <div class="info-label">Pertanyaan audit</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
            <div class="info-label">Status Audit</div>
            <div class="info-value" style="font-size:22px;">
                Belum Dimulai
            </div>
            <div class="info-label">Proses evaluasi</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        '<p class="section-title">Objek Audit</p>',
        unsafe_allow_html=True
    )

    st.info("""
    **PT Muria Bangun Mandiri**

    Objek evaluasi: Aplikasi Audit Persediaan dan Penjualan.

    Fokus evaluasi:
    - Pengelolaan data persediaan.
    - Pencatatan transaksi penjualan.
    - Keamanan dan pengendalian sistem.
    - Ketepatan informasi dan pelaporan.
    """)

    st.markdown(
        '<p class="section-title">Domain COBIT 5</p>',
        unsafe_allow_html=True
    )

    domains = {
        "EDM": "Evaluate, Direct and Monitor",
        "APO": "Align, Plan and Organize",
        "BAI": "Build, Acquire and Implement",
        "DSS": "Deliver, Service and Support",
        "MEA": "Monitor, Evaluate and Assess"
    }

    for kode, nama in domains.items():
        st.markdown(f"**{kode}** — {nama}")

# =====================================
# HALAMAN LAIN
# =====================================
elif menu == "Profil Perusahaan":
    st.title("Profil Perusahaan")
    st.info("Halaman profil perusahaan akan dikembangkan.")

elif menu == "Kuesioner Audit":
    st.title("Kuesioner Audit")
    st.info("Halaman kuesioner audit akan dikembangkan.")

elif menu == "Hasil Audit":
    st.title("Hasil Audit")
    st.info("Halaman hasil audit akan dikembangkan.")

elif menu == "Rekomendasi":
    st.title("Rekomendasi")
    st.info("Halaman rekomendasi audit akan dikembangkan.")
