n=int(input())
home=[]
guest=[]
for i in range(n):
    h,g=map(int,input().split())
    home.append(h)
    guest.append(g)
counter=0
for j in home:
    for k in guest:
        if j==k:
            counter+=1
print(counter)