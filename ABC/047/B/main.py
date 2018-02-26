w, h, n = map(int, input().split())

ma = [[0 for i in range(w)] for i in range(h)]


# a == 1 x < xi
# a == 2 x > xi
# a == 3 y < yi
# a == 4 y > yi

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(x):
            for j in range(h):
                ma[j][i] = 1
    if a == 2:
        for i in range(x, w):
            for j in range(h):
                ma[j][i] = 1
    if a == 3:
        for i in range(y):
            for j in range(w):
                ma[i][j] = 1
    if a == 4:
        for i in range(y, h):
            for j in range(w):
                ma[i][j] = 1

count = 0
for i in range(h):
    for j in range(w):
        if ma[i][j] == 0:
            count += 1
print(count)
