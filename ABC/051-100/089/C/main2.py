def convert(input_lis):
    return [i[0] for i in input_lis]


lis = [i for i in [input() for i in range(int(input()))]
       if i[0] == 'M' or i[0] == 'A'or i[0] == 'R'or i[0] == 'C'or i[0] == 'H']
import itertools
ans_list = []
for i in [sorted(i) for i in [i for i in filter(lambda x: len(list(set(convert(x)))) == len(convert(x)),
                                                itertools.combinations(lis, 3))]]:
    if sorted(i) not in ans_list:
        ans_list.append(i)

print(len(ans_list))
