n=int(input())
arr=list(map(int,input().split()))
max_v=0
def sol(s):
    global max_v

    if len(arr)==2:
        if s> max_v:
            max_v=s
        return
    else:
        for i in range(1,len(arr)-1):
            r=arr[i-1]*arr[i+1]
            tmp=arr[i]
            del arr[i]
            sol(s+r)
            arr.insert(i,tmp)

sol(0)
print(max_v)
