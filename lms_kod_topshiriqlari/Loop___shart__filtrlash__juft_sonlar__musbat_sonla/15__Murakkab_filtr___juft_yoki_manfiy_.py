n = int(input())
print('\n'.join(str(x) for x in map(int, input().split()) if x % 2 == 0 or x < 0))