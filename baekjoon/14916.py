
n=int(input())

answer=-1
a=n//5
for i in range(a,-1,-1):

    if (n-5*i)%2==0:
        answer=i+(n-5*i)//2
        break

print(answer)