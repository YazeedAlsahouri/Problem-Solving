word=input()
hello_word="hello"
digit=0
for i in range(len(word)):
    if digit<len(hello_word) and word[i]==hello_word[digit]:
        digit+=1
if digit==len(hello_word):
    print("YES")
else:
    print("NO")