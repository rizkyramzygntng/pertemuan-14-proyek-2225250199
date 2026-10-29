# Proposal Proyek
# Program Rekap dan Analisis Nilai Matematika Kelas

**Nama:** Muhammad Rizky Ramzy Ramadhan  
**NIM:** 2225250199  
**Kelas:** 3E  
**Mata Kuliah:** Algoritma dan Pemrograman

---

## 1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Kelas

## 2. Latar Belakang

Guru membutuhkan program sederhana untuk membantu membaca data nilai siswa, melakukan validasi data, menghitung statistik nilai, menentukan status ketuntasan berdasarkan KKM, dan menyimpan hasil rekap dalam bentuk laporan.

Program ini dirancang menggunakan Python berbasis terminal sehingga dapat membantu proses rekap nilai dilakukan dengan lebih cepat dan konsisten.

## 3. Pengguna dan Tujuan

### Pengguna

Pengguna utama program adalah guru matematika.

### Tujuan

Program bertujuan untuk membantu pengguna dalam:

- membaca data nilai siswa;
- memvalidasi nilai;
- menghitung rata-rata, nilai minimum, dan nilai maksimum;
- menentukan status ketuntasan siswa;
- menyimpan hasil rekap dalam file laporan.

## 4. Ruang Lingkup

### Fitur Wajib

1. Membaca data nilai dari file.
2. Memvalidasi nilai pada rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan status tuntas atau belum tuntas berdasarkan KKM.
5. Menyimpan hasil rekap ke file laporan.

### Batasan

- Program berbasis terminal/console.
- Data disimpan menggunakan file teks.
- Tidak menggunakan antarmuka grafis atau web.
- Data contoh tidak menggunakan informasi pribadi nyata.
- KKM yang digunakan dalam rancangan adalah 60.

## 5. Kebutuhan

### Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Program dapat membaca data nilai | Wajib |
| F02 | Program dapat memvalidasi nilai 0–100 | Wajib |
| F03 | Program dapat menghitung rata-rata, minimum, dan maksimum | Wajib |
| F04 | Program dapat menentukan status tuntas/belum tuntas | Wajib |
| F05 | Program dapat menyimpan laporan | Wajib |

### Kebutuhan Nonfungsional

- Program mudah dijalankan melalui terminal VS Code.
- Pesan kesalahan mudah dipahami.
- Nama fungsi dan variabel jelas.
- Program dapat diuji ulang menggunakan test case yang sama.

## 6. Input, Proses, dan Output

| Komponen | Isi |
|---|---|
| Input | File berisi NIM, nama, dan nilai siswa |
| Proses | Membaca data, validasi, menghitung statistik, menentukan status ketuntasan |
| Output | Rekap statistik dan laporan nilai |

### Alur IPO

```text
Input
  ↓
Baca file nilai
  ↓
Validasi data
  ↓
Simpan data valid
  ↓
Hitung statistik
  ↓
Tentukan status ketuntasan
  ↓
Tampilkan hasil
  ↓
Simpan laporan
```

## 7. Algoritma / Pseudocode

```text
MULAI

baca data dari file

jika file tidak ditemukan:
    tampilkan pesan error
    SELESAI

untuk setiap baris data:
    validasi format
    validasi nilai 0–100
    simpan data valid

jika tidak ada data valid:
    tampilkan pesan
    SELESAI

hitung rata-rata
hitung nilai minimum
hitung nilai maksimum

tentukan status ketuntasan berdasarkan KKM

tampilkan ringkasan

simpan laporan

SELESAI
```

## 8. Struktur Program

Program dibagi menjadi beberapa modul berdasarkan tanggung jawab.

| Fungsi/Modul | Tanggung Jawab | Input | Output |
|---|---|---|---|
| `baca_data()` | Membaca dan menyiapkan data | Path file | List data |
| `validasi_nilai()` | Memeriksa rentang nilai | Nilai | Boolean |
| `hitung_statistik()` | Menghitung statistik | Data | Dictionary statistik |
| `tentukan_status()` | Menentukan ketuntasan | Nilai, KKM | String |
| `hitung_ketuntasan()` | Menghitung jumlah tuntas | Data, KKM | Dictionary |
| `simpan_laporan()` | Menulis hasil ke file | Hasil, path | File laporan |
| `main()` | Mengatur alur program | - | - |

## 9. Struktur Data

Struktur data yang digunakan:

- **List** untuk menyimpan kumpulan data siswa.
- **Dictionary** untuk menyimpan data setiap siswa.
- **String** untuk nama, NIM, dan isi laporan.
- **File teks** untuk menyimpan data input dan laporan.

Contoh data:

```python
{
    "nim": "A001",
    "nama": "Ayu",
    "nilai": 85
}
```

## 10. Test Case

| ID | Kategori | Input/Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas = jumlah data |

## 11. Pembagian Tugas

| Peran | Tanggung Jawab |
|---|---|
| Koordinator | Menjaga ruang lingkup dan integrasi proyek |
| Programmer Data I/O | Membaca dan menulis file serta validasi |
| Programmer Logika | Mengembangkan perhitungan statistik dan status |
| Tester/QA | Menyusun dan menjalankan test case |
| Dokumentasi | Menyusun README dan dokumentasi proyek |

## 12. Jadwal / Milestone

| Waktu | Target |
|---|---|
| Pertemuan 14 | Proposal, struktur repository, pseudocode, test case, pembagian tugas |
| Antara P14–P15 | Implementasi awal fitur wajib |
| Pertemuan 15 | Integrasi, testing, debugging, dokumentasi |
| Pertemuan 16 | Presentasi, demonstrasi, evaluasi/UAS |

## 13. Repository

Repository GitHub:

https://github.com/rizkyramzygntng/pertemuan-14-proyek-2225250199

## Kesimpulan

Proyek ini dirancang sebagai program sederhana berbasis Python untuk membantu proses rekap dan analisis nilai matematika kelas.

Rancangan telah mencakup masalah, pengguna, tujuan, ruang lingkup, kebutuhan, IPO, pseudocode, struktur program, struktur data, test case, pembagian tugas, milestone, dan repository GitHub.

Proposal ini menjadi dasar implementasi program pada Pertemuan 15.