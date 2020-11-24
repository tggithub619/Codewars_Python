#https://www.codewars.com/kata/5d6f49d85e45290016bf4718/solutions/python/me/best_practice

def any_odd(x):
    n = bin(x)[2:].rjust(32,"0")
    for i, el in enumerate(n):
        if i%2 == 0 and el == "1":
            return True
    return False