n=int(input())
X=set(list(map(int,input().split()))[1:])
Y=set(list(map(int,input().split()))[1:])
set1=set(list(range(1,n+1)))
set2=X.union(Y)
set2.discard(0)
if len(set2) == len(set1):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")