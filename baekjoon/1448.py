n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)

def findTri():
    for i in range(n-2):
        if nums[i]<nums[i+1]+nums[i+2]:
            return nums[i]+nums[i+1]+nums[i+2]

    return -1

print(findTri())
