n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))

dp=[0]*(max(a)+1)
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,max(a)+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]


for i in a:
    print(dp[i])