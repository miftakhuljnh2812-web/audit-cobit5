import streamlit as st

# ==================================================
# 1. KONFIGURASI
# ==================================================

st.set_page_config(
    page_title="Sistem Audit COBIT 5",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# 2. DATA PERTANYAAN AUDIT SESUAI PDF
# ==================================================

daftar_domain = {
    "EDM": {
        "nama": "Evaluate, Direct and Monitor",
        "pertanyaan": [
            ("EDM01", "Apakah pimpinan melakukan evaluasi berkala terhadap proses pencatatan persediaan barang dagang dan penjualan?"),
            ("EDM01", "Apakah peran, tanggung jawab, dan wewenang pengambilan keputusan atas data stok dan penjualan (pimpinan, gudang, penjualan, keuangan) telah ditetapkan secara tertulis?"),
            ("EDM02", "Apakah pimpinan mengevaluasi manfaat informasi bagi usaha, misalnya ketersediaan stok untuk memenuhi pesanan pada musim pembangunan dan berkurangnya barang kosong atau barang lambat laku?"),
            ("EDM03", "Apakah pimpinan telah menetapkan batas risiko yang dapat diterima, misalnya untuk selisih stok, barang rusak atau hilang, dan kebocoran data harga atau data pelanggan?"),
            ("EDM04", "Apakah pimpinan menyediakan sumber daya yang memadai (pegawai, anggaran, dan sarana pencatatan) untuk pengelolaan data persediaan dan penjualan?"),
            ("EDM05", "Apakah laporan persediaan dan penjualan disampaikan secara berkala kepada pimpinan?")
        ]
    },
    "APO": {
        "nama": "Align, Plan and Organise",
        "pertanyaan": [
            ("APO01", "Apakah perusahaan memiliki prosedur tertulis (SOP) untuk penerimaan dan pengeluaran barang di gudang, stok opname, dan penjualan?"),
            ("APO01", "Apakah prosedur tersebut telah disosialisasikan kepada bagian gudang, penjualan, dan keuangan?"),
            ("APO02", "Apakah target penjualan dan kebutuhan stok barang dagang disusun berdasarkan data stok dan pola penjualan, serta dimuat dalam rencana kerja dan anggaran tahunan?"),
            ("APO07", "Apakah pegawai yang mengelola data stok dan penjualan memperoleh pelatihan atau pembekalan yang sesuai dengan tugasnya?"),
            ("APO12", "Apakah risiko pada proses ini telah diidentifikasi dan didokumentasikan, misalnya selisih stok, barang rusak atau hilang, kesalahan harga, pesanan yang tidak terpenuhi, dan kesalahan pencatatan?"),
            ("APO13", "Apakah terdapat kebijakan tertulis tentang keamanan informasi yang mencakup data harga, data pelanggan dan mitra penjual, serta data keuangan?")
        ]
    },
    "BAI": {
        "nama": "Build, Acquire and Implement",
        "pertanyaan": [
            ("BAI02", "Apakah kebutuhan informasi dari bagian gudang, penjualan, dan keuangan telah diidentifikasi dan didokumentasikan?"),
            ("BAI04", "Apakah perusahaan memeriksa kecukupan kapasitas sarana pencatatan terhadap volume stok dan transaksi penjualan, terutama pada masa permintaan tinggi?"),
            ("BAI06", "Apakah setiap perubahan pada sarana pencatatan (format pencatatan, aplikasi, atau daftar harga) disetujui pihak berwenang dan dicatat?"),
            ("BAI07", "Apakah sistem, aplikasi, atau perubahan pada aplikasi atau spreadsheet pencatatan stok dan penjualan diuji sebelum digunakan, dan data lama dipindahkan dengan benar?"),
            ("BAI08", "Apakah tersedia panduan atau dokumentasi kerja sehingga pencatatan tidak bergantung pada satu orang saja?"),
            ("BAI09", "Apakah aset pendukung (komputer, timbangan, printer label, perangkat gudang) telah dicatat dan dipelihara secara berkala?")
        ]
    },
    "DSS": {
        "nama": "Deliver, Service and Support",
        "pertanyaan": [
            ("DSS01", "Apakah penerimaan barang dari pemasok, serta barang keluar gudang untuk penjualan, dicatat tepat waktu sesuai prosedur?"),
            ("DSS02", "Apakah gangguan atau kesalahan pencatatan (misalnya aplikasi error atau selisih data) dicatat, ditangani, dan memiliki penanggung jawab?"),
            ("DSS04", "Apakah data persediaan dan penjualan dicadangkan secara berkala dan pernah diuji pemulihannya?"),
            ("DSS05", "Apakah hak akses ke data dan dokumen (termasuk harga, data pelanggan, dan data keuangan) diberikan sesuai tugas dan dicabut ketika pegawai berpindah atau keluar?"),
            ("DSS06", "Apakah tugas penerimaan barang, penyimpanan, pencatatan stok, penjualan, dan penerimaan pembayaran dipisahkan sehingga tidak dikuasai satu orang?"),
            ("DSS06", "Apakah setiap barang memiliki kode dan satuan yang konsisten, dan setiap barang keluar dicatat dengan nomor faktur atau surat jalan sehingga dapat ditelusuri apabila ada selisih atau keluhan pelanggan?")
        ]
    },
    "MEA": {
        "nama": "Monitor, Evaluate and Assess",
        "pertanyaan": [
            ("MEA01", "Apakah perusahaan menetapkan indikator kinerja, misalnya akurasi stok dan frekuensi barang kosong, serta memantaunya?"),
            ("MEA01", "Apakah realisasi penjualan dibandingkan dengan target dan data stok, dan selisihnya dianalisis?"),
            ("MEA02", "Apakah stok opname barang dagang dilakukan secara berkala dan selisihnya diselidiki serta disesuaikan dengan persetujuan?"),
            ("MEA02", "Apakah terdapat fungsi pengawas atau pemeriksaan internal yang menilai pengendalian pada proses persediaan dan penjualan?"),
            ("MEA02", "Apakah temuan pemeriksaan dan keluhan pelanggan ditindaklanjuti dan statusnya dipantau sampai selesai?"),
            ("MEA03", "Apakah perusahaan memantau kepatuhan terhadap ketentuan eksternal, misalnya perizinan usaha, perpajakan, dan ketentuan perlindungan konsumen?")
        ]
    }
}

pilihan_jawaban = ["Pilih jawaban", "Ya", "Sebagian", "Tidak", "N/A"]

# ==================================================
# 3. SESSION STATE
# ==================================================

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

if "hasil_audit" not in st.session_state:
    st.session_state.hasil_audit = []

# ==================================================
# 4. DESAIN WEBSITE
# ==================================================

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

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #F9DCE6, #F2C4D5);
}

