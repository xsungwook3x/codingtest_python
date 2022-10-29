from itertools import combinations
dp=[0]*200001
dp[0]=1
n=int(input())
data=list(map(int,input().split()))

for i in range(1,n+1):
    for j in combinations(data,i):
        dp[sum(j)]=1
print(dp.index(0))

