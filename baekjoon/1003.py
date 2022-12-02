n=int(input())
l=[]
for _ in range(n):
    l.append(int(input()))

dp=[[0,0] for _ in range(max(l)+1)]

dp[0]=[1,0]
if max(l)!=0:
    dp[1]=[0,1]
for i in range(2,max(l)+1):
    dp[i]=[dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]

for i in l:
    print(dp[i][0],end=' ')
    print(dp[i][1])