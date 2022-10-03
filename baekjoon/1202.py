import heapq

n,k=map(int,input().split())
j=[]
bags=[]
for i in range(n):
    heapq.heappush(j,list(map(int,input().split())))

for i in range(k):
    bags.append(int(input()))

bags.sort()

answer=0
tmp=[]
for bag in bags:
    while j and j[0][0]<=bag:
        heapq.heappush(tmp,-heapq.heappop(j)[1])

    if tmp:
        answer-=heapq.heappop(tmp)

    elif not j:
        break
print(answer)

