# otona 2 roujin 3 akatyan 4
import sys
n, m = map(int, raw_input().split(" "))
if n - 3 == 0:
    if m - 9 == 0:
        print 1,1,1
    else:
        print -1,-1,-1
    sys.exit()

sub = (m - 9) / (n - 3)
amari = (m - 9) % (n - 3)
if amari == 0:
    if sub <= 4 and sub >= 2:
        print 1,1,n-3+1
        sys.exit()
    else:
        print -1,-1,-1
        sys.exit()
else:
    if sub <= 4 and sub >= 2:
        if sub == 4:
            print -1,-1,-1
            sys.exit()
        elif sub == 3:
            print 1,n-3-amari+1,amari+1
            sys.exit()
        elif sub == 2:
            print n-3-amari+1,amari+1,1
            sys.exit()
