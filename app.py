
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
# CSS GRADASI SOFT PINK
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

/* AREA UTAMA */
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: transparent !important;
}

/* HEADER STREAMLIT */
[data-testid="stHeader"] {
    background: rgba(255, 248, 250, 0.85) !important;
}

/* JARAK KONTEN */
.block-container {
    padding-top: 4.5rem !important;
    padding-bottom: 3rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    max-width: 1500px;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #F8D6E2 0%,
        #F1BDD0 45%,
        #EBAAC2 75%,
        #E69AB8 100%
    ) !important;
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
}

[data-testid="stSidebar"] * {
    color: #70465A;
}

/* JUDUL SIDEBAR */
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

/* KARTU RINGKASAN AUDIT */
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

.info-label {
    color: #987586;
    font-size: 14px;
}

.info-value {
    color: #C47796;
    font-size: 27px;
    font-weight: 700;
}

/* KARTU OBJEK AUDIT */
.object-card {
    background: linear-gradient(
        120deg,
        #FFF8FA 0%,
        #FCE4EC 50%,
        #F5D0DE 100%
    );
    border: 1px solid #EFC6D5;
    border-radius: 15px;
    padding: 22px 25px;
    box-shadow: 0 4px 15px rgba(190, 120, 150, 0.10);
    color: #70465A;
}

.object-card h4 {
    color: #90566F;
    font-family: 'Poppins', sans-serif;
    margin-top: 0;
    font-size: 19px;
}

.object-card p,
.object-card li {
    color: #80586B;
    line-height: 1.8;
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

/* KOTAK INFORMASI STREAMLIT */
[data-testid="stAlert"] {
    background: linear-gradient(
        120deg,
        #FFF8FA,
        #FCEAF0
    ) !important;
    border: 1px solid #F1D1DE !important;
    border-left: 5px solid #D987A6 !important;
    border-radius: 12px;
    color: #80586B !important;
}

/* PEMISAH */
hr {
    border-color: #EBCBD7;
}

/* RADIO MENU */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 8px;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    color: #70465A !important;
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

    .info-card {
        margin-bottom: 12px;
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

    # RINGKASAN AUDIT
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

    # OBJEK AUDIT
    st.markdown(
        '<p class="section-title">Objek Audit</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="object-card">

        <h4>PT Muria Bangun Mandiri</h4>

        <p>
            <b>Objek evaluasi:</b>
            Aplikasi Audit Persediaan dan Penjualan.
        </p>

        <p><b>Fokus evaluasi:</b></p>

        <ul>
            <li>Pengelolaan data persediaan.</li>
            <li>Pencatatan transaksi penjualan.</li>
            <li>Keamanan dan pengendalian sistem.</li>
            <li>Ketepatan informasi dan pelaporan.</li>
        </ul>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # DOMAIN COBIT 5
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

    st.info(
        "Halaman kuesioner audit akan dikembangkan."
    )

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
