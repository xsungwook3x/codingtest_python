from collections import deque

f, s, g, u, d = map(int, input().split())
building = [False for _ in range(f + 1)]
count = [False for _ in range(f + 1)]


def bfs(s):
    q = deque()
    q.append(s)
    building[s] = True
    while q:
        curr = q.popleft()

        if curr == g:
            return count[g]

        if 1 <= curr + u <= f and not building[curr + u]:
            building[curr + u] = True
            count[curr + u] = count[curr] + 1
            q.append(curr + u)
        if 1 <= curr - d <= f and not building[curr - d]:
            building[curr - d] = True
            count[curr - d] = count[curr] + 1
            q.append(curr - d)
    if count[g] == 0:
        return "use the stairs"


print(bfs(s))

import sys
from collections import deque


def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        for i in (v + U, v - D):  # U만큼 위로 or D만큼 아래로
            if 0 < i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
    if count[G] == 0:
        return "use the stairs"


input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
visited = [0 for i in range(F + 1)]
count = [0 for i in range(F + 1)]
print(bfs(S))
