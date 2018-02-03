dic = {}
for i in range(int(input())):
    name = input()
    if name in dic.keys():
        dic[name] += 1
    else:
        dic[name] = 1

max_score = 0
max_name = ''
for i in dic.keys():
    if max_score <= dic[i]:
        max_score = dic[i]
        max_name = i
    # max_score = max(dic[i], max_score)

print(max_name)
