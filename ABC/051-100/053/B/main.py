s = list(input())

print(len(s) - list(reversed(s)).index('Z') - s.index('A'))
