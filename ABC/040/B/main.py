n = int(input())
sub = int(n ** 0.5)
min_num = 10000000

for i in range(1, sub + 1):
    y = 1
    while True:
        if i * y > n:
            break
        # print('sub: {0}, {1}'.format(i, y))
        min_num = min((abs(i - y)) + (n - i * y), min_num)
        y += 1
print(min_num)
