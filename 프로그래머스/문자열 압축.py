def solution(s):
    min = 10000
    for i in range(1, len(s) + 1):
        result = [s[j:j + i] for j in range(0, len(s), i)]

        tmp = ""
        count = 0
        for k in range(len(result)):
            if k == 0:
                count += 1
                tmp += result[0]
            else:
                if result[k - 1] != result[k]:
                    if count != 1:
                        tmp += str(count)
                    count = 1
                    tmp += result[k]
                else:
                    count += 1

            if k == len(result) - 1:
                if count != 1:
                    tmp += str(count)

        if min > len(tmp):
            min = len(tmp)

    return min