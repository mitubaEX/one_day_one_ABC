int(input())
lis = list(map(int, input().split()))

# 全通り試す

import sys

sys.setrecursionlimit(1000000)
min_num = sys.maxsize


def solve_dp():
    dp = [sys.maxsize for i in range(len(lis))]
    if len(lis) == 2:
        print(abs(lis[1] - lis[0]))
        return
    dp[0] = 0
    dp[1] = abs(lis[1] - lis[0])
    dp[2] = abs(lis[2] - lis[0])
    index = 1
    while index <= len(lis) - 1:
        dp[index] = min(dp[index - 1] + abs(lis[index - 1] - lis[index]),
                        dp[index - 2] + abs(lis[index - 2] - lis[index]))
        index += 1
    print(dp[len(lis) - 1])


def solve(index, sum_score):
    global min_num
    if index == len(lis) - 1:
        min_num = min(min_num, sum_score)
        return
    # print(index + 1, index + 2, len(lis))
    if index + 1 < len(lis):
        solve(index + 1, sum_score + abs(lis[index + 1] - lis[index]))
    if index + 2 < len(lis):
        solve(index + 2, sum_score + abs(lis[index + 2] - lis[index]))


# solve(0, 0)
# print(min_num)
solve_dp()
