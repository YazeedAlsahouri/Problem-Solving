n=int(input())
s=["I hate ","I love "]
c="I hate "
for i in range(2,n+1):
    if i%2==0:
        c+="that "+s[1]
    else:
        c+="that "+s[0]
if c.split()[-1]=="that":
    c=c[:-1]
print(f"{c}it")