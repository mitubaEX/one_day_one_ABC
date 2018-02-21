lis = list(map(int, input().split()))
filtered_list_5 = list(filter(lambda x: x == 5, lis))
filtered_list_7 = list(filter(lambda x: x == 7, lis))
if len(filtered_list_5) == 2 and len(filtered_list_7) == 1:
    print('YES')
else:
    print('NO')
