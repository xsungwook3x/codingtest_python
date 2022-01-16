import itertools
def primenumber(x):
    for i in range(2, x):
    	if x % i == 0:	
        	return False
    return True	
def exist(list ,tmp):
    for i in range(len(list)):
        if list[i] == tmp:
            return True
    return False

def solution(numbers):
    num=[]
    answer=[]
    for i in range(len(numbers)):
        num.append(numbers[i])
    
    for i in range(1,len(numbers)+1):
        result = list(itertools.permutations(num,i))
        
        for j in range(len(result)):
            tmp=int(("").join(result[j]))
            print(tmp)
            if tmp == 0 : continue
            if tmp == 1 : continue
            if exist(answer,tmp): continue
            if primenumber(tmp) : answer.append(tmp)
        
    return len(answer)