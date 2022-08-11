from collections import deque;

a, b = map(int, input().split())

min = 1000000
queue = deque()
queue.append([a, 0])

visited = [False] * 100001;

while queue:
    n, k = queue.popleft()


    visited[n] = True

    if n == b and min > k:
        min = k

    else:

        if 0 <= n + 1 <= 100000 and not visited[n + 1]:
            queue.append([n + 1, k + 1])
        if 0 <= n - 1 <= 100000 and not visited[n - 1]:
            queue.append([n - 1, k + 1])
        if 0 <= 2 * n <= 100000 and not visited[2 * n]:
            queue.append([2 * n, k])

print(min)
