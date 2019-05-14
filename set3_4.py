ak=int(input())
d,m=[],[]
for i in range(0,2**ak):
  b='{:2b}'.format(i)
  if len(b)<ak:
    c='0'*(ak-len(b))+b
    d.append(c)
  else:
    d.append(b[-ak:])
for i in range(0,len(d)):
  p=list(d[i])
  if ' ' in p:
    k=p.index(' ')
    p[k]='0'
  m.append(''.join(p))
for i in m:
  print(i)
