
# dp [bit]
# dp[1<<N] = INF
#

n = int(input())

lis = []

for i in range(n):
    lis.append(int(input()))

print(lis)


dp = []
for i in range(1 << n):
    dp.append(False)

print(dp)
