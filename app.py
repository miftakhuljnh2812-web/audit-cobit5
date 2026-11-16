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
# CSS WEBSITE
# =====================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');

/* FONT */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* BACKGROUND UTAMA */
.stApp {
    background: linear-gradient(
        135deg,
        #FFF9FB 0%,
        #FCEAF0 35%,
        #F8DCE6 70%,
        #F1C6D6 100%
    ) !important;
    background-attachment: fixed !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: transparent !important;
}

/* HEADER */
[data-testid="stHeader"] {
    background: rgba(255, 249, 251, 0.85) !important;
}

/* JARAK KONTEN */
.block-container {
    padding-top: 4rem !important;
    padding-bottom: 3rem !important;
    max-width: 1500px;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #F9DCE6 0%,
        #F2C4D5 50%,
        #E9A9C1 100%
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
    font-size: 12px;
    letter-spacing: 2px;
    color: #80586B;
}

/* JUDUL UTAMA */
.main-title {
    font-family: 'Poppins', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #90566F;
    margin: 0 0 8px 0;
}

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
    margin-bottom: 12px;
}

/* KARTU RINGKASAN */
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
    margin-top: 8px;
    margin-bottom: 8px;
}

/* KARTU OBJEK AUDIT */
.object-card {
    background: linear-gradient(
        120deg,
        #FFF9FB 0%,
        #FCE4EC 50%,
        #F2C6D6 100%
    );
    border: 1px solid #EFC6D5;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 5px 18px rgba(174, 104, 133, 0.12);
    margin-top: 10px;
    margin-bottom: 20px;
}

.object-card h3 {
    color: #90566F;
    font-family: 'Poppins', sans-serif;
    font-size: 20px;
    margin-top: 0;
}

.object-card p,
.object-card li {
    color: #80586B;
    font-size: 15px;
    line-height: 1.8;
}

/* KARTU INFORMASI */
.notice-card {
    background: linear-gradient(
        120deg,
        #FFF9FB,
        #FCEAF0,
        #F5DCE5
    );
    border: 1px solid #EFC6D5;
    border-radius: 14px;
    padding: 20px;
    color: #80586B;
    line-height: 1.8;
}

/* KARTU DOMAIN */
.domain-card {
    background: linear-gradient(
        120deg,
        #FFFFFF,
        #FCEAF0
    );
    border: 1px solid #F1D1DE;
    padding: 15px 20px;
    border-radius: 12px;
    margin-bottom: 10px;
    color: #80586B;
}

.domain-code {
    color: #C47796;
    font-weight: 700;
    font-size: 17px;
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

/* RADIO SIDEBAR */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 8px;
}

/* PEMISAH */
hr {
    border-color: #EBCBD7;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .block-container {
        padding: 3rem 1rem 2rem 1rem !important;
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
# FUNGSI KARTU INFORMASI
# =====================================
def show_notice(title, description):

    st.markdown(f"""
    <div class="notice-card">
        <b>{title}</b>
        <p>{description}</p>
    </div>
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
# HALAMAN DASHBOARD
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

    # =================================
    # OBJEK AUDIT
    # =================================
    st.markdown(
        '<p class="section-title">Objek Audit</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="
        background: linear-gradient(
            120deg,
            #FFF9FB 0%,
            #FCE4EC 50%,
            #F2C6D6 100%
        );
        border: 1px solid #EFC6D5;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 5px 18px rgba(174, 104, 133, 0.12);
        margin-bottom: 20px;
    ">

        <h3 style="
            color: #90566F;
            font-family: Poppins, sans-serif;
            margin-top: 0;
        ">
            PT Muria Bangun Mandiri
        </h3>

        <p style="color: #80586B; line-height: 1.8;">
            <b>Objek evaluasi:</b><br>
            Aplikasi Persediaan dan Penjualan.
        </p>

        <p style="color: #80586B;">
            <b>Fokus evaluasi:</b>
        </p>

        <ul style="
            color: #80586B;
            line-height: 2;
        ">
            <li>Pengelolaan data persediaan.</li>
            <li>Pencatatan transaksi penjualan.</li>
            <li>Keamanan dan pengendalian sistem.</li>
            <li>Ketepatan informasi dan pelaporan.</li>
        </ul>

    </div>
    """, unsafe_allow_html=True)

    # =================================
    # DOMAIN COBIT 5
    # =================================
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

        st.markdown(f"""
        <div class="domain-card">
            <span class="domain-code">{kode}</span>
            <span> — {nama}</span>
        </div>
        """, unsafe_allow_html=True)


# =====================================
# HALAMAN PROFIL PERUSAHAAN
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

    st.subheader("PT Muria Bangun Mandiri")

    show_notice(
        "Informasi Perusahaan",
        "PT Muria Bangun Mandiri merupakan objek yang digunakan "
        "dalam evaluasi tata kelola teknologi informasi pada "
        "aplikasi persediaan dan penjualan."
    )

    st.write("")

    st.markdown("### Informasi Audit")

    col1, col2 = st.columns(2)

    with col1:
        show_notice(
            "Objek Audit",
            "Aplikasi Persediaan dan Penjualan."
        )

    with col2:
        show_notice(
            "Framework",
            "COBIT 5."
        )

    st.write("")

    show_notice(
        "Fokus Audit",
        "Evaluasi tata kelola dan pengelolaan teknologi informasi."
    )


# =====================================
# HALAMAN KUESIONER AUDIT
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

    show_notice(
        "Kuesioner Audit",
        "Halaman ini nantinya digunakan untuk mengisi "
        "30 pertanyaan evaluasi berdasarkan domain COBIT 5."
    )


# =====================================
# HALAMAN HASIL AUDIT
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

    show_notice(
        "Hasil Evaluasi",
        "Hasil audit akan ditampilkan setelah proses "
        "pengisian kuesioner selesai."
    )

    st.write("")

    show_notice(
        "Tingkat Kapabilitas",
        "Halaman ini nantinya menampilkan hasil penilaian "
        "tingkat kapabilitas berdasarkan domain COBIT 5."
    )


# =====================================
# HALAMAN REKOMENDASI
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

    show_notice(
        "Rekomendasi Perbaikan",
        "Halaman ini nantinya berisi saran perbaikan "
        "berdasarkan hasil penilaian audit untuk meningkatkan "
        "tata kelola teknologi informasi."
    )
