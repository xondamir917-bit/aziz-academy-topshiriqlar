# Oʻquvchi baholarini tekshirish dasturi
# Kurs: IT Dasturlash
# Mavzu: if, elif, else asoslari
# Ball: 100
# Aziz Academy — AI Topshiriq

oquvchi = input().split()
baho = int(oquvchi[1])
ism = str(oquvchi[0])
if baho > 90:
    print(f"{ism} A")
elif baho > 80 and baho < 89:
    print(f"{ism} B")
elif baho > 70 and baho < 79:
    print(f"{ism} C")
elif baho > 60 and baho < 69:
    print(f"{ism} D")
else:
    print(f"{ism} F")