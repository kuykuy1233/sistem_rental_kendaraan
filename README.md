# 🚗 Sistem Rental Kendaraan – Python OOP

## Deskripsi Project
Sistem Rental Kendaraan merupakan program sederhana berbasis Python yang digunakan untuk mengelola penyewaan kendaraan. Program ini memungkinkan pelanggan melihat daftar kendaraan yang tersedia, melakukan penyewaan berdasarkan durasi, menghitung biaya sewa, serta melakukan pengembalian kendaraan.

Program dibuat menggunakan konsep Object-Oriented Programming (OOP) dan dijalankan melalui terminal tanpa menggunakan database.

## Fitur Program
- Menampilkan daftar mobil dan motor yang tersedia.
- Menampilkan tarif sewa kendaraan per hari.
- Melakukan penyewaan kendaraan.
- Memasukkan durasi penyewaan.
- Menghitung total biaya sewa secara otomatis.
- Memeriksa ketersediaan kendaraan.
- Mengubah status kendaraan ketika disewa atau dikembalikan.
- Memvalidasi durasi penyewaan.
- Menampilkan pesan ketika kendaraan berhasil disewa atau dikembalikan.

## Daftar Kendaraan

| Nama Kendaraan | Jenis | Tarif per Hari |
|---|---|---:|
| Avanza | Mobil | Rp350.000 |
| Brio | Mobil | Rp300.000 |
| Vario | Motor | Rp100.000 |
| NMAX | Motor | Rp150.000 |

## Konsep Object-Oriented Programming (OOP)

### 1. Class
Program ini memiliki tiga class utama:

- **Kendaraan**: Mengelola nama kendaraan, jenis kendaraan, tarif sewa, dan status ketersediaan.
- **Pelanggan**: Menyimpan nama pelanggan dan daftar penyewaan yang dilakukan.
- **Rental**: Mengelola daftar kendaraan, proses penyewaan, pengembalian kendaraan, dan transaksi.

### 2. Object
Object merupakan bentuk nyata dari class yang dibuat menggunakan constructor.

Contohnya, object kendaraan seperti Avanza, Brio, Vario, dan NMAX dibuat dari class `Kendaraan`. Object pelanggan dibuat dari class `Pelanggan`, sedangkan object rental dibuat dari class `Rental`.

### 3. Constructor (`__init__`)
Constructor digunakan untuk menginisialisasi data awal ketika object dibuat.

Pada class Kendaraan, constructor digunakan untuk menyimpan nama, jenis, tarif, dan status ketersediaan kendaraan.

Pada class Pelanggan, constructor digunakan untuk menyimpan nama pelanggan dan membuat daftar penyewaan.

Pada class Rental, constructor digunakan untuk menyediakan daftar kendaraan dan menyiapkan daftar transaksi.

### 4. Attribute dan Method
Attribute merupakan variabel yang menyimpan data pada object, seperti nama kendaraan, jenis kendaraan, tarif, status ketersediaan, dan nama pelanggan.

Method merupakan fungsi yang berada di dalam class untuk menjalankan suatu tindakan.

Contoh method yang digunakan:
- `tampilkan()` untuk menampilkan informasi kendaraan.
- `sewa_kendaraan()` untuk melakukan penyewaan.
- `kembalikan_kendaraan()` untuk mengembalikan kendaraan.
- `tampilkan_kendaraan()` untuk menampilkan seluruh kendaraan.
- `jalankan()` untuk menjalankan menu program.

### 5. Encapsulation
Encapsulation diterapkan pada attribute `__tersedia` di class Kendaraan.

Attribute tersebut dibuat privat sehingga pengaturan status kendaraan dilakukan melalui property dan setter. Hal ini membantu mengontrol perubahan status kendaraan agar hanya menerima nilai Boolean, yaitu True atau False.

### 6. Property dan Setter
Property diterapkan menggunakan decorator `@property` pada method `tersedia`, yang berfungsi untuk membaca status ketersediaan kendaraan.

Setter menggunakan decorator `@tersedia.setter` untuk mengubah status kendaraan. Setter melakukan validasi agar status hanya dapat diisi dengan nilai True atau False.

Status True berarti kendaraan tersedia untuk disewa, sedangkan False berarti kendaraan sedang disewa.

### 7. Class Method
Class method diterapkan pada method `buat_kendaraan()` dengan menggunakan decorator `@classmethod`.

Method ini berfungsi sebagai alternatif untuk membuat object kendaraan dengan memanfaatkan class `Kendaraan`. Method tersebut mengembalikan object kendaraan baru berdasarkan nama, jenis, dan tarif yang diberikan.

### 8. Static Method
Static method diterapkan pada method `validasi_durasi()` menggunakan decorator `@staticmethod`.

Method ini berfungsi untuk memeriksa apakah durasi penyewaan berupa bilangan bulat dan lebih dari 0. Jika durasi tidak memenuhi ketentuan, penyewaan tidak dapat dilakukan.

## Perhitungan Biaya Sewa
Biaya sewa dihitung berdasarkan tarif kendaraan dikalikan dengan jumlah hari penyewaan.

**Rumus:**

Total Biaya = Tarif Sewa per Hari × Jumlah Hari

**Contoh:**

Pelanggan menyewa Avanza selama 3 hari.

Rp350.000 × 3 = Rp1.050.000

Jadi, total biaya sewa adalah Rp1.050.000.

## Alur Kerja Program
1. Program dijalankan.
2. Pelanggan memasukkan nama.
3. Program menampilkan menu rental.
4. Pelanggan melihat daftar kendaraan.
5. Pelanggan memilih kendaraan yang ingin disewa.
6. Pelanggan memasukkan durasi penyewaan.
7. Program memeriksa durasi dan status ketersediaan kendaraan.
8. Jika valid, program menghitung biaya dan mengubah status kendaraan menjadi tidak tersedia.
9. Pelanggan dapat mengembalikan kendaraan melalui menu pengembalian.
10. Status kendaraan kembali menjadi tersedia.
11. Program berakhir ketika pelanggan memilih menu keluar.

## Teknologi yang Digunakan
- Python
- Object-Oriented Programming (OOP)
- Terminal / Command Line Interface (CLI)

## Cara Menjalankan Program
1. Pastikan Python sudah terinstal.
2. Download atau clone repository project.
3. Buka folder project di Visual Studio Code.
4. Buka terminal.
5. Jalankan perintah berikut:

```bash
python rental.py
```

## Tujuan Project
Project ini dibuat untuk menerapkan konsep Object-Oriented Programming (OOP) dalam bahasa Python, khususnya penggunaan class, object, constructor, attribute, method, encapsulation, property, setter, class method, dan static method dalam sebuah program penyewaan kendaraan sederhana.

---

**Project ini dibuat untuk memenuhi tugas perkuliahan Python – Object-Oriented Programming (OOP).**