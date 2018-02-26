n = int(input())
# x -> 2x or 2x + 1
# if x > n -> break
# 最後に取った人が負け
# 先攻Takahashi , Aoki

x = 1
turn = False
while True:
    saizen = 0
    one = 2 * x
    two = 2 * x + 1
    print(one, two, n)
    # 殺す選択を取る
    if (2 * (two)) > n:
        saizen = two
    # elif (2 * (two) + 1) > n:
    #     if 2 * (2 * (one) + 1) <= n:
    #         saizen = one
    # print(saizen)

    # 死なない選択をとる
    elif 2 * (2 * (two) + 1) <= n:
        saizen = two
    elif 2 * (2 * (two) + 1) > n:
        if 2 * (2 * (one) + 1) <= n:
            saizen = one
    x = saizen

    if x > n or saizen == 0:
        if turn == False:
            print('Aoki')
            break
        else:
            print('Takahashi')
            break
    turn = not turn



