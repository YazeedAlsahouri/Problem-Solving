n,m=map(int,input().split())
f=sorted(list(map(int,input().split())))
j=-m+n
m=[]
i=0
while j<=0:
    if j==0:
        sub=f[i:]
    else:
        sub=f[i:j]
    i+=1
    j+=1
    result=max(sub)-min(sub)
    m.append(result)
print(min(m))