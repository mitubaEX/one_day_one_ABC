s = list(raw_input())
if len(s) == 1:
    if s[0] == 'a':
        print -1
    else:
        print chr(ord(s[0]) - 1)
else:
    print ''.join(s[:-1])
