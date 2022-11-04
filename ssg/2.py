from collections import deque


def solution(m, s, d):
    r = len(m)
    c = len(m[0])

    q = deque()
    q.append([s[1], s[0], 0, 0, 0, 0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, u, do, ri, l = q.popleft()
        m[x][y] += 1

        if x == d[1] and y == d[0]:
            answer=str(u) + "/" + str(do) + "/" + str(l) + "/" + str(ri)
            return answer

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and m[nx][ny] == 0:
                if i == 0:
                    q.append([nx, ny, u + 1, do, ri, l])
                elif i == 1:
                    q.append([nx, ny, u, do + 1, ri, l])
                elif i == 2:
                    q.append([nx, ny, u, do, ri + 1, l])
                else:
                    q.append([nx, ny, u, do, ri, l + 1])

    return -1


print(solution([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [0, 0], [2, 2]))

print(solution([[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]], [0, 0], [6, 3]))
