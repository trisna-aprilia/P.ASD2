class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class InventoryPeralatanRumahSakit:
    def __init__(self):
        self.head = None

    def tambah_peralatan_di_awal(self, peralatan):
        new_node = Node(peralatan)
        new_node.next = self.head
        self.head = new_node

    def tambah_peralatan_di_akhir(self, peralatan):
        new_node = Node(peralatan)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tambah_peralatan_di_tengah(self, peralatan, posisi):
        if posisi < 0:
            print("Posisi harus non-negatif.")
            return
        if posisi == 0:
            self.tambah_peralatan_di_awal(peralatan)
            return
        new_node = Node(peralatan)
        current = self.head
        prev = None
        count = 0
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Posisi terlalu tinggi.")
            return
        prev.next = new_node
        new_node.next = current

    def hapus_peralatan(self, posisi):
        if posisi < 0:
            print("Posisi harus non-negatif.")
            return
        if not self.head:
            print("Inventaris kosong.")
            return
        if posisi == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 0
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Posisi terlalu tinggi.")
            return
        prev.next = current.next

    def update_peralatan(self, nama_peralatan, kualitas, kondisi):
        current = self.head
        while current:
            if current.data.nama == nama_peralatan:
                current.data.kualitas = kualitas
                current.data.kondisi = kondisi
                return
            current = current.next
        print("Peralatan tidak ditemukan.")

    def tampilkan_chart(self):
        labels = []
        values = []
        current = self.head
        while current:
            labels.append(current.data.kategori)
            values.append(current.data.kualitas)
            current = current.next
        return labels, values

    def tampilkan_peralatan(self):
        if not self.head:
            print("Inventaris kosong.")
            return
        print("Seluruh Peralatan Rumah Sakit:")
        current = self.head
        while current:
            peralatan = current.data
            print(f"Nama: {peralatan.nama}, Kategori: {peralatan.kategori}, Kualitas: {peralatan.kualitas}, Kondisi: {peralatan.kondisi}, Lokasi: {peralatan.lokasi}")
            current = current.next


class PeralatanRumahSakit:
    def __init__(self, nama, kategori, kualitas, kondisi, lokasi):
        self.nama = nama
        self.kategori = kategori
        self.kualitas = kualitas
        self.kondisi = kondisi
        self.lokasi = lokasi


def input_peralatan():
    nama = input("Masukkan nama peralatan: ")
    kategori = input("Masukkan kategori peralatan: ")
    kualitas = input("Masukkan kualitas peralatan: ")
    kondisi = input("Masukkan kondisi peralatan: ")
    lokasi = input("Masukkan lokasi peralatan: ")
    return PeralatanRumahSakit(nama, kategori, kualitas, kondisi, lokasi)


inventory = InventoryPeralatanRumahSakit()

# Menambahkan beberapa peralatan
peralatan1 = PeralatanRumahSakit("Stetoskop", "Alat Kesehatan", "Baik", "Baru", "Depan Ruangan")
peralatan2 = PeralatanRumahSakit("Gunting Medis", "Alat Bedah", "Baik", "Baru", "Ruang Operasi")
peralatan3 = PeralatanRumahSakit("Infus", "Alat Kesehatan", "Baik", "Baru", "Kamar Pasien")
inventory.tambah_peralatan_di_awal(peralatan1)
inventory.tambah_peralatan_di_akhir(peralatan2)
inventory.tambah_peralatan_di_akhir(peralatan3)

while True:
    print("\nPilihan Menu:")
    print("1. Tambah Peralatan di Awal")
    print("2. Tambah Peralatan di Akhir")
    print("3. Tambah Peralatan di Tengah")
    print("4. Hapus Peralatan")
    print("5. Update Peralatan")
    print("6. Tampilkan Peralatan")
    print("7. Tampilkan Chart")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":
        peralatan = input_peralatan()
        inventory.tambah_peralatan_di_awal(peralatan)
    elif pilihan == "2":
        peralatan = input_peralatan()
        inventory.tambah_peralatan_di_akhir(peralatan)
    elif pilihan == "3":
        peralatan = input_peralatan()
        posisi = int(input("Masukkan posisi peralatan yang ingin ditambahkan: "))
        inventory.tambah_peralatan_di_tengah(peralatan, posisi)
    elif pilihan == "4":
        posisi = int(input("Masukkan posisi peralatan yang ingin dihapus: "))
        inventory.hapus_peralatan(posisi)
    elif pilihan == "5":
        nama_peralatan = input("Masukkan nama peralatan yang ingin diupdate: ")
        kualitas_baru = input("Masukkan kualitas baru peralatan: ")
        kondisi_baru = input("Masukkan kondisi baru peralatan: ")
        inventory.update_peralatan(nama_peralatan, kualitas_baru, kondisi_baru)
    elif pilihan == "6":
        inventory.tampilkan_peralatan()
    elif pilihan == "7":
        labels, values = inventory.tampilkan_chart()
        print("Labels:", labels)
        print("Values:", values)
    elif pilihan == "0":
        print("Terima kasih!")
        break
    else:
        print("Pilihan menu tidak valid. Silakan pilih lagi.")
