import collections
dic = collections.defaultdict(lambda: 0)

for i in map(int, input().split()):
    dic[i] += 1

print(len(list(dic.keys())))
