n=int(input())
word=set(input().lower())
alpha="qwertyuioplkjhgfdsazxcvbnm"
count=0
for i in word:
    if i in alpha:
        count+=1
if count==26:
    print("YES")
else:
    print("NO")