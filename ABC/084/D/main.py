import math
import sys

def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial):
            input_list[s] = False

q = input()
lr = []
max_num = 0
INF = sys.maxint
input_list = sieve_of_erastosthenes(100000)
# prime_list = [i for i, b in enumerate(input_list) if b == True]
prime_list_append = []
sum_count = 0
for index, i in enumerate(input_list):
    if i and input_list[(index + 1) / 2]:
        # print i, (index + 1)/2, sum_count
        sum_count += 1
        prime_list_append.append(sum_count)
    else:
        prime_list_append.append(sum_count)

for ii in xrange(q):
    tmp = map(int, raw_input().split(" "))
    # count = 0
    # for j in prime_list_append[tmp[0]:tmp[1]]:
    #     count += 1
    print prime_list_append[tmp[1]] - prime_list_append[tmp[0]-1]
