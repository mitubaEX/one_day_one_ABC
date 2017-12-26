a, b, c, d = map(int, raw_input().split(" "))
if a+b == c+d:
    print "Balanced"
elif a+b > c+d:
    print "Left"
else:
    print "Right"
