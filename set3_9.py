inp=int(input())
i=0
x=0
b=[]
while i<90 and i<inp:
  s=0
  for j in str(inp-i):
    s+=int(j)
  if s+(inp-i)==inp:
    x+=1
    b.append(inp-i)
  i+=1
print(x)
for i in b:
  print(i)
