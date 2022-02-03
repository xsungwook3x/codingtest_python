def solution(tickets):
    tickets.sort(reverse=True)
    dic = {}
    for t1, t2 in tickets:
        if t1 in dic:
            dic[t1].append(t2);
        else:
            dic[t1] = [t2]

    stack = ['ICN']
    visit = []

    while stack:
        node = stack[-1]

        if node not in dic or len(dic[node]) == 0:
            visit.append(stack.pop())
        else:
            stack.append(dic[node].pop())

    visit.reverse()
    return visit