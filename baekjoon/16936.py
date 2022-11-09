n=int(input())
l=list(map(int,input().split()))

a=[]
for i in range(n):
    cnt=0
    num=l[i]
    while True:
        if num%3==0:
            cnt+=1
            num=num//3
        else:
            break
    a.append([cnt,l[i]])

a.sort(key=lambda x:(-x[0],x[1]))
for j in a:
    print(j[1],end=' ')




