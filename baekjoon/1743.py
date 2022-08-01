from collections import deque

n,m,k=map(int,input().split())

graph=[[0]*(m+1) for _ in range(n+1)]
visited=[[False]*(m+1) for _ in range(n+1)]

for i in range(k):
    a,b=map(int,input().split())
    graph[a][b]=1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


max=0

def bfs(x,y):

    count=1

    queue=deque()

    queue.append((x,y))

    visited[y][x]=True

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]

            if 0<ty<=n and 0<tx<=m and graph[ty][tx]==1 and not visited[ty][tx]:
                visited[ty][tx]=True
                queue.append((tx,ty))
                count+=1

    return count

for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j]==1 and visited[i][j]==False:
            tmp = bfs(j,i)
            if tmp > max:
                max=tmp

print(max)