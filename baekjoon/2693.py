n=int(input())
for i in range(n):
    s=list(map(int,input().split()))
    s.sort()
    print(s[-3])