n=int(input())


def assemble(t):
    op, d, a, c=t
    answer=""
    if op[:3]=="ADD":
        if op[-1]=="C":
            answer+="00001"

        else:
            answer+="00000"

    elif op[:3]=="SUB":
        if op[-1]=="C":
            answer+="00011"

        else:
            answer+="00010"

    elif op[:3]=="MOV":
        if op[-1]=="C":
            answer+="00101"

        else:
            answer+="00100"

    elif op[:3]=="AND":
        if op[-1]=="C":
            answer+="00111"

        else:
            answer+="00110"

    elif op[:2]=="OR":
        if op[-1]=="C":
            answer+="01001"

        else:
            answer+="01000"

    elif op=="NOT":
        answer+="01010"

    elif op[:4]=="MULT":
        if op[-1]=="C":
            answer+="01101"

        else:
            answer+="01100"

    elif op[:5]=="LSFTL":
        if op[-1]=="C":
            answer+="01111"

        else:
            answer+="01110"

    elif op[:5]=="LSFTR":
        if op[-1]=="C":
            answer+="10001"

        else:
            answer+="10000"

    elif op[:5]=="ASFTR":
        if op[-1]=="C":
            answer+="10011"

        else:
            answer+="10010"

    elif op[:2]=="RL":
        if op[-1]=="C":
            answer+="10101"

        else:
            answer+="10100"

    elif op[:2]=="RR":
        if op[-1]=="C":
            answer+="10111"

        else:
            answer+="10110"


    answer+="0"
    answer+=bin(int(d))[2:].zfill(3)
    answer+=bin(int(a))[2:].zfill(3)
    if answer[4]=="1":
        answer+=bin(int(c))[2:].zfill(4)
    else:
        answer+=bin(int(c))[2:].zfill(3)+"0"


    return answer




for i in range(n):
    tmp=input().split()
    print(assemble(tmp))