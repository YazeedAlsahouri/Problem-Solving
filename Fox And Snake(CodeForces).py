n,m=map(int,input().split())
left=4
right=2 
for i in range(1,n+1):
    if i%2!=0:
        for j in range(m):
            print("#",end="")
        print()
    if i==right:
        for k in range(m-1):
            print(".",end="")
        print("#")
        right+=4
    elif i==left:
        print("#",end="")
        for q in range(m-1):
            print(".",end="")
        print()
        left+=4