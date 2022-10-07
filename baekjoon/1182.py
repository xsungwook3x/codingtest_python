import itertools
n,s=map(int,input().split())
nums=list(map(int,input().split()))

count=0
for i in range(1,n+1):
    per=itertools.combinations(nums,i)

    for p in per:
        if sum(p)==s:
            count+=1


print(count)

