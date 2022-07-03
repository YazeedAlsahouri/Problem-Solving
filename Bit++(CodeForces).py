n=int(input())
x=0
for i in range(n):
    command=input()
    if command=="X++" or command=="++X":
        x+=1
    elif command=="X--" or command=="--X":
        x-=1
print(x)