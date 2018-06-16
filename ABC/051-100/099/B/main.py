# 1 3 6 10 15

a, b = map(int, input().split())

sub = b - a

sum_num = 0
for i in range(sub):
    sum_num += i + 1

print(sum_num - b)
