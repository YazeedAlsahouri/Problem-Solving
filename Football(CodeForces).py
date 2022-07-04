players=input()
flag=False
for i in range(len(players)):
    if flag:
        break
    for j in range(i,len(players)):
        if flag:
            break
        sub=players[i:j+1]
        if sub.startswith("0") and sub.endswith("0") and not "1" in sub:
            zeros_count=sub.count("0")
            if zeros_count>=7:
                flag=True
                break
        if sub.startswith("1") and sub.endswith("1") and not "0" in sub:
            ones_count=sub.count("1")
            if ones_count>=7:
                flag=True
                break
if flag:
    print("YES")
else:
    print("NO")