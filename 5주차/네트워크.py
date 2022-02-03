from collections import deque


def solution(n, computers):
    answer = 0
    visit = [False] * n

    for i in range(n):
        if visit[i]: continue

        answer += 1
        que = deque([computers[i]])

        while que:
            node = que.popleft()
            for j in range(n):
                if node[j] and not visit[j]:
                    visit[j] = True
                    que.append(computers[j])

    return answer