l=[]
for i in range(9):
    a=int(input())
    l.append(a)

tmp1,tmp2=0,0
for i in range(9):
    for j in range(9):
        if sum(l)-(l[i]+l[j])==100:
            tmp1=l[i]
            tmp2=l[j]
l.remove(tmp1)
l.remove(tmp2)
l.sort()
for i in l:
    print(i)