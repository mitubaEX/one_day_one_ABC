s = input()
flag = False
if s[-2:] == 'ch':
    flag = True
for i in ['o', 'k', 'u']:
    if s[-1:] == i:
        flag = True

if flag:
    print('YES')
else:
    print('NO')
