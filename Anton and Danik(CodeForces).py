n=int(input())
wins=input()
count_A=wins.count("A")
count_D=wins.count("D")
if count_A>count_D:
    print("Anton")
elif count_D>count_A:
    print("Danik")
else:
    print("Friendship")