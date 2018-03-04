dic = {}
for i in [input() for i in range(int(input()))]:
    if i[0] == 'M' or i[0] == 'A'or i[0] == 'R'or i[0] == 'C'or i[0] == 'H':
        if i[0] not in dic:
            dic[i[0]] = [i]
        else:
            dic[i[0]].append(i)

sum_dict = {}
print(dic)
if len(list(dic.keys())) == 0:
    print(0)
else:
    sum_num = 0
    dic_list = list(dic.keys())
    for index, i in enumerate(dic_list):
        if index + 2 >= len(dic_list):
            break
        sum_dict[i] = dic_list[index + 2:]
    print(sum_dict)
    ans_dic = {}
    for i in dic.keys():
        if len(dic[i]) > 1:
            for l in sum_dict.keys():
                if i in sum_dict[l] or i in sum_dict:
                    print('{0}, {1}'.format(len(sum_dict[l]), len(dic[i])))
                    ans_dic[l] = len(sum_dict[l]) * len(dic[i])
            # sum_dict[i] *= len(dic[i])
        elif i in sum_dict:
            ans_dic[i] = len(sum_dict[i])
        print(ans_dic)
    print(ans_dic)
