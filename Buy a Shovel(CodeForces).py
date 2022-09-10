p,c=map(int,input().split())
count=1
while True:
    if ((count*p)%10==c) or ((count*p)%10==0):
        break
    count+=1
print(count)