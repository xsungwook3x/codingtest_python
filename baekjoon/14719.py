a,b=map(int,input().split())

l=list(map(int,input().split()))

left , right=0,b-1
leftMax=l[left]
rightMax=l[right]

answer=0

while left < right:

    leftMax=max(leftMax,l[left])
    rightMax=max(rightMax,l[right])

    if leftMax >= rightMax:
        answer += rightMax-l[right]
        right-=1
    if leftMax<rightMax:
        answer +=leftMax-l[left]
        left+=1

print(answer)


# h, w = map(int, input().split())
# world = list(map(int, input().split()))
#
# ans = 0
# for i in range(1, w - 1):
#     left_max = max(world[:i])
#     right_max = max(world[i+1:])
#
#     compare = min(left_max, right_max)
#
#     if world[i] < compare:
#         ans += compare - world[i]
#
# print(ans)