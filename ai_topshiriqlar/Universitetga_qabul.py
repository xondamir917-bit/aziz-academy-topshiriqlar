# Universitetga qabul
# Kurs: IT Dasturlash
# Mavzu: Ichma-ich shartlar (nested if)
# Ball: 100
# Aziz Academy — AI Topshiriq

y, b = map(int, input().split())
if y > 20:
    if b > 50:
        print("Talaba universitetga qabul qilindi")
    else:
        print("Talaba qabulga layoqatsiz")
else:
    print("Talaba qabulga layoqatsiz")