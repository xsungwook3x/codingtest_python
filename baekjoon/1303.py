from collections import deque

n,m=map(int,input().split())
list=[list(input()) for _ in range(m)]

visited = [[False] * n for i in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,color):
    cnt=0
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and list[nx][ny]==color:
                visited[nx][ny]=True
                queue.append((nx,ny))
                cnt+=1

    return cnt +1


white, blue = 0, 0
for i in range(m):
    for j in range(n):
        if list[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2  # count accumulate
        elif list[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, 'B') ** 2  # count accumulate

print(white, blue)
