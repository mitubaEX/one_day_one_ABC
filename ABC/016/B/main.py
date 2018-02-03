a, b, c = map(int, input().split())

plus, minus = False, False

if (a + b) == c:
    plus = True
if (a - b) == c:
    minus = True

if plus and minus:
    print('?')
elif plus:
    print('+')
elif minus:
    print('-')
else:
    print('!')
