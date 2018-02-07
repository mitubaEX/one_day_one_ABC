n, a, b = map(int, input().split())

position = 0
for i in [list(input().split()) for i in range(n)]:
    multi = 1
    if 'West' == i[0]:
        multi = -1
    elif 'East' == i[0]:
        multi = 1
    if int(i[1]) < a:
        position += a * multi
    elif a <= int(i[1]) and int(i[1]) <= b:
        position += int(i[1]) * multi
    elif int(i[1]) > b:
        position += b * multi

if position < 0:
    print('West {0}'.format(position * -1))
elif position > 0:
    print('East {0}'.format(position))
else:
    print(0)

