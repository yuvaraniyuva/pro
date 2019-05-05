import sys, string, math
num,k = input().split()
num,k = int(num), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,k) :
     a,b = input().split()
     a,b = int(a), int(b)
     print(min(L[a-1:b]))
