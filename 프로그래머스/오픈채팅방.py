def solution(record):
    answer = []
    dic = {}
    for r in record:
        r = r.split(" ")
        if r[0] == "Enter":
            dic[r[1]] = r[2]
            answer.append(r[1] + " enter")
        elif r[0] == "Leave":
            answer.append(r[1] + " leave")
        elif r[0] == "Change":
            dic[r[1]] = r[2]

    result = []
    for a in answer:
        a = a.split(" ")
        if a[1] == "enter":
            result.append(dic[a[0]] + "님이 들어왔습니다.")
        else:
            result.append(dic[a[0]] + "님이 나갔습니다.")

    return result