import math
print(sum([ n**2 * math.pi * -1 if index % 2 == 1 else (n**2) * math.pi for index, n in enumerate(sorted([ int(input()) for i in range(int(input())) ], reverse=True))]))
