n = int(input())
a = [ int(input()) for _ in range(n) ]
b = set()
cnt = 0
for i in a:
    if i in b:
        cnt += 1
    b.add(i)
print(cnt)
