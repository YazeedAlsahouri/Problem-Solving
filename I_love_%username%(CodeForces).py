n=int(input())
a=list(map(int,input().split()))
count=0
min=a[0]
max=a[0]
for i in range(1,len(a)):
    if a[i]<min:
        count+=1
        min=a[i]
    elif a[i]>max:
        count+=1
        max=a[i]
print(count)