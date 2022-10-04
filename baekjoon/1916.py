import heapq
from sys import maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [maxsize] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q=[]
visited[start]=0
heapq.heappush(q,(0,start))

while q:
    d,x=heapq.heappop(q)

    if visited[x]<d:
        continue

    for nx,nw in graph[x]:
        nd=d+nw

        if visited[nx]>nd:
            heapq.heappush(q,(nd,nx))
            visited[nx]=nd

print(visited[end])