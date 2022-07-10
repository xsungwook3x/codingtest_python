n=int(input())
m=int(input())

nums=[]

def find(a):
    if a == 1: return False
    if a==2: return True

    for i in range(2,a):
        if a%i==0:
            return False

    return True

for i in range(n,m+1):
    if find(i):
        nums.append(i)

if len(nums)==0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))