def simpan_laporan(statistik, ketuntasan, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write("LAPORAN REKAP NILAI MATEMATIKA\n")
        file.write("==============================\n")
        file.write(f"Rata-rata : {statistik['rata_rata']:.2f}\n")
        file.write(f"Nilai minimum : {statistik['minimum']:.2f}\n")
        file.write(f"Nilai maksimum : {statistik['maksimum']:.2f}\n")
        file.write(f"Jumlah tuntas : {ketuntasan['tuntas']}\n")
        file.write(f"Jumlah belum tuntas : {ketuntasan['belum_tuntas']}\n")