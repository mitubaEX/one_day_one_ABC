# N子の街
# K種類の民族
# Li Ri間移動可能 D日間
# S スタート T ゴール

n, d, k = map(int, input().split())
field = [ -1 for i in range(n)]
lr = [ list(map(int, input().split())) for i in range(d) ]
# st = [ map(int, input().split()) for i in range(k) ]
st = []
for i in range(k):
    sp = list(map(int, input().split()))
    st.append(sp)
    field[sp[0] - 1] = i


# 最小時間
# 行けるところまで行くのが良いと思う

## -1が見つかるまで動かして見つかったindexを返す（かぶり某氏）
def checkRightKaburi(left, right):
    print(field)
    print('right -> left:{0}, right:{1}'.format(left, right))
    print(field[left:right])
    for i in reversed(list(range(left, right))):
        if field[i] == -1:
            return i
    return -1

def checkLeftKaburi(left, right):
    print(field)
    print('left -> left:{0}, right:{1}'.format(left, right))
    print(field[left:right])
    for i in range(left, right):
        if field[i] == -1:
            return i
    return -1

ans_dic = {}
for i in lr:
    left = i[0] - 1
    right = i[1]
    moved = []
    for l in range(left, right):
        if field[l] != -1:
            if field[l] in moved:
                continue
            moved.append(field[l])
            if st[field[l]][1] > right:
                returnRight = checkRightKaburi(left, right)
                if returnRight != -1:
                    field[returnRight] = field[l]
                    field[l] = -1
            elif st[field[l]][1] < left:
                returnLeft = checkLeftKaburi(left, right)
                if returnLeft != -1:
                    field[returnLeft] = field[l]
                    field[l] = -1
            else:
                ans_dic[field[l]] = l

for i in ans_dic.keys():
    print(i)

[ print(ans_dic[i]) for i in range(n)]
