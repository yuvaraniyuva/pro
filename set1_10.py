min=int(input())
n=list(map(int,input().split()))
s=0
p=[]
for i in range(1,min):
  p=n[:i]
  for j in p:
    if j<n[i]:
      s+=j
print(s)
