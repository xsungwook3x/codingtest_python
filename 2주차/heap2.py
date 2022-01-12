import heapq
def solution(jobs):
    answer=0
    count=0
    time=0
    start=-1
    wait=[]
    
    while count < len(jobs):
        
        for i in jobs:
            if start < i[0] <= time:
                heapq.heappush(wait,[i[1],i[0]])
        
        if len(wait) > 0 :
            tmp=heapq.heappop(wait)
            start=time
            time +=tmp[0]
            answer += time - tmp[1] 
            count +=1
        else:
            time +=1
            
    a,b=divmod(answer,len(jobs))
    return a