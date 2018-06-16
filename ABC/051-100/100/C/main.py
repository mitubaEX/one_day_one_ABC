n = int(input())
lis = map(int, input().split())

fil = list(filter(lambda x: x % 2 == 0, lis))


def soinsuu(giv):
    co = 0
    while True:
        if giv % 2 == 1:
            break
        giv /= 2
        co += 1

    return co


count = 0
for i in fil:
    import math
    count += int(soinsuu(i))
print(count)
