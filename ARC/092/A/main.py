n = int(input())

a_lis = [list(map(int, input().split()))for _ in range(n)]
b_lis = [list(map(int, input().split()))for _ in range(n)]

sorted_a = sorted(sorted(a_lis, key=lambda x: x[0]), key=lambda y: y[1])
sorted_b = sorted(sorted(b_lis, key=lambda x: x[0]), key=lambda y: y[1])

arrive = []

for i in sorted_b:
    for index, j in enumerate(sorted_a):
        if j[0] < i[0] and j[1] < i[1] and index not in arrive:
            arrive.append(index)
            break

print(len(arrive))
