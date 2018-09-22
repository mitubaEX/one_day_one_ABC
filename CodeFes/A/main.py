a = int(input())
b = int(input())
c = int(input())
s = int(input())

s -= a + b + c

if s <= 3 and s >= 0:
    print('Yes')
else:
    print('No')
