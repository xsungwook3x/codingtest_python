i=input()

str=list(i.split(' '));
basic=str[0]
del str[0]
for s in str:
    s=s.replace(",","").replace(";","")

    tmp=basic
    for i in range(len(s)-1,0,-1):
        if not s[i].isalpha():
            tmp+=s[i]

    tmp=tmp.replace("][","[]")
    tmp+=" "
    for i in range(len(s)):
        if s[i].isalpha():
            tmp+=s[i]
    tmp+=";"
    print(tmp)