n=int(input())
num=[int(input()) for _ in range(n)]
num.sort(reverse=True)
answer=0

for i in range(1,n+1):
    a = num[i-1]-(i-1)
    if a>0:
        answer+=a

print(answer)