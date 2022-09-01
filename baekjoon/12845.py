n=int(input())
l=list(map(int,input().split()))


l.sort(reverse=True)
count=0
tmp=l[0]
for i in range(1,n):
    count+=tmp+l[i]

if n==1:
    count+=l[0]
print(count)