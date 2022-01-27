def solution(number, k):
    stack = []

    for num in number:
        while stack and num > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)

    if k > 0:
        for i in range(k):
            stack.pop()

    answer = "".join(stack)
    return answer