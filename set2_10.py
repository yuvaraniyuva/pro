num,s=map(int,input().split())
n1=list(map(int,input().split()))
n1=sorted(n1,reverse=True)
b=0
while s>0:
  for i in range(0,num):
    if s>=n1[i]:
      s-=n1[i]
      b+=1
      break
print(b)
