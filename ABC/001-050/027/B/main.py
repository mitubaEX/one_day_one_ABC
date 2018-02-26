int(input())
lis = list(map(int, input().split()))

per = sum(lis) / len(lis)
bridg = 0

if per == int(per):
    i = 0
    while True:
        if min(lis) == per:
            break
        if min(lis) == lis[i]:
            i += 1
            continue
        else:
            num = lis[i]

            while True:
                if num == per:
                    break
                if lis[i + 1] == per:
                    bridg += 1
                    i += 1
                    continue
                else:
                    bridg += 1
                    num -= per
    print(bridg)
else:
    print(-1)

