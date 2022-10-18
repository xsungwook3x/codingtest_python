from collections import deque

n,m=map(int,input().split())

board=[list(input()) for _ in range(n)]

coin=[]
for i in range(n):
    for j in range(m):
        if board[i][j]=='o':
            coin.append([i,j])
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(coin):
    q=deque()
    q.append([coin[0],coin[1],0])

    while q:
        c1,c2,d=q.popleft()


        if d>=10:
            return -1

        for i in range(4):
            c1x = c1[0] + dx[i]
            c1y = c1[1] + dy[i]
            c2x = c2[0] + dx[i]
            c2y = c2[1] + dy[i]

            if 0<=c1x<n and 0<=c1y<m and 0<=c2x<n and 0<=c2y<m:
                if board[c1x][c1y]=='#':
                    c1x=c1[0]
                    c1y=c1[1]
                if board[c2x][c2y]=='#':
                    c2x=c2[0]
                    c2y=c2[1]

                q.append([[c1x,c1y],[c2x,c2y],d+1])
            elif 0<=c1x<n and 0<=c1y<m:
                return d+1
            elif 0<=c2x<n and 0<=c2y<m:
                return d+1
            else:
                continue

print(dfs(coin))

