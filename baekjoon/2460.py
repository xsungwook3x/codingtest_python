people=0
max=0
for i in range(10):
    a, b= map(int, input().split())
    people-=a
    people+=b
    if max<people:
        max=people


print(max)
