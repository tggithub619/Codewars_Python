#https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4/solutions/python/me/best_practice

def least_larger(a, i):
    if a[i] == max(a):
        return -1
    return a.index(min([x for x in a if x > a[i]]))