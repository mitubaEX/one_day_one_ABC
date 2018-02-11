# a = list(map(int, input().split()))
# print(a[len(a) - 1] + a[len(a) - 2] + a[0])
a = list(map(int, input().split()))
import itertools
b = list(sorted(set([i + j + k for i, j, k in itertools.permutations(a, 3)])))
print(b[len(b) - 3])
