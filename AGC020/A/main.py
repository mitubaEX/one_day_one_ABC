n, a, b = map(int, input().split())
sub = b - a
if sub % 2 == 0:
    print('Alice')
else:
    print('Borys')
