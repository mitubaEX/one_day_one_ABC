import collections
dic = collections.defaultdict(lambda: 0)

s = list(input())
k = int(input())

index = 0

while k <= len(s):
    dic[''.join(s[index:k])] += 1
    index += 1
    k += 1
print(len(list(dic.keys())))
