x = input()
print int(sum([ 10000.0 * float((i + 1) * 1.0) / float(x * 1.0) for i in xrange(x)]))
