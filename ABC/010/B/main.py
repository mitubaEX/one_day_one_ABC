int(input())
cost = 0
for i in map(int, input().split()):
    if i == 2:
        cost += 1
    elif i == 4:
        cost += 1
    elif i == 5:
        cost += 2
    elif i == 6:
        cost += 3
    elif i == 8:
        cost += 1
print(cost)
