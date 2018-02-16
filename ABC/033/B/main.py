import sys
n = int(input())
dic = {}


def add_dict(array):
    dic[array[0]] = int(array[1])


[add_dict(input().split()) for i in range(n)]
sum_num = sum(list(dic.values()))
for i in dic.keys():
    if dic[i] >= int(sum_num / 2) + 1:
        print(i)
        sys.exit(0)
print("atcoder")
