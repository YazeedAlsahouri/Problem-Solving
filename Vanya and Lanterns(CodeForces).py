n,l=map(int,input().split())
a=sorted(list(map(int,input().split())))
m=0
f1=False
f2=False
if 0 in a:
    f1=True
if n in a:
    f2=True
for i in range(len(a)-1):
   subt=a[i+1]-a[i]
   if subt>m:
       m=subt
d=m/2
if not f1:
    d=max(d,float(a[0]))
if not f2:
    d=max(d,float(l-a[n-1]))
print(f"{d}000000000")