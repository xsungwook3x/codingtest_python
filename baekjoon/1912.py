n=int(input())
l=list(map(int, input().split()))

for i in range(1,n):
    l[i]=max(l[i-1]+l[i],l[i])

print(max(l))


# n = int(input())
# l = list(map(int, input().split()))
# dp = []
#
# for i in range(n):
#     tmp = []
#     for j in range(i, n):
#         tmp.append(sum(l[i:j + 1]))
#
#     dp.append(tmp)
#
# max_value = max(map(max, dp))
# print(max_value)
