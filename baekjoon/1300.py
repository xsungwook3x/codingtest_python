n=int(input())
k=int(input())

def counter(x):
    small=0
    big=0
    for i in range(1,n+1):
        # i 번째 행에서 x 보다 작은 수
        small+=min(n,(x-1)//i)
        # i 번째 행에서 x 보다 큰수
        big+=n-min(n,x//i)

    return (small,big)

number=-1
left=1
right=min(n*n,int(1e9))
total=n*n

while left <= right:
    mid=(left+right)//2

    small,big=counter(mid)

    if small > k-1:
        right=mid-1
    if big > total-k:
        left=mid+1


    if small<=k-1 and big <=total-k:
        number = mid
        break

print(number)

