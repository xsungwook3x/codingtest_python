count = 1
while True:
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break

    day = 0
    day += (v // p) * l
    if v % p != 0:
        if v % p < l:
            day += v % p
        else:
            day += l

    print("Case {0}: {1}".format(count,day))
    count += 1
