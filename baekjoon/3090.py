import copy
n,t=map(int, input().split())

nums=list(int, input().split())

def max_dis():
    tmp=copy.deepcopy(nums)
    md=-1
    for i in range(1,n):
        md=max(md,abs(tmp[i-1]-tmp[i]))
    return md

def counter(x):
    tmp=copy.deepcopy(nums)
    cnt=0
    for i in range(1,n):
        if abs(tmp[i-1]-tmp[i])>x:
            cnt+=abs(tmp[i-1]-tmp[i])-x
