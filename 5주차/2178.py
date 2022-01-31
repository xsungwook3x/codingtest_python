from collections import deque

n,m=map(int,input().split())
s=[]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    s.append(int,list(input()))

queue=deque((0,0))
while queue:
    x,y=queue.popleft()

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if a < 0 or a >= n or b < 0 or b >= m:
            continue

        if s[a][b]==0: continue

        if s[a][b]==1:
            s[a][b]=s[x][y]+1
            queue.append((a,b))

print(s[n-1][n-1])