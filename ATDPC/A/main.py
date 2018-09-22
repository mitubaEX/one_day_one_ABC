n = int(input())
lis = list(map(int, input().split()))

# dp[0][0] = True

lis_sum = sum(lis)

dp = [[False for j in range((lis_sum + 1))] for i in range(n + 1)]

# print(dp)

dp[0][0] = True

for i in range(1, n + 1):
    for j in range(lis_sum + 1):
        if (j - lis[i - 1] < 0):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] or dp[i-1][j - lis[i-1]]

# print(dp)

s = 0
for index, i in enumerate(dp[n]):
    if i:
        print(index)
        s += index
print(s)

# print(sum(list(filter(lambda x: x == True, dp[n]))))
