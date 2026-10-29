# Pertemuan 14 — Perancangan Proyek Program Sederhana

**Nama:** Muhammad Rizky Ramzy Ramadhan  
**NIM:** 2225250199  
**Kelas:** 3E

## Tujuan

Merancang proyek program sederhana berbasis Python untuk masalah matematika atau pembelajaran matematika melalui identifikasi masalah, kebutuhan pengguna, input-proses-output, algoritma, struktur program, test case, pembagian tugas, proposal, dan pengelolaan repository GitHub.

## Judul Proyek

**Program Rekap dan Analisis Nilai Matematika Kelas**

Program ini dirancang untuk membantu guru membaca data nilai siswa, melakukan validasi, menghitung statistik nilai, menentukan status ketuntasan berdasarkan KKM, dan menyimpan hasil rekap dalam bentuk laporan.

## Struktur Proyek

```text
pertemuan-14-proyek-2225250199/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## Pengguna

Pengguna utama proyek adalah guru matematika yang membutuhkan program sederhana untuk membantu proses rekap dan analisis nilai siswa.

## Fitur Wajib

- Membaca data nilai dari file.
- Memvalidasi nilai pada rentang 0–100.
- Menghitung rata-rata, nilai minimum, dan nilai maksimum.
- Menentukan status tuntas atau belum tuntas berdasarkan KKM.
- Menyimpan hasil rekap ke file laporan.

## Input, Proses, dan Output

| Komponen | Isi |
|---|---|
| Input | File berisi NIM, nama, dan nilai siswa |
| Proses | Membaca data, validasi, menghitung statistik, menentukan ketuntasan |
| Output | Rekap statistik dan laporan nilai |

## Pseudocode

```text
MULAI

baca data dari file

jika file tidak ditemukan:
    tampilkan pesan error
    SELESAI

untuk setiap baris data:
    validasi format dan nilai
    simpan data valid

jika tidak ada data valid:
    tampilkan pesan
    SELESAI

hitung statistik
tentukan status ketuntasan
tampilkan ringkasan
simpan laporan

SELESAI
```

## Struktur Program

Program dibagi menjadi beberapa modul:

- `data_io.py` untuk membaca data.
- `analisis.py` untuk validasi, statistik, dan status ketuntasan.
- `utilitas.py` untuk menyimpan laporan.
- `main.py` untuk mengatur alur utama program.

## Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas = jumlah data |

## Cara Menjalankan

Jalankan perintah dari terminal VS Code pada folder utama proyek.

Menjalankan program:

```bash
python src/main.py
```

Program akan membaca:

```text
data/nilai_contoh.txt
```

dan menghasilkan laporan pada:

```text
output/laporan.txt
```

## Pembagian Tugas

| Peran | Tanggung Jawab |
|---|---|
| Koordinator | Integrasi dan ruang lingkup proyek |
| Programmer Data I/O | Membaca dan menulis file |
| Programmer Logika | Statistik dan status ketuntasan |
| Tester/QA | Test case dan pengujian |
| Dokumentasi | README dan proposal |

## Milestone

| Waktu | Target |
|---|---|
| Pertemuan 14 | Proposal, struktur repo, pseudocode, test case, pembagian tugas |
| Antara P14–P15 | Implementasi awal fitur wajib |
| Pertemuan 15 | Integrasi, testing, debugging, dokumentasi |
| Pertemuan 16 | Presentasi, demonstrasi, evaluasi/UAS |

## Refleksi

Pada pertemuan ini saya mempelajari bahwa perancangan proyek tidak langsung dimulai dari penulisan kode, tetapi dimulai dari masalah dan kebutuhan pengguna.

Saya juga mempelajari hubungan antara kebutuhan, input-proses-output, pseudocode, struktur program, struktur data, dan test case. Perancangan sejak awal membantu program memiliki ruang lingkup yang jelas dan dapat diuji.

Selain itu, penggunaan GitHub membantu menyimpan rancangan proyek dan mencatat perkembangan melalui commit.

## Referensi

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 14: Perancangan Proyek Program Sederhana.
- RPS Algoritma dan Pemrograman OBE Untirta, Tahun Ajaran 2026/2027 Ganjil.
- Python Software Foundation, Python 3 Documentation.
- GitHub Docs.
- Bantuan AI digunakan untuk mendukung pemahaman konsep dan penyusunan rancangan proyek. Rancangan perlu dipahami dan diuji oleh penulis.