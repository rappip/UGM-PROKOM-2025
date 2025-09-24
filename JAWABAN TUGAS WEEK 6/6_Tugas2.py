nilai = set({3,6,9,2,5,7})

# a. Menambah elemen hingga menjadi {1,2,3,4,5,6,7,8,9,10}
nilai = set({3,6,9,2,5,7})
 # Tambahkan elemen baru
nilai.update([1,4,8,10])
print(nilai)

# b. Menghapus elemen hingga menjadi {6,9,2}
nilai = set({3,6,9,2,5,7})
# Hapus elemen 3,5,7
nilai.remove(3)
nilai.remove(5)
nilai.remove(7)
print(nilai)