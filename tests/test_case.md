# Test Case Proyek

## Tujuan

Test case digunakan untuk memastikan fitur utama program dapat berjalan sesuai dengan kebutuhan yang telah dirancang.

| ID | Kategori | Input/Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas = jumlah data |

## Hasil yang Diharapkan

- Data dengan nilai 0 sampai 100 diterima.
- Data dengan nilai di bawah 0 atau di atas 100 ditolak.
- File yang tidak ditemukan ditangani dengan pesan error.
- Statistik dapat dihitung dari data valid.
- Status ketuntasan dihitung berdasarkan KKM.