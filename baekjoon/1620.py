import sys

input = sys.stdin.readline

n,m=map(int,input().split())

dogam_num={}
dogam_name={}
for i in range(1,n+1):
    name=input().rstrip()
    dogam_num[i]=name
    dogam_name[name]=i

for i in range(m):
    q=input().rstrip()
    if q.isdigit():
        print(dogam_num[int(q)])
    else:
        print(dogam_name[q])