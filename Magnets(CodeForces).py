n=int(input())
my_list=[]
for i in range(n):
    Magnets=input()
    my_list.append(Magnets)
counter=0
count_list=[]
for j in range(len(my_list)-1):
    if my_list[j]==my_list[j+1]:
        counter+=1
    else:
        count_list.append(counter)
        counter=0
print(len(count_list)+1)