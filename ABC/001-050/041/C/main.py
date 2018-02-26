# ai人の身長

int(input())
dic = {}
lis = list(map(int, input().split()))
for index, i in enumerate(lis):
    dic[i] = index

sorted_list = list(sorted(lis, reverse=True))

for i in sorted_list:
    print(dic[i] + 1)
