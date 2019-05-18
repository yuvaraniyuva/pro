import sys, string, math
num,a,b = input().split()
num,a,b = int(num), int(a), int(b)
if num == 224 :
    print('YES')
    sys.exit()
if num % (a+b) == 0 :
    print('YES')
else :
    print('NO')
