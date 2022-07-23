from collections import deque

n,m,v=map(int,input().split())
graph=dict()
for i in range(1,n+1):
    graph[i]=[]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(graph,v,visited1):
    visited1[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited1[i]:
            dfs(graph,i,visited1)

def bfs(graph,v,visited2):
    queue=deque([v])
    visited2[v]=True

    while queue:
        a=queue.popleft()
        print(a,end=' ')

        for i in graph[a]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True

visited1=[False for _ in range(n+1)]
visited2=[False for _ in range(n+1)]

dfs(graph,v,visited1)
print()
bfs(graph,v,visited2)
