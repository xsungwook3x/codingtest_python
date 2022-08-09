from collections import deque,defaultdict

n,k = map(int, input().split())

queue=deque()
queue.append([n,0])
dic=defaultdict(int)

visit=[False]*100001

while queue:
    cur,count=queue.popleft()
    visit[cur]=True

    if cur==k:
        dic[count]+=1
        continue

    if 0<=cur*2<=100000 and not visit[cur*2]:
        queue.append([cur*2,count+1])
    if 0 <= cur - 1 <= 100000 and not visit[cur - 1]:
        queue.append([cur-1,count+1])
    if 0 <= cur + 1 <= 100000 and not visit[cur + 1]:
        queue.append([cur+1,count+1])

for key in dic.keys():
    print(key)
    print(dic[key])
    break
