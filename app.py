
import streamlit as st

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Sistem Audit COBIT 5",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# SESSION STATE
# ==========================================

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"


# ==========================================
# CSS / DESAIN
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #FFF9FB 0%,
        #FCEAF0 50%,
        #F8DCE6 100%
    );
}

/* Area utama */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

[data-testid="stMain"] {
    background: transparent;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #F9DCE6 0%,
        #F2C4D5 100%
    );
}

[data-testid="stSidebar"] * {
    color: #75475B;
    font-family: 'Poppins', sans-serif;
}

/* Judul */
h1, h2, h3 {
    color: #90566F;
    font-family: 'Poppins', sans-serif;
}

/* Paragraf */
p, label {
    color: #80586B;
    font-family: 'Poppins', sans-serif;
}

/* Card umum */
.info-card {
    background: rgba(255, 255, 255, 0.75);
    border: 1px solid #F2C6D6;
    border-radius: 15px;
    padding: 22px;
    box-shadow: 0 4px 12px rgba(144, 86, 111, 0.07);
    min-height: 115px;
}

.info-card h4 {
    color: #A66C85;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 10px;
}

.info-card h2 {
    color: #90566F;
    font-size: 25px;
    margin: 0;
}

/* Card Objek Audit */
.object-card {
    background: linear-gradient(
        135deg,
        #FFF5F8,
        #FCE4EC
    );
    border: 1px solid #F2C6D6;
    border-radius: 16px;
    padding: 28px 32px;
    box-shadow: 0 4px 12px rgba(144, 86, 111, 0.08);
    margin-top: 15px;
}

.object-card h3 {
    color: #90566F;
    font-size: 23px;
    margin-top: 0;
    margin-bottom: 20px;
}

.object-card p,
.object-card li {
    color: #80586B;
    font-size: 14px;
    line-height: 1.9;
}

.object-card ul {
    padding-left: 22px;
    margin-bottom: 0;
}

/* Card domain */
.domain-card {
    background: rgba(255, 255, 255, 0.75);
    border: 1px solid #F2C6D6;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    margin-bottom: 12px;
}

.domain-card h4 {
    color: #90566F;
    font-size: 15px;
    margin-bottom: 5px;
}

.domain-card p {
    color: #80586B;
    font-size: 12px;
    margin: 0;
}

/* Tombol */
.stButton > button {
    background-color: #DFA6BC;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 18px;
    font-family: 'Poppins', sans-serif;
}

.stButton > button:hover {
    background-color: #C987A3;
    color: white;
    border: none;
}

/* Input */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 9px;
}

