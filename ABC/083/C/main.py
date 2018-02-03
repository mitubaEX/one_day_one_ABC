x, y = map(int, raw_input().split(" "))
count = 2
ans = x * 2
if x == y:
    print 0
else:
    while True:
        ans *= 2
        if ans > y:
            break
        count += 1

    print count
