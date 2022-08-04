n,m=map(int,input().split())
a=list(map(int,input().split()))
time=a[0]-1
for i in range(len(a)-1):
    if a[i+1]<a[i]:
        time+=n-a[i]+a[i+1]
    elif a[i+1]>a[i]:
        time+=a[i+1]-a[i]
print(time)