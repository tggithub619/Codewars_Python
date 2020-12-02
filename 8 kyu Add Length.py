#https://www.codewars.com/kata/559d2284b5bb6799e9000047/solutions/python/me/best_practice

def add_length(s):
    return [el+ " " +str(len(el)) for el in s.split()]