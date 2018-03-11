dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

# 0 裏 1 表
n, m = map(int, input().split())
# count = 0
# if n == 1 or m == 1:
#     for i in range(n):
#         for j in range(m):
#             xy_count = 0
#             for x, y in zip(dx, dy):
#                 if i + y == -1 or i + y == n or j + x == -1 or j + x == m:
#                     continue
#                 # lis[i + y][j + x] = not lis[i + y][j + x]
#                 xy_count += 1
#             if xy_count % 2 == 0:
#                 count += 1
#     print(count)
# else:
print(abs(n * m - (2 * n + 2 * m - 4)))
# lis = [[False for i in range(m)] for i in range(n)]
# print(lis)
# count = 0
# for i in range(1, n - 1):
#     for j in range(1, m - 1):
#         xy_count = 0
#         for x, y in zip(dx, dy):
#             if i + y == -1 or i + y == n or j + x == -1 or j + x == m:
#                 continue
#             # lis[i + y][j + x] = not lis[i + y][j + x]
#             xy_count += 1
#         if xy_count % 2 == 0:
#             count += 1
# else:
#     lis[i][j] = True

# print(lis)
# count = 0
# for i in range(n):
#     for j in range(m):
#         if not lis[i][j]:
#             count += 1
