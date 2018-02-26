# l分以上h分以下
l, h = map(int, input().split())
for a in [int(input()) for i in range(int(input()))]:
    if l <= a and a <= h:
        print(0)
    elif a < l:
        print(l - a)
    else:
        print(-1)
