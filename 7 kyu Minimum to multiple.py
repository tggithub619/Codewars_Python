#https://www.codewars.com/kata/5e030f77cec18900322c535d/solutions/python/all/best_practice
def minimum(a, x):
    return min(a % x, -a % x)