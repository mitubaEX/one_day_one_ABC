import sys
class Pair:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

dx = [0,0,1,-1];
dy = [1,-1,0,0];
import Queue
r, c = map(int, raw_input().split(" "))
INF = sys.maxint

d = []
for i in xrange(r):
    d.append([INF for x in xrange(c)])

sx, sy = map(int, raw_input().split(" "))
gx, gy = map(int, raw_input().split(" "))

xymap = []
for i in xrange(r):
    xymap.append(raw_input().split(" "))
for i in xrange(r):
    print xymap[i]

q = Queue.Queue()
p = Pair(sx, sy)
q.put(p)
print p.x, p.y
d[sy][sx] = 0

while not q.empty():
    tmp_p = q.get()
    x = tmp_p.x - 1
    y = tmp_p.y - 1
    if x == gx and y == gy:
        break
    for i in xrange(4):
        mx = x + dx[i]
        my = y + dy[i]
        print mx, my
        if mx < 0 or my < 0 or mx >= c or my >= r:
            continue
        for i in xrange(r):
            print d[i]
        if xymap != '#' and d[my][mx] == INF:
            q.put(Pair(mx, my))
            d[my][mx] = d[y][x] + 1;

print d[gy][gx]
