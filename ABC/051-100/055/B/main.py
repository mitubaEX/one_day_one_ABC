sum_num = 1
for i in range(1, int(input()) + 1):
    sum_num = (sum_num * i) % (10**9 + 7)
print(sum_num)
