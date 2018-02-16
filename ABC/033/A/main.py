lis = list(map(int, list(input())))
if len(list(filter(lambda x: x != lis[0], lis))) == 0:
    print("SAME")
else:
    print("DIFFERENT")
