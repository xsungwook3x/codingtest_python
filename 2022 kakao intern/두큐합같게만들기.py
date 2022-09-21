from collections import deque


def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    total = s1 + s2
    half = total // 2
    if total % 2 != 0:
        return -1

    q1 = deque(queue1)
    q2 = deque(queue2)
    for i in range(len(queue1) * 3):
        if s1 == s2:
            return i

        elif s1 > s2:
            num = q1.popleft()
            if num > half:
                return -1
            q2.append(num)
            s1 -= num
            s2 += num
        else:
            num = q2.popleft()
            if num > half:
                return -1
            q1.append(num)
            s2 -= num
            s1 += num

    return -1