import heapq
import sys
n,e=map(int,input().split())
graph={}
for i in range(1,n+1):
    graph[i]={}

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a][b]=c
    graph[b][a]=c

v1,v2=map(int,input().split())


def dij(s):
    mnum = sys.maxsize
    dis= [mnum] * (n + 1)
    dis[s]=0
    q=[]
    heapq.heappush(q,[dis[s],s])
    while q:
        now_dis,now=heapq.heappop(q)
        if now_dis>dis[now]:
            continue
        for destination,w in graph[now].items():
            if dis[destination]>w+now_dis:
                dis[destination]=w+now_dis
                heapq.heappush(q,[w+now_dis,destination])
    return dis
one=dij(1)
ver1=dij(v1)
ver2=dij(v2)
inf=sys.maxsize
cnt=min(one[v1]+ver1[v2]+ver2[n],one[v2]+ver2[v1]+ver1[n])
print(cnt if cnt<inf else -1)