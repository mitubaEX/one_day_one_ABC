# K個
# N円の品物
init_list = [i + 1 for i in range(10)]
n, k = map(int, input().split())
dont_like_list = list(map(int, input().split()))


def convert(num):
    return_str = list(str(num))
    for index, i in enumerate(list(str(num))):
        # 嫌いな数字だったら
        if i in dont_like_list:
            return_str[index] = str(int(i) + 1)
    join_str = int(''.join(return_str))
    if join_str == num:
        return (True, join_str)
    return (False, join_str)


while True:
    flag, n = convert(n)
