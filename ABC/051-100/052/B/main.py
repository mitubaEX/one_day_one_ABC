input()
max_num = 0
count = 0
for i in list(input()):
    if 'I' == i:
        count += 1
    else:
        count -= 1
    max_num = max(max_num, count)
print(max_num)
