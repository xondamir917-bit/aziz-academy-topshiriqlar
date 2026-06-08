n = int(input())
sonlar = list(map(int, input().split()))
print(*(son for son in sonlar if son % 2 == 0 and son > 0), sep="\n")