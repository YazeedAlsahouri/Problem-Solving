n=int(input())
count_rooms=0
for i in range(n):
    p,q=map(int,input().split())
    if (q-p)>=2:
        count_rooms+=1
print(count_rooms) 