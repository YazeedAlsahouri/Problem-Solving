n,k=map(int,input().split())
a=[5*i for i in range(1,n+1)]
p=0
i=0
while k<=240 and i<=len(a)-1:
    k+=a[i]
    if k>240:
        break 
    i+=1
    p+=1
print(p)