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
