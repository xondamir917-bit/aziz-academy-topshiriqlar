
a = int(input())
numbers = list(map(int, input().split()))
for i in numbers:
    if i < 0:
        print(i)