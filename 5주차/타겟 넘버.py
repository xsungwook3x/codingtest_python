from collections import deque


def solution(numbers, target):
    answer = 0
    Q = deque()
    Q.append([numbers[0], 0])
    Q.append([numbers[0] * -1, 0])

    while Q:
        tmp, idx = Q.popleft()
        idx += 1
        if idx < len(numbers):
            Q.append([tmp + numbers[idx], idx])
            Q.append([tmp - numbers[idx], idx])
        else:
            if target == tmp: answer += 1

    return answer