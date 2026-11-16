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

/* FONT */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* BACKGROUND UTAMA */
.stApp {
    background: linear-gradient(
        135deg,
        #FFF8FA 0%,
        #FCEAF0 50%,
        #F8DCE6 100%
    );
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #F4C9D7 0%,
        #EFB8CA 55%,
        #E8A5BC 100%
    );
}

[data-testid="stSidebar"] * {
    color: #70465A;
}

/* JUDUL */
.main-title {
    font-family: 'Poppins', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #8B526B;
}

.subtitle {
    color: #A47B8C;
    font-size: 15px;
}

/* KARTU DASHBOARD */
.info-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #FFF0F5 100%
    );
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #F2D5DF;
    box-shadow: 0 4px 15px rgba(190, 120, 150, 0.10);
    min-height: 125px;
}

.info-label {
    color: #987586;
    font-size: 14px;
}

.info-value {
    color: #C47796;
    font-size: 27px;
    font-weight: bold;
}

.section-title {
    font-family: 'Poppins', sans-serif;
    color: #8B526B;
    font-size: 22px;
    font-weight: bold;
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
    padding: 8px 20px;
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
    background: #FFF0F5;
    border: 1px solid #F2D5DF;
    border-radius: 12px;
}

/* PEMISAH */
hr {
    border-color: #EBCBD7;
}

/* RADIO MENU SIDEBAR */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 8px;
}

/* JARAK KONTEN */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# SIDEBAR
# =====================================
with st.sidebar:

    st.markdown(
        """
        <h1 style="
            font-family: Poppins;
            color: #70465A;
            font-size: 30px;
            margin-bottom: 0;
        ">
            COBIT 5
        </h1>
        <p style="
            color: #80586B;
            font-size: 13px;
            letter-spacing: 2px;
            margin-top: 0;
        ">
            AUDIT SYSTEM
        </p>
        """,
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

    # OBJEK AUDIT
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

    # DOMAIN COBIT
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

    st.subheader("PT Muria Bangun Mandiri")

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

    st.info("Hasil audit akan ditampilkan setelah proses pengisian kuesioner selesai.")

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

    st.info("Rekomendasi audit akan ditampilkan berdasarkan hasil penilaian.")

    st.write("""
    Halaman ini nantinya berisi saran perbaikan
    untuk meningkatkan tata kelola teknologi informasi
    pada aplikasi persediaan dan penjualan.
    """)
