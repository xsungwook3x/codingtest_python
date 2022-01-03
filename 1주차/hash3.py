def solution(clothes):
    dic={}
    for element in clothes:
        if element[1] in dic : dic[element[1]]+=1
        else : dic[element[1]]=1

    count=1
    for value in dic.values():
        count *=(value+1)

    return count-1