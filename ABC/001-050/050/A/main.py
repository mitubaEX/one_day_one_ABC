lis = list(input().split())
print(int(lis[0]) + int(lis[2]) if lis[1]
      == '+' else int(lis[0]) - int(lis[2]))
