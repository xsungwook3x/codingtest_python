from collections import deque
import copy
t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    print(l)
    curr=s
    answer=0
    for j in range(n):
        min_n=5000
        min_i=-1
        for k in range(n):
            if l[k]==-1:
                continue

            if abs(curr-l[k])<min_n:
                min_n=abs(curr-l[k])
                min_i=k
        answer+=abs(curr-l[min_i])

        curr=l[min_i]
        l[min_i]=-1

    print(answer)


