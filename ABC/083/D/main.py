s = list(raw_input())
flag = False
count = 0
ans = 0
last_flag = False
for index, i in enumerate(reversed(s)):
    if index == len(s) - 1 and i == '1':
        last_flag = True
        break
    if i == '1' and flag == False:
        flag = True
        s[len(s) - index - 1] = '0'
        count += 1
    elif i == '1' and flag:
        s[len(s) - index - 1] = '0'
        count += 1
    else:
        ans = max(count, ans)
        count = 0
        flag = False
    print s

if last_flag:
    ans = max(ans, len(s) - 1)
    print ans
else:
    print ans
