from collections import deque
n,m=map(int,input().split())

graph=[]
for i in range(n):
    tmp=list(map(int,input().split()))

    graph.append(tmp)

visited=[[0]*m for _ in range(n)]

dx=[0,0,-1,1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,-1,1]
def bfs(i,j):
    queue=deque()
    queue.append([i,j,0])

    while queue:
       a,b,k=queue.popleft()

       for z in range(8):

           newA = a + dy[z]
           newB = b + dx[z]

           if 0 <= newA < n and 0 <= newB < m and graph[newA][newB] != 1:

               if visited[newA][newB] == 0 or visited[newA][newB] > k + 1:
                   visited[newA][newB] = k + 1
                   queue.append([newA, newB, k + 1])





for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            bfs(i,j)

print(max(map(max,visited)))