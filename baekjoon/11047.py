n,m=map(int,input().split())

coins=[]

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

num=0
for coin in coins:
    num+=m//coin
    m%=coin

print(num)