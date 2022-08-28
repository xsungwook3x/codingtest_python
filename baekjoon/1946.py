t=int(input())

for i in range(t):
    n=int(input())

    l=[]
    for j in range(n):
        a,b=map(int,input().split())
        l.append([a,b])

    l.sort()

    count=1
    low=l[0][1]

    for k in range(1,n):
        if l[k][1]<low:
            low=l[k][1]
            count+=1

    print(count)