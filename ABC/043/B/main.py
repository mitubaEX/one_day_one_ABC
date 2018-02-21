# lis = [i for i in input().split('B')]
# print(''.join([i[:-1] if index < len(lis) -
#                1 else i for index, i in enumerate(lis)]))
ans_str = ''
for i in list(input()):
    if i == 'B':
        ans_str = list(ans_str)[:-1]
    else:
        ans_str += i
print(''.join(ans_str))
