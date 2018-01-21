lis = []
for i in range(int(input())):
    lis.append(int(input()))

print(sorted(list(set(lis)), reverse=True)[1])

