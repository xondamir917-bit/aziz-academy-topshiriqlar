# Savdo markazi daromadi
# Kurs: IT Dasturlash
# Mavzu: Ma’lumot turlari: int, float
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())

total = 0.0
for i in range(n):
    price, quantity = map(float, input().split())
    total += price * quantity 
    
print(total)