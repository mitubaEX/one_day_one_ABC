n, l, r = map(int, input().split())
lis = []
for x in map(int, input().split()):
    if x < l:
        lis.append(str(l))
    elif x > r:
        lis.append(str(r))
    else:
        lis.append(str(x))

print(' '.join(lis))
