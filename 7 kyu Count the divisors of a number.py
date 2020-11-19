#https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python

def divisors(n):
    count = 0
    for x in range(1, n + 1):
        if n % x == 0 :
            count += 1
    return count


def divisors(n):
    return sum(1 for x in range(1,n + 1) if n % x == 0)