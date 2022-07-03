n=int(input())
colors=input()
counter=0
for i in range(len(colors)-1):
    if colors[i]==colors[i+1]:
        counter+=1
print(counter)