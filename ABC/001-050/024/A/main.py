# 子供A 大人B K人以上C円引き
# 子供S 大人T

a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
ans = s * a + b * t
if k <= (s + t):
    print(ans - (c * (s + t)))
else:
    print(ans)
