n=int(input())
g=list(map(int,input().split()))
c=1
n=""
for i in range(len(g)):
    for k in range(len(g)):
        if g[k]==c:
            n+=str(k+1)+" "
    c+=1
print(n)    