n, x = map(int, input().split())
lis = list(reversed(list(map(int, input().split()))))

bitSize = len(bin(x)) - 2
bits = bin(x)[2:]
if bitSize < n:
    for i in range(n - bitSize):
        bits = '0' + bits

ans = 0
for i in range(n):
    if bits[i] == '1':
        ans += lis[i]

print(ans)
