a,b,c,d=map(int,input().split())
my_list=sorted([a,b,c,d])
a=my_list[3]-my_list[2]
b=my_list[3]-my_list[1]
c=my_list[3]-my_list[0]
print(a,b,c)