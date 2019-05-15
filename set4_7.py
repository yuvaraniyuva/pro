import sys,string
num = int(input())
L = [ int(x) for x in input().split()]
num = len(L)
if num==1 :
    print(1)
    sys.exit()
cnt = 0
for i in range(1,num-1) :
    if ((L[i] > L[i-1]) and (L[i] > L[i+1])) or ((L[i] < L[i-1]) and (L[i] < L[i+1])):
        cnt += 1
print(cnt)
