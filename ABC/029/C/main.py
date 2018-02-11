import itertools
[print(''.join(i)) for i in itertools.product('abc', repeat=int(input()))]
