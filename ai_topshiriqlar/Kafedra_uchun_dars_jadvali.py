# Kafedra uchun dars jadvali
# Kurs: IT Dasturlash
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
for i in range(n):
    malumot = input().split()
    boshlash_vaqti = malumot[-2]
    tugash_vaqti = malumot[-1]
    dars_nomi = " ".join(malumot[:-2])
    
    print(f"{dars_nomi} {boshlash_vaqti}-{tugash_vaqti}")