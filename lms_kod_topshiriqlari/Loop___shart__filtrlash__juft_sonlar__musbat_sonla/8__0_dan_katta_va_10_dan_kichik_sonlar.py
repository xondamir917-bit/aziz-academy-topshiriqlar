n = int(input())
sonlar = list(map(int, input().split()))
print(*(son for son in sonlar if 0 < son < 10), sep="\n")