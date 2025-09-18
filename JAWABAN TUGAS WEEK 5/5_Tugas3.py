# Program menghitung rata-rata nilai sesuai input dari user
jumlah_nilai = int(input("Masukkan jumlah nilai yang akan dihitung: "))
total = 0

for i in range(jumlah_nilai):
    nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
    total += nilai

rata_rata = total / jumlah_nilai
print(f"Rata-rata nilai adalah: {rata_rata}")