from statistics import mean, median,variance,stdev
import sys

sys.setrecursionlimit(10000)

n = int(input())
lis = list(map(int, input().split()))
ans_list = []

## bitを立てるか立てないかの二通り
## すでにdpに値があればそれを利用し，再帰をする
## DPはINFで初期化
## DPがINFのときのみ更新作業を行う

def dfs(i, su):
    # n個決め終わった時
    if i == n:
        if su != 0:
            ans_list.append(su)
        return
    dfs(i + 1, su)
    dfs(i + 1, su + lis[i])


dfs(0, 0)
print(median(list(sorted(ans_list))))
