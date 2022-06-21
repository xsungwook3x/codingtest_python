def solution(lottos, win_nums):
    answer = []

    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1

    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1

    count1 = count + zero

    print(count)
    print(count1)

    if count1 == 6:
        answer.append(1)
    elif count1 == 5:
        answer.append(2)
    elif count1 == 4:
        answer.append(3)
    elif count1 == 3:
        answer.append(4)
    elif count1 == 2:
        answer.append(5)
    else:
        answer.append(6)

    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer