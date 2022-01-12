import heapq

def solution(operations):
    h=[]
    for i in operations:
        command,n=i.split()
        
        if command =="I":
            heapq.heappush(h, int(n))
        else :
            if h :
                if int(n)==1 :
                    heapq._heapify_max(h)
                    heapq._heappop_max(h)
                    heapq.heapify(h)
                else :
                    heapq.heappop(h)
                
    if h:
        heapq._heapify_max(h)
        a=heapq._heappop_max(h)
        heapq.heapify(h)
        b=heapq.heappop(h)
        return [a, b]
    else:
        return [0,0]


import heapq

def solution(operations):
    h=[]
    for i in operations:
        command,n=i.split()
        
        if command =="I":
            heapq.heappush(h, int(n))
        else :
            if h :
                if int(n)==1 :
                    h.pop()
                else :
                    heapq.heappop(h)
                
    if h:
        h.sort()
        return [h[-1], h[0]]
    else:
        return [0,0]