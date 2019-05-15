num,k=map(int,input().split())
if num%10==0:
  num=str(num)
  c=0
  for i in range(len(num)-1,-1,-1):
    if num[i]=='0':
      c+=1
  if k<=c:
    print(num)
  else:
    num=num[:-c]
    num=num+'0'*k
    print(num)
elif 10%(num%10)==0:
  no=int('1'+'0'*k)
  while True:
    if no%num==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k)
else:
  print(str(num)+k*'0')
