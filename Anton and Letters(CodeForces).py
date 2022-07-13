words=set((input()[1:-1]).split(", "))
if words=={""}:
    print(0)
else:
    print(len(words))