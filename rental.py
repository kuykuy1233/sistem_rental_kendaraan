class Kendaraan:
    def __init__(self, nama, jenis, tarif):
        self.nama = nama
        self.jenis = jenis
        self.tarif = tarif
        self.__tersedia = True

    # Property status kendaraan
    @property
    def tersedia(self):
        return self.__tersedia

    # Setter status kendaraan
    @tersedia.setter
    def tersedia(self, status):
        if isinstance(status, bool):
            self.__tersedia = status
        else:
            raise ValueError("Status harus True atau False!")

    # Class method
    @classmethod
    def buat_kendaraan(cls, nama, jenis, tarif):
        return cls(nama, jenis, tarif)

    # Method menampilkan kendaraan
    def tampilkan(self):
        status = "Tersedia" if self.tersedia else "Disewa"
        print(
            f"{self.nama} | {self.jenis} | "
            f"Rp{self.tarif:,}/hari | {status}"
        )


class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_sewa = []


class Rental:
    def __init__(self):
        self.kendaraan = [
            Kendaraan.buat_kendaraan("Avanza", "Mobil", 350000),
            Kendaraan.buat_kendaraan("Brio", "Mobil", 300000),
            Kendaraan.buat_kendaraan("Vario", "Motor", 100000),
            Kendaraan.buat_kendaraan("NMAX", "Motor", 150000)
        ]

        self.transaksi = []

    # Static method
    @staticmethod
    def validasi_durasi(hari):
        return isinstance(hari, int) and hari > 0

    # Method menyewa kendaraan
    def sewa_kendaraan(self, pelanggan, kendaraan, hari):
        if not self.validasi_durasi(hari):
            print("Durasi sewa harus lebih dari 0 hari!")
            return

        if not kendaraan.tersedia:
            print("Kendaraan sedang disewa!")
            return

        total = kendaraan.tarif * hari

        kendaraan.tersedia = False

        data = {
            "pelanggan": pelanggan.nama,
            "kendaraan": kendaraan.nama,
            "hari": hari,
            "total": total
        }

        self.transaksi.append(data)
        pelanggan.daftar_sewa.append(data)

        print("Kendaraan berhasil disewa!")
        print("Total biaya: Rp", format(total, ",.0f"))

    # Method mengembalikan kendaraan
    def kembalikan_kendaraan(self, nama_kendaraan):
        for data in self.transaksi:
            if data["kendaraan"].lower() == nama_kendaraan.lower():
                kendaraan = next(
                    (k for k in self.kendaraan
                     if k.nama.lower() == nama_kendaraan.lower()),
                    None
                )

                if kendaraan and not kendaraan.tersedia:
                    kendaraan.tersedia = True
                    self.transaksi.remove(data)
                    print("Kendaraan berhasil dikembalikan!")
                    return

        print("Data penyewaan tidak ditemukan!")

    # Method menampilkan daftar kendaraan
    def tampilkan_kendaraan(self):
        print("\n=== DAFTAR KENDARAAN ===")
        for i, kendaraan in enumerate(self.kendaraan, 1):
            print(f"{i}. ", end="")
            kendaraan.tampilkan()

    # Method menu utama
    def jalankan(self):
        print("===== SISTEM RENTAL KENDARAAN =====")
        nama = input("Masukkan nama pelanggan: ")
        pelanggan = Pelanggan(nama)

        while True:
            print("\n===== MENU RENTAL =====")
            print("1. Lihat kendaraan")
            print("2. Sewa kendaraan")
            print("3. Kembalikan kendaraan")
            print("4. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tampilkan_kendaraan()

            elif pilihan == "2":
                self.tampilkan_kendaraan()

                try:
                    nomor = int(input("Pilih nomor kendaraan: "))
                    hari = int(input("Berapa hari menyewa: "))

                    if 1 <= nomor <= len(self.kendaraan):
                        kendaraan = self.kendaraan[nomor - 1]
                        self.sewa_kendaraan(
                            pelanggan, kendaraan, hari
                        )
                    else:
                        print("Nomor kendaraan tidak tersedia!")

                except ValueError:
                    print("Masukkan angka yang benar!")

            elif pilihan == "3":
                nama_kendaraan = input(
                    "Masukkan nama kendaraan yang dikembalikan: "
                )
                self.kembalikan_kendaraan(nama_kendaraan)

            elif pilihan == "4":
                print("Terima kasih telah menggunakan rental!")
                break

            else:
                print("Pilihan tidak valid!")


# PROGRAM UTAMA
rental = Rental()
rental.jalankan()