a,b=map(int,input().split())

def dfs(a,b):

    stack=[]
    stack.append((a,1))

    min=100000

    while stack:
        n,i=stack.pop()
        if n <= b:
            if n==b:
                if min>i:
                    min=i

            else:
                stack.append((n*10+1,i+1))
                stack.append((n*2,i+1))

    return min

result=dfs(a,b)

if result ==100000:
    print(-1)
else:
    print(result)

