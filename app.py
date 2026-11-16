
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter

# ==================================================
# 1. KONFIGURASI
# ==================================================

st.set_page_config(
    page_title="Sistem Audit COBIT 5",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# 2. DATA PERTANYAAN AUDIT
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

pilihan_jawaban = [
    "Pilih jawaban",
    "Ya",
    "Sebagian",
    "Tidak",
    "N/A"
]

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
    background: linear-gradient(
        135deg,
        #FFF9FB,
        #FCEAF0,
        #F8DCE6
    );
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
    background: linear-gradient(
        180deg,
        #F9DCE6,
        #F2C4D5
    );
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

.stDownloadButton > button {
    background-color: #C987A3;
    color: white;
    border: none;
    border-radius: 9px;
    font-family: 'Poppins', sans-serif;
    width: 100%;
}

.stDownloadButton > button:hover {
    background-color: #B87592;
    color: white;
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
# 6. FUNGSI REKAPITULASI AUDIT
# ==================================================

def hitung_rekap(data):

    rekap = []

    for kode_domain, informasi in daftar_domain.items():

        jawaban_domain = [
            item for item in data["jawaban"]
            if item["domain"] == kode_domain
        ]

        jumlah_ya = sum(
            item["jawaban"] == "Ya"
            for item in jawaban_domain
        )

        jumlah_sebagian = sum(
            item["jawaban"] == "Sebagian"
            for item in jawaban_domain
        )

        jumlah_tidak = sum(
            item["jawaban"] == "Tidak"
            for item in jawaban_domain
        )

        jumlah_na = sum(
            item["jawaban"] == "N/A"
            for item in jawaban_domain
        )

        jumlah_dinilai = (
            jumlah_ya +
            jumlah_sebagian +
            jumlah_tidak
        )

        rekap.append({
            "Domain": kode_domain,
            "Nama Domain": informasi["nama"],
            "Jumlah Pertanyaan": len(jawaban_domain),
            "Ya": jumlah_ya,
            "Sebagian": jumlah_sebagian,
            "Tidak": jumlah_tidak,
            "N/A": jumlah_na,

            "Persentase Ya": (
                jumlah_ya / jumlah_dinilai * 100
                if jumlah_dinilai else 0
            ),

            "Persentase Sebagian": (
                jumlah_sebagian / jumlah_dinilai * 100
                if jumlah_dinilai else 0
            ),

            "Persentase Tidak": (
                jumlah_tidak / jumlah_dinilai * 100
                if jumlah_dinilai else 0
            )
        })

    return rekap


# ==================================================
# 7. FUNGSI EKSPOR EXCEL
# ==================================================

def buat_excel_audit(data, nomor_audit, rekap):

    output = BytesIO()

    # ----------------------------------------------
    # SHEET 1: IDENTITAS AUDIT
    # ----------------------------------------------

    identitas = pd.DataFrame({
        "Keterangan": [
            "Nomor Audit",
            "Nama Auditor",
            "Nama Responden",
            "Bagian / Unit Kerja",
            "Nama Perusahaan",
            "Objek Audit",
            "Tanggal Ekspor"
        ],

        "Informasi": [
            f"AUDIT-{nomor_audit:03d}",
            data["nama_auditor"],
            data["nama_responden"],
            data["bagian"] or "-",
            "PT Muria Bangun Mandiri",
            "Aplikasi Persediaan dan Penjualan",
            datetime.now().strftime("%d-%m-%Y %H:%M")
        ]
    })

    # ----------------------------------------------
    # SHEET 2: DETAIL JAWABAN
    # ----------------------------------------------

    detail = []

    for item in data["jawaban"]:

        detail.append({
            "Nomor": item["nomor"],
            "Kode Domain": item["domain"],
            "Nama Domain": daftar_domain[item["domain"]]["nama"],
            "Kode Proses COBIT 5": item["kode"],
            "Pertanyaan Audit": item["pertanyaan"],
            "Jawaban": item["jawaban"],
            "Bukti Pendukung": item["bukti"] or "-",
            "Catatan Auditor": item["catatan"] or "-"
        })

    df_detail = pd.DataFrame(detail)

    # ----------------------------------------------
    # SHEET 3: REKAPITULASI DOMAIN
    # ----------------------------------------------

    df_rekap = pd.DataFrame(rekap)

    kolom_rekap = [
        "Domain",
        "Nama Domain",
        "Jumlah Pertanyaan",
        "Ya",
        "Sebagian",
        "Tidak",
        "N/A",
        "Persentase Ya",
        "Persentase Sebagian",
        "Persentase Tidak"
    ]

    df_rekap = df_rekap[kolom_rekap]

    # ----------------------------------------------
    # MEMBUAT FILE EXCEL
    # ----------------------------------------------

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        identitas.to_excel(
            writer,
            sheet_name="Identitas Audit",
            index=False,
            startrow=2
        )

        df_detail.to_excel(
            writer,
            sheet_name="Detail Jawaban",
            index=False,
            startrow=2
        )

        df_rekap.to_excel(
            writer,
            sheet_name="Rekapitulasi",
            index=False,
            startrow=2
        )

        # ------------------------------------------
        # FORMAT SEMUA SHEET
        # ------------------------------------------

        judul_sheet = {
            "Identitas Audit": "IDENTITAS AUDIT COBIT 5",
            "Detail Jawaban": "DETAIL JAWABAN AUDIT COBIT 5",
            "Rekapitulasi": "REKAPITULASI HASIL AUDIT COBIT 5"
        }

        for nama_sheet, judul in judul_sheet.items():

            ws = writer.sheets[nama_sheet]

            jumlah_kolom = ws.max_column

            ws.merge_cells(
                start_row=1,
                start_column=1,
                end_row=1,
                end_column=jumlah_kolom
            )

            cell_judul = ws.cell(row=1, column=1)

            cell_judul.value = judul

            cell_judul.font = Font(
                bold=True,
                size=14,
                color="FFFFFF"
            )

            cell_judul.fill = PatternFill(
                fill_type="solid",
                fgColor="C987A3"
            )

            cell_judul.alignment = Alignment(
                horizontal="center",
                vertical="center"
            )

            ws.row_dimensions[1].height = 30

            # Format header
            for cell in ws[3]:

                cell.font = Font(
                    bold=True,
                    color="FFFFFF"
                )

                cell.fill = PatternFill(
                    fill_type="solid",
                    fgColor="DFA6BC"
                )

                cell.alignment = Alignment(
                    horizontal="center",
                    vertical="center",
                    wrap_text=True
                )

            # Format isi tabel
            for row in ws.iter_rows(
                min_row=4,
                max_row=ws.max_row
            ):

                for cell in row:

                    cell.alignment = Alignment(
                        vertical="top",
                        wrap_text=True
                    )

                    cell.border = Border(
                        bottom=Side(
                            style="thin",
                            color="EBC6D5"
                        )
                    )

            # Lebar kolom
            for column in ws.columns:

                max_length = 0

                column_letter = get_column_letter(
                    column[0].column
                )

                for cell in column:

                    if cell.value is not None:

                        max_length = max(
                            max_length,
                            len(str(cell.value))
                        )

                ws.column_dimensions[
                    column_letter
                ].width = min(
                    max(max_length + 3, 15),
                    55
                )

            ws.freeze_panes = "A4"

            if ws.max_row >= 4:

                ws.auto_filter.ref = (
                    f"A3:{get_column_letter(ws.max_column)}"
                    f"{ws.max_row}"
                )

        # Format angka persentase
        ws_rekap = writer.sheets["Rekapitulasi"]

        for baris in range(4, 9):

            for kolom in ["H", "I", "J"]:

                ws_rekap[
                    f"{kolom}{baris}"
                ].number_format = '0.00"%"'

    output.seek(0)

    return output.getvalue()


# ==================================================
# 8. SIDEBAR
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
# 9. DASHBOARD
# ==================================================

if st.session_state.menu == "Dashboard":

    st.title("Dashboard Audit COBIT 5")

    st.write(
        "Sistem Evaluasi Aplikasi Persediaan dan Penjualan"
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        tampilkan_card(
            "Standar Audit",
            "COBIT 5"
        )

    with col2:
        tampilkan_card(
            "Objek Evaluasi",
            "Aplikasi Persediaan dan Penjualan"
        )

    with col3:
        tampilkan_card(
            "Jumlah Pertanyaan",
            "30 Pertanyaan"
        )

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

    col1, col2, col3 = st.columns(3)

    with col1:
        tampilkan_card(
            "EDM",
            "Evaluate, Direct and Monitor"
        )

    with col2:
        tampilkan_card(
            "APO",
            "Align, Plan and Organise"
        )

    with col3:
        tampilkan_card(
            "BAI",
            "Build, Acquire and Implement"
        )

    col4, col5 = st.columns(2)

    with col4:
        tampilkan_card(
            "DSS",
            "Deliver, Service and Support"
        )

    with col5:
        tampilkan_card(
            "MEA",
            "Monitor, Evaluate and Assess"
        )


# ==================================================
# 10. PROFIL PERUSAHAAN
# ==================================================

elif st.session_state.menu == "Profil Perusahaan":

    st.title("Profil Perusahaan")

    st.write(
        "Informasi perusahaan yang menjadi objek audit."
    )

    tampilkan_card(
        "PT Muria Bangun Mandiri",
        "PT Muria Bangun Mandiri merupakan objek evaluasi tata kelola teknologi informasi menggunakan kerangka kerja COBIT 5."
    )

    st.markdown("### Informasi Objek Audit")

    col1, col2 = st.columns(2)

    with col1:

        tampilkan_card(
            "Nama Perusahaan",
            "PT Muria Bangun Mandiri"
        )

    with col2:

        tampilkan_card(
            "Sistem yang Dievaluasi",
            "Aplikasi Persediaan dan Penjualan"
        )


# ==================================================
# 11. KUESIONER AUDIT
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

            st.markdown(
                f"## {kode_domain} - {data_domain['nama']}"
            )

            st.caption("6 pertanyaan audit")

            for kode_proses, pertanyaan in data_domain["pertanyaan"]:

                st.markdown(
                    f"**Pertanyaan {nomor} | {kode_proses}**"
                )

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

            st.warning(
                "Nama auditor dan nama responden wajib diisi."
            )

        elif any(
            item["jawaban"] == "Pilih jawaban"
            for item in jawaban_audit
        ):

            st.warning(
                "Semua 30 pertanyaan harus diberi jawaban sebelum disimpan."
            )

        else:

            data_baru = {
                "nama_auditor": nama_auditor.strip(),
                "nama_responden": nama_responden.strip(),
                "bagian": bagian.strip(),
                "jawaban": jawaban_audit
            }

            st.session_state.hasil_audit.append(data_baru)

            st.success(
                "30 jawaban audit berhasil disimpan dalam sesi aplikasi."
            )


# ==================================================
# 12. HASIL AUDIT
# ==================================================

elif st.session_state.menu == "Hasil Audit":

    st.title("Hasil Audit")

    st.write(
        "Rekapitulasi jawaban audit berdasarkan lima domain COBIT 5."
    )

    if not st.session_state.hasil_audit:

        st.info(
            "Belum ada data audit. Silakan isi kuesioner terlebih dahulu."
        )

    else:

        for nomor_audit, data in enumerate(
            st.session_state.hasil_audit,
            start=1
        ):

            st.markdown(
                f"## Hasil Audit {nomor_audit}"
            )

            st.write(
                f"**Auditor:** {data['nama_auditor']}"
            )

            st.write(
                f"**Responden:** {data['nama_responden']}"
            )

            st.write(
                f"**Bagian:** {data['bagian'] or '-'}"
            )

            # ------------------------------------------
            # REKAPITULASI
            # ------------------------------------------

            rekap = hitung_rekap(data)

            # ------------------------------------------
            # DOWNLOAD EXCEL
            # ------------------------------------------

            file_excel = buat_excel_audit(
                data,
                nomor_audit,
                rekap
            )

            nama_file = (
                f"Hasil_Audit_COBIT5_{nomor_audit}.xlsx"
            )

            st.download_button(
                label="Download Hasil Audit Excel",
                data=file_excel,
                file_name=nama_file,
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                ),
                key=f"download_excel_{nomor_audit}",
                use_container_width=True
            )

            st.divider()

            # ------------------------------------------
            # TABEL REKAPITULASI
            # ------------------------------------------

            st.markdown("### Rekapitulasi per Domain")

            df_rekap = pd.DataFrame(rekap)

            st.dataframe(
                df_rekap[
                    [
                        "Domain",
                        "Ya",
                        "Sebagian",
                        "Tidak",
                        "N/A"
                    ]
                ],
                hide_index=True,
                use_container_width=True
            )

            # ------------------------------------------
            # GRAFIK PERSENTASE
            # ------------------------------------------

            st.markdown(
                "### Grafik Persentase per Domain"
            )

            df_grafik = pd.DataFrame(rekap).set_index("Domain")

            df_grafik = df_grafik[
                [
                    "Persentase Ya",
                    "Persentase Sebagian",
                    "Persentase Tidak"
                ]
            ]

            df_grafik.columns = [
                "Ya",
                "Sebagian",
                "Tidak"
            ]

            st.bar_chart(
                df_grafik,
                height=350
            )

            st.caption(
                "Persentase dihitung berdasarkan jawaban Ya, "
                "Sebagian, dan Tidak. Jawaban N/A tidak dimasukkan "
                "ke dalam penyebut persentase penilaian."
            )

            # ------------------------------------------
            # TOTAL JAWABAN
            # ------------------------------------------

            total_ya = sum(
                item["Ya"] for item in rekap
            )

            total_sebagian = sum(
                item["Sebagian"] for item in rekap
            )

            total_tidak = sum(
                item["Tidak"] for item in rekap
            )

            total_na = sum(
                item["N/A"] for item in rekap
            )

            total_jawaban = (
                total_ya +
                total_sebagian +
                total_tidak +
                total_na
            )

            persen_ya = (
                total_ya / total_jawaban * 100
                if total_jawaban else 0
            )

            persen_sebagian = (
                total_sebagian / total_jawaban * 100
                if total_jawaban else 0
            )

            persen_tidak = (
                total_tidak / total_jawaban * 100
                if total_jawaban else 0
            )

            persen_na = (
                total_na / total_jawaban * 100
                if total_jawaban else 0
            )

            st.markdown("### Total Jawaban")

            c1, c2, c3, c4 = st.columns(4)

            with c1:

                st.metric(
                    "Ya",
                    total_ya,
                    f"{persen_ya:.1f}%"
                )

            with c2:

                st.metric(
                    "Sebagian",
                    total_sebagian,
                    f"{persen_sebagian:.1f}%"
                )

            with c3:

                st.metric(
                    "Tidak",
                    total_tidak,
                    f"{persen_tidak:.1f}%"
                )

            with c4:

                st.metric(
                    "N/A",
                    total_na,
                    f"{persen_na:.1f}%"
                )

            # ------------------------------------------
            # PERSENTASE DISTRIBUSI JAWABAN
            # ------------------------------------------

            st.markdown(
                "### Persentase Distribusi Jawaban"
            )

            daftar_persentase = [
                ("Ya", persen_ya),
                ("Sebagian", persen_sebagian),
                ("Tidak", persen_tidak),
                ("N/A", persen_na)
            ]

            for label, nilai in daftar_persentase:

                st.write(
                    f"**{label}: {nilai:.1f}%**"
                )

                st.progress(
                    int(round(nilai))
                )

            # ------------------------------------------
            # DETAIL JAWABAN
            # ------------------------------------------

            st.markdown("### Detail Jawaban")

            for kode_domain in daftar_domain:

                with st.expander(
                    f"Detail Domain {kode_domain}"
                ):

                    for item in data["jawaban"]:

                        if item["domain"] == kode_domain:

                            st.markdown(
                                f"**Pertanyaan {item['nomor']} - "
                                f"{item['kode']}**"
                            )

                            st.write(
                                item["pertanyaan"]
                            )

                            st.write(
                                f"Jawaban: {item['jawaban']}"
                            )

                            st.write(
                                f"Bukti Pendukung: {item['bukti'] or '-'}"
                            )

                            st.write(
                                f"Catatan Auditor: {item['catatan'] or '-'}"
                            )

                            st.divider()


# ==================================================
# 13. REKOMENDASI
# ==================================================

elif st.session_state.menu == "Rekomendasi":

    st.title("Rekomendasi Perbaikan")

    st.write(
        "Rekomendasi awal untuk meningkatkan pengelolaan "
        "Aplikasi Persediaan dan Penjualan."
    )

    tampilkan_card(
        "Pengelolaan Persediaan",
        "Melakukan pembaruan data stok secara berkala, "
        "menerapkan stok opname, dan memastikan setiap barang "
        "masuk serta keluar tercatat."
    )

    tampilkan_card(
        "Transaksi Penjualan",
        "Memastikan setiap transaksi penjualan tercatat "
        "secara lengkap, akurat, dan memiliki bukti transaksi."
    )

    tampilkan_card(
        "Keamanan Sistem",
        "Menerapkan pembatasan hak akses pengguna "
        "sesuai tanggung jawab masing-masing."
    )

    tampilkan_card(
        "Pencadangan Data",
        "Melakukan pencadangan data persediaan dan penjualan "
        "secara berkala serta menguji pemulihan data."
    )

    tampilkan_card(
        "Pengawasan dan Pelaporan",
        "Melakukan evaluasi berkala terhadap laporan "
        "persediaan, penjualan, dan hasil pemeriksaan."
    )


# ==================================================
# 14. FOOTER
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
