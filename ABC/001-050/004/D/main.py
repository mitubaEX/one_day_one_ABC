r, g, b = map(int, raw_input().split(" "))
rco = 0
for i in xrange(r - 1):
    rco += i + 1
print rco
bco = 0
for i in xrange(b - 1):
    bco += i + 1
print bco

gco = 0
if g > 196:
    for i in xrange(98):
        gco += i + 1
    for i in xrange(98):
        gco += i + 1
    if r > b:
        for l in xrange(g - 196):
            gco += b + 98 + l + 1
    else:
        for l in xrange(g - 196):
            gco += r + 98 + l + 1
else:
    for i in xrange(g - 1):
        gco += i + 1
print gco

print rco + bco + gco
