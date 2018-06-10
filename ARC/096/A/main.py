# ABピザ C

a, b, c, x, y = map(int, input().split())

# c * 2 <= a + b

sum_num = 0

if c * 2 <= a + b:
    sum_num = c * 2 * min(x, y)
    if x > y:
        sum_num += a * (x - y)
    else:
        sum_num += b * (y - x)
    if sum_num > c * 2 * max(x, y):
        sum_num = c * 2 * max(x, y)
else:
    sum_num += a * x + b * y

print(sum_num)
