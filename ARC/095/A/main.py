n = int(input())

lis = list(map(int, input().split()))

for index, i in enumerate(lis):
    sub_lis = list(sorted(lis[0: index] + lis[index + 1: len(lis)]))
    # print(sub_lis)
    sub_ind = int((len(sub_lis) + 1) / 2) - 1
    # print(sub_ind)
    print(sub_lis[sub_ind])

