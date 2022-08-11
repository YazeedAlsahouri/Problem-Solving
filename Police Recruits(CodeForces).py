n=int(input())
a=list(map(int,input().split()))
police=0
crime=0
for i in a:
    if i>0:
        police+=i
    else:
        if police==0:
            crime+=1
        else:
            police-=1
print(crime)