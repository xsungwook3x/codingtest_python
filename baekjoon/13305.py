n=int(input())
d=list(map(int,input().split()))
city=list(map(int,input().split()))

total=0
curr=city[0]
for i in range(n-1):
    curr=min(city[i],curr)
    total+=d[i]*curr

print(total)