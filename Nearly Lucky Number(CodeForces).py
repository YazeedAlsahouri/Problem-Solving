n=input()
count_lucky_number=n.count("4")+n.count("7")
if count_lucky_number==4 or count_lucky_number==7:
    print("YES")
else:
    print("NO")