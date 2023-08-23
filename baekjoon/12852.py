# from collections import deque
# import copy
#
# x= int(input())
#
# q=deque()
# q.append([x])
#
# while q:
#     a=q.popleft()
#     l=a[-1]
#
#     if l==1:
#         print(len(a)-1)
#         for i in a:
#             print(i,end=' ')
#         break
#
#     if l>0 and l%3==0:
#         b=copy.deepcopy(a)
#         b.append(l//3)
#
#         q.append(b)
#     if l>0 and l%2==0:
#         c=copy.deepcopy(a)
#         c.append(l//2)
#
#         q.append(c)
#     if l>0:
#         d = copy.deepcopy(a)
#         d.append(l-1)
#
#         q.append(d)

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, []] for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[n][0])
print(*reversed(dp[n][1]))