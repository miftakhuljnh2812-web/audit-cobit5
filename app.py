import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Audit COBIT 5",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# SESSION STATE
# =====================================
if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

# =====================================
# CSS SOFT PINK GRADIENT
# =====================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');

/* FONT GLOBAL */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* BACKGROUND UTAMA */
.stApp {
    background: linear-gradient(
        135deg,
        #FFF8FA 0%,
        #FCE4EC 35%,
        #F8D7E3 70%,
        #F2C6D6 100%
    ) !important;
    background-attachment: fixed !important;
}

/* MEMASTIKAN AREA UTAMA TRANSPARAN */
[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

[data-testid="stMain"] {
    background: transparent !important;
}

/* HEADER STREAMLIT */
[data-testid="stHeader"] {
    background: rgba(255, 248, 250, 0.85) !important;
}

/* JARAK KONTEN AGAR TIDAK TERPOTONG */
.block-container {
    padding-top: 4.5rem !important;
    padding-bottom: 3rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    max-width: 1500px;
}

/* SIDEBAR GRADASI */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #F8D6E2 0%,
        #F1BDD0 45%,
        #EBAAC2 75%,
        #E69AB8 100%
    ) !important;
}

/* ISI SIDEBAR */
[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
}

[data-testid="stSidebar"] * {
    color: #70465A;
}

/* JUDUL UTAMA */
.main-title {
    font-family: 'Poppins', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #90566F;
    margin-top: 0;
    margin-bottom: 8px;
}

/* SUBJUDUL */
.subtitle {
    color: #A7798D;
    font-size: 15px;
}

/* JUDUL BAGIAN */
.section-title {
    font-family: 'Poppins', sans-serif;
    color: #90566F;
    font-size: 22px;
    font-weight: 700;
}

/* KARTU DASHBOARD */
.info-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #FFF4F7 55%,
        #FCEAF0 100%
    );
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #F1D1DE;
    box-shadow: 0 5px 18px rgba(174, 104, 133, 0.10);
    min-height: 125px;
}

/* TEKS KARTU */
.info-label {
    color: #987586;
    font-size: 14px;
}

.info-value {
    color: #C47796;
    font-size: 27px;
    font-weight: 700;
}

/* TOMBOL */
.stButton > button {
    background: linear-gradient(
        90deg,
        #E8A5BC,
        #D987A6
    );
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #D987A6,
        #C87596
    );
    color: white;
    border: none;
}

/* KOTAK INFORMASI */
[data-testid="stAlert"] {
    background: linear-gradient(
        120deg,
        #FFF8FA,
        #FCEAF0
    ) !important;
    border: 1px solid #F1D1DE;
    border-radius: 12px;
}

/* PEMISAH */
hr {
    border-color: #EBCBD7;
}

/* RADIO MENU */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 8px;
}

/* RADIO BUTTON */
[data-testid="stSidebar"] [role="radiogroup"] label {
    color: #70465A !important;
}

/* SIDEBAR JUDUL */
.sidebar-title {
    font-family: 'Poppins', sans-serif;
    font-size: 30px;
    font-weight: 700;
    color: #70465A;
    margin-bottom: 0;
}

.sidebar-subtitle {
    color: #80586B;
    font-size: 13px;
    letter-spacing: 2px;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .block-container {
        padding-top: 3rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .main-title {
        font-size: 25px;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================
# SIDEBAR
# =====================================
with st.sidebar:

    st.markdown(
        '<p class="sidebar-title">COBIT 5</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sidebar-subtitle">AUDIT SYSTEM</p>',
        unsafe_allow_html=True
    )

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
# PROFIL PERUSAHAAN
# =====================================
elif menu == "Profil Perusahaan":

    st.markdown(
        '<p class="main-title">Profil Perusahaan</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Informasi objek audit</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.header("PT Muria Bangun Mandiri")

    st.write("""
    PT Muria Bangun Mandiri merupakan objek yang digunakan
    dalam evaluasi tata kelola teknologi informasi pada
    aplikasi persediaan dan penjualan.
    """)

    st.markdown("### Informasi Audit")

    st.write("**Objek Audit:** Aplikasi Persediaan dan Penjualan")
    st.write("**Framework:** COBIT 5")
    st.write("**Fokus Audit:** Tata kelola dan pengelolaan teknologi informasi")


# =====================================
# KUESIONER AUDIT
# =====================================
elif menu == "Kuesioner Audit":

    st.markdown(
        '<p class="main-title">Kuesioner Audit</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Daftar pertanyaan evaluasi COBIT 5</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.info("Halaman kuesioner audit akan dikembangkan.")

    st.write("""
    Kuesioner ini nantinya digunakan untuk menilai
    tingkat kapabilitas proses berdasarkan domain COBIT 5.
    """)


# =====================================
# HASIL AUDIT
# =====================================
elif menu == "Hasil Audit":

    st.markdown(
        '<p class="main-title">Hasil Audit</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Rekapitulasi hasil evaluasi tata kelola TI</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.info(
        "Hasil audit akan ditampilkan setelah proses pengisian kuesioner selesai."
    )

    st.write("""
    Halaman ini nantinya menampilkan hasil penilaian,
    tingkat kapabilitas, dan ringkasan evaluasi
    berdasarkan domain COBIT 5.
    """)


# =====================================
# REKOMENDASI
# =====================================
elif menu == "Rekomendasi":

    st.markdown(
        '<p class="main-title">Rekomendasi Audit</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Saran perbaikan berdasarkan hasil evaluasi</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.info(
        "Rekomendasi audit akan ditampilkan berdasarkan hasil penilaian."
    )

    st.write("""
    Halaman ini nantinya berisi saran perbaikan
    untuk meningkatkan tata kelola teknologi informasi
    pada aplikasi persediaan dan penjualan.
    """)
