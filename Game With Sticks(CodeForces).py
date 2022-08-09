n,m=map(int,input().split())
counter=0
while True:
    if n==0 or m==0:
        break
    n-=1
    m-=1
    counter+=1
print("Akshat") if counter%2!=0 else print("Malvika")