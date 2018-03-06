a, b = map(int, input().split())
if a == 1:
    a = 14
if b == 1:
    b = 14
def calc(a, b):
    if a > b:
        return 'Alice'
    elif a < b:
        return 'Bob'
    else:
        return 'Draw'
print(calc(a, b))
