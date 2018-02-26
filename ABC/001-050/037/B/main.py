# 初期0 長さｎ
# L < i < R => Ti

n, q = map(int, input().split())
lis = [0 for i in range(n)]
for i in [list(map(int, input().split())) for i in range(q)]:
    for l in range(i[0] - 1, i[1]):
        lis[l] = i[2]

for i in lis:
    print(i)
