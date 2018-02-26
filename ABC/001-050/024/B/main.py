# T秒開く，開いている間通るとT秒延長
# N人



n, t = map(int, input().split())
times = [ int(input()) for i in range(n) ]

open_time = 0

def check(index):
    lis = []
    while True:
        if index + 1 == len(times):
            lis.append(times[index])
            return (index + 1, lis)
        sub = times[index + 1] - times[index]
        lis.append(times[index])
        if sub <= t:
            pass
        else:
            return (index + 1, lis)
        index += 1
    return (index, lis)

now = 0
split_list = []
for i in range(n):
    if now == i:
        now, lis = check(i)
        split_list.append(lis)

for i in split_list:
    if len(i) == 1:
        open_time += t
    else:
        open_time += i[len(i) - 1] - i[0] + t

print(open_time)
