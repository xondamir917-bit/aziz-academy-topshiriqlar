n = int(input())
sonlar = list(map(int, input().split()))
a, b = map(int, input().split())
print(len([son for son in sonlar if a <= son <= b]))