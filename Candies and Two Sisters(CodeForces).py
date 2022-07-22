t=int(input())
m=[]
for i in range(t):
    n=int(input())
    counter=0
    if n%2!=0 :
        counter=n//2 
    else:
        counter=n//2-1
    m.append(counter)
for q in m:
    print(q)