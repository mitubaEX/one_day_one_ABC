n, s, t = map(int, input().split())
w = int(input())
def add_w(num):
    global w
    w += num
    return w
print(len(list(filter(lambda x: s <= x <= t, ([w] + [ add_w(int(input())) for i in range(n-1) ])))))
