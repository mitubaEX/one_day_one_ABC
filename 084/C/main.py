m = []

def solve(index):
    time = 0
    for i in m[index:]:
        if time <= i[1]:
            time = i[1]
            time += i[0]
        else:
            tmp = i[1]
            while True:
                if time <= tmp:
                    break
                else:
                    tmp += i[2]
            time = tmp
            time += i[0]
    return time

n = input()
for i in xrange(n - 1):
    m.append(map(int, raw_input().split(" ")))
for i in xrange(n):
    print solve(i)


