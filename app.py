
import streamlit as st

# =====================================
# 1. KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Sistem Audit COBIT 5",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# 2. DESAIN WEBSITE
# =====================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #FFF9FB, #FCEAF0, #F8DCE6);
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: transparent;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #F9DCE6, #F2C4D5);
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

/* Teks */
p, label {
    color: #80586B;
}

/* Card */
.audit-card {
    background: linear-gradient(135deg, #FFF5F8, #FCE4EC);
    border: 1px solid #F2C6D6;
    border-radius: 16px;
    padding: 25px 30px;
    margin: 15px 0;
    box-shadow: 0 4px 12px rgba(144, 86, 111, 0.08);
}

.audit-card h3 {
    color: #90566F;
    margin-top: 0;
    font-size: 22px;
}

.audit-card p,
.audit-card li {
    color: #80586B;
    font-size: 14px;
    line-height: 1.9;
}

.audit-card ul {
    padding-left: 22px;
}

.info-card {
    background: rgba(255,255,255,0.75);
    border: 1px solid #F2C6D6;
    border-radius: 14px;
    padding: 22px;
    min-height: 115px;
    box-shadow: 0 4px 12px rgba(144, 86, 111, 0.06);
}

.info-card p {
    font-size: 13px;
    margin-bottom: 8px;
    color: #A66C85;
}

.info-card h3 {
    margin: 0;
    font-size: 22px;
}

.domain-card {
    background: rgba(255,255,255,0.75);
    border: 1px solid #F2C6D6;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    margin-bottom: 12px;
}

.domain-card h4 {
    color: #90566F;
    margin: 0 0 7px 0;
}

.domain-card p {
    font-size: 12px;
    margin: 0;
}

/* Tombol */
.stButton > button {
    background: #DFA6BC;
    color: white;
    border: none;
    border-radius: 9px;
    font-family: 'Poppins', sans-serif;
}

.stButton > button:hover {
    background: #C987A3;
    color: white;
    border: none;
}

/* Input */
.stTextInput input,
.stTextArea textarea {
    border-radius: 9px;
}

hr {
    border-color: #EBC6D5;
}
</style>
""", unsafe_allow_html=True)


# =====================================
# 3. SESSION STATE
# =====================================

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

if "hasil_kuesioner" not in st.session_state:
    st.session_state.hasil_kuesioner = []


# =====================================
# 4. FUNGSI CARD
# =====================================

def tampilkan_card(judul, isi):
    st.markdown(
        f"""
        <div class="audit-card">
            <h3>{judul}</h3>
            <p>{isi}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================
# 5. SIDEBAR
# =====================================

with st.sidebar:

    st.markdown("""
    <div style="padding: 15px 5px 20px 5px;">
        <h2 style="color:#90566F; margin-bottom:0;">
            COBIT 5
        </h2>
        <p style="font-size:12px; letter-spacing:2px;">
            AUDIT SYSTEM
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    daftar_menu = [
        "Dashboard",
        "Profil Perusahaan",
        "Kuesioner Audit",
        "Hasil Audit",
        "Rekomendasi"
    ]

    for menu_item in daftar_menu:
        if st.button(
            menu_item,
            key="pilih_" + menu_item,
            use_container_width=True
        ):
            st.session_state.menu = menu_item
            st.rerun()

    st.markdown("---")

    st.caption("Sistem Audit Berbasis COBIT 5")


# =====================================
# 6. HALAMAN DASHBOARD
# =====================================

if st.session_state.menu == "Dashboard":

    st.title("Dashboard Audit COBIT 5")

    st.write(
        "Sistem Evaluasi Aplikasi Persediaan dan Penjualan"
    )

    st.divider()

    kolom1, kolom2, kolom3 = st.columns(3)

    with kolom1:
        st.markdown("""
        <div class="info-card">
            <p>Standar Audit</p>
            <h3>COBIT 5</h3>
        </div>
        """, unsafe_allow_html=True)

    with kolom2:
        st.markdown("""
        <div class="info-card">
            <p>Objek Evaluasi</p>
            <h3>Aplikasi</h3>
        </div>
        """, unsafe_allow_html=True)

    with kolom3:
        st.markdown("""
        <div class="info-card">
            <p>Metode Evaluasi</p>
            <h3>Kuesioner</h3>
        </div>
        """, unsafe_allow_html=True)

    # Objek Audit
    st.markdown("""
    <div class="audit-card">
        <h3>PT Muria Bangun Mandiri</h3>

        <p>
            <b>Objek evaluasi:</b><br>
            Aplikasi Persediaan dan Penjualan.
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

    st.subheader("Domain COBIT 5")

    st.write(
        "Lima domain yang digunakan sebagai dasar evaluasi."
    )

    domain1, domain2, domain3 = st.columns(3)

    with domain1:
        st.markdown("""
        <div class="domain-card">
            <h4>EDM</h4>
            <p>Evaluate, Direct and Monitor</p>
        </div>
        """, unsafe_allow_html=True)

    with domain2:
        st.markdown("""
        <div class="domain-card">
            <h4>APO</h4>
            <p>Align, Plan and Organize</p>
        </div>
        """, unsafe_allow_html=True)

    with domain3:
        st.markdown("""
        <div class="domain-card">
            <h4>BAI</h4>
            <p>Build, Acquire and Implement</p>
        </div>
        """, unsafe_allow_html=True)

    domain4, domain5 = st.columns(2)

    with domain4:
        st.markdown("""
        <div class="domain-card">
            <h4>DSS</h4>
            <p>Deliver, Service and Support</p>
        </div>
        """, unsafe_allow_html=True)

    with domain5:
        st.markdown("""
        <div class="domain-card">
            <h4>MEA</h4>
            <p>Monitor, Evaluate and Assess</p>
        </div>
        """, unsafe_allow_html=True)


# =====================================
# 7. HALAMAN PROFIL PERUSAHAAN
# =====================================

elif st.session_state.menu == "Profil Perusahaan":

    st.title("Profil Perusahaan")

    st.write(
        "Informasi perusahaan yang menjadi objek audit."
    )

    tampilkan_card(
        "PT Muria Bangun Mandiri",
        "Perusahaan yang menjadi objek evaluasi tata kelola teknologi informasi menggunakan kerangka kerja COBIT 5."
    )

    st.subheader("Informasi Objek Audit")

    kolom1, kolom2 = st.columns(2)

    with kolom1:
        tampilkan_card(
            "Nama Perusahaan",
            "PT Muria Bangun Mandiri"
        )

    with kolom2:
        tampilkan_card(
            "Sistem yang Dievaluasi",
            "Aplikasi Persediaan dan Penjualan"
        )


# =====================================
# 8. HALAMAN KUESIONER AUDIT
# =====================================

elif st.session_state.menu == "Kuesioner Audit":

    st.title("Kuesioner Audit")

    st.write(
        "Pengisian kuesioner evaluasi Aplikasi Persediaan dan Penjualan."
    )

    tampilkan_card(
        "Petunjuk Pengisian",
        "Isi identitas responden dan pilih jawaban yang sesuai dengan kondisi penggunaan aplikasi."
    )

    st.subheader("Identitas Responden")

    nama = st.text_input("Nama Responden")
    jabatan = st.text_input("Jabatan")

    st.subheader("Pertanyaan Audit")

    daftar_pertanyaan = [
        "Data persediaan dikelola dengan baik.",
        "Transaksi penjualan dicatat secara akurat.",
        "Sistem memiliki pengamanan akses pengguna.",
        "Informasi yang dihasilkan sesuai kebutuhan.",
        "Laporan penjualan dapat diakses dengan mudah."
    ]

    pilihan_jawaban = [
        "Sangat Tidak Setuju",
        "Tidak Setuju",
        "Netral",
        "Setuju",
        "Sangat Setuju"
    ]

    jawaban_responden = []

    for nomor, pertanyaan in enumerate(daftar_pertanyaan, start=1):

        st.markdown(f"**{nomor}. {pertanyaan}**")

        jawaban = st.radio(
            "Pilih jawaban:",
            pilihan_jawaban,
            key=f"pertanyaan_{nomor}",
            horizontal=True
        )

        jawaban_responden.append(jawaban)

    if st.button("Simpan Jawaban"):

        if not nama.strip() or not jabatan.strip():

            st.warning(
                "Nama dan jabatan responden harus diisi."
            )

        else:

            st.session_state.hasil_kuesioner.append({
                "nama": nama,
                "jabatan": jabatan,
                "jawaban": jawaban_responden
            })

            st.success(
                "Jawaban berhasil disimpan dalam sesi aplikasi."
            )


# =====================================
# 9. HALAMAN HASIL AUDIT
# =====================================

elif st.session_state.menu == "Hasil Audit":

    st.title("Hasil Audit")

    st.write(
        "Ringkasan hasil pengisian kuesioner audit."
    )

    jumlah_responden = len(
        st.session_state.hasil_kuesioner
    )

    kolom1, kolom2 = st.columns(2)

    with kolom1:
        st.markdown(f"""
        <div class="info-card">
            <p>Jumlah Responden</p>
            <h3>{jumlah_responden}</h3>
        </div>
        """, unsafe_allow_html=True)

    with kolom2:
        status = "Sudah Ada Data" if jumlah_responden > 0 else "Belum Ada Data"

        st.markdown(f"""
        <div class="info-card">
            <p>Status Pengisian</p>
            <h3>{status}</h3>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Data Responden")

    if jumlah_responden > 0:

        for nomor, data in enumerate(
            st.session_state.hasil_kuesioner,
            start=1
        ):

            with st.expander(
                f"Responden {nomor}: {data['nama']}"
            ):

                st.write("Jabatan:", data["jabatan"])

                for i, jawaban in enumerate(
                    data["jawaban"],
                    start=1
                ):
                    st.write(
                        f"Pertanyaan {i}: {jawaban}"
                    )

    else:

        st.info(
            "Belum ada jawaban kuesioner yang tersimpan."
        )


# =====================================
# 10. HALAMAN REKOMENDASI
# =====================================

elif st.session_state.menu == "Rekomendasi":

    st.title("Rekomendasi Perbaikan")

    st.write(
        "Fokus rekomendasi untuk meningkatkan kualitas sistem."
    )

    tampilkan_card(
        "Pengelolaan Persediaan",
        "Meningkatkan ketepatan pencatatan stok dan melakukan pembaruan data persediaan secara berkala."
    )

    tampilkan_card(
        "Transaksi Penjualan",
        "Memastikan setiap transaksi penjualan tercatat secara lengkap, akurat, dan terdokumentasi."
    )

    tampilkan_card(
        "Keamanan Sistem",
        "Menerapkan pengaturan hak akses pengguna dan perlindungan terhadap data perusahaan."
    )

    tampilkan_card(
        "Pelaporan",
        "Meningkatkan kualitas laporan agar informasi yang dihasilkan akurat dan mudah dipahami."
    )


# =====================================
# 11. FOOTER
# =====================================

st.divider()

st.markdown("""
<p style="
    text-align:center;
    color:#A77B8E;
    font-size:12px;
">
    Sistem Audit COBIT 5<br>
    Aplikasi Persediaan dan Penjualan<br>
    PT Muria Bangun Mandiri
</p>
""", unsafe_allow_html=True)
