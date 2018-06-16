# 1 6^ 9^

n = int(input())

# その数までのリストを持っておく

lis = [1]
head = 6
val = 6
while True:
    if n < head:
        break
    lis.append(head)
    head = val * head

head = 9
val = 9
while True:
    if n < head:
        break
    lis.append(head)
    head = val * head

# print(lis)

count = 0
while True:
    if n == 0:
        break
    if n < 20:
        six_per = int(n / 6)
        nine_per = int(n / 9)
        if six_per > nine_per:
            n = n - six_per * 6
            count += six_per
            count += n
        else:
            n = n - nine_per * 9
            count += nine_per
            count += n
        break

    tmp = 0
    for i in reversed(sorted(lis)):
        if n >= i:
            tmp = i
            count += 1
            break
    n -= tmp
    # print(n)

print(count)
