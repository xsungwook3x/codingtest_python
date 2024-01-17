words=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b_words=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=input()

answer=''
for i in a:
    if i.isupper():
        tmp=ord(i)-ord('A')
        tmp=(tmp+13)%26
        answer+=b_words[tmp]
    elif i.islower():
        tmp=ord(i)-ord('a')
        tmp=(tmp+13)%26
        answer+=words[tmp]
    else:
        answer+=i

print(answer)
