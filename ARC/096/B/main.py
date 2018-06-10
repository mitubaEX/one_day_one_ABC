# N kann xi kyori vi enegy C gaisyuu

n, c = map(int, input().split())

lis = [list(map(int, input().split())) for i in range(n) ]

print(lis)

# max score

# xi == c - xi 反対周り

# 今いる距離から歩いて xi < vi だったら価値がある
# 基本的に時計回りに反時計回りに行くかの二択
# 最初が不利益だとしても後から利益が出てくるかもしれない
# 今のpositionにおける各点の距離のリストが欲しい
# 最優良物件順に並べる（逆回りも全て）

head_index = 0
last_index = -1

head = lis[0]
tail = lis[-1]
position = 0
cost = 0
max_cost = 0

while(True):
    if head_index - last_index == len(lis):
        break
    print()
    print()
    if head[1] - abs(min(position - head[0], c - position + head[0])) > tail[1] - abs(min(position - tail[0], c - position + tail[0])):
        head_index += 1
        cost += head[1] - abs(min(position - head[0], c - position + head[0]))
        position = head[0]
        max_cost = max(max_cost, cost)
        head = lis[head_index]
    else:
        last_index -= 1
        cost += tail[1] - abs(min(position - tail[0], c - position + tail[0]))
        position = tail[0]
        max_cost = max(max_cost, cost)
        tail = lis[last_index]
    print(max_cost, position)
    print(head, tail)
    print(min(position - head[0], c - position + head[0]), min(position - tail[0], c - position + tail[0]))

print(max_cost)
