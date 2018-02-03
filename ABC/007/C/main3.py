class Pair:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
import copy
import queue
sys.setrecursionlimit(10000)

# define
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

height, width = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())
sy = start_y - 1
sx = start_x - 1
gy = goal_y - 1
gx = goal_x - 1

input_map = []

for i in range(height):
    input_map.append(list(input()))

def bfs():
    que = queue.Queue()
    INF = sys.maxsize
    d = [[INF for i in range(width)] for l in range(height)]
    que.put(Pair(sx, sy))
    d[sy][sx] = 0

    while not que.empty():
        p = que.get()

        # ゴールに到達した場合
        if p.x == gx and p.y == gy:
            break

        for i in range(4):
            nx = p.x + dx[i]
            ny = p.y + dy[i]
            if 0 <= nx and nx < width and 0 <= ny and ny < height and input_map[ny][nx] != '#' and d[ny][nx] == INF:
                que.put(Pair(nx, ny))
                d[ny][nx] = d[p.y][p.x] + 1
    return d[gy][gx]

print(bfs())
