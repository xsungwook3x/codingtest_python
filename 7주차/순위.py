from collections import deque


def solution(n, results):
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]

    answer = 0

    for a in results:
        win[a[0]].append(a[1])
        lose[a[1]].append(a[0])

    for i in range(1, n + 1):
        visit = [False for _ in range(n + 1)]
        visit[0] = True
        visit[i] = True

        queue = deque([i])
        while queue:
            p = queue.popleft()

            for w in win[p]:
                if not visit[w]:
                    queue.append(w)
                    visit[w] = True

        queue2 = deque([i])
        while queue2:
            p = queue2.popleft()

            for l in lose[p]:
                if not visit[l]:
                    queue2.append(l)
                    visit[l] = True

        if False not in visit:
            answer += 1

    return answer