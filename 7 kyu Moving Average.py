#https://www.codewars.com/kata/5c745b30f6216a301dc4dda5/solutions/python/me/best_practice

def moving_average(v,n):
    if n == 0 or n > len(v):
        return None
    return [sum(v[i:i+n])/n for i in range(len(v)-n+1)]


def moving_average(v, n):
    if n == 0 or n > len(v):
        return None
    a = []
    for i in range(len(v) - n + 1):
        a.append(sum(v[i:i + n]) / n)
    return a

def moving_average(a, n):
    if 0 < n <= len(a): return [sum(a[i:i+n]) / n for i in range(len(a) - n + 1)]