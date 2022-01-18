def solution(number):
    if 0<=number<100:
        return number
    else:
        count=99
        for i in range(100,number+1):
            if i ==1000:
                break
            a=int(i/100)
            b=int((i%100)/10)
            c=int(i%10)
            if (a-b)==(b-c) :
                count+=1

        return count

number=int(input())

print(solution(number))