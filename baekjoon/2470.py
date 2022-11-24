n=int(input())
arr=list(map(int,input().split()))

arr.sort()
answer=2e+9+1
l,r=0,n-1
ele=[]
while l<r:
    l_e=arr[l]
    r_e=arr[r]

    if abs(l_e+r_e)<answer:
        answer=abs(l_e+r_e)
        ele=[l_e,r_e]

    if (l_e+r_e)<0:
        l+=1
    else:
        r-=1

print(ele[0],ele[1])