s = input()
n = int(input())
lis = [ list(map(int, input().split())) for i in range(n)]

for i in lis:
    s = s[:i[0] - 1] + ''.join(list(reversed(s[i[0] - 1:i[1]]))) + s[i[1]:]

print(s)

