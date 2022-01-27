from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    weight = 0
    cnt = 0
    while people:
        weight = people.pop()
        if people and weight+people[0]<=limit:
            people.popleft()
        weight = 0
        cnt+=1

    answer = cnt
    return answer