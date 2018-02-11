import collections
s = list(input())
dic = collections.defaultdict(lambda: 0)
dic['A'] = 0
dic['B'] = 0
dic['C'] = 0
dic['D'] = 0
dic['E'] = 0
dic['F'] = 0
for i in s:
    dic[i] += 1

print(' '.join([str(dic[i]) for i in sorted(dic.keys())]))
