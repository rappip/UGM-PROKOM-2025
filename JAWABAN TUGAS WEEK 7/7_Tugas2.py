# Membuat dictionary buku
buku = {
    "Harry Potter": 10,
    "Laskar Pelangi": 15,
    "Bumi Manusia": 8,
    "Dilan 1990": 12
}

# 1. Menampilkan semua buku dengan format "Buku: [nama_buku] - Stok: [stok]"
print("Daftar Buku:")
for judul, stok in buku.items():
    print(f"Buku: {judul} - Stok: {stok}")

# 2. Meminta input user untuk menambahkan buku baru beserta stoknya
judul_baru = input("\nMasukkan judul buku baru: ")
stok_baru = int(input("Masukkan stok buku baru: "))
buku[judul_baru] = stok_baru

# 3. Menampilkan pesan "Buku [Judul Baru] berhasil ditambahkan dengan stok[Stok Baru]"
print(f"\nBuku '{judul_baru}' berhasil ditambahkan dengan stok sebanyak {stok_baru}")

# 4. Menampilkan dictionary buku terbaru
print("\nDictionary buku yang telah diperbarui:")
for judul, stok in buku.items():
    print(f"Buku: {judul} - Stok: {stok}")