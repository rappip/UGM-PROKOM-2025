set_A = {20,30,40,50,60}
set_B = {25,30,35,40,45}
set_C = {30,40,50,70,80}
set_D = {40,50,60,90,100}

#a. Irisan ketiga set (A ∩ C ∩ D)
hasil = set_A.intersection(set_C).intersection(set_D)
print(hasil)


# b. Selisih bertingkat ((A - B) - D)
hasil = set_A.difference(set_B)  # A - B
hasilakhir = hasil.difference(set_D)  # (A - B) - D
print(hasilakhir)


# c. Selisih Simetris (B Δ C)
hasil = set_B.symmetric_difference(set_C)
print(hasil)


# d. Gabungan dan Irisan ((A ∪ B) ∩ (C ∪ D))
gab1 = set_A.union(set_B)       # A ∪ B
gab2 = set_C.union(set_D)       # C ∪ D
hasil = gab1.intersection(gab2) # (A ∪ B) ∩ (C ∪ D)
print(hasil)