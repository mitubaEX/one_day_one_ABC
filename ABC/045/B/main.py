a = list(input())
b = list(input())
c = list(input())

import sys

turn = 'a'
while True:
    if len(a) == 0 and turn == 'a':
        print('A')
        sys.exit(0)
    elif len(b) == 0 and turn == 'b':
        print('B')
        sys.exit(0)
    elif len(c) == 0 and turn == 'c':
        print('C')
        sys.exit(0)

    if turn == 'a':
        turn = a[0]
        del a[0]
    elif turn == 'b':
        turn = b[0]
        del b[0]
    elif turn == 'c':
        turn = c[0]
        del c[0]
