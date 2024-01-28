n=int(input())

num=[]
for _ in range(n):
    num.append(int(input()))

num.sort()
answer=[]
for k in num:
    answer.append(k*n)
    n-=1
print(max(answer))