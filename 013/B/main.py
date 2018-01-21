a = int(input())
b = int(input())
sub = abs(a - b)
if sub < 5:
    print(sub)
else:
    if a > b:
        print(abs(b + 10 - a))
    else:
        print(abs(a + 10 - b))
