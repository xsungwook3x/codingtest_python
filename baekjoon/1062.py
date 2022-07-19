n,k = map(int,input().split())
words=[]
for i in range(n):
    words.append(input())

def solution(idx,count,learn,words):
    global result

    if count == k-5: # 글자 개수를 채웠으면 되는 단어 비교 시작

        tmp=0
        for word in words: # 단어들 비교
            isExist=True
            for w in word:
                if not learn[ord(w)-ord('a')]:
                    isExist=False
                    break
            if isExist: # 할 수 있으면 개수에 포함
                tmp+=1
        result=max(tmp,result)
        return

    for i in range(idx,26): # 하나씩 넣어가면서 dfs 구현
        if not learn[i]:
            learn[i]=True
            solution(i,count+1,learn,words) # 다음 단어 찾기 count는 깊이 이다.
            learn[i]=False
            # 풀어줘야지 다른 것도 지정할수있어서 풀어줌

if k < 5: # a n t i c 다섯개는 필수적으로 알아야하기때문에
    print(0)
elif k==26:
    print(n)
else:
    learn = [0] * 26
    result = 0
    for c in ('a', 'c', 'i', 'n', 't'):
        learn[ord(c) - ord('a')] = True

    solution(0,0,learn,words)
    print(result)
