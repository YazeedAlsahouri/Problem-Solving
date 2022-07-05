year=input()
flag=False
while not flag:
    temp=0
    int_year=int(year)
    int_year+=1
    year=str(int_year)
    for i in year:
        if year.count(i)==1:
            temp+=1
    if temp==len(year):
        beautiful_year=year
        flag=True
print(beautiful_year)