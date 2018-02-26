# 'a' + str + 'b'
# 'c' + str + 'a'
# 'b' + str + 'b'

n = int(input())
ans = input()
count = 0
turn = 0
s = 'b'

while True:
    if len(s) > n:
        print(-1)
        break
    elif ans == 'b':
        print(0)
        break
    else:
        if turn == 0:
            s = 'a' + s + 'c'
            turn += 1
            count += 1
        elif turn == 1:
            s = 'c' + s + 'a'
            turn += 1
            count += 1
        elif turn == 2:
            s = 'b' + s + 'b'
            turn = 0
            count += 1
        if s == ans:
            print(count)
            break
