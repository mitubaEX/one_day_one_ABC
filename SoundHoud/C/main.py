dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# r tate c yoko
import sys
sys.setrecursionlimit(10000)
r, c = map(int, input().split())
lis = []
count = 0

def solve(lis, i, j, now_count, cell_count, arrive):
    global count

    arrive[i][j] = 1
    if cell_count >= r * c:
        count = max(count, now_count)
        return;

    if lis[i][j] == '.':
        flag = True
        for x, y in zip(dx, dy):
            if (i + y == -1 or i + y >= r) or (j + x == -1 or j + x >= c):
                pass
            elif lis[i + y][j + x] == '#':
                flag = False
        if flag == True:
            lis[i][j] = '#'
            now_count += 1
            count = max(count, now_count)
    print('#############')
    for i in range(r):
        for j in range(c):
            print(lis[i][j])
        print()
    for x, y in zip(dx, dy):
        if not (i + y == -1 or i + y >= r) and not (j + x == -1 or j + x >= c) and lis[i + y][j + x] == '.' and arrive[i + y][j + x] == 0:
            cell_count += 1
            solve(lis, i + y, j + x, now_count, cell_count, arrive)




for i in range(r):
    lis.append(list(input()))

arrive = [[0 for l in range(c)] for i in range(r)]

# .の時関数に渡してドンドン読んでいく
for i in range(r):
    for j in range(c):
        if lis[i][j] == '.':
            solve(lis, i, j, 1, 1, arrive)
print(count)
