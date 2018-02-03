class Pair:
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b

t = int(input())
sub = 2025 - t

import itertools

dic = {}

for x, y in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 2):
    an = x * y
    if an in dic:
        dic[an].append(Pair(x, y))
    else:
        dic[an] = []
        dic[an].append(Pair(x, y))

for x, y in zip([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]):
    an = x * y
    if an in dic:
        dic[an].append(Pair(x, y))
    else:
        dic[an] = []
        dic[an].append(Pair(x, y))



for i in dic[sub]:
    print(i.a, 'x', i.b)
