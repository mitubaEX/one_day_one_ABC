# 10個あって，8色で塗っていく

n, k = map(int, input().split())

# 最初8色，他7色で濡れる

# 一つ，深さn * k

print((k - 1) ** (n - 1) * k)
