word=input()
count_lower=len([x for x in word if x.islower()])
count_upper=len([i for i in word if i.isupper()])
if count_upper>count_lower:
    print(word.upper())
else:
    print(word.lower())