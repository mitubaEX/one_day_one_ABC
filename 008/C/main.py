# omote / N!

import itertools
import math

lis = []
bool_list = []
def get_result_list(num, index, input_list):
    return_list = input_list
    current_index = index + 1
    for i in input_list[index + 1:]:
        if i % num == 0:
            bool_list[current_index] = not bool_list[current_index]
        current_index += 1


# input
in_num = int(input())
for i in range(in_num):
    lis.append(int(input()))


all_count = 0
for x in itertools.permutations(lis):
    bool_list = [True for i in range(in_num)]
    for index, i in enumerate(x):
        get_result_list(i, index, x)
    all_count += bool_list.count(True)

print(all_count / math.factorial(in_num))
