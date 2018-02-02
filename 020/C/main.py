import sys
import queue
import math
sys.setrecursionlimit(10000)

# Pair
class Pair:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

h, w, t = map(int, input().split())
sx, sy, gx, gy = 0, 0, 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# input_map = [ list(input()) for i in range(h) ]
input_map = []
for i in range(h):
    lis = list(input())
    input_map.append(lis)
    if 'S' in lis:
        sx = lis.index('S')
        sy = i
    if 'G' in lis:
        gx = lis.index('G')
        gy = i

# 二分探索
# MAXをどうする
# 白1 sec  黒x sec
# MAX = 白 x 1 + 黒 + x
# MAX = t

# bfs
def bfs(index):
    que = queue.Queue()
    INF = sys.maxsize
    d = [[INF for i in range(w)] for l in range(h)] # width x heightの配列を作って，INFで埋める
    que.put(Pair(sx, sy))
    d[sy][sx] = 0 # スタートを0に

    while not que.empty():
        p = que.get()

        # ゴールに到達した場合
        if p.x == gx and p.y == gy:
            break

        for i in range(4):
            nx = p.x + dx[i]
            ny = p.y + dy[i]
            if 0 <= nx and nx < w and 0 <= ny and ny < h and d[ny][nx] == INF:
                que.put(Pair(nx, ny))
                if input_map[ny][nx] == '#':
                    d[ny][nx] = d[p.y][p.x] + index
                else:
                    d[ny][nx] = d[p.y][p.x] + 1
    return d[gy][gx]

def nibun(mini, maxi):
    # hanbun
    index = int((mini + maxi) / 2)
    print('mini:{0}, maxi:{1}'.format(mini, maxi))
    if mini == maxi or abs(mini - maxi) == 1:
        return maxi

    res = bfs(index)
    if res < t:
        return nibun(index, maxi)
    else:
        return nibun(mini, index)

print(nibun(1, t))

# print('{0}, {1}, {2}, {3}'.format(sx, sy, gx, gy))
