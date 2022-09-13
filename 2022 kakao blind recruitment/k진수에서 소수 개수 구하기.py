import math


def convert(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def isPrime(q):
    if q == "":
        return False

    tmp = int(q)
    if tmp == 1:
        return False
    elif tmp == 2:
        return True

    for i in range(2, int(math.sqrt(tmp)) + 1):
        if tmp % i == 0:
            return False
    return True


def solution(n, k):
    converted = convert(n, k)

    l = list(converted.split('0'))
    count = 0
    for i in l:
        if isPrime(i):
            count += 1

    return count