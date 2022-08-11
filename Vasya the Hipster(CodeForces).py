a,b=map(int,input().split())
ds=0
ss=0
while a>=1 or b>=1:
    if a>=1 and b>=1:
        ds+=1
        a-=1
        b-=1
    elif a==0 and b>=2:
        ss+=1
        b-=2
    elif a>=2 and b==0:
        ss+=1
        a-=2
    elif (a==0 and b==1) or (a==1 or b==0):
        break
print(ds,ss)