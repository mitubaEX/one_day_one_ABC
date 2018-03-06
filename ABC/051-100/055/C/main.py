n, m = map(int, input().split())
import sys

if n > int(m / 2):
    print(int(m / 2))
    sys.exit(0)

print(n + int((m - n * 2) / 4))

# while True:
#     if n > (m - 2) / 2:
#         break
#     else:
#         n += 1
#         m -= 2
# print(int(m / 2))
