n, s, t = map(int, input().split())
w = int(input())
count = (1 if s <= w <= t else 0)
for i in range(n - 1):
    w += int(input())
    if s <= w <= t:
        count += 1
print(count)
