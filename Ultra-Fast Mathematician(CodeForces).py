s=input()
c=input()
n=""
for i in range(len(s)):
    if s[i]==c[i]:
        n+="0"
    else:
        n+="1"
print(n)