import heapq

n=int(input())
h=[]
for i in range(n):
    heapq.heappush(h,int(input()))

if len(h)==1:
    print(0)
else:
    total=0
    while len(h)>1:
        tmp1=heapq.heappop(h)
        tmp2=heapq.heappop(h)
        total+=tmp1+tmp2
        heapq.heappush(h,tmp1+tmp2)

    print(total)
