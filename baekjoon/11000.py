import heapq

n=int(input())

q=[]
for i in range(n):
    s,e=map(int,input().split())
    q.append([s,e])

q.sort()
room=[]
heapq.heappush(room,q[0][1])

for i in range(1,n):
    if room[0]>q[i][0]:
        heapq.heappush(room,q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,q[i][1])

print(len(room))