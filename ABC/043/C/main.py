# sum / 2の値に整えたら良さそう

import sys
import math

int(input())
lis = list(map(int, input().split()))

tmp = lis[0]
flag = True
for i in lis[1:]:
    if tmp != i:
        flag = False
if flag:
    print(0)
    sys.exit(0)

quot = int(math.ceil(sum(lis) / len(lis)))

cost = 0
for i in lis:
    if i != quot:
        cost += (i - quot) ** 2

print(cost)
