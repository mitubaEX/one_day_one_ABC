from collections import defaultdict
n = int(input())
frequence = defaultdict(lambda: 0)
def add_frequence(num):
    global frequence
    frequence[num] += 1
[ add_frequence(int(input())) for l in range(n) ]
# print()
# for i in frequence.keys():
#     print(i, frequence[i])
# print()
print(sum(list(map(lambda x: int(frequence[x] / 2) if int(frequence[x] % 2 == 0) or frequence[x] == 1 else int((frequence[x] + 1) / 2), frequence.keys()))))

