inp = input()
arr = [1, 2, 3, 4, 5, 6]
for i in xrange(inp % 30):
    tmp = arr[i % 5]
    arr[i % 5] = arr[i % 5 + 1]
    arr[i % 5 + 1] = tmp
    print i,arr

print "".join(map(str, arr))
