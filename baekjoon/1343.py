a=input()

word=[]
flag='.'
tmp=''
for i in a:

    if i==flag:
        tmp+=flag
    else:
        if len(tmp)!=0:
            word.append(tmp)
        tmp=''
        flag=i
        tmp+=flag

word.append(tmp)

answer=''
for w in word:
    if '.' in w:
        answer+=w
    else:
        if len(w)%2!=0:
            answer=-1
            break
        else:
            a=len(w)//4
            answer+='AAAA'*a
            b=len(w)%4
            b=b//2
            answer+='BB'*b

print(answer)