n,k=map(int,input().split())
if ((n+1)//2) >=k:
    print(k*2-1)
else:
    print((k-(n+1)//2)*2)