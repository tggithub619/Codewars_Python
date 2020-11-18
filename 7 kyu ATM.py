#https://www.codewars.com/kata/5635e7cb49adc7b54500001c/solutions/python/all/best_practice

def solve(n):
    if n % 10 != 0:
        return -1
    count = 0
    lst = [500, 200, 100, 50, 20, 10]
    i = 0
    while n > 0:
        count +=  n // lst[i]
        n = n % lst[i]
        i += 1
    return count


def solve(n):
    if n % 10 != 0:
        return -1
    count = 0
    while n > 0:
        if n >= 500:
            count += 1
            n -= 500
        elif n >=  200:
            count += 1
            n -= 200
        elif n >=  100:
            count += 1
            n -= 100
        elif n >=  50:
            count += 1
            n -= 50
        elif n >=  20:
            count += 1
            n -= 20
        elif n >= 10:
            count += 1
            n -= 10
    return count


def solve(n):
    if n%10: return -1
    c, billet = 0, iter((500,200,100,50,20,10))
    while n:
        x, r = divmod(n, next(billet))
        c, n = c+x, r
    return c