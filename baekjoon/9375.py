n=int(input())
for _ in range(n):
    t=int(input())
    dic={}
    for i in range(t):
        a,b=input().split()
        if b not in dic:
            dic[b]=1
        else:
            dic[b]+=1
    answer=1
    for k,v in dic.items():
        answer*=(v+1)
    print(answer-1)