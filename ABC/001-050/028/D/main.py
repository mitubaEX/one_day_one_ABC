n, k = map(int, input().split())
a = [i + 1 for i in range(n)]
sort_a = sorted(a, reverse=True)
import itertools
import statistics
count = 0
# print(len([statistics.median(i) for i in itertools.product(a, repeat=len(a)) if statistics.median(i) == k]) / len(a) ** len(a))

# dp

ans_lis = []
for i in itertools.product(sort_a, repeat=len(sort_a)):
    if sum(i) <= k:
        break
    else:
        tmp = statistics.median(i)
        if tmp == k:
            ans_lis.append(tmp)

len(ans_lis) / (len(a) ** len(a))
