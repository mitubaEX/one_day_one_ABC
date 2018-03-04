import collections
dic = collections.defaultdict(lambda: 0)
int(input())
for i in list(input().split()):
    dic[i] += 1
if len(list(dic.keys())) == 4:
    print('Four')
else:
    print('Three')
