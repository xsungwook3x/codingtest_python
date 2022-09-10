t=int(input())
dp=[0]*101
dp[1]=1
dp[2]=1

def p(n):
    if n<=2:
        return dp[n]
    for i in range(3,n+1):
        if dp[i]==0:
            dp[i]=dp[i-2]+dp[i-3]

    return dp[n]

for i in range(t):
    n=int(input());
    print(p(n))