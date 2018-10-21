n = int(input())
li = list(map(int, input().split()))

even = []
odd = []

for index, i in enumerate(li):
    if index % 2 == 0:
        even.append(i)
    elif index % 2 != 0:
        odd.append(i)

from collections import Counter
so_ev = Counter(even).most_common(2)
so_od = Counter(odd).most_common(2)

if so_ev[0][0] == so_od[0][0]:
    if len(so_ev) == 1 and len(so_od) == 1:
        print(n - so_ev[0][1])
    else:
        print(min(n - so_ev[1][1] - so_od[0][1], n - so_ev[0][1] - so_od[1][1]))
else:
    print(n - so_ev[0][1] - so_od[0][1])
