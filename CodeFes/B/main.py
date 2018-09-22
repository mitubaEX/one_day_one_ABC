n, m, a, b = map(int, input().split())

import collections

dic = collections.defaultdict(lambda: 1)

for i in range(m):
    l, r = map(int, input().split())
    for k in range(l, r + 1):
        dic[k] = 1

print(len(dic.keys()) * a + (n - len(dic.keys())) * b)
