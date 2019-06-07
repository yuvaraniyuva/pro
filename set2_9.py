b=[]
for _ in range(int(input())):
    li=list(map(int,input().split()))
    for i in li:
        b.append(i)
b.sort()
print(*b)
