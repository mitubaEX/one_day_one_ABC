lis = list(map(int, input().split()))
res = [e for e in set(lis) if lis.count(e) == 1]
if len(res) == 0:
    print(lis[0])
else:
    print(res[0])

