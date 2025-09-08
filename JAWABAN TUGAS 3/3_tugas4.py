# a. Menerima input string dari pengguna
input_string = input("Masukkan sebuah string: ")

# b. Menghapus spasi berlebih pada awal dan akhir
stripped_string = input_string.strip()

# c. Mengubah string menjadi lowercase
lowercase_string = stripped_string.lower()

# d. Mengganti semua huruf "a" dengan "@"
replaced_string = lowercase_string.replace('a', '@')

# e. Menghitung jumlah huruf pada string hasil akhir
jumlah_huruf = len(replaced_string)

# Output hasil proses
print("Hasil string setelah proses: ", replaced_string)
print("Jumlah huruf pada string akhir: ", jumlah_huruf)