# 0, 0
# L -1, 0
# R +1, 0
# U 0, +1
# D 0, -1

s = list(input())
ans_x, ans_y = 0, 0
removed_s = list(filter(lambda x: x != '?', s))

if int(input()) == 1:
    for i in removed_s:
        if i == 'L':
            ans_x -= 1
        elif i == 'R':
            ans_x += 1
        elif i == 'U':
            ans_y += 1
        elif i == 'D':
            ans_y -= 1
    for i in range(len(s) - len(removed_s)):
        if ans_x < 0:
            ans_x -= 1
        else:
            ans_x += 1

else:
    for i in removed_s:
        if i == 'L':
            ans_x -= 1
        elif i == 'R':
            ans_x += 1
        elif i == 'U':
            ans_y += 1
        elif i == 'D':
            ans_y -= 1
    for i in range(len(s) - len(removed_s)):
        if ans_x > 0:
            ans_x -= 1
        else:
            ans_x += 1

print(abs(ans_x) + abs(ans_y))
