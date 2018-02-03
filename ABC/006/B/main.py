tri = []
tri.append(0)
tri.append(0)
tri.append(1)
inp = input()
for i in xrange(inp):
    tri.append((tri[i + 2] + tri[i + 1] + tri[i]) % 10007)
print tri[inp - 1]
