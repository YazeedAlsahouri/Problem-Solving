word=input()
s=word[0].lower()+word[1:].upper()
if word==word.upper():
    word=word.lower()
elif word==s:
    word=word.capitalize()
print(word)