n=int(input())

tmp=[]
for _ in range(n):
    tmp.append(list(map(int,input().split())))

for i in tmp:
    rank=1
    for j in tmp:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=' ')