import sys
input = sys.stdin.readline

n,m=map(int,input().split())
k=min(n,m)

nums=[]
for _ in range(n):
    nums.append(list(input()))


def findsquare(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if nums[i][j]==nums[i][j+s-1]==nums[i+s-1][j]==nums[i+s-1][j+s-1]:
                return True

    return False

for c in range(k,0,-1):
    if findsquare(c):
        print(c**2)
        break