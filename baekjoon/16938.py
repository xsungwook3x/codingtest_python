from itertools import combinations

n,l,h,x=map(int,input().split())
nums=list(map(int,input().split()))

answer=0
for i in range(2,n+1):
    tmp=list(combinations(nums,i))
    for t in tmp:
        if l<=sum(t)<=h:
            if max(t)-min(t)>=x:
                answer+=1
print(answer)