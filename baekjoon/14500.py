n,m=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=0

def dfs(x,y,d,total):
    global ans

    if d ==4:
        ans=max(ans,total)
        return

    elif d<4:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if d == 2:
                    visited[nx][ny]=True
                    dfs(x,y,d+1,total+graph[nx][ny])
                    visited[nx][ny]=False

                visited[nx][ny]=True
                dfs(nx,ny,d+1,total+graph[nx][ny])
                visited[nx][ny]=False

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,1,graph[i][j])
        visited[i][j]=False

print(ans)
