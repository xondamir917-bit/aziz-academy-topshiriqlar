n = int(input())
sonlar = list(map(int, input().split()))
print(len([son for son in sonlar if son % 3 == 0]))