a, b, c = map(int, input().split())
num = 0
while True:
    num += a
    if num % b == c:
        print('YES')
        break
    if num == a * b:
        print('NO')
        break
