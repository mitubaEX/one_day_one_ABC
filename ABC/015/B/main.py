import math
input()
lis = list(filter(lambda n:n != 0, map(int, input().split())))
print(math.ceil(sum(lis) / len(lis)))
