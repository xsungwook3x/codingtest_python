n=int(input())
m=list(map(int,input().split()))
total=int(input())

def findBudget(bound):
    s=0
    for i in m:
        s+=min(i,bound)
    return s

if total>=sum(m):
    print(max(m))

else:
    l = 0
    r = max(m)
    best_bound = -1

    while l <= r:
        mid = (l + r) // 2

        if findBudget(mid) <= total:  # 예산보다 작으면 답이될여지가있기에 mid를저장
            best_bound = mid
            l = mid + 1  # 예산보다 작기에 mid의 오른쪽을 살펴본다
        else:
            r = mid - 1  # 예산보다 크기때문에 저장할 가치없고 살펴본 mid 왼쪽을 살펴본다.

    print(best_bound)




