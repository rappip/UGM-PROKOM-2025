# Membuat dictionary harga buah
harga_buah = {
    "Apel": 15000,
    "Jeruk": 10000,
    "Anggur": 25000
}

# 1. Menampilkan harga jeruk
print("Harga Jeruk:", harga_buah["Jeruk"])

# 2. Menambahkan mangga dengan harga Rp12.000
harga_buah["Mangga"] = 12000
print("\nDictionary setelah menambahkan Mangga:")
print(harga_buah)

# 3. Mengubah harga anggur menjadi Rp20.000
harga_buah["Anggur"] = 20000
print("\nDictionary setelah mengubah harga Anggur:")
print(harga_buah)

# 4. Menghapus jeruk dari dictionary
del harga_buah["Jeruk"]
print("\nDictionary setelah menghapus Jeruk:")
print(harga_buah)