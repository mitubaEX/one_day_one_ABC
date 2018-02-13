n, m = map(int, input().split())

if n >= 12:
    n -= 12

tan = (360 / 12)
tyou = (360 / 60)
ans = abs((n * tan + m * tan / 60) - m * tyou)

if ans > 180:
    print(360 - ans)
else:
    print(ans)
