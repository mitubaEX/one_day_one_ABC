def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x, y = map(int, input().split())

# 同じ数字の場合
if x == y:
    print(-1)
else:
    g = gcd(x, y)
    if (x * g) % y != 0:
        print(x * g)
    else:
        if x * (g + 1) % y != 0:
            print(x * (g + 1))
        else:
            print(-1)

