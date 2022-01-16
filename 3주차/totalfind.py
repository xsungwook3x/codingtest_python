def solution(answers):
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    count1,count2,count3=0,0,0
    answer=[]
    
    for i in range(len(answers)):
        
        if answers[i] == num1[i%5] : count1+=1
        if answers[i] == num2[i%8] : count2+=1
        if answers[i] == num3[i%10] : count3+=1
    k=max(count1,count2,count3)
    
    if k == count1 :
        answer.append(1)
    if k == count2 :
        answer.append(2)
    if k == count3 :
        answer.append(3)

    return answer