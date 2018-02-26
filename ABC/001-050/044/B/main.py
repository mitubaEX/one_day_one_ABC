import collections
dic = collections.defaultdict(lambda: 0)
for i in list(input()):
    dic[i] += 1

flag = True
for i in dic.keys():
    if dic[i] % 2 != 0:
        flag = False

if flag:
    print('Yes')
else:
    print('No')
