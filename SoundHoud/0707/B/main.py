s = list(input())
n = int(input())

count = 1
ans = s[0]

for i in s[1:]:
    if count == n:
        count = 0
        ans += i
    count += 1

print(ans)
