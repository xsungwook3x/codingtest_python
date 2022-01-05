def solution(priorities, location):
    answer = 0
    while len(priorities)>=0:
        max_n=max(priorities)

        tmp=priorities.pop(0)
        if max_n == tmp:
            answer+=1
            if location == 0: return answer
            else : location -=1



        else :
            priorities.append(tmp)
            if location <= 0:
                location = len(priorities)-1
            else :
                location-=1
