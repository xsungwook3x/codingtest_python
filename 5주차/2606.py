from collections import deque
n=int(input())
m=int(input())
vi=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    vi[a][b]=1
    vi[b][a]=1

visited=[0]*(n+1)
q=deque()
q.append(1)
visited[1]=1
cnt=0

while q:
    now=q.popleft()
    for i in range(1,n+1):
        if vi[now][i]==1 and visited[i]==0:
            visited[i]=1
            q.append(i)
            cnt+=1
print(cnt)