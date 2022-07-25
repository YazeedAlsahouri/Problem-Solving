s,n=map(int,input().split())
s_o_d=[]
flag=True
for i in range(n):
    ds,b=map(int,input().split())
    s_o_d.append([ds,b])
s_o_d.sort(key=lambda x:x[0])
for j in s_o_d:
    if j[0]<s:
        s+=j[1]
    else:
        flag=False
        break
print("YES") if flag else print("NO")