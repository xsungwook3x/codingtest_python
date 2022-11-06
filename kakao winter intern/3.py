
def solution(box):
    n=len(box)
    total=sum(box)
    avg=total//n
    if total%n!=0:
        avg+=1
    for i in range(n-1,0,-1):
        if box[i]>avg:
            x=(box[i]-avg)
            box[i]-=x
            box[i-1]+=x

    for i in range(0,n-1):
        if box[i]<avg:
            x=avg-box[i]
            box[i+1]-=x
            box[i]+=x


    return max(box)



print(solution([5, 15, 19]))

