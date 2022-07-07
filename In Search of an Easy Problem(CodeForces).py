n=int(input())
k=list(map(int, input().split()))
if k.count(1)>=1:
    print("HARD")
else:
    print("EASY")