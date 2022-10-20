lotto=''
while True:
    n=int(input())
    if n ==7:
        break
    if n==4:
        continue

    lotto+=str(n)

lotto=int(lotto)
if lotto%11==0:
    print("1st prize")
elif lotto%7==0:
    print("2nd prize")

else:
    print("No prize")