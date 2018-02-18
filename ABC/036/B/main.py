# o, x
n = int(input())
lis = [list(list(input())) for i in range(n)]

for i in range(n):
    for j in reversed(range(n)):
        print(lis[j][i], end='')
    print()
