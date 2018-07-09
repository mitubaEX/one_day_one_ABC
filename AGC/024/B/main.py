n = int(input())

lis = [ int(input()) for i in range(n) ]

remove_count = 0
count = 0

while len(lis) != 0:
    print(lis)
    min_num = min(lis)
    min_index = lis.index(min_num)

    print('{0}, {1}'.format(min_num, min_index))
    # remove only
    if min_index == 0:
        lis.pop(min_index)
        remove_count += 1
        # count += remove_count
    else:
        lis.pop(min_index)
        remove_count += 1
        count += remove_count
    print(remove_count, count)

print(count)
