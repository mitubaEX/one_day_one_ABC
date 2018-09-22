lis = map(int, input().split())
sortedt = reversed(list(sorted(lis)))
cost = 0
cost += sortedt[1]
cost += abs(sortedt[2] - sortedt[1])

print(cost)
