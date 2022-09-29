n=int(input())
hi=list(map(int,input().split()))
ai=list(map(int,input().split()))
I=list(range(n))

# 성장폭이 큰 것을 나중에 자르는것이 이득이다.
# 따라서 성장폭 큰순서대로 인덱스를 정렬
I.sort(key=lambda x:ai[x])

total=0
for i in range(len(I)):
    total+=hi[I[i]]+ai[I[i]]*i


print(total)