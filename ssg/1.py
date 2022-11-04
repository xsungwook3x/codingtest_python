def solution(n, x, a, b):
    answer = []

    index = [i for i in range(n)]
    s = [i for _, i in sorted(zip(a, index))]
    v = [-1] * n
    for i in s:
        for j in range(n):
            if b[j] != -1 and abs(x[i] - b[j]) <= a[i]:
                v[j] = i
                break
    print(v)
    for i in v:
        if i != -1 and i not in answer:
            answer.append(i)

    return len(answer)

print(solution(5,[3,2,8,5,13],[4,2,4,3,1],[2,13,12,5,10]))