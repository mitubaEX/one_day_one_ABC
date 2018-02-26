s = list(input())
n = int(input())

import itertools

print(list(sorted([i + j for i, j in itertools.product(s, repeat=2)]))[n - 1])