hr {
    border-color: #EBC6D5;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR / MENU
# ==========================================

with st.sidebar:

    st.markdown("""
    <div style="padding: 15px 5px 25px 5px;">
        <h2 style="
            color: #90566F;
            font-size: 27px;
            margin-bottom: 0;
        ">
            COBIT 5
        </h2>

        <p style="
            color: #80586B;
            font-size: 12px;
            letter-spacing: 2px;
            margin-top: 3px;
        ">
            AUDIT SYSTEM
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    menu_list = [
        "Dashboard",
        "Profil Perusahaan",
        "Kuesioner Audit",
        "Hasil Audit",
        "Rekomendasi"
    ]

    for item in menu_list:
        if st.button(
            item,
            key="menu_" + item,
            use_container_width=True
        ):
            st.session_state.menu = item
            st.rerun()

    st.markdown("---")

    st.markdown("""
    <p style="
        font-size: 11px;
        text-align: center;
        color: #80586B;
    ">
        Sistem Audit Berbasis COBIT 5
    </p>
    """, unsafe_allow_html=True)


# ==========================================
# FUNGSI CARD INFORMASI
# ==========================================

def show_notice(title, description):

    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.75);
        border: 1px solid #F2C6D6;
        border-radius: 15px;
        padding: 25px;
        margin-top: 15px;
    ">
        <h3 style="
            color: #90566F;
            margin-top: 0;
        ">
            {title}
        </h3>

        <p style="
            color: #80586B;
            line-height: 1.8;
            margin-bottom: 0;
        ">
            {description}
        </p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# DASHBOARD
# ==========================================

if st.session_state.menu == "Dashboard":

    st.title("Dashboard Audit COBIT 5")

    st.markdown("""
    <p style="
        color: #80586B;
        font-size: 15px;
        margin-top: -10px;
    ">
        Sistem Evaluasi Aplikasi Persediaan dan Penjualan
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Ringkasan informasi
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>Standar Audit</h4>
            <h2>COBIT 5</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>Objek Evaluasi</h4>
            <h2>Aplikasi</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
            <h4>Metode Evaluasi</h4>
            <h2>Kuesioner</h2>
        </div>
        """, unsafe_allow_html=True)

    # Objek Audit
    st.markdown("""
    <div class="object-card">

        <h3>PT Muria Bangun Mandiri</h3>

        <p>
            <b>Objek evaluasi:</b><br>
            Aplikasi Persediaan dan Penjualan.
        </p>

        <p>
            <b>Fokus evaluasi:</b>
        </p>

        <ul>
            <li>Pengelolaan data persediaan.</li>
            <li>Pencatatan transaksi penjualan.</li>
            <li>Keamanan dan pengendalian sistem.</li>
            <li>Ketepatan informasi dan pelaporan.</li>
        </ul>

    </div>
    """, unsafe_allow_html=True)

    # Domain COBIT 5
    st.markdown("### Domain COBIT 5")

    st.markdown("""
    <p style="color:#80586B;">
        Lima domain COBIT 5 yang menjadi dasar evaluasi tata kelola TI.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="domain-card">
            <h4>EDM</h4>
            <p>Evaluate, Direct and Monitor</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="domain-card">
            <h4>APO</h4>
            <p>Align, Plan and Organize</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="domain-card">
            <h4>BAI</h4>
            <p>Build, Acquire and Implement</p>
        </div>
        """, unsafe_allow_html=True)

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("""
        <div class="domain-card">
            <h4>DSS</h4>
            <p>Deliver, Service and Support</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="domain-card">
            <h4>MEA</h4>
            <p>Monitor, Evaluate and Assess</p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# PROFIL PERUSAHAAN
# ==========================================

elif st.session_state.menu == "Profil Perusahaan":

    st.title("Profil Perusahaan")

    st.markdown("""
    <p style="color:#80586B;">
        Informasi mengenai perusahaan yang menjadi objek audit.
    </p>
    """, unsafe_allow_html=True)

    show_notice(
        "PT Muria Bangun Mandiri",
        "PT Muria Bangun Mandiri merupakan perusahaan yang menjadi objek evaluasi dalam kegiatan audit tata kelola teknologi informasi menggunakan kerangka kerja COBIT 5."
    )

    st.markdown("### Informasi Objek Audit")

    col1, col2 = st.columns(2)

    with col1:
        show_notice(
            "Nama Perusahaan",
            "PT Muria Bangun Mandiri"
        )

    with col2:
        show_notice(
            "Sistem yang Dievaluasi",
            "Aplikasi Persediaan dan Penjualan"
        )


# ==========================================
# KUESIONER AUDIT
# ==========================================

elif st.session_state.menu == "Kuesioner Audit":

    st.title("Kuesioner Audit")

    st.markdown("""
    <p style="color:#80586B;">
        Halaman pengisian kuesioner evaluasi aplikasi.
    </p>
    """, unsafe_allow_html=True)

    show_notice(
        "Petunjuk Pengisian",
        "Kuesioner digunakan untuk mengetahui tingkat penerapan tata kelola teknologi informasi pada Aplikasi Persediaan dan Penjualan PT Muria Bangun Mandiri."
    )

    st.markdown("### Identitas Responden")

    nama = st.text_input("Nama Responden")
    jabatan = st.text_input("Jabatan")

    st.markdown("### Pertanyaan Audit")

    pertanyaan = [
        "Apakah data persediaan telah dikelola dengan baik?",
        "Apakah transaksi penjualan dicatat secara akurat?",
        "Apakah sistem memiliki pengamanan terhadap akses pengguna?",
        "Apakah informasi yang dihasilkan sistem sesuai kebutuhan?",
        "Apakah laporan penjualan dapat diakses dengan mudah?"
    ]

    jawaban = []

    for i, soal in enumerate(pertanyaan):
        st.markdown(f"**{i+1}. {soal}**")

        nilai = st.selectbox(
            "Pilih jawaban",
            [
                "Pilih jawaban",
                "Sangat Tidak Setuju",
                "Tidak Setuju",
                "Netral",
                "Setuju",
                "Sangat Setuju"
            ],
            key=f"jawaban_{i}"
        )

        jawaban.append(nilai)

    if st.button("Simpan Jawaban"):

        if not nama or not jabatan:
            st.warning("Silakan lengkapi nama dan jabatan responden.")

        elif "Pilih jawaban" in jawaban:
            st.warning("Silakan jawab seluruh pertanyaan.")

        else:
            st.success("Jawaban berhasil diproses pada sesi ini.")


# ==========================================
# HASIL AUDIT
# ==========================================

elif st.session_state.menu == "Hasil Audit":

    st.title("Hasil Audit")

    st.markdown("""
    <p style="color:#80586B;">
        Halaman untuk menampilkan hasil evaluasi audit COBIT 5.
    </p>
    """, unsafe_allow_html=True)

    show_notice(
        "Informasi Hasil Audit",
        "Hasil audit akan ditampilkan berdasarkan pengolahan jawaban kuesioner dan penilaian tingkat kapabilitas proses COBIT 5."
    )

    st.markdown("### Ringkasan Hasil")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>Jumlah Responden</h4>
            <h2>0</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>Status Audit</h4>
            <h2>Belum Dinilai</h2>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# REKOMENDASI
# ==========================================

elif st.session_state.menu == "Rekomendasi":

    st.title("Rekomendasi Perbaikan")

    st.markdown("""
    <p style="color:#80586B;">
        Rekomendasi berdasarkan hasil evaluasi tata kelola teknologi informasi.
    </p>
    """, unsafe_allow_html=True)

    show_notice(
        "Rekomendasi Audit",
        "Rekomendasi perbaikan akan disusun berdasarkan hasil pengukuran tingkat kapabilitas dan temuan audit pada Aplikasi Persediaan dan Penjualan."
    )

    st.markdown("### Fokus Rekomendasi")

    rekomendasi = [
        (
            "Pengelolaan Persediaan",
            "Meningkatkan ketepatan pencatatan stok dan melakukan pembaruan data persediaan secara berkala."
        ),
        (
            "Transaksi Penjualan",
            "Memastikan setiap transaksi penjualan tercatat secara lengkap, akurat, dan terdokumentasi."
        ),
        (
            "Keamanan Sistem",
            "Menerapkan pengaturan hak akses pengguna dan perlindungan terhadap data perusahaan."
        ),
        (
            "Pelaporan",
            "Meningkatkan kualitas laporan agar informasi yang dihasilkan akurat dan mudah dipahami."
        )
    ]

    for judul, isi in rekomendasi:
        show_notice(judul, isi)


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<p style="
    color: #A77B8E;
    font-size: 12px;
    text-align: center;
    padding: 10px;
">
    Sistem Audit COBIT 5 | Aplikasi Persediaan dan Penjualan
    <br>
    PT Muria Bangun Mandiri
</p>
""", unsafe_allow_html=True)
