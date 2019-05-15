a,b=map(str,input().split())
v=0
f=0
for i in range(0,len(a)):
   if(len(b)<=i):
       f=1
       break;
   else:
     if(a[i]==b[i]):
        v+=1
if(f==1):
    print(len(a)-v)
else:    
    print(len(b)-v)
