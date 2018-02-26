lis = list(sorted(list(map(int, input().split()))))
if lis[2] == lis[0] + lis[1]:
    print('Yes')
else:
    print('No')
