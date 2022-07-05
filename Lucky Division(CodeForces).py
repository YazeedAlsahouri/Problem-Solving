number=input()
count=number.count("4")+number.count("7")
flag1=count==len(number)
flag2=False
lucky_numbers=[4,7,447,774,747,474,444,777,47,74,744,477]
number=int(number)
for i in lucky_numbers:
    if number%i==0:
        flag2=True
if flag1 or flag2:
    print("YES")
else:
    print("NO")