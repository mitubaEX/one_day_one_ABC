while True:
    n = int(input())
    if n == 0:
        break
    w = list(map(int, input().split()))
    dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]

    def rec(l, r):
        # 既に計算済み？
        if dp[l][r] != -1:
            return dp[l][r]

        # これ以上取り除けない？
        if abs(l - r) <= 1:
            return 0

        res = 0
        # パターン1.
        if abs(w[l] - w[r - 1]) <= 1 and rec(l + 1, r - 1) == r - l - 2:
            res = r - l

        # パターン２.区間を分ける
        for mid in range(l + 1, r - 1):
            res = max(res, rec(l, mid) + rec(mid, r))

        dp[l][r] = res
        return res

    print(rec(0, n))
