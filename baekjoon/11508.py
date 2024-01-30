n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

c=n//3
nums.sort(reverse=True)
result=0
for i in range(2,n,3):
    result+=nums[i]
print(sum(nums)-result)