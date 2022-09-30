n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))

nums.sort()

max=-1
for i in range(1,n-1):
    avg_min=nums[i]+nums[0]+nums[i+1]
    avg_max=nums[i-1]+nums[i]+nums[n-1]
    if abs(avg_min-nums[i]*3)>max:
        max=abs(avg_min-nums[i]*3)

    if abs(avg_max-nums[i]*3)>max:
        max=abs(avg_max-nums[i]*3)


print(max)

