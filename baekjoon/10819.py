import itertools

n=int(input())
l=list(map(int,input().split()))

per=itertools.permutations(l,n)

m=0
for p in per:
    tmp=0
    for i in range(1,n):
        tmp+=abs(p[i]-p[i-1])

    if m<tmp:
        m=tmp

print(m)

