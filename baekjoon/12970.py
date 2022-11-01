n,k=map(int,input().split())

alpha=['B']*n
def check(alpha):
    count=0
    for i in range(n-1):
        if alpha[i]=='A':
            for j in range(i+1,n):
                if alpha[j]=='B':
                    count+=1
    return count

for i in range(n):
    alpha[i]='A'
    if check(alpha)==k:
        answer=''.join(alpha)
        print(answer)
        exit(0)
    if check(alpha)>k:
        alpha[i]='B'

print(-1)

