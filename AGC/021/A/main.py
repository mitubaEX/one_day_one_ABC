lis = list(map(int, list(input())))

for i in reversed(range(len(lis))):
    if i - 1 == -1:
        break
    if lis[i] < 9:
        lis[i-1] -= 1
        lis[i] = 9

print(sum(lis))
