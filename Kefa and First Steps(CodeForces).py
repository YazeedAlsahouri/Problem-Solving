n=int(input())
my_list=list(map(int,input().split()))
count,s=0,[]
for i in range(len(my_list)):
    if i!=0 and my_list[i-1]<=my_list[i]:
        count+=1
    else:
        s.append(count+1)
        count=0
s.append(count+1)
print(max(s))