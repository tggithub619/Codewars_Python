#https://www.codewars.com/kata/5572f7c346eb58ae9c000047/solutions/python/me/best_practice

def pattern(n):
    return '\n'.join(str(i) * i for i in xrange(1, n + 1))

def pattern(n):
    lst = []
    if n < 1:
        return ""
    for i in range(1, n + 1):
        lst.append(str(i) * i)
        if i != n:
            lst.append("\n")
    return "".join(lst)