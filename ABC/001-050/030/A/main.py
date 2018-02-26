a, b, c, d = map(int, input().split())
if float(b/a) > float(d/c):
    print('TAKAHASHI')
elif float(b/a) < float(d/c):
    print('AOKI')
else:
    print('DRAW')
