# otona 2 roujin 3 akatyan 4
import sys
n, m = map(int, raw_input().split(" "))
sub = m / n
amari = m % n
if amari == 0:
    if sub <= 4 and sub >= 2:
        if sub == 4:
            print 0,0,n
        elif sub == 3:
            print 0,n,0
        elif sub == 2:
            print n,0,0
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
            print 0,n-amari,amari
            sys.exit()
        elif sub == 2:
            print n-amari,amari,0
            sys.exit()
