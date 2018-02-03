n = int(input())
lis = [ '2' for i in range(int(n / 2)) ]
a = list(sorted(lis if n % 2 == 0 else lis + ['1']))
print(len(a))
[ print(i) for i in a ]
