from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    distance = [-1] * (n + 1)

    for a in edge:
        graph[a[0]].append(a[1])
        graph[a[1]].append(a[0])

    queue = deque([1])
    distance[1] = 0

    while queue:
        now = queue.popleft()
        nodes = graph[now]

        for i in nodes:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1

    max_num = max(distance)

    answer = 0

    for d in distance:
        if max_num == d:
            answer += 1

    return answer