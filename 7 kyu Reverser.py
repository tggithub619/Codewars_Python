#https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/solutions/python/me/best_practice

def reverse(n):
    res = 0
    while n:
        res = res * 10 + n % 10
        n = n // 10
    return res