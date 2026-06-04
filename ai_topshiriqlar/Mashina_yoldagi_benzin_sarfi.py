# Mashina yo'ldagi benzin sarfi
# Kurs: IT Dasturlash
# Mavzu: Ma’lumot turlari: int, float
# Ball: 100
# Aziz Academy — AI Topshiriq

km, m = map(int, input().split())
max_km = m * 10 

if max_km >= km:
    print(float(km))
else:
    print(float(max_km))