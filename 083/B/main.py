def calc(num):
    ans = 0
    for i in str(num):
        ans += int(i)
    return ans


n, a, b = map(int, raw_input().split(" "))
lis = []
for i in xrange(n):
    tmp = calc(i + 1)
    if a <= tmp  and tmp <= b:
        lis.append(i + 1)

print sum(lis)
