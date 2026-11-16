
import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Sistem Audit COBIT 5",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. DESAIN WEBSITE
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
        #FFF9FB,
        #FCEAF0,
        #F8DCE6
    );
}

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
        #F9DCE6,
        #F2C4D5
    );
}

/* Judul */
h1, h2, h3, h4 {
    color: #90566F;
    font-family: 'Poppins', sans-serif;
}

/* Teks */
p, label, li {
    color: #80586B;
}

/* Card informasi */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: rgba(255, 255, 255, 0.65);
    border-color: #F2C6D6;
    border-radius: 15px;
}

/* Tombol */
.stButton > button {
    background-color: #DFA6BC;
    color: white;
    border: none;
    border-radius: 9px;
    font-family: 'Poppins', sans-serif;
}

.stButton > button:hover {
    background-color: #C987A3;
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


# ==========================================
# 3. SESSION STATE
# ==========================================

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

if "hasil_kuesioner" not in st.session_state:
    st.session_state.hasil_kuesioner = []


# ==========================================
# 4. FUNGSI CARD
# ==========================================

def tampilkan_card(judul, deskripsi):

    with st.container(border=True):
        st.subheader(judul)
        st.write(deskripsi)


# ==========================================
# 5. SIDEBAR
# ==========================================

with st.sidebar:

    st.title("COBIT 5")
    st.caption("AUDIT SYSTEM")

    st.divider()

    daftar_menu = [
        "Dashboard",
        "Profil Perusahaan",
        "Kuesioner Audit",
        "Hasil Audit",
        "Rekomendasi"
    ]

    for item in daftar_menu:

        if st.button(
            item,
            key="menu_" + item,
            use_container_width=True
        ):
            st.session_state.menu = item
            st.rerun()

    st.divider()

    st.caption("Sistem Audit Berbasis COBIT 5")


# ==========================================
# 6. DASHBOARD
# ==========================================

if st.session_state.menu == "Dashboard":

    st.title("Dashboard Audit COBIT 5")

    st.write(
        "Sistem Evaluasi Aplikasi Persediaan dan Penjualan"
    )

    st.divider()

    # Ringkasan informasi
    kolom1, kolom2, kolom3 = st.columns(3)

    with kolom1:
        with st.container(border=True):
            st.caption("Standar Audit")
            st.subheader("COBIT 5")

    with kolom2:
        with st.container(border=True):
            st.caption("Objek Evaluasi")
            st.subheader("Aplikasi")

    with kolom3:
        with st.container(border=True):
            st.caption("Metode Evaluasi")
            st.subheader("Kuesioner")

    # Objek Audit
    st.markdown("### Objek Audit")

    with st.container(border=True):

        st.subheader("PT Muria Bangun Mandiri")

        st.markdown("**Objek evaluasi:**")

        st.write(
            "Aplikasi Persediaan dan Penjualan."
        )

        st.markdown("**Fokus evaluasi:**")

        st.markdown("""
        - Pengelolaan data persediaan.
        - Pencatatan transaksi penjualan.
        - Keamanan dan pengendalian sistem.
        - Ketepatan informasi dan pelaporan.
        """)

    # Domain COBIT
    st.markdown("### Domain COBIT 5")

    st.write(
        "Lima domain yang menjadi dasar evaluasi tata kelola teknologi informasi."
    )

    kolom1, kolom2, kolom3 = st.columns(3)

    with kolom1:
        with st.container(border=True):
            st.subheader("EDM")
            st.caption("Evaluate, Direct and Monitor")

    with kolom2:
        with st.container(border=True):
            st.subheader("APO")
            st.caption("Align, Plan and Organize")

    with kolom3:
        with st.container(border=True):
            st.subheader("BAI")
            st.caption("Build, Acquire and Implement")

    kolom4, kolom5 = st.columns(2)

    with kolom4:
        with st.container(border=True):
            st.subheader("DSS")
            st.caption("Deliver, Service and Support")

    with kolom5:
        with st.container(border=True):
            st.subheader("MEA")
            st.caption("Monitor, Evaluate and Assess")


# ==========================================
# 7. PROFIL PERUSAHAAN
# ==========================================

elif st.session_state.menu == "Profil Perusahaan":

    st.title("Profil Perusahaan")

    st.write(
        "Informasi perusahaan yang menjadi objek audit."
    )

    tampilkan_card(
        "PT Muria Bangun Mandiri",
        "Perusahaan yang menjadi objek evaluasi tata kelola teknologi informasi menggunakan kerangka kerja COBIT 5."
    )

    st.markdown("### Informasi Objek Audit")

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


# ==========================================
# 8. KUESIONER AUDIT
# ==========================================

elif st.session_state.menu == "Kuesioner Audit":

    st.title("Kuesioner Audit")

    st.write(
        "Pengisian kuesioner evaluasi Aplikasi Persediaan dan Penjualan."
    )

    tampilkan_card(
        "Petunjuk Pengisian",
        "Isi identitas responden dan pilih jawaban yang sesuai dengan kondisi penggunaan aplikasi."
    )

    st.markdown("### Identitas Responden")

    nama = st.text_input("Nama Responden")
    jabatan = st.text_input("Jabatan")

    st.markdown("### Pertanyaan Audit")

    pertanyaan = [
        "Data persediaan dikelola dengan baik.",
        "Transaksi penjualan dicatat secara akurat.",
        "Sistem memiliki pengamanan akses pengguna.",
        "Informasi yang dihasilkan sesuai kebutuhan.",
        "Laporan penjualan dapat diakses dengan mudah."
    ]

    pilihan = [
        "Sangat Tidak Setuju",
        "Tidak Setuju",
        "Netral",
        "Setuju",
        "Sangat Setuju"
    ]

    jawaban_responden = []

    for nomor, soal in enumerate(pertanyaan, start=1):

        st.markdown(f"**{nomor}. {soal}**")

        jawaban = st.radio(
            "Pilih jawaban:",
            pilihan,
            key=f"jawaban_{nomor}",
            horizontal=True
        )

        jawaban_responden.append(jawaban)

    if st.button("Simpan Jawaban"):

        if not nama.strip() or not jabatan.strip():

            st.warning(
                "Nama dan jabatan responden harus diisi."
            )

        elif nama.strip() and jabatan.strip():

            st.session_state.hasil_kuesioner.append({
                "nama": nama,
                "jabatan": jabatan,
                "jawaban": jawaban_responden
            })

            st.success(
                "Jawaban berhasil disimpan dalam sesi aplikasi."
            )


# ==========================================
# 9. HASIL AUDIT
# ==========================================

elif st.session_state.menu == "Hasil Audit":

    st.title("Hasil Audit")

    st.write(
        "Ringkasan hasil pengisian kuesioner."
    )

    jumlah = len(
        st.session_state.hasil_kuesioner
    )

    kolom1, kolom2 = st.columns(2)

    with kolom1:
        with st.container(border=True):
            st.caption("Jumlah Responden")
            st.subheader(str(jumlah))

    with kolom2:
        with st.container(border=True):
            st.caption("Status Pengisian")
            st.subheader(
                "Sudah Ada Data" if jumlah > 0 else "Belum Ada Data"
            )

    st.markdown("### Data Responden")

    if jumlah > 0:

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


# ==========================================
# 10. REKOMENDASI
# ==========================================

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


# ==========================================
# 11. FOOTER
# ==========================================

st.divider()

st.markdown(
    "<p style='text-align:center; color:#A77B8E; font-size:12px;'>"
    "Sistem Audit COBIT 5<br>"
    "Aplikasi Persediaan dan Penjualan<br>"
    "PT Muria Bangun Mandiri"
    "</p>",
    unsafe_allow_html=True
)
