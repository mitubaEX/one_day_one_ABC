n, m = map(int, input().split())
# non 0 student 1 check 2
n_lis = [list(map(int, input().split())) for i in range(n)]
m_lis = [list(map(int, input().split())) for i in range(m)]
import sys

for i in n_lis:
    min_num = sys.maxsize
    ans_index = 0
    for index, j in enumerate(m_lis):
        # min_num = min(abs(i[0] - j[0]) + abs(i[1] - j[1]), min_num)
        num = abs(i[0] - j[0]) + abs(i[1] - j[1])
        if min_num > num:
            min_num = num
            ans_index = index + 1
    print(ans_index)
