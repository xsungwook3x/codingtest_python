def solution(participant, completion):
    answer=dict()
    hashCount=0
    for p in participant:
        answer[hash(p)]=p
        hashCount+=hash(p)

    for c in completion:
        hashCount-=hash(c)

    return answer[hashCount]