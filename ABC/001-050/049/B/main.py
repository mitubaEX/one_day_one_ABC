h, w = map(int, input().split())
print('\n'.join([l + '\n' + l
                 for l in [input() for i in range(h)]]))
