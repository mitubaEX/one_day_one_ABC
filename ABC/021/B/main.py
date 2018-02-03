n = int(input())
a, b = map(int, input().split())
k = int(input())
lis = list(map(int, input().split())) + [a, b]
if len(lis) != len(set(lis)):
    print('NO')
else:
    print('YES')