h1, h2, h3, h4 {
    color: #90566F;
    font-family: 'Poppins', sans-serif;
}

p, label {
    color: #80586B;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.65);
    border-color: #F2C6D6;
    border-radius: 14px;
}

.stButton > button,
.stFormSubmitButton > button {
    background-color: #DFA6BC;
    color: white;
    border: none;
    border-radius: 9px;
    font-family: 'Poppins', sans-serif;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #C987A3;
    color: white;
    border: none;
}

.stTextInput input,
.stTextArea textarea {
    border-radius: 9px;
}

hr {
    border-color: #EBC6D5;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# 5. FUNGSI CARD
# ==================================================

def tampilkan_card(judul, deskripsi):
    with st.container(border=True):
        st.subheader(judul)
        st.write(deskripsi)


# ==================================================
# 6. SIDEBAR
# ==================================================

with st.sidebar:
    st.title("COBIT 5")
    st.caption("AUDIT SYSTEM")
    st.divider()

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

    st.divider()
    st.caption("Sistem Audit Berbasis COBIT 5")


# ==================================================
# 7. DASHBOARD
# ==================================================

if st.session_state.menu == "Dashboard":
    st.title("Dashboard Audit COBIT 5")
    st.write("Sistem Evaluasi Aplikasi Persediaan dan Penjualan")
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.caption("Standar Audit")
            st.subheader("COBIT 5")

    with col2:
        with st.container(border=True):
            st.caption("Objek Evaluasi")
            st.subheader("Aplikasi")

    with col3:
        with st.container(border=True):
            st.caption("Jumlah Pertanyaan")
            st.subheader("30 Pertanyaan")

    st.markdown("### Objek Audit")

    with st.container(border=True):
        st.subheader("PT Muria Bangun Mandiri")
        st.markdown("**Objek evaluasi:**")
        st.write("Aplikasi Persediaan dan Penjualan.")
        st.markdown("**Fokus evaluasi:**")
        st.markdown("""
        - Pengelolaan data persediaan.
        - Pencatatan transaksi penjualan.
        - Keamanan dan pengendalian sistem.
        - Ketepatan informasi dan pelaporan.
        """)

    st.markdown("### Domain COBIT 5")
    st.write("Evaluasi dilakukan berdasarkan lima domain COBIT 5.")

    col1, col2, col3 = st.columns(3)
    with col1:
        tampilkan_card("EDM", "Evaluate, Direct and Monitor")
    with col2:
        tampilkan_card("APO", "Align, Plan and Organise")
    with col3:
        tampilkan_card("BAI", "Build, Acquire and Implement")

    col4, col5 = st.columns(2)
    with col4:
        tampilkan_card("DSS", "Deliver, Service and Support")
    with col5:
        tampilkan_card("MEA", "Monitor, Evaluate and Assess")


# ==================================================
# 8. PROFIL PERUSAHAAN
# ==================================================

elif st.session_state.menu == "Profil Perusahaan":
    st.title("Profil Perusahaan")
    st.write("Informasi perusahaan yang menjadi objek audit.")

    tampilkan_card(
        "PT Muria Bangun Mandiri",
        "PT Muria Bangun Mandiri merupakan objek evaluasi tata kelola teknologi informasi menggunakan kerangka kerja COBIT 5."
    )

    st.markdown("### Informasi Objek Audit")
    col1, col2 = st.columns(2)

    with col1:
        tampilkan_card("Nama Perusahaan", "PT Muria Bangun Mandiri")

    with col2:
        tampilkan_card(
            "Sistem yang Dievaluasi",
            "Aplikasi Persediaan dan Penjualan"
        )


# ==================================================
# 9. KUESIONER AUDIT - 30 PERTANYAAN
# ==================================================

elif st.session_state.menu == "Kuesioner Audit":
    st.title("Kuesioner Audit COBIT 5")
    st.write(
        "Form Audit Sistem Informasi Persediaan dan Penjualan "
        "PT Muria Bangun Mandiri."
    )

    st.info(
        "Terdapat 30 pertanyaan yang terbagi ke dalam lima domain COBIT 5. "
        "Pilih jawaban berdasarkan hasil pemeriksaan dan bukti yang tersedia."
    )

    with st.form("form_audit"):
        st.markdown("### Identitas Audit")
        nama_auditor = st.text_input("Nama Auditor")
        nama_responden = st.text_input("Nama Responden")
        bagian = st.text_input("Bagian / Unit Kerja")

        st.divider()

        jawaban_audit = []
        nomor = 1

        for kode_domain, data_domain in daftar_domain.items():
            st.markdown(f"## {kode_domain} - {data_domain['nama']}")
            st.caption("6 pertanyaan audit")

            for kode_proses, pertanyaan in data_domain["pertanyaan"]:
                st.markdown(f"**Pertanyaan {nomor} | {kode_proses}**")
                st.write(pertanyaan)

                jawaban = st.selectbox(
                    "Jawaban",
                    pilihan_jawaban,
                    index=0,
                    key=f"jawaban_{nomor}"
                )

                bukti = st.text_input(
                    "Bukti Pendukung",
                    key=f"bukti_{nomor}",
                    placeholder="Masukkan dokumen, catatan, atau bukti pemeriksaan"
                )

                catatan = st.text_area(
                    "Catatan Auditor",
                    key=f"catatan_area_{nomor}",
                    placeholder="Tuliskan hasil pemeriksaan",
                    height=80
                )

                jawaban_audit.append({
                    "nomor": nomor,
                    "domain": kode_domain,
                    "kode": kode_proses,
                    "pertanyaan": pertanyaan,
                    "jawaban": jawaban,
                    "bukti": bukti,
                    "catatan": catatan
                })

                st.divider()
                nomor += 1

        simpan = st.form_submit_button(
            "Simpan Hasil Audit",
            use_container_width=True
        )

    if simpan:
        if not nama_auditor.strip() or not nama_responden.strip():
            st.warning("Nama auditor dan nama responden wajib diisi.")
        elif any(item["jawaban"] == "Pilih jawaban" for item in jawaban_audit):
            st.warning("Semua 30 pertanyaan harus diberi jawaban sebelum disimpan.")
        else:
            data_baru = {
                "nama_auditor": nama_auditor.strip(),
                "nama_responden": nama_responden.strip(),
                "bagian": bagian.strip(),
                "jawaban": jawaban_audit
            }

            st.session_state.hasil_audit.append(data_baru)
            st.success("30 jawaban audit berhasil disimpan dalam sesi aplikasi.")


# ==================================================
# 10. HASIL AUDIT
# ==================================================

elif st.session_state.menu == "Hasil Audit":
    st.title("Hasil Audit")
    st.write("Rekapitulasi jawaban audit berdasarkan lima domain COBIT 5.")

    if len(st.session_state.hasil_audit) == 0:
        st.info("Belum ada data audit. Silakan isi kuesioner terlebih dahulu.")
    else:
        for nomor_audit, data in enumerate(st.session_state.hasil_audit, start=1):
            st.markdown(f"## Hasil Audit {nomor_audit}")
            st.write(f"**Auditor:** {data['nama_auditor']}")
            st.write(f"**Responden:** {data['nama_responden']}")
            st.write(f"**Bagian:** {data['bagian'] or '-'}")

            rekap = []

            for kode_domain in daftar_domain:
                jawaban_domain = [
                    item for item in data["jawaban"]
                    if item["domain"] == kode_domain
                ]

                rekap.append({
                    "Domain": kode_domain,
                    "Ya": sum(item["jawaban"] == "Ya" for item in jawaban_domain),
                    "Sebagian": sum(item["jawaban"] == "Sebagian" for item in jawaban_domain),
                    "Tidak": sum(item["jawaban"] == "Tidak" for item in jawaban_domain),
                    "N/A": sum(item["jawaban"] == "N/A" for item in jawaban_domain)
                })

            st.markdown("### Rekapitulasi per Domain")
            st.dataframe(
                rekap,
                hide_index=True,
                use_container_width=True
            )

            total_ya = sum(item["Ya"] for item in rekap)
            total_sebagian = sum(item["Sebagian"] for item in rekap)
            total_tidak = sum(item["Tidak"] for item in rekap)
            total_na = sum(item["N/A"] for item in rekap)

            st.markdown("### Total Jawaban")
            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("Ya", total_ya)
            with c2:
                st.metric("Sebagian", total_sebagian)
            with c3:
                st.metric("Tidak", total_tidak)
            with c4:
                st.metric("N/A", total_na)

            st.markdown("### Detail Jawaban")

            for kode_domain in daftar_domain:
                with st.expander(f"Detail Domain {kode_domain}"):
                    for item in data["jawaban"]:
                        if item["domain"] == kode_domain:
                            st.markdown(
                                f"**Pertanyaan {item['nomor']} - {item['kode']}**"
                            )
                            st.write(item["pertanyaan"])
                            st.write(f"Jawaban: {item['jawaban']}")
                            st.write(f"Bukti Pendukung: {item['bukti'] or '-'}")
                            st.write(f"Catatan Auditor: {item['catatan'] or '-'}")
                            st.divider()


# ==================================================
# 11. REKOMENDASI
# ==================================================

elif st.session_state.menu == "Rekomendasi":
    st.title("Rekomendasi Perbaikan")
    st.write(
        "Rekomendasi awal untuk meningkatkan pengelolaan "
        "Aplikasi Persediaan dan Penjualan."
    )

    tampilkan_card(
        "Pengelolaan Persediaan",
        "Melakukan pembaruan data stok secara berkala, menerapkan stok opname, dan memastikan setiap barang masuk serta keluar tercatat."
    )

    tampilkan_card(
        "Transaksi Penjualan",
        "Memastikan setiap transaksi penjualan tercatat secara lengkap, akurat, dan memiliki bukti transaksi."
    )

    tampilkan_card(
        "Keamanan Sistem",
        "Menerapkan pembatasan hak akses pengguna sesuai tanggung jawab masing-masing."
    )

    tampilkan_card(
        "Pencadangan Data",
        "Melakukan pencadangan data persediaan dan penjualan secara berkala serta menguji pemulihan data."
    )

    tampilkan_card(
        "Pengawasan dan Pelaporan",
        "Melakukan evaluasi berkala terhadap laporan persediaan, penjualan, dan hasil pemeriksaan."
    )


# ==================================================
# 12. FOOTER
# ==================================================

st.divider()

st.markdown(
    """
    <p style="
        text-align: center;
        color: #A77B8E;
        font-size: 12px;
    ">
        Sistem Audit COBIT 5<br>
        Aplikasi Persediaan dan Penjualan<br>
        PT Muria Bangun Mandiri
    </p>
    """,
    unsafe_allow_html=True
)
