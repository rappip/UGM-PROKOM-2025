text = "   Praktikum Pemrograman Komputer 2025   "

#a. Hilangkan spasi di kiri dan kanan string
text_stripped = text.strip()
print(text_stripped)


#b. Ubah semua huruf menjadi uppercase
text_uppered = text_stripped.upper()
print(text_uppered)


#c. Hitung jumlah huruf “m”
m_counted = text_stripped.count("m")
print(m_counted)


#d. Cari posisi substring “man”
text_finded = text_stripped.find('man')
print(text_finded)


#e. Periksa apakah string hanya terdiri dari huruf
is_text_only_alpha = text_stripped.isalpha()
print(is_text_only_alpha)
