n = int(input())
sonlar = list(map(int, input().split()))
print(sum(son for son in sonlar if son > 10))