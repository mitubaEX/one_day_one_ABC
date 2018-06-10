h, w = map(int, input().split())
ma = [list(input()) for i in range(h)]

# 連結しているものが一つもなければNo

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
import sys
for i in range(h):
    for j in range(w):
        if ma[i][j] == '#':
            flag = False
            for x, y in zip(dx, dy):
                if j + x < 0 or i + y < 0 or j + x >= w or i + y >= h:
                    continue

                if ma[i + y][j + x] == '#':
                    flag = True

            if flag == False:
                print('No')
                sys.exit(0)
print('Yes')
sys.exit(0)
