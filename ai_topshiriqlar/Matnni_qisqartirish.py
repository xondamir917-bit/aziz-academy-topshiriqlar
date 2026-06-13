# Matnni qisqartirish
# Kurs: Dasturlash / IT
# Mavzu: Ma’lumot turlari: str (string) kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

matn = input()
n = int(input())

if len(matn) <= n:
    print(matn)
else:
    s = matn.split()
    print(" ".join(s[:-1]))