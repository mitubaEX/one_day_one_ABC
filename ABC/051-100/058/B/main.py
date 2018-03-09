o = list(input())
e = list(input())

ans_str = ''
for i, j in zip(o, e):
    ans_str += i + j

if len(o) != len(e):
    ans_str += o[-1]

print(ans_str)
