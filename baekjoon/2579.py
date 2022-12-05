n=int(input())
num=[0]*301
dp=[0]*301
for i in range(n):
    num[i]=int(input())
dp[0]=num[0]
dp[1]=num[0]+num[1]
dp[2]=max(num[0]+num[2],num[1]+num[2])
for i in range(3,n):
    dp[i]=max(num[i]+dp[i-3]+num[i-1],num[i]+dp[i-2])

print(dp[n-1])