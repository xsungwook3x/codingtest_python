

s=list(input())
end=list(input())

while len(s)!=len(end):
    if end[-1]=='A':
        end.pop()
    elif end[-1]=='B':
        end.pop()
        end=end[::-1]

if s==end:
    print(1)
else:
    print(0)

