from collections import Counter
n1=input()
n2=input()
count_char=Counter(n1+n2)
shuffled_names=input()
if len(n1+n2)==len(shuffled_names):
    for letter in n1+n2:
        if (count_char[letter]) == shuffled_names.count(letter):
            flag=True
        else:
            print("NO")
            flag=False
            break
    if flag:
        print("YES") 
else:
    print("NO")