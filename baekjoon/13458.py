n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

count=0

for i in range(n):
    tmp=a[i]-b
    count+=1
    if tmp >0:
        if tmp%c==0:
            count+=tmp//c
        else:
            count+=tmp//c+1

print(count)