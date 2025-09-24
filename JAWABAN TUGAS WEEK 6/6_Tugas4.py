angka = {10,20,30,40,50}


# discard(): Menghapus elemen spesifik. Jika elemen tidak ada, tidak menimbulkan error.
# remove(): Menghapus elemen spesifik. Jika elemen tidak ada, akan menimbulkan error.
     

# Menggunakan remove()
angka.remove(30)
print(angka)  
# Menggunakan discard()
angka.discard(30)
print(angka)  



# Menggunakan discard() - AMAN 
angka.discard(99)
print(angka)  # (output akan sama dengan output sebelumnya, dikarenakan set sudah dimodifikasi sebelumnya oleh .remove(30))
# Menggunakan remove() - ERROR
angka.remove(99)
print(angka)