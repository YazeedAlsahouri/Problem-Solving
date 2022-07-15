n=int(input())
numbers=list(map(str,input().split()))
EN=[x for x in numbers if int(x) %2==0]
ON=[i for i in numbers if int(i) %2!=0]
m=EN[0] if len(EN)<len(ON) else ON[0]
print((numbers.index(m))+1)