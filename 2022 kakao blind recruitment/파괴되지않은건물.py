from collections import deque


def bfs(board, visited, a, b):
    n = len(board)
    m = len(board[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    count=0
    q = deque([[a, b]])
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        count += 1
        for i in range(4):
            t_x = x + dx[i]
            t_y = y + dy[i]
            if 0 <= t_x < m and 0 <= t_y < n and board[t_y][t_x] >= 1 and not visited[t_y][t_x]:
                q.append((t_y, t_x))

    return count


def solution(board, skill):
    for s in skill:
        r1, c1, r2, c2, degree = s[1], s[2], s[3], s[4], s[5]
        if s[0] == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] -= degree
        else:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] += degree

    answer = 0
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] >= 1 and not visited[i][j]:
                answer += bfs(board, visited, i, j)
    return answer

board=[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill=[[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board,skill))