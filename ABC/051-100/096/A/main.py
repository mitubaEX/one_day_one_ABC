a, b = map(int, input().split())

count = 0
for i, j in zip([x for x in range(1, 12)], [x for x in range(1, 12)]):
    if i >= a and j >= b:
        break
    count += 1
print(count)
