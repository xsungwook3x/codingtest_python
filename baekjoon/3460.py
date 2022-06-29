n = int(input())
for i in range(n):
    a=int(input())
    b = format(a, 'b')
    answer=[]
    b=b[::-1]
    for i in range(len(b)):
        if b[i]=="1":
            answer.append(i)
    for i in answer:
        print(i,end=' ')
    print()