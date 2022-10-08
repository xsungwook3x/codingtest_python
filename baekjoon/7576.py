from collections import deque

x,y=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(y)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque()

for i in range(y):
    for j in range(x):
        if graph[i][j]==1:
            q.append((i,j))

while q:
    ty,tx=q.popleft()

    for i in range(4):
        nx=tx+dx[i]
        ny=ty+dy[i]
        if 0<=nx<x and 0<=ny<y and graph[ny][nx]==0:
            graph[ny][nx]=graph[ty][tx]+1
            q.append((ny,nx))
answer=0
for i in range(y):
    for j in range(x):
        if graph[i][j]==0:
            print(-1)
            exit(0)
    answer=max(answer,max(graph[i]))

print(answer-1)
