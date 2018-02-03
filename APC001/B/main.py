# aに2を足す
# b に 1を足す
# ijを選択する

n = int(input())
a = map(int, input().split())
b = map(int, input().split())

# 差分
sub = filter(lambda x: x != 0, [ a - b for a, b in zip(a, b) ])

[ print(n) for n in sub]
