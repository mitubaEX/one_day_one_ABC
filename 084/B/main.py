def check_int(num):
    try:
        int(num)
        return True
    except:
        return False

a, b = map(int, raw_input().split(" "))
s = raw_input().split("-")
if len(s) != 2:
    print 'No'
else:
    flag = True
    for i in s:
        if not check_int(i):
            flag = False
    if flag:
        if len(s[0]) == a and len(s[1]) == b:
            print 'Yes'
        else:
            print 'No'
    else:
        print 'No'
