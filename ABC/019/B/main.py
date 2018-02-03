lis = list(input())
before_string = lis[0]
count = 1
ans_string = ''
for i in lis[1:]:
    if before_string != i:
        ans_string += before_string + str(count)
        before_string = i
        count = 1
    else:
        count += 1
ans_string += before_string + str(count)
print(ans_string)
