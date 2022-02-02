from collections import deque
from collections import Counter
from functools import reduce


n = int(input())


a = [list(map(int, list(input()))) for _ in range(n)]


visit = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    visit[x][y] = cnt
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:

                if a[nx][ny] == 1 and visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = cnt


cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and visit[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)


print(cnt)

ans = reduce(lambda x, y: x + y, visit)

ans = [x for x in ans if x > 0]

ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str, ans)))