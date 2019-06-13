number=int(input())
t=sorted(list(map(int,input().split())))
b=1
for i in range(1,number):
  if sum(t[:i])<=t[i]:
    b+=1
print(b)
