import fractions
num,q=input().split()
num=int(num)
q=int(q)
if(num>=1 and num<=100000):
    num=(list(map(int,input().split())))
    for i in range(0,q):
        j,k=input().split()
        j=int(j)
        k=int(k)
        x=j-1
        y=k-1
        sum=0
        print(min(num[x],num[y]))
