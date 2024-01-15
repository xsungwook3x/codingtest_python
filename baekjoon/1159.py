n=int(input())

dic={}
for i in range(n):
    a=input()[0]
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1

sorted(dic.keys())
answer=""
for k,v in dic.items():
    if v >= 5:
        answer += k

if answer:
    print(answer)
else:
    print("PREDAJA")

