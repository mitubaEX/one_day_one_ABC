# iを打ってxi円設ける
# 価値vi 価格ci

int(input())
x = list(map(int, input().split()))
c = list(map(int, input().split()))
v = list(map(int, input().split()))
c_v_weight = [ j / i for i,j in zip(c, v) ]
aoki_used = []

takahasi_index = 0
takahasi_money = 0
takahasi_value = 0
while True:
    if len(c) == 0:
        break
    if takahasi_money < c[v.index(max(v))]:
        takahasi_money += x[takahasi_index]
        takahasi_index += 1
        tmp_index = 0
        print(len(c), c_v_weight.index(max(c_v_weight)))
        if takahasi_money >= c[c_v_weight.index(max(c_v_weight))]:
            tmp_index = c_v_weight.index(list(sorted(c_v_weight))[len(c_v_weight) - 1])
        else:
            tmp_index = c_v_weight.index(list(sorted(c_v_weight))[len(c_v_weight) - 2])
        del v[tmp_index]
        del c[tmp_index]
        del c_v_weight[tmp_index]
    else:
        max_value_index = c_v_weight.index(max(c_v_weight))
        takahasi_money -= c[max_value_index]
        takahasi_value += v[max_value_index]
        # print(v[max_value_index])
        del c[max_value_index]
        del v[max_value_index]
        del c_v_weight[max_value_index]
print(takahasi_value)
