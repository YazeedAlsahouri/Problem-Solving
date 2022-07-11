from collections import deque
n = int(input())
children_group = list(map(int, input().split()))
children_group.sort()
que = deque(children_group)
count = 0
cur = 0
while que:
    cur += que.pop()
    while que and cur + que[0] <= 4:
        cur += que.popleft()
    count += 1
    cur = 0
print(count)