n=int(input())
per_list=list(map(int,input().split()))
s=sum([x/100 for x in per_list])
print((s/n)*100)