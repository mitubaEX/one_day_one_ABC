li = [int(input()) for i in range(3)]
sorted_list = list(reversed(sorted(li)))
[print(sorted_list.index(i) + 1) for i in li]

