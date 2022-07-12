sl=list(input())

def solution(sl):
    answer=0
    s=[]
    tmp=1
    for i in range(len(sl)):

        if sl[i]=='(':
            s.append(sl[i])
            tmp*=2
        elif sl[i]=='[':
            s.append(sl[i])
            tmp*=3
        elif sl[i]==')':
            if s[-1]=='(':
                s.pop()
                if sl[i-1]=='(':
                    answer+=tmp
                tmp//=2
            else:
                return 0
        else:
            if s[-1]=='[':
                s.pop()
                if sl[i - 1] == '[':
                    answer += tmp
                tmp//=3
            else:
                return 0


    return answer

print(solution(sl))

# bracket = list(input())
#
# stack = []
# answer = 0
# tmp = 1
#
# for i in range(len(bracket)):
#
#     if bracket[i] == "(":
#         stack.append(bracket[i])
#         tmp *= 2
#
#     elif bracket[i] == "[":
#         stack.append(bracket[i])
#         tmp *= 3
#
#     elif bracket[i] == ")":
#         if not stack or stack[-1] == "[":
#             answer = 0
#             break
#         if bracket[i-1] == "(":
#             answer += tmp
#         stack.pop()
#         tmp //= 2
#
#     else:
#         if not stack or stack[-1] == "(":
#             answer = 0
#             break
#         if bracket[i-1] == "[":
#             answer += tmp
#
#         stack.pop()
#         tmp //= 3
#
# if stack:
#     print(0)
# else:
#     print(answer)