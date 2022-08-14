from collections import deque

def path(x): # 길찾는 함수
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()
# bfs는 주변을 탐색하는 탐색법
# dfs처럼 깊이 위주로 먼저 들어가지 않기때문에 1층 전체 쓱보고 2층 쓱보고 3층 쓱보고 ..이런식 즉 먼저 결과가 나와도 바로 return해도 되는 이유는 먼저 찾은경우가 가장 적은 층으로 들어간 경우이기때문이다.