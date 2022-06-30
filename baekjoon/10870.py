a=int(input())

def p(a):
    if a==0:
        return 0
    if a==1:
        return 1

    return p(a-1)+p(a-2)

print(p(a))