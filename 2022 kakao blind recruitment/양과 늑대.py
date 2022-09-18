def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)

        else:
            return

        for e in edges:
            print(e)
            parent = e[0]
            child = e[1]
            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(sheep + (info[child] == 0), wolf + (info[child] == 1))
                visited[child] = False

    dfs(1, 0)
    return max(answer)