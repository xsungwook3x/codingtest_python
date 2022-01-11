def list_cut(array,i,j):
    list=[]
    for k in range(i,j):
        list.append(array[k])
    return list

def solution(array, commands):
    answer=[]

    for a in range(len(commands)):
        list=list_cut(array,commands[a][0]-1,commands[a][1]);
        list.sort()
        answer.append(list[commands[a][2]-1])


    return answer