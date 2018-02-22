n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n - k > 0:
    print(k * x + (n - k) * y)
else:
    print(n * x)
