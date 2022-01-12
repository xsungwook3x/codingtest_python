import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    while scoville[0] < K:
        try:
            tmp=heapq.heappop(scoville)+heapq.heappop(scoville)*2
            heapq.heappush(scoville,tmp)
        except IndexError:
            return -1
            
        count+=1
        
    return count