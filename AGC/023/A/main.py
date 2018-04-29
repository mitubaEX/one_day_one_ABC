# 部分列とって総和が0になるものの数

import sys

n = int(input())
lis = list(map(int, input().split()))

dp = [[sys.maxsize for j in range(n)] for i in range(n)]
#
# for index, i in enumerate(lis):
#     if index + 1 == len(lis):
#         break
#     dp[index][index + 1] = i + lis[index + 1]
#
# # dp[0][2] = dp[0][1] + dp[1][2]
#
# for index, i in enumerate(lis):
#     if dp[index][index + 1]
# print(dp)
count = 0

# for index in range(n):
index = 0
# now_val = lis[index]
dp[index][index] = lis[index]
print(lis[index + 1:])
for now_ind, i in enumerate(lis[index + 1:]):
    if dp[index][now_ind + 1] == sys.maxsize:
        print(dp[index][now_ind], i)
        dp[index][now_ind + 1] = dp[index][now_ind] + i
        print(dp[index][now_ind + 1])
        if dp[index][now_ind + 1] == 0:
            count += 1

print(dp)
for index in range(1, n - 1):
    dp[index][index] = lis[index]
    for now_ind, i in enumerate(lis[index:]):
        if now_ind + index + 1 == n:
            continue
        if dp[index][now_ind + index + 1] == sys.maxsize:
            dp[index][now_ind + index + 1] = dp[0][now_ind + index] - dp[0][index]
            if dp[index][now_ind + index + 1] == 0:
                count += 1
print(dp)
print(count)
