# aに2を足す
# b に 1を足す
# ijを選択する

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_list = []
b_list = []

for i, j in zip(a, b):
    if i > j:
        b_list.append(i - j)
    elif i < j:
        a_list.append((j - i) // 2)

if sum(b_list) >= sum(a_list):
    print('No')
else:
    print('Yes')

