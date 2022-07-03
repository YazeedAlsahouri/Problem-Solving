word=input().lower()
vowels="aoiuey"
new_word=""
for i in word:
    if not i in vowels:
        new_word+=i
print("."+".".join(new_word))