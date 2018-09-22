n, x = map(int, input().split())

lis = map(int, input().split())


count = 0
for i in sorted(lis):
    x -= i
    if x < 0:
        break
    count += 1

if x > 0:
    count -= 1

print(count)
