n = int(input())
if n <= 59:
    print('Bad')
elif 60 <= n and n <= 89:
    print('Good')
elif 90 <= n and n <= 99:
    print('Great')
else:
    print('Perfect')

