n=int(input())
x=0
for i in range(n):
    k=input()
    if k.count("1")>=2:
        x+=1
print(x)