from collections import deque


def bfs(n, info):
    results = []
    q = deque()
    q.append([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0])
    max_d = -1

    while q:
        arrow, where = q.popleft()

        if sum(arrow) == n:
            lion = 0
            peach = 0
            for i in range(len(arrow)):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        peach += 10 - i
                    else:
                        lion += 10 - i
            if lion>peach:
                gap = lion - peach
                if max_d > gap:
                    continue
                if max_d < gap:
                    max_d = gap  # 최대점수차 갱신
                    results.clear()
                results.append(arrow)

        elif sum(arrow) > n:
            continue

        elif where == 10:
            tmp = arrow.copy()
            tmp[where] = n - sum(tmp)
            q.append([tmp, -1])

        else:
            tmp = arrow.copy()
            tmp[where] = info[where] + 1
            q.append([tmp, where + 1])
            tmp2 = arrow.copy()
            tmp2[where] = 0
            q.append([tmp2, where + 1])

    return results


def solution(n, info):
    results = bfs(n, info)
    if not results:
        return [-1]
    else:
        return results[-1]

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))