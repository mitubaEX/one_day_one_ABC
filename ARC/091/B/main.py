n, k = map(int, input().split())
count = 0
for i in range(k + 1, n + 1):
    ro = round((i - k) * n / i)
    print(ro)
    count += ro
print(count)
# lis = [i + 1 for i in range(k, n)]
# print(lis)
# import itertools
# it = itertools.product(lis, repeat=2)
# fil_lis = list(filter(lambda x: x[0] % x[1] >= k, it))
# print(fil_lis)
# print(len(fil_lis))
