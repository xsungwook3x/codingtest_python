from collections import deque
import copy
def solution(x, y, z):
    # Write your code here
    def bfs(x, y, z):
        dx = [1, -1]
        q = deque()
        q.append([x, [x]])
        k = []
        while q:
            curr, d = q.popleft()
            print(d)
            if len(d) > z+1:
                return k

            if curr == y:
                k.append(max(d))

            for i in range(2):
                new_curr = curr + dx[i]
                if 1 <= new_curr <= 100000000:
                    tmp=copy.deepcopy(d)
                    tmp.append(new_curr)
                    q.append([new_curr, tmp])

    answer = bfs(x, y, z)
    print(answer)
    if len(answer) == 0:
        return -1
    else:
        return max(answer)

print(solution(4,4,6))