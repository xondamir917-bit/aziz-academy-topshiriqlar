# Kitob do'konidagi kitoblar sonini hisoblash
# Kurs: IT Dasturlash
# Mavzu: for bilan string va list bo‘ylab yurish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
kitoblar = []
for i in range(n):
    kitob = input().split()
    kitoblar.append((kitob[0], int(kitob[1])))
    
eng_qimmat = kitoblar[0]
eng_arzon = kitoblar[0]

for kitob in kitoblar:
    if kitob[1] > eng_qimmat[1]:
        eng_qimmat = kitob
    if kitob[1] < eng_arzon[1]:
        eng_arzon = kitob
        
print(f"Kitoblar soni: {n}")
print(f"Eng qimmat kitob: {eng_qimmat[0]} {eng_qimmat[1]}")
print(f"Eng arzon kitob: {eng_arzon[0]} {eng_arzon[1]}")