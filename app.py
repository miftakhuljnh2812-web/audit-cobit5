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
