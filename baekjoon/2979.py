a,b,c=map(int,input().split())
time=[0 for _ in range(101)]
for _ in range(3):
    s,e=map(int,input().split())
    for i in range(s,e):
        time[i]+=1
answer=0
for i in range(len(time)):
    if time[i]>=3:
        answer+=time[i]*c
    elif time[i]>=2:
        answer+=time[i]*b
    elif time[i]>=1:
        answer+=time[i]*a
print(answer)


