n, m = map(int, input().split())
import collections
dic = collections.defaultdict(lambda: 0)
for i in range(m):
    a, b = map(int, input().split())
    dic[a] += 1
    dic[b] += 1
for i in sorted(list(dic.keys())):
    print(dic[i])
