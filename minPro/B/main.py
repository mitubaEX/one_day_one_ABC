import sys
x, k = map(int, input().split())

y = 10 ** k
if k == 0:
    print(x + 1)
    sys.exit(1)

while True:
    tmp = 1
    if str(y)[len(str(y)) - k:].isdigit():
        tmp = int(str(y)[len(str(y)) - k:])
    if x + 1 <= y and tmp == 0:
        print(y)
        break
    y += 1
