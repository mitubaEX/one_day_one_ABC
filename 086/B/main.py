import math

def try_square_root_naive(n):
    m = int(n**.5)
    return m if abs(m*m - n) < 1e-6 else None

a, b = input().split()
# print(math.sqrt(int(a + b)))
result = try_square_root_naive(int(a + b))
if result != None:
    print('Yes')
else:
    print('No')


