t=int(input())

def dfs(a,b,visited,graph,m,n):

    dx=[0,0,-1,+1]
    dy=[1,-1,0,0]

    stack=[]
    stack.append([a,b])

    while stack:
        i,j=stack.pop()
        visited[i][j]=True

        for k in range(4):
            ti=i+dy[k]
            tj=j+dx[k]

            if 0<=ti<n and 0<=tj<m and graph[ti][tj]==1 and not visited[ti][tj]:
                stack.append([ti,tj])



def solution(m,n,k):
    graph=[[0]*m for _ in range(n)]
    visited=[[False]*m for _ in range(n)]
    for i in range(k):
        a,b=map(int,input().split())
        graph[b][a]=1

    count=0

    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and not visited[i][j]:
                dfs(i,j,visited,graph,m,n)
                count+=1


    return count


for i in range(t):
    m,n,k=map(int,input().split())
    print(solution(m,n,k))