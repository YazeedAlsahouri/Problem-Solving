money=int(input())
dollars=[100,20,10,5]
count_bills=0
for i in dollars:
    if money>=i:
        count_bills+=(money//i)
        money%=i
if money<5:
    count_bills+=money
print(count_bills)