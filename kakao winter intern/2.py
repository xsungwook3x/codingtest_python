import heapq

def solution(cost,x):
    n=len(cost)
    color=[]
    for i in range(n):
        heapq.heappush(color,[-i,cost[i]])

    answer=0

    while color:
        tmp=heapq.heappop(color)
        print(tmp)
        if x>=tmp[1]:
            answer+=2**(-tmp[0])
            x-=tmp[1]


    return answer

print(solution([3, 4, 1],8))