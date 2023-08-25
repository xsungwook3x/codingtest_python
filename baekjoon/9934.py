n=int(input())
arr=list(map(int,input().split()))
tree=[[] for _ in range(n)]

def makeTree(arr,dept):
    if len(arr)==1:
        tree[dept].append(arr[0])
        return

    mid=len(arr)//2
    tree[dept].append(arr[mid])
    makeTree(arr[:mid],dept+1)
    makeTree(arr[mid+1:],dept+1)

makeTree(arr,0)
for i in range(len(tree)):
    for j in range(len(tree[i])):
        print(tree[i][j],end=' ')
    print()
