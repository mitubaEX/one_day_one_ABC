def calc(lis, m_lis):
    copy_list = lis[:]
    copy_list[m_lis[0] - 1] = m_lis[1]
    print(sum(copy_list))


int(input())
lis = list(map(int, input().split()))
[calc(lis, i) for i in [list(map(int, input().split()))
                        for i in range(int(input()))]]
