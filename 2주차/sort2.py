def change_str(numbers):
    list=[]
    for i in range(len(numbers)):
        list.append(str(numbers[i]))
                    
    return list
                    
def solution(numbers):
    
    list=change_str(numbers)
    list.sort(key = lambda x: x*3,reverse=True)
    
    answer=str(int(''.join(list)))
                    
    return answer