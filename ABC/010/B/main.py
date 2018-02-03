# 2 5 8
# 2 4 6 8

p1 = [2, 4, 6, 8]
p2 = [2, 5, 8]

int(input())
a = map(int, input().split(" "))
count = 0
for i in a:
    flag = False
    j = 0
    before_num = 0
    for j in p1:
        if j >= i:
            flag = True
            break
        before_num = j

    if flag:
        count += i - before_num
    else:
        count += j - i

