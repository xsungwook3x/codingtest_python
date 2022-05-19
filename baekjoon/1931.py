n=int(input())

list=[]
for i in range(n):
    a,b=map(int,input().split())
    c=b-a
    list.append([a,b,c])

time=[]
time.append(list[0])

list.sort(key=lambda x:x[2])


for i in list:

    flag=True
    for t in time:
        if t[0]<=i[0]<t[1]:
            flag=False
            break;
        if t[0]<i[1]<=t[1]:
            flag=False
            break;

    if flag==True:
        time.append(i)

print(len(time))
print(time)



# 정답

n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)
