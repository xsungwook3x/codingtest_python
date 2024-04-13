import sys
input = sys.stdin.readline

n = int(input())

text=[]
for _ in range(n):
    text.append(list(input()))
cmd=text[0]

for i in range(1,n):
    for j in range(len(text[i])):
        if text[i][j]!=cmd[j]:
            cmd[j]='?'

print(''.join(cmd))
