name=input()
my_list=[]
for i in name:
    if not i in my_list:
        my_list.append(i)
if len(my_list)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")