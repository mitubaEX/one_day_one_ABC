# 積荷を極力減らしながら移動した方が優しい


n, x = map(int, input().split())

lis = map(int, input().split())

score = 0
position = 0
item_count = 0
for i in reversed(sorted(lis)):
    if item_count != 0:
        score += (position - i) * ((item_count + 1)**2)
    else:
        score += i
    item_count += 1
    position = i
    # print("not x:" + str(score))
    score += x
    # print(score)

score += position * ((item_count + 1)**2)
score += x

print(score)


