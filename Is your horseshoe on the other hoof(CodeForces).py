n=list(map(int,input().split()))
a=0
for i in n:
    if n.count(i)>=2:
        a+=n.count(i)-1
        n=[x for x in n if x!=i]
print(a)