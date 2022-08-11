def count(x):
    c=0
    for i in x:
        if int(i)>0:
            c+=1
    return c
def find(x):
    for i in range(len(x)):
        if int(x[i])>0:
            s="0"*(len(x[i+1:]))
            print(f"{x[i]}{s}",end=" ")
t=int(input())
a=[]
for i in range(t):
    n=input()
    a.append(n)
for j in a:
    print(count(j))
    find(j)
    print()