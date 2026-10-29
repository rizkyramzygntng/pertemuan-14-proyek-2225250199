from data_io import baca_data
from analisis import hitung_statistik, hitung_ketuntasan
from utilitas import simpan_laporan


def main():
    input_path = "data/nilai_contoh.txt"
    output_path = "output/laporan.txt"

    try:
        data = baca_data(input_path)
    except FileNotFoundError:
        print("File nilai tidak ditemukan.")
        return

    if not data:
        print("Tidak ada data valid.")
        return

    statistik = hitung_statistik(data)
    ketuntasan = hitung_ketuntasan(data, kkm=60)

    print("=== REKAP NILAI MATEMATIKA ===")
    print(f"Jumlah data: {len(data)}")
    print(f"Rata-rata: {statistik['rata_rata']:.2f}")
    print(f"Nilai minimum: {statistik['minimum']:.2f}")
    print(f"Nilai maksimum: {statistik['maksimum']:.2f}")
    print(f"Jumlah tuntas: {ketuntasan['tuntas']}")
    print(f"Jumlah belum tuntas: {ketuntasan['belum_tuntas']}")

    simpan_laporan(statistik, ketuntasan, output_path)
    print(f"Laporan disimpan ke {output_path}")


if __name__ == "__main__":
    main()