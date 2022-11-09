n = int(input())
s = str(n)
count=0
while True:
    tmp = 0
    for j in s:
        tmp += int(j)

    s = s[1] + str(tmp)[-1]


    count+=1
    if int(s) == n:
        break
print(count)



