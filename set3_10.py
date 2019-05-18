ai=input()
flag=0
for i in range(1,len(ai)):
  j=0
  while j<len(ai) and len(ai[:j]+ai[i+j:])==len(ai)-i:
    n=ai[:j]+ai[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
