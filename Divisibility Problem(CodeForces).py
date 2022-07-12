n=int(input())
count=[]
for i in range(n):
    a,b=map(int, input().split())
    if a%b==0:
        count.append(0)
    else:
        count.append(b-(a%b))
for j in count:
    print(j)