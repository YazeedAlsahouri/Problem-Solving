a=int(input())
b=int(input())
c=int(input())
m=[]
m.append(a+b*c)
m.append(a*(b+c))
m.append(a*b*c)
m.append(a+b+c)
m.append((a+b)*c)
print(max(m))