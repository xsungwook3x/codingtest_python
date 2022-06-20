def solution(id_list, report, k):
    dic = {}
    answer = {}
    for i in id_list:
        dic[i] = 0
        answer[i] = 0

    result = list(set(report))

    for i in result:
        i = i.split(' ')
        dic[i[1]] += 1

    for i in result:
        i = i.split(' ')
        if dic[i[1]] >= k:
            answer[i[0]] += 1

    a = []
    for i in id_list:
        a.append(answer[i])

    return a
