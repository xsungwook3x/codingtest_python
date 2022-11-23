n,d,k,c=map(int,input().split())

sushi=[]
for i in range(n):
    sushi.append(int(input()))

l,r=0,0
answer=0

while l!=n:
    r=l+k
    s=set()
    cou=True
    for i in range(l,r):
        i%=n
        s.add(sushi[i])
        if sushi[i]==c:
            cou=False
    cnt=len(s)
    if cou:
        cnt+=1
    answer=max(cnt,answer)
    l+=1

print(answer)

