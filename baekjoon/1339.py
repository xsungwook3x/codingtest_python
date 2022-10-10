n=int(input())

alpha=[]
dic={}
nums=[]

for i in range(n):
    alpha.append(input())

for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in dic:
            dic[alpha[i][j]]+=10**(len(alpha[i])-j-1)
        else:
            dic[alpha[i][j]]=10**(len(alpha[i])-j-1)

for value in dic.values():
    nums.append(value)

nums.sort(reverse=True)


answer=0
count=9
for i in nums:
    answer+=count*i
    count-=1

print(answer)
