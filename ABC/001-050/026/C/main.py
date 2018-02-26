# 高橋くんの社員番号1
# 1の人をピックする -> そいつの部下(2)をピックする -> あとは再帰
# 2の給料が求まったら max(2) + min(2) + 1する

import collections

dic = collections.defaultdict(lambda: 0)
max_num = 0
def add_dict(num):
    dic[num] += 1
    max_num = max(num, max_num)
[add_dict(int(input())) for i in range(int(input()))]

# maxを求めて，そこから1 -> 3 -> 7 -> 15 -> 31
# 部下が一人のみの場合は，2倍+1 1 -> 3 -> 7 -> 15
# 一人しかいない場合も変わらないっぽい




