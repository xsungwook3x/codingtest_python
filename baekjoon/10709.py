h,w=map(int,input().split())

visit=[[-1]*w for _ in range(h)]
arr=[]
for i in range(h):
    arr.append(list(input()))


for i in range(h):
    curr=-1
    for j in range(w):
        if arr[i][j]=='c':
            curr=0

        visit[i][j]=curr

        if curr>=0:
            curr+=1

for i in range(h):
    for j in range(w):
        print(visit[i][j], end=' ')
    print(end='\n')
