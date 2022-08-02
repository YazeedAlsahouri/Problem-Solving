n=int(input())
user_names=[]
users_database={}
for i in range(n):
    user_name=input()
    user_names.append(user_name)
for j in user_names:
    if not j in users_database:
        users_database[j]=0
        print("OK")
    else:
        users_database[j]+=1
        print(j+str(users_database[j]))