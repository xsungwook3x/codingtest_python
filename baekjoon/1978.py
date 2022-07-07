n=int(input())

nums=list(map(int,input().split()))

def find(a):
    if a==1:
        return False
    if a==2:
        return True

    for i in range(2,a):
        if a%i==0:
            return False

    return True

count=0
for i in range(n):
    if find(nums[i]):
        count+=1

print(count)