a,b =map(int,input().split())

def gcd(a,b):
    list_a=[]
    for i in range(1,a+1):
        if a%i==0:
            list_a.append(i)

    list_b=[]
    for j in range(1,b+1):
        if b%j==0:
            list_b.append(j)
    max=0
    for i in list_a:
        if i in list_b and max<i:
            max=i

    return max

def lcm(a,b):
    if a < b:
        tmp=b
        b=a
        a=tmp

    for i in range(1,b):
        if (a*i)%b==0:
            return a*i

    return a*b

print(gcd(a,b))
print(lcm(a,b))